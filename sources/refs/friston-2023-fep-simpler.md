---
type: reference
title: "The free energy principle made simpler but not too simple"
aliases:
  - "Friston et al. 2023"
  - "Friston (2023) FEP Made Simpler"
authors:
  - Karl Friston
  - Lancelot Da Costa
  - Noor Sajid
  - Conor Heins
  - Kai Ueltzhoffer
  - Grigorios A. Pavliotis
  - Thomas Parr
year: 2023
tags:
  - cluster/vfe
  - cluster/participatory
  - cluster/info-geometry
  - project/multi-agent
  - project/transformer
  - field/neuroscience
  - field/physics
  - field/statistics
  - cluster/participatory/consciousness
created: 2026-06-19
updated: 2026-06-19
---

# The free energy principle made simpler but not too simple

> [!info] Citation
> Friston, K., Da Costa, L., Sajid, N., Heins, C., Ueltzhöffer, K., Pavliotis, G. A., & Parr, T. (2023). "The free energy principle made simpler but not too simple." *Physics Reports* **1024**: 1–29. DOI: [10.1016/j.physrep.2023.07.001](https://doi.org/10.1016/j.physrep.2023.07.001).

## TL;DR

This is the consolidated, self-contained statement of the free-energy principle and **[[Bayesian mechanics]]** that strips the program to its mathematical essentials while retaining the steady-state, Markov-blanket, and synchronization-map machinery. It derives, from the stationary density of a random dynamical system and its Helmholtz decomposition, the claim that internal states of a blanketed system parametrize beliefs about external states and flow so as to minimize [[Variational free energy]]. It is the compact reference the project adopts when it needs the precise contemporary form of FEP / Bayesian mechanics.

## What it establishes

- **A clean derivation chain.** From non-equilibrium steady state + Markov blanket + Helmholtz (gradient + solenoidal) decomposition to the inference reading, with the assumptions stated plainly.
- **Mode- and path-tracking forms.** Both the steady-state (most-likely-internal-state) and path-integral formulations of Bayesian mechanics, with their respective conditions.
- **Information-geometric flow.** Free-energy descent as a gradient flow under the [[Fisher information metric]], i.e. [[Natural gradient]] dynamics on the belief manifold.

## Why the project cites it

This is the **compact FEP / Bayesian-mechanics statement the project adopts** as its canonical contemporary reference for the single-observer case that [[participatory-it-from-bit]] generalizes. PIFB takes this derivation — internal states parametrize a density over external states, dynamics minimize variational free energy on a Fisher-geometric manifold — and adds the gauge structure ([[Gauge transformation]], [[Parallel transport]]) and the multi-agent / multi-scale stack ([[Multi-agent variational free energy]], [[Ouroboros multi-scale dynamics]]) absent here. The solenoidal component of the flow is the project's [[Hamiltonian belief dynamics]] / [[Belief inertia]]; the Fisher-natural-gradient descent is its belief-update rule; [[Mass as Fisher information]] reads the metric as inertia. Because this paper lays its assumptions bare, it is also the cleanest target for the [[Markov blanket interpretation debate]] critiques (Bruineberg, Aguilera, Biehl) that PIFB must engage. Companion sources: [[friston-2019-particular-physics]], [[dacosta-2021-bayesian-mechanics]], [[parr-2020-markov-blankets-thermodynamics]], [[ramstead-2023-bayesian-mechanics]].

```bibtex
@article{friston2023simpler,
  title   = {The free energy principle made simpler but not too simple},
  author  = {Friston, Karl and Da Costa, Lancelot and Sajid, Noor and Heins, Conor and Ueltzh{\"o}ffer, Kai and Pavliotis, Grigorios A. and Parr, Thomas},
  journal = {Physics Reports},
  volume  = {1024},
  pages   = {1--29},
  year    = {2023},
  doi     = {10.1016/j.physrep.2023.07.001},
  publisher = {Elsevier}
}
```
