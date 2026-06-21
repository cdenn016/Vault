---
type: paper
title: "A no-go theorem for observer-independent facts"
aliases:
  - "Brukner 2018"
  - "no-go observer-independent facts"
authors:
  - Brukner, Časlav
year: 2018
arxiv: "1804.00749"
url: https://arxiv.org/abs/1804.00749
tags:
  - cluster/participatory/quantum-foundations
  - cluster/participatory/philosophy-of-mind
  - project/multi-agent
  - field/physics
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A no-go theorem for observer-independent facts

> [!info] Citation
> Brukner, Č. (2018). "A no-go theorem for observer-independent facts." arXiv:1804.00749 [quant-ph].

## TL;DR
Brukner derives a Bell-type no-go theorem showing that the assumptions of (1) universal validity of quantum theory, (2) locality, (3) freedom of choice, and (4) observer-independent facts are mutually incompatible. Using an extended Wigner's friend scenario with two super-observers (Alice and Bob) each measuring an entangled laboratory-plus-friend system, the quantum prediction violates the CHSH bound ($S_Q = 2\sqrt{2} > 2$), ruling out any theoretical framework — quantum or otherwise — in which facts observed by different observers can be jointly assigned truth values in a single Boolean algebra. The result suggests that facts in quantum theory are inherently relational, defined only relative to an observer and her experimental arrangement.

## Problem & setting
The Wigner's friend thought experiment poses the question of whether the definite outcome perceived by the friend inside a sealed laboratory and the entangled state assigned by Wigner outside can both be treated as objective, observer-independent "facts of the world." Prior to this work, interpretations such as relational quantum mechanics, QBism, and the Copenhagen interpretation accepted observer-relative facts, while collapse models predicted a breakdown of quantum superposition at macroscopic scale. Brukner formalises the question: is there any theory (not just quantum theory) admitting a joint probability measure over the observational propositions of Wigner and his friend?

## Method
The proof constructs a Bell experiment at the level of entire observer-laboratory systems. Two pairs of observers are considered: super-observers Alice and Bob, each performing measurements on a laboratory containing an inner observer (Charlie and Debbie respectively) who has already measured an entangled spin-1/2 particle. The initial two-spin state is

$$|\psi\rangle_{S_1 S_2} = -\sin\tfrac{\theta}{2}|\phi^+\rangle + \cos\tfrac{\theta}{2}|\psi^-\rangle,$$

and after Charlie and Debbie complete their measurements (described unitarily by Alice and Bob), the joint state is an entangled superposition of compound "up/down" laboratory states. With $\theta = \pi/4$, Alice and Bob each choose between the friend-type observable ($A_1, B_1 = \hat{A}_z, \hat{B}_z$) and the Wigner-type observable ($A_2, B_2 = \hat{A}_x, \hat{B}_x$). The assumptions (2)–(4) jointly imply the existence of local hidden variables and hence the CHSH inequality $S \leq 2$, which quantum mechanics violates ($S_Q = 2\sqrt{2}$). A GHZ extension with three friends and three Wigners is given in the appendix, providing a deterministic (probability-free) version of the incompatibility.

## Key results
The four assumptions — universal quantum validity, locality, freedom of choice, and observer-independent facts — are jointly inconsistent. Any theory satisfying the first three cannot accommodate a joint Boolean algebra of truth values for observations made by different observers. The quantum CHSH value $2\sqrt{2}$ witnesses this violation. The GHZ extension shows the contradiction is not merely statistical: it holds deterministically, with $\hat{A}_x\hat{B}_x\hat{C}_x|\Psi_\mathrm{GHZ}\rangle = -|\Psi_\mathrm{GHZ}\rangle$ contradicting the value $+1$ required by the hidden-variable constraints $A_x B_y C_y = A_y B_x C_y = A_y B_y C_x = 1$. Brukner also argues that the "self-consistency" requirement (SC) of Frauchiger and Renner (arXiv:1604.07422) is equivalent to assuming a single shared Boolean algebra across observers — the very assumption the no-go theorem rules out.

## Relevance to this research
This paper is a foundational reference for the participatory realism strand of the VFE research program and the PIFB manuscript. The core result — that observer-relative facts cannot be amalgamated into a single objective description — provides quantum-mechanical grounding for the participatory "it-from-bit" ontology in which each agent holds a local, frame-dependent belief state. In the gauge-theoretic VFE framework, the GL(K) gauge freedom precisely encodes this observer-relativity: belief tuples $(\mu_i, \Sigma_i)$ are defined relative to an agent's local frame, and the gauge transport $\Omega_{ij}$ relates frames without requiring a global, observer-independent ground truth. The no-go theorem thus offers independent justification for why a globally commuting Boolean algebra of agent beliefs cannot exist, directly motivating the relational structure of VFE attention (belief coupling via transported KL divergences) and the multi-agent active inference architecture in which shared facts are emergent rather than pre-given.

## Cross-links
- Concepts: [[Participatory Realism]], [[Wigner's Friend]], [[Observer-Relative Facts]], [[Bell Inequalities]], [[Relational Quantum Mechanics]]
- Related sources: [[brukner-2016-quantum-measurement-problem]], [[frauchiger-renner-2018-self-consistent]]
- Manuscript/Project: [[PIFB]], [[VFE Transformer Program]], [[GL(K) Attention]]

## BibTeX
```bibtex
@article{Brukner2018,
  author  = {Brukner, \v{C}aslav},
  title   = {A no-go theorem for observer-independent facts},
  year    = {2018},
  eprint  = {1804.00749},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph},
}
```
