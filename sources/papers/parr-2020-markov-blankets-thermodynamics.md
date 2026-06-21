---
type: paper
title: "Markov blankets, information geometry and stochastic thermodynamics"
aliases:
  - "Parr et al. 2020"
  - "Parr (2020) Blankets & Info Geometry"
authors:
  - Thomas Parr
  - Lancelot Da Costa
  - Karl Friston
year: 2020
url: https://royalsocietypublishing.org/doi/10.1098/rsta.2019.0159
tags:
  - cluster/vfe
  - cluster/info-geometry
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/neuroscience
  - field/physics
  - field/statistics
  - cluster/participatory/consciousness
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Markov blankets, information geometry and stochastic thermodynamics

> [!info] Citation
> Parr, T., Da Costa, L., & Friston, K. (2020). "Markov blankets, information geometry and stochastic thermodynamics." *Philosophical Transactions of the Royal Society A* **378**(2164): 20190159. DOI: [10.1098/rsta.2019.0159](https://doi.org/10.1098/rsta.2019.0159).

## TL;DR

This paper makes the **information-geometric** content of Bayesian mechanics explicit: it shows that the internal states of a Markov-blanketed system parametrize a *statistical manifold* of densities over external states, and that the dynamics of inference are a flow on that manifold equipped with the [[Fisher information metric]]. It joins three threads — Markov blankets (the boundary), information geometry (the metric on the belief space), and stochastic thermodynamics (the entropy production / dissipation accounting) — into one picture, supplying the geometric reading that the project's pullback move depends on.

## Problem & setting

A Markov-blanketed system at steady state has internal states `μ` that are conditionally independent of external states `η` given the blanket. Parr et al. ask: what is the *geometry* of the map from internal states to the conditional density `p(η | b)`? And how does the thermodynamic cost (entropy production) of maintaining the steady state relate to that geometry?

## Method

The internal-states-to-density map is treated as a parametrization of a statistical manifold; the natural metric on that manifold is the Fisher information metric, so belief updating is naturally a [[Natural gradient]] flow. Stochastic thermodynamics enters through the steady-state entropy production rate, decomposed (as in the broader Bayesian-mechanics program) via the Helmholtz/solenoidal split of the drift. The dissipative component drives the system up the gradient of model evidence; the conservative component supplies non-relaxational, orbiting dynamics.

## Key results

- **Internal states parametrize a density over external states** — stated and used as the defining property, with the parameter space carrying Fisher geometry. This is the exact precedent for the project's pullback construction.
- **Inference as Fisher-natural-gradient flow.** Free-energy descent is a Riemannian gradient flow under the Fisher metric, linking belief dynamics directly to information geometry.
- **Thermodynamic accounting.** Entropy production quantifies the dissipative cost of self-evidencing, tying the geometry to physical (thermodynamic) bookkeeping.

## Relevance to this research

This is the **exact precedent** for the pullback move in **[[participatory-it-from-bit]]**: internal/observer states parametrize a density over the external world, and the metric on that parameter space is the Fisher metric — so the apparent geometry of the world is the *pulled-back* information geometry of the observer's beliefs. The project's gauge-covariant transport of beliefs ([[Parallel transport]], [[Gauge transformation]]) is built on top of exactly this statistical-manifold-with-Fisher-metric structure, and the [[Natural gradient]] descent it uses for belief updates is the flow this paper identifies. The solenoidal/dissipative split underwrites the project's [[Hamiltonian belief dynamics]] and [[Belief inertia]] ([[Mass as Fisher information]] makes the Fisher metric play the role of inertia). For the multi-agent lift, each agent is a blanketed sub-system whose internal states carry such a manifold, stacked into [[Multi-agent variational free energy]] and [[Ouroboros multi-scale dynamics]]. See [[Bayesian mechanics]] for the program overview and [[Markov blanket interpretation debate]] for the contested assumptions.

## Cross-links

- Concepts: [[Fisher information metric]], [[Natural gradient]], [[Variational free energy]], [[Mass as Fisher information]], [[Hamiltonian belief dynamics]], [[Participatory realism (it from bit)]]
- New pages: [[Bayesian mechanics]], [[Markov blanket interpretation debate]]
- Themes: [[Information geometry and natural gradient]], [[Free-energy principle active inference]]
- Related sources: [[dacosta-2021-bayesian-mechanics]], [[friston-2019-particular-physics]], [[ramstead-2023-bayesian-mechanics]], [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]]
- Manuscript: [[participatory-it-from-bit]]

```bibtex
@article{parr2020markov,
  title   = {Markov blankets, information geometry and stochastic thermodynamics},
  author  = {Parr, Thomas and Da Costa, Lancelot and Friston, Karl},
  journal = {Philosophical Transactions of the Royal Society A},
  volume  = {378},
  number  = {2164},
  pages   = {20190159},
  year    = {2020},
  doi     = {10.1098/rsta.2019.0159},
  publisher = {The Royal Society}
}
```
