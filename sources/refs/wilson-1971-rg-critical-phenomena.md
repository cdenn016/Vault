---
type: reference
title: "Renormalization Group and Critical Phenomena. I. Renormalization Group and the Kadanoff Scaling Picture"
aliases:
  - "Wilson 1971"
  - "Wilson (1971) RG and Kadanoff Scaling"
authors:
  - Kenneth G. Wilson
year: 1971
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/physics
created: 2026-06-19
updated: 2026-06-19
---

# Renormalization Group and Critical Phenomena. I. Renormalization Group and the Kadanoff Scaling Picture

> [!info] Citation
> Kenneth G. Wilson (1971). "Renormalization Group and Critical Phenomena. I. Renormalization Group and the Kadanoff Scaling Picture." *Physical Review B* **4**(9), 3174–3183. DOI: [10.1103/PhysRevB.4.3174](https://doi.org/10.1103/PhysRevB.4.3174).

> [!note] Distinct from [[wilson-1975-renormalization-group]] (the 1975 Reviews of Modern Physics Kondo review). This is the earlier 1971 PRB paper that founds the relevant/irrelevant operator taxonomy.

## TL;DR

The first of Wilson's two 1971 PRB papers turns Kadanoff's heuristic block-spin scaling picture into a concrete renormalization-group transformation: a map on the space of couplings that integrates out short-distance degrees of freedom. Linearizing this map about a fixed point classifies perturbations into *relevant* directions (which grow under coarse-graining and control macroscopic physics) and *irrelevant* directions (which decay and wash out). This relevant/irrelevant retention taxonomy is the conceptual tool the project borrows to say which belief structures survive aggregation.

## What it establishes

Wilson gives an explicit RG transformation realizing the Kadanoff intuition that a system near criticality looks self-similar under rescaling. Fixed points of the transformation correspond to scale-invariant theories; the eigenvalues of the linearized transformation about a fixed point determine critical exponents and sort the eigen-perturbations into relevant (eigenvalue > 1), marginal (= 1), and irrelevant (< 1). Universality follows: microscopically different systems flowing to the same fixed point share the same macroscopic critical behavior because they differ only in irrelevant directions. This 1971 paper predates and underlies the more expository 1975 Kondo review.

## Why the project cites it

The project's [[Renormalization-group flow of beliefs]] needs a principled answer to *which* features of a micro-agent ensemble persist when many agents are coarse-grained into a [[Meta-agents and hierarchical emergence|meta-agent]]. Wilson (1971) supplies exactly the relevant/irrelevant operator classification that answers it: the few belief couplings that grow under coarse-graining are the ones determining the emergent macro-dynamics, while the many that decay are integrated out. This is the source of the retention taxonomy the PIFB manuscript uses to argue that the [[Ouroboros multi-scale dynamics|Ouroboros]] coarse-graining is a genuine RG step with universal large-scale content rather than an arbitrary pooling. Manuscript thread: [[participatory-it-from-bit]]; related methods in [[cardy-1996-scaling-renormalization]] and [[wilson-kogut-1974-epsilon-expansion]].

## BibTeX

```bibtex
@article{wilson1971rg1,
  author  = {Wilson, Kenneth G.},
  title   = {Renormalization Group and Critical Phenomena. I. Renormalization Group and the Kadanoff Scaling Picture},
  journal = {Physical Review B},
  volume  = {4},
  number  = {9},
  pages   = {3174--3183},
  year    = {1971},
  doi     = {10.1103/PhysRevB.4.3174},
  publisher = {American Physical Society}
}
```
