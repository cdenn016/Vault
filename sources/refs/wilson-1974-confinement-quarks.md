---
type: reference
title: "Confinement of Quarks"
aliases:
  - "Wilson 1974"
  - "Wilson (1974) Confinement of Quarks"
authors:
  - Kenneth G. Wilson
year: 1974
tags:
  - cluster/gauge-theory
  - cluster/multi-agent
  - project/multi-agent
  - field/physics
created: 2026-06-19
updated: 2026-06-19
---

# Confinement of Quarks

> [!info] Citation
> Kenneth G. Wilson (1974). "Confinement of quarks." *Physical Review D* **10**(8), 2445–2459. DOI: [10.1103/PhysRevD.10.2445](https://doi.org/10.1103/PhysRevD.10.2445).

## TL;DR

Wilson formulates gauge theory on a spacetime lattice, replacing the continuum connection by *link variables* $U_{x,\mu} = \exp(i a g A_\mu(x)) \in G$ living on the edges between neighboring sites, and builds the gauge action from products of link variables around plaquettes (Wilson loops). The lattice regularization makes gauge theory non-perturbatively well defined and lets him show, in the strong-coupling limit, that the static quark potential rises linearly with separation — quark confinement. The link variable he introduces is precisely the discrete parallel-transport object the project identifies with its edge-relaxed belief transport.

## What it establishes

By discretizing spacetime, Wilson assigns a group element $U_{x,\mu}$ to each oriented link, so a path's parallel transport is the ordered product of links along it and gauge invariance is exact on the lattice. The action is a sum over plaquettes of $\mathrm{Re}\,\mathrm{tr}(U_{\mathrm{plaq}})$, where the plaquette holonomy measures the lattice curvature. In the strong-coupling expansion the Wilson loop expectation obeys an *area law*, $\langle W(C)\rangle \sim e^{-\sigma A(C)}$, whose string tension $\sigma$ encodes a linearly confining potential — the lattice demonstration that confinement can arise non-perturbatively. The construction also provides the standard numerical (lattice QCD) route to gauge-theory observables.

## Why the project cites it

The PIFB construction promotes the flat belief transport $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ to a genuinely non-flat connection in "Regime II," where edge twists relax and the transport around a loop no longer returns to the identity. The object carrying that holonomy is exactly Wilson's lattice link variable: the project's edge-relaxed transport is a link variable $U_{x,\mu}\in GL^{+}(K)$, and the plaquette holonomy is the lattice curvature signaling [[Non-flat connection and the photon analogy|a non-flat connection]]. Wilson (1974) is therefore the origin reference for the lattice-gauge object the model's connection dynamics step (the M-step lattice-connection update) evolves. The plaquette / Wilson-loop construction also supplies the natural gauge-invariant observable for measuring emergent curvature in the agent network. Pairs with [[kogut-susskind-1975-hamiltonian-lattice-gauge]] (the continuous-time formulation the M-step dynamics mirror), [[creutz-1983-quarks-gluons-lattices]] (numerics), and the foundational [[yang-mills-1954]]. Manuscript thread: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@article{wilson1974confinement,
  author  = {Wilson, Kenneth G.},
  title   = {Confinement of quarks},
  journal = {Physical Review D},
  volume  = {10},
  number  = {8},
  pages   = {2445--2459},
  year    = {1974},
  doi     = {10.1103/PhysRevD.10.2445},
  publisher = {American Physical Society}
}
```
