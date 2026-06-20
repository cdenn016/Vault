---
type: paper
title: Natural Gradient Works Efficiently in Learning
aliases:
  - "Amari 1998 — Natural Gradient"
  - "Natural Gradient (Amari 1998)"
authors:
  - Shun-ichi Amari
year: 1998
arxiv: null
url: https://direct.mit.edu/neco/article/10/2/251/6143/Natural-Gradient-Works-Efficiently-in-Learning
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-18
updated: 2026-06-18
---

# Natural Gradient Works Efficiently in Learning

> [!info] Citation
> Shun-ichi Amari (1998). *Natural Gradient Works Efficiently in Learning.* Neural Computation, 10(2), 251–276. MIT Press. URL: https://direct.mit.edu/neco/article/10/2/251/6143/Natural-Gradient-Works-Efficiently-in-Learning

## TL;DR

When the parameters of a model live on a curved statistical manifold rather than in flat Euclidean space, the ordinary gradient is *not* the direction of steepest descent. Amari shows that the true steepest-descent direction is obtained by premultiplying the ordinary gradient by the inverse of the [[Fisher information metric]] — the **natural gradient**. This single correction makes learning invariant to reparameterization, avoids the slowdowns caused by plateaus and ill-conditioning, and, for online estimation, attains the asymptotic statistical efficiency of batch maximum likelihood (the Cramér–Rao bound). It is the founding result behind the [[Natural gradient]] now used throughout machine learning.

## Problem & setting

A learning system is parameterized by a vector $w \in \mathbb{R}^n$, but the parameter space is rarely a flat Euclidean space. For a family of probability distributions $p(x; w)$, the space of distributions is a Riemannian manifold whose intrinsic geometry is encoded by the [[Fisher information metric]] $G(w)$, with entries
$$ g_{ij}(w) = \mathbb{E}\!\left[\partial_i \log p(x;w)\,\partial_j \log p(x;w)\right]. $$
Squared distances between nearby parameter values are measured by $ds^2 = \sum_{ij} g_{ij}\, dw^i dw^j$, not by the naive Euclidean $\sum_i (dw^i)^2$. Because $G(w)$ varies across the manifold and is generally not the identity, the ordinary gradient $\nabla L(w)$ — which implicitly assumes a Euclidean metric — points in the steepest direction only under an arbitrary coordinate choice. Amari's question: what is the genuinely steepest descent direction of a loss $L(w)$ when the geometry is Riemannian?

## Method

The steepest-descent direction is defined as the vector that maximally decreases $L$ per unit *Riemannian* length. Solving this constrained problem yields the **natural gradient**
$$ \tilde{\nabla} L(w) = G^{-1}(w)\,\nabla L(w), $$
the ordinary gradient transformed by the inverse Fisher metric. The corresponding update is $w_{t+1} = w_t - \eta_t\, G^{-1}(w_t)\,\nabla L(w_t)$.

Key properties Amari establishes:

- **Reparameterization invariance.** Because $G$ transforms as a metric tensor, $G^{-1}\nabla L$ transforms as a contravariant vector; the resulting trajectory is independent of how the model is coordinatized. Two equivalent parameterizations produce the same learning path.
- **Online / adaptive efficiency.** For online learning of statistical models, the natural-gradient update with a $1/t$ schedule is *Fisher-efficient*: the estimator's asymptotic covariance attains the Cramér–Rao lower bound, matching offline maximum likelihood. Ordinary online gradient descent does not.
- **Plateau avoidance.** In multilayer perceptrons and similar models the loss surface has plateaus created by the singular, highly anisotropic Fisher metric. The natural gradient rescales by $G^{-1}$ precisely along these flat directions, dramatically accelerating escape from plateaus where ordinary gradient descent stalls.
- **Worked geometries.** The paper computes the Fisher metric (and hence the natural gradient) explicitly for several models, including multilayer perceptrons, blind source separation / independent component analysis, and linear systems, showing the construction is concrete and tractable.

## Key results

