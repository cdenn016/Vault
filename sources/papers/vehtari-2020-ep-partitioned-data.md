---
type: paper
title: "Expectation Propagation as a Way of Life: A Framework for Bayesian Inference on Partitioned Data"
aliases:
  - "Vehtari et al. 2020 EP partitioned data"
authors:
  - Vehtari, Aki
  - Gelman, Andrew
  - Sivula, Tuomas
  - Jylanki, Pasi
  - Tran, Dustin
  - Sahai, Swupnil
  - Blomstedt, Paul
  - Cunningham, John P.
  - Schiminovich, David
  - Robert, Christian P.
year: 2020
arxiv: null
url: https://www.jmlr.org/papers/v21/18-817.html
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/statistics
  - field/cs-ml
created: 2026-08-20
---

# Expectation Propagation as a Way of Life: A Framework for Bayesian Inference on Partitioned Data

> [!info] Citation
> Aki Vehtari, Andrew Gelman, Tuomas Sivula, Pasi Jylanki, Dustin Tran, Swupnil Sahai, Paul Blomstedt, John P. Cunningham, David Schiminovich, and Christian P. Robert (2020). "Expectation Propagation as a Way of Life: A Framework for Bayesian Inference on Partitioned Data." *Journal of Machine Learning Research* **21**(17), 1--53. https://www.jmlr.org/papers/v21/18-817.html

## TL;DR

Expectation propagation provides a general framework for partitioned Bayesian computation by maintaining approximations to local likelihood factors and updating each site in the context of the prior and other sites. This avoids the naive requirement to split a weak prior among independent subposterior fits.

## Problem & setting

Divide-and-conquer Bayes often fits data shards separately and then combines subposteriors. Splitting the prior can remove regularization from local problems, while multiplying approximate subposteriors can mishandle common information.

## Method

EP-style site factors approximate local likelihood contributions. Cavity distributions remove the current site before a local update, and damping, diagnostics, and numerical-stability practices control iterations. The framework supports partitioning of data and parameters and leaves the local approximation method flexible.

## Key results

The paper supplies an algorithmic framework and example implementation rather than one universally convergent algorithm. Its main contribution is disciplined factor accounting: local approximations are updated relative to the current global context instead of fused as if independent after the fact.

## Relevance to this research

The site-factor view is the right comparison for evidence provenance in [[Decentralized Bayesian inference]]. Messages should identify likelihood factors and their versions, not merely transmit moving posteriors. This source also contextualizes the existing posterior-server construction in [[hasenclever-2017-snep-posterior-server]].

## Cross-links

- Concepts: [[Decentralized Bayesian inference]], [[Approximate Bayesian inference]], [[Communication-constrained inference]]
- Related sources: [[hasenclever-2017-snep-posterior-server]], [[ashman-2022-partitioned-variational-inference]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{VehtariEtAl2020EPWayOfLife,
  author  = {Vehtari, Aki and Gelman, Andrew and Sivula, Tuomas and Jylanki, Pasi and Tran, Dustin and Sahai, Swupnil and Blomstedt, Paul and Cunningham, John P. and Schiminovich, David and Robert, Christian P.},
  title   = {Expectation Propagation as a Way of Life: A Framework for Bayesian Inference on Partitioned Data},
  journal = {Journal of Machine Learning Research},
  volume  = {21},
  number  = {17},
  pages   = {1--53},
  year    = {2020},
  url     = {https://www.jmlr.org/papers/v21/18-817.html}
}
```
