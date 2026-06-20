---
type: paper
title: "Quantum Mechanics and the Covariance of Physical Laws in Quantum Reference Frames"
aliases: ["Giacomini, Castro-Ruiz & Brukner 2019", "QRF covariance", "Giacomini 2019"]
authors: ["Flaminia Giacomini", "Esteban Castro-Ruiz", "Časlav Brukner"]
year: 2019
arxiv: "1712.07207"
url: https://arxiv.org/abs/1712.07207
tags: [cluster/participatory, cluster/gauge-theory, project/multi-agent, field/physics, cluster/participatory/quantum-foundations]
created: 2026-06-19
updated: 2026-06-19
---

# Quantum Mechanics and the Covariance of Physical Laws in Quantum Reference Frames

> [!info] Citation
> Giacomini, F., Castro-Ruiz, E., & Brukner, Č. (2019). "Quantum mechanics and the covariance of physical laws in quantum reference frames." *Nature Communications* **10**, 494. DOI: 10.1038/s41467-018-08155-0. Preprint: arXiv:1712.07207.

## TL;DR

The paper promotes a *reference frame* itself to a quantum system and asks how physical descriptions transform when one changes from one quantum reference frame (QRF) to another that may be in a superposition of positions or momenta relative to the first. The authors construct explicit unitary "QRF transformations" generalizing the classical Galilean change of frame, and show that the laws of physics can be made *covariant* under these quantum changes of perspective: what looks like an entangled, delocalized state from one frame can look like a sharp, classical state from another. The work is the founding statement of the Vienna QRF program and reframes superposition and entanglement as frame-dependent — relative to a quantum observer's perspective rather than absolute.

## Problem & setting

Classical physics lets observers attach a coordinate frame to any system and demands that laws be covariant under frame changes (Galilean, Lorentzian). But standard quantum mechanics tacitly assumes a *classical* external reference frame — an idealized rigid rod and clock with no quantum degrees of freedom. Giacomini et al. ask what happens when the reference is itself a quantum particle that can be in superposition. The setting is nonrelativistic quantum mechanics of a few particles, with the position and momentum of one particle reinterpreted as defining the origin of a frame.

## Method

The authors define a unitary operator that transforms states and observables from the frame of particle A to the frame of particle B, generalizing the translation that classically relates the two origins to a *coherent, state-dependent* transformation built from relative coordinates. Applying it, they recompute entanglement, superposition, and the form of dynamical equations across frames. The construction is operator-level and exact for the Galilean case, and the covariance of the Schrödinger dynamics under the QRF map is verified explicitly.

## Key results

Entanglement and superposition are shown to be *relative to the reference frame*: a state that is product and definite in one QRF can be entangled and indefinite in another, so these are not frame-invariant properties. The Schrödinger equation retains its form under QRF change provided the Hamiltonian is transformed appropriately — covariance of the laws is preserved. The notion of a particle "at rest" or "in a definite position" becomes frame-relative, extending the relativity of motion into the quantum domain. The framework launched a research line (perspective-neutral formulations, general symmetry groups) elaborated in follow-up work.

## Relevance to this research

This is the most literal physics precedent for the project's central structural claim in [[participatory-it-from-bit]]: that *gauge covariance is the formal expression of shareability between agents*. Where Giacomini et al. demand that physical laws be covariant under a change of quantum reference frame, the project demands that an agent's belief content be covariant under a change of agent frame — and realizes that demand through [[Parallel transport]] of beliefs with the sandwich-product covariance transport and a connection generating [[Holonomy]] when frames disagree. The QRF transformation operator is the foundational-physics analogue of the project's inter-agent transport map: each agent in [[Multi-agent variational free energy]] carries a local frame ([[Agents as fibre-bundle sections]]), and comparing perspectives requires an explicit, state-aware [[Gauge transformation]] rather than a trivial relabeling. The finding that entanglement is frame-relative parallels the project's stance that "objective" structure is not absolute but is what survives transport between perspectives — the participatory reading of [[wheeler-1990-it-from-bit]]. The paper thus supplies both terminology (covariance under quantum frame change) and a concrete operator template for the [[Quantum reference frames]] strand of the participatory cluster.

## Cross-links

- Concepts: [[Quantum reference frames]], [[Gauge transformation]], [[Participatory realism (it from bit)]]
- Related sources: [[bartlett-rudolph-spekkens-2007-reference-frames]], [[vanrietvelde-2020-change-of-perspective]], [[brukner-2018-no-go-observer-facts]], [[rovelli-1996-relational-qm]]
- Manuscript: [[participatory-it-from-bit]]

```bibtex
@article{giacomini2019qrf,
  author  = {Giacomini, Flaminia and Castro-Ruiz, Esteban and Brukner, {\v{C}}aslav},
  title   = {Quantum mechanics and the covariance of physical laws in quantum reference frames},
  journal = {Nature Communications},
  volume  = {10},
  pages   = {494},
  year    = {2019},
  doi     = {10.1038/s41467-018-08155-0},
  eprint  = {1712.07207},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph}
}
```
