
## Git
* [Primer](https://www.slideshare.net/HubSpot/git-101-git-and-github-for-beginners)
* [Diagrams](https://marklodato.github.io/visual-git-guide/index-en.html)
* Setup
* Exercises

{% if include.pres %}Note: {% endif %}
This is a collection of online resources for those learning Git.

---

## Setup
* Remote Git server (e.g. GitHub, Bitbucket)
* Account with (shared) username
* Local install
* Git config with own name

{% if include.pres %}Note: {% endif %}
Running `git config` sets up your local git client with stateful data, which in turn is applied to each commit.
```
git config --global user.name 'Lightenna training'
git config --global user.email 'lighttrain@users.noreply.github.com'
```

---

## What is git?

* Distributed version control system
* The 'master' copy can be anywhere
* Conventionally, we adopt a single remote
* All contributions pushed to that remote
* Demonstrate with an example

---

## File tree

+ `/home/myuser/devops-workstream/`
    + `kubernetes`
        + `service.yaml`
        + `deployment.yaml`
    + `terraform`
    + `vagrant`
    + `README.md`

{% if include.pres %}Note: {% endif %}Git helps us manage sets of files.

This example set is taken from the open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream) repo.

---

## Changes

+ `/home/myuser/devops-workstream/`
    + `kubernetes`
        + `service.yaml`
        + `deployment.yaml`
    + `terraform`
    + `vagrant`
    + **README.md**

{% if include.pres %}Note: {% endif %}When we change a file, we need everyone else to see those changes.

We could simple copy the files around, but that risks overwriting others' changes.

Git provides a mechanism for us to contribute those changes, while managing the risk of overwriting other changes.

---

## Past: CVS/Subversion

<div class="mermaid">
    sequenceDiagram
    participant Working copy
    participant Remote repo
    Remote repo ->> Working copy: svn checkout
    Remote repo ->> Working copy: svn update
    Working copy ->> Remote repo: svn commit
</div>

* `svn checkout` - get a working copy
* `svn update` - get latest changes
* `svn commit` - push my changes

---

## Git pull (simplified)

<div class="mermaid">
    sequenceDiagram
    participant Working copy
    participant Local repo
    participant Remote repo
    Remote repo ->> Working copy: git clone
    Remote repo ->> Working copy: git pull
</div>

* `git clone` - create local repo and working copy
* `git pull` - update repo and working copy

---

## Git pull

<div class="mermaid">
    sequenceDiagram
    participant Working copy
    participant Local repo
    participant Remote repo
    Remote repo ->> Working copy: git clone
    Remote repo ->> Working copy: git pull
    Remote repo ->> Local repo: git fetch
    Local repo ->> Working copy: git checkout
</div>

* `git clone` - create local repo and working copy
* `git pull` - update repo and working copy
* `git fetch` - update local repo only
* `git checkout` - update working copy only

---

## Local repo stored in .git

+ `/home/myuser/devops-workstream/`
    + **.git**
    + `kubernetes`
        + `service.yaml`
        + `deployment.yaml`
    + `terraform`
    + `vagrant`
    + `README.md`

---

## Pull process

* `git pull`
    * Combines `fetch` and `checkout`
        * Fetch from remote
        * Update local repo
        * Update working copy

---

## Git push (simplified)

<div class="mermaid">
    sequenceDiagram
    participant Working copy
    participant Local repo
    participant Remote repo
    Working copy ->> Local repo: git commit .
    Local repo ->> Remote repo: git push
</div>

* `git commit .` - stage and commit to local
* `git push` - push local to remote

---

## Git push (including stage)

<div class="mermaid">
    sequenceDiagram
    participant Working copy
    participant Stage
    participant Local repo
    participant Remote repo
    Working copy ->> Stage: git add
    Stage ->> Local repo: git commit
    Local repo ->> Remote repo: git push
</div>

* `git add` - stage file for commit
* `git commit` - commit to local
* `git push` - push local to remote

---

## Push process

* `git commit .`
    * Combines `git add` and `git commit`
        * Stage for commit
        * Commit to local repo
* `git push`
        * Push local repo to remote

---

## Exercise: clone remote
* Clone remote repo locally (`git clone <repo_address>`)
* Change README.md, edit a _random_ line
* Stage and commit (`git commit . -m "message"`)
* Push (`git push`)
* Check online

{% if include.pres %}Note: {% endif %}

---

## Exercise: create repo
* Create remote repo
* Clone locally
* Copy files into working directory
* Stage
* Commit
* Push
* Check online

{% if include.pres %}Note: {% endif %}

---

## Exercise: undo a bad commit
* Clone locally (already done)
* Mess up a file
* Stage and commit
* View history
* Checkout a previous commit
* Make rational change
* Stage and commit again
* Push
* Check history online

{% if include.pres %}Note: {% endif %}

---

## Exercise: dump local, fetch remote
* Clone locally (already done)
* Mess up a file
* Stage and commit
* View history
* Fetch remote
* Reset local
* View history again

{% if include.pres %}Note: {% endif %}

---

## Exercise: merge feature branch
* Clone locally (already done)
* Create branch
* Checkout branch
* Make changes
* Stage and commit
* Push (optional)
* Switch to (checkout) master
* Merge
* Push

{% if include.pres %}Note: {% endif %}

---

## Exercise: tag a branch for release
* Clone locally (already done)
* Checkout master
* Check latest commit ID
* Create tag
* Update files
* Stage and commit
* Checkout tag

{% if include.pres %}Note: {% endif %}
[Basics of tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)

---

## Exercise: group collaboration
* [Clone shared repo](https://github.com/lighttrain/mergeo)
* Assign ticket numbers
* Create feature branch
* Add unique file
* Stage and commit
* Switch to (checkout) master
* Merge
* Push

{% if include.pres %}Note: {% endif %}

---

