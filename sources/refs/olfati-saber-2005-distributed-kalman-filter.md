---
type: reference
title: "Distributed Kalman Filter with Embedded Consensus Filters"
aliases: ["olfatisaber2005distributed"]
authors: ["Reza Olfati-Saber"]
year: 2005
venue: "Proceedings of the 44th IEEE Conference on Decision and Control, and the European Control Conference 2005"
doi: "10.1109/CDC.2005.1583486"
url: "https://doi.org/10.1109/CDC.2005.1583486"
tags: [cluster/multi-agent, project/multi-agent, field/cs-ml, field/statistics, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---
# Distributed Kalman Filter with Embedded Consensus Filters

> [!info] Citation
> Olfati-Saber, R. (2005). *Distributed Kalman Filter with Embedded Consensus Filters*. Proceedings of the 44th IEEE Conference on Decision and Control, and the European Control Conference 2005, 8179-8184. IEEE. [DOI](https://doi.org/10.1109/CDC.2005.1583486)

No local copy: no open-access file passed validation on November 10, 2026. Reading basis: abstract and manuscript reading record.

## TL;DR

The paper reduces distributed Kalman filtering for sensor networks to two dynamic consensus problems, on weighted measurements and on inverse-covariance matrices, and shows that a network of micro-Kalman filters then matches the central filter when the nodes agree on two central sums.

## Problem & setting

Distributed Kalman filtering is posed as a basic problem of scalable sensor fusion. The abstract describes low-pass and band-pass consensus filters, which compute average consensus of time-varying signals, with stability treated in a companion paper.

## Key results

The abstract states that a central Kalman filter for a sensor network decomposes into $n$ micro-Kalman filters whose inputs come from two kinds of consensus filter, and that the resulting estimate is identical to the central estimate when all nodes agree on the two sums. It then gives an approximate algorithm in which consensus filters approximate the sums, with a simulation on a network of 200 nodes and more than 1000 links.

## Relevance to this research

The manuscript cites Theorem 1 of this paper as the exact case of inferential closure in a dynamic world: if every member knows the averages of the information matrices and of the weighted measurements at each step, sensing noises are uncorrelated and every member knows $n$, each member's filter reproduces the centralized estimate. It also states that the theorem needs exact average consensus at every step, and compares this with collective beliefs formed as products under consensus with finitely many rounds. The manuscript's reading record says Sections II and III and Theorem 1 were read in the proceedings text; this note rests on the abstract and that record. See [[Kalman filter]], [[Decentralized Bayesian inference]] and [[Conservative information fusion]].

## Cross-links

[[Collective agents literature map]]; [[Kalman filter]]; [[Decentralized Bayesian inference]]; [[Conservative information fusion]]; [[mossel-2016-efficient-bayesian-learning]].

## BibTeX

```bibtex
@inproceedings{olfatisaber2005distributed,
  author    = {Olfati-Saber, Reza},
  title     = {Distributed {Kalman} Filter with Embedded Consensus Filters},
  booktitle = {Proceedings of the 44th IEEE Conference on Decision and Control, and the European Control Conference 2005},
  pages     = {8179--8184},
  publisher = {IEEE},
  year      = {2005},
  doi       = {10.1109/CDC.2005.1583486}
}
```
