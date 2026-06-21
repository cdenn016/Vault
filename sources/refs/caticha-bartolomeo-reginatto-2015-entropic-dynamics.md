---
type: reference
title: "Entropic Dynamics: from Entropy and Information Geometry to Hamiltonians and Quantum Mechanics"
aliases:
  - "Caticha, Bartolomeo & Reginatto 2015"
  - "Entropic Dynamics (MaxEnt 2014)"
authors:
  - Ariel Caticha
  - Daniel Bartolomeo
  - Marcel Reginatto
year: 2015
tags:
  - cluster/info-geometry
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/statistics
  - cluster/participatory/quantum-foundations
created: 2026-06-19
updated: 2026-06-19
---

# Entropic Dynamics: from Entropy and Information Geometry to Hamiltonians and Quantum Mechanics

> [!info] Citation
> Ariel Caticha, Daniel Bartolomeo, and Marcel Reginatto (2015). "Entropic Dynamics: from Entropy and Information Geometry to Hamiltonians and Quantum Mechanics." In *Bayesian Inference and Maximum Entropy Methods in Science and Engineering (MaxEnt 2014)*, AIP Conference Proceedings 1641: 155–164. Preprint: [arXiv:1412.5629](https://arxiv.org/abs/1412.5629).

## TL;DR

The compact core statement of the Entropic Dynamics (ED) program: quantum mechanics is derived as an application of entropic inference. Starting from probabilities over configuration space and the [[Fisher information metric]] as the natural geometry on that statistical manifold, the authors show how *non-dissipative* entropic updating generates a Hamiltonian flow, and how the quantum potential — the term that turns classical dynamics into the Schrödinger equation — arises directly from the information geometry. Entropy supplies the update rule; information geometry supplies the metric; together they yield Hamiltonian quantum dynamics.

## What it establishes

- **Dynamics as entropic inference.** Time evolution is built from successive maximum-entropy updates of a probability distribution under constraints, with no independent dynamical postulate.
- **Hamiltonian flow from non-dissipative ED.** A particular (energy-conserving) class of entropic updates reproduces Hamiltonian mechanics; the conserved "energy" and the symplectic structure emerge rather than being assumed.
- **Quantum potential from information geometry.** The Fisher-information contribution to the dynamics is the quantum potential, recovering the Schrödinger equation — the same Fisher term identified in the minimum-Fisher derivation of co-author Reginatto ([[reginatto-1998-fisher-quantum]]).

> [!note] Editorial: This conference paper is the condensed, jointly authored statement of the ED program later reviewed at length in [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]]; the wiki previously held only the 2019 review.

## Why the project cites it

This is the *cited* entropic-dynamics core for [[participatory-it-from-bit]] — the precise, multi-author primary source for "dynamics as inference on a Fisher-geometric belief manifold," whereas the vault otherwise held only the single-author 2019 review ([[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]]). PIFB's argument that belief dynamics inherit physical structure (Hamiltonian flow, a quantum-like potential) from the [[Fisher information metric]] on belief space is the ED move applied to agents; this paper supplies the cleanest citable derivation. Reginatto's co-authorship links it tightly to the project's [[Mass as Fisher information]] thread and to the minimum-Fisher route of [[reginatto-1998-fisher-quantum]], giving the manuscript two complementary lineages (entropy-side ED and metric-side minimum-Fisher) that converge on the same Schrödinger endpoint. The note links the [[Physics from Fisher information]] theme, the [[Information geometry and natural gradient]] theme, and the [[Participatory realism (it from bit)]] framing.

```bibtex
@inproceedings{caticha2015entropic,
  author    = {Caticha, Ariel and Bartolomeo, Daniel and Reginatto, Marcel},
  title     = {Entropic Dynamics: from Entropy and Information Geometry to Hamiltonians and Quantum Mechanics},
  booktitle = {Bayesian Inference and Maximum Entropy Methods in Science and Engineering (MaxEnt 2014)},
  series    = {AIP Conference Proceedings},
  volume    = {1641},
  pages     = {155--164},
  year      = {2015},
  publisher = {AIP Publishing},
  doi       = {10.1063/1.4905974},
  note      = {arXiv:1412.5629}
}
```
