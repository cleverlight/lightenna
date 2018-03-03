---
layout: single
title: Kubernetes for a migratable future
description: Serverless function-as-a-service (like AWS Lambda) is magic, but it's hard to commit at this early stage
tags: devops scale
header:
  overlay_image: /assets/images/containers_on_ship_05027.jpg
---

Orchestration that might also be the grease that eases vendor lock-in

This week I've been working on the technical design for a production Kubernetes cluster.  Kubernetes, or K8s for short, is a fantastic technology.  The Internet is full of K8s primers so I'm not going to try to introduce the terms or concepts that make K8s a great platform for container orchestration.  Instead I'd like to make the case for using it.

The sea of DevOps tools, Cloud platforms and Infrastructure services is broad and tumultuous.  There are so many to choose from and new entities emerge on a fortnightly basis.  Solution architects are constantly challenged to deeply understand that seascape (or cloud-scape if you're willing to sublimate the metaphor) and, armed only with a tentative but current understanding of the problem to be solved, make justifiable technical decisions: what's the right tool for the job?  Or more accurately, what's the right tool for this job, what's the right version, what's the right division of responsibility between the different components, today, and how does all of this interact with the myriad of previous decisions?

For me it underscores why architecture isn't a once-and-done activity.  Agile projects are learning things about requirements all the time.  Functional and non-functional requirements are discovered and iteratively mined for understanding.  The constraints of a solution are regularly changing.  Architecture must keep pace.  Evolutionary architecture sounds grand, but really it's as important to high-level design as TDD is to coding.

The challenge is trying to work out how the needs (user needs, technical needs, compliance needs, governance needs, security needs, operational needs) are going to develop over time and equally how the solution is going to age.  

Serverless computing feels like the future.  Few businesses need to run EC2 instances as part of their core business, but the services that contain their core business logic need to run somewhere.  The somewhere is changing.  Five years ago I led a major project on Google AppEngine precisely because I didn't have the diversity or scale of tech team required to build and operate our own hosting platform.  We ran on Google's platform-as-a-service (PaaS) and on the whole we had a good experience.  It suited that project.

In between I've built out an app based on Elasticsearch, RabbitMQ and MySQL.  That needed a fine-grain of control.  AWS-everything would have been an option, but with Puppet skills in-house and a NFR to avoid vendor lock-in, we built out VMs in DigitalOcean.  Maintenance was a bigger part of the run-costs, but manageable.

For my next project I'm thinking about where to _place_ the solution.  I won't go into the details, but again it's multiple open-source technologies working side-by-side to deliver a low-latency web service.  Amazon is a compelling option, especially with Terraform for provisioning to make future migration to another Cloud giant at least feasible, but add Lambda to the mix and pretty quickly a migration starts looking a whole lot like a wholesale infrastructure-as-code (IAC) rebuild.  The Serverless framework is interesting, but I haven't seen enough breadth and depth there to give me confidence that it's would be smooth sailing using it for production and at scale.

Cut back to Kubernetes.  Amazon Fargate will be offering K8s-based managed hosting by the end of 2018.  Google Kubernetes Engine is mature and there are others.  The reason I'm leaning towards K8s over serverless is the freedom to move.  If you build your containers, organise them into well-defined pods, you can _relatively_ easily move those pods (and the logical services they offer) from one place to another.  It's a migration path that holds water.  Whether you go to another major incumbent, some yet-to-be-talked-about start-up or your own on-prem solution, there are low-impact, low-cost and well-established migration paths open to you.

Maybe I should stick with Puppet and Docker on my own machines?  Maybe I should just do it all serverless in AWS?  Perhaps I'm clinging to a design principle (vendor-agnosticism) that's now dated or redundant, but with Kubernetes gaining more traction everyday, it feels like a good third way.
