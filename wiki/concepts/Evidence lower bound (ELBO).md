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
updated: 2026-07-10
---

# Evidence lower bound (ELBO)

## Definition

The **evidence lower bound (ELBO)** is the central objective of variational
inference: a tractable lower bound on the log marginal likelihood (the
"evidence") of a probabilistic model. Given observed data $x$, latent
variables $z$, a generative model $p_\theta(x, z)$, and an approximate
posterior (or *belief*) $q_\phi(z)$, the log evidence decomposes exactly as

$$
\log p_\theta(x) = \underbrace{\mathbb{E}_{q_\phi(z)}\big[\log p_\theta(x,z) - \log q_\phi(z)\big]}_{\mathcal{L}(\theta,\phi)\text{ (ELBO)}} + \mathrm{KL}\big(q_\phi(z)\|p_\theta(z\mid x)\big).
$$

Because the Kullback-Leibler (KL) divergence is non-negative, the first term
$\mathcal{L}(\theta,\phi)$ is always a lower bound on $\log p_\theta(x)$ —
hence "evidence lower bound." The gap between the bound and the true evidence
is exactly the KL divergence from the belief $q$ to the true posterior, so
**maximizing the ELBO simultaneously fits the model to the data and drives the
approximate posterior toward the true one.** A common equivalent rewriting
separates a reconstruction term from a prior-matching term,

$$
\mathcal{L}(\theta,\phi) = \mathbb{E}_{q_\phi(z)}\big[\log p_\theta(x\mid z)\big] - \mathrm{KL}\big(q_\phi(z)\|p_\theta(z)\big),
$$

which exposes the ELBO as accuracy (expected log-likelihood) regularized by
complexity (divergence of the belief from the prior).

The ELBO is the exact negative of the **[[Variational free energy]]**:
$\mathcal{F} = -\mathcal{L}$. Minimizing free energy and maximizing the ELBO
are one and the same operation, viewed from opposite signs.

## Why it matters here

The ELBO is textbook background for the belief-side variational construction,
but the deployed VFE transformer does not maximize one ELBO across its whole
alternating loop. Each token carries a diagonal-Gaussian belief
$q=\mathcal{N}(\mu,\Sigma)$. A target-blind belief objective updates those
beliefs, while a separate decode cross-entropy trains the readout and other
parameters. The one-step filter is not a CAVI argmin or Neal–Hinton incremental
EM update, so shared-functional coordinate-ascent and monotone-evidence
guarantees do not transfer to this schedule.

The ELBO therefore supplies a comparison point for the belief objective rather
than the exact meaning of the complete training loss. [[gl-k-attention-2026-07-09-review-revision]]

## Details

**Tightness and the inference gap.** In textbook ELBO optimization, the bound
equals log evidence when $q_\phi(z)=p_\theta(z\mid x)$, and restricting $q$ can
leave an inference gap. In the learned amortized model of
[[marino-2018-iterative-amortized-inference]], repeated refinement reduces an
encoder's amortization gap. These facts do not describe the deployed
target-blind filter as posterior refinement: it has no shared likelihood/ELBO
with the separate decode objective.

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

**Local errors and global gradients.** Under the converged predictive-coding
schedule analyzed by [[millidge-2020-pc-approximates-backprop]], local updates
recover exact backpropagation gradients on the source paper's computation
graphs. The deployed one-step, target-blind belief filter does not meet that
schedule, so the theorem does not identify its belief update with the gradient
of the separate decode loss.

**Generalized bounds and divergences.** [[li-turner-2016-renyi-vi]] defines a
variational Rényi bound whose endpoints include the ELBO and log marginal
likelihood. [[vanerven-2014-renyi-kl]] studies order-Rényi divergence itself,
including its order-one KL limit. [[amari-2000-methods-information-geometry]]
develops a different alpha-divergence family and its dual affine connections.
These constructions are related through power integrals but are not
interchangeable. In particular, selecting a pairwise order-Rényi discrepancy
does not instantiate the Li–Turner bound or an Amari alpha-connection.

**Geometry of the ascent.** For a genuine ELBO, the **[[Natural gradient]]**
is the reparameterization-invariant steepest direction under the
**[[Fisher information metric]]** ([[amari-1998-natural-gradient]]). In the
deployed transformer this geometry supports the Gaussian belief update. It
does not license the frame or decode M-step as a Fisher natural gradient;
the audited frame table uses plain AdamW, with the configured heavy-ball and pullback fields inactive. [[gl-k-attention-2026-07-09-review-revision]]

## In this work

The ELBO surfaces as a reference for the belief-side objective, not as one
functional optimized by the entire model:

- **Distinct objectives.** The target-blind belief objective and decode
  cross-entropy are separate; neither is the complete-model ELBO.
- **`gradient_mode: "filtering"`.** The one-step belief refinement is a
  precision-weighted filter, not an ELBO argmin or a shared-functional
  coordinate-ascent step.
- **`family: gaussian_diagonal`.** The diagonal-Gaussian belief family fixes
  the class used by the belief-side objective; reparameterization can
  differentiate sampled expectations in that objective.
- **`divergence_family: "renyi"`.** The belief-side discrepancy uses the
  order-Rényi family surveyed by [[vanerven-2014-renyi-kl]], with KL recovered
  at order one. This does not instantiate the variational bound of
  [[li-turner-2016-renyi-vi]].
- **Precision-weighted attention.** Gaussian-KL coupling contains a
  precision-weighted mismatch, which motivates the inference interpretation
  of attention. This belief-side structure does not make the complete
  two-objective loop one ELBO.

> [!note] Editorial (2026-07-10): ELBO identities on this page remain textbook
> facts. They do not turn the deployed two-objective schedule into one ELBO or
> grant its one-step filter Neal–Hinton monotonicity.
> [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[neal-1998-variational-em]] — EM as coordinate ascent on one negative-free-energy / ELBO functional.
- [[friston-2010-free-energy-principle]] — Free energy as the negative ELBO / upper bound on surprise.
- [[kingma-2013-auto-encoding-variational-bayes]] — The ELBO trained end-to-end via the reparameterization trick.
- [[bogacz-2017-free-energy-tutorial]] — Gaussian-belief derivation yielding precision-weighted ELBO updates.
- [[rao-1999-predictive-coding]] — Predictive-coding ancestor of precision-weighted error dynamics.
- [[marino-2018-iterative-amortized-inference]] — Closing the inference/amortization gap in the ELBO's E-step.
- [[millidge-2020-pc-approximates-backprop]] — Exact-backprop recovery for the source paper's converged predictive-coding schedule.
- [[li-turner-2016-renyi-vi]] — The variational Renyi bound generalizing the ELBO.
- [[vanerven-2014-renyi-kl]] — KL as the $\alpha\to 1$ limit of the Renyi family.
- [[amari-1998-natural-gradient]] — Natural-gradient ascent on the bound.
- [[amari-2000-methods-information-geometry]] — Amari alpha-divergence and dual-connection geometry, distinct from order-Rényi and variational Rényi constructions.
- [[bishop-2006-pattern-recognition-machine-learning]] — Ch. 10 textbook variational inference, ELBO, and mean-field EM used here as comparison material; the deployed filter does not instantiate that full coordinate-ascent scheme.
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
