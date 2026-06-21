---
type: paper
title: Variational Message Passing
aliases:
  - "Winn, Bishop 2005 — VMP"
  - "Variational Message Passing"
  - "winn-2005-vbem"
  - "winn-2005-variational-message-passing"
  - "winn2005vbem"
authors:
  - John Winn
  - Christopher M. Bishop
year: 2005
arxiv: null
url: https://jmlr.org/papers/v6/winn05a.html
tags:
  - cluster/vfe
  - cluster/methodology
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Variational Message Passing

> [!info] Citation
> Winn, J., & Bishop, C. M. (2005). Variational Message Passing. Journal of Machine Learning Research, 6, 661-694. URL: https://jmlr.org/papers/v6/winn05a.html

## TL;DR

Variational message passing (VMP) turns mean-field variational inference into a purely local algorithm on a graphical model. For the broad class of *conjugate-exponential* Bayesian networks, Winn and Bishop show that the standard coordinate-ascent update for a factorised (mean-field) posterior — the update that, holding all other factors fixed, sets each factor to the exponential of the expected log-joint — can be computed at each node using only messages received from that node's parents and children in the graph. Each message is an expectation of a natural-statistics vector, the local update is a sum of incoming messages in natural-parameter space, and every sweep is guaranteed to increase the same lower bound on the log evidence (the ELBO / negative variational free energy) that the global mean-field objective optimises. The practical payoff is that variational inference no longer has to be hand-derived model by model: VMP gives a single mechanical recipe, and the authors realise it as a general inference engine (VIBES) that solves a graphical model specified by the user without bespoke code.

## Problem & setting

Exact Bayesian inference is intractable for all but the simplest models, so deterministic variational methods approximate the true posterior $p(\mathbf{H}\mid\mathbf{V})$ over hidden variables $\mathbf{H}$ given observed $\mathbf{V}$ by a simpler distribution $q(\mathbf{H})$, chosen to maximise a lower bound on the log marginal likelihood $\log p(\mathbf{V})$. The dominant choice is the *mean-field* family, in which $q$ factorises into a product $q(\mathbf{H}) = \prod_i q_i(H_i)$ over disjoint groups of variables, and the bound is optimised by cyclically updating one factor at a time. The closed-form coordinate-ascent update for each factor was already classical (it is the variational-EM / mean-field result given in Beal's thesis and Bishop's Chapter 10), but deriving and implementing it required tedious, model-specific algebra. VMP builds directly on that mean-field machinery and on the structure of *conjugate-exponential* models — directed graphical models in which every conditional distribution is in the exponential family and each parent–child pair is conjugate — to replace the per-model derivation with a uniform local computation, in the same spirit that belief propagation localises exact inference on trees.

## Method

