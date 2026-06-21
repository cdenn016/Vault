---
type: paper
title: "Latent Dirichlet Allocation"
aliases:
  - "blei-2003-lda"
  - "blei2003lda"
  - "Blei et al. 2003"
  - "LDA"
authors:
  - "Blei, David M."
  - "Ng, Andrew Y."
  - "Jordan, Michael I."
year: 2003
url: https://jmlr.org/papers/v3/blei03a.html
venue: "Journal of Machine Learning Research, 3, 993–1022"
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Latent Dirichlet Allocation

> [!info] Citation
> Blei, David M., Ng, Andrew Y., Jordan, Michael I. (2003). "Latent Dirichlet Allocation." Journal of Machine Learning Research, 3, 993–1022. https://jmlr.org/papers/v3/blei03a.html

## TL;DR
Introduces Latent Dirichlet Allocation, a hierarchical Bayesian topic model in which documents are mixtures over latent topics and topics are distributions over words. Inference uses variational EM to approximate the intractable posterior over topic assignments.

## Relevance to this research
A landmark application of variational inference / variational EM that the stochastic variational inference work builds on; exemplifies the mean-field variational machinery central to the program's VFE foundations.

## Cross-links
[[hoffman-2013-svi]]

## BibTeX
```bibtex
@article{blei2003lda,
  title={Latent Dirichlet Allocation},
  author={Blei, David M. and Ng, Andrew Y. and Jordan, Michael I.},
  journal={Journal of Machine Learning Research},
  volume={3},
  pages={993--1022},
  year={2003}
}
```
