---
type: paper
title: "Periodic Coupling Inhibits Second-Order Consensus on Networks"
aliases:
  - "Second-order consensus resonance (Baumann et al. 2020)"
authors:
  - Fabian Baumann
  - Igor M. Sokolov
  - Melvyn Tyloo
year: 2020
arxiv: 2008.08163
doi: 10.1103/PhysRevE.102.052313
url: https://doi.org/10.1103/PhysRevE.102.052313
tags:
  - cluster/social-physics
  - cluster/social-physics/opinion-dynamics
  - cluster/multi-agent
  - project/social-physics
  - project/multi-agent
  - field/physics
  - field/mathematics
created: 2026-07-12
---

# Periodic Coupling Inhibits Second-Order Consensus on Networks

> [!info] Citation
> Fabian Baumann, Igor M. Sokolov, and Melvyn Tyloo (2020). “Periodic coupling inhibits second-order consensus on networks.” *Physical Review E* 102, 052313. DOI: [10.1103/PhysRevE.102.052313](https://doi.org/10.1103/PhysRevE.102.052313). arXiv: [2008.08163](https://arxiv.org/abs/2008.08163).

## TL;DR

Baumann, Sokolov, and Tyloo show that small periodic modulations of coupling can prevent consensus in established second-order multi-agent network dynamics. Spectral decomposition reveals a parametric-resonance band at intermediate driving frequencies, with the resonances set by the Laplacian spectrum of the underlying network. Second-order consensus and network resonance are therefore established comparators, not new consequences unique to belief inertia.

## Problem & setting

Second-order consensus models describe agents with both state and rate variables and ordinarily relax toward collective agreement under suitable coupling. The paper asks whether consensus remains robust when the network coupling varies periodically in time. The focus is a multi-agent network with a static backbone whose coupling strength receives a small temporal modulation.

## Method

The authors decompose the dynamics into eigenmodes of the static network Laplacian. Each mode becomes a parametrically driven second-order equation, allowing the resonance conditions and growth rates to be calculated analytically. They extend standard parametric-resonance theory to the network setting and quantify excitation as a function of modulation frequency and network spectrum.

## Key results

Very slow and very fast coupling modulation preserve the expected approach to consensus, but intermediate frequencies can excite network modes and inhibit agreement. The theory predicts resonance frequencies from Laplacian eigenvalues and quantifies the resulting instability. The work thereby ties second-order collective dynamics, time-dependent coupling, and network resonance together in a tractable analytic framework.

## Relevance to this research

This paper is a mandatory baseline for oscillation and resonance claims in [[Belief inertia]]. A manuscript cannot treat second-order consensus or resonant loss of agreement as uniquely diagnostic of a Fisher-based kinetic mechanism. Instead, [[Hamiltonian belief dynamics]] needs mechanism-specific predictions that distinguish changes in the belief-space kinetic metric or local VFE stiffness from ordinary parametric excitation through time-dependent coupling.

## Cross-links

The paper belongs with [[Opinion dynamics]], [[Belief inertia]], [[Hamiltonian belief dynamics]], and [[Statistical physics of social systems and collective behavior]]. Its spectral mechanism complements [[olfati-saber-2007-consensus]] and provides a network-resonance comparator for future falsification designs.

## BibTeX

```bibtex
@article{BaumannSokolovTyloo2020,
  author        = {Baumann, Fabian and Sokolov, Igor M. and Tyloo, Melvyn},
  title         = {Periodic Coupling Inhibits Second-Order Consensus on Networks},
  journal       = {Physical Review E},
  volume        = {102},
  number        = {5},
  pages         = {052313},
  year          = {2020},
  doi           = {10.1103/PhysRevE.102.052313},
  eprint        = {2008.08163},
  archivePrefix = {arXiv}
}
```
