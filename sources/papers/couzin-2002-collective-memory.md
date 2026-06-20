---
type: paper
title: "Collective Memory and Spatial Sorting in Animal Groups"
aliases: ["Couzin et al. 2002", "Couzin zonal model"]
authors: ["Couzin I. D.", "Krause J.", "James R.", "Ruxton G. D.", "Franks N. R."]
year: 2002
url: https://doi.org/10.1006/jtbi.2002.3065
tags: [cluster/social-physics, project/social-physics, field/biology, field/physics, cluster/social-physics/social-influence]
created: 2026-06-19
updated: 2026-06-19
---

# Collective Memory and Spatial Sorting in Animal Groups

> [!info] Citation
> Couzin, I. D., Krause, J., James, R., Ruxton, G. D., & Franks, N. R. (2002). *Collective Memory and Spatial Sorting in Animal Groups*. Journal of Theoretical Biology, 218(1), 1–11. DOI 10.1006/jtbi.2002.3065.

## TL;DR
Couzin and colleagues introduce a self-organizing zonal model of group motion in which each individual responds to neighbors through three concentric zones: a short-range zone of repulsion, an intermediate zone of alignment, and a longer-range zone of attraction. Varying just the width of the alignment zone, the group abruptly switches between qualitatively different collective states — a loosely swarming aggregate, a torus (mill), and a highly aligned dynamic group. The transitions are hysteretic: the state the group occupies depends on its history, so the group exhibits collective memory.

## What it establishes
Each agent updates its desired direction by summing contributions from neighbors in the three zones: it turns away from neighbors in the repulsion zone $z_r$, aligns with the average heading of neighbors in the alignment zone $z_o$, and steers toward neighbors in the attraction zone $z_a$, subject to a maximum turning rate and orientation noise. As the alignment-zone width $\Delta r_o$ is increased and then decreased, the group's polarization and angular momentum trace a hysteresis loop: at a given parameter value the collective state (swarm, torus, or polarized group) depends on whether the parameter was approached from above or below. This path dependence is the "collective memory" — information about the group's past is stored in its current configuration, not in any individual.

## Relevance to this research
This demonstrates hysteresis and collective memory in an interacting population, the agent-based counterpart of the program's belief-inertia thesis that history dependence and memory arise from the coupling structure rather than from any single agent's state. The bistability and path dependence are phenomenologically what the underdamped (momentum-carrying) belief regime predicts — overshoot and lag that make the population's current state depend on its trajectory. The alignment is strong at the level of phenomenology (emergent memory from coupling), though the mechanism here is multistability of a first-order zonal model rather than literal inertial mass; the honest framing is a close behavioral analogue, not the same equations as $M\ddot\mu + \gamma\dot\mu + \nabla F = 0$. See [[Belief inertia]], [[Collective motion and flocking]], [[Hamiltonian belief dynamics]].

## Cross-links
- Concept: [[Belief inertia]]
- Related sources: [[couzin-2005-effective-leadership]], [[vicsek-1995-self-driven-particles]], [[reynolds-1987-boids]]

## BibTeX
```bibtex
@article{couzin2002collective,
  author  = {Couzin, Iain D. and Krause, Jens and James, Richard and Ruxton, Graeme D. and Franks, Nigel R.},
  title   = {Collective Memory and Spatial Sorting in Animal Groups},
  journal = {Journal of Theoretical Biology},
  volume  = {218},
  number  = {1},
  pages   = {1--11},
  year    = {2002},
  doi     = {10.1006/jtbi.2002.3065}
}
```
