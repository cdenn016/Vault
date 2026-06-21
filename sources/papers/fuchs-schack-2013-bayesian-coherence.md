---
type: paper
title: "Quantum-Bayesian Coherence"
aliases:
  - "Fuchs & Schack 2013"
  - "Quantum-Bayesian coherence"
  - "QBism Born rule"
authors:
  - Fuchs, Christopher A.
  - Schack, Rüdiger
year: 2013
arxiv: "1301.3274"
url: https://doi.org/10.1103/RevModPhys.85.1693
tags:
  - cluster/participatory/quantum-foundations
  - project/multi-agent
  - field/physics
  - field/philosophy
status: stable
created: 2026-06-19
updated: 2026-06-20
---

# Quantum-Bayesian Coherence

> [!info] Citation
> Fuchs, C. A., & Schack, R. (2013). "Quantum-Bayesian coherence." *Reviews of Modern Physics* **85**(4), 1693–1715. DOI: [10.1103/RevModPhys.85.1693](https://doi.org/10.1103/RevModPhys.85.1693). Preprint: arXiv:1301.3274.

## TL;DR

This is the technical core of QBism. Fuchs and Schack take the Born rule not as a law about objective propensities but as an empirically motivated addition to personal Bayesian probability — a normative coherence condition a single agent imposes on its own gambling commitments. The centerpiece is a reformulation in terms of a symmetric informationally complete positive-operator-valued measure (SIC-POVM): if an agent fixes credences for the outcomes of a fiducial SIC measurement, the Born rule for any other measurement becomes a deformation of the classical law of total probability connecting the SIC credences to the new measurement's credences. Quantum mechanics is thereby recast as a single, dimension-dependent constraint among an agent's subjective probabilities, with no appeal to objective quantum states.

## Problem & setting

QBism holds that the quantum state is a single agent's degrees of belief, not a feature of the world. The challenge is to make this precise: if the wavefunction is subjective, what fixes the Born rule, and in what sense is it a constraint on belief rather than a law of nature? The setting is finite-dimensional quantum theory equipped with a SIC-POVM as a reference (fiducial) measurement — a maximally symmetric informationally complete measurement whose existence in every dimension is conjectured and verified in many cases.

## Method

The authors express an arbitrary quantum measurement's outcome probabilities purely in terms of the agent's probabilities for the fiducial SIC outcomes. The Born rule then takes the form of a "primal" equation — a near-classical relation between the two probability vectors, differing from the law of total probability by a fixed, dimension-dependent term. This recasts the quantum formalism entirely in probability space: states and effects disappear in favor of probability assignments, and the only nonclassical residue is the specific numerical deformation of total probability. Coherence (Dutch-book-style consistency) plus this single deformation is shown to reproduce quantum predictions.

## Key results

The Born rule is exhibited as a single quantitative coherence condition on an agent's subjective probabilities, the "fundamental equation" of QBism, expressed through SIC-POVMs. This supplies the rigorous backbone the QBist program needed: it demonstrates that quantum theory can be written without ever positing an objective state, as a normative addition to Bayesian probability calculus. It also ties the structure of quantum theory to the (conjectured) existence of SICs, sharpening the question of why nature admits this particular deformation.

## Relevance to this research

Fuchs-Schack supplies the technical model the project leans on when it claims that "probability is an agent's commitment, and physics constrains it" — the engine behind the participatory reading in [[participatory-it-from-bit]]. The project's beliefs are variational posteriors that an agent revises to minimize [[Variational free energy]]; QBism's "Born rule as coherence constraint on personal credence" is the foundational-physics analogue of treating the belief update as a normative, agent-internal consistency condition rather than estimation of an external truth. The move that probabilities live with the agent and the formalism only constrains how they hang together is exactly the project's stance in [[Multi-agent variational free energy]], where each agent maintains its own coherent belief and no global state is privileged. The SIC reformulation — quantum theory as a near-classical deformation in pure probability space — also resonates with the project's information-geometric outlook ([[Fisher information metric]], [[Quantum information geometry]]): structure is encoded in relations among probability assignments, and the deformation away from classical total probability is a candidate geometric signature. This is the precise QBist counterpart to the looser interpretive statement in [[fuchs2014-qbism-locality|fuchs-2014-qbism]].

## Cross-links

- Concepts: [[QBism]], [[Quantum information geometry]], [[Participatory realism (it from bit)]]
- Related sources: [[fuchs2014-qbism-locality|fuchs-2014-qbism]], [[fuchs-2017-participatory-realism]], [[hardy-2001-five-axioms]], [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]]
- Manuscript/Project: [[participatory-it-from-bit]]

## BibTeX

```bibtex
@article{Fuchs2013,
  author        = {Fuchs, Christopher A. and Schack, R{\"u}diger},
  title         = {Quantum-{B}ayesian coherence},
  journal       = {Reviews of Modern Physics},
  volume        = {85},
  number        = {4},
  pages         = {1693--1715},
  year          = {2013},
  doi           = {10.1103/RevModPhys.85.1693},
  eprint        = {1301.3274},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph}
}
```
