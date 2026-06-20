---
type: paper
title: "Flocks, Herds, and Schools: A Distributed Behavioral Model"
aliases: ["Reynolds 1987", "Boids"]
authors: ["Reynolds C. W."]
year: 1987
url: https://doi.org/10.1145/37402.37406
tags: [cluster/social-physics, project/social-physics, field/cs-ml, field/biology, cluster/social-physics/social-influence]
created: 2026-06-19
updated: 2026-06-19
---

# Flocks, Herds, and Schools: A Distributed Behavioral Model

> [!info] Citation
> Reynolds, C. W. (1987). *Flocks, Herds, and Schools: A Distributed Behavioral Model*. Computer Graphics (SIGGRAPH '87 Proceedings), 21(4), 25–34. DOI 10.1145/37402.37406.

## TL;DR
Reynolds' boids model is the original distributed simulation of flocking. Each simulated bird ("boid") is an autonomous agent that decides its own motion from three simple local steering rules applied to its visible neighbors: separation (avoid crowding), alignment (match average heading), and cohesion (move toward the local center of mass). With no leader and no global plan, lifelike flocking, herding, and schooling emerge purely from these local interactions. The model became the foundation of agent-based collective-motion modeling in both graphics and science.

## What it establishes
Each boid computes a steering acceleration as a weighted combination of three urges evaluated over neighbors within a limited perception range and field of view:
$$ \mathbf{a}_i = w_s\,\mathbf{a}^{\text{sep}}_i + w_a\,\mathbf{a}^{\text{align}}_i + w_c\,\mathbf{a}^{\text{coh}}_i, $$
where separation pushes away from too-close neighbors, alignment steers toward their average velocity, and cohesion steers toward their centroid. There is no central controller and no global state; each agent acts only on locally perceived information, and the global flock pattern is an emergent consequence. Reynolds emphasized perception locality and the agent-centric formulation, which anticipated the metric/topological-neighborhood debate later settled empirically.

## Relevance to this research
This is the foundational distributed-agent flocking model: global order emerges purely from local, neighbor-based rules with no central controller — the same bottom-up emergence ethos as the program's per-agent VFE minimization, where each agent updates its own belief from local coupling and collective structure is emergent. The three rules are a behavioral precursor to the repulsion/alignment/attraction terms later formalized by Couzin and to the alignment coupling in the Vicsek model. The relevance is adjacent and conceptual — it establishes the local-rule, no-controller paradigm — rather than machinery the VFE functional uses. See [[Sociophysics]], [[Collective motion and flocking]], [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Collective motion and flocking]]
- Related sources: [[couzin-2002-collective-memory]], [[vicsek-1995-self-driven-particles]], [[couzin-2005-effective-leadership]]

## BibTeX
```bibtex
@inproceedings{reynolds1987flocks,
  author    = {Reynolds, Craig W.},
  title     = {Flocks, Herds, and Schools: A Distributed Behavioral Model},
  booktitle = {Computer Graphics (SIGGRAPH '87 Proceedings)},
  volume    = {21},
  number    = {4},
  pages     = {25--34},
  year      = {1987},
  doi       = {10.1145/37402.37406}
}
```
