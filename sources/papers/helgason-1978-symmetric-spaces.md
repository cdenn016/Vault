---
type: paper
title: "Differential Geometry, Lie Groups, and Symmetric Spaces"
aliases:
  - "Helgason 1978"
  - "Helgason (1978) Symmetric Spaces"
authors:
  - Sigurdur Helgason
year: 1978
arxiv: null
url: https://bookstore.ams.org/gsm-34
tags:
  - cluster/spd-geometry
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
  - field/mathematics
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Differential Geometry, Lie Groups, and Symmetric Spaces

> [!info] Citation
> Sigurdur Helgason (1978). *Differential Geometry, Lie Groups, and Symmetric Spaces*. Pure and Applied Mathematics, Vol. 80. Academic Press, New York. (Reprinted as Graduate Studies in Mathematics Vol. 34, American Mathematical Society, 2001; ISBN 978-0-8218-2848-9.) URL: https://bookstore.ams.org/gsm-34

## TL;DR

The standard graduate reference for the theory of symmetric spaces and their construction as homogeneous quotients $G/K$ of a Lie group by a closed subgroup. It develops affine connections, geodesics, curvature, the exp/log correspondence, and the classification of symmetric spaces via the Cartan decomposition. For this project it is the canonical home for the statement that the SPD cone is the symmetric space $GL(K)/O(K)$, which is what makes the affine-invariant covariance geometry "fall out" of group structure rather than being imposed by hand.

## Problem & setting

A Riemannian symmetric space is a manifold whose geodesic symmetry at every point is an isometry; equivalently it is a quotient $G/K$ with a Cartan involution. Helgason builds this machinery from the ground up — Lie groups and algebras, invariant affine connections, the curvature of invariant metrics, totally geodesic submanifolds — and classifies the symmetric spaces of compact and noncompact type. The book is the bridge between abstract Lie theory and concrete differential geometry of homogeneous spaces.

## Method

Starting from a Lie group $G$ with an involutive automorphism whose fixed-point set is $K$, the tangent space at the base coset splits via the $\pm 1$ eigenspaces of the involution (the Cartan decomposition $\mathfrak g = \mathfrak k \oplus \mathfrak p$). The $\mathfrak p$ part carries the invariant metric and the geodesics are one-parameter subgroups exponentiated through $\mathfrak p$; curvature is computed from the Lie bracket. The SPD cone arises as $GL(K,\mathbb R)/O(K)$ (equivalently $GL^+(K)/SO(K)$), a noncompact symmetric space of nonpositive curvature, with the affine-invariant metric as its invariant Riemannian structure and matrix exp/log as the symmetric-space exp/log.

## Key results

- The general theory of Riemannian symmetric spaces $G/K$, their geodesics, curvature, and the Cartan classification.
- The identification of the SPD cone with the noncompact symmetric space $GL(K)/O(K)$, explaining its nonpositive curvature and affine-invariant geometry from first principles.
- The exp/log correspondence and totally-geodesic structure used to do exact computation on such spaces.

## Relevance to this research

The program's covariance fiber $\Sigma$ lives on the SPD cone and its frame fiber $\phi$ lives in the Lie algebra of $GL^+(K)$; the affine-invariant metric and the $\Sigma^{1/2}$-sandwich exp/log used in the `spd_affine` retraction are precisely the symmetric-space structure of $GL(K)/O(K)$ that Helgason formalizes. This reference explains *why* congruence invariance $\Sigma\mapsto G\Sigma G^\top$ and nonpositive curvature are not accidents but consequences of the quotient structure — the same group $GL^+(K)$ whose left action gives the [[Gauge transformation]] of frames acts on covariances by congruence with the symmetric space as orbit. It is also the natural home for the SO(1,1) / split-signature example PIFB uses to illustrate non-Riemannian (indefinite) frame geometry. Supports [[SPD-manifold geometry and Riemannian optimization]] and the NEW page [[Symmetric spaces and the SPD cone]].

## Cross-links

- Symmetric-space structure of the cone: [[Symmetric spaces and the SPD cone]] · [[SPD-manifold geometry and Riemannian optimization]]
- SPD metric and geometric mean: [[bhatia-2007-positive-definite-matrices]], [[pennec-2006-affine-invariant-tensor]], [[moakher-2005-geometric-mean]]
- Lie-group / curvature foundations: [[hall-2015-lie-groups]], [[milnor-1976-left-invariant-metrics]], [[Killing form]]
- Gauge action on covariance: [[Gauge transformation]] · [[Parallel transport]] · [[Holonomy]]
- Manuscript: [[participatory-it-from-bit]]

```bibtex
@book{helgason1978differential,
  title     = {Differential Geometry, Lie Groups, and Symmetric Spaces},
  author    = {Helgason, Sigurdur},
  series    = {Pure and Applied Mathematics},
  volume    = {80},
  publisher = {Academic Press},
  address   = {New York},
  year      = {1978},
  note      = {Reprinted as Graduate Studies in Mathematics Vol. 34, AMS, 2001, ISBN 978-0-8218-2848-9}
}
```
