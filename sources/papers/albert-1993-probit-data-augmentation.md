---
type: paper
title: "Bayesian Analysis of Binary and Polychotomous Response Data"
aliases:
  - "Albert and Chib 1993"
  - "Albert-Chib augmentation"
  - "Probit data augmentation"
authors:
  - "Albert, James H."
  - "Chib, Siddhartha"
year: 1993
url: https://doi.org/10.1080/01621459.1993.10476321
tags:
  - cluster/vfe
  - project/transformer
  - field/statistics
created: 2026-10-25
---

# Bayesian Analysis of Binary and Polychotomous Response Data

> [!info] Citation
> Albert, J. H., & Chib, S. (1993). *Bayesian analysis of binary and polychotomous response data*. Journal of the American Statistical Association, 88(422), 669–679.

## TL;DR
The probit model is a normal linear regression on latent continuous utilities whose sign gives the observed response. Given the response, each utility is a truncated normal, so Gibbs sampling alternates truncated-normal draws of the utilities with a conjugate normal draw of the coefficients. The construction extends to ordered and multinomial responses and to hierarchical models.

## Method
The augmentation $u=x^\top\beta+\epsilon$, $\epsilon\sim\mathcal N(0,1)$, $y=\mathbb 1[u>0]$ makes the complete-data model conjugate. Its EM analogue replaces the draws by the truncated-normal moments of $u$.

> [!note] Editorial: No legal free copy was found (publisher paywall); there is no local PDF, and this note summarizes the abstract and the published record. Equation-level claims should be checked against the article.

## Relevance to this research
The sensor M-step of the local arm in [[vfe3-2026-10-25-local-learner-test]] uses this augmentation at every node of the probit vocabulary tree: under the truncated joint Gaussian of the utility and the latent state, $E[zz^\top]$, $E[z]$ and $E[uz]$ are closed form and the node coefficients come from a ridge solve.

## Cross-links
- Themes: [[Inference machinery — variational EM and filtering]]
- Methods: [[Variational EM]]
- Related sources: [[liu-1998-px-em]], [[minka-2001-expectation-propagation]], [[vfe3-2026-10-25-local-learner-test]]

## BibTeX
```bibtex
@article{albert1993bayesian,
  author  = {Albert, James H. and Chib, Siddhartha},
  title   = {Bayesian Analysis of Binary and Polychotomous Response Data},
  journal = {Journal of the American Statistical Association},
  volume  = {88},
  number  = {422},
  pages   = {669--679},
  year    = {1993},
  doi     = {10.1080/01621459.1993.10476321}
}
```
