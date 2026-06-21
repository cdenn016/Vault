---
type: paper
title: "Probabilistic Programming in Python using PyMC"
aliases:
  - "Salvatier 2016"
  - "PyMC3"
authors:
  - Salvatier, John
  - Wiecki, Thomas V.
  - Fonnesbeck, Christopher
year: 2016
arxiv: "1507.08050"
url: https://arxiv.org/abs/1507.08050
tags:
  - cluster/vfe
  - project/transformer
  - field/statistics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Probabilistic Programming in Python using PyMC

> [!info] Citation
> Salvatier, J., Wiecki, T. V., & Fonnesbeck, C. (2016). "Probabilistic Programming in Python using PyMC." arXiv:1507.08050 [stat.CO].

## TL;DR
PyMC3 is an open-source probabilistic programming framework in Python that enables flexible specification of Bayesian statistical models with readable, statistics-like syntax. Its central contribution is integrating next-generation MCMC algorithms — particularly the No-U-Turn Sampler (NUTS), a self-tuning variant of Hamiltonian Monte Carlo — with automatic differentiation via Theano, allowing efficient posterior inference in high-dimensional models without requiring specialized knowledge of fitting algorithms. The paper presents the framework through a motivating linear regression example and two case studies (stochastic volatility and coal mining disasters) demonstrating inference over complex, high-dimensional posteriors.

## Problem & setting
Classical Bayesian inference requires either analytical posteriors (rarely tractable) or hand-crafted sampling algorithms tuned to each model. Prior probabilistic programming systems (PyMC2, Stan, LaplacesDemon) partially addressed this, but either lacked gradient-based samplers or required non-Python syntax. PyMC3 aims to combine Python's expressivity and scientific ecosystem with state-of-the-art gradient-based MCMC, making complex Bayesian modeling accessible without specialized expertise.

## Method
PyMC3 uses a context-manager pattern (`with Model()`) to build a computational graph of random variables (stochastic and deterministic) whose joint log-posterior is automatically differentiated by Theano. The core inference algorithms are:

- **NUTS (No-U-Turn Sampler):** a self-tuning Hamiltonian Monte Carlo variant that uses gradient information from the log-posterior to achieve fast mixing. NUTS adaptively sets the step size and trajectory length, eliminating the need for manual tuning. It exploits the Hessian diagonal at the MAP estimate as a scaling matrix: $H = -\nabla^2 \log p(\theta | y)$.
- **MAP estimation:** via `find_MAP`, using BFGS or L-BFGS for high-dimensional cases.
- **Metropolis / Metropolis-Hastings:** for discrete variables where gradients are unavailable (e.g., switchpoints in the coal-mining model).

Model specification follows natural statistical notation. For a linear regression:
$$Y \sim \mathcal{N}(\mu, \sigma^2), \quad \mu = \alpha + \beta_1 X_1 + \beta_2 X_2$$
with priors $\alpha, \beta_i \sim \mathcal{N}(0, 100)$ and $\sigma \sim |\mathcal{N}(0,1)|$.

Theano transparently transcodes model expressions to C, compiles to machine code, and handles GPU execution — providing both autodiff and performance without leaving Python.

## Key results
The framework is demonstrated to successfully recover true parameters in simulated linear regression, model time-varying volatility in 400+ dimensional S&P 500 return series using NUTS with parallel chains, and identify a changepoint in UK coal mining disaster rates (circa a 5-10 year window around 1900) using a mixed NUTS/Metropolis sampler for continuous/discrete variables respectively. Sampling 2000 posterior draws from the stochastic volatility model with 400+ parameters completes efficiently using NUTS, a regime where Metropolis-Hastings is prohibitively slow due to high autocorrelation.

## Relevance to this research
PyMC3 is the primary tool used for Bayesian inference experiments in projects adjacent to the VFE transformer program. More directly, its architecture illustrates the modular registry pattern this codebase adopts: swappable inference algorithms behind a common interface mirror the VFE3 registry pattern for divergences, families, and transport modes. The NUTS sampler's use of gradient information from a log-posterior is conceptually analogous to how VFE gradient flow drives belief updates in the VFE transformer — both perform iterative minimization of a free-energy-like objective (negative log-posterior = KL + negative log-likelihood in a flat-prior MAP sense). The stochastic volatility case study's latent Gaussian random walk prior is structurally similar to the VFE hierarchy `h → s → p → q`, where latent states are inferred by minimizing variational free energy rather than sampling. PyMC3's Theano-based autodiff backend is the spiritual predecessor to the PyTorch autograd used for VFE gradient computation.

## Cross-links
- Concepts: [[Variational Free Energy]] [[Bayesian Inference]] [[Markov chain Monte Carlo|MCMC]]
- Related sources: [[hoffman2014no|hoffman2014nuts]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{salvatier2016probabilistic,
  author  = {Salvatier, John and Wiecki, Thomas V. and Fonnesbeck, Christopher},
  title   = {Probabilistic Programming in {Python} using {PyMC}},
  journal = {arXiv preprint arXiv:1507.08050},
  year    = {2016},
  url     = {https://arxiv.org/abs/1507.08050},
}
```
