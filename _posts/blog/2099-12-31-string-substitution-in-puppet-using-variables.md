---
layout: single
title: String substitution in Puppet using variables
description: 
tags: tech devops puppet
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## The call
The user variable is passed into the class explicitly in the node definition `site.pp`:
```
node default {
  class { 'example' :
    user => 'pierre',
  }
}
```

# The definition
The module, as defined in `modules/example/manifests/init.pp`:
```
class example (
  $user,
) {

  # notice how the double quotes allow for variable substitution
  debug("The value of the variable \$user is ${user}, double-quoted")

  # single quoted strings are literal
  debug('Single quoted strings are interpreted literally (no substitution).  The value of the variable \$user is ${user}')

}
```

## Executing locally
When executed with `puppet apply -d ./manifests/site.pp --modulepath=./modules/`, we can see those debug lines in amongst the output:
```
...
Debug: Scope(Class[Example]): The value of the variable $user is pierre, double-quoted
Debug: Scope(Class[Example]): Single quoted strings are interpreted literally (no substitution).  The value of the variable \$user is ${user}
...
```

## No defaults
There are currently no defaults set in the class, so if we run the script without explictly defining the 'user' variable:
```
node default {
  class { 'example' :
  }
}
```

we get an error:
```
...
Debug: Facter: fact "fips_enabled" has resolved to false.
Debug: Reset text domain to :production
Debug: importing '/home/alexs/devops-workstream/puppet/tutorial/03-class-variables/modules/example/manifests/init.pp' in environment production
Debug: Automatically imported example from example into production
Error: Evaluation Error: Error while evaluating a Resource Statement, Class[Example]: expects a value for parameter 'user' (file: /home/alexs/devops-workstream/puppet/tutorial/03-class-variables/manifests/site.pp, line: 11, column: 3) on node puppetnode
```

## Adding class defaults:
By adding a default value to the `user` variable, we can still explicitly define it in the call, or omit it and use the default. 
```
class example (
  $user = 'centos',
) {
...
```

Here's the output when left undefined to fall back to the default:
```
...
Debug: Scope(Class[Example]): The value of the variable $user is centos, double-quoted
Debug: Scope(Class[Example]): Single quoted strings are interpreted literally (no substitution).  The value of the variable \$user is ${user}
...
```

## Open-source
All the code for these tutorials is available as part of [DevOps-Workstream](https://github.com/lightenna/devops-workstream). 
The segments from this tutorial specifically make up `puppet/tutorial/03-class-variables` and `puppet/tutorial/04-class-defaults` [here on GitHub](https://github.com/lightenna/devops-workstream/tree/master/puppet/tutorial/).

## Get your team coding
If you'd like to help your Operations team move to infrastructure-as-code, please [get in touch](/contact) to find out how Lightenna consulting could accelerate your Cloud journey.