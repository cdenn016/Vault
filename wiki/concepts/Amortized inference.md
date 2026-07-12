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
updated: 2026-07-09
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

Amortized inference is a comparison point, not the deployed transformer's inference
mechanism. The pure model has no neural recognition network that predicts posterior
parameters from context. It explicitly carries per-token Gaussian beliefs and applies
a target-blind filtering update, while the decoder is trained by separate cross-entropy.
The one-step filter therefore does not inherit a VAE amortization-gap theorem or
Neal–Hinton coordinate-ascent guarantee. [[gl-k-attention-2026-07-09-review-revision]]

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
  transformer's one-step filter is only an analogy to this refinement; it is not a
  learned optimizer and no amortization-gap result is established.

- **Local prediction-error refinement** ([[millidge-2020-pc-approximates-backprop]]):
  predictive-coding free-energy minimization with purely local error updates
  converges to exact backprop gradients under the source model's schedule and
  convergence assumptions. Those conditions do not certify the transformer's
  truncated two-objective loop.

**Why amortization is natural for Gaussian beliefs.** When $q$ is a diagonal
Gaussian, the network need only output $\mu$ and $\log\sigma^2$, and the KL term
against a Gaussian prior is closed-form, exactly the Gaussian free-energy
derivation laid out step-by-step in [[bogacz-2017-free-energy-tutorial]]. The
[[Precision weighting]] that appears in those updates — errors scaled by inverse
covariance — is what the recognition network must learn to emit.

> [!note] Editorial (2026-07-09): The live covariance family is diagonal SPD and
> the belief update has Fisher/AIRM geometry. No amortized encoder predicts that
> covariance in the pure model. [[gl-k-attention-2026-07-09-review-revision]]

## In this work

The relevant connection is limited: iterative-amortized inference motivates comparing
repeated belief refinement with an optimizer loop. The deployed pure model carries beliefs
explicitly, performs a one-step target-blind filter, and uses separate decode cross-entropy.
It neither contains an amortized recognition network nor establishes an amortization-gap
claim. [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[kingma-2013-auto-encoding-variational-bayes]] — origin of the amortized
  recognition network and the reparameterization trick.
- [[marino-2018-iterative-amortized-inference]] — iterative amortization that
  closes the amortization gap by learning an optimizer.
- [[millidge-2020-pc-approximates-backprop]] — exact-gradient recovery under the
  source model's convergence and scheduling assumptions.
- [[neal-1998-variational-em]] — EM as coordinate ascent on a free-energy/ELBO
  functional, the frame in which the E-step is amortized.
- [[bogacz-2017-free-energy-tutorial]] — explicit Gaussian free-energy and
  precision-weighted updates the recognition network must emit.
- [[friston-2010-free-energy-principle]] — free-energy minimization as the
  governing objective for the predicted beliefs.
- [[rao-1999-predictive-coding]] — feedforward prediction / feedback error
  dynamics that the predict-then-refine scheme mirrors.
- [[bishop-2006-pattern-recognition-machine-learning]] — Ch.10 variational
  inference, ELBO, and mean-field EM as comparison material.
- [[beal-2003-variational-bayesian|beal-2003-variational-algorithms-approximate-bayesian-inference]] —
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
