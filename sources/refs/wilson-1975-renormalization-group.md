---
type: reference
title: "The Renormalization Group: Critical Phenomena and the Kondo Problem"
aliases:
  - "Wilson 1975"
authors:
  - Kenneth G. Wilson
year: 1975
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/physics
created: 2026-06-18
updated: 2026-06-18
---

# The Renormalization Group: Critical Phenomena and the Kondo Problem

> [!info] Citation
> Kenneth G. Wilson (1975). "The Renormalization Group: Critical Phenomena and the Kondo Problem." *Reviews of Modern Physics* **47**(4), 773–840. DOI: [10.1103/RevModPhys.47.773](https://doi.org/10.1103/RevModPhys.47.773).

## TL;DR

Wilson's review develops the renormalization group (RG) as a systematic framework for coarse-graining a physical system across scales, integrating out short-distance degrees of freedom to obtain effective descriptions whose couplings *flow* under successive transformations. It establishes the picture of fixed points, relevant and irrelevant operators, and universality through "block spin" methods on the Ising model, and applies the same machinery to numerically solve the Kondo problem of a magnetic impurity in a metal.

## What it establishes

- **Coarse-graining as a transformation on theories.** The central idea is a map that eliminates fine-scale fluctuations and re-expresses the system in terms of fewer, coarser variables (the "block spin" construction for the two-dimensional Ising model). Iterating this map generates a trajectory in the space of effective couplings — the RG flow.
- **Fixed points and universality.** Attractive fixed points of the flow govern macroscopic behavior; critical exponents are determined by the linearization of the flow about a fixed point. Microscopically distinct systems sharing the same fixed point exhibit identical large-scale behavior, explaining universality.
- **Relevant vs. irrelevant directions.** Eigenperturbations of the linearized flow are classified by whether they grow or decay under coarse-graining, separating the few parameters that control macroscopic physics from the many that wash out.
- **A nonperturbative, numerical solution of the Kondo problem.** The bulk of the paper applies a discretized RG (iterative diagonalization across logarithmically spaced energy shells) to the s-wave Kondo Hamiltonian, resolving the crossover from weak to strong impurity coupling — a problem inaccessible to ordinary perturbation theory.

## Why the project cites it

The project's [[Renormalization-group flow of beliefs]] construction is the direct conceptual descendant of this work: beliefs and their precisions are treated as scale-dependent couplings, and coarse-graining over a population of agents induces a flow on the effective belief parameters, exactly as Wilson's block-spin map induces a flow on Ising couplings. The fixed-point / relevant-direction taxonomy supplies the language for which belief structures survive aggregation and which are integrated out.

This scale-bridging is what underwrites [[Meta-agents and hierarchical emergence]] and the [[Ouroboros multi-scale dynamics]] picture in the [[Multi-agent variational free energy]] model. Coarse-graining many micro-agents into an effective [[Meta-agents and hierarchical emergence|meta-agent]] is an RG step in the space of [[Variational free energy]] functionals; universality is the claim that the emergent macro-dynamics depend only on a few relevant features of the underlying agent ensemble — the social-physics aggregation of microscopic interaction rules into collective laws, for which Wilson's RG is the canonical tool.

The information-geometric side of the project sharpens the analogy: because [[Mass as Fisher information|mass is identified with Fisher information]] and the [[Fisher information metric]] governs distinguishability of beliefs, RG coarse-graining acts on the same geometric data that the [[Natural gradient]] uses, and the flow can be read as a trajectory on the statistical manifold. The notions of [[Belief inertia]] and [[Hamiltonian belief dynamics]] inherit scale dependence through this lens.

> [!note] Editorial: The specific belief-RG flow equations, the choice of coarse-graining map over agents, and any claimed fixed points are contributions of the project manuscripts (see [[meta-entropy-manuscript]]); Wilson (1975) supplies the underlying physics methodology, not these particular results.

## BibTeX

```bibtex
@article{wilson1975renormalization,
  author  = {Wilson, Kenneth G.},
  title   = {The Renormalization Group: Critical Phenomena and the Kondo Problem},
  journal = {Reviews of Modern Physics},
  volume  = {47},
  number  = {4},
  pages   = {773--840},
  year    = {1975},
  month   = {oct},
  doi     = {10.1103/RevModPhys.47.773},
  publisher = {American Physical Society}
}
```
