---
type: paper
title: "Renormalisation-group calculations of finite systems: order parameter and specific heat for epitaxial ordering"
aliases:
  - "Berker Ostlund 1979"
  - "hierarchical lattices"
authors:
  - Berker A.N.
  - Ostlund S.
year: 1979
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/physics
created: 2026-08-17
updated: 2026-08-17
---

# Renormalisation-group calculations of finite systems (hierarchical lattices)

> [!info] Citation
> A.N. Berker, S. Ostlund (1979). "Renormalisation-group calculations of finite systems: order
> parameter and specific heat for epitaxial ordering." *Journal of Physics C: Solid State
> Physics* **12**(22), 4961–4975. DOI:
> [10.1088/0022-3719/12/22/035](https://doi.org/10.1088/0022-3719/12/22/035).

## TL;DR

Introduces the lattices on which the Migdal–Kadanoff recursion
([[kadanoff-1976-migdal-recursion]]) is **exact** rather than approximate: hierarchical
lattices, built by recursively replacing each bond with a fixed cluster of bonds. On these
self-similar graphs the real-space RG map composes exactly by construction, and nontrivial
fixed points with genuine critical behavior exist.

## What it establishes

Exact real-space renormalization is possible when — and essentially only when — the substrate is
built self-similarly, so that one recursion step undoes one construction step. Hierarchical
lattices are directed self-similar multigraph families, not spatial lattices: each coarse bond
aggregates a declared bundle of fine bonds, and the bundle multiplicity is what sustains an
interacting fixed point.

## Relevance to this research

The closest ancestor of the nested-cycle tower in the MultiAgentELBO rescaling laboratory, and
the network-native precedent for its next question. The tower's single-boundary-agent joins make
its instances quasi-one-dimensional, which is why its measured fixed structures are factorized;
hierarchical lattices show that raising boundary multiplicity — bundles of parallel cross-paths
per coarse edge — is how a $\beta_{ij}$ architecture sustains a renormalized coupling that
survives iteration. This reframes "critical dimension" as an architecture property of directed
agent networks. See [[Staged hierarchy formation and RG composability]] and
[[Renormalization group flow]].

## BibTeX

```bibtex
@article{berker1979renormalisation,
  author  = {Berker, A. Nihat and Ostlund, Stellan},
  title   = {Renormalisation-group calculations of finite systems: order parameter and specific
             heat for epitaxial ordering},
  journal = {Journal of Physics C: Solid State Physics},
  volume  = {12},
  number  = {22},
  pages   = {4961--4975},
  year    = {1979},
  doi     = {10.1088/0022-3719/12/22/035}
}
```
