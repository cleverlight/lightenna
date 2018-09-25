
## Anatomy of a Cloud
{% include svg.html svg="/assets/svg/cloud_framework_v1.svg"  png="/assets/svg/cloud_framework_v1.png" %}

{% if include.pres %}Note: {% endif %}This Cloud framework gives you an overview of the different areas we're looking to build up to deliver great scalable web services.

---

## Tools
* Illustrate with tools
* Overlapping functionalities

{% if include.pres %}Note: {% endif %}For each of the main areas, let's pull out some of the tools that can be configured to deliver that function, often by working together.

The nature of the space and its history mean that many of these tools can play multiple roles.  The functional reach of each tool often spans several of the activities listed here.
For example Jenkins and Terraform are so multi-facetted, each one can be used to deliver a whole array of environments, configurations and jobs.
The goal is to pick the right tool for the activity, but to ensure the interplay between tools is seamless.

> Poor integration or misapplication can undermine the effectiveness of these great tools.

---

## Drawing data out
* Log capture (e.g. Fluentd, Logstash, Elasticsearch)
* Application log analysis (e.g. Kibana)
* Security log analysis
* APM (e.g. Stackify, Dynatrace)

{% if include.pres %}Note: {% endif %}

---

## Managing code
* Source control (e.g. GitHub)
* Continuous Integration (e.g. Jenkins)
* Configuration management (e.g. Puppet, Ansible, Chef)
* Artifact management (e.g. Artifactory)

{% if include.pres %}Note: {% endif %}

---

## Deployments and environments
* Environment management
* Continuous Deployment (e.g. Jenkins)
* Container hosting (e.g. Docker)
* Container orchestration (e.g. Kubernetes)

{% if include.pres %}Note: {% endif %}

---

## Machines and services
* Subscribed service provisioning (e.g. CloudFormation for AWS RDS/Lambda/DynamoDB)
* Machine provisioning (e.g. Terraform)
* Patch management
* Secure base operating system
* Off-cloud access and LAN integration (e.g. AWS DirectConnect)

{% if include.pres %}Note: {% endif %}

---

## Users and accounts
* \[Maintenance\] User management
    * Separate from application-user management
* Account billing, management, delegation, governance etc.

{% if include.pres %}Note: {% endif %}

---

## Accessible
* Open-source
* Cloud isn't really an isolated _thing_
* Cloud is about application(s)
* Get in touch

{% if include.pres %}Note: {% endif %}If you'd like to talk to Lightenna about how we can help your business maximise the value of Cloud technology, please [get in touch](/contact).
