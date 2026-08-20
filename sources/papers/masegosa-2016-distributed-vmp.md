---
type: paper
title: "d-VMP: Distributed Variational Message Passing"
aliases:
  - "Masegosa et al. 2016 d-VMP"
authors:
  - Masegosa, Andres R.
  - Martinez, Ana M.
  - Langseth, Helge
  - Nielsen, Thomas D.
  - Salmeron, Antonio
  - Ramos-Lopez, Dario
  - Madsen, Anders L.
year: 2016
arxiv: null
url: https://proceedings.mlr.press/v52/masegosa16.html
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-08-20
---

# d-VMP: Distributed Variational Message Passing

> [!info] Citation
> Andres R. Masegosa, Ana M. Martinez, Helge Langseth, Thomas D. Nielsen, Antonio Salmeron, Dario Ramos-Lopez, and Anders L. Madsen (2016). "d-VMP: Distributed Variational Message Passing." *Proceedings of the Eighth International Conference on Probabilistic Graphical Models*, PMLR **52**, 321--332. https://proceedings.mlr.press/v52/masegosa16.html

## TL;DR

d-VMP distributes conjugate-exponential variational message passing over map-reduce infrastructure and interprets the updates as projected natural-gradient ascent. It is a scalable compute-cluster method, not a peer-to-peer agent protocol.

## Problem & setting

Large probabilistic graphical models can exceed the memory and processing capacity of one machine. The paper targets conjugate-exponential models whose variational messages can be aggregated across data partitions.

## Method

Projected natural-gradient updates are expressed as map and reduce operations and implemented with Apache Flink. The platform handles partitioning and memory management, while variational-message structure supplies the probabilistic computation.

## Key results

The method is reported to be robust to imbalanced and heavy-tailed data and missing values, and scales to a graph with more than one billion nodes on a 128-unit cluster. Its convergence and scaling claims apply to the specified projected updates and infrastructure, not arbitrary decentralized networks.

## Relevance to this research

d-VMP is a clean control separating distribution of computation from distribution of agency. It belongs in [[Decentralized Bayesian inference]] as a centralized-target, cluster-execution baseline. It does not address reciprocal moving peers, evidence lineage on cyclic graphs, or gauge-frame alignment.

## Cross-links

- Concepts: [[Decentralized Bayesian inference]], [[Variational EM]], [[Natural gradient]]
- Related sources: [[winn-2005-variational-message-passing]], [[hua-li-2016-distributed-variational-bayes]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@inproceedings{MasegosaEtAl2016DVMP,
  author    = {Masegosa, Andres R. and Martinez, Ana M. and Langseth, Helge and Nielsen, Thomas D. and Salmeron, Antonio and Ramos-Lopez, Dario and Madsen, Anders L.},
  title     = {d-VMP: Distributed Variational Message Passing},
  booktitle = {Proceedings of the Eighth International Conference on Probabilistic Graphical Models},
  series    = {Proceedings of Machine Learning Research},
  volume    = {52},
  pages     = {321--332},
  year      = {2016},
  publisher = {PMLR},
  url       = {https://proceedings.mlr.press/v52/masegosa16.html}
}
```
