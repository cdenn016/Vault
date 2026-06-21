---
type: concept
title: "Evidence lower bound (ELBO)"
aliases:
  - ELBO
  - Variational lower bound
  - Evidence lower bound
  - Negative variational free energy
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Evidence lower bound (ELBO)

## Definition

The **evidence lower bound (ELBO)** is the central objective of variational
inference: a tractable lower bound on the log marginal likelihood (the
"evidence") of a probabilistic model. Given observed data $x$, latent
variables $z$, a generative model $p_\theta(x, z)$, and an approximate
posterior (or *belief*) $q_\phi(z)$, the log evidence decomposes exactly as

$$
\log p_\theta(x) \;=\; \underbrace{\mathbb{E}_{q_\phi(z)}\!\big[\log p_\theta(x,z) - \log q_\phi(z)\big]}_{\text{ELBO}\;\;\mathcal{L}(\theta,\phi)} \;+\; \mathrm{KL}\!\big(q_\phi(z)\,\|\,p_\theta(z\mid x)\big).
$$

Because the Kullback-Leibler (KL) divergence is non-negative, the first term
$\mathcal{L}(\theta,\phi)$ is always a lower bound on $\log p_\theta(x)$ —
hence "evidence lower bound." The gap between the bound and the true evidence
is exactly the KL divergence from the belief $q$ to the true posterior, so
**maximizing the ELBO simultaneously fits the model to the data and drives the
approximate posterior toward the true one.** A common equivalent rewriting
separates a reconstruction term from a prior-matching term,

$$
\mathcal{L}(\theta,\phi) \;=\; \mathbb{E}_{q_\phi(z)}\big[\log p_\theta(x\mid z)\big] \;-\; \mathrm{KL}\!\big(q_\phi(z)\,\|\,p_\theta(z)\big),
$$

which exposes the ELBO as accuracy (expected log-likelihood) regularized by
complexity (divergence of the belief from the prior).

The ELBO is the exact negative of the **[[Variational free energy]]**:
$\mathcal{F} = -\mathcal{L}$. Minimizing free energy and maximizing the ELBO
are one and the same operation, viewed from opposite signs.

## Why it matters here

The VFE transformer is, at its core, a model trained to maximize an ELBO over
per-token Gaussian beliefs. Each token carries a diagonal-Gaussian belief
$q = \mathcal{N}(\mu, \Sigma)$ over its latent state, and the training
objective is the (negative) free energy of these beliefs — an ELBO whose
reconstruction term measures how well predictions explain the sequence and
whose complexity term keeps beliefs near their priors. This single functional
is what the architecture's alternating inference loop ascends: it is the
glue connecting the E-step (belief updates) and M-step (parameter updates)
into one coherent variational-EM procedure, as formalized by
[[neal-1998-variational-em]], who showed both steps to be coordinate ascent
on the *same* negative-free-energy / ELBO objective. Reading the bound through
the [[Free-energy principle active inference]] lens of
[[friston-2010-free-energy-principle]], the ELBO is an upper bound on surprise
that perception, attention, and learning all act to tighten.

The ELBO therefore furnishes the precise meaning of "training loss" in this
program: it is not an ad hoc penalty but the quantity whose maximization is
provably equivalent to approximate Bayesian inference over the token beliefs.

## Details

**Tightness and the inference gap.** The ELBO equals the log evidence exactly
when $q_\phi(z) = p_\theta(z\mid x)$, i.e. when the belief matches the true
posterior. In practice $q$ is restricted to a tractable family — here the
diagonal-Gaussian family — so a residual gap remains. Refining $q$ within its
family to shrink this gap is precisely the **E-step**; this is the operation
[[Iterative amortized inference]] of
[[marino-2018-iterative-amortized-inference]] learns to perform by repeatedly
encoding free-energy gradients, narrowing the *amortization gap* that a
single-pass encoder leaves open.

**Gaussian beliefs and precision weighting.** For Gaussian generative models
and Gaussian beliefs, the ELBO reduces to a sum of squared
**[[Prediction error]]** terms weighted by precisions (inverse variances), as
[[bogacz-2017-free-energy-tutorial]] derives step by step. The resulting
**[[Precision weighting]]** gives the E-step its characteristic
precision-weighted error-correction form and connects directly to the
predictive-coding circuitry of [[rao-1999-predictive-coding]], where
feedforward signals carry precision-weighted prediction errors and feedback
carries predictions.

**Estimating and differentiating the bound.** When the expectation under $q$
has no closed form, the ELBO is optimized by Monte Carlo gradients. The
**[[Reparameterization trick]]** of
[[kingma-2013-auto-encoding-variational-bayes]] expresses a Gaussian sample as
$z = \mu + \Sigma^{1/2}\epsilon$ with $\epsilon \sim \mathcal{N}(0, I)$,
turning ELBO maximization into ordinary backpropagation through the belief
parameters — the blueprint for gradient-based optimization of per-token
diagonal-Gaussian beliefs and the defining recipe of the
**[[Variational autoencoder (VAE)]]**.

**Local errors recover global gradients.** Maximizing the ELBO by local
prediction-error minimization is not a weaker form of learning:
[[millidge-2020-pc-approximates-backprop]] proves that predictive-coding
free-energy minimization with purely local updates converges to exact
backpropagation gradients on arbitrary computation graphs, unifying the
E-step/M-step loop with end-to-end gradient training.

