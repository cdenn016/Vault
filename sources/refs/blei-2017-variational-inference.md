---
type: reference
title: "Variational Inference: A Review for Statisticians"
aliases:
  - "Blei et al. 2017"
  - "Blei (2017) Variational Inference Review"
authors:
  - David M. Blei
  - Alp Kucukelbir
  - Jon D. McAuliffe
year: 2017
tags:
  - cluster/vfe
  - project/multi-agent
  - project/transformer
  - field/statistics
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# Variational Inference: A Review for Statisticians

> [!info] Citation
> Blei, D. M., Kucukelbir, A., & McAuliffe, J. D. (2017). "Variational Inference: A Review for Statisticians." *Journal of the American Statistical Association* **112**(518), 859–877. DOI: [10.1080/01621459.2017.1285773](https://doi.org/10.1080/01621459.2017.1285773). Preprint: [arXiv:1601.00670](https://arxiv.org/abs/1601.00670).

## TL;DR

The canonical modern survey of **variational inference (VI)**: approximating an intractable posterior $p(z\mid x)$ by the member $q^\star$ of a tractable family $\mathcal{Q}$ closest in KL divergence, recast as maximizing the **evidence lower bound (ELBO)** rather than minimizing KL directly. It covers the mean-field family, coordinate-ascent VI (CAVI), stochastic VI for large data, and the bias-versus-speed trade-off relative to MCMC. It is the standard reference establishing VI as a principled, scalable alternative to sampling.

## What it establishes

The review derives the central identity $\log p(x) = \mathrm{ELBO}(q) + \mathrm{KL}(q \| p(\cdot\mid x))$, so maximizing the ELBO simultaneously tightens a lower bound on the log-evidence and drives $q$ toward the true posterior. It develops the mean-field factorization $q(z) = \prod_j q_j(z_j)$, the coordinate-ascent updates that follow, and stochastic/black-box extensions that scale VI to massive datasets. It also discusses VI's characteristic underestimation of posterior variance and frames the practical choice between VI (fast, biased) and MCMC (asymptotically exact, slow).

## Why the project cites it

[[participatory-it-from-bit]] cites this (`blei2017variational`, alongside `Friston2010`) for the **standard correspondence between additive KL contributions and product priors** — the identity that lets the manuscript read its additive discounted-KL hyperprior $\sum_k \lambda_k \mathrm{KL}(q_i \| p_k)$ as a log-linear / product-of-experts prior. More foundationally, this review is the ELBO machinery underpinning the entire project: the VFE objective the model minimizes *is* the negative ELBO, the E-step is coordinate-ascent VI over per-token Gaussian beliefs, and the mean-field structure is what makes the multi-agent factorization tractable. It is the methodological backbone behind [[Variational free energy]] and [[Multi-agent variational free energy]], and the statistics-side companion to the free-energy-principle reading of the same objective in [[friston-2010-free-energy-principle]].

```bibtex
@article{blei2017variational,
  author  = {Blei, David M. and Kucukelbir, Alp and McAuliffe, Jon D.},
  title   = {Variational Inference: A Review for Statisticians},
  journal = {Journal of the American Statistical Association},
  volume  = {112},
  number  = {518},
  pages   = {859--877},
  year    = {2017},
  doi     = {10.1080/01621459.2017.1285773},
  eprint  = {1601.00670},
  archivePrefix = {arXiv},
  primaryClass  = {stat.CO}
}
```
