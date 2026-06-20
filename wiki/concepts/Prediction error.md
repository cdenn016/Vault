---
type: concept
title: Prediction error
aliases:
  - Prediction errors
  - PE
  - Residual error
tags:
  - cluster/vfe
  - cluster/attention
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Prediction error

## Definition

A **prediction error** is the signed discrepancy between an observation (or a target) and the model's prediction of it: the residual `e = x - g(mu)`, where `x` is the observed quantity, `mu` is the model's current belief (or hidden cause), and `g` is the generative mapping from belief to expected observation. In a probabilistic generative model with Gaussian likelihood, the prediction error is not used raw but **weighted by precision** — the inverse covariance `Pi = Sigma^{-1}` of the relevant distribution — so the quantity that actually drives inference and learning is the *precision-weighted prediction error* `Pi * e`. This weighting is exactly the gradient of a squared-error term `(1/2) e^T Pi e` with respect to the mean, which is why prediction errors appear as the workhorse of every gradient on a Gaussian [[Variational free energy]] objective.

Prediction error generalizes beyond the input layer: in a hierarchical model each level predicts the level below, so there is a prediction error at *every* layer — a sensory error comparing data to top-down prediction, and a "state" or prior error comparing each belief to the prediction descending from the level above. Minimizing the total precision-weighted prediction error across all levels is equivalent to minimizing free energy.

## Why it matters here

The VFE transformer is, at heart, a machine for computing and discharging prediction errors. Its per-token Gaussian beliefs `(mu, Sigma)` are updated in an E-step that descends the free-energy gradient, and that gradient *is* a precision-weighted prediction error: each token's belief is pulled toward the data it must explain and toward the prediction implied by its context, with the pull scaled by precision. The architecture's [[Precision weighting|precision-weighted attention]] is the mechanism by which one token's prediction error is routed to and weighted against the beliefs of other tokens — a learned, content-dependent assignment of how much each error should count. Because the training objective is a free energy / negative [[Evidence lower bound (ELBO)]], the parameters in the M-step are also moved by accumulated prediction errors, so the same quantity that drives perception (belief updates) drives learning (parameter updates). Prediction error is therefore the common currency linking the E-step, the M-step, and the attention computation.

> [!note] Editorial: In the config's "filtering" gradient mode, beliefs are updated by partial, online descent rather than to convergence, so what flows between tokens and layers each step is a residual prediction error rather than a fully relaxed posterior — exactly the incremental-EM picture below.

## Details

**Gaussian generative model.** Suppose `x | mu ~ N(g(mu), Sigma_x)` and a prior `mu ~ N(mu_0, Sigma_0)`. The negative log joint (the free energy under a point/Gaussian belief) is, up to constants,
`F = (1/2) (x - g(mu))^T Sigma_x^{-1} (x - g(mu)) + (1/2) (mu - mu_0)^T Sigma_0^{-1} (mu - mu_0)`.
Define the two prediction errors `e_x = x - g(mu)` (sensory) and `e_mu = mu - mu_0` (prior). The belief gradient is
`dF/dmu = -g'(mu)^T (Sigma_x^{-1} e_x) + Sigma_0^{-1} e_mu`,
i.e. a difference of precision-weighted prediction errors. Gradient descent on `mu` is the E-step; it drives `mu` until the bottom-up error (transposed through the Jacobian) balances the top-down error. [[bogacz-2017-free-energy-tutorial]] derives exactly these updates and shows the precisions `Sigma^{-1}` learn in an analogous M-step, with the prediction error appearing as the error signal in every update.

**Predictive coding.** [[rao-1999-predictive-coding]] introduced this as a cortical model: feedback connections carry predictions `g(mu)`, feedforward connections carry precision-weighted prediction errors `Sigma_x^{-1} e_x`, and dedicated "error units" represent the residual. This is the direct ancestor of the VFE transformer's error-driven belief dynamics and its precision weighting; see [[Predictive coding network]] and the theme [[Variational free energy and predictive coding]]. [[friston-2010-free-energy-principle]] elevates the same arithmetic to a general principle: perception, attention, and action all minimize free energy, and *attention* is precisely the optimization of precision on prediction errors — the inferential reading of [[Precision weighting]].

**Relation to free energy and backprop.** [[neal-1998-variational-em]] frames the whole loop as coordinate ascent on one negative-free-energy functional, with an E-step over beliefs and an M-step over parameters; partial E-steps (filtering) are sanctioned by this view. [[millidge-2020-pc-approximates-backprop]] proves that local prediction-error minimization along an arbitrary computation graph converges to the *exact* backpropagation gradient — so the network's error-passing E-step and ordinary gradient training are two views of the same computation. The amortized refinement of beliefs by re-encoding free-energy gradients (i.e. prediction errors) is [[Iterative amortized inference]] ([[marino-2018-iterative-amortized-inference]]), which closes the amortization gap left by a single-pass encoder.

