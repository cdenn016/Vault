---
type: reference
title: "Finite Markov Chains"
aliases:
  - "Kemeny Snell 1960"
  - "lumpability"
authors:
  - Kemeny J.G.
  - Snell J.L.
year: 1960
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
  - field/statistics
created: 2026-08-17
updated: 2026-08-17
---

# Finite Markov Chains

> [!info] Citation
> J.G. Kemeny, J.L. Snell (1960). *Finite Markov Chains.* Van Nostrand, Princeton, NJ. 210 pp.
> Lumpability: §6.3, Theorem 6.3.2.

## TL;DR

The standard reference for **lumpability**: a Markov chain is lumpable with respect to a state
partition exactly when, for every block, the probability of moving into each block is the same
from every state inside it (Theorem 6.3.2). Lumpability is an exceptional condition — generic
chains coarse-grained over generic partitions are not Markov in the lumped states.

## Relevance to this research

The probabilistic cousin of the C3 result: exact closure of a coarse-graining on a declared
model class is an exceptional structural condition, not a default. The laboratory's downward
kernels are not closed under Bayes composition across levels for the same generic reason lumped
chains are not Markov — and any semigroup-restoration design (a kernel family closed under
composition) will be, in effect, an engineered lumpability condition. See
[[Staged hierarchy formation and RG composability]] and [[Coarse Graining]].

## BibTeX

```bibtex
@book{kemeny1960finite,
  author    = {Kemeny, John G. and Snell, J. Laurie},
  title     = {Finite Markov Chains},
  publisher = {Van Nostrand},
  address   = {Princeton, NJ},
  year      = {1960}
}
```
