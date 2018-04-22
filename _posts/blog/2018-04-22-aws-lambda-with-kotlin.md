---
layout: single
title: Spinning up AWS Lambda functions (Part 1)
description: Serverless infrastructure holds great promise but building something fast that runs fast requires planning
tags: devops front
header:
    overlay_image: /assets/images/spinning_clay_4998_1920x.jpg
---

This week I did a talk for SkyBet at the JVM Thing.  It was [a great night](https://www.meetup.com/Leeds-JVMThing/events/248916472/) and brilliant to see such a broad range of topics covered.

The basis of it was a live demo.  This Terraform module spins up a Lambda function behind an API gateway to store credit card details in a DynamoDB.

```
# add a Lambda function to field HTTP requests
module "lambda" {
  source = "./lambda"
  aws_region = "${var.aws_region}"
}

# create a static site in S3
module "static" {
  source = "./static"
  site_bucket_name = "<bucket name>"
  aws_region = "${var.aws_region}"
  post_target = "${module.lambda.kardapi_gateway_deployment_invoke_url}/card/add"
}
output "static_url" {
  value = "${module.static.site_url}"
}
```

It then creates a static website in an S3-bucket to post card details to the Kotlin handler. 

```
# create bucket
resource "aws_s3_bucket" "site_static" {
  bucket = "${var.site_bucket_name}"
  acl = "public-read"

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["PUT","POST"]
    allowed_origins = ["*"]
    expose_headers = ["ETag"]
    max_age_seconds = 3000
  }
  policy = <<EOF
{
  "Id": "bucket_policy_site_static",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "bucket_policy_site_static_main",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::${var.site_bucket_name}/*",
      "Principal": "*"
    }
  ]
}
EOF
  website {
      index_document = "index.html"
      error_document = "error.html"
  }
  tags {
  }
  force_destroy = true
}
```

For security reasons and to emphasise this is a _proof-of-concept_, it randomly generates the 'card' numbers so that no real credit card information gets stored.

```
// use JS to make up card details
function makeRandom(id, min, max, format) {
    var output = '';
    var separator = '-';
    // split format up into XX blocks
    var chunks = format.split(separator);
    // loop through blocks and substitute
    for (var i=0 ; i<chunks.length ; ++i) {
        // 2nd, 3rd, nth chunk is preceded by a separator
        if (i !== 0) {
            output += separator;
        }
        var chunk = chunks[i];
        // create a random number and pad to be the correct length
        var chnum = pad(Math.floor((Math.random()*(max - min)) + min), chunk.length);
        // append number to output
        output += '' + chnum;
    }
    // apply to field
    $(id).val(output);
    return output;
}
function pad(n, width, z) {
    z = z || '0';
    n = n + '';
    return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}
makeRandom('input[name=number]', 0, 9999, 'XXXX-XXXX-XXXX-XXXX');
makeRandom('input[name=expirymonth]', 01, 12, 'XX');
makeRandom('input[name=expiryyear]', 19, 26, 'XX');
makeRandom('input[name=cvv]', 0, 999, 'XXX');
```

Terraform does a lovely job on the templating, which means we can dynamically insert the handler's (API gateway) URL into the form's HTML.

```
<form name="addcard" action="${post_target}" method="post">
    <p>Name: <input type="text" name="name" value="" /></p>
    <p>Card number: <input class="readonly" type="text" name="number" value="" readonly="readonly" /></p>
    <p>Expiry: <input class="readonly" type="text" name="expirymonth" value="" readonly="readonly" /> / <input class="readonly" type="text" name="expiryyear" value="" readonly="readonly" /></p>
    <p>CVV: <input class="readonly" type="text" name="cvv" value="" readonly="readonly" /></p>
    <input type="submit" name="submit" value="Store" />
</form>
```

The [source code is available](https://github.com/skybet/terraform_lambda_kotlin_example) open-source thanks to SkyBet's progressive attitude towards proof-of-concept work - really enjoying working with [the Nexus team](https://www.linkedin.com/in/victoriahowling/) there.  The infrastructure-as-code is based on Lightenna's [Workstream](https://github.com/lightenna/devops-workstream) examples so can be spun-up with a single `terragrunt apply` command.  Whether you're a pro-coder or just getting started, check it out and let me know how you get on.
