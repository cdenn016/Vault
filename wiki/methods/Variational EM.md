---
type: method
title: Variational EM
aliases:
  - VEM
  - Variational Expectation-Maximization
  - Variational EM algorithm
tags:
  - cluster/vfe
  - cluster/methodology
  - project/transformer
status: stable
created: 2026-06-18
updated: 2026-06-19
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
tractable approximating distribution `q` rather than recover the true posterior,
giving the *variational* EM that the VFE transformer's inference loop instantiates.

## How it works

VEM maximizes a lower bound on the log marginal likelihood
`log p(x) >= F[q, theta]`, where the bound `F` is the [[Variational free energy]]
(taken with a sign convention so that ascent maximizes it). For a single
observation with latent variable `z`, this bound decomposes as expected
log-likelihood minus the KL divergence between the approximate posterior `q(z)`
and the prior. Crucially, the gap between the bound and `log p(x)` is exactly
`KL(q || p(z|x))`, so tightening the bound in `q` *is* approximate posterior
inference. Neal and Hinton's key observation, in [[neal-1998-variational-em]], is
that both steps optimize the **same** objective:

- **E-step (belief update).** Hold parameters `theta` fixed; improve `q`. With an
  exact, unconstrained `q` this recovers the true posterior and closes the KL gap;
  with a restricted variational family (e.g. a Gaussian) it returns the
  closest member. Because the objective is shared, this step need not be run to
  convergence — *partial* and *incremental* E-steps still ascend the bound, which
  is precisely what licenses the online, filtering-style updates used downstream.
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
mode-seeking behaviour of the KL-based ELBO can underestimate posterior variance.
The bound can also be loose, leaving an amortization gap when a single encoder
must serve all inputs — the motivation for the iterative scheme of
[[marino-2018-iterative-amortized-inference]]. And coordinate ascent on a
non-convex bound only guarantees a local optimum.

## Relation to this work

The VFE transformer is built directly on a variational-EM skeleton, and the model
config's `gradient_mode: "filtering"` is the design's name for a partial,
incremental E-step in the sense of [[neal-1998-variational-em]].

- **What it borrows.** Each token carries a Gaussian belief `(mu, Sigma)` from the
  `gaussian_diagonal` family. The **E-step** updates these beliefs by
  precision-weighted free-energy relaxation, in the lineage of
  [[bogacz-2017-free-energy-tutorial]] and [[rao-1999-predictive-coding]], and
  surfaces as [[Precision weighting|precision-weighted attention]]. The **M-step**
  updates the network's gauge and projection parameters. The ELBO/free-energy
  training objective is the [[Variational free energy]] of
  [[friston-2010-free-energy-principle]], and the per-token Gaussian recognition
  beliefs follow the [[kingma-2013-auto-encoding-variational-bayes]] blueprint of
  optimizing diagonal-Gaussian posteriors by gradient descent.

- **How it differs / improves.** Where textbook VEM uses Euclidean gradient steps
  in flat parameter coordinates, the VFE transformer replaces both steps with
  geometry-aware updates. The M-step uses a [[Natural gradient]] preconditioned by
  the [[Fisher information metric]] (after [[amari-1998-natural-gradient]]),
  block-structured over the GL(k) gauge group much as K-FAC factorizes curvature.
  The covariance `Sigma` is treated as a point on the SPD manifold and updated by a
  Riemannian retraction rather than an unconstrained step, so the "M-step" for
  beliefs is Riemannian optimization on the SPD cone. The ELBO is further
  generalized: instead of the KL-based bound the model trains a
  [[Renyi divergence|Renyi]] / [[Alpha-divergence|alpha]] objective, with KL
  recovered as the `alpha -> 1` limit, broadening the single free-energy functional
  that Neal and Hinton, and later Friston, place at the center of the scheme.

> [!note] Editorial: The mapping "E-step = belief/attention update, M-step =
> parameter update, free energy = training loss" is the organizing idea of the
> architecture; the individual sources establish each piece, but the synthesis is
> this wiki's reading.

## Sources

- [[neal-1998-variational-em]] — EM as coordinate ascent on one free-energy/ELBO
  functional; the justification for incremental and partial (filtering) updates.
- [[friston-2010-free-energy-principle]] — perception, attention, and learning as
  free-energy minimization; the objective the transformer trains.
- [[rao-1999-predictive-coding]] — precision-weighted prediction-error dynamics;
  the ancestor of the E-step belief updates.
- [[bogacz-2017-free-energy-tutorial]] — explicit Gaussian E-step / M-step update
  equations mirrored by the filtering gradient mode.
- [[kingma-2013-auto-encoding-variational-bayes]] — ELBO + reparameterization for
  gradient-trained diagonal-Gaussian beliefs.
- [[marino-2018-iterative-amortized-inference]] — iterative refinement of beliefs
  that closes the amortization gap.
- [[millidge-2020-pc-approximates-backprop]] — local free-energy minimization
  equals backprop, unifying the inference loop with gradient training.
- [[amari-1998-natural-gradient]] — Fisher-preconditioned steepest descent for the
  M-step.

## See also

- [[Variational free energy]] — the functional VEM ascends.
- [[Evidence lower bound (ELBO)]] — the bound, in maximization form.
- [[Predictive coding network]] — the neural realization of the E-step.
- [[Free-energy principle active inference]] — the generalized scheme.
- [[Variational autoencoder (VAE)]] — amortized VEM with the reparameterization trick.
- [[Iterative amortized inference]] — multi-step E-step with a learned optimizer.
- [[Natural gradient]] and [[Fisher information metric]] — the geometry of the M-step.
- [[Renyi divergence]] and [[Alpha-divergence]] — the generalized training objective.
- [[Variational free energy and predictive coding]] — the theme grouping these sources.
- [[Inference machinery — variational EM and filtering]] — the theme for the inference loop.
- [[VFE Transformer Program]] — the project this method serves.
