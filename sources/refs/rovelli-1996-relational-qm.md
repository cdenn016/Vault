---
type: reference
title: "Relational Quantum Mechanics"
aliases: ["Rovelli 1996"]
authors: ["Carlo Rovelli"]
year: 1996
tags: [cluster/participatory, project/multi-agent, field/physics, field/philosophy, cluster/participatory/quantum-foundations]
created: 2026-06-18
updated: 2026-06-18
---

# Relational Quantum Mechanics

> [!info] Citation
> Carlo Rovelli (1996). "Relational Quantum Mechanics." *International Journal of Theoretical Physics* **35**(8), 1637–1678. DOI: 10.1007/BF02302261. arXiv: quant-ph/9609002.

## TL;DR

Rovelli argues that the difficulties of interpreting quantum mechanics stem from the untenable assumption of an *observer-independent* state of a system. He proposes that quantum states and physical quantities are not absolute but *relational*: they are properties that one system has only *relative to another system* that interacts with it. The theory is then recast as describing the information that systems possess about one another, with no privileged observer and no observer/observed distinction.

## What it establishes

- **No absolute states.** There is no observer-independent description of a system's state. A state is always the state of one system *relative to* a second system. Different observers may give different, equally valid accounts of the same sequence of events; there is no "view from nowhere."
- **Quantum mechanics as a theory of relative information.** The wavefunction is not a description of an objective reality but a bookkeeping device encoding what one system "knows" about another, given their prior interaction. Measurement is just a physical interaction in which one system acquires information (becomes correlated) about another.
- **All systems are equivalent.** The observer plays no special role; any physical system can serve as the reference relative to which another system's quantities take definite values. This dissolves the measurement problem by denying that there is a frame-independent fact about when a "collapse" happens.
- **Reconstruction from informational postulates.** Rovelli frames the goal of interpretation as *deriving* the quantum formalism from simple physical/informational postulates (e.g. a bound on the relevant information obtainable about a system, and the possibility of always acquiring new information), prefiguring later information-theoretic reconstructions of quantum theory.

> [!note] Editorial: This note summarizes the conceptual content of the work itself; it does not report any results from the project manuscripts.

## Why the project cites it

The relational stance is a direct precedent for the project's [[Participatory realism (it from bit)]] commitments: facts are not pre-given but are constituted in the interaction between systems. This grounds the participatory reading of inference developed in [[participatory-it-from-bit]] and connects to Wheeler's "it from bit" ([[wheeler-1990-it-from-bit]]) and the QBist program ([[fuchs-2014-qbism]]), where probabilities and states are agent-relative.

The relational framing maps naturally onto the project's multi-agent architecture. Each agent in the [[Multi-agent variational free energy]] setting carries beliefs that are well-defined only *relative to its own generative model and local frame* — there is no global, agent-independent belief state. This is the inference-theoretic analogue of Rovelli's claim that quantities are defined only relative to a reference system. In the gauge-theoretic formulation, that frame-relativity is made precise: agents are [[Agents as fibre-bundle sections]], and comparing one agent's beliefs to another's requires [[Parallel transport]] along a connection, with the [[Holonomy]] measuring the failure of relational descriptions to agree globally under a [[Gauge transformation]]. Rovelli's "no view from nowhere" becomes the statement that there is no canonical global section.

Recasting quantum theory as *relative information* also motivates the project's information-geometric treatment of belief: if physics is about information one system holds about another, then the natural metric on that information — the [[Fisher information metric]] — and the dynamics that minimize surprise via [[Variational free energy]] become the appropriate physical language. The paper thus supports the cluster's broader thesis that participatory, agent-relative information is foundational rather than emergent.

## BibTeX

```bibtex
@article{rovelli1996relational,
  author  = {Rovelli, Carlo},
  title   = {Relational Quantum Mechanics},
  journal = {International Journal of Theoretical Physics},
  volume  = {35},
  number  = {8},
  pages   = {1637--1678},
  year    = {1996},
  doi     = {10.1007/BF02302261},
  eprint  = {quant-ph/9609002},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph}
}
```
