---
type: paper
title: Optimal Kullback-Leibler Aggregation via Information Bottleneck
aliases:
  - Geiger et al. 2013 KL Markov aggregation
authors:
  - Bernhard C. Geiger
  - Tatjana Petrov
  - Gernot Kubin
  - Heinz Koeppl
year: 2013
arxiv: "1304.6603"
url: https://arxiv.org/abs/1304.6603
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - project/multi-agent
  - field/statistics
  - field/cs-ml
  - field/mathematics
status: stable
created: 2026-08-10
updated: 2026-08-10
---

# Optimal Kullback-Leibler Aggregation via Information Bottleneck

> [!info] Citation
> Bernhard C. Geiger, Tatjana Petrov, Gernot Kubin, and Heinz Koeppl. “Optimal Kullback-Leibler Aggregation via Information Bottleneck.” arXiv:1304.6603, 2013; journal version in *IEEE Transactions on Automatic Control* 60(4):1010–1022, 2015. [arXiv](https://arxiv.org/abs/1304.6603); [doi:10.1109/TAC.2014.2364971](https://doi.org/10.1109/TAC.2014.2364971).

## TL;DR

The paper reduces a finite-state Markov chain by partitioning its states and minimizing an information-theoretic surrogate for the KL divergence rate between the projected process and a Markov approximation. The surrogate is computable, tight under lumpability, and leads to an agglomerative information-bottleneck algorithm.

## Problem & setting

A deterministic state map turns a Markov chain into a lower-cardinality stochastic process that is generally not Markov. Directly optimizing the KL divergence rate to a reduced Markov chain is difficult, motivating a tractable objective tied to loss of predictive information.

## Method

The authors construct a Markov approximation of the aggregated process and bound the KL divergence rate by an information-bottleneck quantity. They greedily merge states using an agglomerative scheme designed around that upper bound.

## Key results

- The aggregation objective is an upper bound on the relevant KL divergence rate.
- The bound is tight when the partition is lumpable under the paper’s conditions.
- The proposed information-bottleneck heuristic supplies a practical state-partition algorithm and is evaluated on finite Markov models.

## Relevance to this research

This gives a concrete lossy coarse-graining baseline for agent-state or graph-state reduction. A project experiment can compare its proposed RG/coarse variables against the KL aggregation objective and report when exact lumpability fails rather than calling every compressed transition law “renormalized.”

## Scope limits

The method optimizes a computable upper bound and uses greedy partitioning; it is not an exact global coarse-graining theorem. Tightness under lumpability does not imply a learned partition is lumpable, and KL-rate quality does not establish Blackwell equivalence or a Bayesian natural-gradient semiconjugacy.

## Cross-links

- [[Coarse Graining]]
- [[Statistical experiment comparison and deficiency]]
- [[Sufficient statistics]]
- [[Renormalization-group flow of beliefs]]
- [[geiger-temmel-2013-information-preserving-aggregation]]

## BibTeX

```bibtex
@article{geiger2015optimal,
  title   = {Optimal Kullback--Leibler Aggregation via Information Bottleneck},
  author  = {Geiger, Bernhard C. and Petrov, Tatjana and Kubin, Gernot and Koeppl, Heinz},
  journal = {IEEE Transactions on Automatic Control},
  volume  = {60},
  number  = {4},
  pages   = {1010--1022},
  year    = {2015},
  doi     = {10.1109/TAC.2014.2364971},
  note    = {First circulated as arXiv:1304.6603 in 2013}
}
```
