---
type: reference
title: "DEM: a variational treatment of dynamic systems"
aliases:
  - "Friston 2008 DEM"
  - "Friston (2008) DEM"
authors:
  - Karl J. Friston
  - Nelson Trujillo-Barreto
  - Jean Daunizeau
year: 2008
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/multi-agent
  - project/transformer
  - field/neuroscience
  - field/statistics
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# DEM: a variational treatment of dynamic systems

> [!info] Citation
> Friston, K. J., Trujillo-Barreto, N., & Daunizeau, J. (2008). "DEM: a variational treatment of dynamic systems." *NeuroImage* **41**(3): 849–885. DOI: [10.1016/j.neuroimage.2008.02.054](https://doi.org/10.1016/j.neuroimage.2008.02.054).

> [!note] Editorial: The domain brief flagged two candidates for the "Friston2008DEM" citation — a "Hierarchical models in the brain" paper and this DEM (Dynamic Expectation Maximization) paper — with instructions to verify which. The DEM title resolves to this *NeuroImage* 41(3):849–885 article; the brief's own pointer ("DEM: a variational treatment of dynamic systems," NeuroImage 41:849, 2008) matches it. This note records the DEM paper. Confirm the manuscript cites this rather than the separate "Hierarchical models in the brain" (Friston, *PLoS Comput. Biol.* 2008).

## TL;DR

DEM (Dynamic Expectation Maximization) is the variational scheme for inverting *dynamic* generative models: it furnishes time-dependent conditional densities on the **path/trajectory** of a system's hidden states together with time-independent densities on its parameters, by maximizing a **variational action** (a path-integral of free energy) under a fixed-form (Laplace) assumption. The key device is working in **generalized coordinates of motion** — representing not just states but their temporal derivatives — so that inference tracks trajectories rather than static points. It is the dynamic-systems variational treatment the project cites for trajectory-level belief inference.

## What it establishes

- **Variational action as the objective.** For dynamic models the relevant quantity is the path-integral of [[Variational free energy]] (the action), a lower bound on the model's log-evidence; optimizing it yields conditional densities over state trajectories.
- **Generalized coordinates of motion.** Representing states together with their successive time derivatives lets the scheme handle correlated (analytic) noise and continuous dynamics, the foundation later reused in generalized filtering.
- **Joint state/parameter/hyperparameter inference.** A single variational scheme estimates trajectories (D-step), parameters (E-step), and precisions (M-step), generalizing static variational EM to dynamics.

## Why the project cites it

DEM is the dynamic-systems variational machinery underlying the project's treatment of beliefs as evolving in continuous time rather than as static posteriors. In [[participatory-it-from-bit]] and the [[Gauge-Theoretic Multi-Agent VFE Model]], beliefs `(μ, Σ, φ)` follow trajectories governed by [[Hamiltonian belief dynamics]] with [[Belief inertia]]; DEM supplies the canonical variational-action / generalized-coordinates formulation that licenses inference over such trajectories. The action-as-path-integral-of-free-energy view is also the precedent for the project's path-level reading of belief dynamics, and the fast/slow (state vs parameter) split is the [[Variational EM]] structure the model inherits ([[Free-energy principle active inference]]). The trajectory-tracking (path) formulation connects to the path-tracking branch of [[Bayesian mechanics]] ([[dacosta-2021-bayesian-mechanics]], [[ramstead-2023-bayesian-mechanics]]). Geometrically, the variational descent is a [[Natural gradient]] flow under the [[Fisher information metric]].

```bibtex
@article{friston2008dem,
  title   = {DEM: a variational treatment of dynamic systems},
  author  = {Friston, Karl J. and Trujillo-Barreto, Nelson and Daunizeau, Jean},
  journal = {NeuroImage},
  volume  = {41},
  number  = {3},
  pages   = {849--885},
  year    = {2008},
  doi     = {10.1016/j.neuroimage.2008.02.054},
  publisher = {Elsevier}
}
```
