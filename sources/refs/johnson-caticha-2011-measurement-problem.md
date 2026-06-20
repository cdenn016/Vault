---
type: reference
title: "Entropic Dynamics and the Quantum Measurement Problem"
aliases:
  - "Johnson & Caticha 2011"
  - "Johnson-Caticha (2011) Measurement Problem"
authors:
  - David T. Johnson
  - Ariel Caticha
year: 2011
tags:
  - cluster/info-geometry
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/statistics
  - field/philosophy
  - cluster/participatory/quantum-foundations
created: 2026-06-19
updated: 2026-06-19
---

# Entropic Dynamics and the Quantum Measurement Problem

> [!info] Citation
> David T. Johnson and Ariel Caticha (2011/2012). "Entropic dynamics and the quantum measurement problem." In *Bayesian Inference and Maximum Entropy Methods in Science and Engineering (MaxEnt 2011)*, AIP Conference Proceedings 1443: 104–116 (2012). Preprint: [arXiv:1108.2550](https://arxiv.org/abs/1108.2550).

## TL;DR

Johnson and Caticha apply the Entropic Dynamics framework to the measurement problem and argue that quantum mechanics' two apparently distinct modes of evolution — smooth unitary (Schrödinger) evolution and abrupt wave-function "collapse" on measurement — are both instances of a *single* process: entropic updating of probabilities. Collapse is not a separate dynamical law but a Bayesian/entropic information update triggered by acquiring measurement data. The measurement problem dissolves once the quantum state is read as an agent's information rather than an ontic object.

## What it establishes

- **Unified evolution.** Unitary evolution and collapse are two limits of the same entropic-inference update rule, removing the need for a separate projection postulate.
- **Collapse as updating.** Measurement "collapse" is the entropic/Bayesian conditioning of the probability distribution on new data — an epistemic update, continuous with ordinary inference.
- **Epistemic state.** Reinforces the ED reading of the wave function as a representation of information, supporting an observer-centric interpretation of quantum theory.

> [!note] Editorial: This note summarizes the paper's argument from its abstract and the ED literature; specific technical steps should be checked against the proceedings text before quotation.

## Why the project cites it

This reference grounds [[participatory-it-from-bit]]'s "collapse as consensus" claim. PIFB recasts the abrupt updating of an agent's beliefs upon receiving information as the analogue of measurement collapse, and in the multi-agent setting it reads collective convergence as a consensus-driven update — the social-physics counterpart of measurement. Johnson–Caticha supply the physics precedent: collapse *is* entropic updating, the very operation the project's [[Variational free energy]] and entropy-regularized consensus dynamics perform on belief tuples. The same MaxEnt updating that drives the softmax/[[Multi-agent variational free energy|multi-agent VFE]] coupling is, in this reading, the mechanism of "measurement" on beliefs. The note ties to the cited ED core [[caticha-bartolomeo-reginatto-2015-entropic-dynamics]] and the review [[caticha-2019-entropic-dynamics]], to the [[Fisher information metric]] geometry they share, and to the [[Participatory realism (it from bit)]] thread alongside [[wheeler-1990-it-from-bit]]. Links the manuscript [[participatory-it-from-bit]].

```bibtex
@inproceedings{johnson2012entropic,
  author    = {Johnson, David T. and Caticha, Ariel},
  title     = {Entropic dynamics and the quantum measurement problem},
  booktitle = {Bayesian Inference and Maximum Entropy Methods in Science and Engineering (MaxEnt 2011)},
  series    = {AIP Conference Proceedings},
  volume    = {1443},
  pages     = {104--116},
  year      = {2012},
  publisher = {AIP Publishing},
  doi       = {10.1063/1.3703626},
  note      = {arXiv:1108.2550}
}
```
