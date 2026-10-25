---
type: paper
title: "Parameter Expansion to Accelerate EM: The PX-EM Algorithm"
aliases:
  - "Liu, Rubin and Wu 1998"
  - "PX-EM"
  - "Parameter-expanded EM"
authors:
  - "Liu, Chuanhai"
  - "Rubin, Donald B."
  - "Wu, Ying Nian"
year: 1998
url: https://doi.org/10.1093/biomet/85.4.755
tags:
  - cluster/vfe
  - project/transformer
  - field/statistics
created: 2026-10-25
---

# Parameter Expansion to Accelerate EM: The PX-EM Algorithm

> [!info] Citation
> Liu, C., Rubin, D. B., & Wu, Y. N. (1998). *Parameter expansion to accelerate EM: the PX-EM algorithm*. Biometrika, 85(4), 755–770. doi:10.1093/biomet/85.4.755.

## TL;DR
PX-EM enlarges the complete-data model with working parameters that the observed data do not identify, runs EM in the expanded model, and maps back to the original parameters. The expansion corrects the M-step for the covariance adjustment that ordinary EM ignores, so it converges at least as fast as EM while keeping its monotonicity and simplicity. Examples include the multivariate t, factor analysis and probit regression.

## Method
In probit regression the latent utilities get a free scale; the expanded M-step fits it together with the coefficients and divides it out, which removes the slow mode in which plain EM adjusts the coefficient scale.

> [!note] Editorial: No legal free copy was found (publisher paywall); there is no local PDF, and this note summarizes the abstract and the published record. Equation-level claims should be checked against the article.

## Relevance to this research
The `_px` arm of [[vfe3-2026-10-25-local-learner-test]] is this construction for the probit tree: each node's coefficients are rescaled by the expected residual utility variance after the ridge solve. It gave the largest single gain of the accelerations tried (0.011 bits per byte after one pass). The latent state's unidentified $GL(d)$ frame is a larger working group that this arm does not exploit.

## Cross-links
- Themes: [[Inference machinery — variational EM and filtering]]
- Methods: [[Variational EM]]
- Related sources: [[dempster-1977-em-algorithm]], [[meng-1994-em-convergence-rates]], [[albert-1993-probit-data-augmentation]], [[vfe3-2026-10-25-local-learner-test]]

## BibTeX
```bibtex
@article{liu1998parameter,
  author  = {Liu, Chuanhai and Rubin, Donald B. and Wu, Ying Nian},
  title   = {Parameter Expansion to Accelerate {EM}: The {PX-EM} Algorithm},
  journal = {Biometrika},
  volume  = {85},
  number  = {4},
  pages   = {755--770},
  year    = {1998},
  doi     = {10.1093/biomet/85.4.755}
}
```
