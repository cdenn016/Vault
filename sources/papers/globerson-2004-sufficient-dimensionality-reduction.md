---
type: paper
title: "Sufficient Dimensionality Reduction"
aliases:
  - "globerson2004sufficient"
  - "Globerson & Tishby 2004"
  - "Sufficient Dimensionality Reduction"
authors:
  - "Globerson, Amir"
  - "Tishby, Naftali"
year: 2003
url: https://www.jmlr.org/papers/v3/globerson03a.html
venue: "Journal of Machine Learning Research"
tags:
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Sufficient Dimensionality Reduction

> [!info] Citation
> Globerson, Amir, Tishby, Naftali (2003). "Sufficient Dimensionality Reduction." Journal of Machine Learning Research. https://www.jmlr.org/papers/v3/globerson03a.html

## TL;DR
Introduces sufficient dimensionality reduction (SDR), an information-theoretic method that extracts low-dimensional continuous features of one variable that are maximally informative about another, generalizing the information bottleneck to extract sufficient statistics via a max-min information criterion. It yields exponential-family models whose sufficient statistics are the learned features.

## Relevance to this research
A companion to the Gaussian information-bottleneck line (chechik-2005) within the info-geometry cluster; relevant to how the VFE transformer compresses beliefs into sufficient statistics. Connects information bottleneck, exponential families, and learned feature geometry.

## Cross-links
[[Information bottleneck]], [[Canonical Correlation Analysis]]

## BibTeX
```bibtex
@article{globerson2004sufficient,
  author  = {Globerson, Amir and Tishby, Naftali},
  title   = {Sufficient Dimensionality Reduction},
  journal = {Journal of Machine Learning Research},
  volume  = {3},
  pages   = {1307--1331},
  year    = {2003},
}
```
