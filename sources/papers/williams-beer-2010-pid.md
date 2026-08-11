---
type: paper
title: "Nonnegative Decomposition of Multivariate Information"
aliases:
  - "Williams and Beer 2010 PID"
authors:
  - Williams, Paul L.
  - Beer, Randall D.
year: 2010
arxiv: 1004.2515
url: https://arxiv.org/abs/1004.2515
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/statistics
  - field/mathematics
created: 2026-08-10
---

# Nonnegative Decomposition of Multivariate Information

> [!info] Citation
> Paul L. Williams and Randall D. Beer (2010). "Nonnegative Decomposition of Multivariate Information." arXiv: [1004.2515](https://arxiv.org/abs/1004.2515).

## TL;DR

Williams and Beer propose the redundancy lattice and a partial information decomposition (PID) of the mutual information that multiple sources provide about a designated target. Their redundancy functional \(I_{\min}\) yields nonnegative partial-information atoms in the proposed construction. The paper is foundational, but its particular redundancy measure and the resulting PID are proposals rather than a uniquely forced multivariate information decomposition.

## Problem & setting

Ordinary mutual information \(I(X_1,\ldots,X_n;Y)\) does not say which information about target \(Y\) is redundant across sources, unique to one source, or available only synergistically from joint observation. Interaction information can be negative and confounds redundancy with synergy.

## Method

The authors define a redundancy functional by taking, for each target outcome, the minimum specific information supplied by any source and then averaging over target outcomes. Collections of source subsets form a redundancy lattice. A cumulative redundancy function on that lattice is inverted to obtain partial-information atoms.

## Key results

Within this construction, the atoms exhaustively decompose source-target mutual information and are nonnegative, while the sign of interaction information is explained through competing redundant and synergistic contributions. These properties do not establish that \(I_{\min}\) is the only admissible redundancy functional. Later work has proposed inequivalent measures and found obstructions to general multivariate lattice decompositions.

## Relevance to this research

The source supplies the foundational vocabulary for [[Partial information decomposition]]. PID could test whether an aggregate or meta-agent target is predicted redundantly, uniquely, or synergistically by individual agents. Any such test must specify the target, redundancy definition, estimator, and sample regime; reporting "the PID" without those choices is underdetermined.

## Cross-links

- Concepts: [[Partial information decomposition]], [[O-information]], [[Mutual information]]
- Related sources: [[rosas-2019-o-information]], [[lyu-2026-pid-inconsistencies]]

## BibTeX

```bibtex
@article{WilliamsBeer2010,
  author        = {Williams, Paul L. and Beer, Randall D.},
  title         = {Nonnegative Decomposition of Multivariate Information},
  journal       = {arXiv preprint arXiv:1004.2515},
  year          = {2010},
  eprint        = {1004.2515},
  archivePrefix = {arXiv},
  primaryClass  = {cs.IT}
}
```
