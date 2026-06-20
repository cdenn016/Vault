---
type: reference
title: "Functions of Matrices: Theory and Computation"
aliases:
  - "Higham 2008"
  - "Higham (2008) Functions of Matrices"
authors:
  - Nicholas J. Higham
year: 2008
tags:
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
created: 2026-06-19
updated: 2026-06-19
---

# Functions of Matrices: Theory and Computation

> [!info] Citation
> Nicholas J. Higham (2008). *Functions of Matrices: Theory and Computation*. SIAM, Philadelphia. ISBN 978-0-898716-46-7. DOI: [10.1137/1.9780898717778](https://doi.org/10.1137/1.9780898717778).

## TL;DR

The definitive monograph on matrix functions $f(A)$ — their theory (Jordan/Cauchy-integral/polynomial-interpolation definitions, conditioning), their **Fréchet derivatives**, and above all the numerically stable algorithms for computing the matrix exponential, logarithm, square root, and $p$-th roots together with their derivatives. It is the practitioner's reference for getting $\exp$, $\log$, and $\sqrt{\cdot}$ right on real matrices, including scaling-and-squaring with Padé approximants and inverse-scaling-and-squaring for the log.

## What it establishes

- Rigorous equivalent definitions of $f(A)$ and a thorough treatment of conditioning via the Fréchet derivative $L_f(A, E)$, including how to compute the derivative alongside the function and how to estimate the condition number.
- State-of-the-art algorithms: scaling-and-squaring with Padé for $\exp$; inverse scaling-and-squaring with Padé for $\log$; Schur–Newton and Denman–Beavers iterations for the square root; backward-error analysis and overscaling fixes.
- Stability and accuracy analysis for these primitives, the building blocks of any computation on matrix Lie groups and the SPD cone.

## Why the project cites it

Every transport, retraction, and covariance operation in the program is built from matrix $\exp$, $\log$, and $\sqrt{\cdot}$: the gauge transport $\Omega_{ij}=\exp(\phi_i)\exp(-\phi_j)$, the BCH frame retraction, and the affine-invariant SPD update $\Sigma \mapsto \Sigma^{1/2}\exp(\cdot)\Sigma^{1/2}$ all call these matrix functions, and their **gradients** require the Fréchet derivatives Higham analyzes (the `cached_block_exp_pairs` / block-exp gradient machinery in the attention code is exactly a Fréchet-derivative-of-exp computation). This book is the numerical backbone of that apparatus: it specifies the stable algorithms and the conditioning that determine whether transport and SPD retraction stay accurate at scale, and the derivative formulas needed for correct backprop through $\exp$/$\log$. It directly supports [[Parallel transport]] and the covariance-sandwich SPD updates in [[SPD-manifold geometry and Riemannian optimization]]; the exp/log it computes are the operational core of the geometry in [[participatory-it-from-bit]].

> [!note] Editorial: When finite-difference smoke tests check gradient correctness of the transport/SPD code, the analytic reference being checked against is Higham's Fréchet-derivative theory for $\exp$ and $\log$.

## BibTeX

```bibtex
@book{higham2008functions,
  title     = {Functions of Matrices: Theory and Computation},
  author    = {Higham, Nicholas J.},
  publisher = {SIAM},
  address   = {Philadelphia},
  year      = {2008},
  isbn      = {978-0-898716-46-7},
  doi       = {10.1137/1.9780898717778}
}
```
