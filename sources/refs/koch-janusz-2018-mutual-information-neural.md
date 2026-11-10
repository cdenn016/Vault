---
type: reference
title: "Mutual information, neural networks and the renormalization group"
aliases: ["kochjanusz2018mutual"]
authors: ["Maciej Koch-Janusz", "Zohar Ringel"]
year: 2018
venue: "Nature Physics"
doi: "10.1038/s41567-018-0081-4"
url: "https://doi.org/10.1038/s41567-018-0081-4"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/physics, field/cs-ml]
created: 2026-11-10
updated: 2026-11-10
---
# Mutual information, neural networks and the renormalization group

> [!info] Citation
> Koch-Janusz, M., Ringel, Z. (2018). *Mutual information, neural networks and the renormalization group*. Nature Physics, 14(6), 578-582. [DOI](https://doi.org/10.1038/s41567-018-0081-4), [arXiv](https://arxiv.org/abs/1704.06279)

[Local PDF](../pdfs/koch-janusz-2018-mutual-information-neural.pdf), 18 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper presents a neural-network algorithm that identifies relevant degrees of freedom in a spatial region and performs real-space renormalization group steps, trained by estimating mutual information between spatially separated regions.

## Problem & setting

The renormalization group keeps slow degrees of freedom and integrates out the rest, but the relevant degrees of freedom can be hard to identify. The input is samples of system configurations drawn from a Boltzmann distribution, with no knowledge of microscopic details.

## Method

A small visible region $V$ and its environment $E$ form the system. The network learns a conditional distribution of hidden variables $H$ given $V$, optimized by evaluating real-space mutual information between separated regions.

## Key results

The authors apply the method to the Ising and dimer models in two dimensions, obtain an RG flow and extract the Ising critical exponent, and report robustness to physically irrelevant noise.

## Relevance to this research

The manuscript lists the paper among information-theoretic formulations of renormalization in its related-work section, next to Mehta and Schwab (2014) and Beny and Osborne (2015), before turning to Gordon et al. (2021) on bottleneck compression. The manuscript's own record shows the arXiv abstract was the source for the record check. See [[Renormalization group flow]], [[Coarse Graining]], [[Mutual information]] and [[Information bottleneck]].

## Cross-links

[[Collective agents literature map]]; [[Renormalization group flow]]; [[Coarse Graining]]; [[Mutual information]]; [[Information bottleneck]].

## BibTeX

```bibtex
@article{kochjanusz2018mutual,
  author  = {Koch-Janusz, Maciej and Ringel, Zohar},
  title   = {Mutual information, neural networks and the renormalization group},
  journal = {Nature Physics},
  volume  = {14},
  number  = {6},
  pages   = {578--582},
  year    = {2018},
  doi     = {10.1038/s41567-018-0081-4}
}
```
