---
type: paper
title: "Riemannian Metric and Geometric Mean for Positive Semidefinite Matrices of Fixed Rank"
aliases:
  - Bonnabel Sepulchre 2009
  - SPD fixed-rank geometry
  - bonnabel-sepulchre-2009-psd-fixed-rank
  - Bonnabel & Sepulchre 2009
  - Bonnabel & Sepulchre (2009) PSD Fixed Rank
authors:
  - Bonnabel, Silvere
  - Sepulchre, Rodolphe
year: 2009
arxiv: "0807.4462"
url: https://doi.org/10.1137/080731347
tags:
  - cluster/spd-geometry
  - project/transformer
  - field/mathematics
  - field/statistics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Riemannian Metric and Geometric Mean for Positive Semidefinite Matrices of Fixed Rank

> [!info] Citation
> Bonnabel, S. and Sepulchre, R. (2009). "Riemannian Metric and Geometric Mean for Positive Semidefinite Matrices of Fixed Rank." *SIAM Journal on Matrix Analysis and Applications* 31(3), 1055–1070. DOI: [10.1137/080731347](https://doi.org/10.1137/080731347). Preprint: [arXiv:0807.4462](https://arxiv.org/abs/0807.4462).

## TL;DR
This paper introduces a Riemannian quotient geometry on the manifold S+(p,n) of positive semidefinite matrices of fixed rank p, obtained by factoring out the O(p) gauge action from the product of the Stiefel and positive definite cone manifolds. The resulting metric is invariant under orthogonal transformations, scalings, and pseudoinversion; the induced space is geodesically complete. An efficient SVD-based approximation of the Riemannian distance and a rank-preserving geometric mean are derived and shown to inherit the desirable invariance properties of the full-rank natural metric on the positive cone.

## Problem & setting
Positive definite matrices P_n carry a well-studied "natural" (affine-invariant, GL(n)-invariant) Riemannian metric that equals the Fisher information metric for Gaussian covariance estimation and coincides with the barrier metric of interior-point optimization. However, large-scale problems favor low-rank approximations A = ZZ^T with Z of size n x p, p << n, reducing cost from O(n^3) to O(np^2). The natural metric on P_n does not extend directly to rank-deficient matrices. Prior quotient representations (e.g., S+(p,n) ~ R^{nxp}_* / O(p)) had been studied, but no natural-metric analogue preserving the full invariance structure existed for the fixed-rank semidefinite case.

## Method
The key construction is the quotient representation
$$S_+(p,n) \cong (V_{n,p} \times P_p) / O(p),$$
where V_{n,p} is the Stiefel manifold and P_p is the positive definite cone. A matrix A = UR^2U^T with U in V_{n,p} and R in P_p is unique up to the O(p) gauge action (U, R^2) ~ (UO, O^T R^2 O). The proposed Riemannian metric on the horizontal space is the decoupled sum
$$g_{(U,R^2)}((\Delta_1,D_1),(\Delta_2,D_2)) = \mathrm{Tr}(\Delta_1^T \Delta_2) + k\,\mathrm{Tr}(R^{-1}D_1 R^{-2} D_2 R^{-1}),\quad k>0,$$
combining the standard Grassmann metric (for the subspace direction) and the natural metric on P_p (for the shape within the subspace). A connecting curve between A and B is built from the Grassmann geodesic U(t) (via principal angles and SVD of V_B^T V_A) and the cone geodesic R^2(t), yielding the approximation
$$l^2(\gamma_{A\to B}) = \|\Theta\|_F^2 + k\,\|\log R_A^{-1} R_B^2 R_A^{-1}\|_F^2,$$
computable at cost O(np^2). The geometric mean is the midpoint A o B = W K W^T, where K is the Riemannian mean of R_A^2 and R_B^2 in P_p and W is the Riemannian mean of the subspaces in Gr(p,n).

## Key results
Theorem 1 establishes that (S+(p,n), g) is a Riemannian manifold, with the metric invariant under orthogonal transformations, scalings, and pseudoinversion. Proposition 3 proves geodesic completeness: horizontal geodesics extend to all t in R, and S+(p,n) is a complete metric space. Theorem 2 shows that the SVD-based curve gamma_{A->B} is a horizontal lift of a geodesic in the structure space, with squared length given by the decoupled Grassmann-plus-cone formula. Proposition 2 establishes that l(gamma_{A->B}) upper-bounds the true Riemannian distance, with the gap controlled by k times the O(p)-orbit diameter of R_B^2 in P_p; the approximation is exact when the Grassmann contribution dominates (k small). Proposition 4 records that the geometric mean satisfies joint homogeneity, permutation invariance, monotonicity, congruence invariance, and self-duality under pseudoinversion. The mean is rank-preserving, unlike the Ando mean which can drop rank to dim(range(A) cap range(B)).

## Relevance to this research
The VFE transformer represents beliefs as Gaussian tuples (mu, Sigma) where Sigma is a positive definite (or positive semidefinite in low-rank approximations) covariance matrix. The quotient geometry S+(p,n) = (V_{n,p} x P_p)/O(p) is structurally identical to the gauge fiber bundle that underpins GL(K) gauge-equivariant attention: the O(p) group action on representatives is the same gauge redundancy that the VFE transformer's gauge transport Omega_{ij} must handle equivariantly. The decoupled metric decomposing into a Grassmann part (subspace direction) and a P_p part (shape/scale) parallels the decomposition of the VFE free energy into transport terms (which rotate beliefs across tokens) and self-coupling KL terms (which penalize deviation from priors within a fixed reference frame). The SVD-based efficient distance formula at O(np^2) cost is directly relevant for scalable SPD belief geometry in the transformer's E-step. The rank-preserving geometric mean provides a principled interpolation operation for low-rank belief covariances under the natural metric, relevant to any mixture or aggregation step over Gaussian beliefs.

## Cross-links
- Concepts: [[SPD-manifold geometry and Riemannian optimization|SPD Geometry]] | [[Grassmann Manifold]] | [[Riemannian Quotient Manifold]] | [[Information Geometry]] | [[Gauge Theory]]
- Related sources: [[bonnabel-2013-riemannian-sgd]] | [[pennec-2006-affine-invariant-tensor|pennec-2006-riemannian-framework-tensors]]
- Manuscript/Project: [[VFE Transformer Program]] | [[GL(K) Gauge-Equivariant Attention]]

## BibTeX
```bibtex
@article{BonnabelSepulchre2009,
  author  = {Bonnabel, Silv{\`e}re and Sepulchre, Rodolphe},
  title   = {Riemannian Metric and Geometric Mean for Positive Semidefinite Matrices of Fixed Rank},
  journal = {SIAM Journal on Matrix Analysis and Applications},
  year    = {2009},
  volume  = {31},
  number  = {3},
  pages   = {1055--1070},
  doi     = {10.1137/080731347},
  url     = {https://doi.org/10.1137/080731347},
  eprint  = {0807.4462},
  archivePrefix = {arXiv},
}
```
