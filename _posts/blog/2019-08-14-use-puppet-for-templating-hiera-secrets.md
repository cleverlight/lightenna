---
layout: single
title: Use Puppet for templating Hiera secrets into configuration files
description: 
tags: tech devops puppet
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## Templating
The goal is to substitute variables into a template to produce a configuration file.

## Variable scopes
The variables in our template come from multiple sources:

* top-level global variables (from facter), e.g.
    * `::hostname`
    * `::fqdn`

* class-level variables (inherited from Hiera), e.g.
    * `port`
    * `database_name`, `database_user`, `database_pass`

* resource/low-level variables (defined in file resource), e.g.
    * `service_name`

## File resource
```
  file { '/tmp/configuration.xml':
    ensure => 'present',
    content => epp('appserver/configuration.xml.epp', {
      'service_name' => "${::hostname}-appserver"
    }),
  }
```

## Open-source
All the code for these tutorials is available as part of [DevOps-Workstream](https://github.com/lightenna/devops-workstream). 
The segments from this tutorial specifically make up `puppet/tutorial/07-templating` [here on GitHub](https://github.com/lightenna/devops-workstream/tree/master/puppet/tutorial/).

## Get your team coding
If you'd like to help your Operations team move to infrastructure-as-code, please [get in touch](/contact) to find out how Lightenna consulting could accelerate your Cloud journey.
