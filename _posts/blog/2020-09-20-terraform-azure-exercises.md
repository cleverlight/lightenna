---
layout: single
title: Create resources in Azure Cloud using Terraform
description: Terraform provides a great way to create resources in the cloud using infrastructure-as-code.  Just ensure you grant yourself permission to delete the things you create!
tags: tech devops
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## Exercise: create Azure secret store
* Set up git with new feature branch
    * Clone locally (already done)
    * Create branch
    * Checkout branch
* Create resource group
* Create random_id (8 characters, alpha-numeric)
* Create random_string (24 characters)
    * Use limited set of special characters `!@#$%*_`
* Create azurerm_key_vault
    * Restrict access to your (external) IP
* Add tags to all resources to make management easier
* Read current service principal object ID
    * Hint: look at `azurerm_client_config`
* Grant your service principal full access to you key vault
    * Beware creating keys that you cannot see or delete!
* Create secrets
    * `azurerm_key_vault_secret`
    * `azurerm_key_vault_key`
    * `azurerm_key_vault_certificate`
        * Generate the certificate in key vault, then `output` name and size
* Design output {} statements
    * to verify that secrets have been created properly

{% if include.pres %}Note: {% endif %}

---

## Exercise: working with workspaces
* Refactor previous exercise
    * Create dev workspace
    * Create prod workspace
    * Include ${terraform.workspace} name in all resources
* Create side-by-side (per environment) secrets
    * Create set of dev secrets
    * Create set of prod secrets at the same time
* Destroy the dev secrets
    * Verify that prod secrets are still available

---

## Exercise: create Azure Kubernetes cluster
* Coming soon

{% if include.pres %}Note: {% endif %}

---

## Help
If you'd like help moving your team onto GitFlow, please [get in touch](/contact).
