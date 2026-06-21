---
type: paper
title: "Auto-Encoding Variational Bayes"
aliases:
  - "Kingma 2013"
  - "VAE"
  - "kingma-2013-vae"
  - "kingma2013vae"
  - "kingma2014vae"
authors:
  - Kingma, Diederik P.
  - Welling, Max
year: 2013
arxiv: 1312.6114
url: https://arxiv.org/abs/1312.6114
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-18
updated: 2026-06-20
---

# Auto-Encoding Variational Bayes

> [!info] Citation
> Kingma, Diederik P. and Welling, Max (2013). "Auto-Encoding Variational Bayes." arXiv:1312.6114. https://arxiv.org/abs/1312.6114

## TL;DR

This paper introduces the variational autoencoder (VAE): a recipe for learning a directed latent-variable model whose posterior is intractable, by jointly training a generative model and an amortized recognition (inference) network against a single differentiable objective, the [[Evidence lower bound (ELBO)]]. Its central technical device, the [[Reparameterization trick]], rewrites a sample from a Gaussian belief as a deterministic, differentiable function of its parameters plus parameter-free noise, so that low-variance gradient estimates of the bound flow into both networks via ordinary backpropagation. This is the modern blueprint for gradient-based optimization of a Gaussian [[Variational free energy]].

## Problem & setting

Consider a probabilistic model with a continuous latent variable $z$ and observation $x$, generated as $z \sim p(z)$, $x \sim p_\theta(x\mid z)$. Learning the parameters $\theta$ by maximum likelihood requires the marginal $p_\theta(x)=\int p_\theta(x\mid z)p(z)\,dz$ and the posterior $p_\theta(z\mid x)$, both of which are intractable for any expressive (e.g. neural) likelihood. Classical variational inference sidesteps this by introducing a per-datapoint approximate posterior $q(z\mid x)$ and maximizing a lower bound on the log-evidence, but fitting a separate $q$ for every datapoint does not scale, and naive Monte-Carlo gradients of the bound with respect to the parameters of $q$ have prohibitively high variance. The paper targets exactly this regime: efficient, scalable inference and learning when both the posterior and the marginal likelihood are intractable.

## Method

The work contributes two coupled ideas.

**Amortized recognition model.** Rather than optimizing free variational parameters per datapoint, the approximate posterior is itself a neural network $q_\phi(z\mid x)$ — the encoder or recognition model — that maps each input $x$ to the parameters of its belief, here a diagonal Gaussian with mean $\mu_\phi(x)$ and (log-)variance $\sigma^2_\phi(x)$. A single shared parameter set $\phi$ then produces beliefs for all datapoints, an instance of [[Amortized inference]].

**The reparameterization trick and the ELBO.** The objective is the evidence lower bound,
$$\log p_\theta(x) \ge \mathcal{L}(\theta,\phi;x) = \mathbb{E}_{q_\phi(z\mid x)}\!\left[\log p_\theta(x\mid z)\right] - D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\,\|\,p(z)\right),$$
the negative of a [[Variational free energy]]. The first term is a reconstruction/expected-log-likelihood term; the second is a complexity penalty that pulls the belief toward the prior and, for two Gaussians, has a closed form. To differentiate the expectation through the sampling of $z$, the paper reparameterizes: a Gaussian draw is written $z = \mu_\phi(x) + \sigma_\phi(x)\odot\epsilon$ with $\epsilon\sim\mathcal{N}(0,I)$, moving all stochasticity into the parameter-free noise $\epsilon$. The bound becomes a deterministic, differentiable function of $(\theta,\phi)$ under a Monte-Carlo expectation over $\epsilon$, yielding the low-variance Stochastic Gradient Variational Bayes (SGVB) estimator. Both encoder and decoder are then trained jointly by stochastic gradient ascent on minibatches — the Auto-Encoding VB algorithm. This casts variational inference and parameter learning as one end-to-end backpropagation problem, a continuous-latent counterpart to the [[Variational EM]] alternation.

## Key results

The SGVB estimator gives unbiased, low-variance gradients and scales to large datasets and minibatch training, under only mild differentiability conditions on the model. On MNIST and Frey Face data the authors show that the learned lower bound tracks the marginal likelihood well, that amortized inference matches or beats the per-datapoint wake-sleep baseline while being far cheaper at test time (a single forward pass through the encoder yields the belief), and that sample quality and convergence improve with the size of the training set. The framework is generative-model-agnostic: any differentiable likelihood and any reparameterizable approximate posterior can be dropped in.

## Relevance to this research

The VFE-transformer's inference core is, structurally, a VAE recognition model unrolled across a sequence. Each token carries a per-token Gaussian belief $(\mu, \Sigma)$ from the `gaussian_diagonal` family — precisely the diagonal-Gaussian $q_\phi(z\mid x)$ of this paper — and the model trains against an ELBO / free-energy objective, the same bound derived here. Three concrete inheritances:

The reparameterization trick is what makes the per-token beliefs trainable by gradient descent at all; the `gradient_mode "filtering"` E-step that updates $(\mu,\Sigma)$ relies on differentiating expectations under the belief exactly as SGVB does. The amortized recognition idea — a shared network emitting beliefs for every input rather than free per-input parameters — is the design pattern the transformer follows when its layers emit token beliefs in a single forward pass; see also [[Iterative amortized inference]] for the refinement-based extension that the E-step more closely resembles. The KL-to-prior penalty in the ELBO is the seed of the model's information-geometric generalization: where the VAE uses ordinary KL, the VFE transformer swaps in a `divergence_family "renyi"` ([[Renyi divergence]] / [[Alpha-divergence]]) and a [[Natural gradient]] step, but the underlying free-energy decomposition into accuracy minus complexity is the one established here.

> [!note] Editorial: The original VAE assumes a diagonal Gaussian belief with a Euclidean parameterization; the VFE transformer instead carries a full SPD covariance on a Riemannian manifold. The reparameterization and ELBO machinery survive that generalization, but the gradient geometry does not — which is why the project layers natural-gradient and SPD-manifold tooling on top of this foundation.

## Cross-links

- Concepts: [[Evidence lower bound (ELBO)]], [[Variational free energy]], [[Reparameterization trick]], [[Amortized inference]], [[Variational autoencoder (VAE)]], [[Variational EM]], [[Iterative amortized inference]], [[Renyi divergence]], [[Natural gradient]], [[Alpha-divergence]]
- Related sources: [[neal-1998-variational-em]], [[friston-2010-free-energy-principle]], [[marino-2018-iterative-amortized-inference]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@misc{Kingma2013,
  title         = {Auto-Encoding Variational Bayes},
  author        = {Kingma, Diederik P. and Welling, Max},
  year          = {2013},
  eprint        = {1312.6114},
  archivePrefix = {arXiv},
  primaryClass  = {stat.ML},
  url           = {https://arxiv.org/abs/1312.6114}
}
```
