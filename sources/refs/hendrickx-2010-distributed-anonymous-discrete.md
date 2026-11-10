---
type: reference
title: "Distributed anonymous discrete function computation"
aliases: ["hendrickx2010distributed"]
authors: ["Julien M. Hendrickx", "Alex Olshevsky", "John N. Tsitsiklis"]
year: 2010
arxiv: "1004.2102"
url: "https://arxiv.org/abs/1004.2102"
tags: [cluster/multi-agent, project/multi-agent, field/cs-ml, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---

# Distributed anonymous discrete function computation

> [!info] Citation
> Hendrickx, J. M., Olshevsky, A., Tsitsiklis, J. N. (2010). *Distributed anonymous discrete function computation*. arXiv:1004.2102. [arXiv](https://arxiv.org/abs/1004.2102)

[Local PDF](../pdfs/hendrickx-2010-distributed-anonymous-discrete.pdf), 33 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and abstract.

## TL;DR

The paper defines a model of deterministic computation by a network of identical, anonymous nodes with bounded memory that know only their own neighbors, and characterizes which functions of the nodes' initial values such a network can compute. Computing suitably rounded averages is the central subproblem.

## Problem & setting

Each node is a finite automaton that exchanges messages on a fixed bidirectional network. Nodes have no global identifiers (only private labels for their own neighbors), no randomization, no knowledge of the network size or topology, and memory that does not grow with the network. The motivating tasks are quantized consensus, distributed majority voting, direction coordination on a ring, and solitude verification.

## Method

The authors give a necessary condition for computability and show it is nearly sufficient: functions that violate it can at least be approximated. For averaging they provide an algorithm whose running time grows quadratically with the network size.

## Key results

The main result is the necessary condition just described, together with the averaging algorithm. The evidence read here (abstract and introduction) does not state further quantitative results.

## Relevance to this research

The manuscript cites this paper in its appendix on privacy to state what identical deterministic nodes without identifiers can compute on graphs with labeled ports when inputs come from a finite set: with one algorithm for all network sizes, the computable functions depend only on the frequencies of the input values. It is a reference for the limits of anonymous distributed computation, related to [[Decentralized Bayesian inference]] and [[Communication-constrained inference]] among communicating agents.

## Cross-links

[[Collective agents literature map]]; [[Decentralized Bayesian inference]]; [[Communication-constrained inference]].

## BibTeX

```bibtex
@misc{hendrickx2010distributed,
  author = {Hendrickx, Julien M. and Olshevsky, Alex and Tsitsiklis, John N.},
  title = {Distributed anonymous discrete function computation},
  year = {2010},
  eprint = {1004.2102},
  archivePrefix = {arXiv},
  note = {arXiv:1004.2102}
}
```
