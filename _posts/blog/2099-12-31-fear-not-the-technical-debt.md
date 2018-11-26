---
layout: single
title: Fear not the technical debt
description: Tech debt is great, if managed. 
tags: front tech consulting
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

Technical debt sounds terrifying but it's a natural consequence of healthy, business-led technology development.

---

### What is it?
* Everything you should have done,
* Couldn't do or
* Couldn't afford to do earlier

{% if include.pres %}Note: {% endif %}Technical debt (tech debt) is the sum total of all the technical tasks that either _need_ to be completed, or _should_ be completed before an app/web site/web service goes live.
There are many different descriptions of live, but I'm talking about the full production mode of the app after it's been through alpha and beta test stages.

---

### Examples
+ IAC
+ Documentation
+ API formalisation
+ No frameworks

{% if include.pres %}Note: {% endif %}Depending on the scale of the app and the skills of the team working on it, often it seems faster to set up infrastructure by hand rather than write it as infrastructure-as-code.  But before you plunge headlong into production operation, it's worth catching the infrastructure up.

#### Need a new environment
That might be because you will need another production-like environment to:
* conduct some new feature testing
* test the impact of upgrading dependencies
* shift-left your prod environment to increase the accuracy of regression testing
* improve the quality of code being cut by giving developers a live-like environment
* manage a transition to a new platform or cloud
* give access to an auditor, security penetration tester

#### You didn't document anything
At some point a developer sage said "the code is self-documenting" and everyone on the dev team agreed, so nobody wrote anything to explain how it works.

No one likes writing documentation, but a certain amount of it is essential, no matter how well crafted the code is.  It's worth writing a high-level design (or HLD) document retrospectively if one doesn't exist already.
Looking at the project from 30,000 feet, the HLD should guide the uninformed observer through all aspects of the technology contained within or linked to this app.
There doesn't need to be any duplication, so a well-written HLD should link through to the code for more information.  And then, yes, the code should be self-documenting to clearly explain _how_ it works.

#### Components connect by magic
APIs are great.  Formalising the interface between different components means that they can be developed independently and readily decoupled.  Loose coupling means those same components could be reused, or more likely swapped out because:
1. stuff changes
2. no one can predict how it's going to change, accurately, all of the time
3. the (better if refactored) replacement just has to deliver the interface contract, ideally specified as tests.

#### Everything is bespoke
Open source is a transformative tool if well-deployed.
While it does take additional time in the beginning, it's usually worth it to:
* understand the elements of your solution that you share in common with hundreds or perhaps thousands of other dev teams
* research relevant frameworks
* design integrations between distinct open-source components
* curb your architecture to fit with community design patterns and practices
* learn about each framework and deal with the inevitable issues of customisation

The alternative is to code everything in-house.
That's often hugely attractive to inexperienced dev teams, but becomes less attractive when the volume of code maintained by the team grows while headcount remains the same.
Developers are spending more time debugging, maintaining, securing and extending existing code.

Over-reliance on frameworks and under-reliance on frameworks can both be different types of tech debt.
The goal is to tread a pragmatic line:
* try not to invent things that already exist elsewhere
* use community frameworks to prompt 'standards' discussions within the team
* embrace the disciplines that make large open source projects work

---

### More examples
+ Scalability
+ Unmaintainable code
+ High availability, DR
+ Tests
+ Access to production

{% if include.pres %}Note: {% endif %}Tech debt rears it's head in many guises.  Here are some more examples of the kind of things that can hide in web projects.

#### It won't scale
If you design a solution to be infinitely scalable, it will probably take longer to build that it needed to.
Even if you're absolutely certain it's going to need to meet that scale, it's still sensible to build a smaller, leaner iteration before jumping right in.
Agile says when building a sportscar, that you should build a wheel, then a skateboard, then a buggy, then a compact, then eventually evolve it right the way through to your target sportscar.
This approach helps identify unknowns early, before the design becomes too intransigent to change.

If you've taken an agile approach then hopefully you've deliberately accrued some tech debt around scalability.

#### It's a monolith
When building a solution, it's typically _slightly_ to build it as a single large program.
Now quickly this becomes untrue, and purists would argue that it is actually faster to design and build microservices from the start, but judging by how many teams have built monoliths I'd argue that unless prompted, that tends to be how big projects go.
When faced with a monolith, it becomes very difficult to maintain and support that code:
* Maintenance releases typically require downtime.
* Parallel running instances of the codebase create concurrency issues.
* Pinch points accumulate around data write operations.
* Business domains get conflated into single codebases and lose flexibility.

The solution is to build out microservices whose high-level designs follow that of the business or organisation they serve.
Splitting a large monolithic codebase into microservices can be a particularly tricky remediation activity.
This can be a particularly toxic form of tech debt because it's so costly to sort it out later.

#### If anything fails, it all fails
It takes time to go back and swap out those single instances for managed clusters (horizontal scaling) and more time to ensure that there's no scenario where an elaborate combination of failures means that you lose data.
Investing that time too early is wasteful, so it's worth accumulating some technical debt, because it's going to be remediated later... just so long as you do actually remediate it later!
Coding for failure is another area where it's best not to accumulate the debt in the first place, because fixing it retrospectively is tough.

