---
type: concept
title: Amortized inference
aliases:
  - Amortized variational inference
  - Recognition network
  - Inference network
  - Amortization gap
tags:
  - cluster/vfe
  - cluster/methodology
  - project/transformer
status: draft
created: 2026-06-18
updated: 2026-06-18
---

# Amortized inference

## Definition

**Amortized inference** is a strategy for variational inference in which the
per-datapoint optimization that produces an approximate posterior is replaced by
a single learned function. In classical variational inference one fits a separate
set of variational parameters for every observation: given a datapoint $x$, one
runs an inner optimization to find the belief $q(z\mid x)$ — a distribution over
latent variables $z$ — that best approximates the true posterior $p(z\mid x)$.
Amortized inference instead trains a parametric *recognition* (or *inference*)
network $f_\phi$ that maps each observation directly to the parameters of its
belief, $q_\phi(z\mid x) = q\big(z;\, f_\phi(x)\big)$. The cost of the inner
optimization is thus *amortized* — paid once, at training time, across the whole
dataset — so that inference at test time reduces to one forward pass. The
canonical instance is the encoder of a [[Variational autoencoder (VAE)]], which
emits the mean and (diagonal) covariance of a Gaussian belief from the input,
introduced in [[kingma-2013-auto-encoding-variational-bayes]].

The price of this speed is the **amortization gap**: because a single network
must serve all datapoints, the belief it emits for any particular $x$ is
generally worse than the belief a dedicated per-datapoint optimization would
reach. The gap is the difference between the [[Evidence lower bound (ELBO)]]
attainable by the amortized network and the optimum attainable by free
per-datapoint variational parameters.

## Why it matters here

The VFE transformer maintains a per-token Gaussian belief $q(z_t) =
\mathcal{N}(\mu_t, \Sigma_t)$ over a latent state and trains by minimizing
[[Variational free energy]] (the negative ELBO). Amortized inference is the
mechanism that makes this tractable at sequence scale: rather than solving a
fresh variational optimization for every token of every sequence, the network's
forward computation *predicts* the belief parameters $(\mu_t, \Sigma_t)$ from
context, amortizing the inference cost across tokens and training examples. This
is exactly the role the recognition network plays in a VAE, lifted from a single
latent vector to a sequence of per-token beliefs.

The architecture, however, does not rely on a *single-pass* amortized encoder
alone. Its `gradient_mode: "filtering"` E-step refines the predicted beliefs by
taking [[Prediction error]] gradients of the free energy — a learned-plus-iterated
scheme that directly answers the amortization gap (see Details below). In the
predictive-coding reading the network supplies, amortized inference is the
"feedforward" prediction and the filtering refinement is the recurrent relaxation
that corrects it, mirroring the precision-weighted error dynamics of
[[rao-1999-predictive-coding]].

## Details

**The amortized ELBO.** For latent-variable model $p_\theta(x, z)$ and amortized
belief $q_\phi(z\mid x)$, training maximizes the amortized evidence lower bound
$$
\mathcal{L}(\theta,\phi) \;=\; \mathbb{E}_{q_\phi(z\mid x)}\big[\log p_\theta(x\mid z)\big]
\;-\; \mathrm{KL}\big(q_\phi(z\mid x)\,\|\,p(z)\big),
$$
optimized jointly over the generative parameters $\theta$ and the inference-network
parameters $\phi$. The expectation is made differentiable in $\phi$ by the
[[Reparameterization trick]]: sampling $z = \mu_\phi(x) + \sigma_\phi(x)\odot\epsilon$
with $\epsilon\sim\mathcal{N}(0,I)$ moves the randomness off the parameters so a
single sample yields a low-variance gradient
([[kingma-2013-auto-encoding-variational-bayes]]). Maximizing $\mathcal{L}$ is the
M-step/E-step coordinate ascent of [[Variational EM]] with the E-step collapsed
into the network $f_\phi$, in the negative-free-energy view of
[[neal-1998-variational-em]].

**The amortization gap and how to close it.** Let
$\mathcal{L}^\star(x) = \max_{\lambda}\, \mathcal{L}\big(x;\,\lambda\big)$ be the
ELBO under free per-datapoint variational parameters $\lambda$, and
$\mathcal{L}^{\mathrm{amort}}(x) = \mathcal{L}\big(x;\, f_\phi(x)\big)$ the ELBO
under the amortized prediction. The amortization gap
$\mathcal{L}^\star(x) - \mathcal{L}^{\mathrm{amort}}(x) \ge 0$ is the inference
suboptimality attributable to sharing one network across all data. Two families
of remedies are relevant here:

