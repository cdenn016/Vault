---
type: reference
title: "Gauge Fields, Knots and Gravity"
aliases: ["Baez 1994", "Baez & Muniain 1994", "Gauge Fields, Knots and Gravity"]
authors: ["John C. Baez", "Javier P. Muniain"]
year: 1994
tags: [cluster/gauge-theory, project/transformer, project/multi-agent, field/physics, field/mathematics]
created: 2026-06-18
updated: 2026-06-18
---

# Gauge Fields, Knots and Gravity

> [!info] Citation
> John C. Baez and Javier P. Muniain (1994). *Gauge Fields, Knots and Gravity*. Series on Knots and Everything, Vol. 4. World Scientific, Singapore. 480 pp. ISBN 978-981-02-2034-1 (softcover).

## TL;DR

A pedagogical introduction to the differential-geometric machinery of modern gauge theory, building from manifolds and differential forms up through fibre bundles, connections, curvature, Yang-Mills theory, and Riemannian geometry for general relativity. It is prized for developing the abstract apparatus, principal/vector bundles, connections, [[Parallel transport]], [[Holonomy]], and gauge symmetry, with unusual clarity and minimal prerequisites.

## What it establishes

The book is structured as a guided ascent through the geometry underlying field theory. It first treats smooth manifolds and the exterior calculus of differential forms, showing how Maxwell's equations take their natural coordinate-free form on an arbitrary spacetime. It then generalizes to non-abelian gauge theory by introducing vector and principal bundles, connections, and curvature, from which the Yang-Mills equations follow. Key geometric notions developed along the way include:

- The connection as the object defining [[Parallel transport]] of sections along curves, and curvature as its infinitesimal failure to commute.
- [[Holonomy]] as the net transformation accumulated by parallel transport around a closed loop, the gauge-invariant content of a connection.
- The [[Gauge transformation]] as a change of local trivialization (frame) acting on bundle sections, and the corresponding transformation law for connection and curvature.
- Lie groups and Lie algebras as the structure groups of bundles, with the [[Killing form]] supplying the invariant inner product used to build gauge-invariant Lagrangians.

The later chapters introduce Riemannian geometry to formulate Einstein's equations and sketch the connection to knot invariants (the Jones polynomial) arising in attempts to quantize gravity, which gives the volume its title.

## Why the project cites it

This work is the project's standard reference for the fibre-bundle and connection language that underpins the gauge-theoretic reading of belief dynamics. The central modeling move, treating [[Agents as fibre-bundle sections]], borrows exactly the bundle/section/connection vocabulary that Baez and Muniain develop from scratch. In that picture an agent's belief is a section of a statistical bundle, inference across context is [[Parallel transport]] of that section, and the path-dependence of belief updating is [[Holonomy]], the same loop-holonomy construction the book uses to extract the gauge-invariant content of a connection. The requirement that the model's predictions be independent of arbitrary local frame choices is precisely a [[Gauge transformation]] covariance condition in the book's sense.

The same geometric apparatus grounds the project's [[Group equivariance]] machinery on the deep-learning side: the [[Gauge equivariant CNN]] and related architectures realize, on a manifold or discrete grid, the connection-and-parallel-transport structure formalized here, so the book provides the continuum reference for what gauge equivariance is approximating. Where the project couples this geometry to information geometry, identifying [[Mass as Fisher information]] and treating the [[Fisher information metric]] as the relevant Riemannian structure on belief space, the book's treatment of Riemannian geometry and curvature supplies the differential-geometric foundation that the statistical metric specializes.

> [!note] Editorial: This is a textbook; it is cited for the geometric framework (bundles, connections, holonomy, gauge symmetry) rather than for any specific result the project reproduces.

```bibtex
@book{baez1994gauge,
  author    = {Baez, John C. and Muniain, Javier P.},
  title     = {Gauge Fields, Knots and Gravity},
  series    = {Series on Knots and Everything},
  volume    = {4},
  publisher = {World Scientific},
  address   = {Singapore},
  year      = {1994},
  pages     = {480},
  isbn      = {978-981-02-2034-1},
  doi       = {10.1142/2324}
}
```
