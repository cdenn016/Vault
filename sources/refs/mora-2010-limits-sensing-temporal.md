---
type: reference
title: "Limits of sensing temporal concentration changes by single cells"
aliases: ["mora2010limits"]
authors: ["Thierry Mora", "Ned S. Wingreen"]
year: 2010
venue: "Physical Review Letters"
doi: "10.1103/PhysRevLett.104.248101"
url: "https://doi.org/10.1103/PhysRevLett.104.248101"
tags: [cluster/multi-agent, project/multi-agent, field/physics, field/biology]
created: 2026-11-10
updated: 2026-11-10
---

# Limits of sensing temporal concentration changes by single cells

> [!info] Citation
> Mora, T., Wingreen, N. S. (2010). *Limits of sensing temporal concentration changes by single cells*. Physical Review Letters, 104(24), 248101. [DOI](https://doi.org/10.1103/PhysRevLett.104.248101); [arXiv](https://arxiv.org/abs/1002.3907)

[Local PDF](../pdfs/mora-2010-limits-sensing-temporal.pdf), 11 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

Lower bounds on the uncertainty with which a single cell can sense a ramp, that is a temporal change in concentration, extending the Berg and Purcell analysis of static concentration sensing.

## Problem & setting

Counting a small number of molecules gives relative noise scaling as the inverse square root of the count, which limits concentration sensing. Berg and Purcell worked this out for static concentrations; the authors note that no theory existed for ramp sensing, which is what small motile bacteria do in chemotaxis.

## Method

The authors derive bounds for three measurement devices: a single receptor, an absorbing sphere and a monitoring sphere. They compare linear regression of the input signal with maximum likelihood estimation, and they introduce a biochemical signaling network resembling the bacterial chemotaxis system to test implementations of the two strategies.

## Key results

Per the abstract, maximum likelihood estimation can be up to twice as accurate as linear regression. The extract adds that a network emulating maximum likelihood is twice as accurate as one emulating regression, at the cost of either storing signaling proteins near the receptors or irreversibility of the receptor cycle with energy consumption. The authors identify possible signatures of maximum likelihood in real systems.

## Relevance to this research

The manuscript cites the paper for its formula for a sphere that counts molecules in its volume without hindering diffusion. The manuscript's reading record says its Eq. 10, which attributes the formula to Berg and Purcell, was checked against the arXiv text; the manuscript uses the formula as the known leading term in its treatment of sensing in environments. The connection is to [[Communication-constrained inference]], [[Active Inference]] and [[Mutual information]].

## Cross-links

[[Collective agents literature map]]; [[Communication-constrained inference]]; [[Active Inference]]; [[Mutual information]].

## BibTeX

```bibtex
@article{mora2010limits,
  author  = {Mora, Thierry and Wingreen, Ned S.},
  title   = {Limits of sensing temporal concentration changes by single cells},
  journal = {Physical Review Letters},
  volume  = {104},
  number  = {24},
  pages   = {248101},
  year    = {2010},
  doi     = {10.1103/PhysRevLett.104.248101}
}
```
