---
type: reference
title: "Information Geometry and Its Applications"
aliases:
  - "Amari 2016"
authors:
  - "Shun-ichi Amari"
year: 2016
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/statistics
created: 2026-06-18
updated: 2026-06-18
---

# Information Geometry and Its Applications

> [!info] Citation
> Shun-ichi Amari (2016). *Information Geometry and Its Applications*. Applied Mathematical Sciences, vol. 194. Springer Japan, Tokyo. DOI: 10.1007/978-4-431-55978-8.

## TL;DR

Amari's monograph is the standard book-length treatment of information geometry: the study of families of probability distributions as Riemannian manifolds equipped with the [[Fisher information metric]] and a dual pair of affine connections (the $e$- and $m$-connections). It develops the dually flat structure, the canonical divergence, the generalized Pythagorean theorem, and projection theorems, and applies them to estimation, the EM algorithm, and learning machines.

## What it establishes

The book treats a parametric statistical model $\{p(x;\theta)\}$ as a differentiable manifold whose Riemannian metric is the Fisher information,

$$ g_{ij}(\theta) = \mathbb{E}\!\left[ \partial_i \log p \, \partial_j \log p \right], $$

singled out (following Chentsov) as essentially the unique metric invariant under sufficient statistics. Onto this manifold Amari builds:

- A one-parameter family of **$\alpha$-connections**, with the exponential ($e$, $\alpha=1$) and mixture ($m$, $\alpha=-1$) connections forming a *dually coupled* pair with respect to the metric. Relating these connections to [[Parallel transport]] and curvature gives the geometric backbone of the theory.
- The notion of a **dually flat manifold**, where two affine coordinate systems ($\theta$, $\eta$) are Legendre-dual via convex potentials, generating the **canonical divergence** — a Bregman divergence whose members include the Kullback-Leibler divergence and, more broadly, the [[Alpha-divergence]] and [[Renyi divergence]] families.
- The **generalized Pythagorean theorem** and **dual projection** theorems, which underwrite information-geometric accounts of maximum-likelihood estimation, the EM algorithm, and the geometry of the [[Evidence lower bound (ELBO)]].
- The connection between the metric and **second-order learning**: because the Fisher metric is the natural Riemannian structure on the parameter manifold, steepest descent in this geometry is the [[Natural gradient]], $\tilde\nabla L = g^{-1}\nabla L$, which Amari develops as the geometrically correct update for statistical learning.

> [!note] Editorial: This note summarizes the monograph's scope from the standard published edition (Applied Mathematical Sciences vol. 194); specific page or section numbers are not reproduced here.

## Why the project cites it

This reference supplies the geometric foundation that the project's information-geometry thread rests on.

- **Fisher metric and natural gradient.** The [[Fisher information metric]] and the [[Natural gradient]] are taken directly from Amari's framework. In the project's variational setting these provide the metric on belief space used for second-order belief updating, central to the [[Information geometry and natural gradient]] theme.
- **Divergences as the geometry of inference.** The dually flat / Bregman picture grounds how the project measures discrepancy between beliefs and targets. The [[Alpha-divergence]] and [[Renyi divergence]] generalizations of KL connect to variational objectives — the [[Variational free energy]] and the [[Evidence lower bound (ELBO)]] — used throughout the [[Free-energy principle active inference]] and [[Variational EM]] machinery.
- **Mass as Fisher information.** The project's identification of inertial mass with curvature of belief space — [[Mass as Fisher information]], with the attendant [[Belief inertia]] — leans on Amari's reading of the Fisher metric as the intrinsic Riemannian structure of a statistical manifold, the object whose curvature the project endows with dynamical meaning in [[Hamiltonian belief dynamics]].
- **Sections of a bundle.** Treating per-agent belief manifolds as fibres (see [[Agents as fibre-bundle sections]]) requires the dual-connection and [[Parallel transport]] apparatus that this book develops, linking information geometry to the project's [[Gauge transformation]] structure in the [[Gauge-Theoretic Multi-Agent VFE Model]].

See also the companion references [[amari-2000-methods-information-geometry]], [[ay-2017-information-geometry]], [[cencov-1982-statistical-decision-rules]], and the natural-gradient paper [[amari-1998-natural-gradient]].

## BibTeX

```bibtex
@book{amari2016information,
  title     = {Information Geometry and Its Applications},
  author    = {Amari, Shun-ichi},
  year      = {2016},
  series    = {Applied Mathematical Sciences},
  volume    = {194},
  publisher = {Springer Japan},
  address   = {Tokyo},
  doi       = {10.1007/978-4-431-55978-8},
  isbn      = {978-4-431-55977-1}
}
```
