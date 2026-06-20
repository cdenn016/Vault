---
type: reference
title: An Introduction to Optimization on Smooth Manifolds
aliases:
  - "Boumal 2023"
  - "Introduction to Optimization on Smooth Manifolds"
authors:
  - Nicolas Boumal
year: 2023
arxiv: null
url: https://doi.org/10.1017/9781009166164
tags:
  - cluster/spd-geometry
  - cluster/methodology
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# An Introduction to Optimization on Smooth Manifolds

> [!info] Citation
> Boumal, N. (2023). An Introduction to Optimization on Smooth Manifolds. Cambridge University Press. DOI 10.1017/9781009166164. ISBN 9781009166157.

## TL;DR

This is the modern, computation-forward textbook for optimization on Riemannian manifolds: the problem of minimizing a smooth objective $f: \mathcal{M} \to \mathbb{R}$ when the search space $\mathcal{M}$ is a curved manifold rather than a Euclidean vector space. Boumal develops the subject through a deliberately "charts-last" embedded-geometry route, so that the reader first meets tangent spaces, Riemannian gradients, retractions, connections, and Riemannian Hessians as concrete operations on matrices living in an ambient $\mathbb{R}^{n\times p}$, and only later abstracts to intrinsic manifolds and quotients. From these primitives it builds and analyzes the full algorithmic stack — Riemannian gradient descent, Newton's method, and trust-region methods — with explicit worst-case complexity and local/global convergence rates, and it grounds every construction in the manifolds that matter in practice (the sphere, the Stiefel manifold, the Grassmannian, and the symmetric positive-definite cone). It is the natural successor to Absil, Mahony, and Sepulchre's 2008 monograph, updated with the topics that matured afterward (geodesic convexity, complexity bounds, quotient-manifold Hessians) and tied directly to the [Manopt / Pymanopt / Manopt.jl](https://www.manopt.org) software whose implementation choices it justifies.

## Problem & setting

The object of study is the optimization problem $\min_{x \in \mathcal{M}} f(x)$ where $\mathcal{M}$ is a smooth manifold equipped with a Riemannian metric $\langle\cdot,\cdot\rangle_x$ on each tangent space $T_x\mathcal{M}$. Ordinary unconstrained optimization is the special case $\mathcal{M} = \mathbb{R}^n$; the interesting cases arise when the feasible set carries intrinsic curvature — orthonormality constraints (Stiefel, Grassmann), unit-norm constraints (sphere), or positive-definiteness (SPD). The classical move of imposing such constraints with Lagrange multipliers in an extrinsic chart is replaced by working directly in the geometry: the gradient becomes the Riemannian gradient $\operatorname{grad} f(x)$, the orthogonal projection of the ambient gradient onto $T_x\mathcal{M}$, and a step is taken not by adding a vector but by a **retraction** $R_x: T_x\mathcal{M} \to \mathcal{M}$ that maps a tangent move back onto the manifold. The book builds explicitly on Absil, Mahony, and Sepulchre (2008), *Optimization Algorithms on Matrix Manifolds* — the foundational text for this retraction-and-vector-transport viewpoint — and modernizes it with the convergence-rate and complexity machinery, the geodesic-convexity theory, and the quotient-manifold treatment that became standard in the subsequent fifteen years.

## Method

The central pedagogical and computational device is the **retraction**, a first-order-accurate surrogate for the exponential map: any smooth $R$ with $R_x(0)=x$ and $\mathrm{D}R_x(0)=\mathrm{id}$ on $T_x\mathcal{M}$ qualifies, and the iteration
$$ x_{k+1} = R_{x_k}\!\big(-\eta_k\,\operatorname{grad} f(x_k)\big) $$
is Riemannian gradient descent. For second-order methods, the **Riemannian Hessian** $\operatorname{Hess} f(x) = \nabla \operatorname{grad} f(x)$ is defined through a connection $\nabla$ (the Levi-Civita connection for the Riemannian Newton and trust-region methods of Chapter 6), and the analysis distinguishes a generic retraction from a **second-order retraction**, one that additionally matches the geodesic to second order, $\frac{\mathrm{d}^2}{\mathrm{d}t^2}R_x(t v)\big|_{t=0} \in (T_x\mathcal{M})^\perp$. This distinction is precisely what controls whether a cheap retraction degrades the convergence rate of a Hessian-based method or leaves it intact, and Boumal makes the error of a retraction relative to the true exponential map explicit. To move tangent vectors between tangent spaces (needed for conjugate gradients, momentum, and quasi-Newton updates) the book uses **vector transport** and, in Chapter 10, parallel transport. The worked manifolds are concrete: the SPD cone $\mathcal{S}_{++}^n$ with its affine-invariant metric (Chapters 2.7 and 11.7) and the Stiefel manifold $\mathrm{St}(n,p)$ (Chapters 2.4 and 7.3) receive explicit formulas for projection, retraction, gradient, and Hessian, mirroring the Manopt factory implementations.

## Key results

The book is a textbook rather than a single-result paper, so its "results" are the worked theory it organizes and proves rather than benchmark numbers. It establishes the standard convergence guarantees of the field at a rigorous level: global convergence of Riemannian gradient descent to first-order critical points with the expected $O(1/\varepsilon^2)$ iteration complexity for reaching an $\varepsilon$-approximate stationary point under Lipschitz-type smoothness assumptions on the pullback $f \circ R_x$; local superlinear (quadratic) convergence of Riemannian Newton near nondegenerate minimizers; and global convergence with complexity bounds for the Riemannian trust-region method. It develops geodesic convexity (Chapter 11) as the manifold analogue of convexity that yields global optimality, with the SPD cone under the affine-invariant metric as the canonical geodesically convex example. The treatment of second-order retractions makes precise the condition under which a non-exponential retraction preserves the order of a second-order method — the practically load-bearing fact for anyone substituting a cheap matrix retraction for a true geodesic. I have verified the chapter-level structure and topic coverage against the publisher and author pages; specific theorem numbers and constants should be checked against the book itself before being cited as exact.

## Relevance to this research

Boumal is the practical reference for asking whether the VFE transformer's manifold steps stay well-conditioned in fp32. Two operations are squarely in its scope. First, the SPD covariance update — the affine retraction $\Sigma_{\text{new}} = \Sigma^{1/2}\exp\!\big(\eta\,\Sigma^{-1/2} X \Sigma^{-1/2}\big)\Sigma^{1/2}$ and its diagonal/clamped variants used by `spd_affine` — is exactly the affine-invariant SPD geometry of Chapters 2.7, 7, and 11.7; the book's explicit retraction formulas and second-order-retraction error analysis give the standard against which to judge whether the clamp $\exp(\eta\,\mathrm{clamp}(\delta\sigma/\sigma,\cdot))$ both preserves positive-definiteness and keeps the step second-order accurate ([[SPD-manifold geometry and Riemannian optimization]], [[Symmetric spaces and the SPD cone]]). Second, the GL(K) gauge-group steps composed through Baker–Campbell–Hausdorff truncation are Lie-group retractions whose conditioning and order of accuracy are governed by the same retraction-error and vector-transport theory; Boumal's framing tells us when a truncated BCH retraction silently downgrades a second-order update. The Riemannian-gradient and Hessian machinery here is also the geometric setting in which the [[Natural gradient]] M-step lives, so this text connects the affine-invariant SPD picture, the gauge-group transport, and the Fisher-preconditioned descent into one numerically explicit framework.

## Cross-links

- Concepts / Themes: [[SPD-manifold geometry and Riemannian optimization]], [[Symmetric spaces and the SPD cone]], [[Natural gradient]]
- Related sources: [[amari-1998-natural-gradient]]

## BibTeX

```bibtex
@book{boumal2023optimiza,
  author    = {Boumal, Nicolas},
  title     = {An Introduction to Optimization on Smooth Manifolds},
  publisher = {Cambridge University Press},
  year      = {2023},
  isbn      = {9781009166157},
  doi       = {10.1017/9781009166164},
  url       = {https://doi.org/10.1017/9781009166164}
}
```
