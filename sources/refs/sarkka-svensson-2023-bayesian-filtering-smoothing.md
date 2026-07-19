---
type: reference
title: "Bayesian Filtering and Smoothing"
aliases:
  - "Särkkä and Svensson 2023"
  - "Bayesian Filtering and Smoothing 2e"
authors:
  - Simo Särkkä
  - Lennart Svensson
year: 2023
url: https://www.cambridge.org/core/books/bayesian-filtering-and-smoothing/F88740E8D25010CF3119A5CA379FA37A
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/cs-ml
  - field/mathematics
created: 2026-07-19
updated: 2026-07-19
---

# Bayesian Filtering and Smoothing

> [!info] Citation
> Simo Särkkä and Lennart Svensson (2023). *Bayesian Filtering and Smoothing*, 2nd edition. Cambridge University Press. DOI 10.1017/9781108917407.

## TL;DR

Särkkä and Svensson give a systematic treatment of Bayesian inference in state-space models: exact Gaussian filtering and smoothing, nonlinear approximations, particle methods, parameter estimation, and continuous-discrete models.

## What it establishes

The book begins from a normalized dynamic generative model and derives prediction, update, and smoothing recursions. It treats Kalman-family methods, sigma-point and Gaussian approximations, sequential Monte Carlo, and parameter learning as distinct approximations with explicit temporal semantics.

## Relevance to this research

This is the specialized reference for a structured causal or temporal gauge-VFE construction. It helps distinguish filtering from smoothing, online inference from batch posterior inference, and latent-state updates from parameter learning. It supports [[Inference machinery — variational EM and filtering]], the E-step/M-step boundary, and any proposed sequential gauge-causal ELBO.

## Access

The authors provide a complete prepublication PDF with Cambridge University Press's permission for personal viewing. A private local copy is stored at `sources/pdfs/sarkka-svensson-2023-bayesian-filtering-smoothing-prepublication.pdf` and must not be redistributed.

## Cross-links

- Concepts: [[Evidence lower bound (ELBO)]] · [[Generative model]] · [[Predictive Coding]]
- Themes: [[Inference machinery — variational EM and filtering]]
- Related sources: [[murphy-2023-probabilistic-machine-learning-advanced-topics]] · [[west-harrison-1997-bayesian-forecasting]]

## BibTeX

```bibtex
@book{SarkkaSvensson2023Bayesian,
  author    = {Simo S{\"a}rkk{\"a} and Lennart Svensson},
  title     = {Bayesian Filtering and Smoothing},
  edition   = {2},
  publisher = {Cambridge University Press},
  year      = {2023},
  isbn      = {9781108926645},
  doi       = {10.1017/9781108917407}
}
```
