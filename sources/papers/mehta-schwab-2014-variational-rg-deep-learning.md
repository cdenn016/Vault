---
type: paper
title: "An Exact Mapping Between the Variational Renormalization Group and Deep Learning"
aliases:
  - "Mehta & Schwab 2014"
  - "Variational RG = Deep Learning (Mehta-Schwab 2014)"
authors:
  - Pankaj Mehta
  - David J. Schwab
year: 2014
arxiv: 1410.3831
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# An Exact Mapping Between the Variational Renormalization Group and Deep Learning

> [!info] Citation
> Pankaj Mehta and David J. Schwab (2014). "An exact mapping between the Variational Renormalization Group and Deep Learning." Preprint: [arXiv:1410.3831](https://arxiv.org/abs/1410.3831).

## TL;DR

Mehta and Schwab construct an *exact* correspondence between Kadanoff's variational renormalization group (RG) and stacked Restricted Boltzmann Machines (RBMs): the variational coarse-graining transformation that integrates out fine-scale spins is, term for term, the same operation an RBM layer performs when it maps visible units to hidden units. Stacking RBMs into a deep network is therefore literally iterating an RG step, so a trained deep architecture can be read as an RG flow that extracts the relevant features at successive scales. The paper is the canonical precedent for the claim that a learning architecture *is* an RG flow, not merely analogous to one. It links directly to the project's [[Renormalization-group flow of beliefs]].

## Problem & setting

The RG and deep learning both compress data by discarding fine-scale, irrelevant information and retaining coarse-scale, relevant structure, but the connection had been heuristic. The authors ask whether the link is exact for a concrete, tractable pair: Kadanoff's *variational* RG (which introduces auxiliary coarse variables coupled to the microscopic spins and optimizes the coupling so the coarse free energy matches the fine one) and the RBM (a two-layer energy-based model with visible and hidden binary units).

## Method

They write the Kadanoff variational RG as the introduction of a coupling function $T(\{v_i\}, \{h_j\})$ between fine spins $v$ and coarse spins $h$, with the variational condition that the coarse Hamiltonian reproduce the exact free energy. They then show this is identical to the joint Boltzmann distribution defined by an RBM energy $E(v,h)$, with the variational matching condition corresponding to the RBM's exact-reconstruction (zero KL) limit. Each RG decimation step maps to one RBM layer; the deep stack is the iterated flow.

## Key results

The mapping is exact at the level of the partition functions and the variational free energy. Trained on the 2D Ising model, a stacked RBM recovers block-spin-like coarse variables that resemble Kadanoff blocks, demonstrating the architecture spontaneously implementing an RG-style coarse-graining. The relevant operators of the RG correspond to the features the deep network preferentially retains.

## Relevance to this research

This is the precedent that legitimizes reading the project's hierarchical machinery as a genuine RG flow rather than a metaphor. In the PIFB construction, the across-scale coarse-graining map $R_s$ of the Ouroboros tower (the meta-agent formation step) plays exactly the role of the Kadanoff/RBM decimation here: clusters of scale-$s$ agents are integrated into scale-$s{+}1$ meta-agents, inducing a flow on the effective belief couplings ([[Renormalization-group flow of beliefs]], [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]]). Mehta and Schwab supply the proof-of-concept that such a layered coarse-graining can be made *exact* in a tractable model, which is the standard PIFB aspires to when it claims its coarse-graining is the RG step on [[Variational free energy]] functionals rather than an ad hoc pooling.

The information-geometric framing is the natural sharpening: where Mehta-Schwab match free energies, the project measures the information lost across a coarse-graining step with the [[Fisher information metric]], aligning with the metric formulation of RG in [[beny-osborne-2015-info-geometric-rg]]. Read together, the two papers position the project's architecture-as-RG-flow claim between an exact discrete-model construction (Mehta-Schwab) and a continuous information-geometric one (Bény-Osborne). See [[wilson-1975-renormalization-group]] for the physics methodology and [[participatory-it-from-bit]] for the manuscript thread.

## Cross-links

- Concept: [[Renormalization-group flow of beliefs]], [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]].
- Concept: [[Fisher information metric]] (the information-loss measure across a coarse-graining step).
- Sources: [[beny-osborne-2015-info-geometric-rg]], [[wilson-1975-renormalization-group]], [[cardy-1996-scaling-renormalization]].
- Manuscript: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@article{mehta2014exact,
  author  = {Mehta, Pankaj and Schwab, David J.},
  title   = {An exact mapping between the Variational Renormalization Group and Deep Learning},
  journal = {arXiv preprint},
  volume  = {arXiv:1410.3831},
  year    = {2014},
  eprint  = {1410.3831},
  archivePrefix = {arXiv},
  primaryClass  = {stat.ML}
}
```
