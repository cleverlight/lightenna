---
layout: single
title: Kubernetes exercises
description: Create a simple hosted service using Kubernetes and kubectl
tags: tech devops kubernetes
toc: true
header:
    overlay_image: /assets/images/techupdate_25318_1920x.jpg
    small_image: /assets/images/techupdate_25318_640x.jpg
---

## Exercise: roll out a simple deployment to set up a hosted service
* Create a `deployment.yaml` manifest
    * Deploy the [Hello Kubernetes](https://hub.docker.com/r/paulbouwer/hello-kubernetes/) container from Docker Hub
        * Guidance on [authoring deployment manifests](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
    * Label the pods
        * In your spec.template for the deployment you can attach an app label:
```
metadata:
    labels:
        app: my-kubernetes-app
```
    * Run the deployment using `kubectl`
        * `kubectl apply -f deployment.yaml`
    * Verify the pods have been deployed successfully
        * `kubectl get pods`
        * `kubectl get deployments`
* Create a `service.yaml` manifest to deploy the service
    * Guidance on [authoring service manifests](https://kubernetes.io/docs/concepts/services-networking/service/)
    * Use the label from earlier to identify the pods that compose your service.
       * In your spec.selector you can refer to the label you created earlier:
```
        app: my-kubernetes-app
```
* Test the service using a web browser.

{% if include.pres %}Note: {% endif %}
This exercise builds on many of the previous labs for [Docker](/tech/2021/docker-exercises/) and Terraform, parts [1](/tech/2019/terraform-language-exercises/), [2](/tech/2020/terraform-azure-exercises/) and [3](/tech/2021/terraform-integration-exercises/).
If you're attempting these exercises without completing the previous labs, you might need to use this [Terraform Azure AKS solution](https://github.com/lightenna/devops-workstream/tree/master/terraform/tutorial/13-azure-simple-aks) to build a Kubernetes cluster to experiment on.

The solution to the 'Kubernetes deployment and service' exercise is available as a [kubectl/YAML solution](https://github.com/lightenna/devops-workstream/tree/master/kubernetes/tutorial/01-service-deployment) as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

---
