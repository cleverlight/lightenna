---
layout: single
title: Terraform exercises (Part 1 - Language)
description: These exercises for part of the Terraform section of our Cloud training courses.
tags: tech devops terraform
toc: true
header:
    overlay_image: /assets/images/techupdate_25318_1920x.jpg
    small_image: /assets/images/techupdate_25318_640x.jpg
---

## Exercise: variables
* Create a root module
* Create a `unique_id` input variable
    * Give it a sensible default
* Create a local variable
* Create a `message` output variable
    * Use string interpolation to return a string composed of:
        * Your local variable
        * The `var.unique_id` class variable
        * The current terraform workspace `${terraform.workspace}`
* Run `terraform apply`
* Re-run terraform but pass a different value for unique_id

{% if include.pres %}Note: {% endif %}
The [solution to the 'variables' exercise](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/01-variables) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

---

## Exercise: create Azure Resource Groups
Follow the [Create Resource group](/tech/2019/terraform-resource-groups-in-Azure/) tutorial to create resource groups with dynamic naming.

{% if include.pres %}Note: {% endif %}
The [solution to the 'create Resource Group' exercise](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/03-azure-resource-group-with-unique-default) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

---

## Exercise: create Azure Networks
* Create a root module
    * Reuse the standard components (such as `backend.tf` and `provider.tf` from the previous tutorials
* Create an `azurerm_virtual_network`
    * for 10.0.0.0/16
* Create an `azurerm_subnet`
    * for some /24 subnet of that address space
    * e.g. 10.0.1.0/24
* Create an `azurerm_network_security_group`
    * Open port 22 for inbound traffic from the Internet

{% if include.pres %}Note: {% endif %}
The [solution to the 'create Azure Network' exercise](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/04-azure-network) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

---

## Exercise: Network as a module
* Look at the module examples in DevOps Workstream
    * [04b-simple-module](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/04b-simple-module)
    * [04c-house-foundation-module](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/04c-house-foundation-module)
* Re-write your previous solution as a module

{% if include.pres %}Note: {% endif %}
The [solution to the 'Network as a module' exercise](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/05-azure-network-as-module) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

---

## Exercise: using the docs
* Research on Terraform.io how to use the AzureRM provider to create a Linux Virtual Machine
    * Start with the [deprecation notice for the old resource type](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_machine)
    * You should aim to re-use your solution to the previous exercise for the network
* Extend your solution to create virtual machines using a module
    * Instantiate your virtual machine module twice
    * Create two `output` resources that use string interpolation to compose an SSH command
        * One to SSH to each of your new hosts

{% if include.pres %}Note: {% endif %}
The [original solution](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/07-azure-vm-twice) used a now-deprecated resource type.network

The ['referencing secrets' exercise solution](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/09-referencing-secrets) uses the more up-to-date `azurerm_linux_virtual_machine` resource type.

---

As with all exercises that involve Cloud provisioning, please ensure you `terraform destroy` all your Cloud resources after completing the exercise, in order to minimise your Cloud charges from Microsoft.

Further exercises were recently added to this series:
* [Creating more advanced resources in Azure](/tech/2020/terraform-azure-exercises/)

