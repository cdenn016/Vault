---
type: paper
title: "A New Look at the Statistical Model Identification"
aliases:
  - "akaike-1974-aic"
  - "akaike1974aic"
  - "Akaike 1974"
  - "AIC"
authors:
  - "Akaike, Hirotugu"
year: 1974
url: https://doi.org/10.1109/TAC.1974.1100705
venue: "IEEE Transactions on Automatic Control"
tags:
  - cluster/info-geometry
  - cluster/methodology
  - project/transformer
  - project/multi-agent
  - field/statistics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# A New Look at the Statistical Model Identification

> [!info] Citation
> Akaike, Hirotugu (1974). "A New Look at the Statistical Model Identification." IEEE Transactions on Automatic Control. https://doi.org/10.1109/TAC.1974.1100705

## TL;DR
Introduces the Akaike Information Criterion (AIC), selecting models by maximizing penalized log-likelihood with a constant cost of one unit per free parameter, derived as an asymptotically unbiased estimate of the expected Kullback-Leibler divergence between the fitted model and the data-generating process. AIC operationalizes Occam's razor information-theoretically and became a foundational tool of model identification.

## Relevance to this research
AIC is the constant-penalty counterpart to BIC ([[schwarz-1978-bic]]) in the program's penalized-model-selection / Occam machinery, the same accuracy-minus-complexity tradeoff that underlies variational free energy and the species-gated retention criteria for hierarchical coarse-graining.

## Cross-links
[[MDL and BIC model selection]]

## BibTeX
```bibtex
@article{akaike1974aic,
  author  = {Akaike, Hirotugu},
  title   = {A New Look at the Statistical Model Identification},
  journal = {IEEE Transactions on Automatic Control},
  volume  = {19},
  number  = {6},
  pages   = {716--723},
  year    = {1974},
  doi     = {10.1109/TAC.1974.1100705}
}
```
