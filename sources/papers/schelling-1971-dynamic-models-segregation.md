---
type: paper
title: "Dynamic Models of Segregation"
aliases: ["Schelling 1971", "Schelling segregation model"]
authors: ["Schelling T. C."]
year: 1971
url: https://doi.org/10.1080/0022250X.1971.9989794
tags: [cluster/social-physics, project/social-physics, field/economics, field/sociology, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Dynamic Models of Segregation

> [!info] Citation
> Schelling, T. C. (1971). *Dynamic Models of Segregation*. Journal of Mathematical Sociology, 1(2), 143-186. DOI: [10.1080/0022250X.1971.9989794](https://doi.org/10.1080/0022250X.1971.9989794).

## TL;DR
Schelling introduces what is now the archetypal agent-based tipping model. Agents of two types occupy cells on a line or a grid; each agent is content as long as some modest fraction of its immediate neighbors share its type, and relocates to the nearest acceptable spot when that threshold is violated. Schelling shows by hand-simulation that even when every agent is perfectly happy in a well-mixed configuration — tolerating, say, a minority status as long as at least a third of neighbors are like itself — the relocation dynamics drive the whole system to near-total spatial segregation. The macro outcome (sharply segregated neighborhoods) is one *no individual preferred or intended*; it emerges purely from the aggregation of mild local preferences. This is the founding demonstration that discriminatory-looking macrostructure does not require discriminatory micro-preferences.

## What it establishes
The model is the canonical *micromotive-to-macrobehavior* result. Each agent applies a threshold rule: stay if the share of like neighbors $f \ge \tau$, otherwise move, where the individual tolerance $\tau$ can be quite permissive (e.g. $\tau = 1/3$). The aggregate equilibrium is nonetheless almost fully segregated, because every relocation that satisfies a discontented agent tends to make a previously content neighbor of the opposite type discontent, propagating a cascade of moves. Schelling thereby isolates a *tipping point*: small changes in the local mixture push a neighborhood across a threshold after which it rapidly and irreversibly flips to homogeneity. The general lesson — that the relationship between individual incentives and collective outcomes is mediated by an emergent dynamic and can be wildly counterintuitive — became the conceptual cornerstone of agent-based social modeling and of tipping/threshold phenomena generally.

## Relevance to this research
This is the archetypal tipping result and a foundational agent-based model, core canon for the tipping side of the program. It is the qualitative phenomenon the program's collective dynamics must reproduce: local belief-alignment forces (the neighbor-coupling $\sum_j \beta_{ij}\,\mathrm{KL}(q_i\|\Omega_{ij}[q_j])$ that pulls each agent toward its transported neighbors) producing a global phase — consensus, segregation into clusters, or polarization — that the population did not choose and no agent intended. Schelling's threshold-driven flip is the discrete-spatial precursor of the phase transitions and metastable basins the belief-coupling dynamics should exhibit as coupling strength crosses a critical value. The relevance is conceptual and target-setting rather than mechanistic: Schelling's agents move in space under a threshold rule, while the program's agents move beliefs in an information-geometric manifold under smooth gradient flow, so the link is "must reproduce this class of emergent tipping," not a shared equation.

See [[Schelling segregation and tipping points]], [[Sociophysics]], [[Opinion dynamics]], [[Community detection and modularity]].

## Cross-links
- Concept: [[Schelling segregation and tipping points]]
- Related sources: [[schelling-1978-micromotives-macrobehavior]], [[arthur-1989-increasing-returns-lock-in]]

## BibTeX
```bibtex
@article{schelling1971segregation,
  author  = {Schelling, Thomas C.},
  title   = {Dynamic Models of Segregation},
  journal = {Journal of Mathematical Sociology},
  year    = {1971},
  volume  = {1},
  number  = {2},
  pages   = {143--186},
  doi     = {10.1080/0022250X.1971.9989794}
}
```
