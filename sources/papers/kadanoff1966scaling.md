---
type: paper
title: "Scaling Laws for Ising Models Near Tc"
aliases:
  - "Kadanoff 1966"
  - "Kadanoff block spin"
  - "Kadanoff scaling"
authors:
  - Kadanoff, Leo P.
year: 1966
arxiv: null
url: https://doi.org/10.1103/PhysicsPhysiqueFizika.2.263
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/physics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Scaling Laws for Ising Models Near Tc

> [!info] Citation
> Kadanoff, Leo P. (1966). "Scaling Laws for Ising Models Near Tc." *Physics Physique Fizika* **2**(6), 263–272. DOI: [10.1103/PhysicsPhysiqueFizika.2.263](https://doi.org/10.1103/PhysicsPhysiqueFizika.2.263).

## TL;DR

Kadanoff introduces the block-spin construction: replace an $L\times L$ block of Ising spins with a single effective spin, argue that near the critical point the new system is statistically identical to the old one at a rescaled temperature and field, and thereby derive scaling laws relating the critical exponents. This heuristic picture is the conceptual seed from which the full Wilson renormalization group grew, and it supplies the language of coarse-graining, block variables, and self-similarity under rescaling that the project inherits for its belief-RG program.

## Problem & setting

Near the critical temperature $T_c$ of an Ising ferromagnet, correlation lengths diverge, thermodynamic quantities develop power-law singularities with critical exponents $\alpha, \beta, \gamma, \delta, \eta, \nu$, and it was not understood why these exponents obey exact relations. Prior to Kadanoff, each critical exponent was computed independently from ad hoc approximations, and the relations between them (Rushbrooke's inequality, Widom's homogeneity hypothesis) lacked a structural explanation.

## Method

Kadanoff's key move is the **block-spin construction**. Partition the $d$-dimensional lattice into hypercubic blocks of side $L$ (in lattice units). Within each block, define a collective block spin variable. The central hypothesis is that near $T_c$, where correlations extend over many lattice spacings, the block system is statistically self-similar to the original: it is again an Ising model, but with rescaled reduced temperature $t' = L^{y_t}\, t$ and rescaled magnetic field $h' = L^{y_h}\, h$, where $y_t$ and $y_h$ are two fundamental scaling exponents. Demanding that the free energy density transforms homogeneously under this rescaling,

$$
f(t, h) = L^{-d}\, f(L^{y_t} t,\, L^{y_h} h),
$$

immediately forces all critical exponents to be expressible in terms of just $y_t$, $y_h$, and $d$, yielding the scaling laws (Rushbrooke, Widom, Fisher relations) as identities rather than inequalities.

## Key results

The block-spin argument establishes:
- All six standard critical exponents $(\alpha, \beta, \gamma, \delta, \eta, \nu)$ are functions of only two independent exponents $y_t$ and $y_h$ (and dimension $d$), reducing the independent unknowns from six to two.
- The Rushbrooke scaling law $\alpha + 2\beta + \gamma = 2$, the Widom law $\gamma = \beta(\delta-1)$, and the Fisher law $\gamma = (2-\eta)\nu$ all follow from the homogeneity hypothesis.
- The free energy near $T_c$ is a generalized homogeneous function (GHF), which is the same statement as Widom's hypothesis but now derived from a physical picture rather than postulated.
- The correlation length diverges as $\xi \sim |t|^{-\nu}$ with $\nu = 1/y_t$, linking the spatial structure directly to the thermodynamic scaling.

## Relevance to this research

Kadanoff's block-spin picture is the direct conceptual ancestor of the renormalization-group machinery the project borrows for its belief-coarse-graining program. In the project's framework, a coherent cluster of micro-agents plays the role of the spin block; the pooled meta-belief is the block variable; and the rescaled couplings of the parent agent are the renormalized couplings. The demand that the emergent meta-agent's free energy be a generalized homogeneous function of the pooled belief parameters — the project's analog of Kadanoff's homogeneity hypothesis — is what would make the [[Ouroboros multi-scale dynamics|Ouroboros]] coarse-graining a genuine RG step rather than an arbitrary pooling.

Wilson (1971) ([[wilson-1971-rg-critical-phenomena]]) operationalized Kadanoff's heuristic into a precise map on coupling space and added the linearization that yields the relevant/irrelevant taxonomy. This paper is the heuristic seed; Wilson's is the rigorous realization. Both are needed to understand the project's claim that belief aggregation is an RG step: Kadanoff supplies the "what" (block variables, self-similarity, GHF), Wilson supplies the "how" (eigenvalue classification, universality). The PIFB manuscript ([[participatory-it-from-bit]]) and the [[Renormalization-group flow of beliefs]] concept page reference this Kadanoff block-spin language directly when arguing that the few belief couplings which grow under coarse-graining determine emergent macro-dynamics.

## Cross-links
- Concepts: [[Renormalization group flow]], [[Renormalization-group flow of beliefs]], [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]], [[Variational free energy]]
- Related sources: [[wilson-1971-rg-critical-phenomena]], [[wilson-kogut-1974-epsilon-expansion]], [[berges-tetradis-wetterich-2002-nonperturbative-rg]], [[cardy-1996-scaling-renormalization]], [[mehta-schwab-2014-variational-rg-deep-learning]]
- Manuscript/Project: [[participatory-it-from-bit]], [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX
```bibtex
@article{kadanoff1966scaling,
  author  = {Kadanoff, Leo P.},
  title   = {Scaling Laws for {Ising} Models Near {Tc}},
  journal = {Physics Physique Fizika},
  volume  = {2},
  number  = {6},
  pages   = {263--272},
  year    = {1966},
  doi     = {10.1103/PhysicsPhysiqueFizika.2.263},
  publisher = {American Physical Society},
}
```
