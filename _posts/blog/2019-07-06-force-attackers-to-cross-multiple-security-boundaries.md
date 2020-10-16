---
layout: single
title: Force your attackers to cross multiple security boundaries
description: While a single firewall should be enough, the number of successful attacks implies that it's not.
tags: tech devops techupdate
toc: true
header:
    overlay_image: /assets/images/techupdate_25318_1920x.jpg
    small_image: /assets/images/techupdate_25318_640x.jpg
---

Cloud Security is becoming ever more important as organisations increasingly put their faith in the major cloud platforms.

There's loads of good security advice out there, but I wanted to illustrate one specific practice that can better manage the risk associated with placing data or running services in the Cloud.

## Fan out
> Implement your access rules on as wide a set of heterogenous security controls as possible (fan out).

## IAC should be DRY
The goal is to author and maintain a single description of your secure configuration, but apply it to multiple controls.  That makes it easy to maintain - day-to-day activities such as exposing a new port are quick to implement - but also easier to audit.

> Security is much easier to check when it's implemented the same way everytime using infrastructure-as-code (IAC).

## Why double up
One can imagine a criticism along the lines "if I've already got a firewall, why do I need a second one?"

Having multiple boundaries means that an intruder has to cross multiple boundaries, each one nefariously.
If each is different, the nature of the circumnavigation will be different too, vastly increasing his or her workload.

An attacker could still use the IAC as a vector, but that risk needs managing whether it's one boundary or two or more.

