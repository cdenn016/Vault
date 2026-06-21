---
type: paper
title: "Variational Algorithms for Approximate Bayesian Inference"
aliases:
  - Beal 2003
  - VB EM thesis
  - VBEM
  - beal-2003-variational-bayes
  - beal-2003-variational-algorithms-approximate-bayesian-inference
  - Beal 2003 — Variational Bayesian EM
authors:
  - Beal, Matthew J.
year: 2003
arxiv: null
url: null
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
  - field/neuroscience
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Variational Algorithms for Approximate Bayesian Inference

> [!info] Citation
> Beal, Matthew J. (2003). "Variational Algorithms for Approximate Bayesian Inference." PhD Thesis, University of London (Gatsby Computational Neuroscience Unit, UCL). Supervisor: Zoubin Ghahramani.

## TL;DR

This doctoral thesis presents a unified variational Bayesian (VB) framework for tractable approximate Bayesian inference in latent-variable models. The central contribution is the Variational Bayesian EM (VB EM) algorithm, which generalises the standard EM algorithm by integrating over model parameters rather than point-estimating them, yielding a lower bound on the marginal likelihood that enables principled Bayesian model selection. The framework is specialised to conjugate-exponential (CE) graphical models and applied to HMMs, mixtures of factor analysers, linear dynamical systems, and discrete DAG structure learning, with comparisons to BIC, Cheeseman-Stutz, and annealed importance sampling throughout.

## Problem & setting

Exact Bayesian inference requires computing the marginal likelihood $p(y) = \int d\theta\, p(\theta) \sum_x p(x|\theta)p(y|x,\theta)$, which is intractable for most models of practical interest. Maximum likelihood EM avoids this but overfits and cannot perform model selection. Prior art includes Laplace's method, BIC/MDL, the Cheeseman-Stutz approximation, and Monte Carlo (MCMC/AIS), each with significant drawbacks in scalability, accuracy, or computational cost. The thesis asks whether a deterministic variational approximation can provide a practically useful lower bound on the marginal likelihood that scales to real models.

## Method

The VB EM algorithm introduces a factored variational posterior $q(x,\theta) = q(x)q(\theta)$ (mean-field over hidden variables and parameters) and optimises the free-energy lower bound on $\log p(y)$:

$$\mathcal{F}(q) = \langle \log p(y,x,\theta) \rangle_{q(x,\theta)} - \langle \log q(x,\theta) \rangle_{q(x,\theta)} \leq \log p(y).$$

The VBE step updates $q(x)$ treating expected sufficient statistics of $q(\theta)$ as pseudo-parameters; the VBM step updates $q(\theta)$ using expected sufficient statistics from $q(x)$. For conjugate-exponential (CE) models — where $p(\theta)$ is conjugate to $p(y,x|\theta)$ and the complete-data likelihood is in the exponential family — both updates remain in the same exponential/conjugate family and have closed form, mirroring the structure of standard EM. Several theorems establish automatic VB derivation for directed and undirected graphical models. The framework is extended with birth-death heuristics for component-count search (VBMFA), a variational Kalman smoother for linear dynamical systems, and hybrid VB/Monte Carlo importance sampling to assess bound tightness.

## Key results

The VB lower bound satisfies $\mathcal{F} \leq \log p(y)$, with equality when the mean-field factorisation is exact; BIC is recovered from VB in the large-data limit, establishing VB as a consistent model-selection criterion. For HMMs, VB automatically prunes redundant states and outperforms ML and MAP in predictive log-probability on held-out data. For mixtures of factor analysers, VB with birth-death moves simultaneously determines the number of mixture components and the intrinsic dimensionality of each component; it matches or beats BIC in classification accuracy on CEDAR digits. For linear dynamical systems, hyperparameter ARD trajectories recover the true latent state dimensionality from data and identify gene-gene interaction structure in expression data. For discrete DAG structure learning, VB outperforms BIC and Cheeseman-Stutz across data sizes and is competitive with annealed importance sampling at a fraction of the cost.

## Relevance to this research

The VB EM algorithm is the direct intellectual ancestor of the VFE minimisation loops in the V3 transformer. The free-energy lower bound $\mathcal{F}$ computed here is precisely the VFE used throughout the VFE transformer program; the E-step / M-step alternation maps onto the belief-update / parameter-update cycle in `train_vfe3.py`. The conjugate-exponential framework justifies the Gaussian belief tuples $(\mu, \Sigma, \phi)$ as the natural update target: Gaussians are in the CE family, so closed-form VBE updates exist and no sampling is required. The mean-field factorisation $q(x)q(\theta)$ motivates the per-token/per-layer belief factorisation in the transformer architecture. The marginal KL divergence results (Appendix C.3) for gamma-Gaussian variables are directly relevant to the KL divergence terms in the VFE free-energy functional used in GL(K) attention. The model-selection interpretation of $\mathcal{F}$ connects to the hyper-prior coupling term $\lambda_h\,\text{KL}(s_i \| h)$ in the full VFE hierarchy: models $s_i$ compete via the same Occam's razor that the marginal likelihood embodies.

## Cross-links
- Concepts: [[Variational Free Energy]], [[kullback-1951-kl-divergence|KL Divergence]], [[Conjugate-Exponential Family|Conjugate Exponential Family]], [[Variational EM|Expectation Maximisation]], [[Evidence lower bound (ELBO)]], [[Amortized inference]], [[Fisher information metric]]
- Theme: [[Variational free energy and predictive coding]]
- Related sources: [[winn-2005-variational-message-passing|winn-2005-vbem]], [[jordan-1999-introduction-variational]], [[dempster-1977-em-algorithm|dempster-1977-em]], [[neal-1998-variational-em]], [[blei-2017-variational-inference]], [[kingma-2013-auto-encoding-variational-bayes]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) gauge-equivariant attention|GL(K) Attention]], [[Gauge-Theoretic Multi-Agent VFE Model]]

> [!note] Editorial: Beal's monotonicity and closed-form VBEM updates are established for KL-based mean-field bounds in conjugate-exponential families. The VFE transformer departs on two axes — it can replace KL with a Rényi / $\alpha$-divergence in the belief step, and it uses structured Gaussian beliefs with gauge transport rather than a generic conjugate posterior — so it realizes the *spirit* of VBEM (coordinate ascent on a free-energy bound with distributions over both states and parameters) as a principled generalization, not a literal instance of the 2003 algorithm.

## BibTeX
```bibtex
@phdthesis{Beal2003,
  author  = {Beal, Matthew J.},
  title   = {Variational Algorithms for Approximate {B}ayesian Inference},
  school  = {University of London},
  year    = {2003},
  note    = {Gatsby Computational Neuroscience Unit, UCL},
  url     = {https://cse.buffalo.edu/faculty/mbeal/thesis/},
}
```
