---
type: paper
title: "Factorised Active Inference for Strategic Multi-Agent Interactions"
aliases:
  - "Ruiz-Serra et al. 2025 strategic active inference"
authors:
  - Jaime Ruiz-Serra
  - Patrick Sweeney
  - Michael S. Harré
year: 2025
arxiv: 2411.07362
url: https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2025/pdfs/p1793.pdf
tags:
  - cluster/multi-agent
  - cluster/vfe
  - project/multi-agent
  - field/cs-ml
  - field/economics
  - field/neuroscience
created: 2026-08-10
---

# Factorised Active Inference for Strategic Multi-Agent Interactions

> [!info] Citation
> Ruiz-Serra, J., Sweeney, P., & Harré, M. S. (2025). Factorised Active Inference for Strategic Multi-Agent Interactions. In *Proceedings of the 24th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2025)*, 1793-1802. https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2025/pdfs/p1793.pdf

## TL;DR

The paper combines active inference with iterated general-sum games by giving each agent explicit factorized beliefs about other agents' internal policy states. Numerical two- and three-player experiments track individual and ensemble variational and expected free energies under changing game preferences; in the studied models, ensemble EFE is not necessarily minimized at the aggregate level.

## Problem & setting

Standard single-agent active inference does not specify how a strategic agent should represent several adaptive opponents with potentially competing preferences. The authors study repeated games in which agents infer one another's latent policy tendencies and plan in a joint social context.

## Method

Each agent's generative model factorizes latent states by other agent. Variational inference updates beliefs after observed actions, and expected free energy scores prospective policies. Simulations cover two- and three-player general-sum games and nonstationary transitions between payoff structures.

## Key results

The numerical analysis associates ensemble-level EFE with basins of attraction in games having multiple Nash equilibria and reports that it is not necessarily minimized at the aggregate level. This is a model-specific simulation result, not a general theorem that individual EFE minimization can never induce a collective potential or that all collectives fail to minimize an aggregate objective.

## Relevance to this research

The paper supplies a strategic negative control for [[Collective active inference]]. A future policy extension could compare individual, summed, and explicitly joint EFE while retaining the exact finite ELBO as a separate inference objective. The current MultiAgentELBO code contains no policy variable, action-selection model, game dynamics, or EFE evaluator, so this paper is an experiment comparator rather than evidence about present behavior.

## Cross-links

- Concepts: [[Collective active inference]], [[Expected Free Energy]], [[Active Inference]], [[Multi-agent variational free energy]], [[Theory of Mind]]
- Related sources: [[millidge-2021-whence-expected-free-energy]]

## BibTeX

```bibtex
@inproceedings{ruizserra2025factorised,
  author    = {Ruiz-Serra, Jaime and Sweeney, Patrick and Harré, Michael S.},
  title     = {Factorised Active Inference for Strategic Multi-Agent Interactions},
  booktitle = {Proceedings of the 24th International Conference on Autonomous Agents and Multiagent Systems},
  pages     = {1793--1802},
  year      = {2025},
  url       = {https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2025/pdfs/p1793.pdf}
}
```
