---
type: reference
title: "Accuracy and Stability of Numerical Algorithms (2nd ed.)"
aliases:
  - "Higham 2002 — Accuracy and Stability of Numerical Algorithms"
  - "Higham (2002) Accuracy and Stability"
authors:
  - Nicholas J. Higham
year: 2002
url: https://epubs.siam.org/doi/10.1137/1.9780898718027
tags:
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
created: 2026-06-20
updated: 2026-06-20
---

# Accuracy and Stability of Numerical Algorithms (2nd ed.)

> [!info] Citation
> Nicholas J. Higham (2002). *Accuracy and Stability of Numerical Algorithms*, 2nd edition. SIAM, Philadelphia. ISBN 978-0-89871-521-7. DOI: [10.1137/1.9780898718027](https://doi.org/10.1137/1.9780898718027).

## TL;DR

The definitive monograph on **finite-precision error analysis**: how rounding errors are generated, how they propagate through numerical algorithms, and what backward and forward stability mean precisely. It develops the standard model of floating-point arithmetic, the unit roundoff $u$, condition numbers as the amplifiers that turn backward error into forward error, and componentwise as well as normwise perturbation theory, then applies that machinery exhaustively to summation, inner products, triangular and linear systems, LU/Cholesky/QR factorizations, least squares, and the matrix exponential. It is the reference that turns "is this computation accurate?" into a sharp, quantitative question.

## What it establishes

- The **standard model** of floating-point arithmetic, $\mathrm{fl}(x \circ y) = (x \circ y)(1 + \delta)$ with $|\delta| \le u$, and the $\gamma_n = nu/(1 - nu)$ bookkeeping for accumulated rounding error in a length-$n$ computation.
- The backward-error / conditioning decomposition of accuracy: the computed result $\hat{y}$ is the exact result of a perturbed input, and the forward error is bounded by (condition number) $\times$ (backward error). Componentwise and normwise condition numbers are derived for the core linear-algebra primitives.
- Backward-stability proofs and error bounds for summation (including compensated/Kahan summation), substitution for triangular systems, LU with partial pivoting and its growth factor, Cholesky for symmetric positive-definite matrices, Householder/Givens QR, and least-squares solvers.
- A chapter on the matrix exponential and the conditioning of matrix functions, tying finite-precision behavior to the function-of-matrices apparatus.

## Why the project cites it

Every covariance and transport operation in the program is a finite-precision computation on the SPD cone, and Higham 2002 is the reference that says when those computations are trustworthy. The affine-invariant SPD update $\Sigma \mapsto \Sigma^{1/2} \exp(\cdot)\,\Sigma^{1/2}$, the eigenvalue clamping and Cholesky factorizations behind covariance whitening, and the gauge transport $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ all inherit the conditioning and backward-stability theory catalogued here: the Cholesky and symmetric-eigenvalue error bounds govern whether a transported or retracted $\Sigma$ stays numerically positive-definite, and the condition number of a near-singular covariance is exactly the quantity that bounds how rounding error in the M-step is amplified. Where the companion [[higham-2008-functions-of-matrices]] supplies the *algorithms* (scaling-and-squaring, inverse scaling-and-squaring) for the matrix $\exp$/$\log$ used in transport and retraction, this volume supplies the *error analysis* that certifies them — the two are cited together for the SPD numerics. The numerical-analyst audit lens reaches for it whenever a conditioning or backward-stability claim about the eigenvalue, Cholesky, or retraction kernels needs a primary citation, and it grounds the float32-throughout discipline of the implementation. It is the error-analysis backbone of [[Symmetric spaces and the SPD cone]] within [[SPD-manifold geometry and Riemannian optimization]], shared by the [[VFE Transformer Program]] and the [[Gauge-Theoretic Multi-Agent VFE Model]].

> [!note] Editorial: Cited as the standard reference for floating-point error propagation, conditioning, and backward stability — not for any project-specific result. The book proves stability for the classical primitives (Cholesky, symmetric eigenproblem, triangular solves); the project's SPD-specific routines reuse those primitives but their composite stability is asserted via finite-difference smoke tests, not a Higham theorem, so the citation supports the building blocks rather than the composite claim.

## Cross-links

- Concept: [[Symmetric spaces and the SPD cone]]
- Theme: [[SPD-manifold geometry and Riemannian optimization]]
- Projects: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model]]
- Related sources: [[higham-2008-functions-of-matrices]], [[horn-johnson-2013-matrix-analysis]], [[bhatia-2007-positive-definite-matrices]], [[absil-2008-optimization-matrix-manifolds]]

## BibTeX

```bibtex
@book{higham2002accuracy,
  title     = {Accuracy and Stability of Numerical Algorithms},
  author    = {Higham, Nicholas J.},
  edition   = {2nd},
  publisher = {SIAM},
  address   = {Philadelphia},
  year      = {2002},
  isbn      = {978-0-89871-521-7},
  doi       = {10.1137/1.9780898718027}
}
```