**Generalized bounds (Renyi / alpha family).** The standard ELBO uses KL
divergence, but it is the $\alpha\to 1$ member of a one-parameter family. The
variational **[[Renyi divergence]]** bound of [[li-turner-2016-renyi-vi]]
replaces KL with the order-$\alpha$ Renyi divergence, smoothly interpolating
between the ELBO ($\alpha\to 1$) and the exact log marginal likelihood
($\alpha\to 0$), and tuning mass-covering versus mode-seeking behavior via
$\alpha$. [[vanerven-2014-renyi-kl]] establishes that KL is exactly the
$\alpha\to 1$ limit of the Renyi family (see **[[Alpha-divergence]]**),
licensing the model's "renyi" divergence family with the classical ELBO as a
special case. The dual affine connections and alpha-connections underlying
this family are the subject of [[amari-2000-methods-information-geometry]].

**Geometry of the ascent.** Maximizing the ELBO over a statistical manifold is
most efficiently done along the **[[Natural gradient]]** direction — the
ordinary gradient preconditioned by the inverse **[[Fisher information metric]]** — which [[amari-1998-natural-gradient]] shows to be the
reparameterization-invariant steepest-descent direction. This is the
information-geometric machinery the M-step uses to update parameters and the
belief updates use to move efficiently.

## In this work

The ELBO surfaces wherever the config speaks of free energy, beliefs, and the
training objective:

- **Training objective.** The architecture's ELBO / free-energy loss is the
  negative variational free energy of the per-token Gaussian beliefs; this is
  the quantity the whole model maximizes (see **[[Variational free energy]]**).
- **`gradient_mode: "filtering"` and the E-step.** The filtering belief
  updates are the ELBO's E-step — incremental, partial belief refinements that
  [[neal-1998-variational-em]] justifies as valid coordinate ascent on the
  bound and that [[bogacz-2017-free-energy-tutorial]] renders as
  precision-weighted relaxation.
- **`family: gaussian_diagonal`.** The diagonal-Gaussian belief family fixes
  the variational class over which the bound is optimized; the
  reparameterization trick of
  [[kingma-2013-auto-encoding-variational-bayes]] makes it differentiable.
- **`divergence_family: "renyi"`.** The complexity term of the ELBO is
  generalized from KL to the Renyi/alpha family of
  [[li-turner-2016-renyi-vi]] and [[vanerven-2014-renyi-kl]], with KL recovered
  as the $\alpha\to 1$ limit.
- **Precision-weighted attention.** The squared-error, precision-weighted form
  the Gaussian ELBO takes is exactly what makes
  **[[Precision weighting]]** and the model's attention dynamics inference,
  not heuristic — grounded in [[rao-1999-predictive-coding]] and
  [[friston-2010-free-energy-principle]].

> [!note] Editorial: The config exposes the ELBO only implicitly, through the
> free-energy objective, the belief family, and the divergence family; the
> precise decomposition above is the standard reading that makes those knobs
> coherent, not a verbatim field in the run configuration.

## Sources

- [[neal-1998-variational-em]] — EM as coordinate ascent on one negative-free-energy / ELBO functional.
- [[friston-2010-free-energy-principle]] — Free energy as the negative ELBO / upper bound on surprise.
- [[kingma-2013-auto-encoding-variational-bayes]] — The ELBO trained end-to-end via the reparameterization trick.
- [[bogacz-2017-free-energy-tutorial]] — Gaussian-belief derivation yielding precision-weighted ELBO updates.
- [[rao-1999-predictive-coding]] — Predictive-coding ancestor of precision-weighted error dynamics.
- [[marino-2018-iterative-amortized-inference]] — Closing the inference/amortization gap in the ELBO's E-step.
- [[millidge-2020-pc-approximates-backprop]] — Local ELBO minimization recovers exact backprop gradients.
- [[li-turner-2016-renyi-vi]] — The variational Renyi bound generalizing the ELBO.
- [[vanerven-2014-renyi-kl]] — KL as the $\alpha\to 1$ limit of the Renyi family.
- [[amari-1998-natural-gradient]] — Natural-gradient ascent on the bound.
- [[amari-2000-methods-information-geometry]] — Dual / alpha-connection geometry behind the divergence family.
- [[bishop-2006-pattern-recognition-machine-learning]] — Ch.10 variational inference / ELBO / mean-field EM the VFE transformer instantiates per token.
- [[wainwright-2008-graphical-models-variational|wainwright-jordan-2008-graphical-models-variational-inference]] — Exponential-family convex-duality foundation of mean-field variational inference / free energy.
- [[beal-2003-variational-bayesian|beal-2003-variational-algorithms-approximate-bayesian-inference]] — Variational Bayesian EM and the free-energy bound — direct antecedent of iterative VFE minimization.

## See also

- [[Variational free energy]]
- [[Prediction error]]
- [[Precision weighting]]
- [[Amortized inference]]
- [[Reparameterization trick]]
- [[Renyi divergence]]
- [[Alpha-divergence]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[Variational EM]]
- [[Variational autoencoder (VAE)]]
- [[Predictive coding network]]
- [[Iterative amortized inference]]
- [[Free-energy principle active inference]]
