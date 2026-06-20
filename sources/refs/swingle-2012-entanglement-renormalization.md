---
type: reference
title: "Entanglement Renormalization and Holography"
aliases:
  - "Swingle 2012"
  - "MERA = Holography"
authors:
  - Brian Swingle
year: 2012
arxiv: 0905.1317
url: https://arxiv.org/abs/0905.1317
tags:
  - cluster/participatory
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
  - field/physics
  - cluster/participatory/quantum-foundations
created: 2026-06-19
updated: 2026-06-19
---

# Entanglement Renormalization and Holography

> [!info] Citation
> Brian Swingle (2012). "Entanglement renormalization and holography." *Physical Review D* 86(6): 065007. DOI: [10.1103/PhysRevD.86.065007](https://doi.org/10.1103/PhysRevD.86.065007). Preprint: [arXiv:0905.1317](https://arxiv.org/abs/0905.1317).

## TL;DR

Swingle observes that Vidal's MERA tensor network ([[vidal-2007-entanglement-renormalization]]), built from a stack of disentangle-then-coarse-grain layers, has the geometry of a discretized anti-de Sitter space: its extra (renormalization) dimension behaves like the holographic bulk radial direction, and minimal cuts through the network reproduce the Ryu–Takayanagi entanglement-entropy scaling. This identifies the entanglement-renormalization scale tower with emergent holographic geometry, giving a concrete, computable tensor-network model of how a bulk spacetime arises from the entanglement structure of a boundary state.

## What it establishes

- The MERA network of a critical 1D state realizes a discrete hyperbolic (AdS-like) geometry, with radial position corresponding to RG scale.
- Minimal-curve cuts through the network reproduce the logarithmic entanglement entropy of the boundary, matching the Ryu–Takayanagi area law ([[ryu-takayanagi-2006-holographic-entanglement-entropy]]).
- Provides the first explicit tensor-network instantiation of emergent holographic spacetime, seeding the holographic-tensor-network program.

## Why the project cites it

PIFB ([[participatory-it-from-bit]]) cites Swingle as the tensor-network/MERA realization of emergent holographic geometry, and it is the most architecturally relevant of the holography references for the program. The MERA scale tower is the structural template for the program's **Ouroboros Tower**: both stack gauge-covariant coarse-grainings, one rung per scale, and in both the geometry of the tower *is* the [[Renormalization-group flow of beliefs]] ([[Ouroboros multi-scale dynamics]], [[Meta-agents and hierarchical emergence]]). Swingle's "RG depth = bulk radial coordinate" is the precedent PIFB leans on when it asks whether its own scale index can play the role of an emergent dimension, and the minimal-cut/RT correspondence is the entanglement-side mirror of belief-coupling cuts in the program's coupling graph. It is a HIGH-priority node bridging the [[Emergent spacetime and holography]] theme to the program's multi-scale machinery, and is dual-tagged for the transformer project because the same MERA architecture motivates scale-tower readings there.

```bibtex
@article{swingle2012entanglement,
  author  = {Swingle, Brian},
  title   = {Entanglement renormalization and holography},
  journal = {Physical Review D},
  year    = {2012},
  volume  = {86},
  number  = {6},
  pages   = {065007},
  doi     = {10.1103/PhysRevD.86.065007},
  eprint  = {0905.1317},
  archivePrefix = {arXiv},
  primaryClass  = {hep-th}
}
```
