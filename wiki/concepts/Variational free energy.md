---
type: concept
title: Variational free energy
aliases:
  - VFE
  - Free energy
  - Negative ELBO
  - Variational free-energy functional
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Variational free energy

## Definition

The **variational free energy** is a scalar functional that upper-bounds the negative log-evidence (the "surprise") of a probabilistic model and is minimized to perform approximate Bayesian inference. Given observed data \(x\), latent variables \(z\), a generative model \(p_\theta(x, z)\), and an approximate posterior (a *belief*) \(q_\phi(z)\), the variational free energy is

\[
\mathcal{F}[q, \theta] \;=\; \mathbb{E}_{q_\phi(z)}\!\big[\log q_\phi(z) - \log p_\theta(x, z)\big]
\;=\; \underbrace{D_{\mathrm{KL}}\!\big(q_\phi(z)\,\Vert\,p_\theta(z\mid x)\big)}_{\geq 0} \;-\; \log p_\theta(x).
\]

Because the Kullback-Leibler term is non-negative, \(\mathcal{F} \geq -\log p_\theta(x)\): free energy is an upper bound on surprise, and equivalently \(-\mathcal{F}\) is a lower bound on the log evidence. That lower bound is the [[Evidence lower bound (ELBO)]], so variational free energy is exactly the **negative ELBO**. Minimizing \(\mathcal{F}\) jointly tightens the bound (driving \(q\) toward the true posterior in the E-direction) and raises the model evidence (improving \(\theta\) in the M-direction). The functional admits a second, equally important decomposition into an *accuracy* term and a *complexity* term,

\[
\mathcal{F}[q,\theta] \;=\; \underbrace{-\,\mathbb{E}_{q}\!\big[\log p_\theta(x \mid z)\big]}_{\text{negative expected accuracy}} \;+\; \underbrace{D_{\mathrm{KL}}\!\big(q_\phi(z)\,\Vert\,p_\theta(z)\big)}_{\text{complexity}},
\]

which makes explicit that good beliefs explain the data well while staying close to the prior.

## Why it matters here

Variational free energy is the organizing objective of the VFE Transformer. The model attaches to every token a Gaussian belief over a latent state — a mean \(\mu\) and covariance \(\Sigma\) in the `gaussian_diagonal` family — and trains by minimizing a free-energy / ELBO objective rather than a plain cross-entropy loss. The single functional \(\mathcal{F}\) is what ties together the architecture's otherwise disparate ingredients: the [[Variational EM]] split into an E-step that relaxes beliefs and an M-step that updates parameters is precisely coordinate descent on \(\mathcal{F}\); [[Precision weighting]] of attention is the appearance of inverse-covariance weights in the Gaussian instance of \(\mathcal{F}\); and the `filtering` gradient mode is an online, partial minimization of the same functional. In the language of the [[Free-energy principle active inference]], the network is a machine that perpetually minimizes free energy to reduce surprise about its inputs.

> [!note] Editorial: The config's `divergence_family: "renyi"` generalizes the KL term above to an [[Alpha-divergence]] / [[Renyi divergence]], so the trained objective is a Renyi free energy whose \(\alpha \to 1\) limit recovers the standard variational free energy defined here.

## Details

**The Gaussian instance.** When both prior and belief are Gaussian, free energy becomes a sum of precision-weighted squared [[Prediction error]] terms plus log-determinant (complexity) terms. For a hierarchical predictive-coding model with prediction \(g(\mu)\) and precision \(\Pi = \Sigma^{-1}\), the leading contribution is \(\tfrac{1}{2}\,\varepsilon^\top \Pi\, \varepsilon\) with \(\varepsilon = x - g(\mu)\). Setting \(\partial \mathcal{F}/\partial \mu = 0\) yields the E-step belief-relaxation dynamics, and \(\partial \mathcal{F}/\partial \Pi = 0\) yields the M-step precision-learning rule; [[bogacz-2017-free-energy-tutorial]] derives both explicitly, and [[rao-1999-predictive-coding]] gives the cortical reading in which feedback carries predictions and feedforward carries precision-weighted errors.

