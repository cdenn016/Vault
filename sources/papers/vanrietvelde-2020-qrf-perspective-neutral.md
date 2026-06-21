---
type: paper
title: "A change of perspective: switching quantum reference frames via a perspective-neutral framework"
aliases:
  - Vanrietvelde 2020
  - QRF perspective-neutral
  - vanrietvelde-2020-change-of-perspective
  - Vanrietvelde et al. 2020
  - Perspective-neutral framework
  - QRF switching
authors:
  - Vanrietvelde, Augustin
  - Höhn, Philipp A.
  - Giacomini, Flaminia
  - Castro-Ruiz, Esteban
year: 2020
arxiv: "1809.00556"
url: https://arxiv.org/abs/1809.00556
tags:
  - cluster/participatory/quantum-foundations
  - cluster/gauge-theory
  - project/multi-agent
  - field/physics
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A change of perspective: switching quantum reference frames via a perspective-neutral framework

> [!info] Citation
> Vanrietvelde, A., Höhn, P. A., Giacomini, F., & Castro-Ruiz, E. (2020). "A change of perspective: switching quantum reference frames via a perspective-neutral framework." *Quantum*, 4, 225. DOI: [10.22331/q-2020-01-27-225](https://doi.org/10.22331/q-2020-01-27-225). arXiv:1809.00556.

## TL;DR

This paper develops a unifying, perspective-neutral framework for transforming between quantum reference frames (QRFs), drawing on tools from constrained-systems theory (Dirac quantization) and the operational QRF approach of Giacomini et al. 2019. The central insight is that a perspective-neutral super-structure simultaneously encodes all frame perspectives, and adopting a specific frame's perspective corresponds to a gauge-fixing of the symmetry-related redundancies in that structure, while switching frames corresponds to a gauge transformation. The authors recover known QRF transformations within this framework and demonstrate that entanglement and classicality are frame-dependent, operationally testable quantities.

## Problem & setting

Classical reference frames are idealizations: treating them as truly fundamental requires acknowledging that they are physical systems subject to quantum mechanics. Once laboratories and reference bodies are themselves quantum, classical frame transformations are insufficient, especially in scenarios like Wigner's friend. The paper asks: what replaces classical frame transformations in a fully quantum and relational formulation of physics? This question is equally urgent in quantum gravity, where diffeomorphism symmetry (Mach's principle) already enforces spacetime relationalism and purely relational observables (gauge-invariant relational observables in the Dirac sense).

## Method

The authors exploit a gravity-inspired symmetry principle: physical observables must be relational, and the description carries an inherent gauge redundancy. They work with a constrained-systems language on a finite-dimensional phase space subject to a linear constraint (a toy model of three interacting harmonic oscillators). The key steps are:

1. **Perspective-neutral (Dirac) structure:** Dirac quantization of the constrained system produces a Hilbert space that encodes all frame perspectives simultaneously, without an immediate operational interpretation.
2. **Quantum symmetry reduction:** Choosing a quantum reference frame amounts to a gauge-fixing, and the quantum analog of phase-space reduction maps the Dirac theory to a reduced (perspectival) quantum theory — the physics as seen from that frame.
3. **Frame switching:** Changing from one frame's perspective to another corresponds to a gauge transformation in the perspective-neutral structure. The transformation linking Dirac to a reduced quantization is the quantum symmetry reduction procedure.

Within the model, all transformations are globally valid, avoiding Gribov-like obstructions that arise in more general systems.

## Key results

The main technical results are: (i) a precise identification of Dirac quantization with the perspective-neutral super-structure and reduced quantization with a perspectival quantum theory; (ii) recovery of the QRF transformations of Giacomini et al. 2019 embedded in the perspective-neutral framework; (iii) a demonstration that entanglement and classicality of a subsystem depend on the chosen quantum reference frame — a state appearing classical (coherent) from one frame's perspective may appear entangled from another's. The authors also clarify that global operational states do not exist in this framework; only states relative to a chosen frame admit an operational interpretation.

## Relevance to this research

This paper is directly relevant to the participatory-realism and quantum-foundations thread of the research program, as encoded in the PIFB manuscript. The core theme — that physical descriptions are irreducibly perspectival, that a perspective-neutral structure underlies all individual descriptions, and that switching perspectives is a gauge transformation — resonates with the participatory realism program's treatment of agents as co-constitutive reference frames rather than passive observers. Specifically:

- The claim that entanglement and classicality are observer-frame-dependent (not absolute) properties is a concrete formal realization of the participatory realist intuition that the observer's frame is part of the physical situation.
- The perspective-neutral/Dirac vs. perspectival/reduced duality is formally analogous to the distinction between gauge-invariant global descriptions and perspectival local (belief-relative) descriptions in the VFE framework, where each agent holds a gauge-fixed view while the full system is described gauge-invariantly.
- The QRF framework's relational observables and gauge-invariant quantities connect directly to the gauge-equivariant structure of GL(K) attention, where the attention weights and belief updates must be invariant under local gauge transformations (frame re-labelings by agents).
- This paper, together with [[giacomini-2019-qrf-covariance]], provides the quantum-gravitational and quantum-foundational underpinning for the perspectival ontology assumed in the PIFB manuscript.
- The two-step frame switch (reduce to the perspective-neutral structure, re-embed into a new frame) is structurally identical to the project's composition of transports $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$, which likewise factors a perspective change through a common reference; the obstruction to a single global gauge slice is the project's [[Holonomy]], legitimizing the reading of belief-coupling as living on a quotient/gauge-invariant space rather than on raw frame-dependent coordinates.

## Cross-links
- Concepts: [[Quantum Reference Frames]], [[Gauge Theory]], [[Relational Observables]], [[fuchs-2017-participatory-realism|Participatory Realism]], [[Dirac Quantization]], [[Agents as fibre-bundle sections]], [[Holonomy]], [[Gauge transformation]]
- Related sources: [[giacomini-2019-qrf-covariance]], [[fuchs-2017-participatory-realism]], [[bartlett-2007-reference-frames|bartlett-rudolph-spekkens-2007-reference-frames]]
- Manuscript/Project: [[participatory-it-from-bit]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{Vanrietvelde2020,
  author  = {Vanrietvelde, Augustin and H{\"o}hn, Philipp A. and Giacomini, Flaminia and Castro-Ruiz, Esteban},
  title   = {A change of perspective: switching quantum reference frames via a perspective-neutral framework},
  journal = {Quantum},
  year    = {2020},
  volume  = {4},
  pages   = {225},
  doi     = {10.22331/q-2020-01-27-225},
  eprint  = {1809.00556},
  archivePrefix = {arXiv},
}
```
