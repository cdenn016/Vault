---
type: paper
title: "Convexity Arguments for Efficient Minimization of the Bethe and Kikuchi Free Energies"
aliases:
  - "Heskes 2006 Bethe Kikuchi convexity"
authors:
  - Tom Heskes
year: 2006
arxiv: null
url: https://doi.org/10.1613/jair.1933
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-08-10
---

# Convexity Arguments for Efficient Minimization of the Bethe and Kikuchi Free Energies

> [!info] Citation
> Heskes, T. (2006). Convexity Arguments for Efficient Minimization of the Bethe and Kikuchi Free Energies. *Journal of Artificial Intelligence Research*, 26, 153-190. https://doi.org/10.1613/jair.1933

## TL;DR

Heskes addresses nonconvergence of loopy and generalized belief propagation by minimizing nonconvex Bethe/Kikuchi free energies through a sequence of convex constrained upper-bound problems. Tighter convex bounds substantially reduce the cost of this double-loop strategy in the paper's simulations.

## Problem & setting

Belief-propagation fixed points correspond to stationary points of approximate Bethe or Kikuchi free energies, but ordinary message iterations need not converge. Direct minimization is also difficult because the region free energy is generally nonconvex under local-consistency constraints.

## Method

The paper constructs convex upper bounds on the concave entropy contributions and solves a nested sequence of constrained convex problems. The outer loop updates the bound; the inner loop minimizes it. Different allocations of entropy terms produce bounds with different tightness and computational cost.

## Key results

The resulting class includes and improves on earlier double-loop procedures such as CCCP in the tested models. The algorithm supplies a descent-oriented route to a local solution of the approximate free-energy problem; it does not make Bethe/Kikuchi free energy exact on loopy graphs and does not guarantee the global optimum of the original nonconvex objective.

## Relevance to this research

If MultiAgentELBO adds loopy region-graph inference, Heskes motivates monotone surrogate checks, inner-solve residuals, and explicit failure cases. The exact finite joint-law oracle should remain the comparator. Tree exactness belongs to ordinary unconstrained sum-product BP; constrained VMP, EP, and Kikuchi approximations require their own error and convergence diagnostics.

## Cross-links

- Concepts: [[Belief Propagation]], [[Variational free energy]], [[Multi-agent variational free energy]]
- Related sources: [[yedidia-freeman-weiss-2005-region-free-energy]], [[senoz-2021-local-constraint-vmp]], [[bagaev-2023-reactive-message-passing]]

## BibTeX

```bibtex
@article{heskes2006convexity,
  author  = {Heskes, Tom},
  title   = {Convexity Arguments for Efficient Minimization of the Bethe and Kikuchi Free Energies},
  journal = {Journal of Artificial Intelligence Research},
  volume  = {26},
  pages   = {153--190},
  year    = {2006},
  doi     = {10.1613/jair.1933}
}
```
