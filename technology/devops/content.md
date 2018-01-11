
# DevOps

Technology overview from Lightenna

---

## Culture

* Neither a set of tools
* Nor a role
* DevOps as a collaboration

Note: I like the Peter Drucker quote "Culture eats strategy for breakfast."  It's hugely over-used but as relevant for DevOps [as it was for motorcars when Mark Fields referenced it](https://www.torbenrick.eu/blog/culture/organisational-culture-eats-strategy-for-breakfast-lunch-and-dinner/). 

---

## Cost-benefit

<div class="left">

<p data-markdown>Expensive</p>
<p data-markdown>Bespoke</p>
<p data-markdown>Inefficient</p>
<p data-markdown>Hard to manage</p>

</div>
<div class="right">

<p data-markdown>Great</p>

</div>

Note: Collaboration has yielded most of the world's greatest online projects, but managed poorly it can carry a high cost.  The old "how many X does it take to change a lightbulb?" joke owes its creation to redundant collaboration.

<a href="https://xkcd.com/841/"><img src="https://imgs.xkcd.com/comics/audiophiles.png" width="740" height="285" alt="XKCD comic: Audiophiles"></a>

All projects, whether compose of 2 or 200 participants, are searching for the right balance of collaborative activity and skilled individual effort. 

---

## Frag list

<p class="fragment">One</p>
<p class="fragment">Two</p>
<p class="fragment">Three</p>

<pre><code data-trim data-noescape>
(def lazy-fib
  (concat
   [0 1]
   <mark>((fn rfib [a b]</mark>
        (lazy-cons (+ a b) (rfib b (+ a b)))) 0 1)))
</code></pre>
