---
type: paper
title: "A Model for Spatial Conflict"
aliases: ["Clifford & Sudbury 1973", "Voter model (original)"]
authors: ["Clifford P.", "Sudbury A."]
year: 1973
url: https://doi.org/10.1093/biomet/60.3.581
tags: [cluster/social-physics, project/social-physics, field/mathematics, field/physics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# A Model for Spatial Conflict

> [!info] Citation
> Clifford, P., & Sudbury, A. (1973). *A Model for Spatial Conflict*. Biometrika 60(3), 581-588. DOI: [10.1093/biomet/60.3.581](https://doi.org/10.1093/biomet/60.3.581).

## TL;DR
Clifford and Sudbury introduce the interacting-particle system that the statistical-physics and probability communities would later call the voter model. Sites on a lattice each hold one of two discrete states ("species" competing for territory); at random times a site adopts the state of a randomly chosen neighbour. The paper frames this as a model of spatial conflict between two populations and analyzes whether one species eventually takes over the whole space (consensus) or the two coexist indefinitely, finding that the answer depends on the dimensionality of the underlying lattice. This is the founding formulation of the simplest copy-a-neighbour imitation dynamic.

## What it establishes
The dynamics is defined by the elementary update: a chosen site $i$ flips to match a uniformly chosen neighbour $j$, so the state $\sigma_i \in \{0,1\}$ obeys
$$ \sigma_i \to \sigma_j, \qquad j \sim \text{Uniform}(\partial i). $$
Because the rule conserves the global magnetization in expectation, the mean opinion density is a martingale, and the long-run behaviour is governed by fluctuations rather than drift. The central qualitative finding, made rigorous by later work, is a dimension-dependent dichotomy: in low dimensions ($d \le 2$) the system "clusters" and drives toward consensus (one species fixates), whereas in high dimensions ($d \ge 3$) the two states coexist in a fluctuating stationary mixture. The model has no built-in preference, no confidence threshold, and no noise — consensus or coexistence emerges purely from the geometry of imitation.

## Relevance to this research
The voter model is the canonical binary-agreement opinion dynamic and the most-cited discrete model the belief-inertia program claims to subsume in its overdamped limit. Copy-a-neighbour imitation is the zero-confidence, hard-classification edge of the gauge-transported KL coupling $\mathrm{KL}(q_i \| \Omega_{ij}[q_j])$: when an agent simply overwrites its belief with a neighbour's, the coupling has collapsed to deterministic adoption with no inertial resistance, the limit a first-order VFE gradient flow approaches as attention concentrates and precision is ignored. The dimension-dependent consensus-versus-coexistence behaviour is the kind of emergent collective outcome any subsuming functional must recover. This is a foundational original the vault otherwise lacks. See [[Voter model]], [[Opinion dynamics]], [[Belief inertia]].

## Cross-links
- Concept: [[Voter model]]
- Related sources: [[holley-liggett-1975-voter-model-ergodic]], [[sood-redner-2005-voter-heterogeneous-graphs]]

## BibTeX
```bibtex
@article{clifford1973spatial,
  author  = {Clifford, Peter and Sudbury, Aidan},
  title   = {A Model for Spatial Conflict},
  journal = {Biometrika},
  year    = {1973},
  volume  = {60},
  number  = {3},
  pages   = {581--588},
  doi     = {10.1093/biomet/60.3.581}
}
```
