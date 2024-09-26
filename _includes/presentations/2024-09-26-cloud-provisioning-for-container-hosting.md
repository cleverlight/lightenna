
## Cloud provisioning
+ Goal to create infrastructure that is:
  + Managable
  + Scalable
  + Secure
+ Managed as code
  + Terraform
  + AZ CLI
+ Azure examples

{% if include.pres %}Note: {% endif %}

This presentation is a follow-on from:
* [Building blocks for hosting containers](/tech/2020/building-blocks-for-hosting-containers/)
* [Productionising containers](/tech/2020/put-containers-into-production-fast/)
* [Git version control (part 1)](/tech/2019/git-version-control-magic/)
* [Gitflow (part 2)](/tech/2020/adopt-gitflow-for-team-collaboration/)

---

## Kubernetes
+ Container orchestration
+ Pods and services

---

Services broker requests to an orchestrated set of pods
{% include svg.html svg="/assets/svg/kubernetes/k8s-service-across-pods-by-host.svg" png="/assets/svg/kubernetes/k8s-service-across-pods-by-host.png" %}

---

Pods may be replicated across multiple worker nodes
{% include svg.html svg="/assets/svg/kubernetes/k8s-service-across-workers.svg" png="/assets/svg/kubernetes/k8s-service-across-workers.png" %}

---

## Bigger picture
+ Service in project context
+ Service-specific requirements
  + Container registry
  + Secret management
  + Secure access (bastion hosts)
  + Networks

---

## Bigger picture
+ Service in a wider context
+ Adjunct requirements
  + Managing Terraform state
  + Cloud security
  + Logging and monitoring
  + DNS
  + User management (Active Directory)
  + Networks

---

## Bigger picture
{% include svg.html svg="/assets/svg/azure-cloud-architecture2-simplified.svg"  png="/assets/svg/azure-cloud-architecture2-simplified.png" %}

---

## Examples
+ Terraform (Kubernetes)
  + Azure Kubernetes Service (AKS)
+ Terraform (App Service)
  + Azure App Service
  + Azure Container Registry (ACR)
  + Azure Key Vault

---

## Help

{% if include.pres %}Note: {% endif %}
If you'd like help organising and preparing your digital strategy, working with your team to foster a data-driven open culture, or just hands-on-keyboard training in infrastructure-as-code, please [get in touch](/contact).

