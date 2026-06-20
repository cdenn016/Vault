---
type: reference
title: "Quarks, Gluons and Lattices"
aliases:
  - "Creutz 1983"
  - "Creutz (1983) Quarks, Gluons and Lattices"
authors:
  - Michael Creutz
year: 1983
tags:
  - cluster/gauge-theory
  - cluster/multi-agent
  - project/multi-agent
  - field/physics
created: 2026-06-19
updated: 2026-06-19
---

# Quarks, Gluons and Lattices

> [!info] Citation
> Michael Creutz (1983). *Quarks, Gluons and Lattices.* Cambridge Monographs on Mathematical Physics. Cambridge University Press. ISBN: 9780521244053.

## TL;DR

The first textbook on lattice gauge theory, written by one of the pioneers of its Monte Carlo simulation. Creutz develops the link-variable formulation, the plaquette action, gauge-invariant Wilson-loop observables, and the practical machinery for computing them numerically — strong-coupling expansions, the continuum limit, and Markov-chain sampling of gauge configurations. It is the methodology reference for measuring curvature and confinement-type observables on a lattice gauge field.

## What it establishes

Building on [[wilson-1974-confinement-quarks]], the book treats the lattice as a non-perturbative regulator: link variables $U_{x,\mu}\in G$ carry parallel transport, the plaquette product measures local curvature, and the Wilson loop $\langle W(C)\rangle$ diagnoses confinement through its area- vs. perimeter-law behavior. It lays out the numerical toolkit — heat-bath and Metropolis updates of links, extraction of the string tension, and approaching the continuum limit by tuning the bare coupling — that turned lattice gauge theory into a quantitative computational discipline.

## Why the project cites it

The project evolves a lattice connection (edge twists) and needs gauge-invariant ways to *measure* the resulting curvature and holonomy. Creutz supplies the standard Wilson-loop / plaquette methodology for exactly that: the plaquette holonomy as a curvature diagnostic and the Wilson loop as a gauge-invariant observable are the tools for quantifying when the project's connection has become genuinely [[Non-flat connection and the photon analogy|non-flat]] (Regime II). The numerical-update perspective also informs how the M-step lattice-connection dynamics relate to sampling a gauge action. Pairs with [[wilson-1974-confinement-quarks]] (the link variable and action) and [[kogut-susskind-1975-hamiltonian-lattice-gauge]] (the Hamiltonian/dynamical formulation). Manuscript thread: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@book{creutz1983quarks,
  author    = {Creutz, Michael},
  title     = {Quarks, Gluons and Lattices},
  series    = {Cambridge Monographs on Mathematical Physics},
  publisher = {Cambridge University Press},
  year      = {1983},
  isbn      = {9780521244053}
}
```
