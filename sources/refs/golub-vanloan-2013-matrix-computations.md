---
type: reference
title: "Matrix Computations (4th ed.)"
aliases:
  - "Golub & Van Loan 2013 — Matrix Computations"
  - "Golub & Van Loan (2013) Matrix Computations"
authors:
  - Golub G. H.
  - Van Loan C. F.
year: 2013
url: https://jhupbooks.press.jhu.edu/title/matrix-computations
tags:
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
created: 2026-06-20
updated: 2026-06-20
---

# Matrix Computations (4th ed.)

> [!info] Citation
> Gene H. Golub and Charles F. Van Loan (2013). *Matrix Computations*, 4th edition. Johns Hopkins Studies in the Mathematical Sciences. Johns Hopkins University Press, Baltimore. ISBN 978-1-4214-0794-4.

## TL;DR

The standard reference monograph on the algorithms of numerical linear algebra: matrix factorizations (LU, Cholesky, QR), the symmetric eigenvalue problem (the symmetric QR / divide-and-conquer / MRRR algorithms), the singular value decomposition and its computation, the algebra of floating-point error and conditioning, and Krylov-subspace and iterative methods for large systems and eigenproblems. Where Higham's analyses dwell on backward error, Golub & Van Loan is the *recipe book* — it states the algorithms that compute the factorizations, eigenvalues, and singular values on which everything downstream rests, together with their flop counts and stability properties.

## What it establishes

- The canonical factorizations and the stable algorithms that produce them: Gaussian elimination with pivoting, the **Cholesky factorization** $A = R^\top R$ of an SPD matrix, Householder/Givens QR, and the relationships among them.
- The **symmetric eigenvalue problem**: reduction to tridiagonal form followed by the symmetric QR iteration (or divide-and-conquer), giving the orthogonal eigendecomposition $\Sigma = Q\,\Lambda\,Q^\top$ of a symmetric matrix, with the perturbation theory (Weyl, Wielandt–Hoffman) that bounds eigenvalue sensitivity.
- The **singular value decomposition** $A = U\Sigma V^\top$, the Golub–Kahan bidiagonalization that computes it, and its role as the numerically reliable tool for rank, conditioning, and least-squares.
- The arithmetic of **conditioning** — the condition number $\kappa(A) = \sigma_{\max}/\sigma_{\min}$, its amplification of relative error, and how factorization choice controls it.

## Why the project cites it

Every covariance operation in the program reduces to one of these primitives. The Gaussian belief tuples carry SPD covariances $\Sigma$, and the affine-invariant SPD geometry — the matrix $\exp$/$\log$, the geometric mean $\Sigma_i^{1/2}\big(\Sigma_i^{-1/2}\Sigma_j\Sigma_i^{-1/2}\big)^{t}\Sigma_i^{1/2}$, and the retraction back onto the cone — is implemented through the **symmetric eigendecomposition** $\Sigma = Q\Lambda Q^\top$ (apply the scalar function to $\Lambda$) and the **Cholesky factor** (for whitening and for sampling / log-det). Golub & Van Loan is the reference for the algorithms that compute those decompositions and for the conditioning that decides whether they stay accurate: when a transported or averaged covariance approaches the boundary of the SPD cone, $\kappa(\Sigma)$ blows up and eigenvalue floors become necessary, and the bounds justifying those floors are the perturbation results catalogued here. It is the citation the gauge-theory and numerical audit lenses reach for whenever a proof or a kernel says "compute the eigendecomposition / Cholesky / SVD" — the operational layer beneath [[Symmetric spaces and the SPD cone]] and the kernels of [[SPD-manifold geometry and Riemannian optimization]].

> [!note] Editorial: Cited for the standard factorization and symmetric-eigenvalue algorithms and their conditioning, not for any project-specific construction. It is the algorithmic companion to the backward-error analyses in [[higham-2002-accuracy-stability-numerical-algorithms]] and the matrix-function theory in [[higham-2008-functions-of-matrices]]; the SPD eigendecomposition it computes is what makes the [[pennec-2006-intrinsic-statistics]] affine-invariant statistics computable.

## Cross-links

- Concept: [[Symmetric spaces and the SPD cone]]
- Theme: [[SPD-manifold geometry and Riemannian optimization]]
- Projects: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model]]
- Related sources: [[higham-2008-functions-of-matrices]], [[horn-johnson-2013-matrix-analysis]], [[pennec-2006-intrinsic-statistics]]

## BibTeX

```bibtex
@book{golub2013matrix,
  title     = {Matrix Computations},
  author    = {Golub, Gene H. and Van Loan, Charles F.},
  edition   = {4th},
  series    = {Johns Hopkins Studies in the Mathematical Sciences},
  publisher = {Johns Hopkins University Press},
  address   = {Baltimore},
  year      = {2013},
  isbn      = {978-1-4214-0794-4}
}
```
