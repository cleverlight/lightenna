---
layout: single
title: Organise Puppet manifests using classes
description: 
tags: tech devops puppet
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## The value of abstraction
The goal is to hide complexity.  By placing resources in well-defined classes, we can wrap up similar configuration.
Those wrapped resources can then be treated as a single entity.

## Reorganising
In `site.pp` we still define one node, but all the complexity is shifted out into an `example` module:
```
node default {
  class { 'example' : }
}
```

The module is defined in `modules/example/manifests/init.pp`:
```
class example (

) {
  debug("This is some output from the 'example' module, visible only with -d or --debug.")
}
```

## Executing locally
The execute command has changed to accommodate the `modules` directory:
```
puppet apply -dvt ./manifests/site.pp --modulepath=./modules/
```

## Verbose output
As we've using the `-dvt` flags the output has become a lot more verbose:
```
Debug: Runtime environment: puppet_version=6.7.2, ruby_version=2.5.3, run_mode=user, default_encoding=UTF-8
Debug: Loading external facts from /home/alexs/.puppetlabs/opt/puppet/cache/facts.d
Debug: Facter: loading external fact directories from config file
Debug: Facter: fact "facterversion" has resolved to "3.14.2".
Debug: Facter: fact "aio_agent_version" has resolved to "6.7.2".
...

...
Debug: Facter: fact "fips_enabled" has resolved to false.
Debug: Reset text domain to :production
Debug: importing '/home/alexs/devops-workstream/puppet/tutorial/02-local-class/modules/example/manifests/init.pp' in environment production
Debug: Automatically imported example from example into production
Debug: Scope(Class[Example]): This is some output from the 'example' module, visible only with -d or --debug.
Notice: Compiled catalog for puppetnode in environment production in 0.02 seconds
Debug: Creating default schedules
Debug: Loaded state in 0.00 seconds
Debug: Loaded state in 0.00 seconds
Info: Applying configuration version '1565360042'
Debug: Finishing transaction 26069600
Debug: Storing state
Debug: Pruned old state cache entries in 0.00 seconds
Debug: Stored state in 0.04 seconds
Notice: Applied catalog in 0.05 seconds
Debug: Applying settings catalog for sections reporting, metrics
Debug: Finishing transaction 25630540
Debug: Received report to process from puppetnode
Debug: Processing report from puppetnode with processor Puppet::Reports::Store
```

I've abbreviated the `facter` facts at the top of output.  Crucially this debugging line shows that the module ran correctly:
```
Debug: Scope(Class[Example]): This is some output from the 'example' module, visible only with -d or --debug.
```

## Open-source
All the code for these tutorials is available as part of [DevOps-Workstream](https://github.com/lightenna/devops-workstream). 
The segments from this tutorial specifically make up `puppet/tutorial/02-local-class` [here on GitHub](https://github.com/lightenna/devops-workstream/tree/master/puppet/tutorial/).

If you'd like to see all the [previous and future installments of this tutorial](/tech/puppet), they're available under the `puppet` tag.

## Get your team coding
If you'd like to help your Operations team move to infrastructure-as-code, please [get in touch](/contact) to find out how Lightenna consulting could accelerate your Cloud journey.
