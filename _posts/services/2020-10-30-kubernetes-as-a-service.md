---
layout: splash
title: Kubernetes as a service
description: We provide a high-powered (e.g. 48vCPU/256GB RAM) Kubernetes cluster, ready-to-go, fully-managed and monitoring by Lightenna engineers.  Deploy your production workload in minutes using kubectl, Helm or visually with Rancher.
permalink: /services/kubernetes-as-a-service/
canonical_url: https://www.lightenna.com/services/kubernetes/
redirect_from:
  - /products/kubernetes-as-a-service/
tags: services front
header:
    overlay_image: /assets/images/cloudland_01197_1920x.jpg
    small_image: /assets/images/cloudland_01197_640x.jpg
preview:
    parentheses: "(Managed)"
feature_kubernetes_animation:
  - video_id: "U8FtybTpA3c"
    excerpt: "Containers are transforming the way we develop and deploy code, but managing them in production requires a variety of skills.  We specialise in Cloud platforms, so you can concentrate on the core business activity that adds value to your customers.  We offer an array of services ranging from a simple out-of-the-box installation and setup of an on-prem Kubernetes cluster, through to a complete managed service including low-level patching, software updates and even attended deployments."
feature_row_features:
  - title: "Less downtime"
    image_path: /assets/images/superhand_14154_12899_640x.jpg
    excerpt: "By using rolling deployments, you can reduce your service downtime to zero."
    alt: "less-downtime-server-hand-zero"
  - title: "Better utilisation"
    image_path: /assets/images/managedatacentre_157315_640x.jpg
    excerpt: "Fewer distractions from the racks and pipes, so you can focus on delivering business value."
    alt: "better-utilisation-server-monitoring"
  - title: "Route to Cloud"
    image_path: /assets/images/curvyroad_01246_640x.jpg
    excerpt: 'Make on-prem Kubernetes part of your wider digital strategy, perhaps as a 2-5 year stop-gap before migrating to the Cloud.'
    alt: "route-to-cloud-highway-traffic"
feature_foss:
  - title: "Puppet"
    image_path: /assets/screenshots/screenshot-puppetboard_640x.png
    excerpt: "Puppetboard as a user interface (UI) for Puppet and PuppetDB"
    alt: "puppetboard-screenshot"
  - title: "Rancher and Kubectl"
    image_path: /assets/screenshots/screenshot-rancher_640x.png
    excerpt: "Rancher visual UI and Kubectl command-line for cluster maintenance and deployments"
    alt: "rancher-screenshot"
  - title: "Elasticsearch"
    image_path: /assets/screenshots/screenshot-kibana_640x.png
    excerpt: "Elasticsearch, Logstash & Kibana (ELK) for logging and Prometheus & AlertManager for monitoring"
    alt: "kibana-screenshot"
feature_cloudframework:
  - image_path: assets/svg/cloud_framework_cybertunnel_880x.jpg
    title: "Everything you need for Cloud"
    excerpt: "Kubernetes may already fit into your digital strategy, but if you'd like advice on how to integrate an on-prem cluster into your existing Cloud infrastructure, please [get in touch](/contact/).  Our consultants can bring to bear years of experience in Cloud adoption to help your business take on the right mix of services from hyperscale providers such as AWS, Google Cloud and Microsoft Azure."
    alt: "cloud-framework"
    url: "/tech/2018/cloud-framework/"
    btn_label: "Read More"
    btn_class: "btn--inverse"
---

<style>
    /* hack page title for alignment on this particular image */
    h1.page__title {
        padding-top: 1.0em;
    }
</style>

{% include feature_row id="feature_kubernetes_animation" type="left" %}

{% include feature_row id="feature_row_features" %}

# Solid architecture, solid future

No web project should be deployed without the backing of good architecture to ensure we build the right thing and it's built right.  Done right, a new platform can be transformative so we provide clear documentation to show how your environments will work.  We agree with you what hostnames should be assigned, how DNS will work, what level of firewalling should be built into the solution and the base operating system for each machine build.  We then provide a quote that shows precisely what we will deploy if you decide to go ahead.

{% include svg.html svg="/assets/svg/azure-cloud-architecture2-simplified.svg"  png="/assets/svg/azure-cloud-architecture2-simplified.png" %}

<div class="feature__wrapper">&nbsp;</div>

To make sure your Kubernetes cluster continues to run reliably, every Lightenna Kubernetes environment also includes:
* Configuration-managed set of firewalled hosts
* Pre-configured Kubernetes cluster to run across the worker nodes
* Infrastructure-as-code manifests to provision and manage machines
* Distributed block storage class (Cloud storage or Longhorn on-prem)

<div class="feature__wrapper">&nbsp;</div>

# Free and Open-source Software (FOSS) foundations

Everything we do is based on open standards, to ensure that you never become locked into a single vendor.
Along with your cluster, we deliver the infrastructure-as-code that you need to maintain, replicate and extend what you've paid for.  We hope our great service will mean you choose us again in the future.

{% include feature_row id="feature_foss" %}

# Support

The success of any kind of Cloud project depends not only on a good delivery but how well it\'s supported in production.  We offer three different service offerings, depending on what you decide is the best fit for your organisation:
* Staged handover: we train your team to build confidence in the technologies that underpin the cluster, then we're available for ad hoc support, if rather than when it's required.
* Part-managed: we patch and maintain the cluster, by proactively monitoring for issues before they affect the service.
* Fully-managed: as above, but we also handle code deployments to the cluster and application upgrades.

{% include feature_row id="feature_cloudframework" type="right" %}

# Let us show you the business benefits of Kubernetes

<a name="form" />
<form action="https://formspree.io/f/xqaebqzd" method="POST">
    <label>Your name:<input type="text" name="name"></label>
    <label>Your email:<input type="email" name="email"></label>
    <label>Your message:<textarea name="message"></textarea></label>
    <p>There's a human-being on the end of this form, so please tell us how and when you'd like to be contacted
    and anything pertinent the workload you'd like to host in our managed Kubernetes service.</p>
    <button type="submit" class="btn btn--primary btn--large">Send</button>
</form>
<div stlye="clear:both;">&nbsp;</div>