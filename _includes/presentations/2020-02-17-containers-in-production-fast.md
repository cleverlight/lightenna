
## Weeks not years
+ Automate progressively
+ Start with security
+ Iterate
+ Spend your way out of trouble
+ Complexity managed with testing

{% if include.pres %}Note: {% endif %}
The world would lose it's spontaneity if every action was idempotent.

I want the 'play' button to produce a different result each time I watch something because I love the weekly churn of box sets on Netflix.
I don't want to always eat the same flavour of jelly bean.
And if I wanted every day to look the same, I'd still be working for Big Blue.

The thing is, some things really have to be.

I want the fire alarm button to work exactly the same way every time someone needs to press it.
I don't want there to be any random variation when I hit the brake pedal in my car.
I like my test suite green.

So when containers came along, providing an idempotent way of delivering web services, a lot of DevOps engineers breathed a collective sigh of relief.
Docker didn't invent idempotency, but they their read-only, managed-access, largely-stateless view of the world made it a lot more attainable.

But they also have to be run in production.

---

## Docker
+ Containers are good
+ Containers are simple
+ Containers are secure
+ ...but getting production is complex
+ Containers need to be managed

{% if include.pres %}Note: {% endif %}
We love containers.
They work really well.
In closeted environments (like dev) their single-command magic makes service available in a few seconds where previously installs took hours.

In production, containers offer a meaningful simplification of the hosted service world we've all been curating for years.
However, the world containers promise is still beset by the same issues as our present reality.

There are still attackers finding new ways of exploiting previously unknown loopholes.
There are still patches to apply to our service and the libraries, hypervisors, operating systems and hardware that support it.
There are still compounding failures that can occur at any level of that stack.
There are still compliance obligations and governance.

All the things we needed to do yesterday to keep the service running consistently, performantly, securely, resiliently are still things we need to do today.

--

## What is this 'managed'?
+ Patching and updates
    + Scanning and vulnerabilities
    + CI/CD
    + Regression testing
+ Availability and failures
    + Health checks
    + Monitoring
+ Performance and concurrency
    + Routing
    + Load balancing
+ Coupling
    + Service discovery
    + Mutual authentication
+ Secrets
+ Data and replication
+ Logging
    + Application logging and SIEM
+ Ongoing business information and DW
+ People
    + Developer and application engineer access
    + Operations and administrator access

{% if include.pres %}Note: {% endif %}
To cope with these challenges, we need to be able to patch and update containers.
Assuming our move to containers hasn't coincided with a greater appetite for service interruption and downtime, that means multiple instances and load balancers, which themselves will need patching.
Each new container will need scanning for vulnerabilities as part of CI/CD pipeline.
Each new release needs to deliver the same quality of service and user experience without regression, which means automated testing.

We want the service to remain available not only when we intervene, but also when unpredictable failures affect it.
That means health checks and monitoring.

We want to be able to keep up with peak periods in demand.
That means either a high level of redundant capacity, or some kind of reactive scaling.
We also want to manage costs, so scaling down is important too.

All these scaled instances exist for varying lengths of time.
They need to be able to talk to each other, in so far as service A needs to be able to reliably communicate with its dependant services B, C, D to deliver A.
That means we need to sort service discovery and dynamic routing.

All these elements need to be routable, but those routes need to be tightly controlled to remain secure.
They need to be able to mutually authenticate each other so that data doesn't get sent to the wrong, perhaps malicious, masquerading service.
All these elements need firewalling, as part of a multi-level security onion that can withstand at least partial compromise without disclosing or leaking data.

The integrity of the system as a whole relies on credentials, keys, passphrases and other secret data.
Those secrets need to be managed and distributed securely.

Data needs to be managed.
In a 12-factor world, where each microservice has its own autonomous, isolated data source, that's a lot of databases.
Each database needs to have redundant copies of the data, ready for failover.
We need to take backups, regularly, without affecting the principal service.
We need to test and restore them and verify the integrity of the data they store.

With all these complex dataflows and the myriad of multi-tier components

With the nature and complexity of cyber attacks growing year-on-year, we probably need to transfer all that log information to a SIEM for analysis.
Then there's the ongoing business needs to understand what's happening for every actor in this data universe.
For that we have a data warehouse, so data needs extracting and loading (and perhaps transforming) into that.

