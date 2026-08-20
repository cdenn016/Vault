---
type: paper
title: "Distributed Variational Inference for Online Supervised Learning"
aliases:
  - "Paritosh et al. 2025 distributed variational inference"
  - "Distributed variational inference online approach"
authors:
  - Paritosh, Parth
  - Atanasov, Nikolay
  - Martinez, Sonia
year: 2025
arxiv: 2309.02606
url: https://doi.org/10.1109/TCNS.2025.3543665
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-08-20
---

# Distributed Variational Inference for Online Supervised Learning

> [!info] Citation
> Parth Paritosh, Nikolay Atanasov, and Sonia Martinez (2025). "Distributed Variational Inference for Online Supervised Learning." *IEEE Transactions on Control of Network Systems*. https://doi.org/10.1109/TCNS.2025.3543665. arXiv: [2309.02606](https://arxiv.org/abs/2309.02606).

## TL;DR

The paper derives a separable distributed evidence lower bound for online supervised learning over sensor networks. Its gap to measurement evidence is explicitly divided into modeling and consensus errors, and one-hop algorithms optimize Gaussian variational approximations for streaming classification and regression.

## Problem & setting

Continuous-variable inference with intractable posteriors and real-time data must run over a sensor network without centralized processing. Nodes communicate only with immediate neighbors.

## Method

A weighted sum of local likelihood terms and prior divergences forms the distributed ELBO. Online distributed Gaussian VI uses efficient rank-one covariance corrections, with a diagonal approximation for high-dimensional models. Multi-robot probabilistic mapping is the principal application.

## Key results

The construction provides an explicit centralized reference and separates consensus from modeling error. Its correctness is tied to the declared bound, weighting, graph, and Gaussian family; it is not an identity for generic peer-posterior matching.

## Relevance to this research

This is the closest algorithmic template for measuring a decentralized gap against an exact ELBO oracle. The decomposition should inform MultiAgentELBO diagnostics: factorization error, communication-consensus error, and gauge-transport error should be reported separately.

## Cross-links

- Concepts: [[Decentralized Bayesian inference]], [[Evidence lower bound (ELBO)]], [[Communication-constrained inference]]
- Related sources: [[hua-li-2016-distributed-variational-bayes]], [[cao-2024-multi-robot-slam-vi]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{ParitoshAtanasovMartinez2025DistributedVI,
  author  = {Paritosh, Parth and Atanasov, Nikolay and Martinez, Sonia},
  title   = {Distributed Variational Inference for Online Supervised Learning},
  journal = {IEEE Transactions on Control of Network Systems},
  year    = {2025},
  doi     = {10.1109/TCNS.2025.3543665},
  eprint  = {2309.02606},
  archivePrefix = {arXiv}
}
```
