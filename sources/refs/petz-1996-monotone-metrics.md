---
type: reference
title: "Monotone Metrics on Matrix Spaces"
aliases:
  - "Petz 1996"
  - "Petz (1996) Monotone Metrics"
authors:
  - Denes Petz
year: 1996
tags:
  - cluster/info-geometry
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/mathematics
  - field/physics
  - field/statistics
  - cluster/participatory/quantum-foundations
created: 2026-06-19
updated: 2026-06-19
---

# Monotone Metrics on Matrix Spaces

> [!info] Citation
> Dénes Petz (1996). "Monotone metrics on matrix spaces." *Linear Algebra and its Applications* 244: 81–96. DOI: [10.1016/0024-3795(94)00211-8](https://doi.org/10.1016/0024-3795(94)00211-8).

## TL;DR

Petz classifies *all* Riemannian metrics on the space of density matrices that are monotone (contracting) under completely positive, trace-preserving maps — the quantum analogue of invariance under stochastic/Markov maps. The central result: such monotone metrics are in one-to-one correspondence with operator-monotone functions, so there is an *entire family* of admissible quantum information metrics (with the SLD/Bures metric the smallest and the right-logarithmic-derivative metric the largest). This is the quantum non-uniqueness theorem that stands in pointed contrast to the classical Čencov uniqueness of the [[Fisher information metric]].

## What it establishes

- **Quantum monotone-metric classification.** Every metric on quantum states contracting under CPTP maps corresponds to an operator-monotone function via the Kubo–Ando theory of operator means; the family is infinite-dimensional, not a single canonical metric.
- **Bures/SLD as one extreme.** The Bures (SLD quantum Fisher) metric of [[braunstein-caves-1994-quantum-fisher]] is the minimal monotone metric; [[uhlmann-1976-transition-probability]]'s transition probability/fidelity sits in this same family.
- **Classical limit.** On commuting (diagonal) states the whole family collapses to the unique classical Fisher–Rao metric, recovering Čencov's theorem as the commutative special case.

> [!note] Editorial: This note summarizes the well-known content of Petz's classification from general knowledge of the result; page-level claims should be checked against the published article before quotation.

## Why the project cites it

The project's classical information geometry rests on a *uniqueness* theorem — the held reference [[cencov-1982-statistical-decision-rules]] singles out the [[Fisher information metric]] as the only metric invariant under sufficient statistics, which is what licenses the natural-gradient and [[Mass as Fisher information]] constructions as canonical rather than arbitrary. Petz is the foil that exposes the limit of that argument: as soon as [[participatory-it-from-bit]] reaches for a *quantum* extension, uniqueness fails and a metric must be *chosen* from the monotone family. PIFB's quantum-extension thread therefore cannot simply transplant the classical "the geometry is forced" rhetoric; it must justify a specific metric (most naturally the Bures/SLD member, via [[braunstein-caves-1994-quantum-fisher]]). Petz supplies both the precise statement of the non-uniqueness and the operator-monotone-function machinery for making and defending that choice. The note links the project's [[Quantum information geometry]] page, the classical-uniqueness ref [[cencov-1982-statistical-decision-rules]], and the manuscript [[participatory-it-from-bit]].

```bibtex
@article{petz1996monotone,
  author  = {Petz, D{\'e}nes},
  title   = {Monotone metrics on matrix spaces},
  journal = {Linear Algebra and its Applications},
  volume  = {244},
  pages   = {81--96},
  year    = {1996},
  doi     = {10.1016/0024-3795(94)00211-8}
}
```
