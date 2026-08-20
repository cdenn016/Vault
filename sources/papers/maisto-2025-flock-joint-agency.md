---
type: paper
title: "What the flock knows that the birds do not: exploring the emergence of joint agency in multi-agent active inference"
aliases:
  - "Maisto et al. 2025 flock joint agency"
authors:
  - Maisto, Domenico
  - Nuzzi, Davide
  - Pezzulo, Giovanni
year: 2025
arxiv: 2511.10835
url: https://arxiv.org/abs/2511.10835
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/social-physics
  - cluster/social-physics/social-influence
  - project/multi-agent
  - project/social-physics
  - field/neuroscience
  - field/biology
  - field/cs-ml
  - field/mathematics
created: 2026-08-20
---

# What the flock knows that the birds do not: exploring the emergence of joint agency in multi-agent active inference

> [!info] Citation
> Domenico Maisto, Davide Nuzzi, and Giovanni Pezzulo (2025). "What the flock knows that the birds do not: exploring the emergence of joint agency in multi-agent active inference." arXiv: [2511.10835v2](https://arxiv.org/abs/2511.10835). Preprint, revised 2026-01-29.

## TL;DR

A simulated flock of reciprocally coupled active-inference agents develops a higher-order statistical boundary, coordinated predator responses, and synergistic information unavailable to every individual. These are numerical and information-theoretic findings from one model, not a general emergence theorem.

## Problem & setting

The paper asks when a collection acquires agency or knowledge not reducible to any one member. Each bird minimizes its own free energy while coupling to neighbors; an external predator provides a perturbation against which collective sensitivity can be tested.

## Method

The authors simulate flocking active-inference dynamics, identify candidate group-level sensory, active, and internal states, and test conditional-dependence structure for a higher-order Markov blanket. Information decomposition is used to quantify whether the population jointly encodes predator location beyond individual access.

## Key results

The model produces a candidate flock-level blanket, faster coordinated responses than isolated agents, and positive synergistic information about the perturbation. Because the evidence is model- and estimator-dependent, it does not show that reciprocal active inference generically produces a group agent or prove an equality between group and individual free energies.

## Relevance to this research

The paper joins [[Meta-agents and hierarchical emergence]] to [[Partial information decomposition]]. It provides a direct empirical comparator for claims that a block carries new information. MultiAgentELBO should reproduce blanket detection and synergy estimates under null models, alternative partitions, and estimator choices before using them as evidence of a meta-agent.

## Cross-links

- Concepts: [[Collective active inference]], [[Meta-agents and hierarchical emergence]], [[Partial information decomposition]]
- Related sources: [[heins-2024-surprise-minimization]], [[waade-2025-as-one-and-many]], [[palacios-2020-hierarchical-markov-blankets]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@misc{MaistoNuzziPezzulo2025Flock,
  author        = {Maisto, Domenico and Nuzzi, Davide and Pezzulo, Giovanni},
  title         = {What the flock knows that the birds do not: exploring the emergence of joint agency in multi-agent active inference},
  year          = {2025},
  eprint        = {2511.10835},
  archivePrefix = {arXiv},
  primaryClass  = {nlin.AO}
}
```
