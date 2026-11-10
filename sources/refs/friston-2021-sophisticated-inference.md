---
type: reference
title: "Sophisticated Inference"
aliases: ["friston2021sophisticated"]
authors: ["Karl Friston", "Lancelot Da Costa", "Danijar Hafner", "Casper Hesp", "Thomas Parr"]
year: 2021
venue: "Neural Computation"
doi: "10.1162/neco_a_01351"
url: "https://doi.org/10.1162/neco_a_01351"
tags: [cluster/vfe, cluster/multi-agent, project/multi-agent, field/neuroscience, field/cs-ml]
created: 2026-11-10
updated: 2026-11-10
---
# Sophisticated Inference

> [!info] Citation
> Friston, K., Da Costa, L., Hafner, D., Hesp, C., Parr, T. (2021). *Sophisticated Inference*. Neural Computation 33(3), 713-763. [DOI](https://doi.org/10.1162/neco_a_01351)

[Local PDF](../pdfs/friston-2021-sophisticated-inference.pdf), 46 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper develops a sophisticated form of active inference that uses a recursive form of expected free energy, so that an agent holds beliefs about what it would believe after future actions.

## Problem & setting

The introduction presents active inference as an account of motivated behavior that handles epistemic and pragmatic value together, with schemes such as reinforcement learning and optimal control arising as special cases when one kind of uncertainty is ignored. Sophistication refers to the degree to which an agent has beliefs about beliefs.

## Method

The recursive expected free energy functional implements, in the abstract's words, a deep tree search over actions and outcomes. The search runs over sequences of belief states, not over states. The paper illustrates the scheme with numerical simulations of deep decision problems.

## Key results

The abstract reports competent performance in simulated deep decision problems. The extract does not reach the quantitative results.

## Relevance to this research

The manuscript cites the paper for a contingent act, which a recursive evaluation of expected free energy assumes: later acts are chosen given later beliefs. The manuscript states that it knew the work from its abstract. See [[Expected Free Energy]], [[Active Inference]] and [[Belief Propagation]].

## Cross-links

[[Collective agents literature map]]; [[Expected Free Energy]]; [[Active Inference]]; [[Belief Propagation]]; [[friston-2015-active-inference-epistemic-value]].

## BibTeX

```bibtex
@article{friston2021sophisticated,
  author  = {Friston, Karl and Da Costa, Lancelot and Hafner, Danijar and Hesp, Casper and Parr, Thomas},
  title   = {Sophisticated Inference},
  journal = {Neural Computation},
  volume  = {33},
  number  = {3},
  pages   = {713--763},
  year    = {2021},
  doi     = {10.1162/neco_a_01351}
}
```
