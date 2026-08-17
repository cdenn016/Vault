---
type: paper
title: "I-Divergence Geometry of Probability Distributions and Minimization Problems"
aliases:
  - "Csiszár 1975"
  - "I-projection"
  - "I-divergence geometry"
authors:
  - Csiszár I.
year: 1975
tags:
  - cluster/info-geometry
  - project/multi-agent
  - field/statistics
  - field/mathematics
created: 2026-08-17
updated: 2026-08-17
---

# I-Divergence Geometry of Probability Distributions and Minimization Problems

> [!info] Citation
> I. Csiszár (1975). "I-Divergence Geometry of Probability Distributions and Minimization
> Problems." *Annals of Probability* **3**(1), 146–158.
> DOI: [10.1214/aop/1176996454](https://doi.org/10.1214/aop/1176996454).

## TL;DR

Establishes the geometry of Kullback–Leibler divergence as a squared-distance analog: the
**I-projection** of a distribution onto a convex set exists, is unique, and satisfies a
Pythagorean identity, and the iterative algorithms that alternate projections onto constraint
sets — iterative proportional fitting among them — converge to the minimizer.

## What it establishes

Existence, uniqueness, and Pythagorean structure of I-projections onto convex sets of
distributions, and convergence of the natural iterative (alternating-projection) algorithms to
the projection. This is the theorem that makes IPF a deterministic solver for
divergence-minimization under marginal constraints rather than a heuristic.

## Relevance to this research

Load-bearing for the rescaling laboratory's coupling read-back: the variational route of the
renormalization step minimizes $\mathrm{KL}(\pi_{\text{coarse}} \| \pi_{\text{family}}(\theta))$
over the exponential family spanned by admitted subset indicators, and by this paper's results
that minimizer is the marginal-matching member and IPF from a seed inside the family converges
to it deterministically — which is why the primary route has no optimizer-in-a-local-minimum
failure mode to fear (cited in `coupling_readback.py` of MultiAgentELBO). See
[[Renormalization group flow]] and [[Staged hierarchy formation and RG composability]].

## BibTeX

```bibtex
@article{csiszar1975idivergence,
  author  = {Csisz{\'a}r, Imre},
  title   = {I-Divergence Geometry of Probability Distributions and Minimization Problems},
  journal = {Annals of Probability},
  volume  = {3},
  number  = {1},
  pages   = {146--158},
  year    = {1975},
  doi     = {10.1214/aop/1176996454}
}
```