#### You didn't do TDD
There are robust development methodologies that should make it impossible, but sometimes unit and integration tests are:
* functionally incomplete
* missing key areas of the sites functionality
* don't cover all the code
* haven't been kept up-to-date as the product has evolved

#### Nothing's in production yet
If sprint 0 is about setting the team up, sprint #1 is entirely about getting to production.
Sadly it's sprint 26 and while your alpha testing has gone really well and you've got some great user feedback, you've nothing in production.
I see it over and over again that teams leave production to later, or worse expect to hurl the code over the wall to an operations team who "look after live".

> You build it, you run it.

I'm a firm believer that having an app in production as early as possible is a great discipline for a team.
If you can get into a regular release cadence, that empowers everyone in the team to embrace the DevOps methodology that sees Development and Operations collaborating right through the software development lifecycle, you're going to go far.

---

### Why does it accrue?
* Foresight is 0/20
* Risk management

{% if include.pres %}Note: {% endif %}While each of us can make an informed guess of what will happen in some areas of technology, in the short to medium term, no one can tell you in detail what's going to happen next year.
Knowing the limitations of that crystal-ball gazing is empowering.

#### Manage risks not predictions
Project teams deal with this 0/20 foresight using risk management.
Because we can't know the future, we have to:
* build for the present
* build for what we know now
* build to test and learn

#### Derisk early and often
Technical debt is a natural artifact of risk management.  We cut corners now, because we only know about now.
While we might be able to make an informed guess about the future, investing significant development time on features or functionality that might never see the light of day is a sure way to waste money and shorten the runway.
The key principal of deliberately accruing tech debt is that we _will_ return to a feature in the future, but ideally when we completely understand its requirements: what we need versus what we'd like.

### When should it be remediated?
* Never
* Right away
* When it becomes the next blocker
* Risk vs reward

{% if include.pres %}Note: {% endif %}Knowing when to remediate that tech debt comes down to an informed understanding of the gap between what we have now and what we need.
Suprisingly often, the answer is never.
If we cut corner or created a partial implementation of a feature, but later discover that the feature is not important, or less used that we'd hoped, that we can dump the feature and dump all the tech debt attached to it.
No one likes throwing code away, but it's a much nice feeling discarding or writing off effort when it's a bit of proof-of-concept work, rather than an expensive over-engineered, production-grade solution.

Similarly sometimes the tech debt should be dealt with immediately.
I encourage teams to always keep tests up-to-date and ensure appropriate coverage for unit tests.
It's a false economy "just hacking something fast" because bugs cost more the later they're discovered.
Tests first and tests always, unless of course you want a low quality product, in which case let your test suite go.  Just don't imagine that you can 'inspect' quality back into the product later.  Bad source code is just bad source code, unless you've got tests that prove it's good enough.

If there is a 'right' time to remediate, it's usually driven by a need.
Typically the cost of developing a feature drops, but beyond a certain point, the cost starts rising again.
But beware: those increasing costs are often hidden!
If you half-ass your disaster recovery work, you'll find out how expensive that tech debt can be when something goes wrong.

---

### How much of it should we carry?
* Indicators
* Too much
* Too little

{% if include.pres %}Note: {% endif %}It's impossible to say how much is right, but there are some good indicators that you're carrying too much or too little.

#### Too much
If progress against deliverables is slow, often that's caused by unremediated tech debt.
If your developers are not spending time coding afresh, but debugging then you've probably not had sufficiently robust automated test procedures in the past, or scant unit testing.
If your developers are spending too much time coding, then that could be caused by re-building the wheel, when a common framework might save time and nugatory effort.

If your dev team are complaining about the amount of tech debt (or 'hacks') in the solution, it's usually time to review it.
Perfectionist programmers - I've been guilty of this - tend to bemoan anything that isn't quite right.
The solution isn't to down tools and concentrate only on the debt, but perhaps to instigate some kind of progressive improvement process.
Teams can dedicate a certain number of hours/week to fixing, refactoring or sorting out the debt properly.

#### Too little
If your product owner (PO) is complaining about poor progress against features, the answer may be to deliberately accumulate more tech debt.
Again this approach is beset on all sides by precarious risks.
Delaying tech tasks that the PO doesn't care about might seem like a good way of racing forward, but it's important to be clear that by taking short-cuts we're really borrowing from future capacity rather that creating more capacity.

---

### How do we know what we've got
+ Get us in
+ Use our free web audit toolkit
+ Peer behind the curtain

{% if include.pres %}Note: {% endif %}Well you get Lightenna in for a couple of days to do a web audit for you!

Or use our free [web audit framework](/tech/2018/web-service-review-and-cloud-audit/) to conduct your own audit,
but seriously the best way to tackle the problems associated with tech debt is to understand it and manage it explicitly.
There's no reason to fear it, unless you can't quantify it or recognise the consequences of carrying it.
Like every good horror movie director knows, you're much more afraid of that which you can't see.
