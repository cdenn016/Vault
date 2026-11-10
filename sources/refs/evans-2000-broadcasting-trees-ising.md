---
type: reference
title: "Broadcasting on trees and the Ising model"
aliases: ["evans2000broadcasting"]
authors: ["William Evans", "Claire Kenyon", "Yuval Peres", "Leonard J. Schulman"]
year: 2000
venue: "The Annals of Applied Probability"
doi: "10.1214/aoap/1019487349"
url: "https://doi.org/10.1214/aoap/1019487349"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/mathematics, field/physics]
created: 2026-11-10
updated: 2026-11-10
---
# Broadcasting on trees and the Ising model

> [!info] Citation
> Evans, W., Kenyon, C., Peres, Y., Schulman, L. J. (2000). *Broadcasting on trees and the Ising model*. The Annals of Applied Probability 10(2), 410-433. [DOI](https://doi.org/10.1214/aoap/1019487349)

No local copy: no open-access file passed validation on November 10, 2026. Reading basis: abstract and manuscript reading record.

## TL;DR

The paper studies reconstruction of a root bit sent down a noisy tree, and establishes a sharp threshold for general infinite trees in terms of the percolation critical probability.

## Problem & setting

An unbiased random bit at the root is sent down the edges of a tree $T$, each edge flipping it independently with probability $\varepsilon$. The goal is to reconstruct the root bit from the values at level $n$. The abstract notes that the model has been studied in information theory, genetics and statistical mechanics.

## Key results

The abstract bounds the reconstruction probability above by a maximum flow and below by electrical conductance. For general infinite trees, the probability of correct reconstruction tends to $1/2$ if $(1-2\varepsilon)^2 < p_c(T)$ and stays bounded away from $1/2$ in the opposite case, with $p_c(T)$ the percolation critical probability. Reconstruction is equivalent to purity of the free-boundary Gibbs state of the Ising model on a tree. The abstract credits the regular-tree case to Bleher, Ruiz and Zagrebnov, and states that the extension depends on a coupling argument and on a reconstruction algorithm weighting bits by electrical current flow.

## Relevance to this research

The manuscript cites the paper for the statement that the binary symmetric channel on a tree is reconstructible exactly when its squared correlation exceeds the percolation threshold, as a tight case of the Kesten-Stigum condition. The reading record says only the bibliographic data were verified. It relates to [[Critical Phenomena]], [[Mutual information]] and [[Coarse Graining]].

## Cross-links

[[Collective agents literature map]]; [[Critical Phenomena]]; [[Mutual information]]; [[Coarse Graining]]; [[evans-1999-signal-propagation-noisy]].

## BibTeX

```bibtex
@article{evans2000broadcasting,
  author  = {Evans, William and Kenyon, Claire and Peres, Yuval and Schulman, Leonard J.},
  title   = {Broadcasting on trees and the {Ising} model},
  journal = {The Annals of Applied Probability},
  volume  = {10},
  number  = {2},
  pages   = {410--433},
  year    = {2000},
  doi     = {10.1214/aoap/1019487349}
}
```
