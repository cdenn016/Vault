---
type: paper
title: "Walk-Sums and Belief Propagation in Gaussian Graphical Models"
aliases:
  - "Malioutov et al. 2006 walk-sums"
  - "Walk-summable Gaussian graphical models"
authors:
  - Malioutov, Dmitry M.
  - Johnson, Jason K.
  - Willsky, Alan S.
year: 2006
arxiv: null
url: https://www.jmlr.org/papers/v7/malioutov06a.html
tags:
  - cluster/vfe
  - cluster/info-geometry
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
  - field/mathematics
created: 2026-08-10
---

# Walk-Sums and Belief Propagation in Gaussian Graphical Models

> [!info] Citation
> Dmitry M. Malioutov, Jason K. Johnson, and Alan S. Willsky (2006). "Walk-Sums and Belief Propagation in Gaussian Graphical Models." *Journal of Machine Learning Research* **7**, 2031--2064. [Official JMLR record](https://www.jmlr.org/papers/v7/malioutov06a.html).

## TL;DR

The paper represents Gaussian correlations as sums over weighted graph walks and identifies the walk-summable class for which those sums converge absolutely. This gives a practical sufficient condition and a precise interpretation for convergence of loopy Gaussian belief propagation (GaBP).

## Problem & setting

A Gaussian Markov random field has sparse information matrix $J$ and information vector $h$. Exact means and variances can be obtained from $J^{-1}$, but direct inversion can be expensive. GaBP performs local message updates and is exact on trees; on graphs with cycles, convergence and marginal correctness require additional analysis.

## Method

After diagonal normalization, write $J=I-R$. Correlations are expanded as sums of products along walks. The model is walk-summable when the absolute walk series converges, equivalently under the paper's normalization when $\rho(|R|)<1$. GaBP reorganizes subsets of these walks into local message computations.

## Key results

The authors characterize walk-summability and relate it to diagonal dominance, attractive models, and other Gaussian model classes. Walk-summability guarantees convergence of GaBP and correct limiting means. On loopy graphs the variance estimates do not generally contain every closed walk and need not equal exact marginal variances; tree exactness must not be generalized to arbitrary positive-definite precision matrices.

## Relevance to this research

This source upgrades [[Gaussian Belief Propagation]] from a generic message-passing analogy to a testable baseline. MultiAgentELBO already builds exact finite Gaussian precision matrices and exact inverses, so each fixture can report $\rho(|R|)$, GaBP convergence, mean error, and variance error. A symmetric positive-definite interaction precision is not by itself evidence that the corresponding loopy GaBP iteration converges.

## Cross-links

- Concepts: [[Gaussian Belief Propagation]], [[Belief Propagation]], [[Decentralized Bayesian inference]]
- Related sources: [[yedidia-freeman-weiss-2005-region-free-energy]]

## BibTeX

```bibtex
@article{MalioutovJohnsonWillsky2006,
  author  = {Malioutov, Dmitry M. and Johnson, Jason K. and Willsky, Alan S.},
  title   = {Walk-Sums and Belief Propagation in Gaussian Graphical Models},
  journal = {Journal of Machine Learning Research},
  volume  = {7},
  pages   = {2031--2064},
  year    = {2006},
  url     = {https://www.jmlr.org/papers/v7/malioutov06a.html}
}
```
