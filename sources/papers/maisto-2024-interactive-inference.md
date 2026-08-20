---
type: paper
title: "Interactive inference: a multi-agent model of cooperative joint actions"
aliases:
  - "Maisto et al. 2024 interactive inference"
authors:
  - Maisto, Domenico
  - Donnarumma, Francesco
  - Pezzulo, Giovanni
year: 2024
arxiv: 2210.13113
url: https://arxiv.org/abs/2210.13113
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/social-physics
  - cluster/social-physics/social-influence
  - project/multi-agent
  - project/social-physics
  - field/neuroscience
  - field/psychology
  - field/cs-ml
created: 2026-08-20
---

# Interactive inference: a multi-agent model of cooperative joint actions

> [!info] Citation
> Domenico Maisto, Francesco Donnarumma, and Giovanni Pezzulo (2024). "Interactive inference: a multi-agent model of cooperative joint actions." *IEEE Transactions on Systems, Man, and Cybernetics: Systems*. arXiv: [2210.13113](https://arxiv.org/abs/2210.13113). https://doi.org/10.1109/TSMC.2023.3312585

## TL;DR

Cooperating agents infer a shared task goal from one another's movements while selecting actions that make their own intentions legible. Reciprocal prediction aligns beliefs and policies in leaderless and leader--follower simulations, but the construction remains a model of coupled individual active inference rather than a derivation of one exact population ELBO.

## Problem & setting

The target is joint action when agents must coordinate without direct access to one another's intentions. Each agent maintains beliefs about the common goal and treats the partner's movement as evidence, while its own movement simultaneously changes the partner's evidence.

## Method

Each agent performs active inference over task goals and action plans. Policy selection trades individual movement cost against sensorimotor communication: an action can be favored because it is easier for the partner to interpret. The simulations compare leaderless coordination with a leader--follower case in which only one agent initially knows the goal.

## Key results

The simulations produce convergence of beliefs and coordinated action. A knowledgeable leader can rationally choose a more individually costly but more legible movement, allowing the follower to infer the correct goal. These are model-specific computational results, not a general consistency theorem for reciprocal multi-agent inference.

## Relevance to this research

The paper supplies a mechanistic comparator for the reciprocal observation and action channel of [[Collective active inference]]. It separates coordination through legibility from static attractive belief matching. For MultiAgentELBO, it motivates an experiment in which messages or actions are endogenous evidence while retaining a centralized joint-law oracle to measure whether reciprocal updates double-count that evidence.

## Cross-links

- Concepts: [[Collective active inference]], [[Multi-agent variational free energy]], [[Expected Free Energy]]
- Related sources: [[friston-2024-federated-inference]], [[albarracin-2024-shared-protentions]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{MaistoDonnarummaPezzulo2024Interactive,
  author  = {Maisto, Domenico and Donnarumma, Francesco and Pezzulo, Giovanni},
  title   = {Interactive inference: a multi-agent model of cooperative joint actions},
  journal = {IEEE Transactions on Systems, Man, and Cybernetics: Systems},
  year    = {2024},
  doi     = {10.1109/TSMC.2023.3312585},
  eprint  = {2210.13113},
  archivePrefix = {arXiv}
}
```
