---
type: reference
title: "Modeling by Shortest Data Description"
aliases:
  - "Rissanen 1978"
  - "Rissanen (1978) MDL"
authors:
  - Jorma Rissanen
year: 1978
tags:
  - cluster/methodology
  - cluster/multi-agent
  - project/multi-agent
  - field/statistics
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# Modeling by Shortest Data Description

> [!info] Citation
> Jorma Rissanen (1978). "Modeling by shortest data description." *Automatica* **14**(5), 465–471. DOI: [10.1016/0005-1098(78)90005-5](https://doi.org/10.1016/0005-1098(78)90005-5).

## TL;DR

Rissanen introduces the Minimum Description Length (MDL) principle: the best model for a body of data is the one that allows the shortest total encoding of *both* the model and the data given the model. The number of bits to transmit the data depends on the assumed model, so minimizing the combined description length trades fit against complexity automatically and yields estimates of both the integer structure parameters (model order) and the real-valued parameters. MDL is the information-theoretic lens under which the project reads its variational free energy as a description length.

## What it establishes

Coding theory makes a model's quality operational: a model that compresses the data well is a good model. The total code length splits into the cost of describing the parameters plus the cost of the data encoded with those parameters; minimizing the sum penalizes elaborate models whose parameter-encoding cost exceeds the fit they buy. This realizes Occam's razor as a coding principle and, asymptotically, the parameter-coding term reproduces the $\tfrac{1}{2}k\log n$ penalty of [[schwarz-1978-bic|BIC]], unifying MDL with Bayesian model selection.

## Why the project cites it

The project's [[Variational free energy]] decomposes as accuracy (expected log-likelihood) minus complexity (a KL from posterior to prior), which is exactly the description-length tradeoff Rissanen formalizes: the KL-complexity term is the bits spent encoding the belief relative to the prior, and the likelihood term is the bits spent encoding the data given the belief. Reading VFE as a code length makes the project's free-energy minimization an MDL principle, and it supplies the second of the two meta-agent retention criteria — keep a coarse-graining only if it shortens the total description of the agent population ([[Meta-agents and hierarchical emergence]]). It anchors the new [[MDL and BIC model selection]] page alongside [[schwarz-1978-bic]]. Manuscript thread: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@article{rissanen1978modeling,
  author  = {Rissanen, Jorma},
  title   = {Modeling by shortest data description},
  journal = {Automatica},
  volume  = {14},
  number  = {5},
  pages   = {465--471},
  year    = {1978},
  doi     = {10.1016/0005-1098(78)90005-5}
}
```
