---
type: paper
title: "Novel Type of Phase Transition in a System of Self-Driven Particles"
aliases: ["Vicsek et al. 1995", "Vicsek model"]
authors: ["Vicsek T.", "Czirok A.", "Ben-Jacob E.", "Cohen I.", "Shochet O."]
year: 1995
url: https://doi.org/10.1103/PhysRevLett.75.1226
tags: [cluster/social-physics, project/social-physics, field/physics, field/biology, cluster/social-physics/social-influence]
created: 2026-06-19
updated: 2026-06-19
---

# Novel Type of Phase Transition in a System of Self-Driven Particles

> [!info] Citation
> Vicsek, T., Czirók, A., Ben-Jacob, E., Cohen, I., & Shochet, O. (1995). *Novel Type of Phase Transition in a System of Self-Driven Particles*. Physical Review Letters, 75(6), 1226–1229. DOI 10.1103/PhysRevLett.75.1226.

## TL;DR
The Vicsek model is the minimal statistical-physics model of flocking: identical particles move at constant speed and, at each step, adopt the average direction of motion of their neighbors within a fixed radius, plus a random angular perturbation. As the noise amplitude decreases (or density increases), the system undergoes a kinetic phase transition from a disordered state with zero net motion to an ordered state of collective directed motion, via spontaneous breaking of rotational symmetry. It launched the entire statistical-physics-of-active-matter literature.

## What it establishes
Particles at positions $\mathbf{x}_i$ move with velocity of fixed magnitude $v_0$ and heading $\theta_i$ updated by alignment to neighbors plus noise:
$$ \theta_i(t+1) = \langle \theta_j(t)\rangle_{|\mathbf{x}_j-\mathbf{x}_i|<r} + \eta\,\xi_i, $$
where $\langle\cdot\rangle$ is the average heading over neighbors within radius $r$, $\eta$ is the noise strength, and $\xi_i$ is uniform on $[-\pi,\pi]$. The order parameter is the normalized average velocity $\varphi = \frac{1}{N v_0}\big|\sum_i \mathbf{v}_i\big|$, which is zero in the disordered phase and finite in the ordered phase. The paper shows numerically that $\varphi$ vanishes continuously at a critical noise $\eta_c(\rho)$ with $\varphi \sim (\eta_c-\eta)^\beta$, identifying a genuine nonequilibrium continuous phase transition driven by the interplay of alignment, self-propulsion, and noise — distinct from any equilibrium ferromagnetic transition because the particles move.

## Relevance to this research
This is the seminal microscopic model whose mean-field and kinetic limits launched the continuum-alignment literature, and its order–disorder transition under noise is the physical template for consensus-versus-fragmentation transitions in belief populations: as "noise" (idiosyncratic belief perturbation) rises past a threshold, collective alignment collapses. This connects directly to the program's meta-entropy / configuration-counting bridge, which counts the macrostates available to a population and locates the transition. The relevance is strong at the level of phenomenology (a noise-driven symmetry-breaking transition) and as the ancestor of the coarse-grained field theories the program coarse-grains toward, rather than as an equation the VFE functional contains. See [[Sociophysics]], [[Collective motion and flocking]], [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Collective motion and flocking]]
- Related sources: [[toner-tu-1995-flocking-hydrodynamics]], [[vicsek-zafeiris-2012-collective-motion]], [[reynolds-1987-boids]]

## BibTeX
```bibtex
@article{vicsek1995novel,
  author  = {Vicsek, Tam\'as and Czir\'ok, Andr\'as and Ben-Jacob, Eshel and Cohen, Inon and Shochet, Ofer},
  title   = {Novel Type of Phase Transition in a System of Self-Driven Particles},
  journal = {Physical Review Letters},
  volume  = {75},
  number  = {6},
  pages   = {1226--1229},
  year    = {1995},
  doi     = {10.1103/PhysRevLett.75.1226}
}
```
