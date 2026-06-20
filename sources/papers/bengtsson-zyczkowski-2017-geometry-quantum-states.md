---
type: paper
title: "Geometry of Quantum States: An Introduction to Quantum Entanglement (2nd ed.)"
aliases:
  - "Bengtsson & Zyczkowski 2017"
  - "Geometry of Quantum States (2017)"
authors:
  - Ingemar Bengtsson
  - Karol Zyczkowski
year: 2017
arxiv: null
url: https://doi.org/10.1017/9781139207010
tags:
  - cluster/info-geometry
  - cluster/spd-geometry
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/mathematics
  - cluster/participatory/quantum-foundations
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Geometry of Quantum States: An Introduction to Quantum Entanglement (2nd ed.)

> [!info] Citation
> Ingemar Bengtsson and Karol Życzkowski (2017). *Geometry of Quantum States: An Introduction to Quantum Entanglement*, 2nd edition. Cambridge University Press. ISBN: 9781107026254.

## TL;DR

The standard graduate text unifying the geometry of quantum-state space. It develops the convex body of density matrices, the Fubini–Study metric on pure states, the Bures and Hilbert–Schmidt metrics on mixed states, the family of monotone (quantum Fisher) metrics, fidelity, and the geometry of entanglement — situating classical [[Fisher information metric|information geometry]] (the probability simplex, Fisher–Rao metric) as the commutative special case of the quantum theory.

## Problem & setting

Quantum states form a high-dimensional convex set whose geometry encodes distinguishability, entanglement, and dynamics. The book's aim is to give a coherent geometric account: which metrics are natural, how they relate, and what the geometry says about quantum information.

## Method

Expository and synthesizing. It builds from the classical probability simplex and Fisher–Rao geometry up to the quantum case: pure-state Fubini–Study geometry (the [[wootters-1981-statistical-distance]] distinguishability angle), mixed-state distinguishability via the Bures metric and Uhlmann fidelity ([[uhlmann-1976-transition-probability]]), the SLD quantum Fisher information ([[braunstein-caves-1994-quantum-fisher]]), and the Petz classification of monotone metrics ([[petz-1996-monotone-metrics]]). Entanglement geometry and majorization are treated in the same metric language.

## Key results

A textbook rather than a single result; the relevant content is the unified map: classical Fisher–Rao geometry as the commutative limit, the multiplicity of quantum monotone metrics, fidelity/Bures geometry, and the convex/entanglement structure of state space — the reference frame for any quantum-information-geometric argument.

## Relevance to this research

This is the consolidated reference for a *quantum extension* of [[participatory-it-from-bit]]. Where PIFB pulls back a classical distinguishability ([[Fisher information metric|Fisher–Rao]]) metric to read off physics, a quantum lift would work on the state-space geometry this book systematizes, and the text makes explicit the central caveat for that lift: in the quantum case the invariant metric is *not* unique (the Petz family), in contrast with the classical uniqueness held by [[cencov-1982-statistical-decision-rules]]. It is the natural home for the project's [[Quantum information geometry]] page and ties together the cited refs [[petz-1996-monotone-metrics]] and [[uhlmann-1976-transition-probability]] with the uncited distinguishability papers [[wootters-1981-statistical-distance]] and [[braunstein-caves-1994-quantum-fisher]]. It also connects to the SPD/Riemannian geometry the project already uses for covariance ([[pennec-2006-affine-invariant-tensor]]), since mixed-state geometry and SPD geometry share the monotone-metric structure.

## Cross-links

- Concept: [[Fisher information metric]], [[Quantum information geometry]].
- Theme: [[Physics from Fisher information]], [[Participatory realism (it from bit)]], [[Information geometry and natural gradient]].
- Sources: [[petz-1996-monotone-metrics]], [[uhlmann-1976-transition-probability]], [[wootters-1981-statistical-distance]], [[braunstein-caves-1994-quantum-fisher]], [[brody-hughston-2001-geometric-qm]], [[cencov-1982-statistical-decision-rules]], [[pennec-2006-affine-invariant-tensor]].
- Manuscript: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@book{bengtsson2017geometry,
  author    = {Bengtsson, Ingemar and {\.Z}yczkowski, Karol},
  title     = {Geometry of Quantum States: An Introduction to Quantum Entanglement},
  edition   = {2nd},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {2017},
  isbn      = {9781107026254},
  doi       = {10.1017/9781139207010}
}
```
