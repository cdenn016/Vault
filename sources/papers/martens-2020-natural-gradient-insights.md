---
type: paper
title: "New Insights and Perspectives on the Natural Gradient Method"
aliases:
  - "Martens 2020"
  - "Martens 2020 — Natural Gradient Insights"
authors:
  - Martens, James
year: 2020
arxiv: "1412.1193"
url: https://arxiv.org/abs/1412.1193
tags:
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/mathematics
status: stable
created: 2026-06-18
updated: 2026-06-20
---

# New Insights and Perspectives on the Natural Gradient Method

> [!info] Citation
> James Martens (2020). "New Insights and Perspectives on the Natural Gradient Method." *Journal of Machine Learning Research* 21(146):1–76. [arxiv.org/abs/1412.1193](https://arxiv.org/abs/1412.1193)

## TL;DR

Martens reframes natural gradient descent not as an exotic information-geometric trick but as a principled second-order optimization method in which the Fisher information matrix plays the role normally occupied by the Hessian. The central technical result is that, for the loss functions used in practice (negative log-likelihoods of exponential-family or related predictive distributions), the Fisher matrix coincides with the Generalized Gauss-Newton (GGN) matrix — a positive-semidefinite curvature approximation. This identification explains why natural gradient works, justifies bolting on trust regions and Tikhonov damping, and clarifies the difference between the true Fisher and the often-misused empirical Fisher.

## Problem & setting

The natural gradient, introduced by Amari (see [[amari-1998-natural-gradient]]), preconditions the ordinary gradient by the inverse [[Fisher information metric|Fisher information matrix]] \(F^{-1}\), yielding a steepest-descent direction with respect to the [[Renyi divergence|KL divergence]] on the model's output distribution rather than the Euclidean geometry of raw parameters. This makes the update invariant to smooth reparameterization — a property Hessian-based Newton methods lack. The classical justification is geometric (information geometry; see [[amari-2000-methods-information-geometry]]), but that framing leaves practitioners unsure when natural gradient is well-behaved, how to damp it, and how it relates to plain second-order optimization.

Martens's setting is supervised learning where the model defines a conditional density \(p(y\mid x,\theta)\) and the loss is the average negative log-likelihood. The questions he addresses: in what precise sense is \(F\) a curvature matrix? When does it approximate the Hessian? How should one regularize and damp it for non-convex deep networks?

## Method

The paper is primarily analytical rather than algorithmic. Its key moves:

**Fisher = Generalized Gauss-Newton.** For losses that are negative log-likelihoods of a predictive distribution whose natural parameters are the network outputs, the Fisher matrix equals the GGN matrix \(J^\top H_L J\), where \(J\) is the Jacobian of the network outputs w.r.t. parameters and \(H_L\) is the (convex) Hessian of the loss in output space. Because \(H_L \succeq 0\), the Fisher is a positive-semidefinite approximation to the true Hessian that discards the indefinite curvature coming from the network's nonlinearity.

**Second-order view.** Natural gradient is then exactly an approximate Newton step using \(F\) in place of the Hessian. This motivates importing the machinery of second-order optimization: trust regions, Tikhonov / Levenberg-Marquardt damping \((F+\lambda I)^{-1}\), and adaptive choice of \(\lambda\).

**Empirical-Fisher critique.** Martens carefully distinguishes the true Fisher (expectation over the model's sampled labels \(y \sim p(y\mid x,\theta)\)) from the empirical Fisher (using the training labels). The empirical Fisher is not a valid curvature matrix in general and can badly mislead optimization — a frequent source of confusion in practice.

**Invariance and convergence.** He revisits the reparameterization-invariance of natural gradient and gives a convergence-rate analysis for stochastic natural gradient descent on convex quadratics.

## Key results

- The Fisher information matrix is the Generalized Gauss-Newton matrix for standard likelihood losses, making it a principled PSD curvature surrogate for the Hessian.
- This second-order reading explains the empirical robustness of natural-gradient and K-FAC-style optimizers and supplies a recipe for damping and trust-region control (the practical companion is the K-FAC approximation; see [[martens-2015-kfac]]).
- The empirical Fisher is shown to be a poor substitute for the true Fisher, with concrete failure modes.
- Natural gradient inherits parameterization invariance that Hessian-based Newton methods do not.

## Relevance to this research

The VFE-transformer's M-step updates gauge and belief parameters under a curved, non-Euclidean geometry, and this paper supplies the load-bearing justification for doing so with a preconditioned rather than raw gradient.

**Killing-form per-block preconditioning.** The model preconditions block-GL(k) updates by the Killing form of the Lie algebra. Martens's thesis — that the right metric in the parameter geometry acts as a curvature matrix substituting for the Hessian — is exactly the abstract principle the Killing-form preconditioner instantiates: for the gauge directions, the natural quadratic form on the Lie algebra plays the role \(F\) plays for the output distribution. The Fisher-as-GGN identity gives the template for why such a metric-preconditioned step is a sound approximate Newton step rather than an ad hoc rescaling.

**Natural gradient on the belief parameters.** The per-token Gaussian beliefs \((\mu,\Sigma)\) live in an exponential family, where the natural gradient is most natural. Martens clarifies that updating \((\mu,\Sigma)\) along \(F^{-1}\nabla\) is an approximate Newton step on the ELBO surrogate, and that one should use the true Fisher (model-sampled), not the empirical Fisher — a caution directly relevant to estimating curvature inside the filtering/variational-EM loop.

**Damping and stability.** The trust-region / Tikhonov-damping prescription \((F+\lambda I)^{-1}\) maps onto cocycle relaxation and the numerical conditioning needed when the SPD covariance or the gauge blocks become ill-conditioned during training.

> [!note] Editorial: The Killing form is the natural invariant metric on a semisimple Lie algebra, while Martens's Fisher is the metric on the output-distribution manifold; equating their roles (each is the curvature matrix for its own geometry) is an analogy this program adopts, not a theorem proved in this paper.

## Cross-links

- Concepts: [[Natural gradient]] · [[Fisher information metric]] · [[Renyi divergence]] · [[Alpha-divergence]]
- Foundational sources: [[amari-1998-natural-gradient]] · [[amari-2000-methods-information-geometry]] · [[martens-2015-kfac]] · [[ollivier-2015-riemannian-metrics-nn]]
- Theme: [[Information geometry and natural gradient]]
- Program: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{martens2020new,
  author  = {Martens, James},
  title   = {New Insights and Perspectives on the Natural Gradient Method},
  journal = {Journal of Machine Learning Research},
  volume  = {21},
  number  = {146},
  pages   = {1--76},
  year    = {2020},
  url     = {https://arxiv.org/abs/1412.1193},
  note    = {arXiv:1412.1193}
}
```
