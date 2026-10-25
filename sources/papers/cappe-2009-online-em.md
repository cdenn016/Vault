---
type: paper
title: "Online EM Algorithm for Latent Data Models"
aliases:
  - "Cappé 2009"
  - "Cappe and Moulines 2009"
  - "Online EM"
  - "Stepwise EM"
authors:
  - "Cappé, Olivier"
  - "Moulines, Eric"
year: 2009
url: https://doi.org/10.1111/j.1467-9868.2009.00698.x
pdf: sources/pdfs/cappe-2009-online-em.pdf
tags:
  - cluster/vfe
  - project/transformer
  - field/statistics
  - field/cs-ml
created: 2026-10-25
---

# Online EM Algorithm for Latent Data Models

> [!info] Citation
> Cappé, O., & Moulines, E. (2009). *Online EM algorithm for latent data models*. Journal of the Royal Statistical Society B, 71(3), 593–613. arXiv:0712.4273. The local PDF is arXiv v4.

## TL;DR
An online EM for exponential-family complete-data models: a stochastic-approximation E-step updates running expected sufficient statistics, $\hat s_{k+1}=\hat s_k+\gamma_{k+1}(\bar s(Y_{k+1};\hat\theta_k)-\hat s_k)$, and the M-step is the usual batch maximization at $\hat s$. It converges to stationary points of the KL divergence between the data law and the model, also when the model is misspecified, and with Polyak–Ruppert averaging it attains the rate of the maximum-likelihood estimator.

## Method
The step sizes satisfy the standard stochastic-approximation conditions, for instance $\gamma_k=\gamma_0k^{-\alpha}$ with $\alpha\in(1/2,1]$; the paper recommends a slowly decreasing step (about $n^{-0.5+\epsilon}$) with averaging. No complete-data information matrix is needed. In online mode the step size $1/k$ recovers the incremental EM of Neal and Hinton.

## Relevance to this research
This is the averaging rule of the local arm in [[vfe3-2026-10-25-local-learner-test]]: running posterior statistics with $\gamma_k=\max((k+1)^{-0.6},0.2)$, a floored version of the paper's schedule, followed by closed-form M-steps. The floor departs from the theorem's decreasing-step condition and was chosen on synthetic data. The misspecified-model result matters here because a linear-Gaussian byte model is far from the data law.

## Cross-links
- Themes: [[Inference machinery — variational EM and filtering]]
- Methods: [[Variational EM]]
- Related sources: [[neal-1998-variational-em]], [[dempster-1977-em-algorithm]], [[vfe3-2026-10-25-local-learner-test]]

## BibTeX
```bibtex
@article{cappe2009online,
  author  = {Capp{\'e}, Olivier and Moulines, Eric},
  title   = {Online Expectation-Maximization Algorithm for Latent Data Models},
  journal = {Journal of the Royal Statistical Society: Series B},
  volume  = {71},
  number  = {3},
  pages   = {593--613},
  year    = {2009},
  doi     = {10.1111/j.1467-9868.2009.00698.x},
  eprint  = {0712.4273}
}
```
