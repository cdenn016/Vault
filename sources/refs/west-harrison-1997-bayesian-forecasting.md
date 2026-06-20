---
type: reference
title: "Bayesian Forecasting and Dynamic Models"
aliases:
  - "West & Harrison 1997"
  - "West-Harrison (1997) Dynamic Models"
authors:
  - Mike West
  - Jeff Harrison
year: 1997
tags:
  - cluster/vfe
  - cluster/methodology
  - project/multi-agent
  - project/social-physics
  - field/statistics
created: 2026-06-19
updated: 2026-06-19
---

# Bayesian Forecasting and Dynamic Models

> [!info] Citation
> West, M., & Harrison, J. (1997). *Bayesian Forecasting and Dynamic Models* (2nd ed.). Springer Series in Statistics. New York: Springer. DOI: [10.1007/b98971](https://doi.org/10.1007/b98971).

## TL;DR

The standard reference on **dynamic linear models (DLMs)** and Bayesian sequential forecasting: state-space models in which a latent state evolves through time and observations are noisy linear functions of it, updated online by Kalman-filter-style recursions. A central tool is **discounting** — geometrically down-weighting older information by a factor per time step so that recent observations dominate inference — which controls how quickly the model forgets the past.

## What it establishes

The book develops the full Bayesian treatment of DLMs: prior-to-posterior updating, prediction, and retrospective smoothing via conjugate normal recursions, plus practical machinery for model monitoring, intervention, and seasonal/regression components. Its discounting methodology (notably §10.7) replaces an explicit state-evolution variance with a discount factor that inflates uncertainty each step, implementing exponential forgetting of historical data without specifying a full dynamic model for the variance.

## Why the project cites it

[[participatory-it-from-bit]] cites this (`WestHarrison1997`, §10.7) as one of its four anchor identifications for the **multi-generation hyperprior**. The manuscript notes that its geometric weighting $\lambda_k = \lambda_0 \rho^k$ on per-generation contributions "is the same per-step discount used in the discounted-likelihoods construction of dynamic linear models," with one substitution: the role of *historical time* in a DLM is played in the project by the **hierarchical scale-distance $k$** (parent, grandparent, ...), and the role of the historical observation is played by the gauge-transported ancestral belief $p_k = \Omega_{i,I_k}[q_{I_k}]$. So the project's cross-scale discounting in [[Ouroboros multi-scale dynamics]] is a spatial/hierarchical reuse of West & Harrison's temporal discounting. Paired with [[smith-1979-steady-forecasting]] (the geometric-discount form), this reference legitimizes the $\rho^k$ decay in the project's hyperprior as a standard, principled forgetting mechanism rather than an arbitrary weight.

```bibtex
@book{west1997bayesian,
  author    = {West, Mike and Harrison, Jeff},
  title     = {Bayesian Forecasting and Dynamic Models},
  edition   = {2nd},
  series    = {Springer Series in Statistics},
  publisher = {Springer},
  address   = {New York},
  year      = {1997},
  doi       = {10.1007/b98971}
}
```
