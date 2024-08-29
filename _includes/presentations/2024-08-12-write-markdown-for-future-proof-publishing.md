
## Basic syntax
+ Based on text
+ Headings
+ Bold, italic, strike-through
+ Nested lists
+ Links

{% if include.pres %}Note: {% endif %}
Markdown is designed to annotate text in a simple way that is both human-readable and machine-readable.
It's not complicated.  Total knowledge of it is not required to get started.
In fact, with zero knowledge of markdown, you can still write a document that is readable and useful, albeit with basic formatting.

The internet is full of [excellent markdown primers](https://www.markdownguide.org/basic-syntax/) or for something more comprehensive [GitHub's GFM spec](https://github.github.com/gfm/).

---

## Simple examples

```
# Heading

## Sub-heading

* List item
  * Nested list item

Paragraph with some **bold** and *italic* text.
```

---

## Internal publishing
+ Documentation near the code
+ Version control
+ Use of markdown internally
  + and more widely
+ Create a visibility culture

{% if include.pres %}Note: {% endif %}
Markdown is a great tool for publishing documentation for an internal audience, or more widely.
It's highly searchable, readily enriched or reformatted.
It also lends itself to version control because additions and removals are easily tracked by line.
For those working on or near projects that are already stored in repositories (repos for short), Markdown is a great mechanism for annotating or explaining it.
It can provide the high-level view, or 10,000ft summary, that's hard to extract quickly from code alone.

Because all updates are versioned, it also makes it easy to keep pace with recent updates.
By looking at a diff between now and when you last looked at a project, you can quickly see what's changed.
If the documentation has been kept up to date with the code, those docs will reflect what's been updated in a project.
Organisations can use this combination of Markdown and version control to build a culture of visibility,
where staff collaborate to share what they're working on, and what they've learned.

As a simple text mark-up tool, Markdown is increasingly used in many different contexts, so investment in learning and disseminating the skills is worthwhile.
For example, Markdown can be used natively in Azure DevOps, GitHub, GitLab, JIRA, Confluence, and many other tools.
It's even the basis for chat in Microsoft Teams and Slack.

---

## For posterity

+ Separated content from display
+ Minimal formatting
  + titles
  + paragraphs
  + lists
  + emphasis
  + nesting

{% if include.pres %}Note: {% endif %}
Markdown is pure text.  There's a minimal amount of formatting information, really only enough to inform how different sections of the document relate to each other.

Nested headings allow different areas of the document to subsume others.

This presentation illustrates the approach.  It's available as both a web page (blog post) or a presentation (slide deck).
The markdown content that underpins it is identical for both.
This allows you to author once and use the information in multiple contexts, such as:

* Background information for AI prompts
* Introductory material for a training course
* Marketing material for a product launch
* Documentation for a software project
* A blog post for community engagement
* A contribution to a network of interconnected, searchable web pages to aid research.

While every group will have its own specific requirements, the basic structure of the document can be the same, itself included or referenced in other documents.

---

## GitHub README.md and other files
+ File hierarchy
+ The role of README files
+ Working copies
  + in multiple contexts
+ Relative paths

{% if include.pres %}Note: {% endif %}
At the root of the repository, the README.md file is the first thing that GitHub will display.
By convention, this is where high-level information about the project sits.

The project's repository could be checked out into a working copy in multiple situations:
* a software engineer might checkout a working copy to update the code
* an automated test suite might checkout a working copy to run multiple tests against a specific configuration
* a devops engineer might checkout a working copy as part of the build process for a read-only container image

In all these situations, the full path or URL to the working copy's files could be different:
* C:\Users\alex\Documents\GitHub\my-repo
* /home/alex/repos/git/github.com/my-repo
* /etc/puppetlabs/puppet/environments/production/my-repo
* https://www.example.com/open_filesets/my-repo

The goal when creating references is to do so in such a way that they are always accessible.

A link can point at anything but by using relative paths (relative to the current file),
links can be made resilient to the many different locations this repo will be checked out.

```
[Link to another file](./another-file.md)
```

---

## Git commit and push
+ Create branch from source
+ Repeatedly update it
  + Commit changes to branch
  + Push branch
+ Merge changes back into source
  + Direct
    + Push access
  + Indirect
    + Pull requests
    + Approvals

{% if include.pres %}Note: {% endif %}
This isn't a git tutorial as such, so please see our [Git series](https://www.lightenna.com/tech/git/) for the fundamentals.

The goal is to make code repos updatable by lots of users simultaneously.
Everything I'm advocating for here is designed to serve that end.
The key is to make sure that the code is always in a state that can be built and run.
That tends to be less of an issue when publishing documentation, notes or summaries alongside the code, but the principle still applies.

The best way to achieve that is to:
* Identify a source branch
  * This varies by organisation, but often we branch
* Branch from the right source branch
  * This is crucial, because we'll ultimately want to merge back into the same branch.
  * Merging back (accidentally) into a different source branch could bring with it unintended changes.
  * The branch we create is generally known as the `topic` or `feature` branch.
* Make a load of changes
  * This is the rinse and repeat stage.
  * It results in multiple changes, in multiple commits on the feature branch.
* Squash merge
  * This is where we take all the changes we made and merge them back into the source branch.
  * Generally we want to leave behind a single commit with all our changes, hence the squash merge,
    * but it's totally acceptable to just do a merge commit that sends all of our commits back to the source branch if that's the desired behaviour.

Sometimes organisations implement a more formal approval process.
The changes still go back to the source branch, but indirectly via a pull request.
In this an 'approver' will look over the changes before they are merged back into the source branch.
Authoring a pull request is much like authoring a commit, but it's just a bit more formal and facilitates an approval step, which is handy for information governance.

---

## Feature branching

{% include svg.html svg="/assets/svg/gitflow/gitflow-partials-1.svg" png="/assets/svg/gitflow/gitflow-partials-1.png" %}

{% if include.pres %}Note: {% endif %}
This diagram illustrates how a topic branch ('feature') might be branched from a source branch ('develop').
It also shows how the merge process works.
Merging could be implemented here directly, or indirectly via approved pull requests.

---

## GitHub pages
+ In addition to repo view
+ github.io or custom domain
+ Rendered using Jekyll
  + Static site generator
  + Theming
+ Internal or external views
  + Folder and branch linked
    + Approvals again

{% if include.pres %}Note: {% endif %}
GitHub Pages uses Jekyll, a static site generator, to turn Markdown files into a website.
That site could be made available publicly or privately,
such that only those users who can read the repository can view the website.
This works well for enterprise customers who might want to make intranet sites available only within the organisation.
They can be published on a custom domain, after verification by GitHub, or on a subdomain of github.io.

To revisit the *Approvals* discussion early, this means that the approval of a pull request can be used effectively to publish new content to the website.

So why publish a website based on Markdown sourced from GitHub over another CMS?
The answer is about lowering the technological barriers that impede, rather than prevent users from updating the website.
Many if not most companies have had content-managed websites since the mid 90s, yet surprisingly most company websites aren't frequently updated.
Often the hassle, or perceived hassle of accessing and updating the CMS means that sites don't get updated.

Git-based publishing works well in situations where the content is naturally linked with the repo.
If the repo coordinates all activity for a project, then there may be a wider audience interested in that project, beyond those actively driving it forward.
These stakeholders might be interested in newly released features, known issues, upcoming changes or progress against plans.
GitHub Pages enables that wider audience to get a view that's bang-up-to-date, straight from the people working on it, right where they're working on it.

---

## Publishing demo
+ Simple publish process
+ Branded front-end
+ Multiple formats

{% if include.pres %}Note: {% endif %}
When this presentation is published, it will be available at lightenna.github.io, which is aliased to [lightenna.com](https://www.lightenna.com/).

It's available in multiple formats:

* [Web page](https://www.lightenna.com/tech/2024/write-markdown-for-future-proof-publishing/)
* [Presentation deck](https://www.lightenna.com/tech/2024/write-markdown-for-future-proof-publishing/reveal/)
* [Raw text](https://raw.githubusercontent.com/cleverlight/lightenna/main/_includes/presentations/2024-08-12-write-markdown-for-future-proof-publishing.md)
* [Pre-formatted markdown](https://github.com/cleverlight/lightenna/blob/main/_includes/presentations/2024-08-12-write-markdown-for-future-proof-publishing.md)


---

## Contributors
+ Internal or external
  + could be
    + vendor
    + reviewer
    + regulator
    + customer
    + other
+ Access control
  + approval process
+ Fit with single sign-on (SSO)

{% if include.pres %}Note: {% endif %}

---

## Alternative platforms
+ GitHub Pages is not a full CMS
  + there are restrictions
  + but most can be liberated by plugins/configuration
+ Confluence
  + excellent publishing platform
  + proprietary database
  + no code-level/repo-level management
    + web browser/app access only

{% if include.pres %}Note: {% endif %}
Markdown, Git, Jekyll and GitHub Pages are a powerful set of tools.
I find it incredible how applicable they are to many and varied scenarios.
However they're not a panacea.
The key differentiator for choosing a repo-based stack is when the repo is the source of activity for a project
and the project has a wider audience than those working on it.
It's not a comprehensive replacement for Confluence or JIRA, but it can be used an excellent low-cost alternative.

---

## Help

{% if include.pres %}Note: {% endif %}
If you'd like help organising and preparing your digital strategy, working with your team to foster a data-driven open culture, or just hands-on-keyboard training in infrastructure-as-code, please [get in touch](/contact).

