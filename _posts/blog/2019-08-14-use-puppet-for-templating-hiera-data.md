---
layout: single
title: Use Puppet for templating Hiera data into configuration files
description: Maintaining infrastructure-as-code at scale requires a clear, logical and ruthlessly consistent approach to machine state.  Hiera is the way.
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
This file resources composes the contents of the file from an EPP template, which in turn references the variables above.
```
  file { '/tmp/configuration.xml':
    ensure => 'present',
    content => epp('appserver/configuration.xml.epp', {
      'service_name' => "${::hostname}-appserver"
    }),
  }
```

## Hiera
To pull class data from Hiera, we need to create a hiera.yaml file:
```
hierarchy:
  - name: "Per-node data"
    path: "nodes/%{::hostname}.yaml"

  - name: "Common data"
    path: "common.yaml"
```

and refer to it in the `puppet apply` command:
```
puppet apply -dvt ./manifests/site.pp --modulepath=./modules/ --hiera_config=./hiera.yaml
```

## Template
The template could use ERB (Ruby-like) or EPP, but for simplicity's sake, we'll stick with Puppet's Embedded Puppet (EPP) syntax.
```
<?xml version="1.0" encoding="utf-8" ?>
<server address="<%= $::fqdn %>">
  <service name="<%= $service_name %>">
    <port number="<%= $appserver::port %>" />
  </service>
  <database name="<%= $appserver::database_name %>" username="<%= $appserver::database_user %>" password="<%= $appserver::database_pass %>" />
</server>
```

## Open-source
All the code for these tutorials is available as part of [DevOps-Workstream](https://github.com/lightenna/devops-workstream). 
The segments from this tutorial specifically make up `puppet/tutorial/07-templating` [here on GitHub](https://github.com/lightenna/devops-workstream/tree/master/puppet/tutorial/).

If you'd like to see all the [previous and future installments of this tutorial](/tech/puppet), they're available under the `puppet` tag.

{% include call_to_action-opsteam_iac.html %}
