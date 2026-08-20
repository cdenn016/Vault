---
type: paper
title: "Multi-Robot Object SLAM Using Distributed Variational Inference"
aliases:
  - "Cao et al. 2024 distributed variational SLAM"
authors:
  - Cao, Hanwen
  - Shreedharan, Sriram
  - Atanasov, Nikolay
year: 2024
arxiv: 2404.18331
url: https://doi.org/10.1109/LRA.2024.3451389
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-08-20
---

# Multi-Robot Object SLAM Using Distributed Variational Inference

> [!info] Citation
> Hanwen Cao, Sriram Shreedharan, and Nikolay Atanasov (2024). "Multi-Robot Object SLAM Using Distributed Variational Inference." *IEEE Robotics and Automation Letters* **9**(10), 8722--8729. https://doi.org/10.1109/LRA.2024.3451389. arXiv: [2404.18331](https://arxiv.org/abs/2404.18331).

## TL;DR

Multi-robot object SLAM is posed as variational inference over a communication graph with consensus constraints on shared object estimates. Distributed mirror descent and a Gaussian specialization produce a scalable distributed MSCKF without a central server.

## Problem & setting

Robot teams need a common map and frame of reference, but centralized SLAM introduces communication bottlenecks and a single point of failure. Each robot maintains local trajectory and object estimates while communicating opportunistically with neighbors.

## Method

The authors derive a variational objective with consensus regularization and solve it using distributed mirror descent. A Gaussian realization yields a distributed multi-state constraint Kalman filter for object-level SLAM.

## Key results

Real and simulated experiments improve trajectory and object estimates over individual-robot SLAM and scale better than a centralized multi-robot comparison. The result is an application-specific approximation under Gaussian and graph-consensus assumptions, not exact distributed Bayes.

## Relevance to this research

This paper provides a concrete robotics benchmark for [[Decentralized Bayesian inference]] with shared reference-frame semantics. Its frame alignment is geometric but application-specific; it should not be identified with the project's internal statistical gauge without a typed map. The centralized and single-robot baselines are useful experimental controls.

## Cross-links

- Concepts: [[Decentralized Bayesian inference]], [[Communication-constrained inference]], [[Gauge transformation]]
- Related sources: [[paritosh-2025-distributed-variational-inference]], [[campbell-how-2014-decentralized-bayes]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{CaoShreedharanAtanasov2024DistributedSLAM,
  author  = {Cao, Hanwen and Shreedharan, Sriram and Atanasov, Nikolay},
  title   = {Multi-Robot Object {SLAM} Using Distributed Variational Inference},
  journal = {IEEE Robotics and Automation Letters},
  volume  = {9},
  number  = {10},
  pages   = {8722--8729},
  year    = {2024},
  doi     = {10.1109/LRA.2024.3451389},
  eprint  = {2404.18331},
  archivePrefix = {arXiv}
}
```
