
## Migrate-train-run repeat
* Begins with audit
* Cloud migration
* New operational processes
* Role of training

{% if include.pres %}Note: {% endif %}
IT is full of new things.
The unending stream of 'new' can be both seductive and distracting.
Once code is cut, or a server is installed, it needs updating. 
Major releases often package up larger quanta of change, so require a managed migration and training.
When I ran an IT team, I felt like we were constantly in a migrate-train-run cycle.

Cloud is still new enough to be fuelling the current cycle.
Many firms are migrating their physical servers, or entire data centres, to the Cloud.
Cloud brings with it a different philosophy, one where servers persist for hours or days but typically not months.
Coupled with changes in application architecture, which are splitting monoliths into dozens of microservices, the numbers of server instances (or more likely containers) are exploding.
The management surface is getting bigger, which is stretching Operations teams.

![Migrate-train-run cycle visualisation]({{ "/assets/images/migratetrain-swirl-82850_640x.png" | absolute_url }})

Thankfully new tools are allowing us to make giant leaps forward in automation and process efficiency, but adopting those well requires training to upskill the teams that use them.
Coding techniques that originated in software engineering are becoming more popular in infrastructure engineering:

* Infrastructure-as-code allow us to manage herds of servers like cattle.
* Regression test suites identify newly created problems and give us the confidence to refactor old code.
* Dynamic service and application performance monitoring help us keep track of what's happening in real-time.
* Rolling updates, canary deployment and load rebalancing mean we can operate an always-on service.

---

## Breaking out
* Twas ever thus
* Reduce wastage
* Caused by VUCA

{% if include.pres %}Note: {% endif %}
This migrate-train-run cycle isn't new.
What makes IT exciting is that these paradigm shifts happen at a much higher cadence than in other sectors.
Because they are so frequently occurring, the challenge facing IT teams is to get better at the migrate-train-run cycle; not just to perform a single iteration efficiently, but instead to adopt and hone strategic practices to make every cycle as lean and performant as it can be.
As I've written about before, Volatility, Uncertainty, Complexity and Ambiguity (VUCA) exist in practically every modern workplace.  Managing those environments well requires organisation.
VUCA means we don't see 20 years worth of IT migrate-train-run cycles ahead of time. 
In fact, we may only have a clear view of the next 3-18 months, depending on the age and scale of the organisation.

In spite of that looming horizon, there are ways organisations of all sizes can cope better with the cycle, specifically in three areas:
1. planning and architecture
2. vendor and technology selection
3. technical approach to development and operations management

---

## Avoid
* Avoid vendor lock-in
* Derisk with proofs of concept
* Log technical debt

{% if include.pres %}Note: {% endif %}
Unique vendor services are convenient.  That's how they get sold into your organisation.
However they're also typically quick to adopt, so perfect when you don't know for certain that you need to own/run a service.

A proof-of-concept (POC) might seem like a tentative solution to the problem, but it's a great response to unmanaged risk.
Unique vendor services are a great way to quickly build out a solution.
Once proved by a POC, there's a much clearer business case for investing in a full production-grade service or application.

Tech-debt is inevitable: none is worse than too much.
Where you choose to cut corners, abstract using loosely-coupled wrappers, so you can remediate the tech debt in the future.

---

## Adopt
* Sound architecture for roadmap
* Purchase well-competed commodities
* Invest in code

{% if include.pres %}Note: {% endif %}
Architecture is more important as projects get bigger.
The architecture of your service or application *roadmap* is critical.
It's one thing to cut corners now, but shoot for an evolutionary architecture that means you've got a clear long-term view of what good looks like.

I have an old pair of headphones that I don't want to send to landfill.
Sadly spares are only made by a single manufacturer, which drives up the cost.
The vendor lock-in I experience with my headphones informs my making a different choice with my Cloud strategy.

Many clouds have bespoke or highly customised service offerings, which if used with care can make for some early quick-wins.
However, those same services tend to standardise over time.
If possible, choose commoditised services where healthy competition will ensure that prices remain low.
Aim to roll out containers into a managed Kubernetes cluster, or provision generic object storage or elastic compute instances.
Customise and configure those services with standardised multi-platform or cross-platform tooling.

Above all, code.  Where services are provisioned using code, they will implicitly be easier to swap out in the future, even if you're forced to adopt single vendor-specific solutions for now.
That infrastructure-as-code (IAC) encodes the complexity so that almost all requirements and dependencies are clearly captured.
Two years down the road when there are better alternatives available - and history shows us that if you've paid much for anything, there will be better alternatives in time - you'll be able to migrate more easily, perhaps even automatically.

---

## Why code now?
* Repeatable
* Reliable
* Resilient
* Secure
* Dev-like-live

{% if include.pres %}Note: {% endif %}
IAC is not just a means of managing future risk; it delivers benefits now too.
IAC translates to more reliable, secure and efficient service delivery.
It also has ramifications for software development too, such as improved quality and reduced cost of those inevitable and pesky bugs.

---

## Why code for the future?
* Verifiable
* Well-specified
* Often portable

{% if include.pres %}Note: {% endif %}
Today's code is tomorrow's legacy.
None of knows what the future holds precisely, but we can predict the impact of the legacy code and service platform that we'll carry into it.

We do know there'll be data and those who would seek to steal or otherwise exploit it.
We do know there'll be newly discovered security flaws that we'll need to protect ourselves against.
We do know there'll be bugs and misconfigurations that we've introduced already, which only become apparent in time.
And because we know these things, we can plan for them.

IAC means that when there's a data breach, you can isolate its scope and minimise the impact on your users.
IAC means that when there's another Heartbleed, Shellshock or POODLE, you can assess your exposure by simply analysing that code, often just a search-and-replace.
IAC means that when you track down a misconfiguration, especially something systemic, you can fix not only that one but all occurrences of the problem.

New tools will arrive, new technologies that we haven't yet dreamed of will become prosaic.
When they do, history again intimates that we might be able to re-use our existing IAC, or trivially transcode it.
IAC today saves time and money tomorrow.

> It matters less the specific language you code it in or tool you adopt.  It matters that you manage the problem with code.

---

## DevOps culture
* Training is the key
* On-site, at desk, in-situ
* Real environments, real challenges

{% if include.pres %}Note: {% endif %}
So the business case for IAC is pretty water-tight, but I've skirted the main reason we're not all doing it yet: skills.
Learning a new language, or adopting a new tool is hard.
It often requires outside help.
Not a lot of it, but some.
As the outside help, I see a lot of companies stuck with imperfect processes and enthusiastic teams without the time or headspace to improve them.

The frustration is that I know it only takes one day to get started with IAC, then from there it's a progressive and self-driven learning journey that culminates in a fully-managed infrastructure-as-code.
Increasingly the vast open information resource that is our Internet means that almost everything you need to grow and flourish is out there, it's just hard to get started.

---

## Help available

{% if include.pres %}Note: {% endif %}
Lightenna helps you get started.  We offer a 1-day training course in IAC to help traditional operations teams get started with IAC.
If you need help implementing - and deriving tangible business benefits from - anything described here, please [get in touch](/contact).
