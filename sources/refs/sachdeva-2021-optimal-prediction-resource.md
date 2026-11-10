---
type: reference
title: "Optimal prediction with resource constraints using the information bottleneck"
aliases: ["sachdeva2021optimal"]
authors: ["Vedant Sachdeva", "Thierry Mora", "Aleksandra M. Walczak", "Stephanie E. Palmer"]
year: 2021
venue: "PLoS Computational Biology"
doi: "10.1371/journal.pcbi.1008743"
url: "https://doi.org/10.1371/journal.pcbi.1008743"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/biology, field/physics]
created: 2026-11-10
updated: 2026-11-10
---

# Optimal prediction with resource constraints using the information bottleneck

> [!info] Citation
> Sachdeva, V., Mora, T., Walczak, A. M., Palmer, S. E. (2021). *Optimal prediction with resource constraints using the information bottleneck*. PLoS Computational Biology, 17(3), e1008743. [DOI](https://doi.org/10.1371/journal.pcbi.1008743)

[Local PDF](../pdfs/sachdeva-2021-optimal-prediction-resource.pdf), 27 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and manuscript reading record.

## TL;DR

The paper computes, with the information bottleneck, the trade-off between representing past input faithfully and predicting future input, for input dynamics of increasing complexity, and relates the optimal representations to biological prediction.

## Problem & setting

Organisms must encode information about the external world under resource limits, and prediction of future input is useful in many biological systems. The authors study three systems: simple inertial motion, motion with long-tailed temporal correlations, and mutating viral strains.

## Method

The information bottleneck gives the trade-off curve between retained past information and predictive information. The record notes that the manuscript's reading covered the case of a stochastically driven damped harmonic oscillator.

## Key results

For motion prediction, whether velocity or position information is more useful depends on the parameters of the input dynamics. The authors identify representations that transfer best between motion contexts, examine the role of long-term memory for non-Markovian dynamics, and report that, in evolutionary population dynamics, prediction links to clustering allele frequencies into non-overlapping memories, with discrete optimal representations. These are statements of the abstract and author summary.

## Relevance to this research

The manuscript cites the paper for the finding that the optimal predictive representation of a stochastically driven damped oscillator rotates as the prediction lag grows, which it compares with the rotation of its own optimal channel directions. The connection is to resource-limited compression in agent sensing, see [[Information bottleneck]], [[Canonical Correlation Analysis]] and [[Communication-constrained inference]]. The manuscript reads the paper through targeted extraction.

## Cross-links

[[Collective agents literature map]]; [[Information bottleneck]]; [[Canonical Correlation Analysis]]; [[Communication-constrained inference]]; [[scharf-1998-wiener-filters-canonical]].

## BibTeX

```bibtex
@article{sachdeva2021optimal,
  author  = {Sachdeva, Vedant and Mora, Thierry and Walczak, Aleksandra M. and Palmer, Stephanie E.},
  title   = {Optimal prediction with resource constraints using the information bottleneck},
  journal = {PLoS Computational Biology},
  volume  = {17},
  number  = {3},
  pages   = {e1008743},
  year    = {2021},
  doi     = {10.1371/journal.pcbi.1008743}
}
```
