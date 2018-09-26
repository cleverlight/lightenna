---
layout: single
title: Sympathy for the devil (or his legacy anyway)
description: Legacy systems (of any type) pervade almost every one of our roles, yet they are pretty universally hated.  What can we do for our tomorrow-selves to break the circle? 
tags: front consulting
toc: true
header:
    overlay_image: /assets/images/sympathy-for-legacy_00901_1920x.png
    small_image: /assets/images/sympathy-for-legacy_00901_640x.png
---

In 1994 a fantastic trailer rocked cinemas across the UK.  Brad Pitt and Tom Cruise were playing vampires to the Rolling Stones' soundtrack in Neil Jordan's [Interview with the Vampire](https://en.wikipedia.org/wiki/Interview_with_the_Vampire_(film)).
Sadly the film that followed didn't quite live up to the hype (good, but not great with ['clumsy castings'](https://www.rottentomatoes.com/m/interview_with_the_vampire/)) but the trailer ensured its commercial success.  The film was a sort of retrospective on its principal characters' lives, the terrible things they'd done (including en-vampiring a 10-year-old Kirsten Dunst) and what they would leave behind, if they ever died!

## Skeletons in the cupboard
If you work anywhere that's not a start-up, I'm guessing that you'll have inherited some kind of legacy.  Chances are that you'll be taking responsibility for something that you didn't originate, design or even contribute to.
It might be a product line, an accounting system, a contract or business process.  In technical teams, it's often a codebase.  Even where you're working on a greenfield project, there's typically something similar that came before.

## Talking legacy
I'm fascinated by the way teams talk about legacy.  Often it's sh**: it's poorly designed, horribly implemented and consequently doomed to a short-and-soon-to-be-replaced life.  It's performance has been disappointing. 
It's flaws - exposed over many many months and too numerous to count - now cast a dubious shadow over the people that created them.

Jump back in time - because you can do that in films - and you'd find a strong team of bright, committed individuals working hard to produce that code/thing/system.  So where does it all go wrong?

## 1. It's not that bad
Human nature, but inheriting teams often under-estimate the quality of the legacy system.  They focus on the bad bits and gloss over the success the old thing represents.  It too was built in an environment rife with [VUCA](/tech/2018/cost-of-collaboration/) and on some level it did its job.  At the very least, it brought the team to this elevated position where they can now look back (and often down) on it.

## 2. It's known
While deeply flawed, the old system is understood.  The technical aspects of it are fairly familiar, but more importantly the human interactions with it are known.  It took time and effort for lots of people to understand and interact with the old system.  Similarly the new system is unknown.  Its use will necessitate a whole bunch of people who currently don't understand it to learn about it, well before they concede that it's even as good as its predecessor!

## 3. High on hope
Hope that the new system will be better can lead teams to do some crazy things.  That craziness probably fuelled the previous team that produced the legacy system.  At best that ambition motivates and launches teams off the deep-end with a complete rebuild, at worst it sends them to their doom.  Pragmatism: know that no matter what you produce, in a few years time your successors will feel about it as you feel about the legacy system now.

## Iterate, don't reinvent
No matter how hated the legacy system, no matter how bleak the outlook for its continued use, resist-resist-resist the urge to chuck it out.  If it was _so_ poorly designed that all of its components are _so_ tightly coupled that there's absolutely no way to pull it apart, then I guess it's curtains, but there's almost always a way to selectively rebuild part of it.

## Parts are more than the whole
Those parts have known, defined interfaces.  If you replace the part with a common interface, or evolve the interface in a forwards-compatible way, then the whole carries on functioning.  All the actors who interact with it can adapt slowly, when nourished by the familiarity of the bits of the old system that haven't been replaced.

## Avoid the blockers
There are a couple of things that can undermine this evolutionary approach, and managing them during any project is for me the top priority:
1. The knowledge is gone - no one understands the old system, we can't do anything with it.
    + Invest in documentation.
    + Comprehension test the documentation in the same way you functionally test the system itself.
2. We don't own it - the IP for the old system is owned by someone else.
    + If you work with external vendors, make sure that you have clarity on how you're going to take ownership of what they're building.  Make sure the architects are thinking about how to decouple, extend, refactor and turn off anything, before you turn it on.
3. It's a monolith - the old system doesn't decompose into pieces because everything depends on everything else.
    + Build in pieces.  Microservices are in vogue now, as SOA and OO design were before.  It's always been possible to build loosely-coupled systems.  It's always been harder, which is why there are so few of them, but always worth it. 

## Enjoy the trailer, but read the book
When the next salesman is selling you the trailer version of the _new_ system, do your future-self a favour, or the person they promote into your role after you: think legacy.
