---
type: paper
title: Renyi Divergence Variational Inference
aliases:
  - "Li & Turner 2016 — Renyi Divergence VI"
authors:
  - Yingzhen Li
  - Richard E. Turner
year: 2016
arxiv: "1602.02311"
url: https://arxiv.org/abs/1602.02311
tags:
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-18
updated: 2026-06-18
---

# Renyi Divergence Variational Inference

> [!info] Citation
> Yingzhen Li and Richard E. Turner (2016). *Renyi Divergence Variational Inference*. Advances in Neural Information Processing Systems (NIPS) 29. arXiv:1602.02311. [arxiv.org/abs/1602.02311](https://arxiv.org/abs/1602.02311)

## TL;DR

This paper introduces the **variational Renyi bound (VR)**, a one-parameter family of objectives indexed by a divergence order $\alpha$ that generalizes the standard evidence lower bound. Replacing the Kullback-Leibler divergence in classical variational inference with a Renyi $\alpha$-divergence yields a bound that smoothly interpolates from the usual ELBO (at $\alpha \to 1$) up to the exact log marginal likelihood (at $\alpha = 0$), and beyond into mass-covering regimes for other $\alpha$. The authors make the bound tractable with the reparameterization trick, Monte Carlo sampling, and stochastic optimization, and demonstrate it on Bayesian neural networks and variational autoencoders.

## Problem & setting

Classical variational inference approximates an intractable posterior $p(z \mid x)$ by a tractable $q(z)$ chosen to maximize the [[Evidence lower bound (ELBO)]], equivalently minimizing the KL divergence $\mathrm{KL}(q \,\|\, p)$. This choice is consequential but somewhat arbitrary: KL is *mode-seeking* (zero-forcing), so $q$ tends to underestimate posterior variance and collapse onto a single mode. Other members of the divergence family — for instance the mass-covering divergences favored by expectation propagation — trade this bias for different behavior. The paper asks whether a *single* unified objective can expose this entire spectrum as a tunable knob, while remaining as easy to optimize as the ELBO.

The vehicle is the [[Renyi divergence]], a generalization of KL parameterized by an order $\alpha$, with KL recovered as the limit $\alpha \to 1$. Renyi divergences are the same object as the [[Alpha-divergence]] family up to reparameterization of the order, situating the work squarely in [[Information geometry and natural gradient|information geometry]].

## Method

The **variational Renyi bound** is defined by

$$
\mathcal{L}_\alpha(q; x) = \frac{1}{1-\alpha} \log \mathbb{E}_{q(z)}\!\left[\left(\frac{p(x, z)}{q(z)}\right)^{1-\alpha}\right].
$$

Key structural facts:

- **Interpolation.** As $\alpha \to 1$ the bound reduces exactly to the ELBO $\mathbb{E}_q[\log p(x,z) - \log q(z)]$. At $\alpha = 0$ it equals the true log marginal likelihood $\log p(x)$. For $\alpha < 1$ the bound is an upper-bound-like, mass-covering objective; for $\alpha > 1$ it is mode-seeking. A single hyperparameter thus dials between bias regimes.
- **Tractable estimation.** Because the bound is a log of an expectation, it is estimated by drawing samples from $q$ via the [[Reparameterization trick]], forming a Monte Carlo average of the importance-weight powers, and optimizing stochastically. The authors analyze the bias the Monte Carlo estimator introduces and show it can itself be exploited.
- **Negative alpha.** The framework extends to negative $\alpha$, yielding a genuinely new variational method that further widens the accessible bias-variance trade-off.
- **Unification.** Several existing methods — standard VI, the importance-weighted autoencoder bound, and others — fall out as special cases or limits of the VR family.

## Key results

- A clean theoretical statement that the VR bound interpolates monotonically from ELBO to log marginal likelihood as $\alpha$ sweeps from $1$ to $0$.
- A practical stochastic estimator (VR-max and related variants) that requires no more than the machinery of reparameterized variational inference.
- Empirical gains on **Bayesian neural networks** and **variational autoencoders**, where tuning $\alpha$ improves predictive likelihoods relative to the fixed-KL ELBO, confirming that the optimal divergence order is task-dependent rather than universally $\alpha = 1$.

## Relevance to this research

This paper is the direct theoretical ancestor of the VFE transformer's `divergence_family = "renyi"` training objective. The model's free-energy loss is not the textbook ELBO but a Renyi-generalized variational bound, and Li & Turner supply exactly the construction that makes such a loss well-posed:

- **The objective itself.** The per-token Gaussian beliefs $(\mu, \Sigma)$ in the [[Variational free energy]] formulation are fit by maximizing a variational bound. Swapping the KL term for a Renyi $\alpha$-divergence — precisely the VR bound here — turns the training criterion into a tunable interpolation between the ordinary [[Evidence lower bound (ELBO)]] (at $\alpha \to 1$) and the log marginal likelihood (at $\alpha = 0$). The `renyi` divergence family is this knob.
- **Bias control for filtering beliefs.** Because the architecture uses `gradient_mode = "filtering"` with diagonal Gaussian beliefs (`family gaussian_diagonal`), the mode-seeking pathology of pure KL is a real concern: a filtered belief that collapses variance can be overconfident. The $\alpha < 1$ mass-covering regime exposed by the VR bound is a principled lever against this, letting the belief covariance $\Sigma$ remain appropriately broad.
- **Information-geometric coherence.** Renyi / $\alpha$-divergences are the canonical dually-flat divergences of [[Information geometry and natural gradient|information geometry]]; using them as the loss aligns the training objective with the same geometry that motivates [[Natural gradient]] updates and the [[Fisher information metric]] elsewhere in the program.
- **Reparameterized estimation.** The estimator relies on the [[Reparameterization trick]], which is already the mechanism by which the transformer differentiates through its sampled Gaussian beliefs.

> [!note] Editorial: Li & Turner fix the divergence order $\alpha$ as a hyperparameter; in the VFE transformer the same $\alpha$ could in principle be made layer- or token-dependent, or annealed during the M-step, but that is an extension beyond what this paper establishes.

## Cross-links

- Generalizes: [[Evidence lower bound (ELBO)]], [[Variational free energy]]
- Divergence theory: [[Renyi divergence]], [[Alpha-divergence]], [[Fisher information metric]], [[Natural gradient]]
- Estimation: [[Reparameterization trick]], [[Variational autoencoder (VAE)]], [[Variational EM]]
- Related source: [[vanerven-2014-renyi-kl]]
- Theme: [[Information geometry and natural gradient]]
- Program: [[VFE Transformer Program]]

## BibTeX

```bibtex
@inproceedings{li2016renyi,
  title     = {R\'enyi Divergence Variational Inference},
  author    = {Li, Yingzhen and Turner, Richard E.},
  booktitle = {Advances in Neural Information Processing Systems (NIPS)},
  volume    = {29},
  year      = {2016},
  eprint    = {1602.02311},
  archivePrefix = {arXiv},
  primaryClass  = {stat.ML},
  url       = {https://arxiv.org/abs/1602.02311}
}
```
