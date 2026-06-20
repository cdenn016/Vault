---
type: reference
title: "A Generalization of the Bayesian Steady Forecasting Model"
aliases:
  - "Smith 1979"
  - "J.Q. Smith (1979) Steady Forecasting"
authors:
  - Jim Q. Smith
year: 1979
tags:
  - cluster/vfe
  - cluster/methodology
  - project/multi-agent
  - project/social-physics
  - field/statistics
created: 2026-06-19
updated: 2026-06-19
---

# A Generalization of the Bayesian Steady Forecasting Model

> [!info] Citation
> Smith, J. Q. (1979). "A Generalization of the Bayesian Steady Forecasting Model." *Journal of the Royal Statistical Society, Series B (Methodological)* **41**(3), 375–387. DOI: [10.1111/j.2517-6161.1979.tb01092.x](https://doi.org/10.1111/j.2517-6161.1979.tb01092.x). JSTOR: [2985066](https://www.jstor.org/stable/2985066).

> [!note] Identification: the project's manuscript cites `Smith1979` in an opinion-pooling / Bayesian-forecasting context alongside `WestHarrison1997`. Cross-checking the manuscript's `.bbl` resolves this uniquely to J. Q. Smith's 1979 JRSS-B paper on the generalized Bayesian steady forecasting model (title, journal, volume, and pages confirmed against the bibliography entry and JSTOR).

## TL;DR

Generalizes the Bayesian **steady forecasting model** — a dynamic model in which the predictive distribution is updated each step with a fixed geometric **discount** of past information — beyond the normal case to a wide class of processes (Beta-Binomial, Poisson-Gamma, Student-$t$ steady models). The construction defines the time series on the decision/parameter space and gives simple conjugate updating relations in which a multiplicative discount factor controls how rapidly historical observations lose influence on present inference. It is a canonical source for the infinite-horizon geometric-discounting form of sequential Bayesian updating.

## What it establishes

Smith builds steady forecasting models in which the prior at each step is obtained from the previous posterior by a discounting operation, yielding an exponentially-weighted, infinite-horizon dependence on past data. The key structural feature for the project: a single discount factor $\rho \in (0,1)$ generates geometric weights $\rho^k$ on information $k$ steps back, so older observations contribute with geometrically decaying influence. The paper extends this from the Gaussian steady model to non-normal conjugate families, showing the geometric-discount mechanism is general rather than tied to normality.

## Why the project cites it

[[participatory-it-from-bit]] cites this (`Smith1979`) for the **infinite-horizon geometric-discount form** that justifies its multi-generation hyperprior weights. The manuscript's geometric weighting $\lambda_k = \lambda_0 \rho^k$ on per-generation ancestral contributions is identified with "the infinite-horizon geometric-discount form of Smith (1979)," where the role of historical time is replaced by the **hierarchical scale-distance $k$** and the historical observation by the gauge-transported ancestral belief. So Smith (1979) is the source for the geometric $\rho^k$ decay structure of the project's cross-scale coupling in [[Ouroboros multi-scale dynamics]], complementing [[west-harrison-1997-bayesian-forecasting]] (the discounted-likelihoods DLM construction). Together they legitimize the project's hierarchical discounting as a reuse of well-established sequential-Bayesian forgetting.

```bibtex
@article{smith1979generalization,
  author  = {Smith, J. Q.},
  title   = {A Generalization of the {B}ayesian Steady Forecasting Model},
  journal = {Journal of the Royal Statistical Society, Series B (Methodological)},
  volume  = {41},
  number  = {3},
  pages   = {375--387},
  year    = {1979},
  doi     = {10.1111/j.2517-6161.1979.tb01092.x}
}
```
