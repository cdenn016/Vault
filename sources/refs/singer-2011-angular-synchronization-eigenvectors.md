---
type: reference
title: "Angular synchronization by eigenvectors and semidefinite programming"
aliases: ["singer2011angular"]
authors: ["A. Singer"]
year: 2011
venue: "Applied and Computational Harmonic Analysis"
doi: "10.1016/j.acha.2010.02.001"
arxiv: "0905.3174"
url: "https://doi.org/10.1016/j.acha.2010.02.001"
tags: [cluster/multi-agent, cluster/gauge-theory, project/multi-agent, field/mathematics, field/cs-ml]
created: 2026-11-10
updated: 2026-11-10
---

# Angular synchronization by eigenvectors and semidefinite programming

> [!info] Citation
> Singer, A. (2011). *Angular synchronization by eigenvectors and semidefinite programming*. Applied and Computational Harmonic Analysis, 30(1), 20-36. [DOI](https://doi.org/10.1016/j.acha.2010.02.001), [arXiv](https://arxiv.org/abs/0905.3174)

[Local PDF](../pdfs/singer-2011-angular-synchronization-eigenvectors.pdf), 25 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper treats recovery of unknown angles from noisy measurements of their pairwise offsets, mod $2\pi$, and gives an eigenvector method and a semidefinite relaxation that tolerate many outlier measurements.

## Problem & setting

Angles $\theta_1,\dots,\theta_n$ are to be estimated up to a common additive phase from offsets $\theta_i-\theta_j$ measured on the edges of a graph. With exact offsets the problem is solvable if and only if the graph is connected, by integrating along a spanning tree. Tree integration is sensitive to errors, so a globally consistent integration is wanted. In the outlier model, bad edges carry offsets uniformly distributed on $[0,2\pi)$ regardless of the truth. Applications named include time synchronization in distributed networks and surface reconstruction.

## Method

The angles are recovered from the top eigenvector of a specially designed Hermitian matrix, and a semidefinite relaxation is also presented, which the abstract compares with the Goemans-Williamson max-cut algorithm. The analysis uses random matrix theory and information theory, and the eigenvector method is extended to other group structures.

## Key results

The abstract reports that the eigenvector method succeeds with very many outliers; as an example, 400 angles are estimated from all pairwise offsets with 90 percent outliers in under a second on a laptop.

## Relevance to this research

The manuscript cites the paper, with later work on Cheeger-type inequalities and on recovery of group differences on lattices, as precedent for treating consistency of pairwise translation maps as a synchronization problem, and says the paper recovers angles spectrally from noisy offsets. The manuscript's own holonomy criterion comes from the author's gauge-theoretic work, and the new element it claims is the origin of the maps. See [[Graph synchronization and connection Laplacians]], [[Holonomy]], [[Spectral graph theory]] and [[Synchronization and the Kuramoto model]].

## Cross-links

[[Collective agents literature map]]; [[Graph synchronization and connection Laplacians]]; [[Holonomy]]; [[Spectral graph theory]].

## BibTeX

```bibtex
@article{singer2011angular,
  author        = {Singer, A.},
  title         = {Angular synchronization by eigenvectors and semidefinite programming},
  journal       = {Applied and Computational Harmonic Analysis},
  volume        = {30},
  number        = {1},
  pages         = {20--36},
  year          = {2011},
  doi           = {10.1016/j.acha.2010.02.001},
  eprint        = {0905.3174},
  archivePrefix = {arXiv}
}
```
