---
type: paper
title: "Relational Quantum Mechanics"
aliases:
  - "Rovelli 1996"
  - "RQM"
authors:
  - Rovelli, Carlo
year: 1996
arxiv: quant-ph/9609002
url: https://arxiv.org/abs/quant-ph/9609002
tags:
  - cluster/participatory/quantum-foundations
  - cluster/participatory
  - project/multi-agent
  - field/physics
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Relational Quantum Mechanics

> [!info] Citation
> Rovelli, Carlo (1996). "Relational Quantum Mechanics." arXiv:quant-ph/9609002v2 (published in International Journal of Theoretical Physics, 35, 1637–1678, 1996).

## TL;DR
Rovelli argues that the measurement problem in quantum mechanics stems from an incorrect assumption — that physical quantities and system states have observer-independent, absolute values. By dropping this assumption in favor of purely relational states (a state is always a state *relative to* some other physical system), quantum mechanics becomes internally consistent and complete. The theory is then reformulated as a description of the information that physical systems have about each other, reconstructed from two postulates about bounded and inexhaustible information, plus a superposition principle.

## Problem & setting
The measurement problem — why do different observers give different accounts of the same sequence of events — has resisted resolution across Copenhagen, many-worlds, consistent-histories, and modal interpretations for 70 years. Rovelli's "main observation" is that in standard quantum mechanics, observer O (who directly measures system S) and observer P (who treats O+S as a quantum system) necessarily give incompatible descriptions of the same event: for O the quantity q collapses to value 1; for P the composite state is a superposition. Rather than trying to "fix" collapse, Rovelli takes this observer-dependence as fundamental.

## Method
The core move is relational: quantum states and the values of physical quantities are declared intrinsically relational — always relative to a reference physical system, just as velocity is relative to a reference frame in classical mechanics. There is no absolute, observer-independent state of the world. "State" is replaced by the information one physical system has about another (in the Shannon/information-theoretic sense, requiring no conscious observer).

The reconstruction of quantum formalism proceeds from three postulates:

1. **Limited information (Postulate 1):** There is a maximum amount of relevant information N bits that can be extracted from any system S. This bounded information capacity corresponds to the finite-dimensional Hilbert space of the system, and Planck's constant emerges as the conversion factor between physical units and information-theoretic bits.

2. **Unlimited information (Postulate 2):** Even after N bits have been extracted, it is always possible to acquire new information about the system, entailing irreducible indeterminism (the outcomes cannot be fully determined by prior information).

3. **Superposition principle (Postulate 3):** The transition probabilities between two complete families of questions are given by the squared moduli of a unitary matrix, $p_{ij} = |U_{ij}|^2$, with the composition law $U_{cd} = U_{cb}U_{bd}$, recovering the full Hilbert-space formalism.

From these postulates, the orthomodular lattice structure of observables, Born's rule, Schrödinger dynamics (via time-translation symmetry), and the consistency of inter-observer communication all follow.

## Key results
The paper establishes: (1) the observer-dependence of quantum states is not a defect to be patched but a structural feature on par with the observer-dependence of velocity in special relativity; (2) two observers' accounts are always consistent when their communication is treated as a quantum interaction (no contradiction arises as long as comparison of information is itself modeled as a physical, hence quantum, process); (3) quantum mechanics is reconstructed (almost fully, modulo the third postulate) from information-theoretic axioms alone, without invoking collapse, consciousness, or classical/quantum splits; (4) the "third-person problem" (observer O measured by observer P) is resolved by the relational framework: P can confirm O has measured S (via the correlation operator M) without knowing O's outcome, and consistency is guaranteed by von Neumann's chain.

## Relevance to this research
Rovelli's relational quantum mechanics is a direct antecedent and philosophical grounding for the **participatory realism** and **"it from bit"** framework developed in the PIFB manuscript. The identification of physical reality with the information systems have about each other — with no privileged observer-independent description — maps directly onto the participatory ontology in which observation constitutes relational facts. The two postulates (bounded and inexhaustible information) are structurally analogous to the bounded capacity / new-information-from-interaction schema in active inference and variational free energy minimization, where a belief state is always relative to a model and updated by sensory interaction. The reconstruction of unitary dynamics from information-theoretic postulates (Postulate 3 and the consistency of inter-observer descriptions) has a counterpart in the gauge-theoretic VFE framework, where GL(K)-equivariant transport and the softmax attention distribution emerge as the unique self-consistent information-coupling under free energy minimization. The multi-agent extension of RQM — where each agent holds a distinct relative description, and inter-agent consistency is enforced only through physical interaction — is structurally isomorphic to the multi-agent active inference architecture in the MAgent model.

## Cross-links
- Concepts: [[Participatory Realism]], [[It from Bit]], [[Relational Quantum Mechanics]], [[Information Geometry]]
- Related sources: [[wheeler-1989-it-from-bit]], [[friston-2023-path-integrals-active-inference]], [[von-neumann-1932-mathematical-foundations]]
- Manuscript/Project: [[PIFB]], [[VFE Transformer Program]], [[MAgent Model]]

## BibTeX
```bibtex
@article{Rovelli1996,
  author  = {Rovelli, Carlo},
  title   = {Relational Quantum Mechanics},
  journal = {International Journal of Theoretical Physics},
  year    = {1996},
  volume  = {35},
  pages   = {1637--1678},
  archivePrefix = {arXiv},
  eprint  = {quant-ph/9609002},
}
```
