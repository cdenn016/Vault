---
type: paper
title: "Information-Geometric Approach to the Renormalization Group"
aliases:
  - "Beny & Osborne 2015"
  - "Bény-Osborne (2015) Information-Geometric RG"
authors:
  - Cédric Bény
  - Tobias J. Osborne
year: 2015
arxiv: 1206.7004
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/statistics
  - field/mathematics
created: 2026-06-19
updated: 2026-06-19
---

# Information-Geometric Approach to the Renormalization Group

> [!info] Citation
> Cédric Bény and Tobias J. Osborne (2015). "Information-geometric approach to the renormalization group." *Physical Review A* **92**(2), 022330. DOI: [10.1103/PhysRevA.92.022330](https://doi.org/10.1103/PhysRevA.92.022330). Preprint: [arXiv:1206.7004](https://arxiv.org/abs/1206.7004).

## TL;DR

Bény and Osborne recast the renormalization group (RG) as a flow on a *statistical manifold* equipped with an operationally motivated information geometry. A coarse-graining is a quantum channel mapping microscopic states to observable-scale states; pulling the channel back onto the space of Hamiltonians induces a metric in which RG flow becomes a trajectory whose geometry quantifies how much physical distinguishability is lost at each scale. The construction supplies monotone (non-increasing) functions along the flow expressible through two-point correlations, giving a clean information-theoretic reading of irreversibility in coarse-graining. It is the continuous, metric-level counterpart to the project's [[Renormalization-group flow of beliefs]], grounded in the [[Fisher information metric]].

## Problem & setting

Wilsonian RG is usually phrased as a flow of couplings, but *which* couplings matter (relevant vs. irrelevant) and how much information a coarse-graining destroys are geometric facts about the space of states. The authors want a coordinate-free formulation: treat RG as a family of maps between physical theories and measure flow by the operational distinguishability of the states each theory predicts.

## Method

The set of (thermal) states is endowed with an information metric of Fisher–Bures type, defined operationally by how well nearby states can be told apart by measurements. A coarse-graining is a CPTP (quantum-channel) map; its action on states is monotone under the metric (data-processing inequality), and its pullback equips the space of Hamiltonians / couplings with the corresponding metric geometry. Relevant and irrelevant directions become large- vs. small-norm tangent vectors in this metric, and information loss along the flow is the contraction of the metric.

## Key results

RG flow is monotone in the information metric: coarse-graining can only reduce distinguishability, formalizing the loss of microscopic detail. The authors construct a family of functions, computable from two-point correlation functions, that are non-increasing along the flow — candidate monotones playing a role analogous to a c-function. The relevant/irrelevant taxonomy is recovered as the metric magnitude of perturbations rather than as a scaling-dimension bookkeeping device.

## Relevance to this research

This paper is the information-geometric backbone for the project's claim that coarse-graining a population of beliefs is an RG step *on a statistical manifold*. In the PIFB tower, each meta-agent-formation map carries microscopic beliefs into coarse beliefs; the natural way to measure what survives and what is integrated out is the [[Fisher information metric]] on the belief manifold, exactly the Fisher–Bures distinguishability metric Bény and Osborne use. Their monotonicity-under-coarse-graining result is the rigorous version of the project's intuition that relevant belief structure is what remains distinguishable after pooling, while irrelevant fluctuation is washed out ([[Renormalization-group flow of beliefs]], [[Meta-agents and hierarchical emergence]]).

It complements [[mehta-schwab-2014-variational-rg-deep-learning]]: where Mehta-Schwab give an *exact discrete* architecture-as-RG mapping, Bény-Osborne give the *continuous metric* picture, with information loss as metric contraction. Together they bracket the PIFB effective-action / continuum-limit program. The same Fisher metric grounds the [[Natural gradient]] used in the model's optimization, so RG coarse-graining and natural-gradient learning act on one shared geometry. See [[wilson-1975-renormalization-group]] and [[cardy-1996-scaling-renormalization]] for the physics, and [[participatory-it-from-bit]] for the manuscript thread.

## Cross-links

- Concept: [[Renormalization-group flow of beliefs]], [[Fisher information metric]], [[Meta-agents and hierarchical emergence]], [[Natural gradient]].
- Sources: [[mehta-schwab-2014-variational-rg-deep-learning]], [[wilson-1975-renormalization-group]], [[cardy-1996-scaling-renormalization]], [[berges-tetradis-wetterich-2002-nonperturbative-rg]].
- Manuscript: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@article{beny2015information,
  author  = {B\'eny, C\'edric and Osborne, Tobias J.},
  title   = {Information-geometric approach to the renormalization group},
  journal = {Physical Review A},
  volume  = {92},
  number  = {2},
  pages   = {022330},
  year    = {2015},
  doi     = {10.1103/PhysRevA.92.022330},
  eprint  = {1206.7004},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph},
  publisher = {American Physical Society}
}
```
