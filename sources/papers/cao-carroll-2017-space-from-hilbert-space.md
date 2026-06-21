---
type: paper
title: "Space from Hilbert Space: Recovering Geometry from Bulk Entanglement"
aliases:
  - "Cao Carroll Michalakis 2017"
  - "Space from Hilbert Space"
authors:
  - Cao, ChunJun
  - Carroll, Sean M.
  - Michalakis, Spyridon
year: 2017
arxiv: 1606.08444
url: https://doi.org/10.1103/PhysRevD.95.024031
tags:
  - cluster/participatory/quantum-foundations
  - project/multi-agent
  - field/physics
  - field/mathematics
status: stable
created: 2026-06-19
updated: 2026-06-20
---

# Space from Hilbert Space: Recovering Geometry from Bulk Entanglement

> [!info] Citation
> Cao, ChunJun, Sean M. Carroll, and Spyridon Michalakis (2017). "Space from Hilbert Space: Recovering Geometry from Bulk Entanglement." *Physical Review D* 95(2): 024031. DOI: [10.1103/PhysRevD.95.024031](https://doi.org/10.1103/PhysRevD.95.024031). Preprint: [arXiv:1606.08444](https://arxiv.org/abs/1606.08444).

## TL;DR

Starting from an abstract, structureless quantum state in a Hilbert space — no background spacetime assumed — the authors ask when the entanglement structure of that state can be read as the geometry of an emergent space. For a class of "redundancy-constrained" states whose entanglement entropies obey area-law-like relations, they construct a graph whose vertices are factors of the Hilbert space and whose edge weights are set by mutual information. A metric and its dimensionality are then recovered from this entanglement graph, so that geometry, locality, and distance are reconstructed entirely from the informational relations among Hilbert-space factors.

## Problem & setting

Most emergent-geometry work (Ryu–Takayanagi, Van Raamsdonk) assumes an AdS/CFT background and a boundary theory. This paper drops the boundary and the background entirely: the only input is a quantum state and a tensor-factorization of Hilbert space. The question is whether geometry can be bootstrapped from entanglement alone, without any prior manifold structure.

## Method

Define mutual information between Hilbert-space factors; build a weighted graph with edge lengths a decreasing function of mutual information; impose the requirement that entanglement entropies satisfy an approximate area law (the redundancy constraint); then extract an emergent spatial metric and dimension from the graph via a multidimensional-scaling-type reconstruction. Perturbations around such states are argued to obey a linearized Einstein-like equation, connecting the framework to the dynamical content of general relativity.

## Key results

A well-defined emergent space with stable dimensionality and an approximate metric arises from the entanglement structure of redundancy-constrained states. The framework is background-independent and observer-internal, making geometry a derived rather than fundamental notion. The mutual-information graph provides a fully relational, informational origin for spatial structure, without reference to a pre-existing manifold.

## Relevance to this research

This paper is the purest "geometry from informational relations, no background" precedent for the research program, and it speaks directly to the participatory it-from-bit (PIFB) framework's scale-0 partition gap: the question of how the bottom rung of the [[Ouroboros multi-scale dynamics]] tower acquires a base manifold at all, rather than inheriting one. Cao, Carroll, and Michalakis answer the analogous question — they build the manifold from mutual-information edges between Hilbert-space factors, exactly as PIFB would build a base from the relational structure among belief fibres, with the [[Fisher information metric]] (rather than entanglement mutual information) supplying the edge weights. The mutual-information graph is the entanglement-side mirror of the VFE program's belief-coupling graph, tying it to [[Emergent spacetime and holography]] and the [[Participatory realism (it from bit)]] thread.

## Cross-links
- Concepts: [[Participatory realism (it from bit)]], [[Fisher information metric]], [[Ouroboros multi-scale dynamics]]
- Themes: [[Emergent spacetime and holography]]
- Related sources: [[vanraamsdonk-2010-entanglement-spacetime]], [[ryu-takayanagi-2006-holographic-entanglement-entropy]], [[jacobson-2016-entanglement-equilibrium]], [[wheeler-1990-it-from-bit]]
- Manuscript/Project: [[participatory-it-from-bit]]

## BibTeX
```bibtex
@article{Cao2017,
  author        = {Cao, ChunJun and Carroll, Sean M. and Michalakis, Spyridon},
  title         = {Space from {Hilbert} Space: Recovering Geometry from Bulk Entanglement},
  journal       = {Physical Review D},
  year          = {2017},
  volume        = {95},
  number        = {2},
  pages         = {024031},
  doi           = {10.1103/PhysRevD.95.024031},
  eprint        = {1606.08444},
  archivePrefix = {arXiv},
  primaryClass  = {hep-th},
}
```
