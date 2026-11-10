---
type: reference
title: "Modularity and Community Structure in Networks"
aliases: ["newman2006modularity"]
authors: ["M. E. J. Newman"]
year: 2006
venue: "Proceedings of the National Academy of Sciences"
doi: "10.1073/pnas.0601602103"
url: "https://doi.org/10.1073/pnas.0601602103"
tags: [cluster/multi-agent, cluster/social-physics, cluster/social-physics/networks-and-contagion, project/multi-agent, project/social-physics, field/physics, field/sociology]
created: 2026-11-10
updated: 2026-11-10
---
# Modularity and Community Structure in Networks

> [!info] Citation
> Newman, M. E. J. (2006). *Modularity and Community Structure in Networks*. Proceedings of the National Academy of Sciences, 103(23), 8577-8582. [DOI](https://doi.org/10.1073/pnas.0601602103); [arXiv](https://arxiv.org/abs/physics/0602124)

[Local PDF](../pdfs/newman-2006-modularity-community-structure.pdf), 7 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper reformulates the modularity quality function for network divisions in terms of the eigenvectors of a modularity matrix, which yields a spectral algorithm for community detection.

## Problem & setting

Networks in the sciences often divide into communities, meaning densely connected groups with sparser links between groups. The introduction separates graph partitioning, where the number and size of groups is fixed in advance and a best division is sought whether or not a good one exists, from community detection, where the groups and even their existence are unknown. Optimizing modularity directly, for instance by simulated annealing, is described as computationally costly.

## Method

The modularity matrix is defined from the network, and the modularity of a division is expressed through its eigenvectors. Splitting by leading eigenvectors gives the algorithm, which the paper applies to several network data sets.

## Key results

The paper reports that the spectral method returns better-quality divisions than competing methods in noticeably shorter running times on the data sets it tests.

## Relevance to this research

The manuscript cites modularity as a closest precedent for contrast and declared null models: modularity compares within-group links with a null model, and measures contrast in message rates rather than in coherence, so the manuscript translates a transaction-flow contrast into a coherence contrast. Related precedents there are the communication tests of Deutsch and the transaction-flow index of Savage and Deutsch. See [[Community detection and modularity]], [[Spectral graph theory]] and [[Graph Laplacian]] for the vault's treatment of groups in networks.

## Cross-links

[[Collective agents literature map]]; [[Community detection and modularity]]; [[Spectral graph theory]]; [[Graph Laplacian]].

## BibTeX

```bibtex
@article{newman2006modularity,
  author  = {Newman, M. E. J.},
  title   = {Modularity and Community Structure in Networks},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {103},
  number  = {23},
  pages   = {8577--8582},
  year    = {2006},
  doi     = {10.1073/pnas.0601602103}
}
```
