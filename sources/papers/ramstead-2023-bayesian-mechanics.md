---
type: paper
title: "On Bayesian mechanics: a physics of and by beliefs"
aliases:
  - "Ramstead et al. 2023"
  - "Ramstead (2023) Bayesian Mechanics Review"
authors:
  - Maxwell J. D. Ramstead
  - Dalton A. R. Sakthivadivel
  - Conor Heins
  - Magnus Koudahl
  - Beren Millidge
  - Lancelot Da Costa
  - Brennan Klein
  - Karl J. Friston
year: 2023
arxiv: "2205.11543"
url: https://royalsocietypublishing.org/doi/10.1098/rsfs.2022.0029
tags:
  - cluster/vfe
  - cluster/participatory
  - cluster/info-geometry
  - project/multi-agent
  - project/transformer
  - field/neuroscience
  - field/physics
  - field/statistics
  - cluster/participatory/consciousness
status: stable
created: 2026-06-19
updated: 2026-06-20
---

# On Bayesian mechanics: a physics of and by beliefs

> [!info] Citation
> Ramstead, M. J. D., Sakthivadivel, D. A. R., Heins, C., Koudahl, M., Millidge, B., Da Costa, L., Klein, B., & Friston, K. J. (2023). "On Bayesian mechanics: a physics of and by beliefs." *Interface Focus* **13**(3): 20220029. DOI: [10.1098/rsfs.2022.0029](https://doi.org/10.1098/rsfs.2022.0029). Preprint: [arXiv:2205.11543](https://arxiv.org/abs/2205.11543).

## TL;DR

This is the definitive *review and synthesis* of **Bayesian mechanics** — the field, emerged over the prior decade, that treats systems partitioned into "particles" such that their internal states (or trajectories) *encode the parameters of beliefs about external states*. It is "a physics of and by beliefs": physics *of* beliefs (the dynamics of internal states are lawful) and physics *by* beliefs (those dynamics are read as inference). The paper distinguishes path-tracking from mode-tracking formulations, lays out the synchronization map, the Fisher/information geometry, and the steady-state assumptions, and consolidates the lineage running from Friston 2019 through Da Costa et al. 2021 and Parr et al. 2020. PIFB instantiates exactly this "physics of beliefs" stance.

## Problem & setting

Across a scattered literature, what does it actually mean to say a physical system *is doing inference*? The review unifies the answers under one schema: a system with a [[Markov blanket interpretation debate|Markov blanket]] whose internal states parametrize a variational density `q_μ(η)` over external states, with the system's most likely (or path-averaged) internal dynamics minimizing [[Variational free energy]].

## Method

The paper organizes Bayesian mechanics around three pillars: the *partition* (Markov blankets / particular partitions), the *map* (synchronization / "bold" map from internal states to beliefs about external states), and the *flow* (free-energy gradient flow on the resulting statistical manifold, under the [[Fisher information metric]]). It contrasts steady-state (mode-tracking) versus path-integral (path-tracking) formulations, and catalogues the assumptions — non-equilibrium steady state, conditional independence, ergodicity — each requires.

## Key results

- **A unified schema** for what "physics of beliefs" means, consolidating the field's results into partition / map / flow.
- **Mode- vs path-tracking distinction** clarified, with the conditions each needs.
- **An honest accounting of assumptions**, which makes contact with the critical literature ([[Markov blanket interpretation debate]]).

## Relevance to this research

This is the paper whose central phrase — "a physics of and by beliefs" — **[[participatory-it-from-bit]]** most directly instantiates and extends. PIFB takes the Bayesian-mechanics schema (internal states parametrize beliefs about the external world; dynamics are inference) and adds the two ingredients this review does not: a *gauge structure* on the belief fibers ([[Gauge transformation]], [[Parallel transport]], frame-covariant comparison of beliefs across observers) and a *multi-agent / multi-scale* stack ([[Multi-agent variational free energy]], [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]]). The Fisher-geometric flow at the heart of the schema is the project's [[Natural gradient]] belief update; the steady-state solenoidal structure is its [[Hamiltonian belief dynamics]] / [[Belief inertia]]. This review is the best single entry point to the [[Bayesian mechanics]] hub page and frames the foundational debate PIFB must engage.

## Cross-links

- Concepts: [[Variational free energy]], [[Fisher information metric]], [[Natural gradient]], [[Participatory realism (it from bit)]], [[Hamiltonian belief dynamics]]
- New pages: [[Bayesian mechanics]], [[Markov blanket interpretation debate]]
- Methods/themes: [[Free-energy principle active inference]], [[Multi-agent variational free energy]], [[Information geometry and natural gradient]]
- Related sources: [[dacosta-2021-bayesian-mechanics]], [[friston-2019-particular-physics]], [[parr-2020-markov-blankets-thermodynamics]], [[sakthivadivel-2022-geometry-bayesian-mechanics]], [[caticha-2019-entropic-dynamics]]
- Manuscript: [[participatory-it-from-bit]]

```bibtex
@article{ramstead2023bayesian,
  title   = {On Bayesian mechanics: a physics of and by beliefs},
  author  = {Ramstead, Maxwell J. D. and Sakthivadivel, Dalton A. R. and Heins, Conor and Koudahl, Magnus and Millidge, Beren and Da Costa, Lancelot and Klein, Brennan and Friston, Karl J.},
  journal = {Interface Focus},
  volume  = {13},
  number  = {3},
  pages   = {20220029},
  year    = {2023},
  doi     = {10.1098/rsfs.2022.0029},
  eprint  = {2205.11543},
  archivePrefix = {arXiv},
  publisher = {The Royal Society}
}
```
