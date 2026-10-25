---
type: paper
title: "Maximum Likelihood Estimates of Linear Dynamic Systems"
aliases:
  - "Rauch, Tung and Striebel 1965"
  - "RTS smoother"
  - "Rauch-Tung-Striebel smoother"
authors:
  - "Rauch, H. E."
  - "Tung, F."
  - "Striebel, C. T."
year: 1965
url: https://doi.org/10.2514/3.3166
tags:
  - cluster/vfe
  - project/transformer
  - field/statistics
  - field/mathematics
created: 2026-10-25
---

# Maximum Likelihood Estimates of Linear Dynamic Systems

> [!info] Citation
> Rauch, H. E., Tung, F., & Striebel, C. T. (1965). *Maximum likelihood estimates of linear dynamic systems*. AIAA Journal, 3(8), 1445–1450.

## TL;DR
The fixed-interval smoother for a linear-Gaussian state-space model: after a Kalman forward pass, a backward recursion corrects each filtered estimate with the smoothed estimate one step later, $m_{t\mid T}=m_{t\mid t}+J_t(m_{t+1\mid T}-m_{t+1\mid t})$ with gain $J_t=P_{t\mid t}G^\top P_{t+1\mid t}^{-1}$, and the analogous covariance update.

## Method
The recursion uses only the filter's stored means and covariances, so it is a backward posterior message, not a derivative of the filter. The lag-one cross covariance that EM needs for the transition follows from the same gain.

> [!note] Editorial: No legal free copy was found (publisher paywall); there is no local PDF, and this note summarizes the abstract and the published record. Equation-level claims should be checked against the article.

## Relevance to this research
The windowed smoother of [[vfe3-2026-10-25-local-learner-test]] is this recursion applied to the assumed-density filter's Gaussians over windows of 1, 4, 16 or 64 steps; it supplies the lag-one moments of the transition M-step. Expectation correction ([[barber-2006-expectation-correction]]) generalizes it to switching systems. See also [[Kalman filter]].

## Cross-links
- Themes: [[Inference machinery — variational EM and filtering]]
- Methods: [[Variational EM]]
- Related sources: [[barber-2006-expectation-correction]], [[ghahramani-2000-switching-state-space]], [[vfe3-2026-10-25-local-learner-test]]

## BibTeX
```bibtex
@article{rauch1965maximum,
  author  = {Rauch, H. E. and Tung, F. and Striebel, C. T.},
  title   = {Maximum Likelihood Estimates of Linear Dynamic Systems},
  journal = {AIAA Journal},
  volume  = {3},
  number  = {8},
  pages   = {1445--1450},
  year    = {1965},
  doi     = {10.2514/3.3166}
}
```
