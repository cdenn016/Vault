---
type: paper
title: "Collective predictive coding hypothesis: symbol emergence as decentralized Bayesian inference"
aliases:
  - "Taniguchi 2024 collective predictive coding"
  - "CPC hypothesis"
authors:
  - Taniguchi, Tadahiro
year: 2024
arxiv: null
url: https://doi.org/10.3389/frobt.2024.1353870
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/social-physics
  - cluster/social-physics/social-influence
  - project/multi-agent
  - project/social-physics
  - field/cs-ml
  - field/neuroscience
  - field/sociology
created: 2026-08-20
---

# Collective predictive coding hypothesis: symbol emergence as decentralized Bayesian inference

> [!info] Citation
> Tadahiro Taniguchi (2024). "Collective predictive coding hypothesis: symbol emergence as decentralized Bayesian inference." *Frontiers in Robotics and AI* **11**, 1353870. https://doi.org/10.3389/frobt.2024.1353870

## TL;DR

The collective predictive coding hypothesis treats symbol emergence as decentralized Bayesian inference over latent representations shared by agents. It connects naming-game algorithms, predictive coding, and the free-energy principle, but the society-wide free-energy claim is proposed as a hypothesis rather than derived as a general normalized joint objective.

## Problem & setting

Individual agents learn internal representations through sensorimotor experience while a population develops an external symbol system through communication. The paper asks how these micro- and macro-level processes jointly encode knowledge that no individual directly owns.

## Method

The article synthesizes probabilistic symbol-emergence models, especially Metropolis--Hastings naming games, into the CPC hypothesis. A shared latent symbol variable integrates distributed sensory evidence, and decentralized communication is interpreted as posterior inference over that variable.

## Key results

The paper identifies constructive naming-game models in which decentralized interaction targets a shared posterior and maps them to predictive-coding and free-energy language. It is primarily a hypothesis-and-theory synthesis. It does not prove that every symbol-emergence system minimizes a society-level variational free energy.

## Relevance to this research

CPC supplies a concrete shared-latent alternative to direct pairwise belief matching. It suggests that a multi-agent ELBO should declare the shared representation and its evidence factors explicitly, then compare decentralized messages with the centralized posterior. The distinction between a shared symbol label and a continuous gauge frame must remain typed.

## Cross-links

- Concepts: [[Collective active inference]], [[Decentralized Bayesian inference]], [[Multi-agent variational free energy]]
- Related sources: [[hoang-2024-mh-naming-game]], [[fukuoka-2026-variational-bayes-naming-game]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{Taniguchi2024CollectivePredictiveCoding,
  author  = {Taniguchi, Tadahiro},
  title   = {Collective predictive coding hypothesis: symbol emergence as decentralized Bayesian inference},
  journal = {Frontiers in Robotics and AI},
  volume  = {11},
  pages   = {1353870},
  year    = {2024},
  doi     = {10.3389/frobt.2024.1353870}
}
```
