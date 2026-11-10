---
type: reference
title: "Coarse Graining, Fixed Points, and Scaling in a Large Population of Neurons"
aliases: ["meshulam2019coarse"]
authors: ["Leenoy Meshulam", "Jeffrey L. Gauthier", "Carlos D. Brody", "David W. Tank", "William Bialek"]
year: 2019
venue: "Physical Review Letters"
doi: "10.1103/PhysRevLett.123.178103"
url: "https://doi.org/10.1103/PhysRevLett.123.178103"
tags: [cluster/multi-agent, project/multi-agent, field/physics, field/neuroscience]
created: 2026-11-10
updated: 2026-11-10
---

# Coarse Graining, Fixed Points, and Scaling in a Large Population of Neurons

> [!info] Citation
> Meshulam, L., Gauthier, J. L., Brody, C. D., Tank, D. W., Bialek, W. (2019). *Coarse Graining, Fixed Points, and Scaling in a Large Population of Neurons*. Physical Review Letters, 123(17), 178103. [DOI](https://doi.org/10.1103/PhysRevLett.123.178103)

[Local PDF](../pdfs/meshulam-2019-coarse-graining-fixed.pdf), 5 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

A phenomenological coarse-graining procedure for activity in a large neural population, applied to recordings of more than a thousand hippocampal cells, with evidence for scaling and an approach to a nontrivial fixed point.

## Problem & setting

The paper asks whether renormalization-group style simplification can work for biological systems. In conventional uses, microscopic variables have spatial locations and local interactions, so one averages over neighborhoods. Neurons make connections across distances comparable to the whole field of view, so the authors use correlation as a proxy for neighborhood.

## Method

The authors compute the correlation matrix of all variables, greedily pair the most correlated variables, and define each coarse-grained variable as the sum of the pair. Iterating gives clusters whose size doubles at each step, and the variables can be placed on a binary tree. The normalization is restored at each step so that the average amplitude of the nonzero signals is fixed while zero keeps its meaning. The data are calcium fluorescence recordings from the mouse hippocampus during a virtual track task.

## Key results

According to the abstract, the distributions of coarse-grained variables seem to approach a fixed non-Gaussian form, and scaling appears in both static and dynamic quantities. The authors suggest that the network's collective behavior is described by a nontrivial fixed point. The evidence is empirical, from one preparation.

## Relevance to this research

The manuscript cites the paper as a precedent for coarse-graining interacting units, which it flags among precedents still to be checked, and distinguishes its own Gaussian coarse-graining of interacting units from this work. The connection is to [[Coarse Graining]], [[Renormalization group flow]], [[Fixed Points]] and [[Critical Phenomena]].

## Cross-links

[[Collective agents literature map]]; [[Coarse Graining]]; [[Renormalization group flow]]; [[Fixed Points]]; [[Critical Phenomena]].

## BibTeX

```bibtex
@article{meshulam2019coarse,
  author  = {Meshulam, Leenoy and Gauthier, Jeffrey L. and Brody, Carlos D. and Tank, David W. and Bialek, William},
  title   = {Coarse Graining, Fixed Points, and Scaling in a Large Population of Neurons},
  journal = {Physical Review Letters},
  volume  = {123},
  number  = {17},
  pages   = {178103},
  year    = {2019},
  doi     = {10.1103/PhysRevLett.123.178103}
}
```
