---
type: paper
title: "Notes on Migdal's recursion formulas"
aliases:
  - "Kadanoff 1976"
  - "Migdal-Kadanoff"
  - "bond moving"
authors:
  - Kadanoff L.P.
year: 1976
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/physics
created: 2026-08-17
updated: 2026-08-17
---

# Notes on Migdal's recursion formulas

> [!info] Citation
> L.P. Kadanoff (1976). "Notes on Migdal's recursion formulas." *Annals of Physics* **100**(1),
> 359–394. DOI: [10.1016/0003-4916(76)90066-X](https://doi.org/10.1016/0003-4916(76)90066-X).

## TL;DR

Rederives Migdal's approximate real-space recursion relations through a potential-moving
(bond-moving) scheme, connecting them to decimation and block transformations, and shows the
approximation becomes exact for strong ferromagnetic potentials. Together with
[[berker-1979-hierarchical-lattice-rg]], establishes that the Migdal–Kadanoff recursion is the
exact RG of hierarchical lattices.

## What it establishes

The bond-moving construction: an uncontrolled approximation on regular lattices that is
simultaneously the exact recursion of a self-similar graph family. The composability of the
recursion is inherited from the graph construction, not from the physics.

## Relevance to this research

Supplies the mechanism reading for why the MultiAgentELBO tower's coarse maps fail to compose
(C3) while hierarchical-lattice maps compose exactly: composability is purchased by building
the substrate so one blocking step inverts one construction step. The tower is self-similar in
that sense, but its blocking kernels (Bayes posteriors under a declared parent law) are not
closed under composition the way bond-moving recursions are — the closure lives in the kernel
family, not only in the graph. See [[Staged hierarchy formation and RG composability]].

## BibTeX

```bibtex
@article{kadanoff1976migdal,
  author  = {Kadanoff, Leo P.},
  title   = {Notes on {M}igdal's recursion formulas},
  journal = {Annals of Physics},
  volume  = {100},
  number  = {1},
  pages   = {359--394},
  year    = {1976},
  doi     = {10.1016/0003-4916(76)90066-X}
}
```
