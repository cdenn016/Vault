---
type: paper
title: "Ergodic Theorems for Weakly Interacting Infinite Systems and the Voter Model"
aliases: ["Holley & Liggett 1975", "Voter model duality"]
authors: ["Holley R. A.", "Liggett T. M."]
year: 1975
url: https://doi.org/10.1214/aop/1176996306
tags: [cluster/social-physics, project/social-physics, field/mathematics, field/physics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Ergodic Theorems for Weakly Interacting Infinite Systems and the Voter Model

> [!info] Citation
> Holley, R. A., & Liggett, T. M. (1975). *Ergodic Theorems for Weakly Interacting Infinite Systems and the Voter Model*. The Annals of Probability 3(4), 643-663. DOI: [10.1214/aop/1176996306](https://doi.org/10.1214/aop/1176996306).

## TL;DR
Holley and Liggett provide the rigorous probabilistic foundation for the voter model on infinite lattices. Their central tool is a duality between the voter model and a system of coalescing random walks: tracing the genealogy of opinions backward in time turns the forward voter dynamics into walkers that move and merge. This duality yields a complete characterization of the model's long-run behaviour and, in particular, a clean dichotomy governed by lattice dimension — whether the infinite system reaches consensus (one opinion fixates everywhere) or settles into a one-parameter family of nontrivial stationary states in which the two opinions coexist.

## What it establishes
The duality identifies the probability that two sites $x, y$ hold the same opinion with the coalescence probability of two random walks started at $x$ and $y$. Because coalescence is governed by the recurrence or transience of the difference walk, the outcome splits by dimension: in dimensions $d \le 2$ the walks are recurrent, walkers always meet, correlations build up indefinitely, and the system "clusters" toward consensus; in dimensions $d \ge 3$ the walks are transient, coalescence is incomplete, and there exists a continuum of extremal translation-invariant stationary measures $\nu_\rho$ indexed by the conserved opinion density $\rho$, representing genuine coexistence. The paper proves that these $\nu_\rho$ are exactly the extremal invariant measures, settling the ergodic theory of the model.

## Relevance to this research
This paper supplies the rigorous backbone — the consensus-versus-coexistence dichotomy and its dimension dependence — for the voter model, the prototype discrete agreement process whose first-order, no-momentum dynamics belief-inertia positions as the overdamped baseline. Where Clifford-Sudbury introduced the model, Holley-Liggett proves precisely when copy-a-neighbour imitation drives the population to a single opinion versus a frozen mixture, which is the quantitative target a subsuming VFE gradient flow must reproduce in the corresponding limit. The relevance is foundational and mathematical rather than mechanistic: the duality machinery is not used inside the gauge-VFE functional, but it certifies the baseline behaviour the program claims to recover. See [[Voter model]], [[Opinion dynamics]], [[Belief inertia]].

## Cross-links
- Concept: [[Voter model]]
- Related sources: [[clifford-sudbury-1973-spatial-conflict]], [[sood-redner-2005-voter-heterogeneous-graphs]]

## BibTeX
```bibtex
@article{holley1975ergodic,
  author  = {Holley, Richard A. and Liggett, Thomas M.},
  title   = {Ergodic Theorems for Weakly Interacting Infinite Systems and the Voter Model},
  journal = {The Annals of Probability},
  year    = {1975},
  volume  = {3},
  number  = {4},
  pages   = {643--663},
  doi     = {10.1214/aop/1176996306}
}
```
