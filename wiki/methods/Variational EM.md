---
type: method
title: Variational EM
aliases:
  - VEM
  - Variational Expectation-Maximization
  - Variational EM algorithm
  - "Expectation Maximization"
  - "Expectation-Maximization"
  - "E-step and M-step"
tags:
  - cluster/vfe
  - cluster/methodology
  - project/transformer
status: stable
created: 2026-06-18
updated: 2026-07-10
---

# Variational EM

## What it is

Variational EM (VEM) is an iterative algorithm for fitting latent-variable
probabilistic models by alternately optimizing an approximate posterior and the
model parameters. Its modern formulation is due to Neal and Hinton, who showed
in [[neal-1998-variational-em]] that the classical Expectation-Maximization
algorithm can be read as **coordinate ascent on a single functional**: the
negative variational free energy, equivalently the [[Evidence lower bound (ELBO)]].
When the exact posterior cannot be computed, the E-step is relaxed to optimize a
tractable approximating distribution `q` rather than recover the true posterior.
The deployed VFE transformer borrows the alternating belief/parameter skeleton
but does not instantiate this shared-functional algorithm.

## How it works

VEM maximizes a lower bound on the log marginal likelihood
`log p(x) >= F[q, theta]`, where the bound `F` is the [[Variational free energy]]
(taken with a sign convention so that ascent maximizes it). For a single
observation with latent variable `z`, this bound decomposes as expected
log-likelihood minus the KL divergence between the approximate posterior `q(z)`
and the prior. The gap between the bound and `log p(x)` is exactly
`KL(q || p(z|x))`, so tightening the bound in `q` *is* approximate posterior
inference. Neal and Hinton's key observation, in [[neal-1998-variational-em]], is
that both steps optimize the **same** objective:

- **E-step (belief update).** Hold parameters `theta` fixed; improve `q`. With an
  exact, unconstrained `q` this recovers the true posterior and closes the KL gap;
  with a restricted variational family (e.g. a Gaussian) it returns the
  closest member. Partial and incremental E-steps retain the Neal–Hinton guarantee
  only when they improve the same bound later used by the M-step. This condition
  does not hold for the transformer's target-blind belief filter and separate
  decode cross-entropy.
- **M-step (parameter update).** Hold `q` fixed; improve `theta`, typically by
  maximizing the expected complete-data log-likelihood under `q`.

For the Gaussian-belief case the bound and its updates become explicit.
[[bogacz-2017-free-energy-tutorial]] derives the precision-weighted
prediction-error dynamics that minimize free energy for hierarchical Gaussian
models, yielding an E-step that relaxes the belief means toward a
precision-weighted balance of prediction errors and an M-step that learns the
precisions themselves. This is the same machinery that
[[rao-1999-predictive-coding]] proposed as a model of cortical computation, where
feedforward signals carry [[Prediction error]] and feedback carries top-down
predictions, with [[Precision weighting]] gating their relative influence.
[[friston-2010-free-energy-principle]] generalizes the whole scheme into the
free-energy principle, under which perception (the E-step), learning (the M-step),
and action all minimize one variational free-energy functional.

Two refinements connect VEM to gradient-based deep learning. First,
[[kingma-2013-auto-encoding-variational-bayes]] replaces the explicit E-step with
an **amortized** recognition network and optimizes the ELBO end-to-end via the
[[Reparameterization trick]], so the E-step becomes a single feedforward pass (see
[[Amortized inference]] and the [[Variational autoencoder (VAE)]]). Second,
[[marino-2018-iterative-amortized-inference]] reintroduces iteration on top of
amortization — learning an optimizer that repeatedly refines beliefs from
free-energy gradients (see [[Iterative amortized inference]]) — recovering the
multi-step character of a genuine E-step while closing the amortization gap.
[[millidge-2020-pc-approximates-backprop]] then closes the loop theoretically,
proving that local predictive-coding free-energy minimization (a [[Predictive coding network]])
converges to exact backpropagation gradients on arbitrary computation graphs, so
an E-step/M-step inference loop and end-to-end gradient training need not be rivals.

## Strengths / limitations

**Strengths.** VEM turns intractable Bayesian inference into a sequence of
tractable optimization steps over an explicit, monotonically-improving bound. The
shared-objective view of [[neal-1998-variational-em]] guarantees that incremental,
sparse, and partial updates still make progress, which is exactly what online and
streaming settings demand. It is modular: any tighter bound (for example the
Renyi family below) or any better optimizer for either step slots in without
changing the overall scheme.

**Limitations.** The approximation is only as good as the variational family: a
diagonal-Gaussian `q` cannot capture posterior correlations, and the
  reverse-KL orientation of the standard ELBO can underestimate posterior variance.
The bound can also be loose, leaving an amortization gap when a single encoder
must serve all inputs — the motivation for the iterative scheme of
[[marino-2018-iterative-amortized-inference]]. And coordinate ascent on a
non-convex bound only guarantees a local optimum.

## Relation to this work

The VFE transformer uses a structural-EM skeleton. In the retained sweep, its inner
forward stage performs one target-blind model-channel refinement and then one
target-blind Fisher-preconditioned belief refinement with
$q_i^{(0)}=p_i=s_i^{(1)}$. Neither update is a Neal–Hinton incremental step on the
decode objective. [[gl-k-attention-2026-07-09-review-revision]]

