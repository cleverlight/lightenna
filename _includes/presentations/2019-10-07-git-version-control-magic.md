
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

