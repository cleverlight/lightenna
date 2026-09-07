---
layout: single
title: Positive Futures for AI - 4. Document
description: "Moving from chats to useful work means getting AI to do more than relate to us: it's got to understand, process and improve documents"
permalink: /tech/2026/positive-futures-ai-part4-document/
tags: front tech ai future
toc: true
published: false
header:
    overlay_image: /assets/images/techupdate_25318_1920x.jpg
    small_image: /assets/images/techupdate_25318_640x.jpg
---

<!-- ===================================================================
     SHOOTING SCRIPT + POST. One file, both jobs.
       plain bullets = beats, say them your way
       > blockquote  = land this line as written
       paragraphs    = for the reader, not for the camera
       <!- comments -> = screen cues and timings, hidden when published
     Target 11:00. Argument: every step of the loop makes the work
     better and harder to see. By step 4 you've lost the thread.
     NoteThink is how you get it back.
     TODO on upload: og_video in front matter, video include below,
     then remove published:false.
     Preview while drafting: bundle exec jekyll serve --unpublished
     =================================================================== -->

### Twelve agents, one board

<!-- 0:50 · SCREEN: NoteThink kanban FULL SCREEN. Same view returns at the close. -->

+ This is what I'm working on this morning
    + Twelve agents, six projects, one screen
    + None of them is hacking HuggingFace
+ Come back to this board at the end
+ These projects are not all apps

<!-- IMG when captured: notethink_board_open_640x.jpg -->

<!-- SCREEN: VHTR cutaway -->

+ A very high temperature reactor
    + Helium-cooled, walk-away safe, open source
    + I have no background in nuclear physics

<!-- SCREEN: Riverbrief -->

+ Same method, different field
    + 200 news sources, read in real-time
+ Four things got me from a chat window to that board
    + Each one made the work better
    + Each one made it harder to see

I've spent the last year working out how to get useful work out of AI rather than interesting conversations.
The board above is where that ended up.
Behind it sit about a dozen agents running across six to ten projects.
One of them is a design for a very high temperature nuclear reactor, which is a reasonable thing to be sceptical about, because I have no background in nuclear physics whatsoever.
Another reads a couple of hundred news sources in real-time and works out what's likely to move in which market.

Neither of those projects is really the point.
The board is the point.
Getting to the stage where I needed a board at all turned out to be the interesting part, and that's what this article is about.

### The loop

<!-- 0:40 · SCREEN: the diagram, full screen. Corner step marker 1-4 from here on. -->

+ Give them context
+ Give them a job to do
+ Measure how well they do it
+ Repeat, with lots of them working in parallel

{% include svg.html svg="/assets/svg/ai-agent-loop.svg" png="/assets/svg/ai-agent-loop.png" caption="The loop: context, a job to do, a measure of how well it went &mdash; then round again, with many agents at once." %}

+ Four steps, and I'll count them off
+ Watch what happens to how much I can see

Working with AI agents comes down to four things for me.
Give them context, so they know what they're working on.
Give them a job, so they know what finished looks like.
Measure how well they did it, using something that isn't the agent.
Then go round again, with as many of them running at once as I can manage.

Most of what's written about AI stops after the first two steps.
The third is where the value actually is.
The fourth is where the trouble starts, and it's worth watching what happens to my visibility of the work as each step gets added.

### 1. Give them context

<!-- 1:30 · SCREEN: Claude web → pre-staged file → desktop → folder → HOLD trust dialog → pre-baked result -->

+ Single web chat
    + "How does helium cool a nuclear reaction?"
    + Genuinely useful, genuinely educational
    + Abstract and disconnected
    + Knows everything about the world, nothing about my work
+ Upload one file
    + "What opportunities existed in this hour?"
    + A decent answer from a cold file
    + But I could have read it myself in twenty minutes
+ Point it at a folder instead
    + Same tool, running on my machine
    + One difference that matters: it sees a folder

A single web chat is where most people start, and it's genuinely useful.
Asking how helium cools a nuclear reaction taught me a great deal, and it's how I got going on that project in the first place.
But a chat is abstract and disconnected.
It knows everything about the world and nothing at all about my work.

