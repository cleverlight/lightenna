---
layout: single
title: Puppet for configuration-managed Windows desktops
description: Configuration management makes homogenising similar machines easier and there are some great free tools to get started
tags: front tech devops
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## Multiple Windows
Mine is a small company, but I manage a few dozen Windows machines.  Even as the version numbers have ticked up, there's still quite a lot of repetitive work involved.

## Choco-what?
The first step is to get a command-line package manager installed.  [Chocolatey](https://chocolatey.org/docs/installation) has the best traction currently, so we run this script in Powershell to install it:
```
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```
`Powershell` needs to be run as an administrator, so Click `Start` -> type `Powershell` -> right-click `Powershell` result -> Click `Run as administrator`.

As when running anything from the Internet, you should inspect [the referenced script](https://chocolatey.org/install.ps1) to make sure you're happy with its activities.  The pseudo-code below sums them up:

```
# Get latest version of the Chocolatey package for download
# Download the Chocolatey package
# Determine unzipping method (download 7zip if required)
# Unzip the package
# Call chocolatey install
# Ensure chocolatey commands are on the path
# Ensure chocolatey.nupkg is in the lib folder
```

## Puppet agent
Next we need to install an agent to configure our local Windows desktop.  Thankfully the install process is trivial now we've got `choco`:
```
choco install puppet
```
By default this installs an old version of Puppet (3.8.7).  That's convenient if you're talking to an old Puppet master (< 4), but if you've migrated to a more modern Puppet master, you're better off with an up-to-date agent too (6.7.2):
```
choco install puppet-agent
```

## Conf
Finally we need to edit the puppet.conf file (`C:\ProgramData\PuppetLabs\puppet\etc`) to point to our Puppet master and restart the service.

## Perpetually running agent
By default Puppet agent will run every 30 minutes.  You can disable the `Puppet agent` service using the Windows Services component (Click `Start` -> type `services.msc` -> select `Services`).

## Manual
Puppet agent can be run manually, with debugging output from an elevated Powershell command line:
```
puppet agent -dvt
```

## Help available
If you'd like help setting up your Windows estate with infrastructure-as-code, please [get in touch](/contact) to find out how Lightenna consulting could accelerate your Cloud journey.
