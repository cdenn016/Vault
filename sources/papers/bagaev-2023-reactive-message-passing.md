---
type: paper
title: "Reactive Message Passing for Scalable Bayesian Inference"
aliases:
  - "Bagaev and de Vries 2023 reactive message passing"
  - RMP
authors:
  - Dmitry Bagaev
  - Bert de Vries
year: 2023
arxiv: 2112.13251
url: https://doi.org/10.1155/2023/6601690
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-08-10
---

# Reactive Message Passing for Scalable Bayesian Inference

> [!info] Citation
> Bagaev, D., & de Vries, B. (2023). Reactive Message Passing for Scalable Bayesian Inference. *Scientific Programming*, 2023, Article 6601690, 26 pages. https://doi.org/10.1155/2023/6601690

## TL;DR

Reactive message passing (RMP) replaces a globally fixed message schedule with event-driven reactions to changes at neighboring factor-graph nodes. ReactiveMP.jl implements this architecture while minimizing constrained Bethe free energy and supports hybrid BP, VMP, EP, and EM update rules selected through local form and factorization constraints.

## Problem & setting

Fixed schedules are awkward for streaming observations, changing model structure, sensor failures, and components that update at different rates. The paper seeks a software abstraction that can execute local factor-graph inference without precomputing one global synchronous schedule.

## Method

Nodes expose reactive computations that fire when upstream messages or observations change. The probabilistic semantics come from constrained Bethe free-energy minimization, while the reactive programming layer controls execution. The paper implements the design in Julia and benchmarks it on several probabilistic signal-processing and state-space models.

## Key results

The reported implementation handles selected state-space models containing hundreds of thousands of random variables on a standard laptop and compares favorably with the tested Julia alternatives. These are model- and implementation-specific empirical results. Removing a fixed schedule is not a general convergence guarantee, and a reactive fixed point on a loopy graph need not encode one exact normalized global joint law.

## Relevance to this research

RMP is an architectural comparator for future asynchronous agent or meta-agent updates. [[Belief Propagation]] must still keep semantics and execution separate: unconstrained sum-product BP is exact on trees, whereas constrained VMP/EP hybrids can be approximate even on trees and Bethe beliefs on loops can be nonrealizable. The present MultiAgentELBO code has no reactive message engine; adding one would be an explicitly approximate and separately tested layer.

## Cross-links

- Concepts: [[Belief Propagation]], [[Mean-Field Approximation]], [[Multi-agent variational free energy]], [[Collective active inference]]
- Related sources: [[senoz-2021-local-constraint-vmp]], [[heskes-2006-bethe-kikuchi-convexity]]

## BibTeX

```bibtex
@article{bagaev2023reactive,
  author  = {Bagaev, Dmitry and de Vries, Bert},
  title   = {Reactive Message Passing for Scalable Bayesian Inference},
  journal = {Scientific Programming},
  volume  = {2023},
  pages   = {6601690},
  year    = {2023},
  doi     = {10.1155/2023/6601690}
}
```
