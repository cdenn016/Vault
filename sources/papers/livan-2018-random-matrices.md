---
type: paper
title: "Introduction to Random Matrices: Theory and Practice"
aliases: ["Livan, Novaes & Vivo 2018", "Introduction to Random Matrices"]
authors: ["Giacomo Livan", "Marcel Novaes", "Pierpaolo Vivo"]
year: 2018
arxiv: 1712.07903
url: https://doi.org/10.1007/978-3-319-70885-0
tags: [cluster/spd-geometry, cluster/methodology, project/transformer, project/multi-agent, field/mathematics, field/physics]
created: 2026-06-20
updated: 2026-06-20
---

# Introduction to Random Matrices: Theory and Practice

> [!info] Citation
> Livan, G., Novaes, M. & Vivo, P. (2018). *Introduction to Random Matrices: Theory and Practice*. SpringerBriefs in Mathematical Physics, Vol. 26. Springer. arXiv:[1712.07903](https://arxiv.org/abs/1712.07903). DOI: [10.1007/978-3-319-70885-0](https://doi.org/10.1007/978-3-319-70885-0).

## TL;DR
A short, hands-on introduction to **random matrix theory** (RMT): the joint eigenvalue density of Gaussian ensembles, the semicircle law, level spacing and repulsion, the Coulomb-gas / log-gas picture, and Wishart (sample-covariance) matrices with the Marchenko–Pastur law. It is deliberately practical — explicit calculations and numerical recipes rather than rigorous proofs.

## Problem & setting
RMT studies the statistics of eigenvalues/eigenvectors of matrices with random entries, capturing universal spectral features (semicircle bulk, edge statistics, eigenvalue repulsion) that recur from nuclear physics to multivariate statistics. The book covers the Gaussian (GOE/GUE/GSE) and Wishart/Laguerre ensembles and the Dyson Coulomb-gas analogy.

## Method
Joint probability densities of eigenvalues via the Vandermonde Jacobian; saddle-point / Coulomb-gas evaluation of the spectral density; the Marchenko–Pastur distribution for the eigenvalues of sample covariance matrices $\tfrac{1}{n}X X^\top$ in the large-dimension limit.

## Key results
The Wigner semicircle law for Gaussian ensembles; eigenvalue repulsion / level-spacing distributions (Wigner surmise); and the Marchenko–Pastur edge for Wishart matrices — the baseline "null" spectrum against which structured covariance is detected.

## Relevance to this research
A marginal but genuine tools reference. The program's geometry runs on **SPD covariance matrices** $\Sigma_i$ ([[Symmetric spaces and the SPD cone]], [[Fisher information metric]]), and the relevant null model for the spectrum of an empirical / sample covariance is exactly the Wishart–Marchenko–Pastur ensemble RMT supplies — useful for asking when a learned $\Sigma$ carries structure beyond chance. RMT spectral statistics also bear on **attention matrices**: the eigenvalue distribution and the tendency toward low effective rank ([[dong-2021-rank-collapse|rank collapse]]) are spectral questions of the kind RMT answers, and random-matrix disorder is the same mathematics underlying spin-glass ensembles ([[mezard-parisi-virasoro-1987-spin-glass]]). Honestly peripheral — no result here is used directly — but it is the standard primer for the covariance/attention-spectrum analyses the program occasionally needs.

## Cross-links
- Concepts: [[Symmetric spaces and the SPD cone]], [[Fisher information metric]], [[Mechanistic interpretability of attention]]
- Related sources: [[bhatia-2007-positive-definite-matrices]], [[dong-2021-rank-collapse]], [[mezard-parisi-virasoro-1987-spin-glass]]

## BibTeX
```bibtex
@book{livan2018introduction,
  author    = {Livan, Giacomo and Novaes, Marcel and Vivo, Pierpaolo},
  title     = {Introduction to Random Matrices: Theory and Practice},
  series    = {SpringerBriefs in Mathematical Physics},
  volume    = {26},
  publisher = {Springer},
  year      = {2018},
  doi       = {10.1007/978-3-319-70885-0},
  note      = {arXiv:1712.07903}
}
```
