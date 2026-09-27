---
type: concept
title: "Riemannian Quotient Manifold"
aliases:
  - "Quotient Manifold"
tags:
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-09-27
---

# Riemannian Quotient Manifold

A Riemannian quotient manifold is the smooth manifold M/~ obtained by quotienting a Riemannian manifold M by a group action (the equivalence classes being orbits), equipped with the metric inherited by declaring the projection a Riemannian submersion: the quotient metric measures only the horizontal (orbit-transverse) component of tangent vectors. This is the standard device for optimizing over geometric objects defined up to a symmetry — e.g. subspaces ([[Grassmann Manifold]] = Stiefel / O(k)) and fixed-rank SPD matrices, where the gauge/representation redundancy is quotiented away so that gradients live on the true geometric object. Used in [[bonnabel-2009-spd-fixed-rank]] for fixed-rank SPD optimization.

## Proper Banach and Hilbert actions

[[jotz-2008-closedness-of-the-tangent-spaces-to-the-orbits-of-proper-actions]] proves closed ranges of infinitesimal orbit maps for smooth proper Banach–Lie actions (Theorem 2.1, journal p. 518). Its quotient-manifold conclusion adds freeness and a Hilbert manifold (Corollary 2.5, p. 520). Closed range alone does not provide a complemented subspace in an arbitrary Banach space, and the source does not turn a weak or degenerate Fisher form into a strong quotient metric. The journal PDF and exact locators were checked in [[multiagentelbo-2026-09-26-selection-and-reference-review]].

## Related
[[Grassmann Manifold]], [[Symmetric spaces and the SPD cone]], [[SPD-manifold geometry and Riemannian optimization|Riemannian optimization]]

## Sources
[[bonnabel-2009-spd-fixed-rank]], [[pennec-2009-riemannian-computing]]
