---
layout: single
title: Create a Puppetmaster using Puppet masterless
description: A simple exercise in bootstrapping the most complex config-managed server in the estate, the Puppetmaster.
tags: tech devops puppet
toc: true
header:
    overlay_image: /assets/images/techupdate_25318_1920x.jpg
    small_image: /assets/images/techupdate_25318_640x.jpg
---

## Managing complexity
One of the most complex hosts within a configuration-managed server estate is the Puppet master.
Often that host is the most difficult to get right, the most complex to maintain and the most vulnerable, as if compromised it can lead to the whole estate being breached.
The case for automating the deployment and configuration of the Puppet master is easy to make, but often ignored in favour of a manual deployment due to the bootstrapping problem.

## Chicken or egg
We want Puppet to install the Puppetmaster, but most machines typically derive their configuration from the Puppetmaster.
Thankfully we can use Puppet in a light-weight 'masterless' configuration.
We have to do some of the heavy lifting that the master would normally do, such as authenticating the machine and transferring the manifests, but we can use Terraform to help with that.

## Provisioning
Our open-source [DevOps-Workstream](https://github.com/lightenna/devops-workstream) repo contains a full set of integrated scripts to provision a machine then run Puppet masterlessly on it.
I recommend checking that out as it's the easiest way to get started, but I'll highlight what it's doing here.

## Pulling the server up by its bootstraps
Behind the magic of that `terraform apply`, the Terraform script is doing a simple install of Puppet agent and its dependencies:
```
sudo yum -y install epel-release
sudo rpm -Uvh https://yum.puppet.com/puppet6-release-el-7.noarch.rpm
sudo yum -y update
sudo yum -y install puppet-agent
```

Alternatively this could all be done using Puppet Bolt, but that's a conversation for another day.

## Role vs Software
The role this server plays is Puppet master, in that the other hosts connect to the master as an authoritative source of configuration values, mappings and dependencies.
The software that it runs to accomplish this is Puppet Server.  Those two terms tend to get conflated and reversed, but I'll try to use each with a single consistent meaning.

## Starting point
This is the `site.pp` that shows the base description of what's on our `puppetmaster` or `puppetmaster-testX` servers:
```
node 'puppetmaster',/^puppetmaster-test\d+/ {
  # basic machine setup
  class { 'general': }->
  # environment setup
  class { 'puppetmaster': }
}
```

## Including community modules
Rather than write all the Puppet code ourselves, we can rely on a good array of community support made available via [Puppet Forge](https://forge.puppet.com).  For this activity I'd recommend adding these to your `Puppetfile`:
```
mod 'puppet-puppetboard'
mod 'puppet-puppetserver'
mod 'camptocamp-augeas'
mod 'puppetlabs-puppetserver_gem'
mod 'puppetlabs-puppetdb'
mod 'puppetlabs-postgresql'
mod 'puppetlabs-inifile'
```

## Puppetmaster class (and Puppet masterclass)
Inside that `puppetmaster/manifest/init.pp`, we want to install Puppet Server, PuppetDB and Puppetboard to visualise what our Puppetmaster is doing. 
```
# install puppetserver
class { 'puppetserver::repository': } ->
class { 'puppetserver':
  config => {
    'java_args' => {
      # experimenting with smaller footprint, really should be >= 2g,2g
      'xms' => '1g',
      'xmx' => '1g',
      # support removed in JDK8
      # 'maxpermsize' => '512m',
      'tmpdir' => '/tmp',
    },
  },
}

# install puppetdb and its underlying database
class { 'puppetdb':
  manage_firewall => false,
  java_args => {
      '-Xmx' => '512m',
      '-Xms' => '512m',
  },
  disable_ssl => true,
}

# install puppetboard
class { 'puppetboard':
  manage_git => true,
  manage_virtualenv => true,
  reports_count => 20,
  default_environment => 'prod',
}
```

Next we need to configure our Puppetmaster to talk to PuppetDB.  As we're running them on the same machine, there's no harm in allowing Puppet Server to talk to PuppetDB over plain HTTP.  The port (8080) isn't exposed beyond `localhost`:
```
  # configure the Puppetmaster to use puppetdb
  class { 'puppetdb::master::config':
    puppetdb_server => 'localhost',
    puppetdb_port => 8080,
    puppetdb_disable_ssl => true,
  }
  # install eyaml plugin for puppetserver
  class { '::puppetserver::hiera::eyaml':
    require => Class['puppetserver::install'],
  }
```

Let's expose Puppetboard on port 443 (HTTPS):
```
class { 'apache':
  default_vhost => true,
}
class { 'apache::mod::wsgi': }
$filename_certificate = "${cert_directory_path}/${cert_name}.crt"
$filename_key = "${key_directory_path}/${cert_name}.key"
class { 'puppetboard::apache::vhost':
  vhost_name => "${cert_name}",
  ssl => true,
  ssl_cert => $filename_certificate,
  ssl_key => $filename_key,
  port => 443,
}
```

And because this is a production server, we'll need to use proper certs and keys:
```
File {
  owner => 'root',
  group => 'root',
  mode  => '0640',
}

$filename_certificate = "${cert_directory_path}/${cert_name}.crt"
$filename_cabundle = "${cert_directory_path}/${cert_name}.ca-bundle"
$filename_key = "${key_directory_path}/${cert_name}.key"

# create certificate files
file { "$filename_key":
  content => $key,
} ->
file { "$filename_certificate":
  content => $certificate,
} ->
file { "$filename_cabundle":
  content => $ca_bundle,
}
```

## Basic security
A production Puppet master should be hidden behind a firewall, so that it's only visible to your estate of Cloud machines.
Puppet's pretty secure, but I'd still be disinclined to expose 8140 to the open Internet.
Also, I recommend putting some kind of basic password on the dashboard (443).  We can modify the `vhost` resource with a Resource Collector, something like this:
```
::Apache::Vhost <| title == "${cert_name}" |> {
  directories => [
    {
      path => '/',
      auth_type => 'Basic',
      auth_name => 'Basic Auth',
      auth_user_file => '/etc/httpd/secure/.htpasswd',
      auth_require => "valid-user",
    },
  ]
}
```

We'll also need to create the .htpasswd file
```
httpauth { 'name':
  username => 'username',
  file     => '/etc/httpd/secure/.htpasswd',
  password => 'password',
  realm => 'realm',
  mechanism => basic,
  ensure => present,
}
```

If you'd like to see all the [previous and future installments of this tutorial](/tech/puppet), they're available under the `puppet` tag.

{% include call_to_action-opsteam_iac.html %}
