---
type: paper
title: "Measuring Thermodynamic Length"
aliases:
  - "Crooks 2007"
  - "Crooks (2007) Thermodynamic Length"
authors:
  - Gavin E. Crooks
year: 2007
arxiv: null
url: https://doi.org/10.1103/PhysRevLett.99.100602
tags:
  - cluster/info-geometry
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/statistics
  - cluster/participatory/quantum-foundations
status: stable
created: 2026-06-19
updated: 2026-06-20
---

# Measuring Thermodynamic Length

> [!info] Citation
> Gavin E. Crooks (2007). "Measuring Thermodynamic Length." *Physical Review Letters* 99(10): 100602. DOI: [10.1103/PhysRevLett.99.100602](https://doi.org/10.1103/PhysRevLett.99.100602).

## TL;DR

Crooks shows that the *thermodynamic length* of a quasi-static path through a system's parameter space — measured with the [[Fisher information metric|Fisher–Rao]] metric (equivalently the metric of second derivatives of the free energy) — lower-bounds the dissipation incurred along that path. Moving slowly along a geodesic of the Fisher metric minimizes excess work; the squared length over the available time bounds the entropy produced. Fisher arc length is given a direct thermodynamic cost.

## Problem & setting

When a system is driven through a sequence of near-equilibrium states by varying external control parameters $\lambda$, how much energy is irreversibly dissipated along a finite-time protocol, and which paths minimize it? Earlier work (Weinhold, Ruppeiner, Salamon–Berry) had introduced a "thermodynamic length" as a metric on the space of equilibrium states; Crooks ties this length directly to the [[Fisher information metric|Fisher information]] of the underlying distribution and to a sharp lower bound on dissipation.

## Method

The thermodynamic metric is identified with the Fisher information metric of the equilibrium (Gibbs) distribution in the control parameters $\lambda$ — equivalently the Hessian of the free energy, or the covariance matrix of the conjugate forces, $g_{ij}(\lambda)=\langle \delta X_i\,\delta X_j\rangle$. The thermodynamic *length* of a protocol is its arc length $L=\int \sqrt{\dot{\lambda}^{i} g_{ij}\,\dot{\lambda}^{j}}\,dt$ in this metric, and a companion "thermodynamic divergence" measures the path's action. In the near-equilibrium (linear-response) regime the mean excess (dissipated) work of a protocol of duration $\tau$ is controlled by these geometric quantities.

## Key results

For a slow protocol the mean dissipation is bounded below in terms of the squared thermodynamic length divided by the available time — a bound of the form $\langle W_{\mathrm{diss}}\rangle \gtrsim L^{2}/\tau$ — so the minimum-dissipation protocols are the *geodesics* of the Fisher metric, traversed at constant thermodynamic speed. This unifies the Ruppeiner/Weinhold geometry of thermodynamics with information geometry: thermodynamic length is Fisher arc length, and Fisher distance acquires the operational meaning of the least dissipation achievable in moving between two equilibrium states.

## Relevance to this research

This is the cleanest statement that "Fisher arc length costs something" — the energetic price of moving through belief/parameter space is set by the [[Fisher information metric]]. It is the thermodynamic counterpart of the project's [[Mass as Fisher information]] identification (inertia of belief change = Fisher information) and supplies a dissipation reading of the [[Belief inertia]] dynamics: reconfiguring beliefs along a non-geodesic path wastes "work," so geodesic motion in the Fisher metric is the least-dissipative belief update. This grounds [[participatory-it-from-bit]]'s claim that the metric structure of belief space carries physical (energetic) content, complementing the equation-level derivations of [[reginatto-1998-fisher-quantum]] and the entropic-dynamics lineage of [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]]. Links [[Physics from Fisher information]] and [[Information geometry and natural gradient]].

## Cross-links

- Concepts: [[Fisher information metric]], [[Statistical manifold]], [[Mass as Fisher information]], [[Belief inertia]], [[Natural gradient]]
- Related sources: [[amari-1998-natural-gradient]], [[reginatto-1998-fisher-quantum]], [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]], [[parr-2020-markov-blankets-thermodynamics]]
- Manuscript: [[participatory-it-from-bit]]

## BibTeX

```bibtex
@article{crooks2007measuring,
  author  = {Crooks, Gavin E.},
  title   = {Measuring Thermodynamic Length},
  journal = {Physical Review Letters},
  volume  = {99},
  number  = {10},
  pages   = {100602},
  year    = {2007},
  publisher = {American Physical Society},
  doi     = {10.1103/PhysRevLett.99.100602}
}
```
