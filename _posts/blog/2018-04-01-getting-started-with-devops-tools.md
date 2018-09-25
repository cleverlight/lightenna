---
layout: single
title: Getting Started in the DevOps space 
description: The Development-Operations world is a wash with some fantastic tools, but sometimes getting started can be too great an impediment to realise the 'DevOps' efficiency promise.
tags: devops front
header:
  overlay_image: /assets/images/explosive_start_02329_1920x.jpg
  small_image: /assets/images/explosive_start_02329_640x.jpg
---

Starting out in anything can be rough.  While the prospect of having a helpful colleague or trainer sit down with you to walk you through it is wonderful, it and they aren't always available.

This post is designed to help you get started using DevOps tools like Terraform, Puppet or Docker.
Even if you just want to familiarise yourself with the toolset because you manage people who use it, I hope you'll find this an accessible primer.
Depending on its popularity, there may follow more in the series.

### The Examples Repo
You'll need some source code.  You could gather it together yourself because the Internet is full of helpful documentation and primers, but I've coded up a set of examples to help accelerate the learning curve.  All the examples are published open-source, so please feel free to change them or extend them.

[DevOps Workstream - Infrastructure-as-code examples on Github](https://github.com/lightenna/devops-workstream.git) 

### The Account
You'll need an AWS account.  Amazon offer the [AWS Free Tier](https://aws.amazon.com/free/) whose generous allowances should more than cover your usage, but beware.  AWS is a business.  When provisioning machines, you are renting those resources from Amazon and they do charge for them.  Be careful to follow the instructions about shutting down and cleaning up your environment so that you don't incur any unexpected charges.

### The Machine
You'll need a machine to provision this code from.  There are fundamentally two options:

1. Local provisioning
    + where you set up your local desktop or laptop computer with the tools and source code you need
1. Remote provisioning
    + where you instantiate a machine in the AWS Cloud that comes pre-installed with all the tools and source code you need

If you're new to this Remote provisioning may be a good way to start, but long-term I recommend getting your local machine set up.

### The Guide
Part of the joy of the Github platform is that as a developer I can keep the documentation that describes and supports the software on Github, right there with the software.  As a result the first lesson is embedded in the repo.

Take the next step by following the [Getting set up](https://github.com/lightenna/devops-workstream/blob/master/docs/getting_set_up.md) guide.

