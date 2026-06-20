---
type: reference
title: "Physics and Social Science — The Approach of Synergetics"
aliases: ["Weidlich 1991", "Synergetics of Social Science"]
authors: ["Weidlich W."]
year: 1991
url: https://doi.org/10.1016/0370-1573(91)90024-G
tags: [cluster/social-physics, project/social-physics, field/physics, field/sociology, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Physics and Social Science — The Approach of Synergetics

> [!info] Citation
> Weidlich, W. (1991). *Physics and Social Science — The Approach of Synergetics*. Physics Reports **204**(1), 1–163. DOI: [10.1016/0370-1573(91)90024-G](https://doi.org/10.1016/0370-1573(91)90024-G).

## TL;DR
The seminal, book-length review that founded **sociodynamics** as a quantitative discipline. Weidlich imports the synergetics program of Haken into the social sciences, building a stochastic description of society in which the fundamental object is a probability distribution over macroscopic "socioconfigurations." From individual-level probabilistic transition rates — themselves governed by dynamical utilities and trend parameters — he constructs a **master equation** for the time evolution of that distribution and then derives, by mean-value and Fokker-Planck reductions, deterministic macroscopic equations of motion. The framework yields collective phenomena including order-parameter bifurcations and phase-transition-like switches between social states (polarization, consensus, migration patterns).

## What it establishes
Let $\mathbf{n}$ denote a socioconfiguration (e.g. counts of agents holding each opinion) and $P(\mathbf{n},t)$ the probability distribution over configurations. Individual decisions induce configurational transition rates $w(\mathbf{n}'|\mathbf{n})$, and the distribution evolves by the master equation
$$ \frac{\partial P(\mathbf{n},t)}{\partial t} = \sum_{\mathbf{n}'} \big[\, w(\mathbf{n}|\mathbf{n}')\,P(\mathbf{n}',t) - w(\mathbf{n}'|\mathbf{n})\,P(\mathbf{n},t)\,\big]. $$
The transition rates are built from dynamical utility functions, so that agents move preferentially toward more attractive configurations. A Kramers-Moyal / Fokker-Planck expansion gives drift and diffusion for the macrovariables, and taking expectation values yields closed deterministic **equations of motion** for mean opinion shares. Tuning trend and coupling parameters drives the deterministic system through bifurcations that Weidlich interprets as social phase transitions.

## Relevance to this research
This is the most authoritative statement of the stochastic-population route to opinion macrodynamics, and the historical template for the program's central claim that a continuum belief dynamics emerges from a finite agent population. The ascent from individual probabilistic transition rates, through a master equation over configurations, to expectation-value equations of motion is precisely the configuration-counting move the SocialPhysics [[Meta-entropy]] argument reprises in information-geometric dress. The order-parameter bifurcations Weidlich derives are the ancestor of the consensus/polarization phase structure the gauge-VFE attention coupling produces. Honestly, the connection is genealogical rather than mechanical: Weidlich's state space is discrete socioconfiguration counts and his rates come from scalar utilities, not from KL divergences between Gaussian beliefs on a fibre bundle, so there is no gauge transport or inertial (underdamped) content here. It is the conceptual and methodological grandparent of the program, not a component of its functional.

## Cross-links
- Concept: [[Sociodynamics and synergetics]]
- Related sources: [[weidlich-haag-1983-quantitative-sociology]], [[helbing-2010-quantitative-sociodynamics]]

## BibTeX
```bibtex
@article{weidlich1991physics,
  author  = {Weidlich, Wolfgang},
  title   = {Physics and Social Science --- The Approach of Synergetics},
  journal = {Physics Reports},
  volume  = {204},
  number  = {1},
  pages   = {1--163},
  year    = {1991},
  doi     = {10.1016/0370-1573(91)90024-G}
}
```
