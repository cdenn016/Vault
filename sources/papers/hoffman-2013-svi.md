---
type: paper
title: "Stochastic Variational Inference"
aliases:
  - "Hoffman 2013"
  - "SVI"
authors:
  - Hoffman, Matt
  - Blei, David M.
  - Wang, Chong
  - Paisley, John
year: 2013
arxiv: "1206.7051"
url: https://arxiv.org/abs/1206.7051
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Stochastic Variational Inference

> [!info] Citation
> Hoffman, M., Blei, D. M., Wang, C., & Paisley, J. (2013). "Stochastic Variational Inference." *Journal of Machine Learning Research* (in press). arXiv:1206.7051.

## TL;DR
Stochastic variational inference (SVI) scales mean-field variational Bayes to massive datasets by replacing the full-data coordinate ascent update for global parameters with stochastic natural-gradient steps computed on random mini-batches. The key insight is that the natural gradient of the ELBO with respect to the global variational parameter reduces to the coordinate-ascent update minus the current parameter, making noisy estimates cheap and unbiased. Applied to latent Dirichlet allocation and the hierarchical Dirichlet process topic model on corpora of up to 3.8M documents, SVI outperforms classical variational inference in both speed and held-out likelihood.

## Problem & setting
Classical coordinate-ascent variational inference requires a full pass through all N data points before updating the global variational parameters, making it prohibitively expensive for large-scale datasets. The paper addresses scalable approximate posterior inference for a broad class of probabilistic models with local and global hidden variables whose complete conditionals lie in exponential families — a class encompassing mixture models, LDA, HMMs, Kalman filters, and Bayesian nonparametrics.

## Method
The model class factorizes as $p(x, z, \beta \mid \alpha) = p(\beta \mid \alpha)\prod_n p(x_n, z_n \mid \beta)$, with global variables $\beta$ and per-datapoint local variables $z_n$. Mean-field variational inference maximizes the ELBO $\mathcal{L}(q) = \mathbb{E}_q[\log p(x,z,\beta)] - \mathbb{E}_q[\log q(z,\beta)]$ by coordinate ascent, yielding updates $\lambda = \mathbb{E}_\phi[\eta_g(x, z, \alpha)]$ for global parameters and $\phi_{nj} = \mathbb{E}_\lambda[\eta_\ell(x_n, z_{n,-j}, \beta)]$ for local parameters.

Because $\lambda$ lies in a natural-parameter exponential family, the Fisher information matrix equals $\nabla^2_\lambda a_g(\lambda)$, and premultiplying the ordinary gradient by its inverse yields a natural gradient with the elegant form $\hat{\nabla}_\lambda \mathcal{L} = \mathbb{E}_\phi[\eta_g(x,z,\alpha)] - \lambda$. SVI replaces the full-data expectation with a mini-batch estimate: sample a subset of data points, compute their optimal local parameters, form an intermediate global parameter as if that subset were repeated $N$ times, then update $\lambda$ by taking a step of size $\rho_t$ toward this intermediate value. Step sizes satisfying $\sum\rho_t = \infty$, $\sum\rho_t^2 < \infty$ guarantee convergence (Robbins-Monro conditions).

## Key results
SVI analyzed 300K Nature articles, 1.8M New York Times articles, and 3.8M Wikipedia articles — scales at which classical variational inference is intractable. On held-out perplexity, SVI matches or exceeds classical VI while processing orders-of-magnitude more data per unit time. The Bayesian nonparametric HDP topic model trained with SVI outperforms the parametric LDA counterpart on the same data. The paper establishes that classical coordinate-ascent variational inference is a special case of natural-gradient ascent with step size 1, providing a unified theoretical view.

## Relevance to this research
SVI is a foundational reference for the VFE transformer's E-step: the VFE3 architecture performs iterative variational free-energy minimization over Gaussian belief tuples $(\mu, \Sigma, \phi)$, and the coordinate structure of SVI — local updates per token, global updates over the layer — maps directly onto the per-token belief update versus the shared prior/model update in the VFE hierarchy $h \to s \to p \to q \to o$. The natural-gradient perspective is directly relevant to the information-geometric foundations of the project: the Fisher metric on the variational parameter space is the same object that appears in the SPD / Riemannian geometry of Gaussian beliefs, and the natural gradient's invariance to reparameterization is the scalar analogue of the gauge-equivariance property pursued in GL(K) attention. The ELBO decomposition into expected log-joint minus entropy is the direct precursor to the free-energy functional used throughout the manuscripts. SVI's stochastic mini-batch paradigm also motivates the scalable training regime in `train_vfe3.py`.

## Cross-links
- Concepts: [[Variational Free Energy]], [[Evidence lower bound (ELBO)|Evidence Lower Bound]], [[Natural Gradient]], [[Information Geometry]], [[Exponential Family]]
- Related sources: [[jordan-1999-introduction-variational|jordan-1999-variational]], [[amari-1998-natural-gradient]], [[blei-2003-lda]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) gauge-equivariant attention|GL(K) Attention]]

## BibTeX
```bibtex
@article{Hoffman2013,
  author  = {Hoffman, Matt and Blei, David M. and Wang, Chong and Paisley, John},
  title   = {Stochastic Variational Inference},
  journal = {Journal of Machine Learning Research},
  year    = {2013},
  note    = {arXiv:1206.7051},
}
```
