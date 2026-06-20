---
type: reference
title: "Pattern Recognition and Machine Learning"
aliases:
  - "Bishop 2006 — Pattern Recognition and Machine Learning"
  - "PRML"
authors:
  - "Bishop C. M."
year: 2006
url: https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-06-20
updated: 2026-06-20
---

# Pattern Recognition and Machine Learning

> [!info] Citation
> Christopher M. Bishop (2006). *Pattern Recognition and Machine Learning.* Information Science and Statistics. Springer, New York. ISBN 978-0-387-31073-2.

## TL;DR

Bishop's textbook is the standard graduate reference for Bayesian pattern recognition. For this project the load-bearing chapter is Chapter 10, *Approximate Inference*, which develops variational inference from first principles: the decomposition of the log marginal likelihood into the [[Evidence lower bound (ELBO)]] plus a Kullback-Leibler gap, the mean-field (factorized-$q$) approximation and its coordinate-ascent update, variational EM, and worked Gaussian and mixture examples. Chapters 8-9 supply the surrounding machinery — graphical models, message passing, latent-variable models, and the EM algorithm — that frames variational inference as approximate Bayesian computation on a model with hidden variables.

## What it establishes

The variational identity that the project rests on is Bishop's eq. (10.2)-(10.4). For observed data $X$ and latent variables $Z$, any distribution $q(Z)$ decomposes the log evidence as

$$ \log p(X) = \mathcal{L}(q) + \mathrm{KL}\!\big(q \,\|\, p(Z\mid X)\big), $$

where the **evidence lower bound** is

$$ \mathcal{L}(q) = \int q(Z)\,\log\frac{p(X,Z)}{q(Z)}\,\mathrm{d}Z = \mathbb{E}_q[\log p(X,Z)] + \mathrm{H}[q]. $$

Because $\mathrm{KL} \ge 0$, $\mathcal{L}(q)$ is a lower bound on $\log p(X)$, tight exactly when $q$ equals the true posterior. The negative of $\mathcal{L}(q)$ is the **variational free energy**; maximizing the bound and minimizing the free energy are the same operation, and the gap to be closed is the KL from the variational $q$ to the exact posterior.

Restricting $q$ to a factorized form $q(Z) = \prod_i q_i(Z_i)$ (the **mean-field** family) and maximizing $\mathcal{L}$ with respect to one factor at a time gives Bishop's coordinate-ascent update (eq. 10.9),

$$ \log q_j^\star(Z_j) = \mathbb{E}_{i \ne j}\!\big[\log p(X,Z)\big] + \text{const}, $$

so each factor is the exponentiated expected complete-data log-joint under the other factors — a closed-form update for conjugate-exponential models that is iterated to convergence. Chapter 10 then works this through for the univariate Gaussian, Bayesian linear regression, and the variational Gaussian mixture, and casts the result as a **variational EM** scheme in which an approximate E-step over $q$ alternates with an M-step over model parameters.

> [!note] Editorial: equation labels (10.2)-(10.4) and (10.9) and the chapter/section structure follow the published first edition (Springer, 2006); this note summarizes that edition's variational-inference development rather than reproducing its full derivations.

## Why the project cites it

This reference is the textbook statement of the variational machinery the VFE transformer instantiates per token, and it is the common entry point the variational and information-geometry audit lenses appeal to when checking the model's objective against standard practice.

- **Free energy as the objective.** The model's training objective is a [[Variational free energy]] over per-token Gaussian belief tuples $(\mu, \Sigma, \phi)$; Bishop's $\log p(X) = \mathcal{L}(q) + \mathrm{KL}$ identity is the canonical justification that minimizing this free energy tightens a bound on the evidence. The $\mathrm{KL}(q_i \| p_i)$ self-coupling term in the project's free-energy functional is exactly the belief-to-prior gap this chapter formalizes.
- **Mean-field and the per-token belief.** The factorized $q$ of the mean-field approximation is the textbook precedent for the model's structured, per-token belief: each token carries its own approximate posterior, refined by coordinate-ascent-style updates rather than a single global posterior solve. Bishop's coordinate-ascent license is the same one [[neal-1998-variational-em]] sharpens into partial / incremental E-steps.
- **Variational EM and the two timescales.** The E-step (update beliefs / $q$) versus M-step (update parameters) split that organizes the model's optimization is Bishop's variational-EM scheme; the [[Evidence lower bound (ELBO)]] is the shared quantity both steps ascend.
- **Amortization and precision.** Where Bishop optimizes $q$ directly, the transformer amortizes the belief update across tokens (see [[Amortized inference]]), and the Gaussian-posterior precisions that weight prediction errors in the model are the variational analogue of Bishop's precision-parameterized Gaussian updates (see [[Precision weighting]]).

This grounds the project's [[Variational free energy and predictive coding]] theme. See the companion variational sources [[neal-1998-variational-em]], [[dempster-1977-em]], [[blei-2017-variational-inference]], and the amortized / deep-latent extension [[kingma-2013-auto-encoding-variational-bayes]].

Project hubs: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model]].

## BibTeX

```bibtex
@book{bishop2006pattern,
  author    = {Bishop, Christopher M.},
  title     = {Pattern Recognition and Machine Learning},
  series    = {Information Science and Statistics},
  publisher = {Springer},
  address   = {New York},
  year      = {2006},
  isbn      = {978-0-387-31073-2}
}
```
