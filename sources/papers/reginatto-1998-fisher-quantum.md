---
type: paper
title: "Derivation of the equations of nonrelativistic quantum mechanics using the principle of minimum Fisher information"
aliases:
  - "Reginatto 1998"
  - "Reginatto (1998) Minimum Fisher Information"
authors:
  - Marcel Reginatto
year: 1998
arxiv: null
url: https://doi.org/10.1103/PhysRevA.58.1775
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

# Derivation of the equations of nonrelativistic quantum mechanics using the principle of minimum Fisher information

> [!info] Citation
> Marcel Reginatto (1998). "Derivation of the equations of nonrelativistic quantum mechanics using the principle of minimum Fisher information." *Physical Review A* 58(3): 1775–1778. DOI: [10.1103/PhysRevA.58.1775](https://doi.org/10.1103/PhysRevA.58.1775).

## TL;DR

Reginatto shows that the Schrödinger equation can be derived by adding a single information-theoretic term — the [[Fisher information metric|Fisher information]] of the probability density over configuration space — to the classical Hamilton–Jacobi action and extremizing. The classical theory plus a *minimum Fisher information* requirement reproduces the full quantum dynamics: the Fisher term becomes the quantum (Bohm) potential, and Planck's constant appears as the coupling that sets the cost of localizing probability. Quantum behavior is recast as the consequence of a probability distribution carrying minimal Fisher information consistent with its constraints, rather than as an independent postulate.

## Problem & setting

The classical ensemble of a particle is described by a probability density $\rho(x,t)$ and a Hamilton–Jacobi action $S(x,t)$, evolving by the continuity equation and the classical Hamilton–Jacobi equation. This pair is underdetermined as a *quantum* theory: nothing in it forces the uncertainty relations or the wave-like interference of quantum mechanics. Reginatto asks what minimal information-theoretic principle, applied to $\rho$, promotes the classical ensemble to the quantum one.

## Method

He augments the classical action functional with a term proportional to the Fisher information of the spatial density,
$$ I_F = \int \frac{|\nabla \rho|^2}{\rho}\, dx, $$
and extremizes the total action subject to normalization. The variational equations for $\rho$ and $S$ then combine, via the Madelung substitution $\psi = \sqrt{\rho}\,e^{iS/\hbar}$, into exactly the time-dependent Schrödinger equation. The Fisher term generates the quantum potential $Q = -(\hbar^2/2m)\,\nabla^2\sqrt{\rho}/\sqrt{\rho}$, and the proportionality constant fixes $\hbar$. The principle is *minimum* Fisher information: among densities compatible with the constraints, the dynamics selects the one of least Fisher information, mirroring maximum-entropy reasoning but on the metric (distinguishability) side rather than the entropy side.

## Key results

1. Nonrelativistic single-particle quantum mechanics (the Schrödinger equation) follows from classical mechanics plus a minimum-Fisher-information requirement on the configuration-space density.
2. The quantum potential is identified as the Fisher-information contribution to the energy; the "quantumness" of the dynamics is the price of curvature in the statistical metric.
3. The framework gives an information-geometric meaning to $\hbar$ as the coupling between classical action and Fisher information.

## Relevance to this research

This is the most on-point neighbor for the central thesis of [[participatory-it-from-bit]]: that physical structure can be *read off* the information geometry of beliefs rather than postulated. Where the manuscript argues that an agent's belief dynamics inherit physics from the [[Fisher information metric]] on belief space, Reginatto supplies the cleanest concrete precedent — an actual field equation (Schrödinger) obtained by extremizing a Fisher term over a probability density. The mapping is direct: the Fisher-info penalty on $\rho$ is the same quantity the project treats as inertial cost in [[Mass as Fisher information]], where "mass" is identified with Fisher information and resistance to belief change is the curvature of the statistical metric. Reginatto's minimum-Fisher principle is also the information-geometric companion to the maximum-entropy lineage the project draws on through [[caticha-2019-entropic-dynamics]]; indeed Reginatto co-authored the cited entropic-dynamics core [[caticha-bartolomeo-reginatto-2015-entropic-dynamics]], so this paper and the Caticha program are two routes (metric-side vs. entropy-side) to the same Schrödinger endpoint. For PIFB's Level-3 "physics from information" claim, Reginatto is the existence proof that the move is mathematically real, not merely suggestive.

## Cross-links

- Concept: [[Fisher information metric]] — the functional extremized here.
- Concept: [[Mass as Fisher information]] — the project's identification of inertia with Fisher info.
- Theme: [[Physics from Fisher information]], [[Information geometry and natural gradient]].
- Sources: [[caticha-2019-entropic-dynamics]], [[caticha-bartolomeo-reginatto-2015-entropic-dynamics]], [[frieden-1998-physics-fisher]].
- Manuscript: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@article{reginatto1998derivation,
  author  = {Reginatto, Marcel},
  title   = {Derivation of the equations of nonrelativistic quantum mechanics using the principle of minimum Fisher information},
  journal = {Physical Review A},
  volume  = {58},
  number  = {3},
  pages   = {1775--1778},
  year    = {1998},
  publisher = {American Physical Society},
  doi     = {10.1103/PhysRevA.58.1775}
}
```
