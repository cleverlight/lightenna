
## Your service
* Scale
* Value

{% if include.pres %}Note: {% endif %}Websites vary hugely in scale and aspiration.  One might offer basic product information and contact details to an audience of a few dozen, another may process thousands of page requests each second. 

Value is a completely independent axis.  Those few dozen customers may represent 90% of the revenue to a boutique business, whereas high-traffic advertising-driven sites may value their users in fractions of a cent.  The common element is the web service itself.

Each of these web services has a value to the organisation that owns it.  They're both figuratively and literally invested in its success.

If you're reading this, chances are that you have some kind of stake in some kind of web service.

---

## What you call it
* Software
* Server
* Somewhere
* Someone

{% if include.pres %}Note: {% endif %}I'm using the term 'web service' to describe this group of disparate web properties because whether whatever it does, there is some _software_ that sits on a _server_, _somewhere_ and it delivers a _service_ to _someone_. 

---

## What's it worth?
* Why price it
* Audit

{% if include.pres %}Note: {% endif %}Understanding that value is itself important.  If you're making or seeking investment to grow your business, most future investment will seek to understand the present valuation.  If you want to sell it, or buy another one, that transaction needs a price.

Similarly if your company is about to refresh the web service, it helps to think about that as an explicit investment to yield a return.  The return may be indirect or non-financial, but quantifying and measuring the value is essential.

I've been doing some web audit work again recently and I wanted to share some of the patterns I've seen repeatedly and what businesses can do to maximise the value of their web services, irrespective of how they intend to seek it.

--- 

## Assessment
* Func and non-func
* Userbase
* People and processes
* (Also software)

{% if include.pres %}Note: {% endif %}What the web service does is an important part of its value, but it's the non-functional properties that create value.

Things like the reach of the service, it's presence in search engines, the profile of user interactions

How it was built is almost as important as its current functionality.  Think about the people who built the service, the knowledge they gleaned during development and the processes they adopted to run it.  How much of this is written down in an accessible way versus stored only in someone's head.  What if they leave?

---

## Questions
* Performance
* Security
* Compliance
* Extensibility
* Robustness

{% if include.pres %}Note: {% endif %}How well is it going to perform in production?  How likely is it to get hacked and what would that cost the business?  Does it conform the legislation like GDPR?  Can it be maintained and handle failures?  These are the

### Evidence, not hand-waving
It's quite easy to answer some of these questions with hand waving, but the challenge is to provide *evidence*.  The web audit process is really just about assembling that evidence and identifying short-falls.

---

## Future
* Proving the future
* Experience
* Shortcomings are good
* Tech debt

{% if include.pres %}Note: {% endif %}How can we prove that this system is going to extensible in the future?  The best evidence is a design that's based on reuse and refactoring.  Philosopically, the only methodology I've ever seen work efficiently, at scale and over a sustained time period is test and learn: stop throwing things away; never start again from scratch.  Iterate.

If the team can demonstrate that they've done something before, great.  If not, can they prove that they're robustly following a development methodology that's worked for other teams in similar situations before?

The best audit yields a shopping-list of stuff that's:
* not been thought about yet/designed
* not been done
* been only partly done
* been done deliberately badly

Every web service has technical debt.  It's a consequence of expedient decision-making and it's fundamentally a good thing, if managed.

Technical debt for a web service tends to take the form of development work that _could_ have been done before, but wasn't because other things were prioritised.  It's actually really healthy but you might ask why.  The answer is risk (but that'll be another blog post).

---

## Free
* Audit checklist
* Open-source

{% if include.pres %}Note: {% endif %}The web audit process doesn't have to be intimidating.  We publish a [free list of questions to inform your audit](/tech/2018/web-service-review-and-cloud-audit/).  They're free and open-source so please use them however you'd like.

The aim of the questions is to help teams think around a web service, not just about what it does.

> If you'd like help with a web service that you're looking to grow, Lightenna can complete a web audit on-site, typically within 1-3 days.  If you'd like to talk about that, please [get in touch](/contact/).

