---
type: paper
title: "Differentially private partitioned variational inference"
aliases:
  - "Heikkila et al. 2023 DP-PVI"
authors:
  - Heikkila, Mikko A.
  - Ashman, Matthew
  - Swaroop, Siddharth
  - Turner, Richard E.
  - Honkela, Antti
year: 2023
arxiv: 2209.11595
url: https://arxiv.org/abs/2209.11595
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-08-20
---

# Differentially private partitioned variational inference

> [!info] Citation
> Mikko A. Heikkila, Matthew Ashman, Siddharth Swaroop, Richard E. Turner, and Antti Honkela (2023). "Differentially private partitioned variational inference." *Transactions on Machine Learning Research*. arXiv: [2209.11595v2](https://arxiv.org/abs/2209.11595).

## TL;DR

DP-PVI adds formal differential privacy to partitioned variational inference while limiting communication rounds. It studies local-output perturbation and two global-update perturbation schemes, making the privacy--approximation--communication tradeoff explicit.

## Problem & setting

Federated Bayesian learning does not automatically protect individuals merely because raw data stay local. The task is to learn a global variational posterior from distributed sensitive data with an explicit differential-privacy guarantee.

## Method

The authors combine PVI site updates with clipping and noise. One implementation perturbs local optimization, while two perturb global updates, including a federated-averaging-style method and a virtual-client construction. The mechanisms are analyzed and compared empirically.

## Key results

The paper supplies a general differentially private federated-VI framework and explores communication and utility costs. Privacy noise changes the posterior approximation, so the result should not be presented as exact centralized Bayes with an implementation detail added.

## Relevance to this research

This source fixes an important scope boundary for [[Communication-constrained inference]]: decentralization is not privacy. Any privacy extension of MultiAgentELBO should report the formal privacy parameters together with posterior error, calibration, and gauge-sensitive message transformations.

## Cross-links

- Concepts: [[Decentralized Bayesian inference]], [[Communication-constrained inference]], [[Approximate Bayesian inference]]
- Related sources: [[ashman-2022-partitioned-variational-inference]], [[mildner-2025-fedgvi]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{HeikkilaEtAl2023DPPVI,
  author  = {Heikkila, Mikko A. and Ashman, Matthew and Swaroop, Siddharth and Turner, Richard E. and Honkela, Antti},
  title   = {Differentially private partitioned variational inference},
  journal = {Transactions on Machine Learning Research},
  year    = {2023},
  eprint  = {2209.11595},
  archivePrefix = {arXiv}
}
```
