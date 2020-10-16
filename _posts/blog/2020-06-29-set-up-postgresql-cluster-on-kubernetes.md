---
layout: single
title: Set up PostgreSQL cluster on Kubernetes in 5 minutes
description: Managing the data layer is non-trivial because containers need redundancy and high-availability in order to be reliable.  Enter Helm, the Kubernetes package manager, to make the orchestration simpler.
tags: tech devops kubernetes
toc: true
header:
    overlay_image: /assets/images/techupdate_25318_1920x.jpg
    small_image: /assets/images/techupdate_25318_640x.jpg
---

## Docker first
The world has become containerised and where before we'd spend hours trying to perfect an environment to then _begin_ installing an application, we can now simply load the container and set some environment variables.

## Productionising
However, rarely are these apps ready to go.  If we're going to run them in production we need to think about things like high availability, reliability, secrets and backups.
Enter Kubernetes, which allows us to configure multiple instances of an app into a cluster and distribute volumes over multiple nodes.

## PostgreSQL
Postgres is a relational database.  As part of the data layer, it represents the 'harder' sort of deployment: one that contains state that we care about.

## Getting started with a cluster
To preserve that state reliably (and be performant) we cluster the app, which means instantiating multiple instances of those containers and getting them to talk to each other.

### Install Helm
Download and [install Kubernetes Helm](https://helm.sh/docs/intro/install/), which is sort of like a package manager for Kubernetes:
```
wget https://get.helm.sh/helm-v3.2.4-linux-amd64.tar.gz
tar -zxvf helm-v3.2.4-linux-amd64.tar.gz
```

### Add the Bitnami repo
Bitnami offer a [pre-configured set of Helm charts](https://github.com/bitnami/charts/tree/master/bitnami/postgresql-ha) for multi-node PostgreSQL:
```
helm repo add bitnami https://charts.bitnami.com/bitnami
```

### Fire up cluster
Create a cluster configuration file (`values.yaml`), for any settings that we don't want to be default.  I've gone with 3 nodes rather than 2.
```
---
postgresql:
    replicaCount: 3
...
```

Next we spin up the PostgreSQL cluster, confined to a namespace to make it easier to clean up afterwards:
```
RELEASE_NAME="hapostgres"
RELEASE_NAMESPACE="${RELEASE_NAME}"
helm install ${RELEASE_NAME} bitnami/postgresql-ha --create-namespace --namespace=${RELEASE_NAMESPACE}
```

### Inspecting the cluster
Helm is an over-the-top package manager, so underneath it we're still using `kubectl`, from which the former inherits its settings (typically `.kube/config`).
```
kubectl get all -n ${RELEASE_NAMESPACE}
```

### Shutting down
Helm makes this pretty easy:
```
helm delete ${RELEASE_NAME} --namespace=${RELEASE_NAMESPACE}
```

but we just need to tell Longhorn (or whatever persistence layer you're using on your K8S cluster) to clean up the volumes and finally, delete the containing namespace:
```
kubectl delete pvc --all -n ${RELEASE_NAMESPACE}
kubectl delete namespace ${RELEASE_NAMESPACE}
```

