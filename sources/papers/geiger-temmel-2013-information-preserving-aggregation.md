---
type: paper
title: Information-Preserving Markov Aggregation
aliases:
  - Geiger Temmel 2013 Markov aggregation
authors:
  - Bernhard C. Geiger
  - Christoph Temmel
year: 2013
arxiv: "1304.0920"
url: https://arxiv.org/abs/1304.0920
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

# Information-Preserving Markov Aggregation

> [!info] Citation
> Bernhard C. Geiger and Christoph Temmel. “Information-Preserving Markov Aggregation.” *2013 IEEE Information Theory Workshop*, pp. 258–262, 2013. [doi:10.1109/ITW.2013.6691265](https://doi.org/10.1109/ITW.2013.6691265); [arXiv:1304.0920](https://arxiv.org/abs/1304.0920).

## TL;DR

The paper gives a sufficient condition under which a noninjective function of a finite-state Markov chain has the same entropy rate as the original chain while becoming a second-order Markov process. It also bounds the attainable reduced alphabet and gives an enumeration procedure.

## Problem & setting

State aggregation normally destroys path information and Markov structure. The authors seek deterministic reductions that preserve entropy rate—hence permit lossless sample-path coding in their information-theoretic sense—while controlling the order of the aggregated process.

## Method

They impose a combinatorial condition on the original transition graph and the aggregation map, analyze preimages of aggregated paths, and derive a reduced process with finite Markov order. Candidate maps can be enumerated using the graph structure.

## Key results

- A stated sufficient condition guarantees entropy-rate preservation.
- Under that condition, the aggregate is second-order Markov even when it is not first-order lumpable.
- Transition-graph degrees yield a lower bound on the reduced-state cardinality, and an algorithm enumerates eligible aggregations.

## Relevance to this research

This is a sharp counterpoint to approximate KL aggregation: exact preservation is possible, but only under explicit structural conditions and possibly at higher Markov order. It suggests tests of entropy rate, preimage ambiguity, and induced memory after an agent-state coarse-graining.

## Scope limits

Equal entropy rate is not the same as Blackwell equivalence, sufficient-statistic recovery for every parameter, or preservation of every decision risk. The sufficient condition is not necessary in general. This proceedings paper must not be conflated with the authors’ later article on higher-order lumpability.

## Cross-links

- [[Coarse Graining]]
- [[Statistical experiment comparison and deficiency]]
- [[geiger-2013-kl-aggregation]]
- [[Sufficient statistics]]

## BibTeX

```bibtex
@inproceedings{geiger2013information,
  title     = {Information-Preserving Markov Aggregation},
  author    = {Geiger, Bernhard C. and Temmel, Christoph},
  booktitle = {2013 IEEE Information Theory Workshop (ITW)},
  pages     = {258--262},
  year      = {2013},
  doi       = {10.1109/ITW.2013.6691265},
  eprint    = {1304.0920},
  archivePrefix = {arXiv}
}
```
