---
type: paper
title: "Lagrangian and Hamiltonian Dynamics for Probabilities on the Statistical Bundle"
aliases:
  - "Statistical-bundle dynamics (Chirco et al. 2022)"
authors:
  - Goffredo Chirco
  - Luigi Malagò
  - Giovanni Pistone
year: 2022
arxiv: 2009.09431
doi: 10.1142/S0219887822502140
url: https://doi.org/10.1142/S0219887822502140
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
  - field/physics
created: 2026-07-12
---

# Lagrangian and Hamiltonian Dynamics for Probabilities on the Statistical Bundle

> [!info] Citation
> Goffredo Chirco, Luigi Malagò, and Giovanni Pistone (2022). “Lagrangian and Hamiltonian dynamics for probabilities on the statistical bundle.” *International Journal of Geometric Methods in Modern Physics* 19(13), 2250214. DOI: [10.1142/S0219887822502140](https://doi.org/10.1142/S0219887822502140). arXiv: [2009.09431](https://arxiv.org/abs/2009.09431).

## TL;DR

Chirco, Malagò, and Pistone formulate Lagrangian and Hamiltonian mechanics for positive probability distributions on a finite sample space by working on a statistical bundle with explicit tangent and cotangent structures. The framework yields accelerated [[Natural gradient]] dynamics on the probability simplex and is a direct probability-bundle mechanics predecessor, so a later belief-dynamics manuscript should present its kinetic energy as an explicit postulate rather than as something automatically forced by information geometry.

## Problem & setting

Ordinary information geometry supplies a manifold of probability distributions and dual affine connections, but second-order mechanics additionally needs well-defined velocities, momenta, accelerations, and an action principle. The paper studies the full set of positive probability functions on a finite sample space and builds the bundle machinery needed to express these objects without reducing the discussion to a single parametric family.

## Method

The authors describe tangent and cotangent fibers through a Hilbert-bundle structure over the statistical manifold. Using the canonical pair of dual parallel transports, they calculate velocities and accelerations of one-dimensional statistical models and construct Lagrangian and Hamiltonian descriptions connected by the relevant duality transformations. The resulting equations provide a geometric account of accelerated natural-gradient motion on the simplex.

## Key results

The paper gives coherent bundle-level definitions of kinematics and mechanics for probabilities and shows, through worked examples, that the formalism produces accelerated natural-gradient dynamics. Its contribution is structural: it demonstrates that Lagrangian and Hamiltonian probability dynamics can be built consistently on an information-geometric statistical bundle. It does not imply that every divergence or Fisher metric uniquely determines a physical kinetic energy.

## Relevance to this research

This work is a central predecessor for [[Hamiltonian belief dynamics]] and [[Mass as Fisher information]]. It narrows the defensible novelty claim: mechanics on probability bundles and accelerated natural-gradient equations already exist. The present program's contribution must therefore lie in its specific gauge-transported multi-agent VFE, interaction architecture, and stiffness construction. It also supports the required explicit-postulate framing: the intrinsic [[Fisher information metric]] can motivate a kinetic metric, but choosing the kinetic energy remains an additional modeling decision.

## Cross-links

The source connects directly to [[Natural gradient]], [[Fisher information metric]], [[Hamiltonian belief dynamics]], [[Belief inertia]], and [[Mass as Fisher information]]. It should be read alongside [[pistone-2018-statistical-bundle-lagrangian]] and [[leok-zhang-2017-information-geometric-mechanics]] for the distinction between information-geometric structure and a separately specified mechanical model.

## BibTeX

```bibtex
@article{ChircoMalagoPistone2022,
  author        = {Chirco, Goffredo and Malag{\`o}, Luigi and Pistone, Giovanni},
  title         = {Lagrangian and Hamiltonian Dynamics for Probabilities on the Statistical Bundle},
  journal       = {International Journal of Geometric Methods in Modern Physics},
  volume        = {19},
  number        = {13},
  pages         = {2250214},
  year          = {2022},
  doi           = {10.1142/S0219887822502140},
  eprint        = {2009.09431},
  archivePrefix = {arXiv}
}
```
