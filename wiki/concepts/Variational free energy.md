---
type: concept
title: Variational free energy
aliases:
  - VFE
  - Free energy
  - Negative ELBO
  - Variational free-energy functional
  - "VFE Functional"
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-07-10
---

# Variational free energy

## Definition

The **variational free energy** is a scalar functional that upper-bounds the negative log-evidence (the "surprise") of a probabilistic model and is minimized to perform approximate Bayesian inference. Given observed data \(x\), latent variables \(z\), a generative model \(p_\theta(x, z)\), and an approximate posterior (a *belief*) \(q_\phi(z)\), the variational free energy is

\[
\mathcal{F}[q, \theta] = \mathbb{E}_{q_\phi(z)}\big[\log q_\phi(z) - \log p_\theta(x, z)\big]
= \underbrace{D_{\mathrm{KL}}\big(q_\phi(z)\Vert p_\theta(z\mid x)\big)}_{\geq 0} - \log p_\theta(x).
\]

Because the Kullback-Leibler term is non-negative, \(\mathcal{F} \geq -\log p_\theta(x)\): free energy is an upper bound on surprise, and equivalently \(-\mathcal{F}\) is a lower bound on the log evidence. That lower bound is the [[Evidence lower bound (ELBO)]], so variational free energy is exactly the **negative ELBO**. Minimizing \(\mathcal{F}\) jointly tightens the bound (driving \(q\) toward the true posterior in the E-direction) and raises the model evidence (improving \(\theta\) in the M-direction). The functional admits a second, equally important decomposition into an *accuracy* term and a *complexity* term,

\[
\mathcal{F}[q,\theta] = \underbrace{-\mathbb{E}_{q}\big[\log p_\theta(x \mid z)\big]}_{\text{negative expected accuracy}} + \underbrace{D_{\mathrm{KL}}\big(q_\phi(z)\Vert p_\theta(z)\big)}_{\text{complexity}},
\]

which makes explicit that good beliefs explain the data well while staying close to the prior.

## Why it matters here

The deployed transformer uses structural EM, not one shared VFE/ELBO. Its target-blind Gaussian belief E-step descends alignment and self-coupling terms, while the decode M-step minimizes cross-entropy. The one-step belief update is a filter, not an argmin or coordinate-ascent update, and no monotone-evidence guarantee follows. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Editorial (2026-07-10): The config's `divergence_family: "renyi"`
> selects an order-Rényi pairwise belief discrepancy. Its order-one limit is KL,
> but the configured term is not the Li–Turner variational Rényi bound and does
> not make the separate belief and decode objectives one free-energy functional.
> [[gl-k-attention-2026-07-09-review-revision]]

## Details

**The Gaussian instance.** When both prior and belief are Gaussian, free energy becomes a sum of precision-weighted squared [[Prediction error]] terms plus log-determinant (complexity) terms. For a hierarchical predictive-coding model with prediction \(g(\mu)\) and precision \(\Pi = \Sigma^{-1}\), the leading contribution is \(\tfrac{1}{2}\varepsilon^\top \Pi \varepsilon\) with \(\varepsilon = x - g(\mu)\). Setting \(\partial \mathcal{F}/\partial \mu = 0\) yields the E-step belief-relaxation dynamics, and \(\partial \mathcal{F}/\partial \Pi = 0\) yields the M-step precision-learning rule; [[bogacz-2017-free-energy-tutorial]] derives both explicitly, and [[rao-1999-predictive-coding]] gives the cortical reading in which feedback carries predictions and feedforward carries precision-weighted errors.

**Textbook coordinate ascent / EM.** Neal and Hinton's result applies when both steps improve one functional. It is valid background but does not license the transformer's deployed two-objective structural-EM filter. [[gl-k-attention-2026-07-09-review-revision]]

**Amortization comparisons.** VAEs use a recognition network and a shared ELBO,
while iterative amortized inference learns an optimizer that refines encoded
beliefs. The pure transformer contains neither component; it stores beliefs
explicitly and applies a target-blind finite filter. Likewise, the converged
predictive-coding schedule of [[millidge-2020-pc-approximates-backprop]] does not
identify that filter with the gradient of the separate decode objective.

