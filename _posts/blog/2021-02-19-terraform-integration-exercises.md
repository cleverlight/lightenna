---
layout: single
title: Terraform-Docker integration exercises
description: Azure provides all the building blocks we need to securely run containers in the Cloud, we just need Terraform to glue them together
tags: tech devops docker kubernetes terraform
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
    * Declaring the Key Vault's access policies inline (as part of the [azurerm_key_vault](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/key_vault) resource) makes deletion easier and removes the need for manual depends_on references.
* Provision an Azure Container registry using the [azurerm_container_registry resource type](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_registry).
    * The Container registry must be created in a separate root module.
    * Enable the admin user.
    * Record the admin user's username and password in your Key Vault.
        * Use a [azurerm_key_vault data source](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/data-sources/key_vault) to reference your existing Key Vault.
        * Store each credential in its own secret.
* Use [docker login](https://docs.docker.com/engine/reference/commandline/login/) to authenticate against your new container registry.
    * Extend your Container registry module to produce a `docker login` command as output to make command-line login easier.
        * You'll need to inline the password for now with either `--password` or `--password-stdin`.  While this is too insecure for production, it's sufficient for a short-lived password in an IAC exercise.
        * Also provider a `docker logout` command as output.
* Create a containerised Node.js application
    * You might choose to use the `Dockerfile` and management scripts that your wrote as your solution to the [previous 'environment variables' exercise](https://github.com/lightenna/devops-workstream/tree/master/docker/tutorial/03-dockerfile-environment-variables).
    * Configure docker to accept a `PORT` environment variable.
    * Modify your management scripts to build the container and upload it to your container registry.
        * Be careful to re-build and re-push your container if you re-create your container registry.
        * Verify you can see your repository and tag in the [Azure Portal](https://portal.azure.com/) `Container registry` dashboard, `Repositories` blade
* Create an [azurerm_app_service](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/app_service) instance.
    * Again, the instance must be created using a separate root module.
        * Hint: start by using a community module, such as [this one by InnovationNorway](https://registry.terraform.io/modules/innovationnorway/web-app-container/azurerm/latest), to create all the azurerm_app_service resources.
    * Initially configure the app service to run a public container image, before trying to authenticate against your Azure Container Registry.
        * Hint: use a public image that you're familiar with (default ports etc.) from a previous exercise such as [nginx:latest](https://hub.docker.com/_/nginx) to make testing easier.
        * Output the app_service hostname to test your deployment in a browser.
            * Give azure_app_service plenty of time (2-3 minutes) to pull and start the container.
            * Check the start-up process using the logs visible in the [Azure Portal](https://portal.azure.com/) `App Service` dashboard, `Deployment Centre` blade
* Deploy a container from your Container registry to your App Service instance.
    * Set up authentication so that your App Service instance can pull container images from the Container Registry.
    * Output a URL that allows you to test you Node.js application from a browser.

{% if include.pres %}Note: {% endif %}
This exercise is highly dependent upon the Cloud you're using to provision resources and has been written with Microsoft Azure in mind.  It's also much more substantial than previous exercises.  Please take it slowly, code a couple of lines then test and iterate, refactor as needed.

The solution to the 'container hosting' exercise is composed of both [a Terraform solution](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/12-container-hosting), [a Docker solution](https://github.com/lightenna/devops-workstream/tree/master/docker/tutorial/06-dockerfile-cloud-hosting) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

## Exercise: build and connect to a Kubernetes cluster
* Provision Kubernetes cluster
* Download a local Kubeconfig file
    * Store in `~/.kube`
        * The default file used by `kubectl` is `~/.kube/config
    * If using an alternative file name, perhaps because you've already got Kube configurations set up on your machine, set up a KUBECONFIG environment variable to temporarily point at the right filename.
        * e.g. `export KUBECONFIG=~/.kube/azure-aks-kubeconfig`
        * If exported in a script file, the environment variable will only be available to commands run in that script file.
        * If exported at a (Linux) command prompt, the environment variable will only be available during that session.
* Connect to cluster using `kubectl`
    * List nodes that make up the cluster
        * `kubectl get nodes`
    * List available pods
        * `kubectl get pods`

{% if include.pres %}Note: {% endif %}
Again, this exercise is highly dependent upon the Cloud you're using to provision resources and has been written with Microsoft Azure in mind.

The solution to the 'kubernetes cluster' exercise is available as [a set of Terraform manifests](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/13-azure-aks) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).



---
