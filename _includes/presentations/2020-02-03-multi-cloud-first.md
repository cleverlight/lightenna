
## Why Multi-cloud at all?
+ Vendor competition
+ Commoditised resources
+ Long-term price resilience
+ Wider opportunity surface

{% if include.pres %}Note: {% endif %}
Many organisations are moving their digital services and websites to the Cloud.
Large or 'Hyperscale' Cloud vendors offer organisations of every size ways to reduce their total cost of ownership (TCO),
either by:
* increased flexibility - provisioning just what you need, just when you need it or
* reduced service operation cost - provisioning managed services that allow you to specialise on your core activity

Common infrastructure-as-a-service (IaaS) standards have 'commoditised' many of the simple offerings.
The plethora of Cloud vendors offering "a virtual server" or "an object store" or "an SQL database" has driven down cost.
That highly competitive marketplace ensures that prices will stay low, often close to the marginal cost of delivery.

Amongst that field, innovation can be a differentiator.
They're all trying to flank each other, with new offerings that are designed to help you do what you're doing in the digital age, more effectively and at lower cost.

When developing a Cloud strategy many IT managers have said to me "We're going to start with Vendor X only.  We will use Vendor Y for something else later."
In reality, later, they don't.

There's a base cost-of-doing-business with Vendor X, such as setting up a billing relationship, provisioning and managing access, integrating with governance processes, familiarity with the way Vendor X does thing etc.
Once you've paid that, it's just easier to keep adopting more services from Vendor X.
That choice shuts down new opportunities, gives Vendor X a monopoly on your business and in the long-term increases costs.

Radical as it may sound, don't choose just one Cloud vendor.  Start with multi-cloud!

---

## Downside
+ Increased complexity
+ Not viable with click-and-tick
+ Requires infrastructure-as-code
+ Exposure to more intra-cloud changes
+ Little inter-cloud standardisation

{% if include.pres %}Note: {% endif %}
This decision is not a no-brainer, which is good because you've got a brain.
There are downsides: largely short-term pain to recoup as long-term gain.

Multi-cloud means increased complexity.
You can't manage multiple clouds with those nice click-and-tick web interfaces that the big vendors provide.
Even if you're doing single-cloud, you shouldn't anyway.

Managing that complexity across multiple clouds requires infrastructure-as-code.
All aspects of the provisioning, configuration and management of the Cloud, ranging from security and credential management to log aggregation, needs to be coded.
That code becomes the entity that is testable, verifiable, securable.
It's the key to resilience and reliability in services.
Component failures are unavoidable, but disasters become manageable, often mitigated entirely.

There's little Cloud standardisation, so in order to avoid getting overwhelmed in a deluge of vendor patches and API changes, we need an abstraction layer to make multi-Cloud an possibility.

---

## Bigger upside
+ Infrastructure-as-code
+ Terraform as cloud standardisation layer
+ Puppet for configuration management
+ K8s/Docker app standard platform
+ Free Devops-Workstream reference implementation

{% if include.pres %}Note: {% endif %}
Thankfully the landscape is full of tools that provide exactly that abstraction, for example:
* Rancher for Kubernetes deployments
* Terraform for IaaS and PaaS
* Puppet, Chef or Ansible for configuration management
* Docker for containers

By adopting these tools, rather than their vendor-specific equivalents, it becomes viable to build out the same basic building blocks in multiple cloud, which opens up a fistful of opportunities.
What's more, it's often not substantially more effort if well-managed.

---

## Multi-cloud first
+ Avoid single-vendor offerings
+ Avoid vendor lock-in
+ Keep vendors competitive
+ Ensure solid architecture
+ Stay agile to seize next opportunity

{% if include.pres %}Note: {% endif %}
Multi-cloud works because you're not competing an RTT just once: you're competing every single service, every single time you provision it.
The advantage is constant choice and forces vendors to constantly compete, which is better for pricing and flexibility.

Migration is never _just_ lift and shift.  Any migration typically exposes technical debt.
If there were shortcuts taken when designing the service architecture, or hacks put in place when engineering it, a cross-cloud (or on-premise to off-premise) migration will expose them.
But if the service was designed with a few basic principles in mind, to be multi-cloud or better, cloud-agnostic, then the benefit multiplies accordingly.
You see that return once when competing the service, once when extending the service and again when migrating it.

Agility is only important if you can't entirely predict the future of your service.
That said, I've yet to meet any organisation that could accurately foresee the future.
(Possibly except the bookies!)

---

## Help

If you'd like help organising and preparing your digital strategy, working with your team to foster a data-driven culture, or just training in the nuts and bolts of infrastructure as code, please [get in touch](/contact).

