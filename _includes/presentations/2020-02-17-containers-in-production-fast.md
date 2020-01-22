
## Weeks not years
+ Automate progressively
+ Start with security
+ Iterate
+ Spend your way out of trouble
+ Complexity managed with testing

{% if include.pres %}Note: {% endif %}

---

## Docker
+ Containers are good
+ Containers are simple
+ Containers are secure
+ ...but getting production is complex
+ Containers need to be managed

{% if include.pres %}Note: {% endif %}

--

## What is this 'managed'?
+ Patching and updates
+ Availability and failures
    + Health checks
+ Performance and concurrency
    + Routing
    + Load balancing
+ Coupling
    + Service discovery
    + Mutual authentication
+ Data and replication
+ Logging
+ Scanning and vulnerabilities
+ Secrets

{% if include.pres %}Note: {% endif %}

--

## Automate progressively
+ Don't try to build it all
+ Don't try to do it in one go
+ Regular releasing
+ MVP

{% if include.pres %}Note: {% endif %}

--

## Start with security
+ MVP must be secure
+ Threat surface
    + Application
    + Application dependencies
    + Container
    + Host OS
    + Host hardware
+ Staying secure
    + Never once-and-done

{% if include.pres %}Note: {% endif %}

--

## Iterate
+ Needs to be updateable
+ Start with blue-green
+ Start manual, weekly cadence

{% if include.pres %}Note: {% endif %}

--

## Backfill spending
+ Consume managed services as a stop-gap
+ Avoid vendor-specific APIs
+ Avoid starting on-prem
    + Familiar but
    + Fit for purpose?
+ Duplicate and shift-left environments
    + dev < staging < test < prod

{% if include.pres %}Note: {% endif %}
Amazon's Kubernetes service (EKS) can [run on Fargate](https://aws.amazon.com/blogs/aws/amazon-eks-on-aws-fargate-now-generally-available/), which means Amazon manage the underlying infrastructure that your pods run on.

--

## Invest in tests
+ Deliver against tests
+ Test from day 1
    + Smoke test
    + Full integration tests
    + Load test
    + UAT

{% if include.pres %}Note: {% endif %}

--

## Deliver
+ Something up in weeks
+ Gets better over time
+ Hardest part is staff training
+ Invest in your Ops team

{% if include.pres %}Note: {% endif %}

--

## Help

{% if include.pres %}Note: {% endif %}
If you'd like help organising and preparing your digital strategy, working with your team to foster a data-driven culture, or just training in the nuts and bolts of infrastructure as code, please [get in touch](/contact).