Uploading a file closes some of that gap.
The models are good enough now to make something worthwhile out of a single cold document, and the answers are perfectly reasonable.
The trouble is that one file is one file.
If I can read it myself in twenty minutes, I haven't gained very much by asking a machine to do it.

The step that matters is moving from a file to a folder.
It's the same tool, but running on my own machine instead of in a browser tab, and it can see a whole directory rather than whatever I've bothered to upload.

<!-- HOLD HERE. Don't click through. This is the security beat. -->

+ The trust dialog is the easiest thing in the world to click past
    + Inside this folder, it reads and changes anything
    + Outside it, nothing

At the moment you grant that access, you get asked whether you trust the workspace, and it's the easiest dialog in the world to click straight past.
It shouldn't be.
What you're doing is drawing a boundary: inside that folder the agent can read and change anything it likes, and outside it, nothing.
That boundary is the single most important decision in this whole article.

> The folder is the sandbox. Pick it on purpose.

+ Now ask the question that was too big before
    + "What opportunities recur across everything in here?"
    + Three months of files, several hundred documents
+ A million tokens is roughly 800,000 words
    + The complete works of Shakespeare
    + [Part 3](/tech/2025/positive-futures-ai-part3-context/) was about that number
    + This is about filling it with my own material
+ Not a job I'd have done faster
    + A job I'd never have started

With a folder attached, I can ask the question that was too big before, and look for patterns that recur across three months of analysis rather than a single hour of it.
A million-token context window holds roughly 800,000 words, which is about the complete works of Shakespeare.
[Part 3](/tech/2025/positive-futures-ai-part3-context/) was about that number getting large.
This part is about filling it with my own material instead of the world's.

That distinction matters more than it sounds.
Reading several hundred documents and looking for repeated patterns isn't a job I would have done faster with help.
It's a job I would never have started.

> I can't read what it read.

### 2. Give them a job to do

<!-- 0:50 · SCREEN: loop step 2, then a real todo.md with acceptance criteria -->

+ Context on its own is a library card
+ A prompt is a question you ask once
+ A job is a definition of done that outlives the session
+ Most of my time goes here now
    + Not writing prompts
    + Writing down what finished looks like

Context on its own is just a bigger library card.
The agent also needs a job, and a job is not the same thing as a prompt.
A prompt is a question you ask once and then throw away.
A job is a definition of done that outlives the session it was written in, so the next agent to pick the work up inherits the same standard.

This is where most of my time goes now.
I write far fewer prompts than I did a year ago, and far more descriptions of what finished looks like.
Those descriptions live in the repository as ordinary markdown, alongside the work itself, which means they're versioned and they accumulate.

> I can't watch it work.

### 3. Measure how well they do it

<!-- 1:30 · SCREEN: loop step 3 → CODING_STANDARDS.md → run /prod-ready → SHOW IT FAIL -->

+ If the only thing judging the agent is the agent, you have a machine for generating confident nonsense
+ You need a grader that isn't the model
+ Standing instructions, built up over months
    + When it gets something wrong in a way that will recur, don't correct it
    + Write it down, so the correction outlives the conversation
+ One automatic check
    + Lint, coding standards, unit tests, browser tests
    + Deterministic and boring
    + The only reason I trust any of the rest of it

This is the step almost nobody demonstrates, and it's the one that makes the difference.
If the only thing judging the agent's work is the agent, what you've built is a machine for generating confident nonsense.
You need a grader that isn't the model.

Two things do that job for me.
The first is a set of standing instructions that I've built up over months.
When an agent gets something wrong in a way that's going to recur, I don't correct it in the chat; I write the correction down in the repository so it outlives the conversation.
Over time those files become the framework every future session runs inside, and they're worth far more than any individual prompt.

The second is a single automatic check that runs the linter, the coding standards, the unit tests and the browser tests.
None of that is AI.
It's deterministic, it's boring, and it's the only reason I trust anything else in this article.

<!-- Let it fail on camera. Green proves nothing to a sceptic. -->

> A red result is the point. Green proves nothing.

