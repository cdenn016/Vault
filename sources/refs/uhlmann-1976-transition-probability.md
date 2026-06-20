---
type: reference
title: "The Transition Probability in the State Space of a *-Algebra"
aliases:
  - "Uhlmann 1976"
  - "Uhlmann (1976) Transition Probability"
authors:
  - Armin Uhlmann
year: 1976
tags:
  - cluster/info-geometry
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/mathematics
  - field/physics
  - cluster/participatory/quantum-foundations
created: 2026-06-19
updated: 2026-06-19
---

# The Transition Probability in the State Space of a *-Algebra

> [!info] Citation
> Armin Uhlmann (1976). "The 'transition probability' in the state space of a *-algebra." *Reports on Mathematical Physics* 9(2): 273–279. DOI: [10.1016/0034-4877(76)90060-4](https://doi.org/10.1016/0034-4877(76)90060-4).

## TL;DR

Uhlmann defines a generalized transition probability between two states of a *-algebra and proves a purification/maximization formula for it: the transition probability between density operators $\rho$ and $\sigma$ is the supremum, over all purifications, of the overlap of their purifying vectors. This quantity is the **fidelity** $F(\rho,\sigma) = (\mathrm{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}})^2$, and its infinitesimal form is the Bures metric — a distinguished member of the [[petz-1996-monotone-metrics|Petz family]] of quantum monotone metrics.

## What it establishes

- **Operational transition probability / fidelity.** A symmetric, basis-independent measure of overlap between mixed states, generalizing the pure-state $|\langle\psi|\phi\rangle|^2$ to density operators via Uhlmann's theorem (maximization over purifications).
- **Origin of the Bures metric.** The Riemannian metric induced by fidelity is the Bures metric, equal to the SLD quantum Fisher information of [[braunstein-caves-1994-quantum-fisher]] up to a factor; it is the minimal monotone metric in the [[Fisher information metric|information-geometric]] sense.
- **Algebraic generality.** The construction is stated for general *-algebras, giving the result a foundational, representation-independent character.

> [!note] Editorial: This note summarizes Uhlmann's result from general knowledge; the purification formula and its identification with Bures fidelity are standard, but page-level details should be checked against the original before quotation.

## Why the project cites it

Uhlmann is the origin of the fidelity/Bures distance that any quantum lift of [[participatory-it-from-bit]] would use to measure distinguishability between agent states. The project pulls back a distinguishability metric to derive physical structure; in the quantum case that metric is Bures, and Uhlmann's transition probability is its source. It is one concrete member of the [[petz-1996-monotone-metrics|monotone-metric family]] — the operationally favored one — so it pairs with Petz (the non-uniqueness foil) and Braunstein–Caves (the SLD/Cramér–Rao reading) to fill out the quantum-extension toolkit referenced from the project's [[Quantum information geometry]] page. The pure-state limit of fidelity is exactly the [[wootters-1981-statistical-distance|Wootters]] distinguishability angle, tying Uhlmann back to the classical Fisher–Rao geometry the project already uses. Links the manuscript [[participatory-it-from-bit]] and the [[Physics from Fisher information]] theme.

```bibtex
@article{uhlmann1976transition,
  author  = {Uhlmann, Armin},
  title   = {The ``transition probability'' in the state space of a $*$-algebra},
  journal = {Reports on Mathematical Physics},
  volume  = {9},
  number  = {2},
  pages   = {273--279},
  year    = {1976},
  doi     = {10.1016/0034-4877(76)90060-4}
}
```
