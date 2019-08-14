---
layout: single
title: Import Hiera values into Puppet classes
description: When configuration code contains 'hard-coded' configuration values, it's much harder to maintain.  Hiera allows us to break the latter out into something readable.
tags: tech devops puppet
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## Introduction
Hiera is great.  It allows us to lift the values out of our Puppet manifests, which creates a healthy separation.
Hiera contains the values.
Puppet manifests contain the description of what to do with those values.

In a well-managed infrastructure, it should be possible to clone repeating, but subtly different, config patterns by simply adding to the Hiera config.
The Puppet manifest is like a blueprint that maps the Hiera config to the machine configuration.

## Node definition
This is an abstract concept, so let's take a look at an example:
```
node default {
  class { 'example' : }
}
```

# The definition
The module is defined without a default:
```
class example (
  $user,
) {
...
}
```

## Command line with --hiera_config
```
puppet apply -dvt ./manifests/site.pp --modulepath=./modules/ --hiera_config=./hieradata/hiera.yaml
```

## Hiera setup
`hiera.yaml` tells Puppet where and how to find values:
```
#
# hiera.yaml
#   referenced by `puppet apply` and `puppet agent` calls
#   during masterless/mastered puppet run
#
---
version: 5
hierarchy:
  - name: "Per-node data"
    path: "nodes/%{::hostname}.yaml"

  - name: "Common data"
    path: "common.yaml"

defaults:
  data_hash: yaml_data
  datadir: ./

```

In `common.yaml` we define our first value for the `example` class:
```
example::user: "azula"
```

This means that the value `azula` is going to be passed to the `$user` variable in the `example` class.

## Output
The debugging output now features a lot of information from Hiera:
```
...
Debug: Automatically imported example from example into production
Debug: Automatic Parameter Lookup of 'example::user'
  Searching for "lookup_options"
    Global Data Provider (hiera configuration version 5)
      Using configuration "/home/alexs/devops-workstream/puppet/tutorial/05-class-attribute-values-from-hiera/hieradata/hiera.yaml"
      Merge strategy hash
        Hierarchy entry "Per-node data"
          Path "/home/alexs/devops-workstream/puppet/tutorial/05-class-attribute-values-from-hiera/hieradata/nodes/remprov.yaml"
            Original path: "nodes/%{::hostname}.yaml"
            Path not found
        Hierarchy entry "Common data"
          Path "/home/alexs/devops-workstream/puppet/tutorial/05-class-attribute-values-from-hiera/hieradata/common.yaml"
            Original path: "common.yaml"
            No such key: "lookup_options"
    Module data provider for module "example" not found
  Searching for "example::user"
    Global Data Provider (hiera configuration version 5)
      Using configuration "/home/alexs/devops-workstream/puppet/tutorial/05-class-attribute-values-from-hiera/hieradata/hiera.yaml"
      Hierarchy entry "Per-node data"
        Path "/home/alexs/devops-workstream/puppet/tutorial/05-class-attribute-values-from-hiera/hieradata/nodes/remprov.yaml"
          Original path: "nodes/%{::hostname}.yaml"
          Path not found
      Hierarchy entry "Common data"
        Path "/home/alexs/devops-workstream/puppet/tutorial/05-class-attribute-values-from-hiera/hieradata/common.yaml"
          Original path: "common.yaml"
          Found key: "example::user" value: "azula"
...
```

and crucially the correct `debug()` message using the class variable sourced from Hiera:
```
Debug: Scope(Class[Example]): The value of the variable $user is azula
```

## Open-source
All the code for these tutorials is available as part of [DevOps-Workstream](https://github.com/lightenna/devops-workstream). 
The segments from this tutorial specifically make up `puppet/tutorial/05-class-attribute-values-from-hiera` [here on GitHub](https://github.com/lightenna/devops-workstream/tree/master/puppet/tutorial/).

If you'd like to see all the [previous and future installments of this tutorial](/tech/puppet), they're available under the `puppet` tag.

## Get your team coding
If you'd like to help your Operations team move to infrastructure-as-code, please [get in touch](/contact) to find out how Lightenna consulting could accelerate your Cloud journey.
