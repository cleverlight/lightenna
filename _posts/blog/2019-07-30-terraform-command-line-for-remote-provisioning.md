---
layout: single
title: Get started with remote provisioning using Terraform
description: Often local machines or firewalls make it impossible to run Terraform locally, but remote provisioning offers a convenient secure alternative
tags: front tech devops remprov
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## Restricted local desktop
Tools like Terraform, Packer, Ansible and Puppet offer great ways to automate web operations, but even though they're freely available it can be hard to get them running.  Local restrictions make the act of downloading, installing and executing hard; perhaps it's an overzealous firewall that won't allow external SSH access on port 22, content filtering that blocks the download of zips or a Windows group policy that restricts the execution of unsanctioned apps.

## Complex dependencies
When you factor in some of the command line tools that facilitate Cloud access (AWS CLI, Azure CLI) and their dependencies (Ruby, Python, PIP), the starting block looks even further away.

## Remprov
Thankfully there is a free alternative.  These tools run best in well set-up environments.  Their provisioning and configuration management activities are often Cloud-based, so they themselves can be run in the cloud.  Remote provisioning (or remprov) rather than local provisioning, makes that easier.

## AWS Marketplace
We provide a free Amazon Machine Image (AMI) in the AWS Marketplace that has all these tools, their dependencies pre-configured.  It makes it quick and easy to 

It can be provisioned using the AWS Web console.

<!--- @todo insert Web console screenshot -->

## Keys to the city
When provisioning that machine, AWS will give you the option to create and download SSH keys to access it.  By storing and loading these keys into an SSH agent (like ssh-agent, Pageant) or your SSH client (like Putty or MobaXterm) directly, you can connect to 

> Store SSH keys with care, because these privileged credentials allow access to your new machine.

## Next steps
Once you've moved beyond experimentation and into production, it's good practice to generate your own SSH keys locally with an additional passphrase.

## Access
Because SSH is sometimes blocked on port 22, `workstream-remprov` also runs SSH on port 443.  That means you can connect to your new remprov machine using an alternative port:
```
ssh -A -p 443 centos@<public-ip-address>
```
The `-A` flag passes your loaded SSH keys

<!--- @todo insert Web console screenshot -->

## Get your team coding
If you'd like to help your Operations team move to infrastructure-as-code, please [get in touch](/contact) to find out how Lightenna consulting could accelerate your Cloud journey.
