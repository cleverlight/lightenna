---
layout: single
title: Scalability trumps speed 
description: Serverless promises a world without low-level worries, but what's it like at scale?
tags: devops consulting
header:
  overlay_image: /assets/images/fly-at-scale_01542_1920x.jpg
---

At one stage I was trying to license a mainstream games engine on behalf of a Bristol-based tech company.  As part of my vendor research, I was putting together a comparison table, because [this page on Wikipedia](https://en.wikipedia.org/wiki/List_of_game_engines) didn't exist back in 2005!  The conversations got a bit testy when I asked one vendor about the basic licence fees and they replied "we'll get an NDA out to you, but basically it's a small six-figure sum."  As I wasn't exactly working on [Battlefield 2](https://en.wikipedia.org/wiki/Battlefield_2), I knew I was 'shopping in the wrong mall'.

But the idea of estimating things based on the number of figures stuck with me.  When specifying non-functional requirements (NFRs) about up-time or service reliability, we talk about 5 9s, or 99.999% which equates to about 5 minutes of downtime per year of operation.  Similarly with requests per second, orders of magnitude are a good way of short-cutting the conversation.

AWS Lambda doesn't currently offer a service-level agreement, but the company traditionally engineers its web services to maintain 100% availability.

`AWS Lambda is designed to use replication and redundancy to provide high availability for both the service itself and for the Lambda functions it operates. There are no maintenance windows or scheduled downtimes for either.`

Availability isn't the differentiator, services should just be there all the time.  It's not really about speed any more either: services should always return responses quickly.  [Akamai places the total page load time limit](https://www.akamai.com/uk/en/about/news/press/2017-press/akamai-releases-spring-2017-state-of-online-retail-performance-report.jsp) at about 2.4s, so allowing for overhead (DNS requests, HTTPS setup, network travel time) and some nested requests (only spawned after their predecessors have completed), our target's below 1-second per response. 

I'm doing some work at Sky Betting and Gaming at the moment.  They're a really interesting company to work with for a bunch of reasons, but particularly scale: at peak times their 2.6m customers place [over 350 bets per second](https://www.skybetcareers.com/uploads/article/CYA001_Annual_Report_2017_Interactive.pdf).  When you think about the complexity of striking a bet, it's not surprising some internal system components have to cope with five-figure loads each second.

Back in 2005, we talked about uniques over a month and 300k was a decent site.  If you're building a web service to cope with 2-3 requests per second, you do things like vertically scaling your application server, breaking your DB out to a small cluster.  If you're personalising shopping recommendations for 50-80 customers per second, you split your application into tiers, roll out load balancers between them and scale horizontally using pre-warmed ASGs.  If you're building an API to cope with more than 10,000 requests per second, it requires a similar quantum leap forward.

Right now I'm working on a talk on for [The JVM Thing Meetup](https://www.meetup.com/Leeds-JVMThing/).  As part of that I hope to share some infrastructure-as-code to demonstrate how AWS Lambda can be used to host a Kotlin microservice capable of processing the kind of massive loads that make SkyBet tick.  More to follow!
