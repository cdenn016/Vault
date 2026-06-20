---
type: reference
title: "Matrix Analysis"
aliases:
  - "Horn & Johnson 2013"
  - "Horn & Johnson (2013) Matrix Analysis"
authors:
  - Roger A. Horn
  - Charles R. Johnson
year: 2013
tags:
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
created: 2026-06-19
updated: 2026-06-19
---

# Matrix Analysis

> [!info] Citation
> Roger A. Horn and Charles R. Johnson (2013). *Matrix Analysis*, 2nd edition. Cambridge University Press, Cambridge. ISBN 978-0-521-54823-6.

## TL;DR

The standard reference monograph on matrix theory: eigenvalues and the spectral theorem, unitary/Schur/Jordan canonical forms, Hermitian and positive-(semi)definite matrices, the Löwner order and **congruence**, Sylvester's law of inertia, variational (Courant–Fischer) characterizations, matrix and vector norms, singular values, and the theory of positive and nonnegative matrices. It is the lookup source for the congruence, determinant, and inertia lemmas that recur in proofs about covariances and gauge actions.

## What it establishes

- The theory of positive-definite matrices: Cholesky and spectral factorizations, the Löwner partial order, and characterizations of positivity.
- **Congruence** $A \mapsto S^* A S$ and Sylvester's law of inertia: congruence preserves the signature (numbers of positive/negative/zero eigenvalues), and $\det(S^*AS) = |\det S|^2 \det A$.
- Variational eigenvalue characterizations (Courant–Fischer, Weyl, interlacing), norm theory, and the singular value decomposition with its perturbation bounds.

## Why the project cites it

The GL($K$)-invariance proofs at the heart of the gauge construction rest on two elementary but load-bearing facts about the **congruence (sandwich) action** $\Sigma \mapsto \Omega\,\Sigma\,\Omega^\top$: it preserves positive-definiteness (inertia is unchanged, Sylvester's law), so a transported covariance is still a valid covariance; and it scales the determinant by $(\det\Omega)^2$, the identity used when checking how volume forms and Gaussian normalizations transform under a [[Gauge transformation]]. Both are Horn & Johnson results. The SO(1,1) / split-signature example in PIFB is precisely a case where the structure group preserves an *indefinite* inertia rather than definiteness — again governed by Sylvester's law. This monograph is therefore the citation backing the linear-algebra steps of the GL($K$)-invariance argument and the covariance-transport well-posedness used throughout [[SPD-manifold geometry and Riemannian optimization]] and [[participatory-it-from-bit]].

> [!note] Editorial: Cited for foundational matrix-analysis lemmas (congruence, inertia, determinant under sandwich), not for any project-specific result.

## BibTeX

```bibtex
@book{horn2013matrix,
  title     = {Matrix Analysis},
  author    = {Horn, Roger A. and Johnson, Charles R.},
  edition   = {2nd},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {2013},
  isbn      = {978-0-521-54823-6}
}
```