- **Iterative amortized inference** ([[marino-2018-iterative-amortized-inference]]):
  instead of emitting a belief in one shot, the network *learns an optimizer* that
  repeatedly encodes the current free-energy gradient and updates the belief, so
  inference becomes a short learned-gradient loop. This narrows the gap toward the
  per-datapoint optimum while keeping the speed of amortization. The VFE
  transformer's `filtering` E-step is precisely such an iterated, gradient-driven
  refinement of the amortized belief.

- **Local prediction-error refinement** ([[millidge-2020-pc-approximates-backprop]]):
  predictive-coding free-energy minimization with purely local error updates
  converges to exact backprop gradients, so an amortized prediction followed by
  local relaxation recovers the same optimization signal as end-to-end training —
  unifying the feedforward (amortized) and recurrent (refinement) views.

**Why amortization is natural for Gaussian beliefs.** When $q$ is a diagonal
Gaussian, the network need only output $\mu$ and $\log\sigma^2$, and the KL term
against a Gaussian prior is closed-form, exactly the Gaussian free-energy
derivation laid out step-by-step in [[bogacz-2017-free-energy-tutorial]]. The
[[Precision weighting]] that appears in those updates — errors scaled by inverse
covariance — is what the recognition network must learn to emit.

> [!note] Editorial: In the full model the belief covariance $\Sigma_t$ is a
> first-class SPD object, so the "parameters" the inference machinery predicts and
> refines live on a curved manifold rather than in a flat $(\mu,\log\sigma^2)$
> space; amortization there means predicting a point on the SPD cone, and
> refinement means a Riemannian update of it. This couples amortized inference to
> the project's SPD geometry rather than leaving it in the plain VAE setting.

## In this work

Amortized inference surfaces wherever the VFE transformer turns context into
beliefs without an explicit per-token optimization:

- **Belief prediction.** The forward pass acts as the amortized recognition
  network, predicting each token's Gaussian belief $(\mu_t,\Sigma_t)$ from
  context — the sequence-scale analogue of the VAE encoder of
  [[kingma-2013-auto-encoding-variational-bayes]].
- **Filtering E-step.** `gradient_mode: "filtering"` refines the predicted
  beliefs by iterating free-energy/prediction-error gradients, the
  iterative-amortized scheme of [[marino-2018-iterative-amortized-inference]] that
  closes the amortization gap, consistent with the local-update equivalence of
  [[millidge-2020-pc-approximates-backprop]].
- **ELBO / free-energy objective.** The amortized inference parameters are trained
  jointly with the generative parameters under the [[Variational free energy]]
  objective, the coordinate-ascent / negative-free-energy picture of
  [[neal-1998-variational-em]] and the free-energy principle of
  [[friston-2010-free-energy-principle]].
- **Precision-weighted attention.** Attention reweights token interactions by
  belief precision, so the amortized network is in effect predicting the
  precisions that drive [[rao-1999-predictive-coding]]-style error dynamics.

## Sources

- [[kingma-2013-auto-encoding-variational-bayes]] — origin of the amortized
  recognition network and the reparameterization trick.
- [[marino-2018-iterative-amortized-inference]] — iterative amortization that
  closes the amortization gap by learning an optimizer.
- [[millidge-2020-pc-approximates-backprop]] — local prediction-error refinement
  recovers exact gradients, unifying amortized prediction with backprop.
- [[neal-1998-variational-em]] — EM as coordinate ascent on a free-energy/ELBO
  functional, the frame in which the E-step is amortized.
- [[bogacz-2017-free-energy-tutorial]] — explicit Gaussian free-energy and
  precision-weighted updates the recognition network must emit.
- [[friston-2010-free-energy-principle]] — free-energy minimization as the
  governing objective for the predicted beliefs.
- [[rao-1999-predictive-coding]] — feedforward prediction / feedback error
  dynamics that the predict-then-refine scheme mirrors.
- [[bishop-2006-pattern-recognition-machine-learning]] — Ch.10 variational
  inference, the ELBO, and mean-field EM that the VFE transformer instantiates
  per token.
- [[beal-2003-variational-algorithms-approximate-bayesian-inference]] —
  variational Bayesian EM and the free-energy bound, a direct antecedent of the
  iterative VFE minimization.

## See also

- [[Variational free energy]]
- [[Evidence lower bound (ELBO)]]
- [[Reparameterization trick]]
- [[Precision weighting]]
- [[Prediction error]]
- [[Variational autoencoder (VAE)]]
- [[Variational EM]]
- [[Iterative amortized inference]]
- [[Predictive coding network]]
- [[Free-energy principle active inference]]
