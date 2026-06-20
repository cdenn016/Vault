---
type: reference
title: "Agglomerative Information Bottleneck"
aliases:
  - "Slonim & Tishby 2000"
  - "Agglomerative Information Bottleneck"
authors:
  - Noam Slonim
  - Naftali Tishby
year: 2000
url: https://papers.nips.cc/paper/1651-agglomerative-information-bottleneck
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-06-19
updated: 2026-06-19
---

# Agglomerative Information Bottleneck

> [!info] Citation
> Noam Slonim and Naftali Tishby (2000). "Agglomerative Information Bottleneck." *Advances in Neural Information Processing Systems* 12 (NIPS 1999), pp. 617–623. <https://papers.nips.cc/paper/1651-agglomerative-information-bottleneck>

## TL;DR

A greedy, bottom-up ("agglomerative") solver for the [[Information bottleneck]]: start with every data point in its own cluster and repeatedly **merge the pair whose merger loses the least relevant information** $I(T;Y)$, building a hierarchy of progressively coarser representations. It is the hard, hierarchical counterpart to the soft top-down IB, with the merge cost given by a Jensen-Shannon-like information loss.

## TL;DR relevance

This is the coarse-graining cousin of PIFB's ([[participatory-it-from-bit]]) **meta-agent formation**. Building a scale-$s{+}1$ agent by pooling a cluster of scale-$s$ agents is, in information terms, an agglomerative merge that should preserve the relevant (predictive) information while compressing detail — exactly the merge-by-least-information-loss criterion Slonim & Tishby formalize. The bottom-up hierarchy of clusters is the algorithmic shadow of the project's tower of [[Meta-agents and hierarchical emergence]] and its [[Renormalization-group flow of beliefs]]. Cited as the agglomerative IB precedent for relevance-preserving coarse-graining; see also the deterministic hard-clustering limit ([[strouse-2017-deterministic-ib]]) and the founding IB ([[tishby-1999-information-bottleneck]]).

```bibtex
@inproceedings{slonim2000agglomerative,
  title     = {Agglomerative Information Bottleneck},
  author    = {Slonim, Noam and Tishby, Naftali},
  booktitle = {Advances in Neural Information Processing Systems 12 (NIPS)},
  pages     = {617--623},
  year      = {2000},
  url       = {https://papers.nips.cc/paper/1651-agglomerative-information-bottleneck}
}
```