**Variants.**
- *Raw vs. precision-weighted*: the bare residual `e` versus `Pi e`. Only the weighted form is the free-energy gradient.
- *Sensory vs. prior/state error*: bottom-up data residual versus top-down belief residual; both are minimized jointly across a hierarchy.
- *Divergence generalization*: under a Renyi/[[Alpha-divergence]] objective ([[li-turner-2016-renyi-vi]], [[vanerven-2014-renyi-kl]]) the squared Mahalanobis error generalizes to an alpha-reweighted discrepancy that recovers the ordinary precision-weighted error as `alpha -> 1` (the KL limit).
- *Reparameterized error*: when beliefs are sampled rather than held at the mode, the [[Reparameterization trick]] ([[kingma-2013-auto-encoding-variational-bayes]]) lets the prediction error's gradient flow through the sampled `mu = mu + Sigma^{1/2} eps`.

**Geometry.** Because the error is weighted by an inverse covariance, the "right" descent direction on it is the [[Natural gradient]] — the gradient preconditioned by the inverse [[Fisher information metric]] ([[amari-1998-natural-gradient]], [[amari-2000-methods-information-geometry]]). For the SPD covariance itself the relevant residual lives in a curved space, so updates use a retraction on the SPD manifold rather than a Euclidean step (see [[SPD-manifold geometry and Riemannian optimization]]).

## In this work

Prediction error surfaces wherever the model config exposes its inference machinery:

- **E-step / belief updates.** The per-token Gaussian belief `(mu, Sigma)` is relaxed by descending the free-energy gradient, whose mean component is the difference of precision-weighted prediction errors above. The `gradient_mode: filtering` setting makes these partial, online updates, so a *residual* prediction error is what propagates — the incremental-EM regime of [[neal-1998-variational-em]] and the filtering theme [[Inference machinery — variational EM and filtering]].
- **Precision-weighted attention.** Attention scores weight inter-token contributions by precision, routing each token's prediction error to the beliefs that should absorb it; this is the architectural realization of [[Precision weighting]] and the precision-optimization-as-attention reading of [[friston-2010-free-energy-principle]]. The kernel-smoother view of attention ([[tsai-2019-kernel-attention]]) and the softmax baseline ([[vaswani-2017-attention]]) are the operations this modifies.
- **M-step / parameter learning.** Accumulated prediction errors drive parameter updates on the ELBO/free-energy loss, with Fisher/[[Killing form|Killing-form]] preconditioning per block — the metric-aware learning of [[bogacz-2017-free-energy-tutorial]] and [[amari-1998-natural-gradient]].

## Sources

- [[rao-1999-predictive-coding]] — cortical predictive coding; feedforward precision-weighted prediction errors.
- [[friston-2010-free-energy-principle]] — free energy as bounded surprise; attention as precision on prediction errors.
- [[bogacz-2017-free-energy-tutorial]] — explicit Gaussian E-step/M-step updates in terms of prediction errors.
- [[neal-1998-variational-em]] — EM as coordinate ascent on negative free energy; partial (filtering) E-steps.
- [[millidge-2020-pc-approximates-backprop]] — local prediction-error updates equal backprop gradients.
- [[marino-2018-iterative-amortized-inference]] — iterative refinement of beliefs from free-energy gradients.
- [[kingma-2013-auto-encoding-variational-bayes]] — ELBO, reparameterized Gaussian beliefs.
- [[li-turner-2016-renyi-vi]], [[vanerven-2014-renyi-kl]] — Renyi/alpha generalization of the error-bearing objective.
- [[amari-1998-natural-gradient]], [[amari-2000-methods-information-geometry]] — natural-gradient geometry of precision-weighted descent.
- [[vaswani-2017-attention]], [[tsai-2019-kernel-attention]] — attention baseline and kernel view that precision weighting modifies.

## See also

- [[Variational free energy]]
- [[Evidence lower bound (ELBO)]]
- [[Precision weighting]]
- [[Amortized inference]]
- [[Reparameterization trick]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[Predictive coding network]]
- [[Iterative amortized inference]]
- [[Free-energy principle active inference]]
- [[Variational EM]]
- [[Variational free energy and predictive coding]]
- [[Inference machinery — variational EM and filtering]]
