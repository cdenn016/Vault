---
type: paper
title: "Quantifying High-Order Interdependencies via Multivariate Extensions of the Mutual Information"
aliases:
  - "Rosas et al. 2019 O-information"
authors:
  - Rosas, Fernando E.
  - Mediano, Pedro A. M.
  - Gastpar, Michael
  - Jensen, Henrik J.
year: 2019
arxiv: 1902.11239
url: https://doi.org/10.1103/PhysRevE.100.032305
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/statistics
  - field/physics
  - field/mathematics
created: 2026-08-10
---

# Quantifying High-Order Interdependencies via Multivariate Extensions of the Mutual Information

> [!info] Citation
> Fernando E. Rosas, Pedro A. M. Mediano, Michael Gastpar, and Henrik J. Jensen (2019). "Quantifying High-Order Interdependencies via Multivariate Extensions of the Mutual Information." *Physical Review E* 100, 032305. DOI: [10.1103/PhysRevE.100.032305](https://doi.org/10.1103/PhysRevE.100.032305). arXiv: [1902.11239](https://arxiv.org/abs/1902.11239). [APS record](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.100.032305).

## TL;DR

The paper introduces O-information, a permutation-symmetric scalar that contrasts redundancy-dominated and synergy-dominated dependence in a multivariate system without choosing predictors and a target. Positive values indicate redundancy dominance and negative values synergy dominance at the aggregate level. The compact algebra does not make high-dimensional entropy estimation easy and the sign is neither a causal claim nor a complete decomposition of information atoms.

## Problem & setting

Pairwise mutual information and interaction information do not by themselves give a stable, target-free summary of whether a many-variable distribution is dominated by shared or collective-only dependence. The authors seek a model-agnostic statistic for intrinsic high-order interdependence.

## Method

For variables \(X^n=(X_1,\ldots,X_n)\), O-information is the difference between total correlation and dual total correlation,

\[
\Omega(X^n)=\mathrm{TC}(X^n)-\mathrm{DTC}(X^n).
\]

Equivalently, it is a linear combination of the joint entropy, single-variable entropies, and leave-one-out marginal entropies. This makes the population quantity algebraically compact and symmetric, but each required entropy can still be statistically difficult to estimate in high dimension.

## Key results

The authors derive analytical properties connecting the sign of \(\Omega\) to redundancy- and synergy-dominated systems, relate it to other multivariate information measures, and illustrate it on Baroque music data. O-information is one signed aggregate: cancellation can hide heterogeneous atoms, and a near-zero result need not mean that high-order dependence is absent.

## Relevance to this research

O-information is a candidate diagnostic for ensemble or meta-agent distributions in [[O-information]], especially when a target-free statistic is desired. It should be estimated with uncertainty and finite-sample controls. It does not replace [[Partial information decomposition]], identify a mechanism, validate a meta-agent ontology, or by itself establish emergent causation.

## Cross-links

- Concepts: [[O-information]], [[Partial information decomposition]], [[Mutual information]]
- Related sources: [[williams-beer-2010-pid]], [[lyu-2026-pid-inconsistencies]]

## BibTeX

```bibtex
@article{Rosas2019,
  author  = {Rosas, Fernando E. and Mediano, Pedro A. M. and Gastpar, Michael and Jensen, Henrik J.},
  title   = {Quantifying High-Order Interdependencies via Multivariate Extensions of the Mutual Information},
  journal = {Physical Review E},
  volume  = {100},
  number  = {3},
  pages   = {032305},
  year    = {2019},
  doi     = {10.1103/PhysRevE.100.032305},
  eprint  = {1902.11239},
  archivePrefix = {arXiv}
}
```