**Coordinate ascent / EM.** [[neal-1998-variational-em]] showed that the EM algorithm is coordinate ascent on a *single* negative-free-energy functional: the E-step maximizes over \(q\), the M-step over \(\theta\). This is what licenses *incremental* and *partial* updates — exactly the filtering-style, not-fully-converged belief updates the transformer uses, since any move that decreases \(\mathcal{F}\) is principled even if neither step is run to convergence.

**Amortization.** Rather than solving the E-step per example, the [[Variational autoencoder (VAE)]] of [[kingma-2013-auto-encoding-variational-bayes]] amortizes it with a recognition network and optimizes the ELBO end-to-end via the [[Reparameterization trick]]. Single-pass encoders leave an *amortization gap*; [[Iterative amortized inference]] ([[marino-2018-iterative-amortized-inference]]) closes it by learning an optimizer that repeatedly ingests free-energy gradients to refine the belief — the iterative refinement view that motivates the transformer's repeated belief updates. [[millidge-2020-pc-approximates-backprop]] further shows that local free-energy minimization via prediction errors can approximate exact backpropagation, unifying the E/M inference loop with gradient training.

**Variants.** Beyond the KL form, the variational Renyi bound of [[li-turner-2016-renyi-vi]] replaces KL with an \(\alpha\)-Renyi divergence, giving a one-parameter family that interpolates between the ELBO (\(\alpha \to 1\)) and the log marginal likelihood; [[vanerven-2014-renyi-kl]] is the definitive reference for that divergence family and its \(\alpha \to 1 \Rightarrow\) KL limit. Minimizing \(\mathcal{F}\) on the statistical manifold is most efficiently done with the [[Natural gradient]] preconditioned by the [[Fisher information metric]] ([[amari-1998-natural-gradient]]); [[khan-rue-2023-bayesian-learning-rule]] turns that natural gradient into a concrete learning rule, showing that natural-gradient descent on the natural parameters of an exponential-family posterior — with the update reading off the expectation-parameter gradient — unifies Adam, Newton, variational inference, and online learning, and yields exactly the closed-form Fisher-preconditioned Gaussian belief update the VFE transformer performs.

## In this work

Variational free energy surfaces throughout the model and config:

- **Training objective.** The loss is an ELBO / free-energy functional in the `gaussian_diagonal` belief family, grounded by [[friston-2010-free-energy-principle]] and [[bogacz-2017-free-energy-tutorial]].
- **E-step / M-step.** The reference block-GL($k$) configuration ([[VFE Transformer Program]]) has a belief step and parameter step that implement the E-step and M-step of [[Variational EM]] as coordinate descent on \(\mathcal{F}\), in the incremental spirit of [[neal-1998-variational-em]].
- **Filtering gradient mode.** `gradient_mode: "filtering"` performs online, partial free-energy minimization — a sequential E-step over per-token beliefs, consistent with the [[Predictive coding network]] dynamics of [[rao-1999-predictive-coding]].
- **Precision-weighted attention.** The attention mechanism weights interactions by belief precisions \(\Sigma^{-1}\), the attention analogue of the precision-weighted prediction errors that appear when \(\mathcal{F}\) is Gaussian.
- **Renyi divergence loss.** `divergence_family: "renyi"` swaps the KL complexity term for an \(\alpha\)-divergence, realizing the variational Renyi bound of [[li-turner-2016-renyi-vi]] with the standard VFE as the \(\alpha \to 1\) special case ([[vanerven-2014-renyi-kl]]).

## Sources

- [[neal-1998-variational-em]] — EM as coordinate ascent on one negative-free-energy functional; justifies incremental/partial updates.
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
- [[bishop-2006-pattern-recognition-machine-learning]] — Ch. 10 variational inference: the ELBO and mean-field EM that the VFE transformer instantiates per token.
- [[wainwright-jordan-2008-graphical-models-variational-inference]] — Exponential-family convex-duality foundation of mean-field variational inference and the free-energy bound.
- [[beal-2003-variational-algorithms-approximate-bayesian-inference]] — Variational Bayesian EM and the free-energy bound; direct antecedent of iterative VFE minimization.

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
