---
type: reference
title: "Fitting Graphical Interaction Models to Multivariate Time Series"
aliases: ["eichler2006fitting"]
authors: ["Michael Eichler"]
year: 2006
venue: "Proceedings of the Twenty-Second Conference on Uncertainty in Artificial Intelligence (UAI 2006)"
arxiv: "1206.6839"
url: "https://arxiv.org/abs/1206.6839"
tags: [cluster/multi-agent, project/multi-agent, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# Fitting Graphical Interaction Models to Multivariate Time Series

> [!info] Citation
> Eichler, M. (2006). *Fitting Graphical Interaction Models to Multivariate Time Series*. Proceedings of the Twenty-Second Conference on Uncertainty in Artificial Intelligence (UAI 2006), 147-154. [arXiv](https://arxiv.org/abs/1206.6839)

[Local PDF](../pdfs/eichler-2006-fitting-graphical-interaction.pdf), 8 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper proposes parametric graphical interaction models for multivariate stationary Gaussian time series, defined through inverse covariances, and shows they correspond to vector autoregressive models under conditional independence constraints given by an undirected graph.

## Problem & setting

Graphical interaction models describe the interrelationships among the components of a time series by an undirected graph, called a partial correlation graph in the work of Dahlhaus, with conditional independences read off the inverse of the spectral matrix. The introduction states that identification of the graph had relied on nonparametric spectral estimation, which lacks a rigorous theory for choosing the best fitting graph and blocks ordinary model selection strategies.

## Method

The models generalize covariance selection to the time series setting. Maximum likelihood estimation uses Whittle's approximation to the log-likelihood, with an iterative method proposed for the resulting likelihood equations. Structure estimation becomes model selection, minimizing a distance such as the Kullback-Leibler divergence.

## Key results

The abstract states the correspondence between the inverse-covariance models and constrained vector autoregressions, and illustrates the concepts with one example. The extract covers the abstract and the introduction only.

## Relevance to this research

The manuscript lists exact stationary blankets for Gaussian processes among results it does not claim as new, pointing to the graphical models of stationary Gaussian processes of Dahlhaus (2000), which it knows through this restatement. The reading record says Sections 1 to 3 were read. It relates to [[Markov blanket interpretation debate]], [[Nonequilibrium steady state]] and [[Gaussian State Space Model]].

## Cross-links

[[Collective agents literature map]]; [[Markov blanket interpretation debate]]; [[Nonequilibrium steady state]]; [[Gaussian State Space Model]].

## BibTeX

```bibtex
@inproceedings{eichler2006fitting,
  author        = {Eichler, Michael},
  title         = {Fitting Graphical Interaction Models to Multivariate Time Series},
  booktitle     = {Proceedings of the Twenty-Second Conference on Uncertainty in Artificial Intelligence (UAI 2006)},
  pages         = {147--154},
  year          = {2006},
  eprint        = {1206.6839},
  archivePrefix = {arXiv}
}
```
