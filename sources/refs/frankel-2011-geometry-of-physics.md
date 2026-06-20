---
type: reference
title: "The Geometry of Physics: An Introduction"
aliases:
  - "Frankel 2011"
  - "Frankel, Geometry of Physics"
authors:
  - "Theodore Frankel"
year: 2011
tags:
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/physics
created: 2026-06-18
updated: 2026-06-18
---

# The Geometry of Physics: An Introduction

> [!info] Citation
> Theodore Frankel. *The Geometry of Physics: An Introduction.* 3rd edition. Cambridge University Press, 2011. ISBN 978-1-107-60260-1.

## TL;DR

Frankel's text is a physicist-facing introduction to the geometric machinery underlying modern physics: exterior differential forms, smooth manifolds, Lie groups and their algebras, fiber bundles, connections, curvature, and the associated topological invariants. The third edition is notable for opening with an Overview that previews these concepts and for its sustained treatment of gauge theory as the geometry of connections on principal and associated bundles. It serves the project as a single coherent reference for the differential-geometric and gauge-theoretic vocabulary that the manuscripts build on.

## What it establishes

The book develops, from a working-physicist standpoint, the core apparatus of differential geometry and its physical applications:

- **Exterior calculus and manifolds.** Differential forms, the exterior derivative, integration on manifolds, Stokes' theorem, and de Rham cohomology, presented as the natural language for field theory and conservation laws.
- **Lie groups and Lie algebras.** Matrix groups, the exponential map, the [[Killing form]], invariant forms, and the relation between a group and its algebra — the structures behind continuous symmetry in physics.
- **Fiber bundles and connections.** Principal and associated bundles, connections (gauge potentials) and curvature (field strengths), [[Parallel transport]], and [[Holonomy]] around loops, framing gauge symmetry geometrically.
- **Gauge theory.** A [[Gauge transformation]] as a change of local section/trivialization, with the Yang–Mills construction presented as curvature of a bundle connection.
- **Topology and characteristic classes.** Chern and other characteristic forms relating curvature to global topological invariants.

> [!note] Editorial: This is a textbook; it is cited for definitions and standard constructions rather than for novel results of its own.

## Why the project cites it

The project recasts belief dynamics and inference in explicitly geometric, gauge-theoretic terms, and Frankel supplies the canonical definitions for that recasting.

- **Gauge structure of belief.** The manuscripts treat agents and their belief states as living on bundles — see [[Agents as fibre-bundle sections]] — so the bundle/connection/curvature framework and the notions of [[Parallel transport]] and [[Holonomy]] are exactly Frankel's subject matter. The project's use of a [[Gauge transformation]] to express frame-dependence of beliefs inherits this vocabulary, sitting within the broader theme of [[Gauge equivariance and geometric deep learning]].
- **Lie-group machinery.** Geometric deep-learning components such as [[Steerable CNN]] and [[Group equivariant CNN (G-CNN)]], together with concepts like [[Irreducible representation]] and the [[Baker-Campbell-Hausdorff formula]], rely on the Lie-group and Lie-algebra constructions Frankel lays out, including the [[Killing form]].
- **Bridge to information geometry.** The differential-geometric foundation here underpins the project's information-geometric layer — the [[Fisher information metric]] and [[Natural gradient]] — where beliefs evolve on a curved statistical manifold, connecting the gauge picture to [[Variational free energy]] and the theme of [[Information geometry and natural gradient]].
- **Foundational reference.** Frankel complements the project's other geometry sources ([[kobayashi-nomizu-1963-foundations]], [[nakahara-2003-geometry-topology-physics]], [[baez-muniain-1994-gauge-fields]], [[hall-2015-lie-groups]]) as the accessible, physics-oriented entry point to the same material.

## BibTeX

```bibtex
@book{frankel2011geometry,
  author    = {Frankel, Theodore},
  title     = {The Geometry of Physics: An Introduction},
  edition   = {3},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {2011},
  isbn      = {978-1-107-60260-1}
}
```
