---
type: paper
title: "Conic Geometric Optimization on the Manifold of Positive Definite Matrices"
aliases:
  - "Sra & Hosseini 2015"
  - "Sra & Hosseini (2015) Conic Geometric Optimization"
authors:
  - Suvrit Sra
  - Reshad Hosseini
year: 2015
arxiv: "1312.1039"
url: https://epubs.siam.org/doi/10.1137/140978168
tags:
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Conic Geometric Optimization on the Manifold of Positive Definite Matrices

> [!info] Citation
> Suvrit Sra and Reshad Hosseini (2015). "Conic Geometric Optimization on the Manifold of Positive Definite Matrices." *SIAM Journal on Optimization* 25(1), 713–739. DOI: [10.1137/140978168](https://epubs.siam.org/doi/10.1137/140978168). Preprint: [arXiv:1312.1039](https://arxiv.org/abs/1312.1039).

## TL;DR

Develops the theory of **geodesic convexity** (g-convexity) on the SPD cone under the affine-invariant metric and uses it to design and analyze optimization algorithms for problems involving positive-definite matrices. A function nonconvex in the Euclidean sense can be convex along the cone's geodesics, in which case stationary points are global minima and Riemannian descent converges to the optimum. The paper catalogs g-convex objectives (log-determinant terms, $\operatorname{tr}(AX)$, geometric-mean and metric-nearness problems) and supplies a "manifold of PD matrices" optimization toolkit.

## Problem & setting

Many estimation problems — maximum-likelihood for elliptical/Gaussian models, metric and geometric-mean computations, log-det divergence minimization — are nonconvex over the open cone of SPD matrices when viewed in the ambient vector space, so Euclidean convex analysis gives no guarantees. Sra and Hosseini ask which of these become convex once the cone is given its intrinsic affine-invariant (and related conic) geometry, and how to exploit that for provably good algorithms.

## Method

The cone is treated as a Riemannian manifold with the affine-invariant metric (geodesics $A\#_t B = A^{1/2}(A^{-1/2}BA^{-1/2})^t A^{1/2}$). The authors establish a calculus of geodesically convex functions: closure under composition rules, g-convexity of building blocks like $\log\det X$, $\operatorname{tr}(AX^{-1})$, and Riemannian distance terms, and the consequence that g-convex problems have unique minimizers reached by Riemannian first-order methods. They also connect to Thompson-metric / conic contraction arguments for fixed-point iterations.

## Key results

- A systematic theory of geodesic convexity on the PD cone, with a library of g-convex objectives and operation-preserving rules.
- Global-optimality guarantees: g-convex stationary points are global minima, so Riemannian gradient descent on the affine-invariant manifold converges optimally.
- Application to ML estimation for scatter/covariance matrices and to geometric-mean–type subproblems, outperforming naive Euclidean handling.

## Relevance to this research

Wherever PIFB or the VFE transformer poses a subproblem in the covariance $\Sigma$ — the M-step / E-step SPD retraction, computing or approximating a Karcher barycenter for meta-agent pooling, or any regularizer expressed through $\log\det\Sigma$ and affine-invariant distances — this paper says when that subproblem is *geodesically convex* and therefore globally solvable by the affine-invariant [[Natural gradient]] / Riemannian descent the model already uses. It is the optimization-theoretic license for treating SPD updates as well-behaved convex problems on a curved manifold, complementing the existence/uniqueness statements of [[moakher-2005-geometric-mean]] and the algorithmic cost survey of [[jeuris-2012-matrix-geometric-mean]]. Supports [[SPD-manifold geometry and Riemannian optimization]].

## Cross-links

- Geodesic convexity and natural-gradient descent on SPD: [[Natural gradient]] · [[SPD-manifold geometry and Riemannian optimization]]
- SPD geometry foundations: [[bhatia-2007-positive-definite-matrices]], [[pennec-2006-affine-invariant-tensor]]
- Means and their cost: [[moakher-2005-geometric-mean]], [[jeuris-2012-matrix-geometric-mean]]
- Manifold optimization: [[absil-2008-optimization-matrix-manifolds]], [[bonnabel-2013-riemannian-sgd]]
- Manuscript: [[participatory-it-from-bit]]

```bibtex
@article{sra2015conic,
  title   = {Conic Geometric Optimization on the Manifold of Positive Definite Matrices},
  author  = {Sra, Suvrit and Hosseini, Reshad},
  journal = {SIAM Journal on Optimization},
  volume  = {25},
  number  = {1},
  pages   = {713--739},
  year    = {2015},
  publisher = {SIAM},
  doi     = {10.1137/140978168},
  eprint  = {1312.1039},
  archivePrefix = {arXiv}
}
```
