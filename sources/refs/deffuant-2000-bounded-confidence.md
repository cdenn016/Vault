---
type: reference
title: "Mixing Beliefs among Interacting Agents"
aliases:
  - "Deffuant 2000"
  - "Deffuant et al. 2000"
  - "Bounded confidence (Deffuant model)"
authors:
  - Guillaume Deffuant
  - David Neau
  - Frédéric Amblard
  - Gérard Weisbuch
year: 2000
tags:
  - cluster/social-physics
  - project/multi-agent
  - project/social-physics
  - field/physics
  - field/sociology
  - cluster/social-physics/opinion-dynamics
created: 2026-06-18
updated: 2026-06-18
---

# Mixing Beliefs among Interacting Agents

> [!info] Citation
> Deffuant, G., Neau, D., Amblard, F., & Weisbuch, G. (2000). "Mixing Beliefs among Interacting Agents." *Advances in Complex Systems*, **3**(1n04), 87–98. DOI: [10.1142/S0219525900000078](https://doi.org/10.1142/S0219525900000078).

## TL;DR

A foundational opinion-dynamics model in which agents holding *continuous* opinions update through random pairwise encounters, but only when their opinions differ by less than a fixed threshold $d$ (the **bounded confidence** rule). Large thresholds drive convergence to a single consensus opinion; small thresholds fragment the population into several mutually non-influencing opinion clusters.

## What it establishes

The model considers a population of agents, each carrying a continuous opinion $x_i \in [0,1]$. At each step a random pair $(i,j)$ meets. If their opinions are close enough,

$$
|x_i - x_j| < d,
$$

they move toward each other by a fraction $\mu$ of their gap:

$$
x_i \leftarrow x_i + \mu\,(x_j - x_i), \qquad x_j \leftarrow x_j + \mu\,(x_i - x_j).
$$

If the gap exceeds the threshold $d$, no interaction occurs and both opinions are left unchanged. The key results the paper reports:

- The **confidence threshold $d$** controls the asymptotic regime. Above a critical value the whole population converges to a single average opinion (consensus); below it the system settles into multiple stable clusters.
- The number of surviving clusters scales roughly as $1/d$ — narrower confidence bounds admit more distinct, internally homogeneous opinion groups that no longer exchange influence.
- The convergence parameter $\mu$ sets the *rate* of approach but not the qualitative cluster structure, which is governed by $d$.
- The dynamics is studied both on fully mixed (complete-graph) populations and on social-network topologies, establishing the rule as a minimal, tunable mechanism for consensus-versus-fragmentation transitions.

> [!note] Editorial: The exact critical-threshold value and cluster-count formulas above are summarized from the standard reading of this well-known model; treat the $1/d$ scaling as the qualitative claim made in the paper rather than a precise theorem.

## Why the project cites it

This reference anchors the **social-physics** side of the [[Gauge-Theoretic Multi-Agent VFE Model]]. The project models populations of belief-carrying agents, and Deffuant's bounded-confidence rule is a canonical, minimal precedent for two themes the project formalizes more richly:

- **Belief interaction as gated local averaging.** The Deffuant update is exactly a confidence-weighted convex pull of one belief toward another. In the project's framing this is the scalar, Euclidean shadow of [[Precision weighting]]-modulated belief mixing, where the bounded-confidence gate plays the role of a hard precision cutoff. The project lifts this to distributional beliefs $(\mu,\Sigma)$ updated under [[Multi-agent variational free energy]], replacing the flat threshold with a curvature-aware coupling governed by the [[Fisher information metric]].

- **Consensus vs. fragmentation as an emergent, scale-dependent phenomenon.** The transition between a single consensus cluster and many isolated clusters is a clean instance of [[Meta-agents and hierarchical emergence]]: clusters are the coarse-grained agents that survive when fine-grained influence is gated off. This connects to the project's [[Renormalization-group flow of beliefs]], where the confidence threshold acts like a coupling constant whose value selects the number of effective degrees of freedom at the macroscopic scale.

- **Reluctance to move beliefs.** The thresholded "don't update if too far" behavior is a discrete cousin of [[Belief inertia]] (see [[belief-inertia]]): agents resist assimilating evidence that lies outside their confidence interval, just as inertial beliefs resist [[Prediction error]] that conflicts with strong priors.

Within the social-physics lineage, this work sits beside [[degroot-1974-consensus]] and [[friedkin-johnsen-1990]] (linear consensus and stubborn-agent models) and is the continuous-opinion counterpart to the synchronous bounded-confidence dynamics of [[hegselmann-krause-2002]]; together with [[galam-2008-sociophysics]] they form the classical backdrop against which the project's gauge-theoretic, variational treatment of interacting agents is positioned.

## BibTeX

```bibtex
@article{deffuant2000mixing,
  author  = {Deffuant, Guillaume and Neau, David and Amblard, Fr{\'e}d{\'e}ric and Weisbuch, G{\'e}rard},
  title   = {Mixing Beliefs among Interacting Agents},
  journal = {Advances in Complex Systems},
  volume  = {3},
  number  = {1n04},
  pages   = {87--98},
  year    = {2000},
  doi     = {10.1142/S0219525900000078},
  publisher = {World Scientific}
}
```
