---
type: paper
title: "Tweedie's Formula and Selection Bias"
aliases:
  - Efron 2011
  - efron2011tweedie
  - Tweedie's formula
authors:
  - Efron, Bradley
year: 2011
url: https://doi.org/10.1198/jasa.2011.tm11181
pdf: sources/pdfs/efron-2011-tweedie-formula.pdf
tags:
  - cluster/vfe
  - project/transformer
  - field/statistics
created: 2026-10-24
---

# Tweedie's Formula and Selection Bias

> [!info] Citation
> Efron, B. (2011). *Tweedie's formula and selection bias*. Journal of the American Statistical Association, 106(496), 1602–1614. doi:10.1198/jasa.2011.tm11181. The local PDF is the author-hosted preprint.

## TL;DR
For $\mu\sim g$ and $z\mid\mu\sim\mathcal N(\mu,\sigma^2)$, the posterior mean is $E\{\mu\mid z\}=z+\sigma^2l'(z)$ with $l=\log f$ the log marginal density of $z$ (Eq. 1.4), a formula Robbins (1956) attributed to Tweedie. Because it needs only the marginal density, it gives an empirical Bayes correction of selection bias (the winner's curse) estimated from the observed $z$ values.

## Method
Section 2 states the formula in the exponential-family form $z\mid\eta\sim e^{\eta z-\psi(\eta)}f_0(z)$ (Eq. 2.1) and derives the posterior cumulants, in particular $\mathrm{var}\{\mu\mid z\}=\sigma^2(1+\sigma^2l''(z))$, so that log-concavity of the marginal bounds the posterior variance by $\sigma^2$. Later sections estimate $l'$ by Poisson regression, connect the formula to James–Stein estimation, define "empirical Bayes information" and "relevance", and relate it to false discovery rates.

## Relevance to this research
The exact prototype block MLP of [[VFE Transformer Program|vfe3]] is the multivariate second-order form of this formula: with evidence $p(\xi)=\sum_a\pi_a\mathcal N(\xi;\nu_a,C+\Lambda_a)$ the block computes $\xi^+=\xi+C\nabla\log p(\xi)$ and $C^+=C+C\nabla^2\log p(\xi)C$ (verified numerically in VFE_3.0 `explainer_video/research/notes_2026-10-24/answers_verified.md`, Q51(1)). The structural consequence used in the MLP discussion follows: any exact posterior-mean map with a Gaussian record has Jacobian $\mathrm{Cov}(X\mid\xi)C^{-1}$, so in whitened coordinates it is the gradient of a convex function, which constrains which residual MLPs it can equal ([[Template routing]]).

## Cross-links
- Methods: [[Template routing]]
- Themes: [[Inference machinery — variational EM and filtering]]
- Related sources: [[bovy-2011-extreme-deconvolution]], [[ramsauer2021hopfield]]

## BibTeX
```bibtex
@article{efron2011tweedie,
  author  = {Efron, Bradley},
  title   = {Tweedie's Formula and Selection Bias},
  journal = {Journal of the American Statistical Association},
  volume  = {106},
  number  = {496},
  pages   = {1602--1614},
  year    = {2011},
  doi     = {10.1198/jasa.2011.tm11181}
}
```
