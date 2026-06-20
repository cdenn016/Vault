---
type: reference
title: "Riemannian Metric and Geometric Mean for Positive Semidefinite Matrices of Fixed Rank"
aliases:
  - "Bonnabel & Sepulchre 2009"
  - "Bonnabel & Sepulchre (2009) PSD Fixed Rank"
authors:
  - Silvère Bonnabel
  - Rodolphe Sepulchre
year: 2009
tags:
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
created: 2026-06-19
updated: 2026-06-19
---

# Riemannian Metric and Geometric Mean for Positive Semidefinite Matrices of Fixed Rank

> [!info] Citation
> Silvère Bonnabel and Rodolphe Sepulchre (2009). "Riemannian Metric and Geometric Mean for Positive Semidefinite Matrices of Fixed Rank." *SIAM Journal on Matrix Analysis and Applications* 31(3), 1055–1070. DOI: [10.1137/080731347](https://doi.org/10.1137/080731347). Preprint: [arXiv:0807.4462](https://arxiv.org/abs/0807.4462).

## TL;DR

Extends the affine-invariant SPD geometry to **positive semidefinite matrices of fixed rank** $r < n$, which form a non-Euclidean manifold but not the full-rank cone. The authors build a Riemannian quotient geometry — factoring a rank-$r$ PSD matrix as $W = U R U^\top$ with $U$ on a Grassmannian (the range) and $R$ a full-rank SPD matrix (the "scale") — and define a distance and a geometric mean that respect this range/scale split. It is the principled treatment of *degenerate*, low-rank covariances.

## What it establishes

- A quotient-manifold structure on fixed-rank PSD matrices separating the column space (a point on a Grassmann manifold) from the residual full-rank SPD factor.
- A Riemannian metric combining a subspace (Grassmann) distance with an affine-invariant SPD distance on the scale factor, invariant under the relevant group action.
- A corresponding geometric mean / interpolation for low-rank PSD matrices, computable via Grassmann and SPD primitives.

## Why the project cites it

The full-rank affine-invariant geometry of [[pennec-2006-affine-invariant-tensor]] and [[bhatia-2007-positive-definite-matrices]] breaks down exactly where covariances become singular — and in the VFE transformer the per-token belief covariance $\Sigma$ can be driven toward low rank when beliefs collapse (high precision in some directions, near-zero variance in others), or when diagonal/low-rank approximations are used for speed. This paper supplies the geometry for that **degenerate regime**: it tells the program how to measure distance, transport, and average covariances when $\Sigma$ is rank-deficient, so that pooling and natural-gradient updates do not blow up as eigenvalues approach zero. It sits beside [[bonnabel-2013-riemannian-sgd]] (Riemannian stochastic optimization) and [[pennec-2006-affine-invariant-tensor]] (full-rank affine-invariant metric) as the fixed-rank complement, relevant to the SPD-pooling and covariance-collapse discussion in [[SPD-manifold geometry and Riemannian optimization]] and the meta-agent formation in [[Meta-agents and hierarchical emergence]].

> [!note] Editorial: Relevant chiefly as the geometry of the low-rank limit; the program's default full-rank affine-invariant path is the generic case, with this as the principled boundary treatment.

## BibTeX

```bibtex
@article{bonnabel2009riemannian,
  title   = {Riemannian Metric and Geometric Mean for Positive Semidefinite Matrices of Fixed Rank},
  author  = {Bonnabel, Silv{\`e}re and Sepulchre, Rodolphe},
  journal = {SIAM Journal on Matrix Analysis and Applications},
  volume  = {31},
  number  = {3},
  pages   = {1055--1070},
  year    = {2009},
  doi     = {10.1137/080731347},
  eprint  = {0807.4462},
  archivePrefix = {arXiv}
}
```
