---
type: paper
title: "Gravitation from Entanglement in Holographic CFTs"
aliases:
  - "Faulkner et al. 2014"
  - "Gravitation from Entanglement"
authors:
  - Thomas Faulkner
  - Monica Guica
  - Thomas Hartman
  - Robert C. Myers
  - Mark Van Raamsdonk
year: 2014
arxiv: 1312.7856
url: https://arxiv.org/abs/1312.7856
tags:
  - cluster/participatory
  - project/multi-agent
  - field/physics
  - cluster/participatory/quantum-foundations
created: 2026-06-19
updated: 2026-06-19
---

# Gravitation from Entanglement in Holographic CFTs

> [!info] Citation
> Thomas Faulkner, Monica Guica, Thomas Hartman, Robert C. Myers and Mark Van Raamsdonk (2014). "Gravitation from entanglement in holographic CFTs." *Journal of High Energy Physics* 2014(3): 51. DOI: [10.1007/JHEP03(2014)051](https://doi.org/10.1007/JHEP03(2014)051). Preprint: [arXiv:1312.7856](https://arxiv.org/abs/1312.7856).

## TL;DR

This paper turns Van Raamsdonk's slogan "spacetime is built from entanglement" into a derivation. Starting from the *entanglement first law* — the statement that, to linear order around the vacuum, the change in a region's entanglement entropy equals the change in its modular (entanglement) Hamiltonian, $\delta S = \delta \langle H_{\mathrm{mod}}\rangle$ — and combining it with the Ryu–Takayanagi area prescription, the authors show that the linearized Einstein equations in the AdS bulk are *equivalent* to the first law holding for every ball-shaped boundary region. Bulk gravitational dynamics is thereby recovered from a purely information-theoretic constraint on the boundary CFT.

## Problem & setting

[[ryu-takayanagi-2006-holographic-entanglement-entropy]] identifies entanglement entropy with bulk minimal-surface area, and [[VanRaamsdonk-2010-spacetime-entanglement|vanraamsdonk-2010-entanglement-spacetime]] argues qualitatively that entanglement glues geometry together. What was missing was a quantitative bridge showing that the *dynamical* law of gravity (not just the kinematics of distance) follows from entanglement. This work supplies that bridge in the linearized regime.

## Method

The entanglement first law for a CFT ball-region is rewritten holographically via RT, yielding an integral constraint on the bulk metric perturbation. Demanding the constraint hold for all ball regions and all boundary positions is shown to be precisely the bulk linearized Einstein equation sourced by the perturbation's stress tensor.

## Key results

Linearized Einstein equations emerge from the first law of entanglement; the result is independent of the bulk Lagrangian's higher-curvature details at linear order, and connects directly to Jacobson's thermodynamic derivation of gravity by recasting the Clausius-like relation as an entanglement constraint.

## Relevance to this research

This is the technical hinge between the two emergent-gravity strands the PIFB manuscript ([[participatory-it-from-bit]]) leans on: Jacobson's thermodynamic-of-spacetime derivation ([[jacobson-1995-einstein-equation-of-state|jacobson-1995-thermodynamics-spacetime]]) and Van Raamsdonk's entanglement-builds-geometry picture. It shows that a *variational/stationarity* statement about an information functional yields field equations for a metric — exactly the structural move PIFB proposes when it asks whether stationarity of [[Variational free energy]] over belief fibres can induce dynamics on an emergent base manifold via the pullback of the [[Fisher information metric]]. The "first law" here is the entanglement analogue of PIFB's claim that information determines geometry; it anchors the [[Emergent spacetime and holography]] theme and sharpens the [[Participatory realism (it from bit)]] thread by making the it-from-bit dependence quantitative rather than slogan-level.

## Cross-links
- Concepts: [[Participatory realism (it from bit)]], [[Fisher information metric]]
- Themes: [[Emergent spacetime and holography]]
- Related sources: [[jacobson-1995-einstein-equation-of-state|jacobson-1995-thermodynamics-spacetime]], [[VanRaamsdonk-2010-spacetime-entanglement|vanraamsdonk-2010-entanglement-spacetime]], [[ryu-takayanagi-2006-holographic-entanglement-entropy]], [[jacobson-2016-entanglement-equilibrium]], [[wheeler-1990-it-from-bit]]

## BibTeX
```bibtex
@article{faulkner2014gravitation,
  author  = {Faulkner, Thomas and Guica, Monica and Hartman, Thomas and Myers, Robert C. and Van Raamsdonk, Mark},
  title   = {Gravitation from entanglement in holographic {CFTs}},
  journal = {Journal of High Energy Physics},
  year    = {2014},
  volume  = {2014},
  number  = {3},
  pages   = {51},
  doi     = {10.1007/JHEP03(2014)051},
  eprint  = {1312.7856},
  archivePrefix = {arXiv},
  primaryClass  = {hep-th}
}
```
