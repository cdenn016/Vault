---
type: paper
title: "An Elementary Introduction to Information Geometry"
aliases:
  - "Nielsen 2020 — Elementary Introduction to Information Geometry"
  - "Nielsen IG review"
authors:
  - Frank Nielsen
year: 2020
arxiv: "1808.08271"
url: https://www.mdpi.com/1099-4300/22/10/1100
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# An Elementary Introduction to Information Geometry

> [!info] Citation
> Frank Nielsen (2020). *An Elementary Introduction to Information Geometry.* Entropy, 22(10), 1100. MDPI. DOI: 10.3390/e22101100. arXiv:1808.08271.

## TL;DR

A self-contained, pedagogical review of information geometry written for non-specialists. It develops the geometry of a [[Statistical manifold]] from first principles: the [[Fisher information metric]] as the canonical Riemannian metric on a parametric family, the dual pair of $\alpha$-connections (the exponential $e$-connection and mixture $m$-connection) tied together by the Amari–Chentsov cubic tensor, and the *dually flat* structure in which Bregman / canonical divergences, the [[Alpha-divergence]] family, and a generalized Pythagorean theorem live. The treatment is example-driven (Gaussian and categorical families, exponential families with their convex log-partition / dual potential pair) and closes with the role of these structures in the [[Natural gradient]] and in statistical estimation. It is the gentlest modern on-ramp to the apparatus that Amari's monographs ([[amari-2000-methods-information-geometry]], [[amari-2016-information-geometry-applications]]) and the Ay–Jost–Lê–Schwachhöfer book ([[ay-2017-information-geometry]]) cover at research depth.

## Problem & setting

Information geometry studies a family of probability distributions $\{p(x;\theta)\}$ not as a flat parameter box but as a curved manifold $\mathcal{M}$ whose intrinsic structure is dictated by statistics rather than by an arbitrary coordinate choice. The motivating difficulty the review addresses is expository: the foundational results (Chentsov's uniqueness theorem, the dual-connection formalism, the Legendre / convex-duality picture of exponential families) are scattered across measure-theoretic monographs that presuppose Riemannian geometry. Nielsen's setting is the finite-dimensional, regular parametric case, where everything can be written explicitly and checked on the Gaussian and discrete examples, deferring the singular and infinite-dimensional subtleties handled in [[ay-2017-information-geometry]].

## Method

The construction proceeds in layers. On a parametric family the [[Fisher information metric]] is introduced as the expected outer product of score functions,
$$ g_{ij}(\theta) = \mathbb{E}_{p(x;\theta)}\!\left[\partial_i \log p(x;\theta)\,\partial_j \log p(x;\theta)\right], $$
giving a Riemannian metric whose canonical status follows from invariance under sufficient statistics (Chentsov). Onto this metric the review layers a one-parameter family of affine connections $\nabla^{(\alpha)}$, the $\alpha$-connections, with the exponential ($\alpha=1$) and mixture ($\alpha=-1$) connections forming a *dual pair* with respect to $g$: the difference of their Christoffel symbols is the totally symmetric Amari–Chentsov tensor $T_{ijk}$. When the manifold is dually flat — as every exponential family is — there exist two global affine coordinate systems, the natural parameter $\theta$ and the expectation parameter $\eta$, related by the Legendre transform of the convex log-partition function $F(\theta)$ and its dual potential $F^{*}(\eta)$. The canonical (Bregman) divergence built from $F$ is the relative entropy for exponential families, and divergence minimization becomes orthogonal projection, yielding a generalized Pythagorean theorem. The review then identifies the steepest-descent direction in this geometry as the [[Natural gradient]] $G^{-1}\nabla L$, recovering Amari's correction.

## Key results

1. The Fisher metric, the $\alpha$-connections, and the Amari–Chentsov tensor are presented as the canonical, reparameterization-invariant structures on a statistical manifold, with the dual-connection identity $\nabla^{(\alpha)} + \nabla^{(-\alpha)} = 2\nabla^{(0)}$ (Levi-Civita) made explicit.
2. Dually flat (exponential-family) manifolds carry a Legendre pair $(F,F^{*})$ of convex potentials, dual affine coordinates $(\theta,\eta)$, and a canonical Bregman divergence; KL divergence is the Bregman divergence of the log-partition function, recovered here as a worked corollary.
3. A generalized Pythagorean theorem and projection theorem hold for these divergences, framing maximum-likelihood and variational fits as geometric projections.
4. The $\alpha$-divergences, the relative entropy, and the natural gradient are all unified as facets of one dual geometry, presented concretely on Gaussian and categorical models.

## Relevance to this research

This review is the pedagogical entry point — explicitly the role the ingest manifest assigns it and the way the info-geometry audit and debate lenses cite it — to the information geometry that the VFE transformer's divergence terms and natural-gradient M-step rest on. The model's free-energy functional is built almost entirely from KL terms between Gaussian belief tuples $(\mu, \Sigma)$ and their priors; Nielsen's dually-flat exposition is the clean statement that, for the Gaussian exponential family, each such KL is the canonical Bregman divergence of the log-partition function, so the E-step's belief refinement is a sequence of information projections rather than ad hoc fitting. The dual coordinates $(\theta,\eta)$ are exactly the natural / expectation parameterizations the architecture moves between when it works in the Lie-algebra `phi` coordinate, the SPD covariance, or the moment representation, and the review makes the reparameterization invariance of the whole picture transparent. The $\alpha$-connection / [[Alpha-divergence]] material is the umbrella under which the model's KL and its Rényi/$\alpha$ generalizations ([[li-turner-2016-renyi-vi]], [[vanerven-2014-renyi-kl]]) sit, and the closing natural-gradient section is the elementary version of the result developed in full by [[amari-1998-natural-gradient]] that motivates the Fisher / Killing preconditioning of the M-step.

> [!note] Editorial: This is a review / survey, not a source of new theorems — its value to the project is as a citable, self-contained reference for the standard dual-geometry facts, useful when a manuscript needs to state the Fisher-metric or dually-flat KL identity without re-deriving it. Where research-grade rigor (singular models, infinite dimensions, Chentsov uniqueness with proof) is needed, cite [[ay-2017-information-geometry]] or [[amari-2000-methods-information-geometry]] instead. Page references here track the structure of the standard text; the equation numbers were not transcribed from a local copy and should be checked against the published version before quoting.

## Cross-links

- Concept: [[Fisher information metric]] — the canonical Riemannian metric the review builds the geometry on.
- Concept: [[Natural gradient]] — recovered in the closing section as steepest descent in the Fisher geometry.
- Concept: [[Statistical manifold]] — the central object, families of distributions as curved manifolds.
- Concept: [[Alpha-divergence]] — the divergence family arising from the dual $\alpha$-connections.
- Theme: [[Information geometry and natural gradient]].
- Related sources: [[amari-2000-methods-information-geometry]], [[amari-2016-information-geometry-applications]], [[ay-2017-information-geometry]], [[amari-1998-natural-gradient]].
- Projects: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model]].

## BibTeX

```bibtex
@article{nielsen2020elementary,
  author  = {Nielsen, Frank},
  title   = {An Elementary Introduction to Information Geometry},
  journal = {Entropy},
  volume  = {22},
  number  = {10},
  pages   = {1100},
  year    = {2020},
  publisher = {MDPI},
  doi     = {10.3390/e22101100},
  url     = {https://www.mdpi.com/1099-4300/22/10/1100}
}
```
