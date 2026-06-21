---
type: paper
title: "Entanglement Renormalization"
aliases:
  - "Vidal 2007"
  - "MERA"
authors:
  - Guifré Vidal
year: 2007
arxiv: cond-mat/0512165
url: https://arxiv.org/abs/cond-mat/0512165
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

# Entanglement Renormalization

> [!info] Citation
> Guifré Vidal (2007). "Entanglement renormalization." *Physical Review Letters* 99(22): 220405. DOI: [10.1103/PhysRevLett.99.220405](https://doi.org/10.1103/PhysRevLett.99.220405). Preprint: [arXiv:cond-mat/0512165](https://arxiv.org/abs/cond-mat/0512165).

## TL;DR

Vidal introduces the multi-scale entanglement renormalization ansatz (MERA): a coarse-graining transformation for quantum lattice systems that, before each blocking step, applies local *disentanglers* to remove short-range entanglement, so that the renormalization flow does not accumulate spurious correlations. Iterating disentangle-then-coarse-grain builds a layered tensor network — one layer per length scale — whose geometry literally is a discretized extra (renormalization) dimension. MERA is the structural origin of the tensor-network picture of holography (later read as an emergent bulk by [[swingle-2012-entanglement-renormalization-holography|swingle-2012-entanglement-renormalization]]).

## Problem & setting

Standard real-space RG (block-spin) fails for critical systems because it does not handle the entanglement that proliferates across scales. The setting is the ground state of a quantum many-body Hamiltonian on a lattice; the goal is an efficient, scale-resolved representation.

## Method

A MERA alternates two local unitary/isometric operations per layer: disentanglers acting across block boundaries to strip inter-block entanglement, and isometries that coarse-grain blocks into effective sites. The number of layers grows logarithmically with system size; the causal-cone structure makes expectation values efficiently computable.

## Key results

MERA captures critical (scale-invariant) ground states with logarithmic entanglement scaling, gives a constructive entanglement-aware RG, and — by giving the network an explicit extra-dimensional geometry — seeds the idea that a bulk geometry can emerge from the entanglement structure of a boundary state.

## Relevance to this research

MERA is a direct structural cousin of the program's **Ouroboros Tower**: both are stacks of gauge-covariant coarse-grainings, one rung per scale, where the entanglement/correlation removed by disentanglers corresponds to the program's covariant pooling of constituents into meta-agents. Vidal's disentangle-then-block step is the quantum analogue of the [[Renormalization-group flow of beliefs]] that PIFB ([[participatory-it-from-bit]]) runs vertically through its scale tower (see [[Ouroboros multi-scale dynamics]] and [[Meta-agents and hierarchical emergence]]). Because MERA's layered geometry is the seed of emergent-spacetime tensor-network holography, it ties the program's multi-scale machinery to the [[Emergent spacetime and holography]] theme and, through Swingle, to the [[Participatory realism (it from bit)]] reading that geometry is built from informational structure.

## Cross-links
- Concepts: [[Renormalization-group flow of beliefs]], [[Ouroboros multi-scale dynamics]], [[Meta-agents and hierarchical emergence]]
- Themes: [[Emergent spacetime and holography]], [[Participatory realism (it from bit)]]
- Related sources: [[swingle-2012-entanglement-renormalization-holography|swingle-2012-entanglement-renormalization]], [[ryu-takayanagi-2006-holographic-entanglement-entropy]], [[wilson-1975-renormalization-group]], [[VanRaamsdonk-2010-spacetime-entanglement|vanraamsdonk-2010-entanglement-spacetime]]

## BibTeX
```bibtex
@article{vidal2007entanglement,
  author  = {Vidal, Guifr\'e},
  title   = {Entanglement Renormalization},
  journal = {Physical Review Letters},
  year    = {2007},
  volume  = {99},
  number  = {22},
  pages   = {220405},
  doi     = {10.1103/PhysRevLett.99.220405},
  eprint  = {cond-mat/0512165},
  archivePrefix = {arXiv},
  primaryClass  = {cond-mat.str-el}
}
```
