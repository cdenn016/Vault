---
type: paper
title: "Frequentist Guarantees of Distributed (Non)-Bayesian Inference"
aliases:
  - "Wu and Uribe 2025 distributed inference guarantees"
authors:
  - Wu, Bohan
  - Uribe, Cesar A.
year: 2025
arxiv: null
url: https://www.jmlr.org/papers/v26/23-1504.html
tags:
  - cluster/multi-agent
  - cluster/vfe
  - project/multi-agent
  - field/statistics
  - field/mathematics
  - field/cs-ml
created: 2026-08-20
---

# Frequentist Guarantees of Distributed (Non)-Bayesian Inference

> [!info] Citation
> Bohan Wu and Cesar A. Uribe (2025). "Frequentist Guarantees of Distributed (Non)-Bayesian Inference." *Journal of Machine Learning Research* **26**(168), 1--65. https://www.jmlr.org/papers/v26/23-1504.html

## TL;DR

The paper establishes posterior consistency, asymptotic normality, and contraction rates for networked distributed Bayesian and non-Bayesian updates under explicit graph and statistical assumptions. It quantifies how graph design trades communication efficiency against statistical contraction.

## Problem & setting

Agents observe decentralized data and update beliefs over a common parameter through network communication. The question is whether the resulting distributed posterior-like objects retain standard frequentist guarantees and parametric efficiency.

## Method

The analysis treats fixed and time-varying graphs, derives contraction and asymptotic-normality results, and applies them to exponential families, distributed logistic regression, and decentralized detection. Connectivity and graph size enter the rates.

## Key results

Under the paper's assumptions, distributed inference can retain parametric efficiency and robust uncertainty quantification. Communication topology affects posterior contraction, so network consensus and statistical correctness cannot be evaluated by the same scalar diagnostic.

## Relevance to this research

This source supplies asymptotic benchmarks for [[Decentralized Bayesian inference]]. MultiAgentELBO's exact finite oracle and these large-sample guarantees answer different questions. A future distributed implementation should separately report consensus disagreement, error to the centralized target, calibration, and communication cost.

## Cross-links

- Concepts: [[Decentralized Bayesian inference]], [[Non-Bayesian social learning]], [[Communication-constrained inference]]
- Related sources: [[lalitha-2018-distributed-hypothesis-testing]], [[jadbabaie-2012-non-bayesian-social-learning]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{WuUribe2025DistributedGuarantees,
  author  = {Wu, Bohan and Uribe, Cesar A.},
  title   = {Frequentist Guarantees of Distributed (Non)-Bayesian Inference},
  journal = {Journal of Machine Learning Research},
  volume  = {26},
  number  = {168},
  pages   = {1--65},
  year    = {2025},
  url     = {https://www.jmlr.org/papers/v26/23-1504.html}
}
```
