---
layout: single
title: Transferring Terraform state in S3 over to another project
description: Terraform state files in S3 are the way forward, but when you need to split a project, managing those state files requires care
tags: tech devops techupdate terraform
toc: true
header:
    overlay_image: /assets/images/techupdate_25318_1920x.jpg
    small_image: /assets/images/techupdate_25318_640x.jpg
---

## Process
The process is relatively simple but I couldn't find much supporting documentation, so it's outlined here:

1. use [terraform state mv](https://www.terraform.io/docs/commands/state/mv.html) command to export state from previous module into transfer file
1. rename transfer.tfstate to terraform.tfstate and move to new module
1. set up manifests to point at s3 backend
1. `terraform init -reconfigure`
1. prompts to transfer state from <randomly named local file>, yes
1. check S3, looks like it's there
1. terraform apply confirms that the resources are there
