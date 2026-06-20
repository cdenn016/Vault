---
type: paper
title: "A Differential Geometric Approach to the Geometric Mean of Symmetric Positive-Definite Matrices"
aliases:
  - "Moakher 2005"
  - "Moakher (2005) SPD Geometric Mean"
authors:
  - Maher Moakher
year: 2005
arxiv: null
url: https://epubs.siam.org/doi/10.1137/S0895479803436937
tags:
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# A Differential Geometric Approach to the Geometric Mean of Symmetric Positive-Definite Matrices

> [!info] Citation
> Maher Moakher (2005). "A Differential Geometric Approach to the Geometric Mean of Symmetric Positive-Definite Matrices." *SIAM Journal on Matrix Analysis and Applications* 26(3), 735–747. DOI: [10.1137/S0895479803436937](https://epubs.siam.org/doi/10.1137/S0895479803436937).

## TL;DR

Moakher formalizes the *intrinsic* (Riemannian) mean of symmetric positive-definite (SPD) matrices and shows that the naive arithmetic mean is the wrong notion of "average" on the SPD cone. Using the affine-invariant metric $\langle X,Y\rangle_A = \operatorname{tr}(A^{-1}XA^{-1}Y)$, the cone is a Hadamard manifold (complete, simply connected, nonpositive curvature), so the geodesic distance, the geodesic interpolation $A\#_t B = A^{1/2}(A^{-1/2}BA^{-1/2})^t A^{1/2}$, and the **Karcher/Fréchet mean** (minimizer of the sum of squared geodesic distances) are all well posed. For more than two matrices the mean has no closed form and is characterized by the variational fixed-point equation $\sum_i \log(\bar A^{-1/2} A_i \bar A^{-1/2}) = 0$, solved by a Riemannian gradient iteration. This is the canonical small-matrix-analysis treatment of the SPD geometric mean. See [[SPD-manifold geometry and Riemannian optimization]].

## Problem & setting

Given a finite set of SPD matrices (covariances, diffusion tensors, elasticity tensors), what is their "mean"? The arithmetic mean $\frac1n\sum A_i$ is SPD but inflates the determinant (swelling) and is not invariant under congruence $A\mapsto GAG^\top$ or inversion $A\mapsto A^{-1}$ — both of which are natural symmetries of a covariance. Moakher poses the problem as finding the Riemannian barycenter on the SPD manifold under the affine-invariant metric, and asks for its existence, uniqueness, and the geometric properties (determinant inequalities, invariance) the right mean should satisfy.

## Method

The affine-invariant metric makes the SPD cone a symmetric space of nonpositive curvature; geodesics, distance, and the exp/log maps have the $A^{1/2}$-sandwiched closed forms. Two distinct "means" are analyzed: the Riemannian-geometric (Karcher) mean defined by the variational problem $\bar A = \arg\min_X \sum_i \delta^2(X, A_i)$, and a Euclidean-projection mean tied to the log-Euclidean structure. Nonpositive curvature delivers geodesic convexity of the variance functional, hence existence and uniqueness of the Karcher mean and convergence of the gradient-descent fixed-point iteration. Moakher derives the first-order optimality condition $\sum_i \log(\bar A^{-1/2} A_i \bar A^{-1/2}) = 0$ and proves determinant and invariance identities.

## Key results

- Existence and uniqueness of the affine-invariant Karcher mean of finitely many SPD matrices, with a convergent Riemannian gradient iteration.
- The variational fixed-point characterization $\sum_i \log(\bar A^{-1/2} A_i \bar A^{-1/2}) = 0$, generalizing the two-matrix geometric mean $A\#B$ to $n>2$.
- Congruence- and inversion-invariance of the geometric mean, plus determinant inequalities relating it to the arithmetic and harmonic means.

## Relevance to this research

PIFB and the VFE transformer pool covariances across constituents when forming a coarse-grained meta-agent: $\bar\Sigma_I = \sum_i w_i\,\Omega_{I,i}\Sigma_i\Omega_{I,i}^\top / \sum_i w_i$ (the gauge-covariant sandwich-then-average rule in `meta_agents.py`). That weighted *sandwich-average* is an arithmetic mean in the ambient space, not the affine-invariant Karcher mean Moakher characterizes. This paper is the precise statement of the **open question** flagged in the program: the cheap sandwich pool only *approximates* the true Fréchet barycenter, and the two coincide only in the small-dispersion limit (first-order / linearized). Moakher's fixed-point equation $\sum_i w_i \log(\bar\Sigma^{-1/2}\Sigma_i\bar\Sigma^{-1/2})=0$ is the exact target the coarse-graining would solve if it ran a Karcher iteration instead of one averaging step, and its nonpositive-curvature uniqueness theory is what licenses calling any such barycenter "the" meta-agent covariance. This directly supports [[Meta-agents and hierarchical emergence]] and the SPD-pooling discussion in [[SPD-manifold geometry and Riemannian optimization]].

## Cross-links

- Meta-agent SPD pooling and the sandwich-vs-Fréchet gap: [[Meta-agents and hierarchical emergence]]
- SPD geometry foundations: [[bhatia-2007-positive-definite-matrices]], [[pennec-2006-affine-invariant-tensor]], [[arsigny-2006-log-euclidean]]
- Existence/uniqueness of Riemannian barycenters: [[karcher-1977-center-of-mass]]
- Cost of exact vs cheap means: [[jeuris-2012-matrix-geometric-mean]]
- Theme: [[SPD-manifold geometry and Riemannian optimization]] · [[Natural gradient]]
- Manuscript: [[participatory-it-from-bit]]

```bibtex
@article{moakher2005differential,
  title   = {A Differential Geometric Approach to the Geometric Mean of Symmetric Positive-Definite Matrices},
  author  = {Moakher, Maher},
  journal = {SIAM Journal on Matrix Analysis and Applications},
  volume  = {26},
  number  = {3},
  pages   = {735--747},
  year    = {2005},
  publisher = {SIAM},
  doi     = {10.1137/S0895479803436937}
}
```
