---
type: reference
title: "Geometry, Topology and Physics (Second Edition)"
aliases: ["Nakahara 2003", "Nakahara GTP"]
authors: ["Mikio Nakahara"]
year: 2003
tags: [cluster/gauge-theory, project/transformer, project/multi-agent, field/physics, field/mathematics]
created: 2026-06-18
updated: 2026-06-18
---

# Geometry, Topology and Physics (Second Edition)

> [!info] Citation
> Mikio Nakahara (2003). *Geometry, Topology and Physics*, Second Edition. Graduate Student Series in Physics. Bristol and Philadelphia: Institute of Physics Publishing (IOP / CRC Press). ISBN 0-7503-0606-8.

## TL;DR

Nakahara's *Geometry, Topology and Physics* is a standard graduate-level textbook that develops the differential-geometric and topological machinery of modern physics — manifolds, differential forms, fibre bundles, connections, curvature, holonomy, and characteristic classes — in a unified and physics-oriented language. It is the project's primary reference for the fibre-bundle and gauge-connection formalism on which the gauge-theoretic constructions are built.

## What it establishes

The book provides self-contained, pedagogical treatments of the core objects used throughout the gauge-theoretic side of the project:

- **Smooth manifolds, tangent/cotangent spaces, and differential forms**, with the exterior derivative and integration on manifolds.
- **Lie groups and Lie algebras** as the structure groups of physical theories, including the exponential map and the adjoint action.
- **Fibre bundles** — principal bundles and associated vector bundles — as the geometric setting in which gauge fields live.
- **Connections, the connection one-form, and curvature**, identifying the gauge potential with a connection and the field strength with its curvature.
- **[[Parallel transport]] and [[Holonomy]]**, including the holonomy group of a connection and the relation between curvature and infinitesimal holonomy.
- **[[Gauge transformation]]s** as changes of local trivialization / local frame, and the transformation laws of connection and curvature.
- **Characteristic classes** (Chern, Pontryagin, Euler) and index theorems, tying local curvature data to global topological invariants.

These are presented in the standard mathematical-physics idiom, alongside companion treatments in [[kobayashi-nomizu-1963-foundations]], [[baez-muniain-1994-gauge-fields]], and [[frankel-2011-geometry-of-physics]], and grounded in the original gauge theory of [[yang-mills-1954]].

## Why the project cites it

The project models agents and their beliefs in an explicitly geometric, gauge-theoretic frame, and Nakahara supplies the rigorous definitions behind that frame.

- **Agents as bundle sections.** The construction of [[Agents as fibre-bundle sections]] takes the principal/associated-bundle picture from this text directly: each agent is a local section, and the choice of section is a [[Gauge transformation]]. Nakahara's treatment of local trivializations and transition functions is the mathematical backbone here.
- **Belief transport and holonomy.** Comparing beliefs across an agent network requires a connection. The project's use of [[Parallel transport]] of beliefs and the path-dependent mismatch measured by [[Holonomy]] rests on Nakahara's connection/curvature formalism — non-zero curvature is precisely the obstruction to consistent transport. This underpins the [[belief-inertia]] manuscript's notion of [[Belief inertia]] and the role of the connection in [[Hamiltonian belief dynamics]].
- **Equivariance and structure groups.** The text's Lie-group and representation material supports the geometric-deep-learning side of the [[VFE Transformer Program]] — [[Group equivariance]], [[Irreducible representation]]s, and the structure-group viewpoint behind a [[Gauge equivariant CNN]] and [[Steerable CNN]].
- **Bridge to information geometry.** Where the project's metric structure is the [[Fisher information metric]] (see [[ay-2017-information-geometry]], [[amari-2016-information-geometry-applications]]), Nakahara furnishes the underlying language of connections and parallel transport on manifolds that information geometry specializes to the statistical setting, informing constructions such as [[Mass as Fisher information]].

In short, this reference is cited wherever the manuscripts need the precise, standard definition of a bundle, connection, curvature, holonomy, or gauge transformation, within the broader theme of [[Gauge equivariance and geometric deep learning]].

```bibtex
@book{nakahara2003geometry,
  author    = {Nakahara, Mikio},
  title     = {Geometry, Topology and Physics},
  edition   = {2nd},
  series    = {Graduate Student Series in Physics},
  publisher = {Institute of Physics Publishing},
  address   = {Bristol and Philadelphia},
  year      = {2003},
  isbn      = {978-0-7503-0606-5}
}
```
