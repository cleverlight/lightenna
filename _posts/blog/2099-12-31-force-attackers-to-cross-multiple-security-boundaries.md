---
layout: single
title: Force your attackers to cross multiple security boundaries
description: While a single firewall should be enough, the number of successful attacks implies that it's not.
tags: tech devops techupdate
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## Fan out
Implement your access rules on as wide a set of heterogenous security controls as possible (fan out).

## IAC should be DRY
Author and maintain a single description of your secure configuration, but apply it to multiple controls.

## Why double up
Having multiple boundaries means that an intruder to cross more than one nefariously.
If each is different, the nature of the circumnavigation will be different too, vastly increasing his or her workload.
An attacker could still use the IAC as a vector, but that risk needs managing whether it's one boundary or three.
