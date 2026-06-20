---
type: reference
title: "Lie Algebras in Particle Physics: From Isospin to Unified Theories"
aliases: ["Georgi 1999", "Lie Algebras in Particle Physics"]
authors: ["Howard Georgi"]
year: 1999
tags: [cluster/gauge-theory, project/transformer, project/multi-agent, field/physics, field/mathematics]
created: 2026-06-20
updated: 2026-06-20
---

# Lie Algebras in Particle Physics: From Isospin to Unified Theories

> [!info] Citation
> Georgi, H. (1999). *Lie Algebras in Particle Physics: From Isospin to Unified Theories*, 2nd ed. Frontiers in Physics, Vol. 54. Perseus Books (Westview Press), Reading, MA. ISBN 978-0-7382-0233-4.

## TL;DR

A physicist's working manual for **Lie algebras and their representations**, built around the practical machinery of decomposing tensor products, using roots and weights, and applying $SU(N)$ representation theory. It is computation-first where [[fulton-harris-1991-representation-theory|Fulton–Harris]] and [[hall-2015-lie-groups|Hall]] are structure-first: Georgi teaches how to *use* irreps — Young tableaux, weight diagrams, Dynkin labels, and explicit [[Clebsch-Gordan coefficients|Clebsch–Gordan]] decompositions — to reduce a representation into [[Irreducible representation|irreducibles]].

## What it establishes

Standard but thoroughly worked: the structure of simple Lie algebras via roots, the [[Killing form|Cartan–Killing]] classification, highest-weight representations, tensor-product decomposition and branching rules, and the $SU(2)\subset SU(3)\subset\dots$ chain culminating in grand-unified $SU(5)/SO(10)$ model building. The recurring deliverable is the explicit reduction $V_\lambda\otimes V_\mu = \bigoplus_\nu N^\nu_{\lambda\mu} V_\nu$ and the tools to compute the multiplicities.

## Why the project cites it

The program's gauge-theoretic core rests on group/representation structure — the block-$GL(K)$ form of [[VFE Transformer Program|GL(K) attention]] and the [[Gauge transformation|gauge action]] on belief frames — and Georgi is the practical reference for the irrep-decomposition arithmetic that underlies it: how a representation splits into [[Irreducible representation|irreducibles]], how tensor products reduce, and how [[Clebsch-Gordan coefficients|Clebsch–Gordan]] data organizes equivariant maps. It complements the more abstract [[fulton-harris-1991-representation-theory|Fulton–Harris]]/[[hall-2015-lie-groups|Hall]] references already in the vault by supplying the explicit, computational side the equivariance constructions ([[Group equivariance]]) lean on.

> [!note] Editorial: Cited as a computational representation-theory reference complementing the abstract treatments already in the vault; the program uses its irrep-decomposition and Clebsch–Gordan machinery, not its particle-physics model-building.

```bibtex
@book{georgi1999lie,
  author    = {Georgi, Howard},
  title     = {Lie Algebras in Particle Physics: From Isospin to Unified Theories},
  edition   = {2nd},
  series    = {Frontiers in Physics},
  volume    = {54},
  publisher = {Perseus Books},
  address   = {Reading, MA},
  year      = {1999},
  isbn      = {978-0-7382-0233-4}
}
```
