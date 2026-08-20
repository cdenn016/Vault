---
type: paper
title: "Distributed Variational Bayesian Algorithms Over Sensor Networks"
aliases:
  - "Hua and Li 2016 distributed variational Bayes"
authors:
  - Hua, Junhao
  - Li, Chunguang
year: 2016
arxiv: 2011.13600
url: https://doi.org/10.1109/TSP.2015.2493979
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/statistics
  - field/cs-ml
created: 2026-08-20
---

# Distributed Variational Bayesian Algorithms Over Sensor Networks

> [!info] Citation
> Junhao Hua and Chunguang Li (2016). "Distributed Variational Bayesian Algorithms Over Sensor Networks." *IEEE Transactions on Signal Processing*. https://doi.org/10.1109/TSP.2015.2493979. arXiv: [2011.13600](https://arxiv.org/abs/2011.13600).

## TL;DR

The paper develops two distributed variational-Bayes algorithms for conjugate-exponential models: stochastic natural-gradient updates followed by information diffusion, and a natural-parameter consensus problem solved by ADMM. Performance close to centralized VB is empirical, not an exact equality.

## Problem & setting

Sensor nodes hold distributed observations and cannot send all raw data to a fusion center. The goal is to approximate the same Bayesian model collaboratively while retaining local computation and neighbor communication.

## Method

One method updates global natural parameters with stochastic natural gradients on the variational manifold and then diffuses information across neighbors. The second writes equality constraints among local natural parameters and applies alternating-direction optimization. Gaussian-mixture inference provides the worked application.

## Key results

Synthetic and real-data experiments report estimates almost as accurate as centralized VB. The algorithms require conjugate-exponential structure and network consensus; the empirical comparison does not establish exact posterior recovery or rule out evidence recycling on arbitrary schedules.

## Relevance to this research

This is a direct algorithmic baseline for [[Decentralized Bayesian inference]] and for natural-parameter communication. Its centralized comparison should be mirrored by the MultiAgentELBO exact oracle. The natural gradient is statistical optimization, while gauge transport is a separate coordinate operation that must be applied consistently before parameter consensus.

## Cross-links

- Concepts: [[Decentralized Bayesian inference]], [[Natural gradient]], [[Variational free energy]]
- Related sources: [[masegosa-2016-distributed-vmp]], [[paritosh-2025-distributed-variational-inference]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{HuaLi2016DistributedVB,
  author  = {Hua, Junhao and Li, Chunguang},
  title   = {Distributed Variational Bayesian Algorithms Over Sensor Networks},
  journal = {IEEE Transactions on Signal Processing},
  year    = {2016},
  doi     = {10.1109/TSP.2015.2493979},
  eprint  = {2011.13600},
  archivePrefix = {arXiv}
}
```
