---
type: paper
title: "Oscillatory and Excitable Dynamics in an Opinion Model with Group Opinions"
aliases:
  - "Group-opinion oscillations (Sampson et al. 2025)"
authors:
  - Corbit R. Sampson
  - Juan G. Restrepo
  - Mason A. Porter
year: 2025
arxiv: 2408.13336
doi: 10.1103/PhysRevE.112.024303
url: https://doi.org/10.1103/PhysRevE.112.024303
tags:
  - cluster/social-physics
  - cluster/social-physics/opinion-dynamics
  - project/social-physics
  - field/physics
  - field/mathematics
  - field/sociology
created: 2026-07-12
---

# Oscillatory and Excitable Dynamics in an Opinion Model with Group Opinions

> [!info] Citation
> Corbit R. Sampson, Juan G. Restrepo, and Mason A. Porter (2025). “Oscillatory and excitable dynamics in an opinion model with group opinions.” *Physical Review E* 112, 024303. DOI: [10.1103/PhysRevE.112.024303](https://doi.org/10.1103/PhysRevE.112.024303). arXiv: [2408.13336](https://arxiv.org/abs/2408.13336).

## TL;DR

Sampson, Restrepo, and Porter introduce a hypergraph opinion model in which individual agents and three-agent groups both possess opinions. Interactions between dyadic and group-level states produce self-sustained oscillations and excitable, fad-like swings in some parameter regimes. These oscillations arise without the kinetic-inertia mechanism proposed in the present manuscript and therefore demand mechanism-specific comparisons.

## Problem & setting

Most opinion models assign states only to individual agents and update them through pairwise interactions. This paper asks what changes when groups themselves carry opinions that can differ from those of their members. The authors study a hypergraph with opinions on agents and on groups of three, including both dyadic interactions and polyadic group memberships.

## Method

The authors formulate coupled microscopic dynamics for individual and group opinions, simulate the finite system, and derive a mean-field approximation. They compare the mean-field predictions with direct simulations across parameter regimes and examine how the correlation between the numbers of dyadic and polyadic interactions per agent changes the collective dynamics.

## Key results

The model exhibits a regime with self-sustained oscillations of the population's mean opinion and an excitable regime in which finite-size fluctuations trigger large but transient opinion swings resembling social fads. The mean-field description agrees well with direct numerical simulations. Oscillations occur only when dyadic and polyadic degrees are not completely correlated, identifying a structural condition for the phenomenon.

## Relevance to this research

This source blocks any inference from “oscillatory opinions” directly to [[Belief inertia]] or [[Hamiltonian belief dynamics]]. Group-opinion feedback provides an alternative mechanism that does not use a Fisher-based kinetic metric. Future tests should therefore manipulate or estimate the proposed mechanism: compare frequency and damping changes predicted by the kinetic metric and local VFE stiffness against changes caused by dyadic–polyadic degree correlations or group-level feedback.

## Cross-links

The paper links to [[Opinion dynamics]], [[Sociophysics]], [[Belief inertia]], [[Hamiltonian belief dynamics]], and [[Statistical physics of social systems and collective behavior]]. It is a complementary oscillation comparator to [[baumann-sokolov-tyloo-2020-second-order-consensus]], which produces resonance through periodically modulated coupling rather than group-opinion feedback.

## BibTeX

```bibtex
@article{SampsonPorterRestrepo2025,
  author        = {Sampson, Corbit R. and Restrepo, Juan G. and Porter, Mason A.},
  title         = {Oscillatory and Excitable Dynamics in an Opinion Model with Group Opinions},
  journal       = {Physical Review E},
  volume        = {112},
  number        = {2},
  pages         = {024303},
  year          = {2025},
  doi           = {10.1103/PhysRevE.112.024303},
  eprint        = {2408.13336},
  archivePrefix = {arXiv}
}
```
