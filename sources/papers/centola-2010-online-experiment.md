---
type: paper
title: "The Spread of Behavior in an Online Social Network Experiment"
aliases: ["Centola 2010", "Online network behavior experiment"]
authors: ["Centola D."]
year: 2010
url: https://doi.org/10.1126/science.1185231
tags: [cluster/social-physics, project/social-physics, field/sociology, field/cs-ml, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# The Spread of Behavior in an Online Social Network Experiment

> [!info] Citation
> Centola, D. (2010). *The Spread of Behavior in an Online Social Network Experiment*. Science, 329(5996), 1194-1197. doi:10.1126/science.1185231.

## TL;DR
Centola built an Internet-based health community and randomly assigned participants to either a *clustered-lattice* network or a *random* network with identical average degree, then seeded a health-behavior adoption (registering for a health forum / diffusion of a health-tracking tool) and measured its spread. Contrary to the small-world intuition that random shortcuts speed diffusion, the behavior spread *farther and faster* in the clustered network, because clustering supplies the repeated, redundant social reinforcement that a complex contagion requires before an individual adopts. This is the cleanest experimental demonstration that the topology favoring complex contagion is the opposite of the topology favoring simple contagion.

## What it establishes
The experiment is a randomized controlled trial at the network level — the same individuals, the same average degree, only the wiring differs — which isolates topology as the causal variable. In the clustered condition an undecided individual receives adoption signals from *multiple* network neighbors who share neighbors, so the reinforcement needed to cross an adoption threshold accumulates; in the random condition the same number of signals arrive from socially distant, non-overlapping sources and rarely concentrate on any one ego. The measured adoption probability rose with the number of adopting neighbors, the empirical signature of a threshold/complex-contagion rule rather than the per-contact independence of simple contagion.

## Relevance to this research
This is an empirical anchor for the claim that clustering — the same structure that produces echo chambers — can *aid* rather than impede the spread of a reinforced behavior. The gauge-coupled VFE model should reproduce this when belief change requires accumulated KL pressure from several agreeing neighbors, i.e. when the contagion is complex: clustered coupling concentrates the pressure needed to cross the flip. It is a strong empirical validation target for the model's topology effects, though it tests behavior adoption rather than continuous belief revision directly. See [[Threshold models and complex contagion]], [[Echo chambers and polarization]], and [[Opinion dynamics]].

## Cross-links
- Concept: [[Threshold models and complex contagion]]
- Related sources: [[centola-macy-2007-complex-contagion]], [[watts-2002-global-cascades]], [[granovetter-1978-threshold-models]]

## BibTeX
```bibtex
@article{centola2010spread,
  author  = {Centola, Damon},
  title   = {The Spread of Behavior in an Online Social Network Experiment},
  journal = {Science},
  year    = {2010},
  volume  = {329},
  number  = {5996},
  pages   = {1194--1197},
  doi     = {10.1126/science.1185231}
}
```
