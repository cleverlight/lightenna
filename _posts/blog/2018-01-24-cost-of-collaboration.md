---
layout: single-reveal
title: Cost of Dev-Ops Collaboration
description: Collaboration is brilliant - the only way - but managing the volatility, uncertainty, confusion and ambiguity associated with it is expensive.
tags: devops collaboration presentations
---

## What is DevOps?

* Neither a set of tools
* Nor a job role
* DevOps as a collaboration
* DevOps as a culture

Note: Job roles are advertised as DevOps, tools are labelled 'DevOps', but the word is a contraction of Development and Operations and eludes to a collaboration between the two.

Peter Drucker said "Culture eats strategy for breakfast."  It's a hugely over-used quote but as relevant for DevOps [as it was for motorcars when Mark Fields referenced it](https://www.torbenrick.eu/blog/culture/organisational-culture-eats-strategy-for-breakfast-lunch-and-dinner/).

To create a culture of collaboration, we've got to understand it.

---

## Cost - benefit

<div class="n-col">
<ul class="left">
<li>Hard to manage</li>
<li>Expensive</li>
<li>Bespoke or unique</li>
<li>Inefficient</li>
</ul>

<ul class="right-as-right">
<li>Great</li>
</ul>
</div>

Note: Collaboration has yielded most of the world's greatest online projects, but managed poorly it can carry a high cost.  The old "how many X does it take to change a lightbulb?" joke owes its creation to redundant collaboration.

<a href="https://xkcd.com/841/"><img src="https://imgs.xkcd.com/comics/audiophiles.png" width="740" height="285" alt="XKCD comic: Audiophiles"></a>

All projects, whether composed of 2 or 200 participants, are searching for the right balance of collaborative activity and skilled individual effort.

---

## VUCA

<p class="fragment">Volatility</p>
<p class="fragment">Uncertainty</p>
<p class="fragment">Complexity</p>
<p class="fragment">Ambiguity</p>

Note: To design a team's culture, we need to know the context in which it will work.

VUCA emerged from the US's elite training academcy [U.S. Army War College](https://books.google.co.uk/books?id=sEkp6GlK19cC&pg=PA34&dq=VUCA&redir_esc=y&hl=en#PPA6,M1).  It described the multilateral world in which the US Military found itself at the end of the Cold War.  Their experience precipitated a way of thinking about and solving problems.

For technology projects in large enterprises, that context is constantly changing.

---

## VUCA'

<p class="fragment">Vision</p>
<p class="fragment">Understanding</p>
<p class="fragment">Clarity</p>
<p class="fragment">Agility</p>

Note: Coping and excelling in that world requires a shift from VUCA to VUCA Prime, as described by [PDF: Bob Johansen, Getting There Early, 2007](https://www.bkconnection.com/static/getthereearlyPR.pdf).  The tools, processes and practices outlined here are designed to help teams maintain these prime qualities in order to be effective.

---

## Clarity as an asset

* Common language
* Source code, everything-as-code
* Version-controlled
* Dated

Note: Version-controlled means not only that the source is versioned, but also that commits are logged, attributed to the author, branched, merged and tagged for release.

The tools named here may quickly appear dated and the balance of effort invested in each will change, but the high-level activity will hopefully be consistent over time.

---

## 2. Engineering

<div class="n-col">
<ul class="left" style="width: 44%">
<li>Provisioning</li>
<li>Config management</li>
<li>Artefact management</li>
<li>Containerisation</li>
<li>Orchestration</li>
</ul>

<ul class="right as-right"  style="width: 48%">
<li>Monitoring</li>
<li>Logging</li>
<li>Performance management</li>
<li>Continuous integration</li>
<li>Disaster recovery</li>
</ul>
</div>

Note: Engineering is first because it's the most obvious as-code example.  Everything we build should be reliably and repeatably built from code.

This tutorial series will look at specific technologies in each of these areas.

---

## 1. Architecture

* Functional and non-functional requirements
* Block diagrams
* API definitions
* Message schema

Note: Architecture appears second in this deck even though it's a logical pre-cursor to Engineering.  All aspects of the solution evolve at the same time, all managed as source code.

While the Engineering team is going through set up activities in Sprint-0 (environments, pipeline config etc.) the Architecture team is piecing together minimum viable product (MVP) requirements and initial microservice designs. 

---

## 3. Testing

* TDD
* BDD
* Unit
* Integration
* Regression

Note: Test-Driven Development (TDD) helps us build the thing right.

User stories form the spec as the basis of behaviour-driven development (BDD).  If BDD helps us build the right thing, TDD makes sure we build only the right thing.  (Over-)Extending that metaphor, Unit testing and regression test suites make sure we build it right.

---

## 4. Governance and security

* Risk assessment
* Compliance audit
* Governance checklist
* Stakeholder RACI

Note: Again, keep the risk assessment with the code.  It will evolve over the course of the project, but your ability to track, mitigate and manage risks associated with the project is key.

---

## Summary

* The future
* Open source example
* Lightenna can help
* Consulting and on-site training

Note: Over the next few months, we'll be releasing, free and open-source, an example that illustrates how you and your team might put together a new project and embed DevOps collaboration at the centre of it.

If you'd like help with a particularly project, either hands-on keyboard engineering, guidance or on-site training for your team, please get in touch.