**Variants.** The variational Rényi bound of [[li-turner-2016-renyi-vi]] and the order-Rényi divergence surveyed by [[vanerven-2014-renyi-kl]] are related but distinct constructions. The configured pairwise belief divergence uses the latter family and recovers KL at order one; it is not automatically the Li–Turner bound. Gaussian belief updates retain their [[Natural gradient]] / [[Fisher information metric]] geometry, while frame and decode updates are separate. [[gl-k-attention-2026-07-09-review-revision]]

## In this work

Variational free energy surfaces throughout the model and config:

- **Structural objectives.** The belief step and cross-entropy parameter step descend distinct objectives. [[gl-k-attention-2026-07-09-review-revision]]
- **Filtering gradient mode.** The belief update is one natural-gradient filtering step on its target-blind objective, not a one-shot minimizer. [[gl-k-attention-2026-07-09-review-revision]]
- **Precision-weighted attention.** The attention mechanism weights interactions by belief precisions \(\Sigma^{-1}\), the attention analogue of the precision-weighted prediction errors that appear when \(\mathcal{F}\) is Gaussian.
- **Rényi belief divergence.** `divergence_family: "renyi"` selects an order-Rényi pairwise divergence with KL as its order-one limit. It does not by itself realize the variational Rényi bound or merge the decode cross-entropy into the belief objective. [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[neal-1998-variational-em]] — EM as coordinate ascent on one negative-free-energy functional; incremental or partial updates retain its guarantee only when both coordinates optimize that functional.
- [[friston-2010-free-energy-principle]] — Free energy as an upper bound on surprise unifying perception, attention, and learning.
- [[rao-1999-predictive-coding]] — Hierarchical predictive coding; precision-weighted prediction-error dynamics.
- [[kingma-2013-auto-encoding-variational-bayes]] — VAE; ELBO optimized end-to-end via the reparameterization trick.
- [[bogacz-2017-free-energy-tutorial]] — Explicit Gaussian free-energy E-step/M-step derivation.
- [[marino-2018-iterative-amortized-inference]] — Iterative amortized inference closing the amortization gap.
- [[millidge-2020-pc-approximates-backprop]] — Local free-energy minimization approximating backprop.
- [[li-turner-2016-renyi-vi]] — Variational Renyi bound interpolating ELBO and log evidence.
- [[vanerven-2014-renyi-kl]] — Renyi divergence family with KL as the \(\alpha \to 1\) limit.
- [[amari-1998-natural-gradient]] — Fisher-preconditioned natural gradient for efficient minimization on the statistical manifold.
- [[khan-rue-2023-bayesian-learning-rule]] — Natural-gradient descent on exponential-family natural parameters as a single learning rule unifying Adam, Newton, VI, and online learning; the Fisher-preconditioned Gaussian belief update.
- [[bishop-2006-pattern-recognition-machine-learning]] — Ch. 10 ELBO and mean-field EM as belief-side comparison material.
- [[wainwright-2008-graphical-models-variational|wainwright-jordan-2008-graphical-models-variational-inference]] — Exponential-family convex-duality foundation of mean-field variational inference and the free-energy bound.
- [[beal-2003-variational-bayesian|beal-2003-variational-algorithms-approximate-bayesian-inference]] — Variational Bayesian EM and the free-energy bound; direct antecedent of iterative VFE minimization.

## See also

- [[Evidence lower bound (ELBO)]]
- [[Prediction error]]
- [[Precision weighting]]
- [[Amortized inference]]
- [[Reparameterization trick]]
- [[Variational EM]]
- [[Variational autoencoder (VAE)]]
- [[Predictive coding network]]
- [[Iterative amortized inference]]
- [[Free-energy principle active inference]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[Renyi divergence]]
- [[Alpha-divergence]]
- [[Variational free energy and predictive coding]]
- [[Inference machinery — variational EM and filtering]]
- [[VFE Transformer Program]]

## Related sources (ingested 2026-06-20)

- [[friston-2016-active-inference-learning]] — Active-inference treatment of learning as free-energy minimization over time;
