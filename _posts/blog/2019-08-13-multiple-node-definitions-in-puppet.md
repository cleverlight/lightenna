---
layout: single
title: Multiple node definitions in puppet's site.pp
description: 
tags: tech devops puppet
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## More the merrier
We've started with a single node, which probably translates to a single machine or a single family of nearly-identical machines.

Now let's start to add in other machine definitions (nodes):
```
node default {
  class { 'example' : }
}

node remprov {
  class { 'example' : }
}
```

## Specialising hiera values
So far, we've already defined user in the class (where the default is 'centos') and in `common.yaml` (azula).

We now define it just for the new node (remprov) in `remprov.yaml`:
```
example::user: "yuliana"
```

Hiera operates an inheriting structure.  Values are sourced in order from hiera.yaml, so it tries to find the value in `hieradata/nodes/remprov.yaml` in preference to `hieradata/common.yaml`.

## Output
Similar to the previous installment, we execute locally again giving `puppet` a relative path for the `modules` and `hieradata` directories, i.e. `puppet apply -dvt ./manifests/site.pp --modulepath=./modules/ --hiera_config=./hieradata/hiera.yaml`.  When run on the `remprov` host, the output shows our specialised user value:
```
Debug: Scope(Class[Example]): The value of the variable $user is yuliana on remprov
```

## Open-source
All the code for these tutorials is available as part of [DevOps-Workstream](https://github.com/lightenna/devops-workstream). 
The segments from this tutorial specifically make up `puppet/tutorial/06-second-node` [here on GitHub](https://github.com/lightenna/devops-workstream/tree/master/puppet/tutorial/).

If you'd like to see all the [previous and future installments of this tutorial](/tech/puppet), they're available under the `puppet` tag.

## Get your team coding
If you'd like to help your Operations team move to infrastructure-as-code, please [get in touch](/contact) to find out how Lightenna consulting could accelerate your Cloud journey.
