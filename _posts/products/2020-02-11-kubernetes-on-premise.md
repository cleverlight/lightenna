---
layout: splash
title: Kubernetes on-premise
description: Make the most of your existing tin with a standardised cloud platform.  Our part/fully-managed, on-premise Kubernetes offerings give you improved reliability and resilience, reduced Operations costs and a migration path to the Cloud.
permalink: /products/kubernetes-on-premise
tags: products front kubernetes
header:
    overlay_image: /assets/images/datacentre_00934_1920x.jpg
    actions:
      - label: "Convert now!"
        url: "#form"
reference_test_page: https://raw.githubusercontent.com/mmistakes/minimal-mistakes/master/test/_pages/splash-page.md
preview:
    parentheses: "(Part/fully-managed)"
feature_intro:
  - excerpt: 'Containers are transforming the way we develop and deploy code, but managing them in production requires a variety of skills.  We specialise in Cloud platforms, so you can concentrate on the core business activity that adds value to your customers.  We offer an array of services ranging from a simple out-of-the-box installation and setup of an on-prem Kubernetes cluster, through to a complete managed service including low-level patching, software updates and even attended deployments.'
feature_row:
  - image_path: assets/images/superhand_14154_12899_640x.jpg
    title: "Less downtime"
    excerpt: "By using rolling deployments, you can reduce your service downtime to zero."
    alt: "less-downtime-server-hand-zero"
  - image_path: /assets/images/managedatacentre_157315_640x.jpg
    title: "Better utilisation"
    excerpt: "Fewer distractions from the racks and pipes, so you can focus on delivering business value."
    alt: "better-utilisation-server-monitoring"
  - image_path: /assets/images/curvyroad_01246_640x.jpg
    title: "Route to Cloud"
    excerpt: 'Make on-prem Kubernetes part of your wider digital strategy, perhaps as a 2-5 year stop-gap before migrating to the Cloud.'
    alt: "route-to-cloud-highway-traffic"
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

{% include feature_row id="feature_intro" type="center" %}

{% include feature_row %}

{% include feature_row id="feature_cloudframework" type="right" %}

<a name="form" />
<form action="https://formspree.io/alex_stanhope@hotmail.com"
      method="POST">
    <input type="text" name="name" placeholder="Your name">
    <input type="email" name="email" placeholder="Your email">
    <textarea name="message" placeholder="Your message"></textarea>
    <p>There's a human-being on the end of this form, so please tell us how and when you'd like to be contacted
    and anything pertinent about the on-prem environment that you'd like to move to Kubernetes.</p>
    <button type="submit" class="btn btn--primary btn--large">Send</button>
</form>
<div stlye="clear:both;">&nbsp;</div>