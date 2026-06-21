---
type: paper
title: "Statistical Computing on Manifolds: From Riemannian Geometry to Computational Anatomy"
aliases:
  - "Pennec 2009"
  - "Riemannian Computing Manifolds"
authors:
  - Pennec, Xavier
year: 2009
arxiv: null
url: null
tags:
  - cluster/spd-geometry
  - cluster/info-geometry
  - project/transformer
  - field/mathematics
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Statistical Computing on Manifolds: From Riemannian Geometry to Computational Anatomy

> [!info] Citation
> Pennec, Xavier (2009). "Statistical Computing on Manifolds: From Riemannian Geometry to Computational Anatomy." Book chapter (INRIA Sophia Antipolis – Asclepios Team), pp. 348–.

## TL;DR
Pennec develops a unified computational framework for statistics on Riemannian manifolds, grounding every algorithm — mean, covariance, Gaussian distribution, interpolation, PDE-based regularization — in the Exp/Log map pair as atomic operations. The framework is intrinsic (no ambient-space embedding) and is illustrated concretely on symmetric positive-definite (SPD) matrices (diffusion tensors) and on sulcal-line variability in computational anatomy. A key contribution is the Riemannian Gaussian defined by maximum-entropy in the exponential chart, with tractable Taylor approximations relating the concentration matrix to the covariance via the Ricci curvature.

## Problem & setting
Classical linear statistics break on curved manifolds: weighted sums of SPD matrices can leave the cone, Euclidean means on rotation groups yield non-rotations, and PDEs on tensor fields produce negative eigenvalues. Prior work either embedded manifolds extrinsically (losing intrinsic geometry) or treated each space ad hoc. The paper asks: can one build a general, intrinsic, algorithmic framework that specialises correctly to each curved space via only the Exp and Log maps?

## Method
The framework rests on a geodesically complete Riemannian manifold equipped with its Levi-Civita connection. The two atomic operations are:

- **Exp map**: $\mathrm{Exp}_p(v) = \gamma_{(p,v)}(1)$, the endpoint of the geodesic starting at $p$ with tangent $v$.
- **Log map**: $\mathrm{Log}_p(q) = \overrightarrow{pq}$, the smallest tangent vector at $p$ mapping to $q$.

Standard operations are uniformly recast as in Table 1 of the paper: subtraction $\to \mathrm{Log}$, addition $\to \mathrm{Exp}$, gradient descent $\to$ geodesic marching. The **Riemannian (Fréchet/Karcher) mean** minimises the variance $\sigma^2(q) = \frac{1}{n}\sum_i \mathrm{dist}(p_i, q)^2$ and is computed by the Gauss–Newton iteration
$$\bar{p}_{t+1} = \mathrm{Exp}_{\bar{p}_t}\!\left(\frac{1}{n}\sum_{i=1}^n \overrightarrow{\bar{p}_t p_i}\right),$$
which converges quadratically near non-degenerate critical points in 5–10 iterations for rotations, rigid motions, and SPD matrices. The **covariance** is computed in the exponential chart at the mean: $\Sigma = \frac{1}{n}\sum_i \overrightarrow{\bar{p}q_i}\,\overrightarrow{\bar{p}q_i}^T$. The **Riemannian Gaussian** is defined by maximum intrinsic entropy given mean and covariance:
$$\mathcal{N}_{(\bar{p},\Gamma)}(q) = k\exp\!\left(-\tfrac{1}{2}\overrightarrow{\bar{p}q}^T \Gamma\, \overrightarrow{\bar{p}q}\right),$$
with the curvature correction $\Gamma = \Sigma^{-1} - \tfrac{1}{3}\mathrm{Ric} + O(\sigma)$ relating concentration to covariance at first order. Principal Geodesic Analysis (PGA) generalises PCA by covariance analysis in the tangent space at the mean. The framework extends to manifold-valued fields (images) via PDEs formulated with Exp/Log, enabling interpolation, isotropic/anisotropic smoothing, and in-painting.

## Key results
The Riemannian variance is differentiable at all points where the cut locus has null probability mass, with gradient $\nabla\sigma^2(q) = -2\int \overrightarrow{qp}\,dP(p)$, matching the exponential-barycenter characterisation of the Karcher mean. The Riemannian chi-squared law for the Mahalanobis distance of a Riemannian Gaussian agrees with its Euclidean counterpart to third order in $\sigma$, opening the door to manifold generalisations of standard statistical tests. The Gauss–Newton mean algorithm converges to machine precision in 5–10 steps on SPD matrices and rotation groups. Applications demonstrate joint estimation and anisotropic smoothing of diffusion-tensor (DTI) fields and covariance-based modelling of sulcal-line variability in the brain.

## Relevance to this research
This paper is a core reference for the SPD belief geometry in the VFE transformer. The VFE framework represents beliefs as Gaussian tuples $(\mu, \Sigma, \phi)$ on SPD manifolds, and every operation — transporting beliefs via gauge parallel transport $\Omega_{ij}$, computing the KL divergence $\mathrm{KL}(q_i \| \Omega_{ij} q_j)$, retracting updated parameters back onto the SPD cone — requires exactly the Exp/Log atomic machinery Pennec formalises here. The Riemannian Gaussian maximum-entropy characterisation directly motivates why Gaussian beliefs are the natural exponential-family choice on SPD space, and the curvature correction $\Gamma = \Sigma^{-1} - \tfrac{1}{3}\mathrm{Ric}$ is relevant to higher-order accuracy of the VFE E-step. PGA / covariance analysis in the exponential chart at the mean is the geometric analogue of the attention-weighted mean used in the belief-update E-step. The extrinsic-vs-intrinsic robustness discussion (Section 3.5) also bears on whether Euclidean approximations to SPD geometry are acceptable in the VFE regime.

## Cross-links
- Concepts: [[SPD-manifold geometry and Riemannian optimization|SPD Manifold]], [[Riemannian Geometry]], [[Exponential map (Riemannian)|Exponential Map]], [[karcher-1977-center-of-mass|Karcher Mean]], [[Information Geometry]]
- Related sources: [[moakher-2005-geometric-mean|moakher-2005-spd-means]], [[bhatia-2007-positive-definite-matrices|bhatia-2009-positive-definite]], [[amari-2016-information-geometry-applications|amari-2016-information-geometry]]
- Manuscript/Project: [[VFE Transformer Program]], [[gl-k-attention|GL(K) Attention Manuscript]]

## BibTeX
```bibtex
@incollection{Pennec2009,
  author    = {Pennec, Xavier},
  title     = {Statistical Computing on Manifolds: From {Riemannian} Geometry to Computational Anatomy},
  booktitle = {Emerging Trends in Visual Computing},
  year      = {2009},
  pages     = {347--386},
  note      = {INRIA Sophia Antipolis -- Asclepios Team},
}
```
