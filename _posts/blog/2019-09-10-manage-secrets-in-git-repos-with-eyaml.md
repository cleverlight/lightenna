---
layout: single
title: Manage secrets in Git repos using Eyaml
description: Strong asymmetric encryption can keep secrets confidential even if the repository that stores them is open source
tags: tech devops puppet
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## Templating continued
In the [previous tutorial]((/tech/puppet)) we looked at how Puppet can pull configuration data from Hiera.

Some of that configuration data is secret, for example `appserver::database_pass`.  In the previous example, we encoded that in plaintext, which potentially opens up the database to anyone with access to the repository.

## Encryption
We can encode that password with `eyaml encrypt -s '<plaintext password>'` to produce an encrypted version:
```
ENC[PKCS7,MIIbiQYJKoZIhvcNAQcDoIIBejCCAXYCAQAxggEhMIIBHQIBADAFMAACAQEw
DQYJKoZIhvcNAQEBBQAEggEAOdNlUw/ZeV9V5gV+C+hlq0Y56Z4RTL8HI2s+
5c2Ido2oNgL/XwGarrKLtRzmRm5a9B1Fsr90E9z5hfxsnneb9tqKq/mleEDh
+NBwbnSvElBdm9cQ5nwd2o/c/KYHYoL8xt/vBNzFbmhsSR7/dHjkwb3ub2vG
8zx6dDQo2k7faYN2H/RjbvG6jjtp8Un9waQJFRA+RsGxI6ddmXjNuryTDOiM
EjlxN23tsPwtET9WMc5cPH6bkeTKx+Ho5hepAOPOyDI6V3qxcJPN3740tCsU
Uj00Lebe/Va9JYw68pwwaQErm0Nt5yx1K5JqCLI5hIy7Wud8p09LgosGpaHs
JK26fzBMBgkqhkiG9w0BBwEwHQYJYIZIAWUDBAEqBBAE32W9EkB7OUY6CHaY
QiICgCBeGUugpo8nsz/nhRjngbGHxfFh4yhv3ZJ2tsgin8MBeg==]
```

## Setup
To facilitate this we need to install the `eyaml` gem, the command that allows us to encrypt or decrypt data from the command line.
```
gem install hiera-eyaml
```

If we're using this on a Puppet master (with Puppetserver installed) there's a handy shortcut that obviates the Ruby dependency:
```
puppetserver gem install hiera-eyaml
```

Full installation information can be found on the [Hiera-eyaml project page](https://github.com/voxpupuli/hiera-eyaml) on GitHub.

## Keys
We also need to generate a public-private key pair to handle the encryption and decryption operations respectively:
```
eyaml createkeys
```

## Puppet decryption
So far we've created a mechanism to put secrets into the repo and read them out.  The really clever bit about using eyaml is the hiera-eyaml backend.

Once the gem and the decryption (private) keys are installed, the hiera-eyaml backend empowers Hiera to read encrypted data at puppet-time.  This means that Puppet gets access to the secrets, without their being persisted anywhere in plaintext.

## Set up Hiera to use the hiera-eyaml backend
We can extend `hiera.yaml` to hunt for a `secrets.eyaml` in the hierarchy:
```
hierarchy:
  - name: "Per-node data"
    path: "nodes/%{::hostname}.yaml"

  - name: "Common data"
    path: "common.yaml"

  - name: "Secret data"
    lookup_key: eyaml_lookup_key
    path: "secrets.eyaml"
    options:
        pkcs7_private_key: /etc/puppetlabs/puppet/eyaml/puppet-azure-teaching-private-key-pkcs7.pem
        pkcs7_public_key: /etc/puppetlabs/puppet/eyaml/puppet-azure-teaching-public-key-pkcs7.pem

```

## Secrets.eyaml
When we embed the confidential data in `secrets.eyaml`, it's treated as a normal multi-line variable.  Take care of the indenting:
```
#
# Secrets
#
---
appserver::database_pass:
    ENC[PKCS7,MIIBiQYJKoZIhvcNAQcDoIIBejCCAXYCAQAxggEhMIIBHQIBADAFMAACAQEw
    DQYJKoZIhvcNAQEBBQAEggEAWzdGsRd9E9kt2TkAiK19JyIu6drSpY/KXTnW
    Abg6Rp3MJHBx97NJeBc5ddcDvhN+N6akAdxbDLEVY0JbJrfsoWfy0crpl/U+
    xY8BwfpdCQxUnRJ3Ervb7hxsLXqsF9BnXpNyePbTBOC3w3XTKLBCVwmIZhuz
    g32m33j3zIBA3hHc6akFmdq+gSs9yFcjFTakoj33kGyoxCcv06XyqDXjWuB5
    ccVYwbForaERLAKnfbTJkRxrNcgyRlEXAFxaw3JdjfZhRb+R91PKcqOQ5G8M
    LhSd8xfQ/IouQXtx2NlOBZS3K6/dXJ3flndHvnN6clpuVbUYODS9c4VRGPfh
    6bmOtTBMBgkqhkiG9w0BBwEwHQYJYIZIAWUDBAEqBBDLyNXKQNLzIlhAUrcx
    /pJugCAMEMRjFxSFws1HaDA6y6395XWxfrGFxmpysOMRxggZzg==]
...
```

## ...Puppet
Finally the `puppet apply` run uses the exact same command as the previous example:
```
puppet apply -dvt ./manifests/site.pp --modulepath=./modules/ --hiera_config=./hiera.yaml
```

## Open-source
All the code for these tutorials is available as part of [DevOps-Workstream](https://github.com/lightenna/devops-workstream). 
The segments from this tutorial specifically make up `puppet/tutorial/08-secret-templating-with-eyaml` [here on GitHub](https://github.com/lightenna/devops-workstream/tree/master/puppet/tutorial/).

If you'd like to see all the [previous and future installments of this tutorial](/tech/puppet), they're available under the `puppet` tag.

## Get your team coding
If you'd like to help your Operations team move to infrastructure-as-code, please [get in touch](/contact) to find out how Lightenna consulting could accelerate your Cloud journey.
