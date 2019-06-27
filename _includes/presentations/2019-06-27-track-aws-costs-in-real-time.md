
## AWS web limitations
* Resources in multiple services
* Resources in multiple regions
* Retrospective billing

{% if include.pres %}Note: {% endif %}I provision a lot of cloud resources each day.
While VM (EC2) instances are the mainstay of many a modern cloud I, like others, am doing more with Lambda and AWS' other SaaS offerings.
When you factor in provisioning those many services across multiple regions around the world, in multiple accounts for multiple clients, it quickly gets easy to lose or overlook resources.
I can and do use Cost Explorer to see what happened yesterday and my monthly bill presents the hard truth of what these cloud resources have cost me, but I needed something more immediate.

---

## Cloudlog.live
* Real-time view
* Current usage
* Cost projection

{% if include.pres %}Note: {% endif %}I made a free tool to address this problem.
[Cloudlog.live](https://poc.cloudlog.live/track-aws-costs-in-real-time) is a web app that takes a real-time event stream from your Cloud provider, AWS in this example.
Based on those events it maintains a picture of all the resources in an account, then uses that to compute a cost projection.
Every time a new resource appears, or an old one gets shutdown, the projection updates.

There's a demo online now if you'd like to see what I'm talking about: [https://poc.cloudlog.live/](https://poc.cloudlog.live/track-aws-costs-in-real-time)

{% include video id="XSyfSghBCYA" provider="youtube" %}

---

## Next steps
* More clouds (Azure and Digital Ocean)
* More services

{% if include.pres %}Note: {% endif %}Cloudlog.live is going to support more services and more Cloud providers.
Microsoft Azure, Google Compute Platform and Digital Ocean are next on the list.

---

## Cost comparisons
* With other services (intra-cloud)
* With smaller instances (intra-cloud)
* With other Cloud providers (inter-cloud)

{% if include.pres %}Note: {% endif %}Where it gets really interesting is in comparison.
If I can identify that I'm over-provisioning resources, either too many (horizontally) or instances that are too big (vertically), then I can react to that insight and adapt.
Rescaling or reducing my Cloud saves money.
They're savings that I can project in Cloudlog.live.

Similarly if I can see that I'm using resources in one region or Cloud that could be more cheaply provisioned elsewhere, then I can check to see if they can be moved.
Sometimes complex constraints apply to resources that mean they have to remain in their current state and location, but often either now or in the future, they can move.
When the cost savings are significant, they should.

