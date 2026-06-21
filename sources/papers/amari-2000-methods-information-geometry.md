---
type: paper
title: Methods of Information Geometry
aliases:
  - "Amari & Nagaoka 2000 — Methods of Information Geometry"
  - "amari-2000-information-geometry"
  - "amari2000informationgeometry"
authors:
  - Shun-ichi Amari
  - Hiroshi Nagaoka
year: 2000
arxiv: null
url: https://bookstore.ams.org/mmono-191
tags:
  - cluster/info-geometry
  - project/transformer
  - field/mathematics
  - field/statistics
status: stable
created: 2026-06-18
updated: 2026-06-18
---

# Methods of Information Geometry

> [!info] Citation
> Shun-ichi Amari and Hiroshi Nagaoka (2000). *Methods of Information Geometry*. Translations of Mathematical Monographs, Vol. 191. American Mathematical Society & Oxford University Press, 206 pp. Translated from the 1993 Japanese original by Daishi Harada. [bookstore.ams.org/mmono-191](https://bookstore.ams.org/mmono-191)

## TL;DR

This is the canonical monograph of *information geometry*: the study of families of probability distributions as differentiable manifolds equipped with a Riemannian metric (the [[Fisher information metric]]) and a one-parameter family of dual affine connections (the alpha-connections). Its central structural result is that an exponential family carries a *dually-flat* geometry in which the Kullback–Leibler divergence is a canonical Bregman divergence, the exponential (e-) and mixture (m-) connections are mutually dual with respect to the Fisher metric, and a generalized Pythagorean theorem governs projections. The book systematizes the geometry underlying maximum-likelihood estimation, the EM algorithm, and the [[Natural gradient]], and supplies the formal scaffolding behind [[Alpha-divergence]] and [[Renyi divergence]] families.

## Problem & setting

Classical statistics treats a parametric model as an indexed set of distributions $\{p_\theta\}$ but says little about its intrinsic *shape*. Amari and Nagaoka's program is to give that shape a rigorous differential-geometric form. A statistical model becomes a smooth manifold whose points are distributions and whose coordinates are parameters $\theta$. The question the book answers is: which geometric structures on this manifold are natural — that is, invariant under reparameterization and under sufficient statistics — and what do estimation, inference, and divergence minimization look like once expressed in those terms?

The answer requires more than a single metric. A defining move of information geometry is that the relevant structure is a *triple*: a metric plus a **pair** of affine connections that are dual to one another. This dual structure has no counterpart in ordinary Riemannian geometry and is what makes the theory specific to spaces of probability distributions.

## Method

The construction proceeds in layers.

- **Fisher metric.** On the manifold of distributions, the unique (up to scale) invariant Riemannian metric is the [[Fisher information metric]] $g_{ij}(\theta) = \mathbb{E}\!\left[\partial_i \log p_\theta \, \partial_j \log p_\theta\right]$. Chentsov's theorem (treated in the book) shows this invariance pins it down essentially uniquely. The Fisher metric measures distinguishability of nearby distributions and is the second-order term of the KL divergence.

- **Alpha-connections and duality.** Beyond the metric, the book introduces a one-parameter family of affine connections $\nabla^{(\alpha)}$ indexed by $\alpha \in \mathbb{R}$. The cases $\alpha = +1$ (exponential, **e-connection**) and $\alpha = -1$ (mixture, **m-connection**) are central. Two connections $\nabla$ and $\nabla^*$ are **dual** with respect to $g$ when parallel transport by one preserves inner products measured against transport by the other; the e- and m-connections are exactly dual, and $\nabla^{(\alpha)}$, $\nabla^{(-\alpha)}$ are dual in general. This is the formal home of *dual affine connections*.

- **Dually-flat spaces and Bregman/canonical divergences.** When a manifold is flat with respect to *both* members of a dual pair (an exponential family is the archetype), it admits two affine coordinate systems — the natural parameters $\theta$ and the expectation parameters $\eta$ — related by a Legendre transform of the log-partition (cumulant) function. In such a *dually-flat* space the canonical divergence is a Bregman divergence and reduces to the Kullback–Leibler divergence for exponential families.

- **Generalized Pythagorean theorem and projection.** In a dually-flat space, if the m-geodesic from $P$ to $Q$ is orthogonal (in the Fisher metric) to the e-geodesic from $Q$ to $R$, then $D(P\Vert R) = D(P\Vert Q) + D(Q\Vert R)$. Divergence minimization becomes a geometric *projection* onto a submanifold along a dual geodesic — the structure behind the EM algorithm (the e- and m-steps as alternating dual projections) and behind iterative scaling.

- **Alpha-divergences.** Paired with the alpha-connections is a family of alpha-divergences whose flat geometry reproduces the alpha-connection; KL is the $\alpha \to \pm 1$ limit. This family is the geometric backbone connecting to Rényi-type divergences.

## Key results

1. **Uniqueness of the Fisher metric** as the invariant metric on statistical manifolds (Chentsov).
2. **Dual structure** $(g, \nabla, \nabla^*)$ as the fundamental object, generalizing Levi-Civita geometry (where $\nabla = \nabla^*$ is the self-dual special case).
3. **Dually-flat geometry of exponential families**, with Legendre-conjugate $\theta$/$\eta$ coordinates and KL as the canonical divergence.
4. **Generalized Pythagorean theorem** and the interpretation of EM, mixture estimation, and maximum-likelihood as dual projections.
5. **Natural-gradient learning**: steepest descent in the Fisher metric, $\tilde{\nabla}L = G^{-1}\nabla L$, presented as the geometrically correct update on a statistical manifold (developed jointly with [[amari-1998-natural-gradient]]).
6. **Wide applications**: statistical inference, the EM algorithm, linear systems and time series, information theory, quantum information geometry, convex analysis, and neural networks.

## Relevance to this research

This monograph supplies the geometric grammar for the project's entire information-geometric and variational layer.

- **Fisher metric and natural gradient for the M-step.** The project's M-step updates parameters by [[Natural gradient]] descent; the legitimacy of preconditioning by the inverse [[Fisher information metric]] — rather than by an arbitrary curvature estimate — rests on Amari–Nagaoka's identification of the Fisher metric as the unique invariant metric. Killing-form per-block preconditioning on the `block_glk` gauge group is the Lie-group analogue of the same "use the invariant metric of the manifold" principle that this book establishes for statistical manifolds.

- **Dual connections and the variational E/M split.** The book's reading of EM as a pair of *dual projections* (e-projection in the M-step direction, m-projection for the inference step) is precisely the geometry beneath the project's variational EM with `gradient_mode "filtering"`: the E-step refines per-token Gaussian beliefs $(\mu, \Sigma)$ while the M-step moves parameters, and the two steps live on dual affine connections of the same manifold. The `family gaussian_diagonal` belief model is an exponential family, so the project's beliefs inhabit exactly the *dually-flat* setting where KL is the canonical Bregman divergence and the Pythagorean decomposition of free energy holds.

- **Alpha/Rényi divergence machinery.** The project's `divergence_family "renyi"` (with KL as the $\alpha\to 1$ limit) is a direct instance of the alpha-divergence/alpha-connection family catalogued here. The book explains *why* varying the divergence order continuously deforms the underlying connection and metric — grounding the choice of $\alpha$ as a geometric, not merely heuristic, knob. See [[Renyi divergence]] and [[Alpha-divergence]].

- **SPD covariance geometry.** The Gaussian belief covariances $\Sigma$ are symmetric-positive-definite; the affine-invariant Riemannian metric used for `spd_affine` retraction is the multivariate-Gaussian restriction of the Fisher-information geometry treated here, tying the project's SPD-manifold optimization back to the same invariant-metric foundation.

> [!note] Editorial: The project's pairing of an exponential-family belief model with a Rényi/alpha divergence and Fisher-metric natural gradient is, geometrically, a single coherent choice — the dually-flat structure of this monograph is what makes E-step inference, M-step learning, and divergence selection three views of one geometry rather than three unrelated design decisions.

## Cross-links

- Concepts: [[Fisher information metric]], [[Natural gradient]], [[Renyi divergence]], [[Alpha-divergence]]
- Related sources: [[amari-1998-natural-gradient]], [[martens-2020-natural-gradient-insights]], [[ollivier-2015-riemannian-metrics-nn]], [[li-turner-2016-renyi-vi]], [[vanerven-2014-renyi-kl]], [[pennec-2006-affine-invariant-tensor]]
- Themes: [[Information geometry and natural gradient]], [[SPD-manifold geometry and Riemannian optimization]]
- Methods: [[Variational EM]]
- Project: [[VFE Transformer Program]]

```bibtex
@book{amari2000methods,
  author    = {Amari, Shun-ichi and Nagaoka, Hiroshi},
  title     = {Methods of Information Geometry},
  series    = {Translations of Mathematical Monographs},
  volume    = {191},
  publisher = {American Mathematical Society and Oxford University Press},
  address   = {Providence, RI},
  year      = {2000},
  pages     = {206},
  note      = {Translated from the 1993 Japanese original by Daishi Harada},
  isbn      = {978-0-8218-0531-2}
}
```
