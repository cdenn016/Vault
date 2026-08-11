---
type: paper
title: Nonperturbative Trivializing Flows for Lattice Gauge Theories
aliases:
  - Gerdes et al. 2025 trivializing flows
authors:
  - Mathis Gerdes
  - Pim de Haan
  - Roberto Bondesan
  - Miranda C. N. Cheng
year: 2025
arxiv: "2410.13161"
url: https://doi.org/10.1103/31d5-hvp6
tags:
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
  - field/physics
  - field/cs-ml
  - field/mathematics
status: stable
created: 2026-08-10
updated: 2026-08-10
---

# Nonperturbative Trivializing Flows for Lattice Gauge Theories

> [!info] Citation
> Mathis Gerdes, Pim de Haan, Roberto Bondesan, and Miranda C. N. Cheng. “Nonperturbative Trivializing Flows for Lattice Gauge Theories.” *Physical Review D* 112, 094516, 2025. [doi:10.1103/31d5-hvp6](https://doi.org/10.1103/31d5-hvp6); [arXiv:2410.13161](https://arxiv.org/abs/2410.13161).

## TL;DR

The paper constructs continuous normalizing flows directly on matrix Lie-group variables, with an equivariant vector field and Lie-group numerical integration, and demonstrates them for two-dimensional $SU(2)$ and $SU(3)$ lattice gauge theories.

## Problem & setting

Strongly coupled lattice gauge targets can be difficult for conventional Monte Carlo because nearby link configurations are highly correlated. A trivializing flow aims to map a simple reference measure to a distribution close to the interacting target while respecting gauge transformations and group constraints.

## Method

The authors parameterize a continuous-time flow by an equivariant vector field on lattice links, integrate it with a Lie-group integrator, and account for the density change. The demonstrations use compact special-unitary link groups, a Haar reference measure, Wilson-loop features, reverse-KL training, and a Metropolis correction when exact sampling is desired.

## Key results

- A general group-aware continuous-flow architecture is developed for matrix Lie-group variables.
- The construction is equivariant under lattice gauge transformations by design.
- Two-dimensional $SU(2)$ and $SU(3)$ experiments report high effective sample sizes and competitive performance in the studied regimes.

## Relevance to this research

This is an implementation-level precedent for gauge-equivariant proposals/samplers: group-valued links remain on-manifold, the density/Jacobian is tracked, and Metropolis correction cleanly separates approximation quality from asymptotic exactness. Those are concrete requirements for any claimed gauge-equivariant flow baseline.

## Scope limits

The demonstrated targets use compact $SU(N)$ groups and a normalized Haar prior. A noncompact $\mathrm{GL}(K)$ or $\mathrm{GL}^{+}(K)$ model has no normalized Haar probability and needs separate proofs of target normalizability, divergence/Jacobian formulas, integrator stability, and proposal validity. Finite site variables alone are not lattice gauge theory: one also needs an interaction complex, oriented group-valued links, and appropriate loop/plaquette observables.

## Cross-links

- [[Lattice gauge theory]]
- [[Gauge transformation]]
- [[Holonomy]]
- [[Parallel transport]]

## BibTeX

```bibtex
@article{gerdes2025nonperturbative,
  title   = {Nonperturbative Trivializing Flows for Lattice Gauge Theories},
  author  = {Gerdes, Mathis and de Haan, Pim and Bondesan, Roberto and Cheng, Miranda C. N.},
  journal = {Physical Review D},
  volume  = {112},
  number  = {9},
  pages   = {094516},
  year    = {2025},
  doi     = {10.1103/31d5-hvp6},
  eprint  = {2410.13161},
  archivePrefix = {arXiv}
}
```
