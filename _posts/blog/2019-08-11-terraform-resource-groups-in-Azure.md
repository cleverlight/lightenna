---
layout: single
title: Create resource groups in Microsoft Azure using Terraform
description: Resource groups hold everything together in Azure, like virtual containers for the resources we provision.
tags: tech devops remprov
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## Creating resources
Now that we've got a Terraform command-line and given it the credentials it needs to provision resources in our Cloud, we can start provisioning.

## Keeping it unique
When running these kind of tutorials, I find it helpful to keep all the resources unique.  That can either be done by appending a unique name, or using a short random string.

This resource creates a random string, which can be accessed using `${random_string.unique_key.result}`.
```
resource "random_string" "unique_key" {
  length = 8
  special = false
}
```

We only want to use this random_string if the user hasn't passed a variable, either using the `-var` command line option, a TF_VAR_ environment variable or .tfvars.  We can detect that based on the value and derive a local variable:
```
locals {
  # use a unique ID for all resources based on a random string unless one is specified
  unique_append = "${ var.unique_id == "" ? "-${random_string.unique_key.result}" : "-${var.unique_id}"}"
}
```

## Terraform resource group
```
resource "azurerm_resource_group" "rg" {
  name     = "rg${local.unique_append}"
  location = "${var.region}"
}
```

## Filtering in the console
By selecting a unique name, we can easily filter the Azure web console 'Resource' view to show only those resources.

<!--- @todo insert console screenshot -->

## Open-source
All the code for these tutorials is available as part of [DevOps-Workstream](https://github.com/lightenna/devops-workstream).  The segments from this tutorial specifically make up `terraform/tutorial/03-azure-resource-group-with-unique-default` [here on GitHub](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/03-azure-resource-group-with-unique-default).

## Get your team coding
If you'd like to help your Operations team move to infrastructure-as-code, please [get in touch](/contact) to find out how Lightenna consulting could accelerate your Cloud journey.
