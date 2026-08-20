---
type: paper
title: "Spin glass systems as collective active inference"
aliases:
  - "Heins et al. 2023 spin glass active inference"
authors:
  - Heins, Conor
  - Klein, Brennan
  - Demekas, Daphne
  - Aguilera, Miguel
  - Buckley, Christopher L.
year: 2023
arxiv: 2207.06970
url: https://arxiv.org/abs/2207.06970
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/social-physics
  - cluster/social-physics/social-influence
  - project/multi-agent
  - project/social-physics
  - field/physics
  - field/cs-ml
  - field/neuroscience
created: 2026-08-20
---

# Spin glass systems as collective active inference

> [!info] Citation
> Conor Heins, Brennan Klein, Daphne Demekas, Miguel Aguilera, and Christopher L. Buckley (2023). "Spin glass systems as collective active inference." In *Active Inference: Third International Workshop, IWAI 2022*, CCIS 1721, 75--98. arXiv: [2207.06970](https://arxiv.org/abs/2207.06970). https://doi.org/10.1007/978-3-031-28719-0_6

## TL;DR

A deliberately parameterized population of active-inference agents can reproduce the sampling dynamics of a spin glass. The equivalence is exact under a specific factorized generative model, symmetric mutual precisions, and asynchronous updates, but the paper stresses that it is fragile under simple changes to either agent models or interactions.

## Problem & setting

The paper asks when local Bayesian or active-inference dynamics admit an autonomous collective description at a higher scale. Ising-like binary agents and a spin-glass target provide a controlled setting in which individual generative models can be compared with a population-level Boltzmann distribution.

## Method

The authors choose individual likelihoods and precisions so that each agent's variational free-energy update matches the conditional update of a spin variable. With symmetric pairwise couplings and an asynchronous schedule, the population transition kernel implements Glauber-style sampling from the corresponding spin-glass stationary distribution.

## Key results

The resulting collective dynamics are equivalent to sampling from the declared Boltzmann machine. The result does not survive arbitrary changes to the factorization, precision symmetry, or update schedule. The collective is therefore a narrow exact construction rather than a theorem that any mutually coupled free-energy-minimizing agents optimize a global ELBO.

## Relevance to this research

This is the strongest exact comparator for [[Multi-agent variational free energy]]. It shows that a global statistical-mechanical law can emerge from local active inference, while making the load-bearing assumptions inspectable. MultiAgentELBO should reproduce this special case as a positive control before claiming a broader reciprocal construction, and should treat broken symmetry, synchronous updating, and altered local models as negative controls.

## Cross-links

- Concepts: [[Collective active inference]], [[Multi-agent variational free energy]], [[Bayesian mechanics]]
- Related sources: [[heins-2024-surprise-minimization]], [[waade-2025-as-one-and-many]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@inproceedings{HeinsEtAl2023SpinGlass,
  author    = {Heins, Conor and Klein, Brennan and Demekas, Daphne and Aguilera, Miguel and Buckley, Christopher L.},
  title     = {Spin glass systems as collective active inference},
  booktitle = {Active Inference: Third International Workshop, IWAI 2022},
  series    = {Communications in Computer and Information Science},
  volume    = {1721},
  pages     = {75--98},
  year      = {2023},
  doi       = {10.1007/978-3-031-28719-0_6},
  eprint    = {2207.06970},
  archivePrefix = {arXiv}
}
```
