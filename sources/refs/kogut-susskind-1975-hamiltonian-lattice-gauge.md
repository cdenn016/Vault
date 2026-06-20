---
type: reference
title: "Hamiltonian Formulation of Wilson's Lattice Gauge Theories"
aliases:
  - "Kogut & Susskind 1975"
  - "Kogut-Susskind (1975) Hamiltonian Lattice Gauge"
authors:
  - John Kogut
  - Leonard Susskind
year: 1975
tags:
  - cluster/gauge-theory
  - cluster/multi-agent
  - project/multi-agent
  - field/physics
created: 2026-06-19
updated: 2026-06-19
---

# Hamiltonian Formulation of Wilson's Lattice Gauge Theories

> [!info] Citation
> John Kogut and Leonard Susskind (1975). "Hamiltonian formulation of Wilson's lattice gauge theories." *Physical Review D* **11**(2), 395–408. DOI: [10.1103/PhysRevD.11.395](https://doi.org/10.1103/PhysRevD.11.395).

## TL;DR

Kogut and Susskind recast Wilson's Euclidean lattice gauge theory as a *Hamiltonian* with continuous time and a spatial lattice. Time is left continuous while space is discretized, so the dynamical variables are the spatial link group elements $U_{x,\mu}$ and their conjugate electric-field operators, evolving under a lattice Hamiltonian with a magnetic (plaquette) term and an electric term. This continuous-time lattice-gauge formulation is the direct reference for the project's M-step dynamics that *step* the lattice connection in time, rather than sampling it from a static Euclidean action.

## What it establishes

Starting from Wilson's plaquette action, the authors derive the corresponding Hamiltonian by taking the temporal-continuum limit, obtaining $H = \tfrac{g^2}{2}\sum E^2 - \tfrac{1}{g^2}\sum_{\mathrm{plaq}} \mathrm{tr}(U_{\mathrm{plaq}} + \text{h.c.})$ with link variables $U$ and conjugate electric fields $E$ obeying group commutation relations, subject to a Gauss-law constraint enforcing gauge invariance on physical states. The electric term is diagonal in the representation basis; the magnetic term is the lattice curvature. This gives gauge theory the structure of a quantum-mechanical Hamiltonian system with the links as configuration variables — the natural setting for *dynamical* (time-stepped) link evolution.

## Why the project cites it

The project's connection dynamics evolve the lattice link variables (the edge twists $V$) in time during the M-step, treating the gauge connection as a dynamical field rather than a static background. Kogut-Susskind is the continuous-time reference for exactly this: their Hamiltonian, with link group elements as coordinates and a magnetic plaquette term as the curvature energy, is the template for the project's bounded gauge-invariant lattice action and its time-stepping of twists. Where [[wilson-1974-confinement-quarks]] supplies the link variable and the Euclidean action, Kogut-Susskind supply the Hamiltonian / equation-of-motion picture that a *dynamics* (not a sampler) requires, grounding the model's [[Non-flat connection and the photon analogy|non-flat connection]] evolution. Pairs with [[creutz-1983-quarks-gluons-lattices]] for numerics and [[yang-mills-1954]] for the continuum origin. Manuscript thread: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@article{kogut1975hamiltonian,
  author  = {Kogut, John and Susskind, Leonard},
  title   = {Hamiltonian formulation of Wilson's lattice gauge theories},
  journal = {Physical Review D},
  volume  = {11},
  number  = {2},
  pages   = {395--408},
  year    = {1975},
  doi     = {10.1103/PhysRevD.11.395},
  publisher = {American Physical Society}
}
```
