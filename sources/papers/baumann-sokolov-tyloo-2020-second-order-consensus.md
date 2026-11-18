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

Baumann, Sokolov, and Tyloo show that small periodic modulations of coupling can prevent consensus in established second-order multi-agent network dynamics. Spectral decomposition reveals a parametric-resonance band at intermediate driving frequencies, with the resonances set by the Laplacian spectrum of the underlying network.
## Problem & setting

Second-order consensus models describe agents with both state and rate variables and ordinarily relax toward collective agreement under suitable coupling. The paper asks whether consensus remains robust when the network coupling varies periodically in time. The focus is a multi-agent network with a static backbone whose coupling strength receives a small temporal modulation.

## Method

The authors decompose the dynamics into eigenmodes of the static network Laplacian. Each mode becomes a parametrically driven second-order equation, allowing the resonance conditions and growth rates to be calculated analytically. They extend standard parametric-resonance theory to the network setting and quantify excitation as a function of modulation frequency and network spectrum.

## Key results

Very slow and very fast coupling modulation preserve the expected approach to consensus, but intermediate frequencies can excite network modes and inhibit agreement. The theory predicts resonance frequencies from Laplacian eigenvalues and quantifies the resulting instability. The work thereby ties second-order collective dynamics, time-dependent coupling, and network resonance together in a tractable analytic framework.

## Cross-links

The paper belongs with [[Opinion dynamics]] and [[Statistical physics of social systems and collective behavior]]. Its spectral mechanism complements [[olfati-saber-2007-consensus]].

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
