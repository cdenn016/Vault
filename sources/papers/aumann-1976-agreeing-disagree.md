---
type: paper
title: "Agreeing to Disagree"
aliases:
  - "Aumann 1976 agreement theorem"
authors:
  - Aumann, Robert J.
year: 1976
arxiv: null
url: https://doi.org/10.1214/aos/1176343654
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/economics
  - field/statistics
  - field/mathematics
created: 2026-08-10
---

# Agreeing to Disagree

> [!info] Citation
> Robert J. Aumann (1976). "Agreeing to Disagree." *The Annals of Statistics* 4(6), 1236--1239. DOI: [10.1214/aos/1176343654](https://doi.org/10.1214/aos/1176343654). [Publisher record](https://projecteuclid.org/journals/annals-of-statistics/volume-4/issue-6/Agreeing-to-Disagree/10.1214/aos/1176343654.full).

## TL;DR

If two Bayesian agents have the same prior and their posterior probabilities of an event are common knowledge, then those posterior probabilities are equal. This is an agreement theorem under a common-prior information-partition model, not a theorem that arbitrary communication dynamics converge, that the common posterior is true, or that differently specified agents can safely pool their beliefs.

## Problem & setting

Agents share a probability space and a common prior but observe different information cells. Each posterior for an event is the common prior conditioned on that agent's information. The theorem asks whether unequal posterior probabilities can themselves be common knowledge.

## Method

At a state where posterior values are common knowledge, the common-knowledge event is a union of information cells for each agent. Applying conditional expectation over that event shows that each announced posterior has the same prior-weighted average. Because each value is constant on the event by common knowledge, the announced values must coincide.

## Key results

Under the stated assumptions, common knowledge of the agents' posterior probabilities implies agreement. The proof does not establish that a finite message protocol reaches common knowledge, does not relax the common-prior assumption, and does not imply that agreement identifies the realized state. Equality of posteriors is therefore weaker than posterior accuracy and logically distinct from decentralized Bayesian fusion.

## Relevance to this research

This result supplies the sharp assumption boundary for [[Common knowledge and Bayesian agreement]]. MultiAgentELBO can represent agents with a common generative model, but that alone does not construct Aumann information partitions or make posterior reports common knowledge. Gauge-frame compatibility, consensus of parameter vectors, and Aumann agreement are different conditions and should not be substituted for one another.

## Cross-links

- Concepts: [[Common knowledge and Bayesian agreement]], [[Non-Bayesian social learning]], [[Decentralized Bayesian inference]]
- Related sources: [[jadbabaie-2012-non-bayesian-social-learning]], [[lalitha-2018-distributed-hypothesis-testing]]

## BibTeX

```bibtex
@article{Aumann1976,
  author  = {Aumann, Robert J.},
  title   = {Agreeing to Disagree},
  journal = {The Annals of Statistics},
  volume  = {4},
  number  = {6},
  pages   = {1236--1239},
  year    = {1976},
  doi     = {10.1214/aos/1176343654}
}
```
