
## Introduction
* First steps
* Pre-requisites
* Tools
* Clouds
* Provisioning models
* Firewalls
* Access and user accounts

{% if include.pres %}Note: {% endif %}This module is the first part of the Cloud Starter course.

It introduces the course and establishes some guidelines on what you need to get started.

---

## First steps
* Teach a person to ~fish~ mess around with Internet examples for hours on end...
* Not comprehensive

{% if include.pres %}Note: {% endif %}This course is about giving those unfamiliar with the tools a starting point.

This is not a ground-up introduction of:
* every single tool/language and
+ every single coding statement in
+ every single example

Instead it's a good way to get started, build something really quickly and give you the basic grounding you need to mine the Internet for a deeper understanding.

This is intended to be the beginning of your DevOps journey, but I hope the course will also be relevant for those who've got some experience.

The course is experimentation-driven, meaning that you'll get nothing from it unless you're firing up the examples and pinging the servers and systems we create.

---

## What is DevOps?

* Not a person
* Not a programming language
* Not a fad
* It's a collaboration
* ...and tools that aid that

{% if include.pres %}Note: {% endif %}It's a contraction of Development and Operations, essentially an idea about how the two fundamental activities of web service delivery have to work together.

In a grim and not so distant past, a 'Dev' team wrote some code, then hurled it over the fence for the 'Ops' team to run it.
A lot of the rich understanding of how the application was designed to function was lost.  Frequently third-line support ended up reverting to the Dev team anyway.

Increasingly today, we rely on a more pragmatic "you build it, you run it" mentality.  This empowers developers to really think about the likely issues they'll encounter once in Production.

This means that as coders, we have a greater responsibility for building and maintaining the _environment_ in which our application will perform, as well as the application itself.

This 'DevOps' collaboration has precipitated a new set of tools - the subject of this course - which facilitate that.

---

## Pre-requisites
* Laptop
* Account with major Cloud Provider
* Time

{% if include.pres %}Note: {% endif %}

+ Essential
   + Basic coding knowledge.
   * A local machine with an SSH client and a web browser, both required for remote provisioning.
+ Preferred
   + A local machine with root/Administrator access and 100MB free space, required for local provisioning.
   + Familiarity with an IDE such as IntelliJ IDEA.

---

## Tools
* Ever improving
* Generalised methodology
* Alternatives available

{% if include.pres %}Note: {% endif %}These tools are likely to change.
Their evolution, even over Internet-timescales, has been short and storied.
Many came before and many new tools will follow, but hopefully the skills you adopt in learning these will give you the confidence to repeat the process when there are new, better alternatives available in the future.

Equally, this is a developing course, so future iterations will try to keep pace with their evolution.

---

## The tools, specifically
* Provisioning (Terraform)
* Machine images (Packer)
* Configuration management (Puppet/Ansible)
* Containerisation (Docker)
* Container orchestration (Kubernetes)

{% if include.pres %}Note: {% endif %}

---

## Clouds
* AWS
* Alternatives available

{% if include.pres %}Note: {% endif %}

---

## Local vs Remote provisioning
* Local development
* Remote production
* Remote provisioning (remprov)

{% if include.pres %}Note: {% endif %}when developing application code, there are pros and cons to all development models.

Local development places all the source code on your local desktop/laptop computer.  Access is typically fast (low latency) and high-bandwidth (direct GUI).  If the application can be run locally, testing can benefit from that same fast/high-bandwidth access.

While 'local' is a great place for application development, it's not the best place to host production solutions.  Always on hosts, reliably power supplies and dedicated network connections make servers a better place to host production services.

When developing infrastructure-as-code (IAC), the same applies but to a lesser extent.  Since most provisioning involves the client talking to a Cloud Provider (AWS/Google Cloud/Microsoft Azure), the advantage of local development is lessened.

## Remprov starter
* AWI

{% if include.pres %}Note: {% endif %}

---

## Open-source code
+ Available on [GitHub](https://github.com/lightenna/).

This course introduces the [DevOps Workstream](https://github.com/lightenna/devops-workstream) set of open-source examples in Terraform, Packer, Ansible and Puppet.

All the [Markdown source code for this presentation](https://github.com/cleverlight/lightenna/blob/master/_includes/presentations/2018-09-21-cloud-starter.md) is available on GitHub.

