---
type: reference
title: "The Markov blankets of life: autonomy, active inference and the free energy principle"
aliases:
  - "Kirchhoff et al. 2018"
  - "Kirchhoff (2018) Markov Blankets of Life"
authors:
  - Michael Kirchhoff
  - Thomas Parr
  - Ensor Palacios
  - Karl Friston
  - Julian Kiverstein
year: 2018
tags:
  - cluster/vfe
  - cluster/participatory
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
  - field/neuroscience
  - field/biology
  - field/philosophy
  - cluster/participatory/consciousness
created: 2026-06-19
updated: 2026-06-19
---

# The Markov blankets of life: autonomy, active inference and the free energy principle

> [!info] Citation
> Kirchhoff, M., Parr, T., Palacios, E., Friston, K., & Kiverstein, J. (2018). "The Markov blankets of life: autonomy, active inference and the free energy principle." *Journal of the Royal Society Interface* **15**(138): 20170792. DOI: [10.1098/rsif.2017.0792](https://doi.org/10.1098/rsif.2017.0792).

## TL;DR

This paper develops the idea of **nested Markov blankets** — blankets within blankets — as the formal signature of biological autonomy and individuality. A living system is not a single boundary but a hierarchy of statistical boundaries (organelle within cell within tissue within organism), each an active-inference unit minimizing [[Variational free energy]], and each nested inside the next. It is the canonical precedent for treating agents as recursively composed of sub-agents, which the project lifts into its multi-scale meta-agent tower.

## What it establishes

- **Nested blankets = nested agents.** Markov blankets compose hierarchically; a blanket at one scale is built from sub-systems that are themselves blanketed agents, giving a recursive, scale-spanning notion of biological individuality.
- **Autonomy as self-evidencing.** A living system maintains its own boundary by minimizing free energy, so autonomy and active inference are two readings of the same dynamics.
- **Life as multi-scale inference.** Adaptive behaviour is free-energy minimization running simultaneously at many nested scales, not a single-level optimization.

## Why the project cites it

This is the **canonical nested-blanket precedent** for the project's central architectural commitment: that agents are recursively composed and that coarse-graining a cluster of agents yields a higher-scale agent. The nested-blanket picture is the conceptual seed of [[Meta-agents and hierarchical emergence]] and the full [[Ouroboros multi-scale dynamics]] tower, where scale-`s+1` agents are coarse-grainings of clusters of scale-`s` agents and a parent's beliefs become its constituents' priors (the cross-scale shadow-prior construction). It also grounds [[Multi-agent variational free energy]] (each agent is a blanketed self-evidencing unit) and [[Renormalization-group flow of beliefs]] (moving between blanket scales is an RG step). For [[participatory-it-from-bit]], the nested-blanket account supplies the multi-scale observer structure: an "observer" is itself a blanket inside larger blankets, so the participatory cut is scale-relative — connecting to [[Participatory realism (it from bit)]] and the [[Markov blanket interpretation debate]] over whether such boundaries are real or perspectival. See [[Agents as fibre-bundle sections]] for the bundle-theoretic rendering.

```bibtex
@article{kirchhoff2018markov,
  title   = {The Markov blankets of life: autonomy, active inference and the free energy principle},
  author  = {Kirchhoff, Michael and Parr, Thomas and Palacios, Ensor and Friston, Karl and Kiverstein, Julian},
  journal = {Journal of the Royal Society Interface},
  volume  = {15},
  number  = {138},
  pages   = {20170792},
  year    = {2018},
  doi     = {10.1098/rsif.2017.0792},
  publisher = {The Royal Society}
}
```
