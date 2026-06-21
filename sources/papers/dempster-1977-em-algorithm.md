---
type: paper
title: "Maximum Likelihood from Incomplete Data via the EM Algorithm"
aliases:
  - Dempster 1977
  - EM Algorithm
  - EM
  - dempster-1977-em
  - Dempster
  - Laird & Rubin 1977
authors:
  - Dempster, A. P.
  - Laird, N. M.
  - Rubin, D. B.
year: 1977
arxiv: null
url: https://links.jstor.org/sici?sici=0035-9246%281977%2939%3A1%3C1%3AMLFIDV%3E2.0.CO%3B2-Z
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Maximum Likelihood from Incomplete Data via the EM Algorithm

> [!info] Citation
> Dempster, A. P., Laird, N. M., & Rubin, D. B. (1977). "Maximum Likelihood from Incomplete Data via the EM Algorithm." *Journal of the Royal Statistical Society, Series B (Methodological)*, 39(1), 1–38. JSTOR stable URL: https://links.jstor.org/sici?sici=0035-9246%281977%2939%3A1%3C1%3AMLFIDV%3E2.0.CO%3B2-Z

## TL;DR
Dempster, Laird, and Rubin present the EM (Expectation-Maximization) algorithm as a broadly applicable framework for computing maximum-likelihood estimates from incomplete data. Each iteration alternates an E-step, which computes the conditional expectation of the complete-data log-likelihood given the observed data and current parameter estimate, with an M-step, which maximizes that expected log-likelihood. The paper proves that the observed-data likelihood is monotonically non-decreasing under every EM iteration and characterizes the rate of convergence in terms of the fraction of missing information.

## Problem & setting
Classical maximum-likelihood estimation presupposes fully observed data. In many real problems the observations $y$ are a many-to-one projection of hypothetical "complete data" $x$: missing values, grouped or censored measurements, finite mixture memberships, variance components, and latent factors all fit this mould. Prior work (Hartley 1958, Orchard & Woodbury 1972, Sundberg 1976) had exploited similar ideas in special cases, but without a unified algorithmic framework or general convergence theory. The authors formalize a two-sample-space setting with a mapping $x \mapsto y(x)$ and derive EM at three levels of generality: regular exponential families, curved exponential families, and the fully general case.

## Method
The algorithm cycles between two steps starting from an initial estimate $\phi^{(0)}$. Define

$$Q(\phi \mid \phi^{(p)}) = E\bigl[\log f(x \mid \phi) \mid y,\, \phi^{(p)}\bigr],$$

the conditional expectation of the complete-data log-likelihood.

- **E-step**: Compute $Q(\phi \mid \phi^{(p)})$. For regular exponential families this reduces to computing the conditional expectation of the sufficient statistics $t^{(p)} = E[t(x) \mid y, \phi^{(p)}]$.
- **M-step**: Set $\phi^{(p+1)} = \arg\max_\phi\, Q(\phi \mid \phi^{(p)})$.

A generalized EM (GEM) algorithm only requires $Q(M(\phi) \mid \phi) \geq Q(\phi \mid \phi)$ rather than a full maximization. The observed-data log-likelihood decomposes as $L(\phi) = Q(\phi \mid \phi^{(p)}) - H(\phi \mid \phi^{(p)})$, and Jensen's inequality ensures $H(\phi^{(p+1)} \mid \phi^{(p)}) \leq H(\phi^{(p)} \mid \phi^{(p)})$, which together with the non-decreasing Q gives Theorem 1: $L(\phi^{(p+1)}) \geq L(\phi^{(p)})$ for every GEM step. The rate of convergence near a stationary point is governed by

$$DM(\phi^*) = -\bigl[D^2_{00} Q(\phi^* \mid \phi^*)\bigr]^{-1} D^2_{00} H(\phi^* \mid \phi^*),$$

