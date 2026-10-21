---
layout: single
title: Positive Futures for AI - 4. A thousand typewriters
description: Getting the best out of AI today is less about asking better questions and more about a feedback loop of context, goal, measure and improve, run many times in parallel.
permalink: /tech/2026/positive-futures-ai-part4-a-thousand-typewriters/
tags: front tech ai future
toc: false
header:
    overlay_image: /assets/images/ai_thousand_typewriters_vhtr_1920x.jpg
    small_image: /assets/images/ai_thousand_typewriters_vhtr_640x.jpg
    og_video: https://www.youtube.com/v/bnIZFcde-QQ/
---

{% include video id="bnIZFcde-QQ" provider="youtube" %}

Right now, before the intelligence of AI rises to the level that deserves the "super intelligence" moniker, getting the best out of it doesn't necessarily mean asking better questions.
For me, the results that have been most useful professionally have come from setting up a feedback cycle: context, goal, measure, improve, run many times in parallel.

## Monkeys and typewriters

The old idea goes that a thousand monkeys at a thousand typewriters will eventually produce the complete works of Shakespeare.
A small amount of intelligence, given a very long time, can do astonishing things.
Today's AI models are far more capable than a macaque, and it may not be long before they outstrip you and me.
The more useful question is how to set them up so that whatever intelligence they have produces meaningful outcomes, knowing that the intelligence itself keeps improving.

## The cycle

* **Context.** Give the model rich information about what it is doing and the environment it is working in.
* **Goal.** Be very specific about what you want it to achieve.
* **Measure.** Assess how well it did. This is the hard part with monkeys: you would have to read an awful lot of scripts to find out they are garbage. With an automated way to assess the output, you have a much better chance.
* **Improve.** Feed that assessment back in, and repeat.

{% include svg.html svg="/assets/svg/ai-agent-loop.svg" png="/assets/svg/ai-agent-loop.png" caption="The loop: context, a job to do, a measure of how well it went, then round again with many agents at once." %}

Run that loop across many agents in parallel, not one agent going round and round, and the results get exciting.

## Two examples

I gave an AI model a difficult mission: trade the stock market.
It struggled for a long time, but over a few months it built [River](https://www.riverbrief.com/en?utm_source=blog&utm_medium=referral&utm_campaign=fv-2026-10&utm_content=founder-blog), which takes in the news, aggregates it, looks for patterns that might move stocks and shares, and produces predictions from them.

I also asked about efficient nuclear reactors with passive safety features.
It came up with a design for a [high temperature, helium cooled reactor](https://github.com/cleverlight/mistergy) that turns itself off if something goes wrong, which could help produce cheap, carbon free energy.
This is one of its drawings.

{% include svg.html svg="/assets/svg/vhtr-exploded-isometric-cutaway.svg" png="/assets/svg/vhtr-exploded-isometric-cutaway.png" caption="An exploded isometric cutaway of the 20 metre VHTR unit, from the mistergy design set." %}

## Single shots and loops

When I ask for a single answer, I get the model as it is today, which is a long way beyond the monkey and maybe beyond me, and it does very well.
The best results have come from putting it in the loop: give it a mission, assess the result, feed that back, and repeat, with thousands of agents rather than one.

Whatever you apply AI to, I think this is a useful way to think about it.
If you are working on something like this, or have ideas for future videos in the series, let me know on [the LinkedIn post](https://www.linkedin.com/posts/alexstanhope_ai-si-didaristotleknoweverything-activity-7513463414892085250-tOVA).

### Series

+ [Part 1: Understand it](/tech/2023/positive-futures-ai-part1-understand-it/)
+ [Part 2: Train](/tech/2023/positive-futures-ai-part2-train/)
+ [Part 3: Context](/tech/2025/positive-futures-ai-part3-context/)
+ Part 4: A thousand typewriters (this post)
