---
type: reference
title: "Aggregation and long memory: recent developments"
aliases: ["leipus2013aggregation"]
authors: ["Remigijus Leipus", "Anne Philippe", "Donata Puplinskaitė", "Donatas Surgailis"]
year: 2013
arxiv: "1306.3301"
url: "https://arxiv.org/abs/1306.3301"
tags: [cluster/multi-agent, project/multi-agent, field/statistics, field/economics]
created: 2026-11-10
updated: 2026-11-10
---
# Aggregation and long memory: recent developments

> [!info] Citation
> Leipus, R., Philippe, A., Puplinskaitė, D., Surgailis, D. (2013). *Aggregation and long memory: recent developments*. Preprint. [arXiv](https://arxiv.org/abs/1306.3301)

[Local PDF](../pdfs/leipus-2013-aggregation-long-memory.pdf), 19 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and abstract.

## TL;DR

A review of contemporaneous aggregation of random-coefficient AR(1) and related models, with attention to the long memory that the aggregated series can have although each individual series does not.

## Problem & setting

The introduction starts from Granger's observation that an AR(1) process whose coefficient is random with a Beta-type law can have a covariance that decays as slowly as in long-memory processes. It then considers a large heterogeneous population of independent micro-agents, each following an AR(1) with its own coefficient, whose average gives the aggregate variable. The condition on the coefficient's density near the unit root is that it behaves like a power of $1-x$ with exponent $\beta>-1$.

## Key results

For $0<\beta<1$ the introduction gives the covariance of the stationary solution decaying like $t^{-\beta}$. The extract does not reach the later sections on infinite variance, scaling limits and anisotropic models, which the abstract lists.

## Relevance to this research

The manuscript cites this review, together with Granger's 1980 paper, for the known route by which averaging uncoupled members with differing persistence yields long memory in the aggregate. Its reading record says the first two sections were read and that Granger's paper, known only through this review, was not opened. The result is a known form that the manuscript recovers for the aggregate of uncoupled members. It connects to [[Coarse Graining]] and to [[Meta-agents and hierarchical emergence]], where a collective variable averages members with different time scales.

## Cross-links

[[Collective agents literature map]]; [[Coarse Graining]]; [[Meta-agents and hierarchical emergence]].

## BibTeX

```bibtex
@misc{leipus2013aggregation,
  author        = {Leipus, Remigijus and Philippe, Anne and Puplinskait{\.e}, Donata and Surgailis, Donatas},
  title         = {Aggregation and long memory: recent developments},
  year          = {2013},
  eprint        = {1306.3301},
  archivePrefix = {arXiv},
  note          = {Preprint}
}
```