+ Every run writes plans, notes, a diff, a test report

A check that passes proves very little.
A check that fails proves the measurement is real, which is why a red result is worth more to me than a green one.

But notice what measuring costs.
Every run now produces a plan, a set of notes, a diff and a test report, and all of that is written down somewhere I'm supposed to read.

> I can't read what it wrote.

### 4. Repeat, in parallel

<!-- 1:20 · SCREEN: tmux tab bar, sessions flicking past → one diff, five seconds -->

+ Once the framework exists, one agent or twelve is the same work for me

Once the framework exists, running one agent and running twelve is roughly the same amount of work for me.
That's the whole argument for the fourth step.
The sessions sit side by side in a terminal, each one working on a different project, and I move between them rather than waiting on any of them.

> The chat isn't the thing I'm interested in. It's the actions the agent takes on my behalf.

+ Version control stops being optional
    + Parallel agents changing files means every change has to be visible
    + Branches keep them out of each other's way
    + You can always get back
+ Covered properly elsewhere
    + [Git for version controlled magic](/tech/2019/git-version-control-magic/)
    + [Markdown for future-proof publishing](/tech/2024/write-markdown-for-future-proof-publishing/)

At this point version control stops being a nice habit and becomes structural.
Several agents changing files at once means every change has to be visible and reversible, and branches are what keep them out of each other's way.
I've written about both [Git](/tech/2019/git-version-control-magic/) and [markdown](/tech/2024/write-markdown-for-future-proof-publishing/) before, so I won't repeat it here.

### Losing the thread

<!-- 0:20 · SCREEN: stay on tmux, let it look overwhelming. Slow down here. -->

+ Can't read what it read
+ Can't watch it work
+ Can't read what it wrote
+ Now multiply by twelve

Look at what each step of the loop cost me.
Giving an agent a folder means I can't read what it read.
Giving it a job means it works for twenty minutes without me, so I can't watch it work.
Measuring it properly means it produces plans and diffs and reports faster than I can get through them, so I can't read what it wrote.
Then the fourth step multiplies all of that by twelve.

> The real problem with AI at this point isn't quality, and it isn't cost. It's that I lost the thread.

### NoteThink

<!-- 2:20 · THE SELL. Biggest block. Everything above exists to earn this. -->
<!-- SCREEN: plain markdown file → toggle to NoteThink → kanban → scale out to many repos -->

+ So I stopped trying to read the chats
+ The agents already write everything down
    + Plans, progress, decisions
    + It's markdown, it's in the repo, it's already version controlled
+ I didn't need a new system
    + I needed to see the one I already had

So I stopped trying to read the chats.
The realisation that fixed this was that the agents already write everything down.
Every plan, every decision, every bit of progress is being recorded as markdown, in the repository, under version control, because that's how I set the work up in the first place.

I didn't need a new system.
I needed a way to see the one I already had.

<!-- IMG when captured: notethink_markdown_to_board_640x.jpg -->

+ Same file, two views
    + On the left, markdown
    + On the right, a board

> Nothing here is proprietary. Delete the tool and you've still got your notes.

+ Every agent's work as a card
    + Status, assignee, progress, checklist
    + A stuck story is obvious in two seconds
    + The chat log would take twenty minutes
+ Not one repository, dozens
    + One view across all of them

NoteThink takes those plain markdown files and renders them as boards, charts and structured documents.
The file on the left is the same file as the board on the right; there's no database and no separate copy.
That matters more than it might seem, because it means nothing is locked in.
Delete the tool tomorrow and you still have every note, in plain text, in your own repositories.

Each piece of an agent's work shows up as a card with a status, an owner, a progress figure and a checklist.
A story that's stuck is obvious in about two seconds, where reading the underlying chat log would take twenty minutes.
And it isn't limited to one repository: I run it across dozens, so a single board covers every project at once.

<!-- SCREEN: back to the opening board. Say it. -->

+ This is the board I opened with
    + Now you know what's behind each card
+ The bottleneck stopped being how much AI can do
    + It's how much I can keep track of
    + Raise that ceiling and everything else scales

