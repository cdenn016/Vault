---
type: reference
title: A Riemannian Geometry of the Multivariate Normal Model
aliases:
  - "Skovgaard 1984"
  - "Riemannian Geometry of the Multivariate Normal Model"
authors:
  - Lene Theil Skovgaard
year: 1984
arxiv: null
url: https://www.jstor.org/stable/4615960
tags:
  - cluster/spd-geometry
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A Riemannian Geometry of the Multivariate Normal Model

> [!info] Citation
> Skovgaard, L. T. (1984). A Riemannian Geometry of the Multivariate Normal Model. Scandinavian Journal of Statistics, 11(4), 211-223. JSTOR 4615960.

## TL;DR

Skovgaard treats the family of $n$-variate normal distributions $N(\mu, \Sigma)$ as a Riemannian manifold whose metric is the Fisher information of the *full* parameter vector — mean and covariance jointly — and works out its differential geometry in concrete coordinates. The paper writes down the line element, derives the geodesic equations as a coupled system of second-order ODEs in $(\mu(t), \Sigma(t))$, identifies the closed-form Rao (geodesic) distance on the two tractable submanifolds (fixed covariance, and fixed mean), and computes the curvature, finding it negative but non-constant. It is the canonical reference for the statement that a Gaussian belief $(\mu, \Sigma)$ lives on a curved statistical manifold whose mean and covariance directions are geometrically *coupled*, and it remains the standard citation whenever the Fisher-Rao distance between Gaussians is invoked. The general joint-parameter geodesic problem has no known elementary closed form, a fact already implicit in Skovgaard's ODE system and still true today.

## Problem & setting

By 1984 the program initiated by Rao (1945) — equip a parametric family with the Fisher information as a Riemannian metric and measure statistical dissimilarity by geodesic ("Rao") distance — had produced clean answers for low-dimensional and single-parameter families, and for the univariate normal, whose Fisher-Rao geometry is the hyperbolic plane. The multivariate case was the natural next target and considerably harder: the parameter manifold is $\mathbb{R}^n \times \mathrm{Sym}^{+}(n)$, with the covariance ranging over the cone of symmetric positive-definite (SPD) matrices, and the Fisher metric mixes the mean and covariance blocks. Skovgaard's setting is exactly this full model. The assumptions are minimal — a regular $n$-variate normal family, the Fisher information as metric tensor — and the prior art it builds on is Rao's information-distance program together with the standard expressions for the Fisher information of a Gaussian. The contribution is to push that program through for the joint $(\mu, \Sigma)$ manifold rather than treating mean and covariance in isolation.

## Method

The metric is the Fisher information of $N(\mu, \Sigma)$. In the joint parameters its line element is
$$
ds^2 = d\mu^{\top}\,\Sigma^{-1}\,d\mu \;+\; \tfrac{1}{2}\,\mathrm{tr}\!\left[\left(\Sigma^{-1} d\Sigma\right)^2\right],
$$
the first term an affine-invariant inner product on mean increments scaled by the precision, the second the affine-invariant SPD metric on covariance increments. The mean and covariance blocks are *separately* diagonal in this expression, but they couple dynamically through the Christoffel symbols: a geodesic that moves the mean also bends the covariance, and vice versa. Skovgaard derives the geodesic equations as the coupled second-order system
$$
\ddot{\mu} \;=\; \dot{\Sigma}\,\Sigma^{-1}\,\dot{\mu},
\qquad
\ddot{\Sigma} \;=\; \dot{\Sigma}\,\Sigma^{-1}\,\dot{\Sigma} \;-\; \dot{\mu}\,\dot{\mu}^{\top},
$$
in which the $-\dot{\mu}\dot{\mu}^{\top}$ source term is precisely the mean-covariance coupling — motion in the mean feeds curvature back into the covariance trajectory. From these he extracts the Rao distance on the submanifolds where the system decouples and integrates in closed form, and he computes the sectional curvature of the full manifold.

## Key results

On the fixed-mean submanifold — covariance only, i.e. the SPD cone with the affine-invariant metric — the geodesic distance is the closed form
$$
d_F\!\left(\Sigma_1, \Sigma_2\right) \;=\; \tfrac{1}{\sqrt{2}}\,\Big(\textstyle\sum_i \log^2 \lambda_i\Big)^{1/2},
$$
where $\lambda_i$ are the eigenvalues of $\Sigma_1^{-1}\Sigma_2$; this is the now-standard affine-invariant / log-Euclidean-eigenvalue distance on SPD matrices. On the fixed-covariance submanifold — mean only, with $\Sigma$ held constant — the geometry is hyperbolic, recovering the classical hyperbolic-plane picture of the univariate normal in its $n$-dimensional form. For the *full* joint manifold Skovgaard establishes that the sectional curvature is negative but not constant, so the multivariate Gaussian model is not a space of constant curvature and is not, in general, a symmetric space treated naively; the mean-covariance coupling produces a curvature that varies across the manifold. The general $(\mu_1,\Sigma_1) \to (\mu_2,\Sigma_2)$ geodesic and its length admit no known elementary closed form — they must be obtained by integrating the ODE system numerically — which is why the modern literature devotes whole papers to bounding and approximating the Fisher-Rao distance between Gaussians. (The numerical claims here are reported qualitatively where I could not verify exact constants against the primary text; the line element, geodesic ODEs, and fixed-mean distance are corroborated across the secondary literature cited below.)

## Relevance to this research

This paper is the geometry of the object a token belief actually *is*. In the VFE transformer each token carries a Gaussian tuple $(\mu, \Sigma, \phi)$, and the $(\mu, \Sigma)$ part lives on exactly Skovgaard's joint mean-covariance manifold — not on the covariance-only SPD cone that the affine-invariant transport machinery usually foregrounds. Skovgaard is the first to write the geodesic ODEs and Rao distance for that joint manifold and to make explicit the mean-covariance coupling (the $-\dot\mu\dot\mu^\top$ term) and the non-constant negative curvature, which matters because any claim that belief transport or coupling acts on the covariance cone *alone* is using a submanifold, not the full Fisher-Rao geometry. The fixed-mean result is precisely the affine-invariant SPD distance the program leans on for covariance transport (see [[SPD-manifold geometry and Riemannian optimization]]), so this note is the primary-source anchor for that formula; the fixed-covariance hyperbolic result and the joint curvature qualify it. More broadly the metric here is the [[Fisher information metric]] specialized to the Gaussian family, the same tensor that defines the natural gradient used in the M-step, so Skovgaard fixes the curved geometry in which the model's beliefs and divergences should be read.

## Cross-links
- Concepts / Themes: [[SPD-manifold geometry and Riemannian optimization]], [[Fisher information metric]]
- Related sources: [[amari-1998-natural-gradient]], [[pennec-2006-affine-invariant-tensor]]

## BibTeX
```bibtex
@article{skovgaard1984riemannian,
  author  = {Skovgaard, Lene Theil},
  title   = {A {Riemannian} Geometry of the Multivariate Normal Model},
  journal = {Scandinavian Journal of Statistics},
  volume  = {11},
  number  = {4},
  pages   = {211--223},
  year    = {1984},
  publisher = {Wiley},
  url     = {https://www.jstor.org/stable/4615960}
}
```
