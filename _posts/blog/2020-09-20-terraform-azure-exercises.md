---
layout: single
title: Terraform exercises (Part 2 - Secret management)
description: Terraform provides a great way to create resources in the cloud using infrastructure-as-code.  Just ensure you grant yourself permission to delete the things you create!
tags: tech devops terraform
toc: true
header:
    overlay_image: /assets/images/techupdate_25318_1920x.jpg
    small_image: /assets/images/techupdate_25318_640x.jpg
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
* Grant your service principal full access to your key vault
    * Beware creating keys that you cannot see or delete!
* Grant your read-only Portal user access to your key vault
    * Ensure your networking access includes the IP of the machine that you're accessing the portal from
* Create secrets
    * `azurerm_key_vault_secret`
    * `azurerm_key_vault_key`
    * `azurerm_key_vault_certificate`
        * Generate the certificate in key vault, then `output` name and size
* Use `depends_on` to ensure that your secrets are created after and destroyed before the access permission
    * Typically this setting `depends_on` in each secret with a reference to the policy
* Design output {} statements
    * to verify that secrets have been created properly

{% if include.pres %}Note: {% endif %}
The [solution to the 'create Azure secret store' exercise](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/08-azure-secrets) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

---

## Exercise: working with workspaces
* Refactor 'create Azure secret store' exercise
    * Create dev workspace
    * Create prod workspace
    * Include ${terraform.workspace} name in all resources
* Create side-by-side (per environment) secrets
    * Create set of dev secrets
    * Create set of prod secrets at the same time
* Destroy the dev secrets
    * Verify that prod secrets are still available

---

## Exercise: referencing secrets
* Create a second root module
    * Reference a secret using the [data source](https://www.terraform.io/docs/providers/azurerm/d/key_vault_secret.html)
    * Create an output block to return some property of a secret
* Use the prod secrets in tutorial/07
    * Refactor your previous tutorial/07 code
    * Source the admin password for your VMs from AKV
        * `prod` secrets

{% if include.pres %}Note: {% endif %}
The [solution to the 'referencing secrets' exercise](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/09-referencing-secrets) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

---

## Exercise: create a VM as a docker host
* Using tutorial/06 as a reference, create a VM
    * Open up port 80 using the Network Security Group
* Customise your azurerm_virtual_machine to run a command `whoami`
    * Use the [custom_data](https://www.terraform.io/docs/providers/azurerm/r/virtual_machine.html#custom_data) field, or
    * Use a [remote-exec provisioner](https://www.terraform.io/docs/provisioners/remote-exec.html)
* Alter your command to install docker
    * `sudo curl -fsSL https://get.docker.com/ | sh`
    * Add your current user to the docker group
    * Start the docker service
    * Start the docker service on start-up (enable)
* Extend to install docker-compose
    * `sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
    * `sudo chmod +x /usr/local/bin/docker-compose`
* SSH into the VM
    * Check you can see the (empty) running container list using `docker ps`
    * List out current containers using `docker ps -a` (should be empty)
* Use the docker command line to install the [Apache HTTPd container](https://hub.docker.com/_/httpd)
* Use `curl` to connect to http://localhost:80
* Use a local web browser to connect to your public IP (http://...)

{% if include.pres %}Note: {% endif %}
The [solution to the 'docker host' exercise](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/10-docker-host) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

---

## Exercise: create single-node Kubernetes cluster with Rancher
+ Use the docker host VM from the [previous exercises](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/10-docker-host) as a base
    + Note down your hostname (e.g. host1)
+ Either: install Rancher Server using RancherD
+ Or: install Rancher Server [using a docker container](https://rancher.com/docs/rancher/v2.x/en/installation/other-installation-methods/single-node-docker/)
    + use version 2.4.11 of the container, which is the latest at the time of writing and has been tested
    + expose port 8443 on your VM by updating the Network Security Group
    + configure docker to run Rancher Server API [on a non-standard port (8443)](https://rancher.com/docs/rancher/v2.x/en/installation/other-installation-methods/single-node-docker/advanced/#running-rancher-rancher-and-rancher-rancher-agent-on-the-same-node)
+ Use a browser to connect over HTTPS your VM on port 8443
    + set an admin password for your Rancher install
+ Create a cluster in Rancher (based on existing nodes)
    + Select `Add cluster`
    + Select `From existing nodes (Custom)`
    + Select a cluster name, then `Next`
+ Add your VM as an all-roles agent node to your cluster
    + You'll need to run the agent using docker with suitable credentials for server/token etc.
    + Hint: start with the command in the `Customize Node Run Command` or `Edit cluster` screen
        + Set --server to your https://<hostname>:8443
        + Set --address to <hostname>
        + Add all roles (etcd, control plane and worker)

{% if include.pres %}Note: {% endif %}
There are at least two possible solutions to the 'kubernetes host' exercise, [using RancherD](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/11-kubernetes-host), which uses [this RancherD install script](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/11-kubernetes-host/scripts/install_rancherd.sh), or [using a docker container](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/11-kubernetes-host/scripts/install_rancher_server.sh).  They are available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).
