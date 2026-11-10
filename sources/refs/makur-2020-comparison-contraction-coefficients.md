---
type: reference
title: "Comparison of Contraction Coefficients for $f$-Divergences"
aliases: ["makur2020comparison"]
authors: ["Anuran Makur", "Lizhong Zheng"]
year: 2020
venue: "Problems of Information Transmission"
doi: "10.1134/S0032946020020015"
arxiv: "1510.01844"
url: "https://doi.org/10.1134/S0032946020020015"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/statistics, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---

# Comparison of Contraction Coefficients for $f$-Divergences

> [!info] Citation
> Makur, A., Zheng, L. (2020). *Comparison of Contraction Coefficients for $f$-Divergences*. Problems of Information Transmission, 56(2), 103-156. [DOI](https://doi.org/10.1134/S0032946020020015); [arXiv](https://arxiv.org/abs/1510.01844) (arXiv title: Linear bounds between contraction coefficients for $f$-divergences)

[Local PDF](../pdfs/makur-2020-comparison-contraction-coefficients.pdf), 37 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and abstract.

## TL;DR

A study of contraction coefficients, the distribution-dependent constants that sharpen data processing inequalities for $f$-divergences into strong data processing inequalities, and of how the coefficients for different $f$ compare.

## Problem & setting

For a source distribution and a channel, the contraction coefficient of an $f$-divergence is at most one and at least the coefficient for the $\chi^2$-divergence. The paper examines when these bounds are attained and how the coefficients relate to each other.

## Key results

Per the abstract and the extract, the upper bound of one is attained when the joint distribution is decomposable, and the $\chi^2$ lower bound is attained by driving the input $f$-divergences to zero. The paper gives a linear upper bound on the coefficients for a class of $f$-divergences in terms of the $\chi^2$ coefficient, refined for the Kullback-Leibler case. It gives an alternative proof that the KL and $\chi^2$ coefficients are equal for a Gaussian source with additive Gaussian noise (the KL coefficient possibly under a power constraint). It also shows that the coefficients of channels, after extremizing over sources, coincide for all nonlinear operator convex $f$, which yields a characterization of the less noisy preorder by any such divergence.

## Relevance to this research

The manuscript cites the paper for the statement that its own contraction coefficient is known in substance: for a Gaussian source and an additive Gaussian channel the KL and $\chi^2$ coefficients coincide. The manuscript proves the coefficient directly and derives consequences along relay paths. The reading record is of the abstract of the arXiv version. Related pages are [[Data processing inequality]], [[Mutual information]], [[Canonical Correlation Analysis]] and [[Statistical experiment comparison and deficiency]].

## Cross-links

[[Collective agents literature map]]; [[Data processing inequality]]; [[Mutual information]]; [[Canonical Correlation Analysis]]; [[Statistical experiment comparison and deficiency]]; [[makur-2020-broadcasting-random-directed]].

## BibTeX

```bibtex
@article{makur2020comparison,
  author        = {Makur, Anuran and Zheng, Lizhong},
  title         = {Comparison of Contraction Coefficients for $f$-Divergences},
  journal       = {Problems of Information Transmission},
  volume        = {56},
  number        = {2},
  pages         = {103--156},
  year          = {2020},
  doi           = {10.1134/S0032946020020015},
  eprint        = {1510.01844},
  archivePrefix = {arXiv},
  note          = {arXiv title: Linear bounds between contraction coefficients for $f$-divergences}
}
```
