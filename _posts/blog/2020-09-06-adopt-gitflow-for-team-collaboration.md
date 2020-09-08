---
layout: single
title: Adopt GitFlow for team collaboration
description: Git scales well from a 1-2 person team to a vast enterprise of developers, but the key is branching and merging.
tags: tech front devops git
toc: true
header:
    overlay_image: /assets/images/waterfall_flow_01392_1920x.jpg
    small_image: /assets/images/waterfall_flow_01392_640x.jpg
---

## Flow
A single developer can work on a single `develop` branch to produce a well-versioned codebase.
{% include svg.html svg="/assets/svg/gitflow/gitflow-partials-0.svg" png="/assets/svg/gitflow/gitflow-partials-0.png" %}

## Feature branching
Once there are multiple developers involved, the `develop` branch takes on a new function.  It's always in a working state, i.e. when feature branches are merged back in, the full set of integration tests pass.
{% include svg.html svg="/assets/svg/gitflow/gitflow-partials-1.svg" png="/assets/svg/gitflow/gitflow-partials-1.png" %}

Multiple independent features can be developed in parallel, by appropriate subsets of the team, such that their work doesn't interfere with each other.
{% include svg.html svg="/assets/svg/gitflow/gitflow-partials-2.svg" png="/assets/svg/gitflow/gitflow-partials-2.png" %}

## Features under epics
Where features overlap with each other, they can sit under epics.  Each epic may have multiple component feature branches.
The epic as a whole gets merged back into `develop` when meaningful to do so.
If it's working, perhaps feature-toggled, it does not necessarily have to be complete.
{% include svg.html svg="/assets/svg/gitflow/gitflow-partials-3.svg" png="/assets/svg/gitflow/gitflow-partials-3.png" %}

## Releases
Eventually it's not viable to just deploy directly from `develop`, so we create dedicated release branches.
{% include svg.html svg="/assets/svg/gitflow/gitflow-partials-4.svg" png="/assets/svg/gitflow/gitflow-partials-4.png" %}

Those release branches are periodically and systematically deployed to live.
Often the master branch is used for sending code to production.
Individual commits can be tagged with a release version number.

Release branches tend to be ephemeral: they exist for as long as they're in service (or recently in service), then get archived off or deleted.
Once deleted, the code they released will still be available as a tagged commit in `master`.
{% include svg.html svg="/assets/svg/gitflow/gitflow-partials-5.svg" png="/assets/svg/gitflow/gitflow-partials-5.png" %}

## Hotfixing
When something goes wrong the master branch can be rolled back, or fixed forward.
In most situations, time allowing, a release can be patched and flushed through, but occasionally something quicker is required.
{% include svg.html svg="/assets/svg/gitflow/gitflow-partials-6.svg" png="/assets/svg/gitflow/gitflow-partials-6.png" %}

Where hotfixes are created, the challenge is ensuring that the rest of the codebase gets that code, so that `master` does not diverge from `develop`.
Once the hotfix changes have made it back into `develop`, they will inherently become part of every new release, but old/active releases that have yet to be deprecated may need the hotfix merging in manually to ensure the pre-deployment tests are representative of live.
{% include svg.html svg="/assets/svg/gitflow/gitflow-partials-7.svg" png="/assets/svg/gitflow/gitflow-partials-7.png" %}

## Release patching
Where patches are created against a release, rather than master/live, their code too needs to be merged back into `develop`.
{% include svg.html svg="/assets/svg/gitflow/gitflow-partials-8.svg" png="/assets/svg/gitflow/gitflow-partials-8.png" %}

## GitFlow
Ultimately, the completely picture looks complicated, but is just based on a series of logical steps that make it surprisingly easy to follow so long as rare events (like hotfixes or patches) are done with rigorously.
{% include svg.html svg="/assets/svg/gitflow/gitflow.svg" png="/assets/svg/gitflow/gitflow.png" %}

## Help
If you'd like help moving your team onto GitFlow, please [get in touch](/contact).
