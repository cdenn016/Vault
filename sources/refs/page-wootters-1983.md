---
type: reference
title: "Evolution without Evolution: Dynamics Described by Stationary Observables"
aliases: ["Page 1983", "Page & Wootters 1983"]
authors: ["Don N. Page", "William K. Wootters"]
year: 1983
tags: [cluster/participatory, project/multi-agent, field/physics, cluster/participatory/quantum-foundations]
created: 2026-06-18
updated: 2026-06-18
---

# Evolution without Evolution: Dynamics Described by Stationary Observables

> [!info] Citation
> Page, D. N., & Wootters, W. K. (1983). *Evolution without Evolution: Dynamics Described by Stationary Observables.* Physical Review D, **27**(12), 2885–2892. DOI: 10.1103/PhysRevD.27.2885.

## TL;DR

Page and Wootters show that a closed quantum system in a *stationary* (energy-eigenstate) global state can nonetheless exhibit apparent dynamical evolution, provided one reads time off an internal "clock" subsystem rather than an external parameter. Conditioning the global state on successive readings of the clock recovers the ordinary Schrödinger evolution of the rest of the system, so dynamics becomes a pattern of *correlations* among stationary observables rather than a primitive flow in external time.

## What it establishes

The paper begins from the observation that the time parameter $t$ in the Schrödinger equation is not itself an observable. For a closed system such as the Universe, this leads to a superselection rule on energy: physical observables must commute with the Hamiltonian and are therefore stationary. At face value this seems to forbid any evolution at all.

The resolution is relational. Partition the global Hilbert space into a "clock" $C$ and a "rest" $R$, and take the total state $|\Psi\rangle$ to satisfy a constraint $\hat{H}_{\text{tot}}|\Psi\rangle = 0$ (or, more generally, to be an energy eigenstate). Evolution of $R$ is then encoded as a *conditional* state: fixing the clock observable to read $t$ projects out a $|\psi_R(t)\rangle$, and the family of such conditional states obeys the usual time-dependent Schrödinger equation in the clock variable $t$. Thus:

$$ |\Psi\rangle = \sum_t |t\rangle_C \otimes |\psi_R(t)\rangle, \qquad i\,\partial_t |\psi_R(t)\rangle = \hat{H}_R |\psi_R(t)\rangle . $$

The "flow of time" is reinterpreted as correlation structure within a globally timeless state: nothing evolves with respect to an outside parameter, yet an internal observer reading the clock infers a fully dynamical history. This is the now-canonical *Page–Wootters mechanism*, foundational to relational and timeless approaches to quantum mechanics and quantum gravity.

## Why the project cites it

The project's participatory thread treats physical and inferential dynamics as emergent from relational, observer-conditioned structure rather than as primitive external processes — the same move Page and Wootters make for time. It sits naturally alongside [[Participatory realism (it from bit)]] and the manuscript [[participatory-it-from-bit]], where physics is reconstructed from acts of observation and conditioning rather than from a pre-given background.

Concretely, the Page–Wootters construction is a clean precedent for the project's claim that apparent evolution can arise from *conditioning a static joint distribution* — the same logic underlying belief updating in [[Variational free energy]] and [[Multi-agent variational free energy]], where an agent's trajectory is a sequence of conditional posteriors rather than motion in an external time. The clock-as-reference-frame idea also resonates with [[Agents as fibre-bundle sections]]: choosing which subsystem reads "now" is a choice of reference frame analogous to a [[Gauge transformation]], and physically meaningful content lives in the relational, frame-independent correlations. This relational stance connects to the broader participatory cluster's neighbours such as [[rovelli-1996-relational-qm]], [[fuchs2014-qbism-locality|fuchs-2014-qbism]], and [[wheeler-1990-it-from-bit]].

> [!note] Editorial: The specific bridge to variational free energy, gauge structure, and multi-agent belief dynamics is the project's own framing; Page and Wootters (1983) address only the quantum-mechanical timelessness/relational-time problem and make no claims about inference or gauge theory.

```bibtex
@article{PageWootters1983,
  title   = {Evolution without Evolution: Dynamics Described by Stationary Observables},
  author  = {Page, Don N. and Wootters, William K.},
  journal = {Physical Review D},
  volume  = {27},
  number  = {12},
  pages   = {2885--2892},
  year    = {1983},
  publisher = {American Physical Society},
  doi     = {10.1103/PhysRevD.27.2885}
}
```
