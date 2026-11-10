---
type: reference
title: "Coherence in Large-Scale Networks: Dimension-Dependent Limitations of Local Feedback"
aliases: ["bamieh2012coherence"]
authors: ["Bassam Bamieh", "Mihailo R. Jovanović", "Partha Mitra", "Stacy Patterson"]
year: 2012
venue: "IEEE Transactions on Automatic Control"
doi: "10.1109/TAC.2012.2202052"
arxiv: "1112.4011"
url: "https://doi.org/10.1109/TAC.2012.2202052"
tags: [cluster/multi-agent, project/multi-agent, field/mathematics, field/physics]
created: 2026-11-10
updated: 2026-11-10
---
# Coherence in Large-Scale Networks: Dimension-Dependent Limitations of Local Feedback

> [!info] Citation
> Bamieh, B., Jovanović, M. R., Mitra, P., Patterson, S. (2012). *Coherence in Large-Scale Networks: Dimension-Dependent Limitations of Local Feedback*. IEEE Transactions on Automatic Control, 57(9), 2235-2249. [DOI](https://doi.org/10.1109/TAC.2012.2202052) / [arXiv](https://arxiv.org/abs/1112.4011)

[Local PDF](../pdfs/bamieh-2012-coherence-large-scale.pdf), 15 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper asks whether local feedback can keep large networks coherent under stochastic disturbances, and shows that for consensus and vehicular formations on regular lattices the answer depends on the spatial dimension.

## Problem & setting

The setting is distributed consensus and vehicular formation control. The introduction notes that platooning studies have long observed that good performance needs some global information, such as a leader's state, broadcast to the whole formation, and that no precise analysis of local versus global strategies existed.

## Method

The authors define macroscopic performance measures, global quantities that express how closely a formation resembles a solid object, and study how they scale with network size on lattices of dimension 1, 2 and higher. They analyze the effect through the underlying energetic modes of motion, which have large temporal and spatial scales.

## Key results

Higher dimension gives more favorable scaling of the coherence measures, and dimension 3 is needed for coherence in consensus and formations under certain conditions. The abstract states that large coherent one-dimensional vehicular platoons are impossible with only local feedback. The authors distinguish the effect from string instability.

## Relevance to this research

The manuscript cites this paper in its related work on opinion dynamics and noisy consensus: the variance of deviations from the average, which the paper calls coherence, scales poorly with network size in one and two dimensions. This is the control-theoretic counterpart of the manuscript's analysis of coherence and correlation length in collectives, relevant to [[Opinion dynamics]], [[Graph Laplacian]], [[Synchronization and the Kuramoto model]] and [[Critical Phenomena]].

## Cross-links

[[Collective agents literature map]]; [[Opinion dynamics]]; [[Graph Laplacian]]; [[Synchronization and the Kuramoto model]]; [[Critical Phenomena]].

## BibTeX

```bibtex
@article{bamieh2012coherence,
  author        = {Bamieh, Bassam and Jovanovi{\'c}, Mihailo R. and Mitra, Partha and Patterson, Stacy},
  title         = {Coherence in Large-Scale Networks: Dimension-Dependent Limitations of Local Feedback},
  journal       = {IEEE Transactions on Automatic Control},
  volume        = {57},
  number        = {9},
  pages         = {2235--2249},
  year          = {2012},
  doi           = {10.1109/TAC.2012.2202052},
  eprint        = {1112.4011},
  archivePrefix = {arXiv}
}
```
