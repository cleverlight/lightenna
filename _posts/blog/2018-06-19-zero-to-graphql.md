---
layout: single
title: Zero to GraphQL
description: Much-hyped and misunderstood, GraphQL isn't for everything but it might be just right for your API
tags: front
header:
    overlay_image: /assets/images/zero-to-speed_5180_1920x.jpg
---

Newphoria, the feeling of excitement and wonder that goes with your first experience of a new thing, is gripping but is it the best guide for tech choices?

### Left behind
In fast-moving sectors such as technology, the love of the new-and-shiny is complemented by the fear of being left behind with the old and out-of-date.
Old standards are deprecated and new ones reach widespread adoption.
It's a difficult landscape to navigate, but as ever solid business-driven strategy is the best guide to inform day-to-day choices.

### Why why API?
For most companies, the argument for having an API, internal or external, is to broker an agreement:

* A wants data from B,
* A wants B to do something,
* A wants to be notified when B has done something

Why have an agreement?  Value.  A is going to get something from B.  If the agreement is going to last, B should be deriving some value too.  That value proposition is crucial to the API's existance and longevity.

### Changing the contract
The API consumer may lie outside of the bounds of your organisation, or be sitting next to you, but both cases require the same discipline around testing, releasing and versioning to ensure that the system continues to work (and work well) when things change.

Changes happen.  We can and should try to minimise them but they're an inevitable part of evolving software.  The crucial thing is that we manage that change carefully to "preserve the business case underpinning that value exchange", which is a jargonesque way of saying that it everyone involved continues to get enough out of being involved to stay involved.

### Consequences
Every major change to an API requires work from all its downstream consumers.  For external APIs, that in itself is a difficult contract to broker.  If a developer has gone to the trouble of integrating with your API because they perceive some value from it, now or in the future, then that value is going to be diminished if they frequently have to invest dev time in keeping up with your API changes rather than working on new functionality: it's painful working hard to stand still!

### APIs mate for life
That resistance reduces the cadence at which you can test and iterate an API.  You're going to be stuck with those API design decisions for years!

Irrelevant of how well the API is engineered, or how robust your software development lifecycle (SDLC) is, there's going to be a perception at least (and often the stark reality) that changing your API will break stuff.

### To GraphQL or not?
Making the right decision about API design is hard.  Is it right for your organisation?

There isn't a 500-word answer to this, but after designing a few GraphQL implementations recently, I think the complexity is broadly in one area: resolvers.

### Three pieces
It's not in the response.  Whether you choose REST, RPC or GraphQL, chances are your response will just be JSON.

Similarly it's not in the request.  While it's probably worth using a client-side library to compose the GraphQL request object, it's not essential.  Much like querying Elasticsearch, consumers can simply compose-and-cURL query strings.  Yes, if you change the API (say you're moving from REST to GraphQL) then you will need to re-write these queries, but that's not a major operation if well-managed and well-messaged.

However the glue that takes a request, understands it, queries the DB and composes a response, that's the hard bit.  It doesn't have to be criminally difficult to write a resolver, but scope and ambition can spiral out of control pretty quickly, especially if you start with a really big schema.

### Good thing
It's good that the resolvers are the point where the proverbial rubber meets the road:

* Their implementation is abstracted from consumers.
* Updates and changes to the resolver do not need to affect requests or responses, which means consumers don't need to update their code.
* Resolvers can progressively evolve to become more highly functioning, performant or complex.

### First pass
When implementing GraphQL, my advice is to start with the basic stuff:

* Keep your schema fairly flat initially.  As the name suggests, GraphQL is great at delivering graphs of data, but optimising resolvers to deliver multi-level nested objects at scale is a tricky problem.  You don't want to get DOS'd on day one.
* Aggregate GraphQL APIs to create complex structures.  Microservices are at the heart of almost everything we do these days.  They're as great a design principle to apply to GraphQL services as they are to MVC monoliths.
* Think about your backing store before you publish your API.  If there's a major disconnect between the way your data is stored and the way you plan to surface it through the API, then you're creating more work for your resolvers.
* Use domain-driven design to inform the way you carve up your business processes and the entities that interact with them.  It gives you best chance of locking down your schema.  Since _some_ schema changes affect consumers - not additions because GraphQL queries are implicitly partial subsets of available attributes - be careful to minimise their impact.

As ever, if you've got questions or comments, please tweet, reply or [get in touch](/contact).