+ Free and open source, a VS Code extension: [notegit.com](https://www.notegit.com/)
    + NoteGit is the workbench
    + NoteThink is the view that turns markdown into boards

+ More news this morning of AI escaping its box and hacking other sites
+ Today's challenge is monitoring and securing AI.  If you want help with that, please get in touch.


That's the board this article opened with, and now every card on it means something.

The reason I keep coming back to this is that the bottleneck moved.
It used to be how much AI could do, and for a while it was how much context I could give it.
Now it's simply how much I can keep track of.
Raise that ceiling and everything else scales behind it; leave it where it is and it doesn't matter how capable the agents get.

All of this is free and open source, and it runs as a VS Code extension: [notegit.com](https://www.notegit.com/).
NoteGit is the markdown workbench, and NoteThink is the view that turns those plain files into boards.

### Boundaries

<!-- 1:10 · SCREEN: talking head, or back to the trust dialog -->

+ One more reason to be able to see it
+ The failure mode isn't a bad answer
    + It's an agent going further than you meant it to
+ An agent that can't get what it needs inside its box will try outside it

<!-- FLAG: run-thru1 named OpenAI, "this week" and Hugging Face. Either put a
     source on screen, say "one of the big labs", or cut it. -->

+ Same questions at every scale
    + One person on a desktop, or ten thousand in an organisation
    + Where does the data go, how long is it kept, who can reach it, GDPR
+ The hard part of AI governance isn't policy
    + It's that nobody can see what the agents are doing

There's one more reason to care about being able to see this work.
The failure mode that should worry you isn't a bad answer, because a bad answer is obvious and cheap.
It's an agent going further than you meant it to.
An agent that can't get what it needs inside the box you've drawn will quite reasonably try to get it from outside, and there have been well-publicised cases of exactly that.

The questions are the same whether it's one person experimenting on a desktop or thousands of people working across a large organisation.
Where is the data going, how long is it kept, who can reach it, and what are the GDPR implications of processing it that way?
A lot of the work I do with enterprises is about answering those questions in a way that lets people get on and experiment safely.

The hard part of AI governance isn't writing the policy.
It's that nobody can see what the agents are actually doing, so there's nothing concrete for the policy to attach to.

> You can't govern what you can't see. That's the whole argument.

### What to try

<!-- 0:50 · SCREEN: NoteThink board, identical to 0:00 -->

+ Point AI at a folder, not a file
    + The jump from one document to a corpus is the biggest step up available today
+ Write down what good looks like, and check it automatically
    + Standing instructions plus one honest test beats any amount of prompt engineering
+ Then get yourself a way to see all of it
    + Because that's the wall you'll hit

+ Everything here is free or open source
+ Part 5 is about what happens when the agents start talking to each other

If you take three things from this, take these.

Point AI at a folder rather than a file, because the jump from a single document to a whole corpus is the biggest increase in usefulness available to most people today.
Write down what good looks like and get something other than the model to check it, because standing instructions plus one honest test will beat any amount of prompt engineering.
Then find yourself a way to see all of it at once, because that's the wall you'll hit next, and it arrives sooner than you'd expect.

Everything I've described here is free or open source.
Part 5 will be about what happens when the agents start talking to each other.

### Series

+ [Part 1: Understand it](/tech/2023/positive-futures-ai-part1-understand-it/)
+ [Part 2: Train](/tech/2023/positive-futures-ai-part2-train/)
+ [Part 3: Context](/tech/2025/positive-futures-ai-part3-context/)

---

<!-- ===================================================================
     PREP
       Market-analysis file open before recording, no file picker on camera
       Broad folder query pre-run, live took 2m17s
       /prod-ready primed to fail
       Identical NoteThink board at open and close, so the bookend lands
       Tics to kill: a little bit · very very · if you like · sort of ·
                     I'm not going to get into that today

     BEFORE PUBLISHING
       Remove published:false
       Add og_video to front matter and the video include at the top
       Capture the two screenshots flagged above
       2099-12-31-positive-futures-ai-4-agency.md also claims part 4;
         the close above assumes agency becomes part 5
     =================================================================== -->
