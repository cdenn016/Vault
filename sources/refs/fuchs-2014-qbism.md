---
type: reference
title: "An Introduction to QBism with an Application to the Locality of Quantum Mechanics"
aliases: ["Fuchs 2014", "Fuchs, Mermin & Schack 2014"]
authors: ["Christopher A. Fuchs", "N. David Mermin", "Rüdiger Schack"]
year: 2014
tags: [cluster/participatory, project/multi-agent, field/physics, field/philosophy, field/statistics, cluster/participatory/quantum-foundations]
created: 2026-06-18
updated: 2026-06-18
---

# An Introduction to QBism with an Application to the Locality of Quantum Mechanics

> [!info] Citation
> Fuchs, C. A., Mermin, N. D., & Schack, R. (2014). "An Introduction to QBism with an Application to the Locality of Quantum Mechanics." *American Journal of Physics*, **82**(8), 749–754. DOI: 10.1119/1.4874855.

## TL;DR

This paper is the canonical short introduction to QBism (Quantum Bayesianism), the interpretation in which a quantum state is not an objective feature of the world but a single agent's *personal, Bayesian* degrees of belief about the consequences of that agent's own actions on the world. The authors argue that taking probability to be strictly subjective dissolves the standard quantum "paradoxes," and they show in particular that the apparent nonlocality of quantum mechanics evaporates once measurement outcomes are understood as personal experiences elicited by the agent rather than as objective events.

## What it establishes

- **Quantum states as personal degrees of belief.** A wavefunction $|\psi\rangle$ encodes one agent's probabilistic expectations, assigned via the Born rule, for the experiences that agent will have upon acting on the world. Different agents may legitimately assign different states to the same system; there is no "true" state to be discovered.
- **The Born rule as a normative constraint.** Quantum mechanics functions as an addition to Bayesian probability theory — a *coherence* condition (an empirically motivated extension of Dutch-book consistency) that a rational agent uses to keep their gambling commitments mutually consistent, not a law describing objective propensities.
- **Measurement as participatory action.** A measurement is an action the agent takes on the world, and its outcome is an *experience* created in that act — not the revelation of a pre-existing value. The "collapse" of the state is simply the agent's Bayesian updating of beliefs in light of that experience.
- **Dissolution of nonlocality.** Because outcomes are personal experiences localized to the acting agent, correlations of the EPR/Bell type carry no instantaneous action at a distance: nothing objective propagates, so there is nothing nonlocal to explain. The authors present this as the headline application of the QBist stance.

## Why the project cites it

QBism supplies the philosophical backbone for the project's [[Participatory realism (it from bit)]] commitment: the idea that physical description is irreducibly indexed to an agent who acts, observes, and updates, rather than to a view from nowhere. This is the same move the project makes when it treats a model not as a passive estimator of an external state but as an agent maintaining beliefs that it revises by acting. In that sense QBism is the quantum-foundations precedent for the project's broader [[Participatory realism (it from bit)]] reading of [[wheeler-1990-it-from-bit]]'s "it from bit," and it sits naturally alongside relational [[rovelli-1996-relational-qm]] approaches in this cluster.

Concretely, the connections the project draws:

- **Belief as the primary object.** QBism's quantum state-as-personal-credence directly parallels the project's treatment of an agent's belief (its variational posterior) as the fundamental carried quantity. Updating that belief under new experience is exactly the move that [[Variational free energy]] minimization formalizes in the [[Free-energy principle active inference]] setting: the QBist "collapse-as-Bayesian-update" is the foundational-physics cousin of the project's variational belief update.
- **Many agents, many states.** That distinct agents hold distinct, equally valid states is the conceptual seed of the project's [[Multi-agent variational free energy]] picture and of [[Agents as fibre-bundle sections]] — each agent carries its own belief in its own local frame, with no privileged global state, echoing how a [[Gauge transformation]] relates agent-local descriptions without any of them being the "true" one.
- **Action and participation.** QBism's insistence that outcomes are produced by the agent's action, not read off the world, underwrites the project's active-inference framing in which perception and action jointly minimize free energy.

> [!note] Editorial: This paper is an interpretational and philosophical statement; it does not develop the information-geometric or gauge-theoretic machinery the project builds on top of it. Those formal links (e.g. to the [[Fisher information metric]] or to gauge structure) are the project's own contribution, motivated by — not asserted in — Fuchs, Mermin & Schack.

## BibTeX

```bibtex
@article{fuchs2014qbism,
  author  = {Fuchs, Christopher A. and Mermin, N. David and Schack, R{\"u}diger},
  title   = {An Introduction to {QBism} with an Application to the Locality of Quantum Mechanics},
  journal = {American Journal of Physics},
  volume  = {82},
  number  = {8},
  pages   = {749--754},
  year    = {2014},
  doi     = {10.1119/1.4874855}
}
```
