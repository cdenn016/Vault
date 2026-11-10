---
type: reference
title: "Application of the information-percolation method to reconstruction problems on graphs"
aliases: ["polyanskiy2019application"]
authors: ["Yury Polyanskiy", "Yihong Wu"]
year: 2019
venue: "Mathematical Statistics and Learning"
doi: "10.4171/MSL/10"
arxiv: "1806.04195"
url: "https://doi.org/10.4171/MSL/10"
tags: [cluster/info-geometry, cluster/multi-agent, project/multi-agent, field/cs-ml, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# Application of the information-percolation method to reconstruction problems on graphs

> [!info] Citation
> Polyanskiy, Y., Wu, Y. (2019). *Application of the information-percolation method to reconstruction problems on graphs*. Mathematical Statistics and Learning, 2(1), 1--24. [DOI](https://doi.org/10.4171/MSL/10), [arXiv](https://arxiv.org/abs/1806.04195)

[Local PDF](../pdfs/polyanskiy-2019-application-information-percolation.pdf), 20 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper proves impossibility results for reconstruction on graphs by applying strong data-processing inequalities, bounding the mutual information between far-apart variables of a Markov random field by the probability of an open path in bond percolation.

## Problem & setting

The setting is a Markov random field on a graph, with the aim of limiting how much information variables at large graph distance can carry about each other, in order to prove that certain estimation problems cannot be solved.

## Method

Strong data-processing inequalities are applied edge by edge. Stronger bounds follow from comparing the mutual information with that of an erasure model on the same graph, whose erasure probabilities are given by the contraction coefficients.

## Key results

The mutual information between two distant variables is bounded by the open-path probability in bond percolation on the same graph. The applications stated are a sharp threshold for partial recovery in the spiked Wigner model, the best known upper bound on the noise level for group synchronization (obtained concurrently by Abbe and Boix), and a new impossibility result for community detection in the stochastic block model with $k$ communities.

## Relevance to this research

The manuscript cites its Theorem 1 for conventions checked pairwise through agreement observations that flip with some probability: the information that all observations and the conventions of a set carry about one agent's convention is bounded through bond percolation, so group-wide consistency cannot be inferred beyond a certain scale. It also cites the paper in related work for the mutual-information bound on distant variables. See [[Data processing inequality]], [[Mutual information]], [[Graph synchronization and connection Laplacians]] and [[Community detection and modularity]]. A companion note is [[polyanskiy-2017-strong-data-processing]].

## Cross-links

[[Collective agents literature map]]; [[Data processing inequality]]; [[Mutual information]]; [[Graph synchronization and connection Laplacians]]; [[Community detection and modularity]]; [[polyanskiy-2017-strong-data-processing]].

## BibTeX

```bibtex
@article{polyanskiy2019application,
  author        = {Polyanskiy, Yury and Wu, Yihong},
  title         = {Application of the information-percolation method to reconstruction problems on graphs},
  journal       = {Mathematical Statistics and Learning},
  volume        = {2},
  number        = {1},
  pages         = {1--24},
  year          = {2019},
  doi           = {10.4171/MSL/10},
  eprint        = {1806.04195},
  archivePrefix = {arXiv}
}
```
