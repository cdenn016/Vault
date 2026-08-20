---
type: paper
title: "Partitioned Variational Inference: A Framework for Probabilistic Federated Learning"
aliases:
  - "Ashman et al. 2022 PVI"
  - "Partitioned variational inference"
authors:
  - Ashman, Matthew
  - Bui, Thang D.
  - Nguyen, Cuong V.
  - Markou, Stratis
  - Weller, Adrian
  - Swaroop, Siddharth
  - Turner, Richard E.
year: 2022
arxiv: 2202.12275
url: https://arxiv.org/abs/2202.12275
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/statistics
  - field/cs-ml
created: 2026-08-20
---

# Partitioned Variational Inference: A Framework for Probabilistic Federated Learning

> [!info] Citation
> Matthew Ashman, Thang D. Bui, Cuong V. Nguyen, Stratis Markou, Adrian Weller, Siddharth Swaroop, and Richard E. Turner (2022). "Partitioned Variational Inference: A Framework for Probabilistic Federated Learning." arXiv: [2202.12275v4](https://arxiv.org/abs/2202.12275).

## TL;DR

Partitioned variational inference represents a global variational approximation through local site factors associated with data partitions. Scheduled site updates provide a probabilistic federated-learning framework that unifies several continual and distributed variational algorithms.

## Problem & setting

Federated data owners need a shared probabilistic model without centralizing raw observations. Point-estimate federated learning does not retain posterior uncertainty, while naive posterior aggregation loses the connection between local evidence and the global target.

## Method

The global approximation is written as a prior multiplied by approximate local likelihood factors. A client forms a cavity by removing its current site, performs a local variational update, and returns a revised site contribution. Different schedules and local objectives recover multiple existing algorithms.

## Key results

The paper proves structural properties of PVI, develops a unifying view of related algorithms, and reports empirical performance in several federated settings. Exactness still depends on the approximation family and update assumptions; the framework makes the target and factor ownership explicit rather than promising generic centralized-posterior recovery.

## Relevance to this research

PVI is the most direct external template for a decentralized layer around the MultiAgentELBO oracle. Factor IDs, owners, priors, and versions correspond to site bookkeeping. A gauge-aware version would have to transport sufficient statistics or site factors consistently without turning frame alignment into duplicated evidence.

## Cross-links

- Concepts: [[Decentralized Bayesian inference]], [[Communication-constrained inference]], [[Evidence lower bound (ELBO)]]
- Related sources: [[vehtari-2020-ep-partitioned-data]], [[heikkila-2023-dp-partitioned-vi]], [[mildner-2025-fedgvi]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@misc{AshmanEtAl2022PVI,
  author        = {Ashman, Matthew and Bui, Thang D. and Nguyen, Cuong V. and Markou, Stratis and Weller, Adrian and Swaroop, Siddharth and Turner, Richard E.},
  title         = {Partitioned Variational Inference: A Framework for Probabilistic Federated Learning},
  year          = {2022},
  eprint        = {2202.12275},
  archivePrefix = {arXiv},
  primaryClass  = {stat.ML}
}
```
