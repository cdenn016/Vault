---
type: paper
title: "Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments"
aliases:
  - "lowe-2017-maddpg"
  - "lowe2017multi"
  - "MADDPG"
  - "Lowe 2017"
authors:
  - "Lowe, R."
  - "Wu, Y."
  - "Tamar, A."
  - "Harb, J."
  - "Abbeel, P."
  - "Mordatch, I."
year: 2017
url: https://arxiv.org/abs/1706.02275
venue: "NeurIPS 2017"
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/cs-ml
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments

> [!info] Citation
> Lowe, R., Wu, Y., Tamar, A., Harb, J., Abbeel, P., Mordatch, I. (2017). "Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments." NeurIPS 2017. https://arxiv.org/abs/1706.02275

## TL;DR
Introduces MADDPG, a multi-agent deep deterministic policy-gradient method using centralized critics with decentralized actors. Each agent learns a critic conditioned on all agents' observations and actions, stabilizing learning in mixed cooperative-competitive settings where the environment is non-stationary from any single agent's view.

## Relevance to this research
A canonical multi-agent reinforcement-learning baseline relevant to the MAgent multi-agent VFE model: it exemplifies the centralized-training / decentralized-execution paradigm and the non-stationarity problem that arises when many learning agents interact, which the gauge-theoretic multi-agent framework reframes through coupled belief dynamics.

## Cross-links
[[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX
```bibtex
@inproceedings{lowe2017multi,
  title={Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments},
  author={Lowe, Ryan and Wu, Yi and Tamar, Aviv and Harb, Jean and Abbeel, Pieter and Mordatch, Igor},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2017}
}
```
