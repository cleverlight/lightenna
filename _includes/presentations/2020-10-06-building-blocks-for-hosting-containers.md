
## Start simple
+ Massively powerful tools
+ Simple to use
+ Complex use cases
+ Focus on the key activities

{% if include.pres %}Note: {% endif %}
This piece is about a massively powerful set of tools that collectively manage container-based applications.
Each of these tools is vast in its power and scope.
As such, each can be used in a plethora of different ways.
By means of an introduction to each, my goal is to focus on a few functions of each tool, how they work and what they do.

---

## Docker
+ Docker runtime
+ Running containers
+ Concurrent but isolated
+ Installation options
    + Dev
    + UAT and Production

{% if include.pres %}Note: {% endif %}
Docker is not a hypervisor, but it behaves a little bit like one.
It allows different workloads to be run side-by-side without interfering with each other.
Containers ensure standardisation for distribution and isolation for execution.
Docker can be installed for a [variety of platforms](https://docs.docker.com/get-docker/).
In production, or Production-like environments, that's typically as a package for Linux.

---

## Docker interactions
+ Runs containers
    + Entry point
    + Run as 1000:1000
+ Read-only file system
+ Volumes
+ Port mapping

---

## Docker command-line
```
docker run -d --restart=unless-stopped \
  -p 80:80 -p 443:443 \
  rancher/rancher:latest
```

---

A single container running on a Docker host
{% include svg.html style="width: 25%; min-width: 150px" svg="/assets/svg/kubernetes/k8s-docker-singlehost.svg" png="/assets/svg/kubernetes/k8s-docker-singlehost.png" %}

---

## Docker build process
+ Create container image: `docker build`
+ Instantiated container: `docker run`
+ Connect into container: `docker exec -it`
+ Stop container: `docker stop`
+ Delete container: `docker rm`
+ Delete container image: `docker rmi`

---

## Docker compose
+ Run up multiple containers
+ File-based, YAML
+ Simple to start up `docker-compose up`
+ Simple to stop them `docker-compose down`

{% if include.pres!=true %}
```
version: "3"
services:
    elasticsearch:
        image: docker.elastic.co/elasticsearch/elasticsearch:7.5.1
        environment:
            - discovery.type=single-node
        ports:
            - 9200:9200

    logstash:
        image: docker.elastic.co/logstash/logstash:7.5.1
        ports:
            - 5044:5044

    kibana:
        image: docker.elastic.co/kibana/kibana:7.5.1
        ports:
            - 5601:5601
        depends_on:
            - elasticsearch
```
{% endif %}

---

A single Docker host running multiple containers side-by-side
{% include svg.html style="width: 25%; min-width: 150px" svg="/assets/svg/kubernetes/k8s-docker-singlehost-multicontainer.svg" png="/assets/svg/kubernetes/k8s-docker-singlehost-multicontainer.png" %}

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

## Kubernetes entities
+ Pod
    + wraps a container
+ Deployment
    + defines pod and how it's deployed to cluster
    + multiple instances of a pod
    + multiple different pods

---

A Kubernetes pod wrapping a single container
{% include svg.html style="width: 40%;" svg="/assets/svg/kubernetes/k8s-pod.svg" png="/assets/svg/kubernetes/k8s-pod.png" %}

---

A single Kubernetes pod wrapping multiple containers (sidecar pattern)
{% include svg.html style="width: 40%;" svg="/assets/svg/kubernetes/k8s-pod-sidecar.svg" png="/assets/svg/kubernetes/k8s-pod-sidecar.png" %}

---

## Kubernetes entities
+ Services
    + routed across multiple pods
    + hides underlying implementation
+ Route to service
    + ClusterIP
    + NodePort
    + Ingress

---

Services broker requests to an orchestrated set of pods
{% include svg.html svg="/assets/svg/kubernetes/k8s-service-across-pods.svg" png="/assets/svg/kubernetes/k8s-service-across-pods.png" %}

---

Pods may be replicated across multiple worker nodes
{% include svg.html svg="/assets/svg/kubernetes/k8s-service-across-workers.svg" png="/assets/svg/kubernetes/k8s-service-across-workers.png" %}

---

## Kubernetes cluster
+ Master nodes
+ Worker nodes

---

## Help

{% if include.pres %}Note: {% endif %}
If you'd like help organising and preparing your digital strategy, working with your team to foster a data-driven culture, or just hands-on-keyboard training in infrastructure-as-code, please [get in touch](/contact).

