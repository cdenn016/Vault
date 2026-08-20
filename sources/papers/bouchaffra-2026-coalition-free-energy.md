---
type: paper
title: "Coalition Free Energy and Adaptive Precision in Multi-Agent Cooperation"
aliases:
  - "Bouchaffra et al. 2026 coalition free energy"
authors:
  - Bouchaffra, Djamel
  - Ykhlef, Faycal
  - Lebbah, Mustapha
  - Azzag, Hanane
year: 2026
arxiv: 2605.26278
url: https://arxiv.org/abs/2605.26278
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/social-physics
  - cluster/social-physics/evolutionary-and-cultural
  - project/multi-agent
  - project/social-physics
  - field/cs-ml
  - field/economics
  - field/statistics
created: 2026-08-20
---

# Coalition Free Energy and Adaptive Precision in Multi-Agent Cooperation

> [!info] Citation
> Djamel Bouchaffra, Faycal Ykhlef, Mustapha Lebbah, and Hanane Azzag (2026). "Coalition Free Energy and Adaptive Precision in Multi-Agent Cooperation." arXiv: [2605.26278v1](https://arxiv.org/abs/2605.26278). Preprint.

> [!warning] Preprint status
> This recent manuscript has not been peer reviewed. Its theoretical and empirical claims are recorded as author claims pending independent assessment.

## TL;DR

The paper uses a Gibbs distribution over coalitions to connect free energy, cooperative credit assignment, Shapley values, and adaptive observation precision. An online controller adjusts precision from local cooperative contribution estimates and is evaluated on traffic trajectories and a derived multi-agent control task.

## Problem & setting

Cooperative agents must assign credit under uncertain observations. Too little precision produces noisy inference, while excessive local confidence can reduce effective cooperation. The authors seek a variational account of this tradeoff.

## Method

Coalition structures are weighted by a free-energy distribution. Precision-dependent cooperative contributions yield Shapley values, and Adaptive Precision Control changes observation precision online using locally estimated contribution.

## Key results

The authors report a nonmonotonic precision--influence relation and performance near the best fixed precision without prior tuning on Swiss roundabout data and a multi-agent control task. The connection to a normalized Bayesian posterior and the generality of the coalition representation remain subjects for independent review.

## Relevance to this research

The paper is a direct comparator for adaptive precision in [[Precision weighting]] and coalition-level [[Meta-agents and hierarchical emergence]]. Its credit assignment should not be conflated with the project's attention weights or exact ELBO without matching probabilistic inventories and normalization.

## Cross-links

- Concepts: [[Multi-agent variational free energy]], [[Precision weighting]], [[Meta-agents and hierarchical emergence]]
- Related sources: [[bouchaffra-2026-collective-variational-principle]], [[bouchaffra-2026-attention-synergy]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@misc{BouchaffraEtAl2026CoalitionFreeEnergy,
  author        = {Bouchaffra, Djamel and Ykhlef, Faycal and Lebbah, Mustapha and Azzag, Hanane},
  title         = {Coalition Free Energy and Adaptive Precision in Multi-Agent Cooperation},
  year          = {2026},
  eprint        = {2605.26278},
  archivePrefix = {arXiv},
  primaryClass  = {cs.GT}
}
```
