---
layout: single
title: Terraform-Docker integration exercises
description: Azure provides all the building blocks we need to securely run containers in the Cloud, we just need Terraform to glue them together
tags: tech devops docker terraform
toc: true
header:
    overlay_image: /assets/images/techupdate_25318_1920x.jpg
    small_image: /assets/images/techupdate_25318_640x.jpg
---

## Exercise: build a container hosting environment
* Create an Azure Key Vault
    * Create a randomly-generated [azurerm_key_vault_secret](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/key_vault_secret) called `temp-password`.
        * While this secret isn't used, it validates that AKV can create (and destroy) secrets.
        * Create an `output` resource to show some information about the created secret.
    * The Key Vault must be created in its own isolated root module.
    * Declaring the Key Vault's access policies inline (as part of the azurerm_key_vault resource) makes deletion easier and removes the need for manual depends_on references.
* Provision an Azure Container registry using the [azurerm_container_registry resource type](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_registry).
    * The Container registry must be created in a separate root module.
    * Enable the admin user.
    * Record the admin user's password in your Key Vault.
        * Use a [azurerm_key_vault data source](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/data-sources/key_vault) to reference your existing Key Vault.
* Use [docker login](https://docs.docker.com/engine/reference/commandline/login/) to authenticate against your new container registry.
* Create a containerised Node.js application
    * You might choose to use the `Dockerfile` and management scripts that your wrote as your solution to the [previous 'environment variables' exercise](https://github.com/lightenna/devops-workstream/tree/master/docker/tutorial/03-dockerfile-environment-variables).
    * Configure docker to accept a `PORT` environment variable.
    * Modify your management scripts to build the container and upload it to your container registry.
* Create an [azurerm_app_service](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/app_service) instance.
    * Again, the instance must be created using a separate root module.
* Deploy a container from your Container registry to your App Service instance.
    * Output a URL that allows you to test you Node.js application from a browser.

{% if include.pres %}Note: {% endif %}
This exercise is much more substantial than previous exercises.  Please take it slowly, code a couple of lines then test and iterate, refactor as needed.

The solution to the 'container hosting' exercise is composed of both [a Terraform solution](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/12-container-hosting), [a Docker solution](https://github.com/lightenna/devops-workstream/tree/master/docker/tutorial/06-dockerfile-cloud-hosting) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

---
