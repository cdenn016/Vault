---
type: reference
title: "PCA Meets RG"
aliases: ["bradde2017pca"]
authors: ["Serena Bradde", "William Bialek"]
year: 2017
venue: "Journal of Statistical Physics"
doi: "10.1007/s10955-017-1770-6"
url: "https://doi.org/10.1007/s10955-017-1770-6"
tags: [cluster/multi-agent, project/multi-agent, field/physics, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---

# PCA Meets RG

> [!info] Citation
> Bradde, S., Bialek, W. (2017). *PCA Meets RG*. Journal of Statistical Physics, 167(3-4), 462-475. [DOI](https://doi.org/10.1007/s10955-017-1770-6)

[Local PDF](../pdfs/bradde-2017-pca-meets-rg.pdf), 8 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper argues that choosing which principal components of a covariance matrix to keep is analogous to the momentum-shell renormalization group when the eigenvalue spectrum is nearly continuous, and uses the analogy to define relevant and irrelevant operators.

## Problem & setting

A system with many degrees of freedom is summarized by a covariance matrix, and principal components analysis keeps the high-variance eigenmodes. When the spectrum is nearly continuous, the abstract states, the division between kept and discarded modes is arbitrary, so the authors ask what happens as the cutoff varies.

## Method

The cutoff in the spectrum is treated as the arbitrary boundary between explicit and implicit degrees of freedom, as in momentum-shell renormalization. Following the analogy, relevant and irrelevant operators are defined, with the role of dimensionality played by properties of the eigenvalue density. The introduction notes that for lattice systems with translation-invariant interactions the principal components are Fourier modes.

## Key results

According to the abstract, an analysis of neural activity in the vertebrate retina under naturalistic movies shows evidence of behavior controlled by a nontrivial fixed point, and an analysis of financial data separates modes dominated by sampling noise from a smaller number of modes described by a non-Gaussian distribution. These are the authors' results on their own data sets.

## Relevance to this research

The collective-agents manuscript names this paper as a precedent, still to be checked, for Gaussian coarse-graining of interacting units, listed alongside a related coarse-graining paper in its related-work discussion. The reading record says the bibliographic record was checked and the paper was named as a precedent; the note rests on the abstract and introduction in the local file. It connects to the vault's coarse-graining and renormalization material, see [[Coarse Graining]], [[Renormalization group flow]], [[Dimensionality reduction]] and [[Gaussian Beliefs]].

## Cross-links

[[Collective agents literature map]]; [[Coarse Graining]]; [[Renormalization group flow]]; [[Dimensionality reduction]]; [[Gaussian Beliefs]]; [[bialek-2005-physical-limits-biochemical]].

## BibTeX

```bibtex
@article{bradde2017pca,
  author  = {Bradde, Serena and Bialek, William},
  title   = {{PCA} Meets {RG}},
  journal = {Journal of Statistical Physics},
  volume  = {167},
  number  = {3-4},
  pages   = {462--475},
  year    = {2017},
  doi     = {10.1007/s10955-017-1770-6}
}
```
