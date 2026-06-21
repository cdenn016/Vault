---
type: paper
title: "The No-U-Turn Sampler: Adaptively Setting Path Lengths in Hamiltonian Monte Carlo"
aliases:
  - "Hoffman & Gelman 2014"
  - "NUTS"
  - "hoffman-2014-objects-of-consciousness"
  - "hoffman2014objectsofconsciousness"
  - "Hoffman & Prakash 2014"
  - "hoffman2014nuts"
authors:
  - Hoffman, Matthew D.
  - Gelman, Andrew
year: 2014
arxiv: "1111.4246"
url: https://arxiv.org/abs/1111.4246
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The No-U-Turn Sampler: Adaptively Setting Path Lengths in Hamiltonian Monte Carlo

> [!info] Citation
> Hoffman, M. D., & Gelman, A. (2014). "The No-U-Turn Sampler: Adaptively Setting Path Lengths in Hamiltonian Monte Carlo." *Journal of Machine Learning Research*, 15(1), 1593–1623. https://arxiv.org/abs/1111.4246

## TL;DR
NUTS is an adaptive extension of Hamiltonian Monte Carlo (HMC) that eliminates the need to hand-tune the number of leapfrog steps — the most sensitive hyperparameter in HMC. It uses a recursive doubling procedure that halts when the simulated Hamiltonian trajectory would reverse direction (the "U-turn" criterion), and couples this with the dual-averaging step-size adaptation of Nesterov (2009). The result is an essentially tuning-free HMC that matches or exceeds the efficiency of carefully hand-tuned HMC on a broad range of posteriors.

## Problem & setting
Standard HMC requires the practitioner to specify two hyperparameters: the step size $\varepsilon$ and the number of leapfrog steps $L$. While step size can be tuned by targeting a desired acceptance rate, $L$ has no such automatic proxy: too small and the sampler is nearly a random walk; too large and it wastes computation retracing its path. Prior work offered heuristics but no principled automatic procedure. The paper addresses this gap for general continuous posterior distributions, targeting the setting of modern probabilistic programming (e.g., Stan) where users should not need MCMC expertise.

## Method
The No-U-Turn criterion declares a trajectory "done" when the inner product $(\theta^+ - \theta^-) \cdot r^- < 0$ or $(\theta^+ - \theta^-) \cdot r^+ < 0$, where $\theta^\pm$ and $r^\pm$ are the endpoints and momenta of the trajectory — i.e., when the trajectory begins to loop back. A slice-sampler acceptance step preserves detailed balance. To avoid bias from stopping at a preselected point, NUTS uses a balanced binary-tree doubling scheme that builds the trajectory in both directions and proposes a uniformly drawn point from the new subtree, accepting with a Metropolis-style correction. Step size $\varepsilon$ is adapted during a warm-up phase via Nesterov dual averaging targeting an acceptance probability of 0.65.

Key equations: the Hamiltonian is $H(\theta, r) = U(\theta) + K(r)$ with $U(\theta) = -\log \pi(\theta)$ and $K(r) = \frac{1}{2} r^T M^{-1} r$; leapfrog integrator preserves volume and (approximately) $H$. The U-turn condition is $(\theta^+ - \theta^-)^\top r^- < 0$ or $(\theta^+ - \theta^-)^\top r^+ < 0$.

## Key results
NUTS matches or outperforms hand-tuned HMC on a range of test problems (a 250-dimensional multivariate Gaussian, a hierarchical logistic regression, a stochastic volatility model, and a 3072-dimensional item-response model). In the hierarchical models it substantially outperforms Gibbs sampling in effective samples per second. The dual-averaging adaptation reliably selects $\varepsilon$ near the theoretically optimal value, and the automatic path-length selection adds little overhead compared to a single leapfrog step. These results established NUTS as the default sampler in Stan and subsequently in PyMC, NumPyro, and Pyro.

## Relevance to this research
NUTS is relevant to the VFE transformer program primarily as a high-quality posterior sampler that can be used to validate variational approximations — i.e., to check whether the Gaussian beliefs $(μ, Σ)$ maintained by the VFE layers are faithful summaries of the true posterior, and to generate ground-truth samples for calibration diagnostics. More directly, the paper's dual-averaging step-size schedule is a clean example of adaptive mirror-descent on a simplex-like constraint, which is conceptually adjacent to the natural-gradient / information-geometry updates in the VFE E-step. The NUTS U-turn criterion also has a geometric flavor (detecting curvature reversal in Hamiltonian flow) that parallels the SPD / Riemannian geometry used in the belief-state updates. In multi-agent active inference experiments, NUTS could serve as an oracle sampler for individual agent posteriors against which the variational updates are benchmarked.

## Cross-links
- Concepts: [[Hamiltonian Monte Carlo]], [[blei-2017-variational-inference|Variational Inference]], [[Information Geometry]], [[Natural Gradient]]
- Related sources: [[neal-2011-mcmc-hamiltonian|neal2011mcmc]], [[wainwright-2008-graphical-models-variational|wainwright2008graphical]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{hoffman2014no,
  author  = {Hoffman, Matthew D. and Gelman, Andrew},
  title   = {The No-U-Turn Sampler: Adaptively Setting Path Lengths in {Hamiltonian Monte Carlo}},
  journal = {Journal of Machine Learning Research},
  year    = {2014},
  volume  = {15},
  number  = {1},
  pages   = {1593--1623},
}
```
