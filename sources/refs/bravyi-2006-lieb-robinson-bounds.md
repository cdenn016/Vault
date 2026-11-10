---
type: reference
title: "Lieb-Robinson Bounds and the Generation of Correlations and Topological Quantum Order"
aliases: ["bravyi2006lieb"]
authors: ["S. Bravyi", "M. B. Hastings", "F. Verstraete"]
year: 2006
venue: "Physical Review Letters"
doi: "10.1103/PhysRevLett.97.050401"
arxiv: "quant-ph/0603121"
url: "https://doi.org/10.1103/PhysRevLett.97.050401"
tags: [cluster/multi-agent, project/multi-agent, field/physics]
created: 2026-11-10
updated: 2026-11-10
---

# Lieb-Robinson Bounds and the Generation of Correlations and Topological Quantum Order

> [!info] Citation
> Bravyi, S., Hastings, M. B., Verstraete, F. (2006). *Lieb-Robinson Bounds and the Generation of Correlations and Topological Quantum Order*. Physical Review Letters, 97(5), 050401. [DOI](https://doi.org/10.1103/PhysRevLett.97.050401); [arXiv](https://arxiv.org/abs/quant-ph/0603121)

[Local PDF](../pdfs/bravyi-2006-lieb-robinson-bounds.pdf), 5 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper draws consequences of the Lieb-Robinson bound, an effective light cone with exponentially decaying tails for local Hamiltonian evolution, for the speed at which correlations and entanglement can be generated.

## Problem & setting

The introduction contrasts relativistic theories, where a light cone is automatic, with non-relativistic quantum mechanics, where a strict light cone does not exist. It describes the Lieb-Robinson bound, with generalizations by Hastings and by Nachtergaele and Sims, as giving an effective light cone for evolution under local Hamiltonians, so that information exchanged between regions not connected by the cone is exponentially small.

## Method

The authors work in the setting of quantum information theory and apply the bound to three questions: leakage of information to space-like separated regions, lower bounds on the time to convert states without topological quantum order into states with it, and the rate of entropy creation in a block of spins.

## Key results

The abstract states that information leaking to space-like separated regions is negligible, that correlations and entanglement are distributed at a finite speed, and that the rate at which entropy can be created in a block of spins scales with the boundary of the block.

## Relevance to this research

The collective-agents manuscript cites this paper for the finite speed at which correlations are generated, as a quantum counterpart of its own exact discrete-time statements about how fast correlation can spread among communicating members, and again in related work next to other Lieb-Robinson results. The connection to the vault is the limit that local, bounded-range communication places on the growth of correlation across a collective, see [[Communication-constrained inference]], [[Quantum information]], [[Entanglement entropy]] and [[Critical Phenomena]].

## Cross-links

[[Collective agents literature map]]; [[Communication-constrained inference]]; [[Quantum information]]; [[Entanglement entropy]]; [[Critical Phenomena]].

## BibTeX

```bibtex
@article{bravyi2006lieb,
  author        = {Bravyi, S. and Hastings, M. B. and Verstraete, F.},
  title         = {{Lieb-Robinson} Bounds and the Generation of Correlations and Topological Quantum Order},
  journal       = {Physical Review Letters},
  volume        = {97},
  number        = {5},
  pages         = {050401},
  year          = {2006},
  doi           = {10.1103/PhysRevLett.97.050401},
  eprint        = {quant-ph/0603121},
  archivePrefix = {arXiv}
}
```
