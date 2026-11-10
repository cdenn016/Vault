---
type: reference
title: "Physical limits to biochemical signaling"
aliases: ["bialek2005physical"]
authors: ["William Bialek", "Sima Setayeshgar"]
year: 2005
venue: "Proceedings of the National Academy of Sciences"
doi: "10.1073/pnas.0504321102"
url: "https://doi.org/10.1073/pnas.0504321102"
tags: [cluster/multi-agent, project/multi-agent, field/physics, field/biology]
created: 2026-11-10
updated: 2026-11-10
---

# Physical limits to biochemical signaling

> [!info] Citation
> Bialek, W., Setayeshgar, S. (2005). *Physical limits to biochemical signaling*. Proceedings of the National Academy of Sciences, 102(29), 10040-10045. [DOI](https://doi.org/10.1073/pnas.0504321102)

[Local PDF](../pdfs/bialek-2005-physical-limits-biochemical.pdf), 13 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper revisits and generalizes the Berg and Purcell argument that molecule-counting noise limits how precisely a cell can measure a chemical concentration, and applies it to signaling inside the cell.

## Problem & setting

The introduction recalls the Berg and Purcell estimate: a sensor of linear size $a$ in a mean concentration $\bar c$ counts about $\bar c a^3$ molecules, each count has Poisson-type noise, and averaging over a time $\tau$ gives independent measurements at a rate set by the diffusive clearing time $a^2/D$. The resulting fractional accuracy scales as $(D a \bar c \tau)^{-1/2}$. The authors ask whether this holds for a single receptor independent of molecular details, how correlations among nearby receptors produce a limit set by the size of a receptor cluster, whether a corresponding minimum averaging time exists, and whether cells operate near such limits.

## Method

The extract shows the problem set up through the Berg and Purcell argument and the three questions above; the derivations lie beyond the portion read. The manuscript's reading record states that Sections I and II of the preprint were read, that its first equation restates the Berg and Purcell estimate, and that a later equation gives the single-receptor lower bound.

## Key results

The abstract states that recent experiments are consistent with performance approaching these physical limits. The detailed bounds were not read beyond the two sections noted above.

## Relevance to this research

The collective-agents manuscript uses the single-receptor lower bound on relative root-mean-square error, scaling inversely with the square root of the product of diffusion constant, receptor size, concentration and integration time, to bound what a sensing member can learn about a chemical environment, and remarks that other sensor models change the constant but not the scaling. This links to the vault's treatment of limits on what an agent can infer from a finite sensing channel, see [[Communication-constrained inference]], [[Channel Capacity]] and [[Collective active inference]].

## Cross-links

[[Collective agents literature map]]; [[Communication-constrained inference]]; [[Channel Capacity]]; [[Collective active inference]]; [[bradde-2017-pca-meets-rg]].

## BibTeX

```bibtex
@article{bialek2005physical,
  author  = {Bialek, William and Setayeshgar, Sima},
  title   = {Physical limits to biochemical signaling},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {102},
  number  = {29},
  pages   = {10040--10045},
  year    = {2005},
  doi     = {10.1073/pnas.0504321102}
}
```