Then there are the people that need to interact with this complex system, and interact in such a way that they never accidentally break it.
They need to be authenticated, repeatedly and regularly with multiple factors.
Their access needs to be controlled and restricted appropriately.
They different live-like environments to conduct their tests or develop new functionality.

--

## Automate progressively
+ Don't try to build it all
+ Don't try to do it in one go
+ Regular releasing
+ MVP

{% if include.pres %}Note: {% endif %}
This is a pretty overwhelming list, but this container-utopia can be built progressively.

Never build applications in isolation, in the vain hope that we can "sort out production" when the app's nearly finished.

> Build the app and it's production environment side-by-side.

* Start with a simple, private (firewalled) deployment.
* Work out how to iterate.
* Implement a regular release cycle.
* Focus on a minimum viable 'product' in each area, then improve it.

That's the entirety of what's required.
Once you've got that, you will eventually deliver the kind of comprehensive platform described earlier.

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
It's hard to know which corners to cut.
Generally I recommend cutting functionality, not non-functional requirements.
The very first minimum viable product (MVP) must be secure, so it's worth investing in proper container scanning and infrastructure security.
Managing that with infrastructure-as-code is a great way to make that iterable.
Iteration is the key - nothing is ever done!

--

## Iterate
+ Needs to be updatable
+ Start with blue-green
+ Start manual, weekly cadence

{% if include.pres %}Note: {% endif %}
The instant you've got a single secure container hosted in production, you'll need to update it.
I'm a big proponent of engineering-discipline over vendor-hype, which means infrastructure-as-code.
Having that code makes it fairly trivial to duplicate the setup.
Instead of just having a single production environment, create two.
If _Blue_ is hosting the website now, set up _Green_ with the new version.
Once you're confident that Green will deliver the same quality of service, switch the DNS across.
This blue-green independence allows you to run tests against new versions, patching on-the-fly, or even try out new features with a subset of your users.
You can build up the complexity (like Canary deployments, Parallel running or Load sharing) over time.

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
It's a great example of relying on the managed services that Hyperscale Cloud vendors provide, rather than building it all yourself.

It's not the only way.  It may not even be the right way for you in the future, but it's almost certainly the right way to start out.
By paying the vendor (who has greater access to massive economies of scale) to take care of the service management, you can concentrate on your core business activities\: the special sauce that allows you to differentiate your product, not the sesame seems that make you like every other company in your space.

When you know that you need to run a 100,000 server farm to build a rendering pipeline for your next 3D Animated feature, maybe paying AWS for on-demand EC2 instances won't be the way to go, but it might be now.

--

## Invest in tests
+ Deliver against tests
+ Test from day 1
    + Smoke test
    + Full integration tests
    + Load test
    + UAT

{% if include.pres %}Note: {% endif %}
Away from the nuts, bolts and engine grease that goes into managing bare-metal servers, there are several more important areas of your web service to invest in.

Get your test suite to the point that it confidently reflects the users' journeys through your service.
At that point, it instill confidence not only that your service is working properly (every time you run it),
but more that it will _continue_ to work properly.
That test suite is becomes the yardstick for every patch, every migration, every newly developed feature.
If the test suite is solid, then so is the service.

--

## Deliver
+ Something up in weeks
+ Gets better over time
+ Hardest part is staff training
+ Invest in your Ops team

{% if include.pres %}Note: {% endif %}
I don't know if it was Andy Hertzfeld or Steve Jobs who said "real artists ship", but I like the sentiment.
It's possible to get lost in the ever-changing flux of the Cloud hosting world, or over-elaborate a solution that really just needs as single t2.micro with a MySQL DB.
Instead, building up a production container hosting environment is about pragmatism.
Start small, start secure and iterate.

Of all the issues here, staff training is the hardest.
~Bottom or~ Cloud is not a weekend retreat.
The skills an operations team needs to manage a cloud of servers are not exactly the same as those required to manage a room of servers.
I don't believe good engineering skills ever go out of fashion, but the days of command-line hacks and click-and-tick web interfaces are numbered.
Cloud provisioning is a shot-in-the-arm for an ops team.

It's worth investing in, either by giving that team the time they need to experiment and learn about the Cloud, or fast-tracking their progress by bringing someone in to work with them.

--

## Help

{% if include.pres %}Note: {% endif %}
If you'd like help organising and preparing your digital strategy, working with your team to foster a data-driven culture, or just hands-on-keyboard training in infrastructure-as-code, please [get in touch](/contact).

