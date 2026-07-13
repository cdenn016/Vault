---
type: paper
title: "Lagrangian Function on the Finite State Space Statistical Bundle"
aliases:
  - "Finite-state statistical-bundle Lagrangian (Pistone 2018)"
authors:
  - Giovanni Pistone
year: 2018
doi: 10.3390/e20020139
url: https://doi.org/10.3390/e20020139
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
  - field/physics
created: 2026-07-12
---

# Lagrangian Function on the Finite State Space Statistical Bundle

> [!info] Citation
> Giovanni Pistone (2018). “Lagrangian Function on the Finite State Space Statistical Bundle.” *Entropy* 20(2), 139. DOI: [10.3390/e20020139](https://doi.org/10.3390/e20020139).

## TL;DR

Pistone develops a Lagrangian formulation on the statistical bundle of positive probability densities and centered random variables over a finite sample space. The paper computes velocities and accelerations, derives Euler–Lagrange equations from an action integral, and discusses a Lagrangian with negative entropy as potential energy. It is an explicit finite-state statistical-bundle predecessor to later inertial belief dynamics.

## Problem & setting

The statistical bundle consists of pairs $(Q,W)$ in which $Q$ is a positive probability density and $W$ is centered under $Q$. The problem is to equip this bundle with enough differential structure to define motion and an action principle for probability trajectories. The finite-state assumption makes the geometry explicit while retaining the central information-geometric features.

## Method

Pistone constructs an affine atlas for the probability manifold, describes the tangent space of the statistical bundle, and calculates the velocity and acceleration of one-dimensional statistical models. A Lagrangian function is integrated along a path to form an action, and variation of that action yields Euler–Lagrange equations. The paper then briefly examines a model in which negative entropy supplies the potential term.

## Key results

The paper supplies explicit kinematic formulas and derives the Euler–Lagrange equation on the finite-state statistical bundle. The entropy-potential example illustrates how familiar information-theoretic functionals can enter a mechanical formulation. Crucially, the construction begins by specifying a Lagrangian; the statistical manifold alone does not force the particular kinetic and potential terms.

## Relevance to this research

Pistone's formulation is a direct predecessor for [[Hamiltonian belief dynamics]] and the probability-space interpretation of [[Belief inertia]]. It prevents a broad claim that the present work is the first to write Lagrangian motion for probabilities. Its deeper value is conceptual discipline: [[Mass as Fisher information]] should be stated as a deliberate kinetic-metric choice layered on the intrinsic [[Fisher information metric]], not as an unavoidable consequence of having a statistical bundle.

## Cross-links

This source links to [[Fisher information metric]], [[Natural gradient]], [[Hamiltonian belief dynamics]], [[Belief inertia]], and [[Mass as Fisher information]]. It is the immediate precursor to [[chirco-2022-statistical-bundle-dynamics]] and a concrete statistical-bundle counterpart to [[leok-zhang-2017-information-geometric-mechanics]].

## BibTeX

```bibtex
@article{Pistone2018StatisticalBundle,
  author  = {Pistone, Giovanni},
  title   = {Lagrangian Function on the Finite State Space Statistical Bundle},
  journal = {Entropy},
  volume  = {20},
  number  = {2},
  pages   = {139},
  year    = {2018},
  doi     = {10.3390/e20020139}
}
```
