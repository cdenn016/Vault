---
type: paper
title: "From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators"
aliases: ["Strogatz 2000", "From Kuramoto to Crawford"]
authors: ["Strogatz S. H."]
year: 2000
url: https://doi.org/10.1016/S0167-2789(00)00094-4
tags: [cluster/social-physics, project/social-physics, field/physics, field/mathematics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators

> [!info] Citation
> Strogatz, S. H. (2000). *From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators*. Physica D: Nonlinear Phenomena, 143(1–4), 1–20. DOI 10.1016/S0167-2789(00)00094-4.

## TL;DR
A lucid analytical review tracing the mathematics of the synchronization onset in the Kuramoto model, from Kuramoto's original self-consistency argument to Crawford's amplitude-equation / center-manifold treatment of the bifurcation. Strogatz explains why the seemingly simple self-consistency calculation is subtle (the incoherent state is neutrally stable, with a continuous spectrum), and how Crawford's analysis resolved the stability of the incoherent state and the nature of the branching synchronized solutions.

## What it establishes
The review organizes the theory of the transition at $K_c = 2/[\pi g(0)]$. It contrasts two viewpoints: Kuramoto's mean-field self-consistency, $r = K r \int_{-\pi/2}^{\pi/2}\cos^2\theta\, g(Kr\sin\theta)\, d\theta$, which predicts the supercritical branch $r\sim\sqrt{K-K_c}$, and Crawford's rigorous bifurcation analysis using the continuity equation for the oscillator density $\rho(\theta,\omega,t)$ and center-manifold reduction. Strogatz clarifies the role of the continuous spectrum, the marginal stability of the incoherent state below $K_c$, and the effect of noise in regularizing the spectrum. The article frames the open problems (global stability, finite-size effects) that motivated the next two decades of work.

## Relevance to this research
This is the standard analytical and pedagogical entry point for the mathematics of synchronization onset: mean-field self-consistency, the stability of the incoherent state, and the bifurcation to collective phase-locking. These are exactly the tools one would want when porting stability and bifurcation analysis to the program's underdamped, momentum-carrying belief dynamics, where the question is whether a population of beliefs locks or fragments as coupling strength varies. The connection is in the analytical toolkit (bifurcation theory of a mean field) rather than in shared equations with the VFE functional. See [[Hamiltonian belief dynamics]], [[Synchronization and the Kuramoto model]], [[Opinion dynamics]].

## Cross-links
- Concept: [[Synchronization and the Kuramoto model]]
- Related sources: [[kuramoto-1975-coupled-oscillators]], [[acebron-2005-kuramoto-review]], [[winfree-1967-coupled-oscillators]]

## BibTeX
```bibtex
@article{strogatz2000kuramoto,
  author  = {Strogatz, Steven H.},
  title   = {From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators},
  journal = {Physica D: Nonlinear Phenomena},
  volume  = {143},
  number  = {1--4},
  pages   = {1--20},
  year    = {2000},
  doi     = {10.1016/S0167-2789(00)00094-4}
}
```
