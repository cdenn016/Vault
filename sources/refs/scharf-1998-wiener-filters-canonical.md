---
type: reference
title: "Wiener filters in canonical coordinates for transform coding, filtering, and quantizing"
aliases: ["scharf1998wiener"]
authors: ["Louis L. Scharf", "John K. Thomas"]
year: 1998
venue: "IEEE Transactions on Signal Processing"
doi: "10.1109/78.661332"
url: "https://doi.org/10.1109/78.661332"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/statistics, field/cs-ml]
created: 2026-11-10
updated: 2026-11-10
---

# Wiener filters in canonical coordinates for transform coding, filtering, and quantizing

> [!info] Citation
> Scharf, L. L., Thomas, J. K. (1998). *Wiener filters in canonical coordinates for transform coding, filtering, and quantizing*. IEEE Transactions on Signal Processing, 46(3), 647-654. [DOI](https://doi.org/10.1109/78.661332)

[Local PDF](../pdfs/scharf-1998-wiener-filters-canonical.pdf), 8 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and manuscript reading record.

## TL;DR

Canonical correlations decompose the Wiener filter into a whitening transform coder, a canonical filter and a coloring decoder, and the resulting canonical coordinates are the ones reduced in rank and quantized in a finite-precision version of the Gauss-Markov theorem.

## Problem & setting

The introduction frames canonical correlations, which are cosines of canonical angles between a source vector and a measurement vector, as a minimal description of the correlation between the two. The concrete motivation is that they determine how a Wiener filter can be reduced in rank and quantized.

## Method

The singular value decomposition of a coherence matrix gives the decomposition: right singular vectors define the whitening coder that yields canonical measurement coordinates, the singular values act as a diagonal canonical Wiener filter, and left singular vectors define the coloring decoder. The filter is reduced in rank by purging measurement coordinates with small squared canonical correlation to the source coordinates, and quantization is applied to the canonical coordinates independently.

## Key results

The abstract states new formulas for error covariance, spectral flatness and entropy. According to the manuscript's reading record, Section V poses the minimization of the trace of the error covariance under a bit constraint, discards weakly correlated canonical measurement coordinates, and states that a single slicing level fixes the bit allocation, the rank and the minimum distortion. Displayed equations did not extract and were not read.

## Relevance to this research

The manuscript cites the paper as an existing joint treatment of rank reduction and a rate budget in canonical coordinates, and does not claim priority for combining a channel cap with a budget. This ties to the manuscript's sensing environments and aggregate memory; see [[Canonical Correlation Analysis]], [[Information bottleneck]], [[Communication-constrained inference]] and [[Channel Capacity]].

## Cross-links

[[Collective agents literature map]]; [[Canonical Correlation Analysis]]; [[Information bottleneck]]; [[Communication-constrained inference]]; [[sachdeva-2021-optimal-prediction-resource]].

## BibTeX

```bibtex
@article{scharf1998wiener,
  author  = {Scharf, Louis L. and Thomas, John K.},
  title   = {Wiener filters in canonical coordinates for transform coding, filtering, and quantizing},
  journal = {IEEE Transactions on Signal Processing},
  volume  = {46},
  number  = {3},
  pages   = {647--654},
  year    = {1998},
  doi     = {10.1109/78.661332}
}
```
