---
layout: single
title: Storing Terraform state in S3
description: Terraform is a great solo tool but, when you start working together as a team, keep the tfstate files in the Cloud (S3) 
tags: front tech devops techupdate terraform
toc: true
header:
    overlay_image: /assets/images/techupdate_25318_1920x.jpg
    small_image: /assets/images/techupdate_25318_640x.jpg
---

## Terraform state in the Cloud
Terraform provisions cloud resources and keeps a record of the work it's done.  That record is held in the terraform.tfstate file.

Having those files locally makes it difficult to scale up from a single DevOps engineer working in isolation to a team of engineers collaborating.

## Set up the S3 bucket
The solution is to store it in AWS S3 with a lock maintained in AWS DynamoDB.  Here's `setup.tf`:

```
# terraform state file setup
# create an S3 bucket to store the state file in
resource "aws_s3_bucket" "terraform-state-storage-s3" {
  bucket = "my-terraform-state-s3"
  region = "eu-west-2"

  versioning {
    # enable with caution, makes deleting S3 buckets tricky
    enabled = false
  }

  lifecycle {
    prevent_destroy = true
  }

  tags {
    name = "S3 Remote Terraform State Store"
    proj = "example-iac"
    env = "prod"
  }
}

# create a DynamoDB table for locking the state file
resource "aws_dynamodb_table" "dynamodb-terraform-state-lock" {
  name = "example-iac-terraform-state-lock-dynamo"
  hash_key = "LockID"
  read_capacity = 20
  write_capacity = 20

  attribute {
    name = "LockID"
    type = "S"
  }

  tags {
    name = "DynamoDB Terraform State Lock Table"
    proj = "example-iac"
    env = "prod"
  }
}
```

## Bootstrapping problem
If you skip ahead and simply copy all the code from this tutorial (including the `backend` bit below) then do one big run with a `terraform init && terraform apply`, you'll get this error:
```
[lightenn@do7 aws-background {master}]$ terraform apply
Error loading state: NoSuchBucket: The specified bucket does not exist
        status code: 404, request id: 716AE642035C23D4, host id: LR4R+2PWWXe217qGThkw9/c4FcNDxAjan0ogipubvHl2f5e+gFb/otXRx5tFjjHWx4nENt5iAGw=
[lightenn@do7 aws-background {master}]$ terraform init

Initializing the backend...
Error loading state: NoSuchBucket: The specified bucket does not exist
        status code: 404, request id: 542A0B8F18D21884, host id: glZaVv4mnpq2t3lo7toVrSHxsCCBqykk7f4Wp6zhu8GxeTZgsfsJdGd+dykNH0TexNVYosOgO78=
```

We need to create the S3 bucket and DynamoDB table before relying on them.

`terraform init` then `terraform apply` to create the resources.

That first Terraform run creates state itself and it's stored locally.  Now we want to transfer that state to the Cloud.

## Start using S3 bucket for storing state
Create another file `main.tf` in the `terraform-s3` module:
```
provider "aws" {
  region = "eu-west-2"
}

# store tfstate in s3 and locking information in DynamoDB
terraform {
  backend "s3" {
    encrypt = true
    # cannot contain interpolations
    # bucket = "${aws_s3_bucket.terraform-state-storage-s3.bucket}"
    bucket = "my-terraform-state-s3"
    # region = "${aws_s3_bucket.terraform-state-storage-s3.region}"
    region = "eu-west-2"
    # dynamodb_table = "example-iac-terraform-state-lock-dynamo"
    key = "terraform-state/terraform.tfstate"
  }
}
```

Note that you can't use interpolations `"${}"` otherwise you'll get an error like this:

```
Failed to load backend: Error loading backend config: 1 error(s) occurred:

* terraform.backend: configuration cannot contain interpolations
```

Also note that the DynamoDB line is commented.  You might ask why.  The problem is a race condition.
First of all we need to get Terraform storing its state in the Cloud (S3 bucket), then locking it.

So again `terraform init`, but this time it asks us what we want to do with our local state.

```
[lightenn@do7 terraform-s3 {master}]$ terraform init

Initializing the backend...
Do you want to copy state from "local" to "s3"?
  Pre-existing state was found in "local" while migrating to "s3". No existing
  state was found in "s3". Do you want to copy the state from "local" to
  "s3"? Enter "yes" to copy and "no" to start with an empty state.

  Enter a value: yes
```

Answer `yes` because that transfers the local state, which includes information about the S3 bucket and DynamoDB table that we've created, to the Cloud.

Do a `terraform apply` to check everything is still working smoothly.

## Enable locking
Once that's sorted we can enable locking by uncommenting the DynamoDB table reference:

```
    region = "eu-west-2"
    dynamodb_table = "example-iac-terraform-state-lock-dynamo"
    key = "terraform-state/terraform.tfstate"
```

Again `terraform init` and Terraform detects the change then prompt us to confirm what we want to do:

```
[lightenn@do7 terraform-s3 {master}]$ terraform init

Initializing the backend...
Backend configuration changed!

Terraform has detected that the configuration specified for the backend
has changed. Terraform will now reconfigure for this backend. If you didn't
intend to reconfigure your backend please undo any changes to the "backend"
section in your Terraform configuration.


Do you want to copy the state from "s3"?
  Would you like to copy the state from your prior backend "s3" to the
  newly configured "s3" backend? If you're reconfiguring the same backend,
  answering "yes" or "no" shouldn't make a difference. Please answer exactly
  "yes" or "no".

  Enter a value: yes
```

Answer `yes` again because the state we've built up to this point is important to avoid the bootstrapping problem I mentioned earlier.

Finally `terraform apply` and we've got a complete working manifest with state stored in the Cloud.