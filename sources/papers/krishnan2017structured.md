---
type: paper
title: "Structured Inference Networks for Nonlinear State Space Models"
aliases:
  - "Krishnan 2017"
  - "DMM"
  - "Deep Kalman Model"
authors:
  - Krishnan, Rahul G.
  - Shalit, Uri
  - Sontag, David
year: 2017
arxiv: "1609.09869"
url: https://arxiv.org/abs/1609.09869
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Structured Inference Networks for Nonlinear State Space Models

> [!info] Citation
> Krishnan, R. G., Shalit, U., & Sontag, D. (2017). "Structured Inference Networks for Nonlinear State Space Models." AAAI 2017. arXiv:1609.09869.

## TL;DR
This paper introduces a unified learning algorithm for a broad class of linear and nonlinear Gaussian state space models (GSSMs), including deep variants where emission and transition distributions are parameterized by neural networks (Deep Markov Models, DMMs). The core innovation is a family of structured inference networks — RNN-based recognition networks whose factorization mirrors the true posterior's Markov structure — that simultaneously learn alongside the generative model via a structured variational lower bound. Structured approximations that incorporate future observations substantially outperform mean-field and past-only baselines.

## Problem & setting
Classical methods for learning and inference in nonlinear GSSMs (dual extended Kalman filter, EM, particle filters) are computationally demanding and scale poorly to high-dimensional data. Recent variational approaches using recognition networks often rely on mean-field or past-only approximations, which ignore the information from future observations that the true posterior depends on. The paper addresses how to efficiently compile structured posterior inference into a recognition network's parameters for sequential latent variable models.

## Method
The generative model is a GSSM:

$$z_t \sim \mathcal{N}(G_\alpha(z_{t-1}, \Delta_t),\; S_\beta(z_{t-1}, \Delta_t)), \quad x_t \sim \Pi(F_\kappa(z_t))$$

The key observation is that the true posterior factorizes as:

$$p(\vec{z}|\vec{x}) = p(z_1|\vec{x})\prod_{t=2}^{T} p(z_t | z_{t-1}, x_t, \ldots, x_T)$$

meaning inference at time $t$ requires information from the future, not just the past. The proposed variational approximation mimics this structure:

$$q_\phi(\vec{z}|\vec{x}) = q_\phi(z_1|\vec{x})\prod_{t=2}^{T} q_\phi(z_t | z_{t-1}, x_t, \ldots, x_T)$$

where means and diagonal covariances are parameterized by bidirectional or right-to-left RNNs combined via a "combiner function" performing Gaussian belief propagation (variance-weighted mean combination). The variational lower bound is:

$$\mathcal{L}(\vec{x};\theta,\phi) = \sum_{t=1}^{T} \mathbb{E}_{q_\phi(z_t|\vec{x})}[\log p_\theta(x_t|z_t)] - \mathrm{KL}(q_\phi(z_1|\vec{x})\|p_\theta(z_1)) - \sum_{t=2}^{T} \mathbb{E}_{q_\phi(z_{t-1}|\vec{x})}[\mathrm{KL}(q_\phi(z_t|z_{t-1},\vec{x})\|p_\theta(z_t|z_{t-1}))]$$

The KL factorization yields analytic (closed-form Gaussian) KL terms at each step, avoiding high-variance Monte Carlo gradient estimates. Five inference network variants are evaluated: mean-field left (MF-L), mean-field bidirectional (MF-LR), structured left (ST-L), structured right / Deep Kalman Smoother (DKS = ST-R), and structured bidirectional (ST-LR). For the Deep Markov Model, a gated transition function (inspired by GRUs but unconditional on observations) is used, providing flexible linear/nonlinear interpolation per dimension.

## Key results
On synthetic linear GSSMs, DKS (ST-R) and ST-LR converge to the RMSE of the exact Kalman smoother, while their variational lower bound becomes tight; mean-field past-only (MF-L) fails to match. On nonlinear synthetic systems, structured inference matches the Unscented Kalman Filter. On polyphonic music generation (JSB, Nottingham, Piano, Musedata), DMM with DKS achieves substantially lower NLL than RNNs, HMSBN, and TSBN; DMM-Aug further improves across all four datasets. With NADE emission, DMM-Aug-NADE is competitive with RNN-NADE. On electronic health records (diabetic cohort), the model correctly recovers the counterfactual effect of anti-diabetic medication on A1C levels via do-calculus queries on the latent trajectory.

## Relevance to this research
The structured variational lower bound in Eq. (6) is directly analogous to the VFE functional used in the VFE transformer: both decompose a KL between approximate posterior and prior into a sum of stepwise, analytically tractable KL terms over Gaussian beliefs. The DMM's latent state tuple $(z_t)$ with Gaussian belief propagation in the combiner function is a prototype of the belief tuple $(\mu, \Sigma)$ architecture in VFE3. The paper's emphasis on building inference networks that mirror the exact posterior's factorization structure parallels the gauge-equivariant attention design principle — structure imposed on the approximation to respect the generative model's symmetries. The factored KL derivation (Appendix A–B) is directly relevant to verifying the KL decomposition in the VFE free-energy functional. Missing-data marginalization (simply ignoring absent likelihood terms) is the same principle used when observations are partially observed in the VFE setting.

## Cross-links
- Concepts: [[Variational Free Energy]], [[Gaussian State Space Model]], [[Amortized inference|Recognition Network]], [[kullback-1951-kl-divergence|KL Divergence]]
- Related sources: [[kingma-2013-auto-encoding-variational-bayes|kingma2014vae]], [[Reparameterization trick|rezende2014stochastic]], [[chung-2015-vrnn|chung2015vrnn]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{krishnan2017structured,
  author    = {Krishnan, Rahul G. and Shalit, Uri and Sontag, David},
  title     = {Structured Inference Networks for Nonlinear State Space Models},
  booktitle = {Proceedings of the Thirty-First AAAI Conference on Artificial Intelligence},
  year      = {2017},
  note      = {arXiv:1609.09869},
}
```
