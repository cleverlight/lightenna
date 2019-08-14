---
layout: single
title: Set up Terraform to provision in Microsoft Azure
description: Terraforming your Azure Cloud means building out a more predictable, reliable and extensible Cloud estate for the future
tags: front tech devops remprov
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## Follow-on
Once you've got Terraform installed, perhaps using an open-source [Lightenna remprov machine image](https://aws.amazon.com/marketplace) as described in [the previous post](/tech/2019/terraform-command-line-for-remote-provisioning) in this series, you then need to empower it to act on your behalf.  Terraform will instruct your Cloud provider, in this example Microsoft's Azure, to create networks and firewalls and machines and all manner of hosted services to glue them together.  To do that, it needs credentials.

## Great power
Rather than give Terraform keys to the kingdom, we want to limit its scope to the operations that we meaningfully want it to do.  To create a special kind of automated user, known as a Service Principal, we use the Azure command line.  First log into the command line:
```
az login
```
then create the Service Principal using the Azure Subscription ID (available from the Azure web console when you signed up).
```
az ad sp create-for-rbac --name certname.domain.tld --create-cert --scopes /subscriptions/<%= @subscription_id %>
```
Replace `<%= @variable_name %>` in these code snippets with the values from your Cloud provider.  This command generates a certificate with a random name, something like `/home/user/tmppeKMDz.pem`, which I recommend renaming to the form `certname.domain.tld.pem` and storing securely:

```
Changing "certname.domain.tld" to a valid URI of "http://certname.domain.tld", which is the required format used for service principal names
Please copy /home/user/tmppeKMDz.pem to a safe place. When run 'az login' provide the file path to the --password argument
{
  "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "displayName": "certname.domain.tld",
  "fileWithCertAndPrivateKey": "/home/user/tmppeKMDz.pem",
  "name": "http://certname.domain.tld",
  "password": null,
  "tenant": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

The PEM file then needs to be turned into a PFX file for use with Terraform:

```
openssl pkcs12 -export -out "certname.domain.tld.pfx" -in "certname.domain.tld.pem" -passout pass:
```

## Listing the Service principals
After you've created a service principal, you can optionally list the ones you've created to check they're correct:
```
az ad sp list --display-name="certname.domain.tld"
```

Executing this command unrestricted `az ad sp list` produces a very long JSON string, so I recommend filtering it to see just the ones you've created.

## Environment variables
The connection to Terraform is made using environment variables.  The instructions below explain how to do set them up on a Linux-based operating system, but Terraform supports an array of other platforms.

Create a script file to export the environment variables, e.g. `~/.azure/environment`
```
#!/bin/sh
echo "Setting Azure environment variables for Terraform client [subscription]"
export ARM_SUBSCRIPTION_ID="<%= @subscription %>"
export ARM_TENANT_ID="<%= @tenant_id %>"
export ARM_CLIENT_ID="<%= @client_id %>"
export ARM_CLIENT_CERTIFICATE_PATH="${HOME}/.azure/certname.domain.tld.pfx"
```

`<%= @tenant_id %>` here is your Azure Active Directory ID.  `<%= @client_id %>` here is your Service Principal user ID.

## Load once
To load these environment variables from the command-line type:
```
source ~/.azure/environment
```

## Load every time
The environment variables will only remain set within that session unless you include the script as part of your session initialisation.  To do that, append these lines to your user's `.bashrc` file:
```
# add Azure environment variables if present
if [ -f ~/.azure/environment ]; then
        source ~/.azure/environment
fi
```

## Terraform on
Now that you're set up to provision resources in Azure, you should be able to run `terraform apply` on the next tutorial as part of [DevOps-Workstream](https://github.com/lightenna/devops-workstream).

If you'd like to see all the [previous and future installments of this tutorial](/tech/remprov), they're available under the `remprov` tag.

## Get your team coding
If you'd like to help your Operations team move to infrastructure-as-code, please [get in touch](/contact) to find out how Lightenna consulting could accelerate your Cloud journey.
