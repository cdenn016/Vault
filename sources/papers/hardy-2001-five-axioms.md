---
type: paper
title: "Quantum Theory From Five Reasonable Axioms"
aliases: ["Hardy 2001", "Five reasonable axioms", "Hardy reconstruction"]
authors: ["Lucien Hardy"]
year: 2001
arxiv: "quant-ph/0101012"
url: https://arxiv.org/abs/quant-ph/0101012
tags: [cluster/participatory, project/multi-agent, project/transformer, field/physics, field/philosophy, cluster/participatory/quantum-foundations]
created: 2026-06-19
updated: 2026-06-19
---

# Quantum Theory From Five Reasonable Axioms

> [!info] Citation
> Hardy, L. (2001). "Quantum Theory From Five Reasonable Axioms." Preprint: arXiv:quant-ph/0101012.

## TL;DR

Hardy derives the full apparatus of finite-dimensional quantum theory — complex Hilbert spaces, Hermitian operators, the trace rule for probabilities — from five simple, operationally stated axioms about probabilities, states, and measurements. Four of the axioms are shared by classical probability theory and quantum theory; only the fifth, demanding the existence of *continuous* reversible transformations between pure states, singles out quantum theory and rules classical probability out. The work is a founding example of the *informational reconstruction* program: rather than postulating the strange Hilbert-space formalism, one obtains it as the unique theory satisfying reasonable requirements on how information is gathered and updated.

## Problem & setting

Quantum theory is normally presented through opaque mathematical postulates with no evident physical motivation. Hardy asks whether the formalism can be *derived* from transparent operational principles framed entirely in terms of preparations, measurements, and the probabilities connecting them. The setting is a generalized probabilistic framework in which a state is the list of probabilities for a fiducial set of measurements, and a theory is fixed by how many such numbers (the dimension $K$) are needed and how they relate to the number of distinguishable states $N$.

## Method

Hardy introduces two integers — $K$, the number of degrees of freedom (fiducial probabilities) fixing a state, and $N$, the maximum number of perfectly distinguishable states — and posits a simplicity relation $K = N^r$. The five axioms (probabilities, simplicity, subspaces, composite systems, and continuity of reversible transformations) then force $r = 2$, i.e. $K = N^2$, which is precisely the dimension count of quantum density matrices, and reconstruct the Hilbert-space formalism. Dropping the continuity axiom collapses the theory to classical probability ($K = N$).

## Key results

Quantum theory emerges as the unique generalized probabilistic theory satisfying five reasonable axioms, with the continuity-of-pure-state-transformations axiom as the lone "quantum" ingredient. The reconstruction explains *why* the formalism takes the shape it does — complex amplitudes, the trace rule, the $N^2$ parameter count — and positions quantum theory on a principled axis between classical probability and more exotic possibilities. It launched the device-independent / operational reconstruction literature that followed.

## Relevance to this research

Hardy's reconstruction is the template for the "it from bit, then emergent structure" arc that [[participatory-it-from-bit]] pursues: begin with bare informational/probabilistic primitives and *derive* the rich geometric structure rather than postulating it. The project's ambition is analogous — beliefs are probability assignments (variational posteriors), and the gauge-theoretic, information-geometric structure ([[Fisher information metric]], [[Quantum information geometry]], [[Gauge transformation]]) is meant to *emerge* from requirements on how agents represent, update, and share information, not to be imposed by fiat. The $K$/$N$ counting and the fiducial-probability picture also connect to the project's representational dimension $K$ and to the broader [[VFE Transformer Program]], where the dimensionality of belief space is a design variable. Hardy supplies the methodological precedent (and a measure of intellectual discipline): if the project claims its geometry is the *natural* one, the standard set by reconstruction theorems is to show it follows from reasonable axioms about agent inference, not merely that it is convenient.

## Cross-links

- Concepts: [[Participatory realism (it from bit)]], [[Quantum information geometry]], [[Fisher information metric]]
- Related sources: [[fuchs-schack-2013-bayesian-coherence]], [[caticha-2019-entropic-dynamics]], [[spekkens-2007-toy-theory]], [[wheeler-1990-it-from-bit]]
- Manuscript: [[participatory-it-from-bit]]
- Project: [[VFE Transformer Program]]

```bibtex
@article{hardy2001five,
  author  = {Hardy, Lucien},
  title   = {Quantum Theory From Five Reasonable Axioms},
  year    = {2001},
  eprint  = {quant-ph/0101012},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph},
  note    = {Preprint; no journal DOI}
}
```
