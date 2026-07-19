---
type: reference
title: "Convex Optimization"
aliases:
  - "Boyd and Vandenberghe 2004"
  - "Boyd-Vandenberghe Convex Optimization"
authors:
  - Stephen Boyd
  - Lieven Vandenberghe
year: 2004
url: https://web.stanford.edu/~boyd/cvxbook/
tags:
  - cluster/vfe
  - cluster/info-geometry
  - cluster/methodology
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/cs-ml
created: 2026-07-19
updated: 2026-07-19
---

# Convex Optimization

> [!info] Citation
> Stephen Boyd and Lieven Vandenberghe (2004). *Convex Optimization*. Cambridge University Press. ISBN 978-0-521-83378-3.

## TL;DR

Boyd and Vandenberghe provide the convex-analysis and optimization language beneath exponential-family inference: convex sets and functions, conjugacy, Lagrange duality, entropy and log-sum-exp examples, semidefinite constraints, interior-point methods, and disciplined formulation.

## What it establishes

The book develops primal and dual optimization problems, constraint qualifications, optimality conditions, and numerical methods for convex programs. Its examples make entropy, relative entropy, log-partition-like functions, and positive-semidefinite matrix constraints concrete rather than formal symbols.

## Relevance to this research

The duality used by [[wainwright-2008-graphical-models-variational]] is convex duality. This text therefore supports derivations of entropy-regularized attention, variational representations of log partition functions, constrained covariance estimation, and proofs about uniqueness or global optimality. It also provides the baseline against which nonconvex manifold optimization in [[boumal-2023-optimization-smooth-manifolds]] should be understood.

## Access

The [authors' Stanford page](https://web.stanford.edu/~boyd/cvxbook/) provides the complete book PDF with Cambridge University Press's permission. A private local copy is stored at `sources/pdfs/boyd-vandenberghe-2004-convex-optimization.pdf`.

## Cross-links

- Concepts: [[Evidence lower bound (ELBO)]] · [[Attention Mechanism]]
- Themes: [[Inference machinery — variational EM and filtering]] · [[SPD-manifold geometry and Riemannian optimization]]
- Related sources: [[wainwright-2008-graphical-models-variational]] · [[boumal-2023-optimization-smooth-manifolds]]

## BibTeX

```bibtex
@book{BoydVandenberghe2004,
  author    = {Stephen Boyd and Lieven Vandenberghe},
  title     = {Convex Optimization},
  publisher = {Cambridge University Press},
  year      = {2004},
  isbn      = {9780521833783},
  url       = {https://web.stanford.edu/~boyd/cvxbook/}
}
```
