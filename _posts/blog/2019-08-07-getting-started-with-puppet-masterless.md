---
layout: single
title: Getting started with Puppet, masterless
description: Getting going with Puppet can be as simple a few lines of infrastructure-as-code (IAC).
tags: tech devops puppet
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## Simple manifest
In `site.pp` we define a simple 'default' node:
```
# define a single general node
node default {
  notify { 'This message was posted by a simple `notify` resource' : }
}
```

## Executing locally
When run using `puppet apply site.pp`, this manifest produces a simple output:
```
Notice: Compiled catalog for puppetnode in environment production in 0.02 seconds
Notice: This message was posted by a simple `notify` resource
Notice: /Stage[main]/Main/Node[default]/Notify[This message was posted by a simple `notify` resource]/message: defined 'message' as 'This message was posted by a simple `notify` resource'
Notice: Applied catalog in 0.02 seconds
```

## Open-source
All the code for these tutorials is available as part of [DevOps-Workstream](https://github.com/lightenna/devops-workstream). 
The segments from this tutorial specifically make up `puppet/tutorial/01-site-nodes` [here on GitHub](https://github.com/lightenna/devops-workstream/tree/master/puppet/tutorial/).

## Get your team coding
If you'd like to help your Operations team move to infrastructure-as-code, please [get in touch](/contact) to find out how Lightenna consulting could accelerate your Cloud journey.
