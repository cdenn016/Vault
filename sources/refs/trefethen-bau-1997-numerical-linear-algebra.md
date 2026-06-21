---
type: reference
title: "Numerical Linear Algebra"
aliases:
  - "Trefethen & Bau 1997 — Numerical Linear Algebra"
  - "Trefethen & Bau 1997"
authors:
  - Trefethen L. N.
  - Bau D. III
year: 1997
url: https://doi.org/10.1137/1.9780898719574
tags:
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
created: 2026-06-20
updated: 2026-06-20
---

# Numerical Linear Algebra

> [!info] Citation
> Lloyd N. Trefethen and David Bau III (1997). *Numerical Linear Algebra*. SIAM, Philadelphia. ISBN 978-0-89871-361-9. DOI: [10.1137/1.9780898719574](https://doi.org/10.1137/1.9780898719574).

## TL;DR

A graduate text on numerical linear algebra organized as forty self-contained lectures, prized for putting the **geometry of the SVD, conditioning, and backward stability** at the conceptual center rather than treating them as afterthoughts. It develops the QR factorization (Householder, Gram-Schmidt), least squares, the conditioning of problems versus the stability of algorithms, eigenvalue and singular-value algorithms (QR iteration, Rayleigh-quotient iteration), and Krylov-subspace iterative methods (Arnoldi, GMRES, Lanczos, conjugate gradients). Its signature contribution is the clean separation of two distinct quantities — the **condition number** $\kappa(A)$ of a problem and the **backward error** of an algorithm — tied together by the rule of thumb that the forward error is bounded by their product.

## What it establishes

- The singular value decomposition $A = U\Sigma V^{\!\top}$ as the organizing object of the subject: it diagonalizes any matrix by orthonormal frames, exposes the 2-norm condition number $\kappa_2(A) = \sigma_{\max}/\sigma_{\min}$, and gives the geometry of how a matrix stretches the unit sphere into a hyperellipse.
- A precise definition of **conditioning** — the relative sensitivity of a problem's output to perturbations of its input — and of **backward stability** — an algorithm is backward stable if its computed answer is the exact answer to a slightly perturbed problem. The central inequality, relative forward error $\lesssim \kappa(\text{problem}) \cdot \varepsilon_{\text{machine}}$, governs how many digits survive a finite-precision computation.
- Stable factorizations and their error analysis: Householder QR (unconditionally backward stable), the loss of orthogonality in classical Gram-Schmidt, Cholesky for symmetric positive-definite systems, and the conditioning of least-squares problems through the normal equations versus QR.
- Eigenvalue and singular-value machinery: the QR algorithm with shifts, Hessenberg/tridiagonal reduction, Rayleigh-quotient iteration, and the symmetric eigenproblem whose orthogonal eigendecomposition underlies every operation on the SPD cone.

## Why the project cites it

The model's belief tuples carry SPD covariances $\Sigma$, and every operation on them — the matrix $\exp$/$\log$, the geometric mean, the affine-invariant retraction $\Sigma \mapsto \Sigma^{1/2}\exp(\cdot)\Sigma^{1/2}$ — is computed through a symmetric eigendecomposition or Cholesky factor whose accuracy is exactly what Trefethen and Bau analyze. Their condition-number/backward-stability framework is the lens the numerical-analyst audit lens applies when asking whether the SPD eigenvalue and retraction kernels stay accurate in float32: an ill-conditioned $\Sigma$ (a covariance with a small minimum eigenvalue) loses digits in proportion to $\kappa_2(\Sigma)$, which is why the code floors eigenvalues and clamps the SPD cone away from its boundary. The SVD geometry the book centers is also the right picture for the gauge frames: an orthonormal $U$ and $V$ are the singular frames a congruence/transport acts through, and the $\sigma_i$ are the precisions the covariance encodes. This text supplies the conditioning vocabulary for [[Symmetric spaces and the SPD cone]] and the stability guarantees the Riemannian updates in [[SPD-manifold geometry and Riemannian optimization]] rely on; it sits alongside [[higham-2008-functions-of-matrices]] (matrix-function algorithms and their Fréchet derivatives) and [[horn-johnson-2013-matrix-analysis]] (the algebraic theory of the same matrices) as the floating-point-stability member of that trio.

> [!note] Editorial: Trefethen and Bau treat conditioning at the level of general matrices and the SVD; the program's specific concern is the *intrinsic* (affine-invariant) conditioning of operations restricted to the SPD manifold, where the relevant sensitivity is governed by the eigenvalue spread of $\Sigma$ rather than the 2-norm condition of an arbitrary linear map. The book gives the Euclidean-ambient backward-stability tools; the manifold-restricted statements are the project's own application of them.

## Cross-links

- Concept: [[Symmetric spaces and the SPD cone]]
- Theme: [[SPD-manifold geometry and Riemannian optimization]]
- Projects: [[VFE Transformer Program]] · [[Gauge-Theoretic Multi-Agent VFE Model]]
- Related sources: [[higham-2008-functions-of-matrices]] · [[horn-johnson-2013-matrix-analysis]] · [[pennec-2006-intrinsic-statistics]] · [[bonnabel-2009-spd-fixed-rank|bonnabel-sepulchre-2009-psd-fixed-rank]]

## BibTeX

```bibtex
@book{trefethen1997numerical,
  title     = {Numerical Linear Algebra},
  author    = {Trefethen, Lloyd N. and Bau, III, David},
  publisher = {SIAM},
  address   = {Philadelphia},
  year      = {1997},
  isbn      = {978-0-89871-361-9},
  doi       = {10.1137/1.9780898719574}
}
```