- **What it borrows.** Each token carries diagonal-Gaussian model and belief states.
  The retained **inner stage** first refines $s_i$ toward the learned global $r$ and
  gamma-weighted model consensus, then uses $q_i^{(0)}=p_i=s_i^{(1)}$ for one
  precision-weighted belief refinement, in the lineage of
  [[bogacz-2017-free-energy-tutorial]] and [[rao-1999-predictive-coding]], and
  surfaces as [[Precision weighting|precision-weighted attention]]. The **M-step**
  updates the learned parameters against decode cross-entropy through both unrolled
  refinements, a distinct objective. [[gl-k-attention-2026-07-09-review-revision]]

  The per-token Gaussian beliefs are explicit optimized state variables. The
  architecture has no neural recognition network, so the VAE amortization theorem
  is comparison material rather than a description of this update.

- **How it differs.** Joint Gaussian belief updates use Fisher geometry; the
  covariance block is one-half conventional AIRM. The frame table uses
  plain AdamW in the audited path, not
  a Fisher/K-FAC natural gradient, and the decode optimizer is separate. The
  configured order-[[Renyi divergence|Rényi]] term is a pairwise belief
  discrepancy with KL at order one; it is neither a Li–Turner variational bound
  nor an Amari alpha-connection. [[gl-k-attention-2026-07-09-review-revision]]

- **Where it departs from textbook VEM (2026-06-29).** Neal and Hinton's defining
  property is that the E-step and M-step ascend the **same** functional. The deployed
  vfe3 transformer does **not**: its model and belief refinements are **target-blind**.
  The first uses the hyper-prior and gamma model-consensus terms; the second carries no
  observation/likelihood term (the canonical $-\mathbb{E}_q[\log p(o\mid x)]$ is a
  gated stub with no live caller) and descends a self-coupling-plus-belief-alignment
  energy. The outer update instead minimizes decode cross-entropy through both paths.
  These are **distinct objectives**, a *structural* (generalized) EM with no
  monotone-evidence guarantee.
  The [[gl-k-attention|GL(K) manuscript]] states this in plain text ("the observation
  enters only the M-step loss, so the E-step is target-blind"; "rather than coordinate-
  ascent steps on a single shared free energy"), a deliberate deviation from the
  canonical [[participatory-it-from-bit|PIFB]] functional, where the observation term
  lives in the fast belief subsystem the beliefs descend. The measured consequence is
  that the belief covariance gets no per-token data precision and collapses to a near-
  constant learned prior, failing the $\sigma$-validation gate
  ([[2026-06-29-sigma-gate-fail-and-collapse]]).

> [!note] Editorial (2026-07-10): “Structural EM” names the alternating schedule,
> not a proof that the two inner refinements and outer decode optimize one ELBO. The
> retained one-$s$/one-$q$ schedule has no
> Neal–Hinton monotonicity or converged predictive-coding/backpropagation
> guarantee. [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[neal-1998-variational-em]] — EM as coordinate ascent on one free-energy/ELBO
  functional; incremental and partial updates retain the guarantee only when both
  coordinates optimize that same functional.
- [[friston-2010-free-energy-principle]] — shared-free-energy background used as
  comparison material; the deployed transformer uses separate objectives.
- [[rao-1999-predictive-coding]] — precision-weighted prediction-error dynamics;
  the ancestor of the E-step belief updates.
- [[bogacz-2017-free-energy-tutorial]] — explicit Gaussian E-step/M-step equations
  for a shared free energy; conceptual ancestry rather than an identity with the
  deployed filter.
- [[kingma-2013-auto-encoding-variational-bayes]] — ELBO + reparameterization for
  gradient-trained diagonal-Gaussian beliefs.
- [[marino-2018-iterative-amortized-inference]] — iterative refinement of beliefs
  that closes the amortization gap.
- [[millidge-2020-pc-approximates-backprop]] — converged predictive-coding updates
  recover backpropagation under the source paper's schedule; the truncated
  target-blind filter is outside that result.
- [[amari-1998-natural-gradient]] — Fisher-preconditioned steepest descent for the
  Gaussian belief update, not the frame or decode M-step.

## See also

- [[Variational free energy]] — the functional VEM ascends.
- [[Evidence lower bound (ELBO)]] — the bound, in maximization form.
- [[Predictive coding network]] — the neural realization of the E-step.
- [[Free-energy principle active inference]] — the generalized scheme.
- [[Variational autoencoder (VAE)]] — amortized VEM with the reparameterization trick.
- [[Iterative amortized inference]] — multi-step E-step with a learned optimizer.
- [[Natural gradient]] and [[Fisher information metric]] — the geometry of the Gaussian belief update.
- [[Renyi divergence]] and [[Alpha-divergence]] — distinct belief-side divergence comparisons, not one generalized complete-model training objective.
- [[Variational free energy and predictive coding]] — the theme grouping these sources.
- [[Inference machinery — variational EM and filtering]] — the theme for the inference loop.
- [[VFE Transformer Program]] — the project this method serves.
