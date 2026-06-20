---
type: reference
title: "Scaling and Renormalization in Statistical Physics"
aliases:
  - "Cardy 1996"
  - "Cardy (1996) Scaling and Renormalization"
authors:
  - John L. Cardy
year: 1996
tags:
  - cluster/multi-agent
  - cluster/methodology
  - project/multi-agent
  - field/physics
created: 2026-06-19
updated: 2026-06-19
---

# Scaling and Renormalization in Statistical Physics

> [!info] Citation
> John L. Cardy (1996). *Scaling and Renormalization in Statistical Physics.* Cambridge Lecture Notes in Physics 5. Cambridge University Press. ISBN: 9780521499590.

## TL;DR

Cardy's graduate text is the standard pedagogical account of scaling, the renormalization group (RG), and critical phenomena in statistical physics. It develops the Wilsonian effective action by integrating out short-wavelength fluctuations, the scaling hypothesis and critical exponents, finite-size scaling, and the Gaussian/saddle-point (Laplace) treatment of the partition function around a mean-field configuration. It is the most-cited RG reference in the PIFB manuscript (nine occurrences), supplying the working machinery behind the project's belief-RG closure.

## What it establishes

The book sets out the Kadanoff block-spin picture and Wilson's momentum-shell RG as a flow on the space of couplings, with fixed points controlling universality and the relevant/irrelevant classification of perturbations. It treats the Wilsonian *effective action* obtained by integrating out fast modes, the Gaussian (saddle-point/Laplace) approximation to the functional integral that linearizes the theory about a saddle, and finite-size scaling — how critical quantities depend on system size near a fixed point, which is the natural tool for a finite population of agents. The presentation is operational and oriented toward computing exponents and scaling functions, making it a methods reference rather than a foundational paper.

## Why the project cites it

PIFB treats a population of variational beliefs as a statistical-mechanical system and coarse-grains it across the scales of the Ouroboros tower. Cardy supplies three pieces of that program directly. The **Laplace / saddle-point closure** of the belief partition function — expanding the free energy about its dominant configuration — is the Gaussian-approximation technique the book teaches, and it is how the project obtains a tractable effective free energy at each scale (see [[wong-2001-asymptotic-integrals]] and [[bender-orszag-1999-asymptotic-methods]] for the asymptotic-integral side). The **Wilsonian effective action** obtained by integrating out fine-scale agent fluctuations is the field-theoretic object underlying [[Renormalization-group flow of beliefs]], and the formation of [[Meta-agents and hierarchical emergence|meta-agents]] is a block-spin RG step in the space of [[Variational free energy]] functionals. **Finite-size scaling** is the relevant correction for a finite ensemble of agents, governing how emergent macro-quantities approach their thermodynamic-limit values. This last point connects to the meta-entropy thermodynamic-limit program ([[meta-entropy-manuscript]]) and the continuum-limit open problem flagged in [[berges-tetradis-wetterich-2002-nonperturbative-rg]]. Manuscript thread: [[participatory-it-from-bit]]; physics lineage: [[wilson-1975-renormalization-group]].

## BibTeX

```bibtex
@book{cardy1996scaling,
  author    = {Cardy, John L.},
  title     = {Scaling and Renormalization in Statistical Physics},
  series    = {Cambridge Lecture Notes in Physics},
  number    = {5},
  publisher = {Cambridge University Press},
  year      = {1996},
  isbn      = {9780521499590},
  doi       = {10.1017/CBO9781316036440}
}
```
