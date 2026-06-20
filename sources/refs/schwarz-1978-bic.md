---
type: reference
title: "Estimating the Dimension of a Model"
aliases:
  - "Schwarz 1978"
  - "Schwarz (1978) BIC"
authors:
  - Gideon Schwarz
year: 1978
tags:
  - cluster/methodology
  - cluster/multi-agent
  - project/multi-agent
  - field/statistics
created: 2026-06-19
updated: 2026-06-19
---

# Estimating the Dimension of a Model

> [!info] Citation
> Gideon Schwarz (1978). "Estimating the dimension of a model." *Annals of Statistics* **6**(2), 461–464. DOI: [10.1214/aos/1176344136](https://doi.org/10.1214/aos/1176344136).

## TL;DR

Schwarz derives the Bayesian Information Criterion (BIC) by computing the leading asymptotic terms of the Bayes posterior probability of a model. Selecting the model that maximizes the marginal likelihood reduces, to leading order, to maximizing $\log \hat{L} - \tfrac{1}{2} k \log n$, where $\hat{L}$ is the maximized likelihood, $k$ the number of free parameters, and $n$ the sample size. The $\tfrac{1}{2}k\log n$ term is an automatic Occam penalty on model complexity, growing with data size. It is one of the two retention criteria the project uses to decide which meta-agents are worth keeping.

## What it establishes

For comparing models of different dimension under a Bayesian framework with priors that do not vanish too fast, the log marginal likelihood admits a Laplace (saddle-point) expansion whose leading terms are $\log \hat{L}_k - \tfrac{1}{2}k\log n + O(1)$. Choosing the model maximizing this quantity is asymptotically the Bayes-optimal selection, and the penalty $\tfrac{1}{2}k\log n$ penalizes added parameters more heavily than AIC's constant-per-parameter penalty, yielding consistent model-order selection.

## Why the project cites it

When the project forms [[Meta-agents and hierarchical emergence|meta-agents]] by coarse-graining clusters of agents, it must decide whether introducing a coarse parent (adding parameters) is justified by the data — a model-selection problem. BIC is one of the two criteria invoked for this retention test: a candidate meta-agent is kept only if the gain in fit outweighs the $\tfrac{1}{2}k\log n$ complexity penalty. This gives the hierarchy-growth rule a principled Bayesian footing and connects naturally to the description-length reading of [[rissanen-1978-mdl]], since BIC is the asymptotic Bayesian counterpart of MDL. It anchors the new [[MDL and BIC model selection]] page; the underlying Laplace expansion is the same saddle-point technique as the RG closure ([[cardy-1996-scaling-renormalization]], [[wong-2001-asymptotic-integrals]]). Manuscript thread: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@article{schwarz1978estimating,
  author  = {Schwarz, Gideon},
  title   = {Estimating the dimension of a model},
  journal = {Annals of Statistics},
  volume  = {6},
  number  = {2},
  pages   = {461--464},
  year    = {1978},
  doi     = {10.1214/aos/1176344136},
  publisher = {Institute of Mathematical Statistics}
}
```