1. The natural gradient $G^{-1}\nabla L$ is the unique steepest-descent direction in a Riemannian parameter space.
2. Online natural-gradient learning is asymptotically Fisher-efficient, reaching the Cramér–Rao bound — a statistical optimality guarantee no plain-gradient scheme enjoys.
3. Empirically and theoretically, the method removes the plateau phenomenon that plagues backpropagation in neural networks.
4. The framework is reparameterization-invariant, giving a coordinate-free notion of "best local descent."

## Relevance to this research

This paper supplies the geometric backbone for the **M-step** of the VFE transformer's variational EM. After the E-step refines the per-token Gaussian beliefs $(\mu, \Sigma)$, parameters must be updated in a way that respects the curvature of the statistical model rather than treating raw coordinates as Euclidean. The natural gradient is exactly that update: it preconditions the free-energy gradient by the inverse Fisher metric so that learning is invariant to how the model is parameterized — directly relevant because the architecture exposes the *same* belief manifold through several coordinate systems (the Lie-algebra `phi` parameterization of the gauge group, the SPD covariance, the rotary/relative position encodings). Reparameterization invariance means the optimizer behaves identically regardless of these chart choices.

Several concrete connections:

- **Fisher-efficient belief estimation.** The "filtering" gradient mode performs online updates of the variational beliefs; Amari's Fisher-efficiency result is the precise statement that such online estimation can match batch maximum likelihood, which is the target the [[VFE Transformer Program]] wants for its streaming belief updates.
- **Preconditioning lineage.** The Killing-form per-block preconditioner on the `block_glk` gauge group is, conceptually, a natural-gradient-style metric correction restricted to a Lie-algebra; the Fisher metric is the canonical such correction for the probabilistic part of the model. The practical large-scale descendant of this idea — block/Kronecker approximations to the Fisher — appears in [[martens-2015-kfac]] and is analyzed in [[martens-2020-natural-gradient-insights]].
- **SPD geometry as a special case.** The affine-invariant metric on the SPD covariance manifold is a Riemannian metric of exactly the kind Amari abstracts; natural-gradient descent on $\Sigma$ is Riemannian optimization, tying this paper to [[pennec-2006-affine-invariant-tensor]] and [[bonnabel-2013-riemannian-sgd]].
- **Information-geometric foundation.** The Fisher metric here is the same object that underlies the dual-affine-connection picture and the Rényi/α-divergence family used for the model's divergence terms ([[amari-2000-methods-information-geometry]], [[li-turner-2016-renyi-vi]], [[vanerven-2014-renyi-kl]]).
- **Parameter-space metrics for neural nets.** The natural extension of these ideas to general deep networks is treated by [[ollivier-2015-riemannian-metrics-nn]].

> [!note] Editorial: The VFE transformer's preconditioning is best read as a *patchwork of metrics* — Fisher on the belief parameters, Killing form on the gauge algebra, affine-invariant on the SPD covariance — each the appropriate natural-gradient correction for its own factor of the parameter manifold. Amari's 1998 paper is the prototype that justifies all three as instances of one principle: descend along the gradient measured in the geometry that actually governs the quantity being optimized.

## Cross-links

- Concept: [[Natural gradient]] — the construction this paper introduces.
- Concept: [[Fisher information metric]] — the metric tensor $G(w)$ that defines the geometry.
- Concept: [[Renyi divergence]] and [[Alpha-divergence]] — divergences built on the same information-geometric foundation.
- Theme: [[Information geometry and natural gradient]].
- Methods/sources: [[martens-2015-kfac]], [[martens-2020-natural-gradient-insights]], [[amari-2000-methods-information-geometry]], [[ollivier-2015-riemannian-metrics-nn]], [[bonnabel-2013-riemannian-sgd]], [[pennec-2006-affine-invariant-tensor]].
- Project: [[VFE Transformer Program]].

## BibTeX

```bibtex
@article{amari1998natural,
  author  = {Amari, Shun-ichi},
  title   = {Natural Gradient Works Efficiently in Learning},
  journal = {Neural Computation},
  volume  = {10},
  number  = {2},
  pages   = {251--276},
  year    = {1998},
  publisher = {MIT Press},
  doi     = {10.1162/089976698300017746},
  url     = {https://direct.mit.edu/neco/article/10/2/251/6143/Natural-Gradient-Works-Efficiently-in-Learning}
}
```