Restrict attention to a conjugate-exponential Bayesian network, where the conditional for each node $X$ given its parents $\mathrm{pa}(X)$ has exponential-family form
$$
p(X\mid \mathrm{pa}(X)) = \exp\!\big[\,\boldsymbol{\eta}(\mathrm{pa}(X))^{\top} \mathbf{u}(X) + g(\mathrm{pa}(X)) + f(X)\,\big],
$$
with natural-parameter vector $\boldsymbol{\eta}$, natural-statistics vector $\mathbf{u}(X)$, and conjugacy chosen so that, viewed as a function of any one parent, the log-conditional is linear in that parent's own natural statistics. Under the mean-field factorisation $q(\mathbf{H}) = \prod_i q_i(H_i)$, the optimal factor for node $X$ holding the others fixed is
$$
\log q^{\star}(X) = \mathbb{E}_{q\setminus X}\!\big[\log p(X, \text{Markov blanket})\big] + \text{const},
$$
where the expectation is taken over the current factors of every variable other than $X$. The contribution of conjugate-exponential structure is that this expectation collapses into a sum over the node's Markov blanket: the updated natural parameter of $q^{\star}(X)$ is
$$
\boldsymbol{\eta}^{\star}_X = \mathbb{E}\!\big[\boldsymbol{\eta}(\mathrm{pa}(X))\big] + \sum_{Y \in \mathrm{ch}(X)} \mathbf{m}_{Y\to X},
$$
a *parent message* carrying the expected natural parameters from above plus *child messages* $\mathbf{m}_{Y\to X}$ coming up from each child. Every message is itself an expectation of a natural-statistics vector under the sender's current factor, $\langle \mathbf{u} \rangle$, so the messages a node emits are determined entirely by its own moments and those of its co-parents. The algorithm therefore reduces to: each node collects messages from its parents and children, sums them in natural-parameter space to obtain $\boldsymbol{\eta}^{\star}_X$, and recomputes the moments $\langle \mathbf{u}(X)\rangle$ it will broadcast in turn. Sweeping these local updates is exactly mean-field coordinate ascent, so each update monotonically raises the lower bound
$$
\mathcal{L}(q) = \mathbb{E}_q[\log p(\mathbf{H},\mathbf{V})] - \mathbb{E}_q[\log q(\mathbf{H})] \le \log p(\mathbf{V}),
$$
and the bound can be evaluated in closed form to monitor convergence and to compare models. The paper also shows how to handle distributions that break strict conjugacy by introducing additional variational parameters, extending the reach beyond the purely conjugate case.

## Key results

The principal result is structural rather than empirical: VMP is a provably bound-increasing, fully local realisation of mean-field variational inference for arbitrary conjugate-exponential Bayesian networks, with each node's update expressed as a sum of natural-parameter messages over its Markov blanket. Because the lower bound $\mathcal{L}(q)$ is available in closed form, the same machinery serves both as a convergence diagnostic and as an approximate model-evidence score for Bayesian model comparison. The authors demonstrate generality by implementing VMP as VIBES, a general-purpose inference engine that accepts a graphical-model specification and produces the variational solution automatically, removing the need to derive update equations by hand for each new model. The contribution is best read as a unification and automation result — it makes the mean-field update mechanical and reusable — rather than as a claim of a new statistical optimality bound; the specifics here are the algorithmic guarantees (locality, monotone bound increase, conjugate-exponential closure) and the working software, not benchmark performance figures.

## Relevance to this research

VMP casts mean-field variational inference on conjugate-exponential models as local message passing on a factor graph, which is precisely the computational structure the gauge-theoretic VFE attention realises when it routes precision-weighted prediction errors between token-belief factors. The natural-parameter-summation form of the VMP update — collect messages over the Markov blanket, add in natural coordinates, rebroadcast moments — is the template against which the transformer's coupled E-step over the Gaussian belief tuples $(\mu, \Sigma, \phi)$ should be checked: the cross-token KL-coupling terms in the free energy $F$ play the role of child/parent messages, and the gauge transport $\Omega_{ij}$ is the conjugate reparameterisation a message undergoes as it crosses an edge. Reading the architecture through VMP pins down exactly which mean-field factorisation underwrites a given E-step update — a product over per-token factors $\prod_i q_i$ — and supplies the standard guarantee that each local update is bound-increasing, which is the property the iterated VFE minimisation must inherit to be a legitimate variational scheme rather than an ad hoc fixed-point. See [[Inference machinery — variational EM and filtering]] and [[Variational free energy and predictive coding]] for how this localisation maps onto the predictive-coding reading of the model.

## Cross-links

- Concepts / Themes: [[Inference machinery — variational EM and filtering]], [[Variational free energy and predictive coding]]
- Related sources: [[amari-1998-natural-gradient]]

## BibTeX

```bibtex
@article{winn2005variational,
  author  = {Winn, John and Bishop, Christopher M.},
  title   = {Variational Message Passing},
  journal = {Journal of Machine Learning Research},
  volume  = {6},
  pages   = {661--694},
  year    = {2005},
  url     = {https://jmlr.org/papers/v6/winn05a.html}
}
```
