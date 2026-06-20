---
type: reference
title: "Curvatures of Left Invariant Metrics on Lie Groups"
aliases:
  - "Milnor 1976"
  - "Milnor (1976) Left-Invariant Metrics"
authors:
  - John Milnor
year: 1976
tags:
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
  - field/mathematics
created: 2026-06-19
updated: 2026-06-19
---

# Curvatures of Left Invariant Metrics on Lie Groups

> [!info] Citation
> John Milnor (1976). "Curvatures of Left Invariant Metrics on Lie Groups." *Advances in Mathematics* 21(3), 293–329. DOI: [10.1016/S0001-8708(76)80002-3](https://doi.org/10.1016/S0001-8708(76)80002-3).

## TL;DR

A self-contained study of the Riemannian geometry of Lie groups equipped with **left-invariant metrics**: it computes sectional, Ricci, and scalar curvatures directly from the structure constants, and characterizes which Lie groups admit bi-invariant metrics and flat metrics. The punchline relevant here is that a connected Lie group admits a **bi-invariant** metric if and only if it is (isomorphic to) the product of a compact group and a vector group — so noncompact groups like $GL^+(K)$ do not.

## What it establishes

- Explicit formulas for the curvature of a left-invariant metric in terms of the Lie-bracket structure constants and the metric coefficients.
- The bi-invariance criterion: bi-invariant metrics exist iff the group is compact-times-abelian; equivalently, the metric must be $\mathrm{Ad}$-invariant, which for semisimple groups means proportional to (minus) the [[Killing form]].
- Characterizations of flat left-invariant metrics and of groups whose left-invariant metrics have definite-sign Ricci curvature, with the role of the Killing form throughout.

## Why the project cites it

The program transports beliefs with $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ and averages frames by a first-order barycenter $\phi_I = \sum_i w_i\phi_i$ in the Lie algebra of $GL^+(K)$. Both operations implicitly pick a metric and a notion of "straight" on the group, and Milnor's theorem says $GL^+(K)$, being noncompact and non-abelian, admits **no bi-invariant metric**. Two consequences run straight into the code. First, there is no canonical inner product making the [[Baker-Campbell-Hausdorff formula]] barycenter exact: $\log(e^{\phi_i}e^{\phi_j}) = \phi_i + \phi_j + \tfrac12[\phi_i,\phi_j]+\dots$, so the linear average $\sum_i w_i\phi_i$ is only a *first-order* (BCH-truncated) mean — the commutator corrections that Milnor's curvature formulas quantify are exactly what is dropped. Second, this is why the program exposes an `omega_metric` choice (`frobenius` default, `killing` bi-invariant-style, `pullback` Fisher): on a group with no bi-invariant metric the metric is a genuine modeling decision, not a foregone conclusion, and the [[Killing form]] option is the closest thing to canonical only on the semisimple part. Milnor supplies the structural reason these toggles exist and bounds the error of the BCH barycenter used in [[Meta-agents and hierarchical emergence]]. Ground for the frame-geometry discussion in [[participatory-it-from-bit]].

## BibTeX

```bibtex
@article{milnor1976curvatures,
  title   = {Curvatures of Left Invariant Metrics on Lie Groups},
  author  = {Milnor, John},
  journal = {Advances in Mathematics},
  volume  = {21},
  number  = {3},
  pages   = {293--329},
  year    = {1976},
  doi     = {10.1016/S0001-8708(76)80002-3}
}
```
