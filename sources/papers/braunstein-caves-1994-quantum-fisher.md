---
type: paper
title: "Statistical distance and the geometry of quantum states"
aliases:
  - "Braunstein & Caves 1994"
  - "Braunstein-Caves (1994) Quantum Fisher Information"
authors:
  - Samuel L. Braunstein
  - Carlton M. Caves
year: 1994
arxiv: null
url: https://doi.org/10.1103/PhysRevLett.72.3439
tags:
  - cluster/info-geometry
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/statistics
  - cluster/participatory/quantum-foundations
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Statistical distance and the geometry of quantum states

> [!info] Citation
> Samuel L. Braunstein and Carlton M. Caves (1994). "Statistical distance and the geometry of quantum states." *Physical Review Letters* 72(22): 3439–3443. DOI: [10.1103/PhysRevLett.72.3439](https://doi.org/10.1103/PhysRevLett.72.3439).

## TL;DR

Braunstein and Caves extend Wootters' pure-state statistical distance to general (mixed) quantum states and to arbitrary parameter estimation. They define the **quantum Fisher information** via the symmetric logarithmic derivative (SLD) and show it is the metric obtained by maximizing the classical [[Fisher information metric|Fisher information]] of the measurement statistics over all possible measurements (POVMs). This yields the quantum Cramér–Rao bound — the ultimate precision limit for estimating a parameter encoded in a quantum state — and equips the space of density operators with a Riemannian distinguishability metric (the Bures metric).

## Problem & setting

[[wootters-1981-statistical-distance]] settled the pure-state case (statistical distance = Hilbert-space angle). Real estimation involves mixed states and a choice of measurement. The question is: what is the best achievable distinguishability between nearby quantum states, optimized over all measurements, and what metric does it define on the full state space of density matrices?

## Method

For a one-parameter family $\rho_\theta$, each measurement induces an outcome distribution with a classical Fisher information. Braunstein and Caves maximize this over all POVMs; the optimum is the **quantum Fisher information** $F_Q$, expressible through the symmetric logarithmic derivative $L_\theta$ defined by $\partial_\theta \rho = \tfrac{1}{2}(L_\theta \rho + \rho L_\theta)$, giving $F_Q = \mathrm{Tr}(\rho L_\theta^2)$. The associated line element is the Bures metric, and the optimal-measurement bound on estimation variance is the quantum Cramér–Rao inequality. The construction is operational: the metric is the best distinguishability an observer can extract.

## Key results

1. Defines the quantum Fisher information (SLD form) as the measurement-optimized classical Fisher information.
2. Establishes the quantum Cramér–Rao bound, the foundation of quantum metrology.
3. Identifies the Bures/SLD metric as a canonical distinguishability metric on mixed-state space — one distinguished member of the larger family of monotone metrics later classified by [[petz-1996-monotone-metrics]].

## Relevance to this research

This paper is the bridge from the project's classical information geometry to a *quantum* extension of [[participatory-it-from-bit]]. PIFB pulls back a distinguishability metric to derive physical structure; Braunstein–Caves give the quantum version of exactly that metric, the SLD/Bures metric, defined operationally as best-case distinguishability under measurement. For a quantum lift of PIFB's argument, the SLD metric is the natural object on which "physics from information geometry" would be built. It also matters for positioning: unlike the classical case — where the Čencov/Chentsov theorem ([[cencov-1982-statistical-decision-rules]]) makes the [[Fisher information metric]] unique — the quantum case admits a *family* of monotone metrics ([[petz-1996-monotone-metrics]]), and the SLD metric here is one principled choice. PIFB's quantum-extension discussion must confront that non-uniqueness, with Braunstein–Caves supplying the operationally favored representative. Links to [[Quantum information geometry]], [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]], and the distinguishability lineage from [[wootters-1981-statistical-distance]].

## Cross-links

- Concept: [[Fisher information metric]] (quantum/SLD form), [[Quantum information geometry]].
- Theme: [[Physics from Fisher information]], [[Participatory realism (it from bit)]].
- Sources: [[wootters-1981-statistical-distance]], [[petz-1996-monotone-metrics]], [[uhlmann-1976-transition-probability]], [[bengtsson-zyczkowski-2017-geometry-quantum-states]], [[cencov-1982-statistical-decision-rules]].
- Manuscript: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@article{braunstein1994statistical,
  author  = {Braunstein, Samuel L. and Caves, Carlton M.},
  title   = {Statistical distance and the geometry of quantum states},
  journal = {Physical Review Letters},
  volume  = {72},
  number  = {22},
  pages   = {3439--3443},
  year    = {1994},
  publisher = {American Physical Society},
  doi     = {10.1103/PhysRevLett.72.3439}
}
```
