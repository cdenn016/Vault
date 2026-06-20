---
type: paper
title: "Competing Technologies, Increasing Returns, and Lock-In by Historical Events"
aliases: ["Arthur 1989", "Increasing returns and lock-in"]
authors: ["Arthur W. B."]
year: 1989
url: https://doi.org/10.2307/2234208
tags: [cluster/social-physics, project/social-physics, field/economics, field/mathematics, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Competing Technologies, Increasing Returns, and Lock-In by Historical Events

> [!info] Citation
> Arthur, W. B. (1989). *Competing Technologies, Increasing Returns, and Lock-In by Historical Events*. The Economic Journal, 99(394), 116-131. DOI: [10.2307/2234208](https://doi.org/10.2307/2234208).

## TL;DR
Arthur formalizes how **increasing returns to adoption** make technology choice path-dependent. When the benefit of a technology grows with the number of prior adopters (through learning effects, network externalities, or coordination), agents arriving in sequence choose between competing options whose relative attractiveness is shaped by who came before. Modeling adoption as a stochastic process with positive feedback, Arthur proves that small early *historical accidents* — the order and identity of the first few choosers — can drive the system to lock irreversibly onto one technology. The selected outcome is non-ergodic (history matters), unpredictable in advance, potentially inflexible (hard to escape once entrenched), and not necessarily the most efficient option. This is the canonical economic statement of path dependence and the QWERTY-style lock-in.

## What it establishes
The adoption dynamics are a nonlinear Pólya-type urn / random walk with reinforcement. With constant or diminishing returns the market share converges to a predictable, efficiency-determined split; with *increasing* returns the share dynamics have multiple absorbing attractors, and the realized path is captured by one of them according to early random events:

$$\text{increasing returns} \;\Rightarrow\; \text{non-ergodic, multiple stable equilibria, history-selected lock-in}.$$

Arthur characterizes the four properties that distinguish increasing-returns allocation: *non-predictability* (the limit cannot be forecast from fundamentals alone), *potential inefficiency* (an inferior technology can win), *inflexibility* (lock-in resists later correction), and *non-ergodicity* (early small events are never averaged away). The positive-feedback loop turns transient fluctuations into permanent structure.

## Relevance to this research
Path dependence and lock-in are the *persistence-of-state* side of tipping, strong adjacent economics canon for the program. Once a consensus basin is entered it self-reinforces, which maps onto the **metastable attractors** of the belief-coupling dynamics: when neighbor coupling $\sum_j\beta_{ij}\,\mathrm{KL}(q_i\|\Omega_{ij}[q_j])$ provides positive feedback (agents in agreement pull each other deeper into agreement), the population settles into one of several stable consensus configurations selected by early conditions, not by which is "best." The link is especially suggestive for the *underdamped* regime ([[Belief inertia]], [[Hamiltonian belief dynamics]]): inertial belief momentum gives rise to overshoot and **hysteresis**, the dynamical signature of history-dependent lock-in that first-order flow lacks. The relevance is structural and analogical — Arthur's mechanism is a reinforced stochastic process over discrete technologies, the program's is deterministic-plus-noise gradient flow over Gaussian beliefs — so lock-in is a phenomenon the program aims to reproduce, not a borrowed theorem.

See [[Schelling segregation and tipping points]], [[Belief inertia]], [[Hamiltonian belief dynamics]], [[Opinion dynamics]].

## Cross-links
- Concept: [[Schelling segregation and tipping points]]
- Related sources: [[schelling-1971-dynamic-models-segregation]], [[schelling-1978-micromotives-macrobehavior]]

## BibTeX
```bibtex
@article{arthur1989lockin,
  author  = {Arthur, W. Brian},
  title   = {Competing Technologies, Increasing Returns, and Lock-In by Historical Events},
  journal = {The Economic Journal},
  year    = {1989},
  volume  = {99},
  number  = {394},
  pages   = {116--131},
  doi     = {10.2307/2234208}
}
```