and the largest eigenvalue of $DM(\phi^*)$ equals the fraction of missing information, so convergence is slow when incomplete data lose a large fraction of information. The extension to posterior-mode estimation requires adding $G(\phi) = \log p(\phi)$ to the M-step objective.

## Key results
Theorem 1 (monotone likelihood): For every GEM step $L(M(\phi)) \geq L(\phi)$, with equality if and only if $k(x \mid y, M(\phi)) = k(x \mid y, \phi)$ almost everywhere.

Theorem 2 (convergence): Under a quadratic lower bound on the Q-gain at each step and boundedness of $L(\phi^{(p)})$, the sequence $\phi^{(p)}$ converges to some $\phi^*$ in the closure of $\Omega$.

Theorem 4 (rate): The local convergence rate is the spectral radius of $DM(\phi^*)$, which equals the fraction of information about $\phi$ contained in the missing (unobserved) part of $x$. An informative Bayesian prior reduces missing information and therefore accelerates convergence.

Examples covered include: multinomial missing data, normal linear model with missing values, multivariate normal with arbitrary missing patterns, grouped/censored/truncated data, finite mixture models, variance component estimation, hyperparameter estimation in empirical Bayes, iteratively reweighted least squares (robust regression), and factor analysis.

## Relevance to this research
The EM algorithm is the direct computational ancestor of the E-step / M-step structure in the VFE transformer. In the VFE framework the E-step minimizes free energy over beliefs $(μ, Σ)$ while holding model parameters fixed, and the M-step updates parameters (prior bank, connection weights, scalars) while holding beliefs fixed — a direct analogue of Dempster et al.'s cycle. The monotone decrease of variational free energy under coordinate updates mirrors the monotone increase of the incomplete-data likelihood under EM, and both derive from Jensen's inequality applied to a KL divergence. The EM rate-of-convergence result in terms of missing information fraction has an exact parallel in VFE convergence rates driven by the ratio of prior precision to total precision. The extension to posterior-mode finding (adding $G(\phi)$ to the M-step) is the precursor to MAP / free-energy minimization with an explicit prior, which is the foundational operation of the VFE transformer and active inference more broadly.

> [!note] Editorial (from manuscript-citation note): The free-energy / ELBO reinterpretation of EM is *later* work (Neal & Hinton; see [[neal-1998-variational-em]] / [[neal-1998-variational-em|neal-hinton-1998-em-variational]]). The 1977 paper itself states the algorithm and proves likelihood monotonicity, and does **not** use free-energy language. The project leans on the modern "free-energy view of EM" — E-step = belief updating, M-step = parameter learning, both ascent on one functional — which connects the classical algorithm to the [[Fisher information metric]], [[Natural gradient]], and the inertial / [[Mass as Fisher information]] reading of belief dynamics.

## Cross-links
- Concepts: [[Variational Free Energy]], [[Variational EM|E-step and M-step]], [[kullback-1951-kl-divergence|KL Divergence]], [[Information Geometry]], [[Missing Information Principle]], [[Variational EM]], [[Evidence lower bound (ELBO)]], [[Fisher information metric]], [[Natural gradient]], [[Mass as Fisher information]], [[Free-energy principle active inference]]
- Related sources: [[neal-1998-variational-em|neal-hinton-1998-em-variational]], [[neal-1998-variational-em]], [[beal-2003-variational-bayesian|beal-2003-variational-bayes]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) gauge-equivariant attention|GL(K) Attention]]

## BibTeX
```bibtex
@article{Dempster1977,
  author  = {Dempster, A. P. and Laird, N. M. and Rubin, D. B.},
  title   = {Maximum Likelihood from Incomplete Data via the {EM} Algorithm},
  journal = {Journal of the Royal Statistical Society, Series B (Methodological)},
  year    = {1977},
  volume  = {39},
  number  = {1},
  pages   = {1--38},
  doi     = {10.1111/j.2517-6161.1977.tb01600.x},
  note    = {With discussion},
}
```
