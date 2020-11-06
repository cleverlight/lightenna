
## What is Kubernetes?
+ What are containers?
+ What is Docker?
+ Where are my apps?
+ Why orchestrate?

{% if include.pres %}Note: {% endif %}

---

## Applications
+ Hosted on a server
+ Installed on the disk
+ Run as processes
+ Provide a service
+ Quality of service

{% if include.pres %}Note: {% endif %}

---

A single application running on a host
{% include svg.html style="width: 25%; min-width: 150px" svg="/assets/svg/kubernetes/k8s-app-singlehost.svg" png="/assets/svg/kubernetes/k8s-app-singlehost.png" %}

---

## Containers
+ Standardised
+ Isolated
+ Easily distributed
+ Improved security

{% if include.pres %}Note: {% endif %}
Containers ensure standardisation for distribution and isolation for execution.

---

A single container running on a host
{% include svg.html style="width: 25%; min-width: 150px" svg="/assets/svg/kubernetes/k8s-docker-singlehost.svg" png="/assets/svg/kubernetes/k8s-docker-singlehost.png" %}

---

## Docker
+ Docker is a container platform
+ Standard for containers
+ Not a hypervisor
+ Docker Hub is a library

{% if include.pres %}Note: {% endif %}
Docker is not a hypervisor, but it behaves a little bit like one.
It allows different workloads to be run side-by-side without interfering with each other.
Docker can be installed for a [variety of platforms](https://docs.docker.com/get-docker/).
In production, or Production-like environments, that's typically as a package for Linux.

---

## Multiple containers
+ All isolated from one another
+ Managed interactions
+ Workload control
+ Security

---

A single host running multiple containers side-by-side
{% include svg.html style="width: 25%; min-width: 150px" svg="/assets/svg/kubernetes/k8s-docker-singlehost-multicontainer.svg" png="/assets/svg/kubernetes/k8s-docker-singlehost-multicontainer.png" %}

---

## Things go wrong
+ Hosts crash
+ Goal is quality service delivery:
    + Reliability
    + Performance
    + High-availability
+ Redundant copies

---

Multiple Docker hosts behind a load balancer
{% include svg.html svg="/assets/svg/kubernetes/k8s-docker-multi-host.svg" png="/assets/svg/kubernetes/k8s-docker-multi-host.png" %}

---

## More to manage
+ Config management
    + Networking
+ Secret distribution
+ Simplicity of load balancer
+ Identical nodes
    + Non-adaptive
+ Need help orchestrating

---

Kubernetes
{% include svg.html style="width: 25%; min-width: 150px" svg="/assets/svg/kubernetes/k8s-icon.svg" png="/assets/svg/kubernetes/k8s-icon.png" %}

---

## Kubernetes
+ Container orchestration
+ Networking
+ Services
    + Load balancing
    + High availability
+ Ingress
+ Secret management

---

A Kubernetes pod wrapping a single container
{% include svg.html style="width: 40%;" svg="/assets/svg/kubernetes/k8s-pod-elasticsearch.svg" png="/assets/svg/kubernetes/k8s-pod-elasticsearch.png" %}

---

## Kubernetes entities
+ Pod
    + Wraps a container
+ Deployment
    + Defines pod and how it's deployed to cluster
    + Multiple instances of a pod
    + Multiple different pods

---

Multiple Kubernetes pods deployed across multiple hosts
{% include svg.html svg="/assets/svg/kubernetes/k8s-distributed-pods-multi-host.svg" png="/assets/svg/kubernetes/k8s-distributed-pods-multi-host.png" %}

---

## Kubernetes entities
+ Services
    + Routed across multiple pods
    + Hide underlying implementation

---

Services broker requests to an orchestrated set of pods
{% include svg.html svg="/assets/svg/kubernetes/k8s-service-across-pods-by-host.svg" png="/assets/svg/kubernetes/k8s-service-across-pods-by-host.png" %}

---

## Help

{% if include.pres %}Note: {% endif %}
If you'd like help organising and preparing your digital strategy, working with your team to foster a data-driven culture, or just hands-on-keyboard training in infrastructure-as-code, please [get in touch](/contact).

