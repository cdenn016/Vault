---
type: paper
title: Optimization Algorithms on Matrix Manifolds
aliases:
  - "Absil, Mahony & Sepulchre 2008 — Optimization on Matrix Manifolds"
authors:
  - P.-A. Absil
  - Robert Mahony
  - Rodolphe Sepulchre
year: 2008
arxiv: null
url: https://press.princeton.edu/books/hardcover/9780691132983/optimization-algorithms-on-matrix-manifolds
tags:
  - cluster/spd-geometry
  - project/transformer
  - field/mathematics
status: stable
created: 2026-06-18
updated: 2026-06-18
---

# Optimization Algorithms on Matrix Manifolds

> [!info] Citation
> P.-A. Absil, Robert Mahony, and Rodolphe Sepulchre. *Optimization Algorithms on Matrix Manifolds*. Princeton University Press, 2008. [Publisher page](https://press.princeton.edu/books/hardcover/9780691132983/optimization-algorithms-on-matrix-manifolds).

## TL;DR

This monograph is the standard reference for *Riemannian optimization*: minimizing a smooth cost function whose variable is constrained to a smooth matrix manifold (the sphere, Stiefel and Grassmann manifolds, the orthogonal group, the manifold of fixed-rank or symmetric-positive-definite matrices, and so on). Its central contribution is a clean, implementable framework in which the two computationally awkward operations of manifold optimization — moving along the manifold from a point in a tangent direction, and moving tangent vectors between different tangent spaces — are replaced by cheap, locally-correct surrogates called **retractions** and **vector transports**. With these two primitives the authors lift the entire toolbox of unconstrained optimization (steepest descent, conjugate gradient, Newton, trust-region) onto curved spaces while preserving the convergence guarantees.

## Problem & setting

Many problems are most naturally posed not over a Euclidean parameter space but over a manifold of structured matrices: eigenvalue and invariant-subspace problems live on the Grassmann manifold, rotation estimation lives on the orthogonal group, and covariance estimation lives on the manifold of symmetric positive-definite (SPD) matrices. Treating such constraints with Lagrange multipliers or generic constrained solvers ignores the geometry and is numerically fragile. The Riemannian viewpoint instead treats the feasible set itself as the search space: a smooth Riemannian manifold equipped with a metric (an inner product on each tangent space). The cost is then unconstrained *on the manifold*, and one seeks critical points where the **Riemannian gradient** — the tangent vector representing the differential of the cost under the metric — vanishes.

The difficulty is that the exact geometric operations are expensive. The **exponential map** that follows a geodesic from a point in a given tangent direction generally requires solving an ODE or computing matrix exponentials, and **parallel transport** along that geodesic, which carries tangent vectors between tangent spaces consistently with the connection, is similarly costly. The book's organizing idea is that exact geodesics and exact transport are *more than the optimizer needs*.

## Method

The two key abstractions:

- **Retraction.** A retraction at a point $x$ is a smooth map $R_x$ from the tangent space back onto the manifold that agrees with the exponential map to first order: $R_x(0)=x$ and $\mathrm{d}R_x(0)=\mathrm{id}$. Any such map suffices to define a step "$x_+ = R_x(t\,\xi)$" along a search direction $\xi$, and first-order agreement is enough to inherit the local and global convergence rates of the Euclidean algorithm. Retractions are typically far cheaper than the true exponential — e.g. a QR- or polar-decomposition projection on the Stiefel manifold, or a closed-form update on the SPD cone.
- **Vector transport.** A vector transport is the analogous first-order surrogate for parallel transport: a way to move a tangent vector from one tangent space to another (needed to combine gradients across iterations in conjugate-gradient and quasi-Newton methods) without integrating the connection exactly.

Around these, the authors develop: line-search and trust-region methods on manifolds with rigorous global convergence and local superlinear/quadratic rates; Riemannian Newton and the geometric conjugate-gradient method; and the systematic treatment of *quotient manifolds* (such as Grassmann as a quotient of Stiefel), where one optimizes over equivalence classes by working with horizontal lifts. The text is explicit and matrix-oriented throughout, giving concrete formulas for tangent spaces, projections, retractions, and gradients on each canonical manifold.

## Key results

- A unified algorithmic framework in which retraction + vector transport reduce manifold optimization to bookkeeping over Euclidean iterations, with convergence theory transferred intact.
- Trust-region methods on manifolds (the Riemannian trust-region, RTR) with global convergence to second-order critical points and local quadratic convergence under standard assumptions.
- Worked geometry for the principal matrix manifolds — sphere, Stiefel, Grassmann, orthogonal/rotation groups, fixed-rank and SPD matrices — including explicit retractions and transports usable directly in code.
- A clear separation between the *intrinsic* problem (minimize on the manifold) and the *representation* (which retraction, which metric), making it straightforward to swap in cheaper approximations without changing the optimizer.

## Relevance to this research

This book supplies the optimization scaffolding that the VFE-transformer's M-step rides on. Two of the program's state variables live on matrix manifolds, and both are updated with exactly the machinery formalized here.

First, each token's belief covariance $\Sigma$ is a symmetric-positive-definite matrix, so updating it is optimization on the SPD manifold. The project's `spd_affine` retraction and its use of the affine-invariant Riemannian metric are special cases of Absil–Mahony–Sepulchre's retraction/metric framework; the affine-invariant geometry itself is developed in [[pennec-2006-affine-invariant-tensor]] and [[arsigny-2006-log-euclidean]], but the *optimization-as-retraction* viewpoint and its convergence guarantees come from this text. Riemannian SGD on such manifolds ([[bonnabel-2013-riemannian-sgd]]) is precisely a stochastic instance of the line-search methods analyzed here.

Second, the gauge-group parameters live in (or are parameterized through the Lie algebra of) the block general-linear group GL(k). The `phi` Lie-algebra parameterization with a BCH retraction is, in this book's language, a retraction on a matrix Lie group: the exponential/BCH map sends a Lie-algebra element back onto the group to first order, and combining successive group updates requires a vector transport between tangent spaces. The Killing-form-based per-block preconditioning is a *choice of Riemannian metric* on the group — exactly the degree of freedom the book isolates as separate from the retraction — and parallel transport / holonomy in the architecture are the geometric operations whose cheap first-order surrogates are formalized here.

> [!note] Editorial: The architecture's design — a retraction plus a transport plus a metric, chosen independently per manifold (SPD cone vs. GL(k) group) — mirrors the book's deliberate decoupling of these three ingredients. Reading the SPD covariance update and the gauge-parameter update as two instantiations of one Riemannian-optimization template is the cleanest way to see why the same code patterns recur in both.

Because natural-gradient methods are themselves Riemannian descent under the Fisher metric, this text is also the bridge between the information-geometry side of the program ([[amari-1998-natural-gradient]], [[ollivier-2015-riemannian-metrics-nn]]) and its concrete manifold implementations.

## Cross-links

- [[SPD-manifold geometry and Riemannian optimization]] — the theme this text anchors.
- [[pennec-2006-affine-invariant-tensor]], [[arsigny-2006-log-euclidean]], [[bhatia-2007-positive-definite-matrices]] — the specific SPD-manifold geometry the retractions act on.
- [[bonnabel-2013-riemannian-sgd]] — stochastic Riemannian descent, a direct application of the line-search framework.
- [[huang-2017-spdnet]], [[wang-2023-riemannian-self-attention-spd]] — neural architectures operating on the SPD manifold.
- [[Natural gradient]], [[Fisher information metric]], [[amari-1998-natural-gradient]], [[ollivier-2015-riemannian-metrics-nn]] — natural gradient as Riemannian descent.
- [[VFE Transformer Program]] — the program whose M-step reuses these retractions and transports.

```bibtex
@book{absil2008optimization,
  title     = {Optimization Algorithms on Matrix Manifolds},
  author    = {Absil, P.-A. and Mahony, Robert and Sepulchre, Rodolphe},
  publisher = {Princeton University Press},
  address   = {Princeton, NJ},
  year      = {2008},
  isbn      = {9780691132983},
  url       = {https://press.princeton.edu/books/hardcover/9780691132983/optimization-algorithms-on-matrix-manifolds}
}
```
