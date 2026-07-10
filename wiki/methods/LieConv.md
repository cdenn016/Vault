---
type: method
title: LieConv
aliases:
  - Lie Group Convolution
  - Lie-algebra convolution
  - Finzi LieConv
tags:
  - cluster/gauge-theory
  - project/transformer
status: stable
created: 2026-06-18
updated: 2026-07-10
---

# LieConv

## What it is

LieConv is a convolutional layer introduced by Finzi, Stanton, Izmailov, and
Wilson in [[finzi-2020-lieconv]]. It is equivariant to Lie-group actions under
the construction's stated exponential-map assumptions and operates on
continuous, irregularly sampled data. It evaluates kernels in Lie-algebra
coordinates and recovers group elements with the group exponential, which is a
matrix exponential only after choosing a matrix-group representation. The VFE
transformer's represented GL($k$) path uses that matrix-group special case.

## How it works

A standard convolution sums weighted neighbor contributions; a group convolution
generalizes this so the weight depends on a relative group element. LieConv
lifts data to a group or homogeneous space, evaluates a learned kernel in chosen
Lie-algebra coordinates of relative elements, and estimates the group integral
by Monte Carlo sampling over a local neighborhood. Surjectivity of the
exponential map ensures the required group elements have algebra preimages; it
does **not** make exp injective or establish a global exp/log bijection. Logarithm
branches and multiple preimages therefore remain part of the coordinate
construction in [[finzi-2020-lieconv]].

This construction sits alongside the discrete-group convolutions of [[cohen-2016-gcnn]] and the compact-group theory of [[kondor-2018-compact-group-conv]], extending equivariance from finite or compact symmetry groups to continuous Lie groups, and it is one of the concrete instances of the broader equivariance blueprint surveyed in [[bronstein-2021-geometric-deep-learning]].

## Strengths / limitations

The principal strength is generality: a single layer template covers a whole catalog of symmetry groups, chosen by supplying the group's exp/log maps, and it applies to genuinely irregular data where grid-based [[Group equivariant CNN (G-CNN)|G-CNNs]] do not. Working in algebra coordinates avoids hand-derived, group-specific kernel constraints such as those that [[weiler-2019-e2-steerable|steerable CNNs]] solve per-irrep, trading representation-theoretic bookkeeping for a learned MLP on the tangent space.

The limitations follow from the same assumptions. Non-surjective exponential
maps leave group elements without algebra preimages, while noninjectivity makes
log coordinates multivalued even when exp is surjective. The Monte Carlo
neighborhood integral introduces sampling variance, and lifting and pairwise
relative computation grow with neighborhood size. Unlike
[[thomas-2018-tensor-field-networks|tensor field networks]] or steerable
approaches, LieConv does not natively decompose features into
[[Irreducible representation|irreps]] coupled by
[[Clebsch-Gordan coefficients]].

## Relation to this work

The VFE transformer's gauge sector uses the same broad algebra-first pattern.
It stores a Lie-algebra coordinate `phi` and obtains group actions through the
matrix exponential. [[Baker-Campbell-Hausdorff formula|BCH]] has a different
type: it maps a pair of local algebra coordinates to another algebra coordinate
approximating the logarithm of a product. Exponentiation or a separately defined
group-valued retraction then maps that coordinate to the group.

> [!note] Editorial (2026-07-10): LieConv supplies a comparison for algebra-first
> coordinates, not the layer or its neural MLP kernel. The VFE transformer has no
> LieConv-style convolution, and LieConv's equivariance theorem does not establish
> the transformer's gauge, optimizer, or positional claims.
> [[gl-k-attention-2026-07-09-review-revision]]

The transformer's use of transported Gaussian beliefs and blockwise group actions
must be justified by its own construction. In realized Regime I,
$\Omega_{ij}=U_iU_j^{-1}$ is a flat pure-gauge transport, so citing LieConv does
not supply nontrivial holonomy. Joint Gaussian belief updates use Fisher
geometry, whose covariance block is one-half conventional AIRM, whereas the
audited frame table uses plain AdamW and leaves the configured heavy-ball/pullback path inactive. LieConv contributes only the
comparison that algebra coordinates can parameterize continuous group actions.

## Sources

- [[finzi-2020-lieconv]] — the LieConv paper: Lie-group-equivariant convolution on arbitrary continuous data via Lie-algebra coordinates and the exponential map.
- [[cohen-2016-gcnn]] — group-equivariant convolution for discrete groups, the precursor LieConv generalizes to continuous Lie groups.
- [[kondor-2018-compact-group-conv]] — necessity and sufficiency of group convolution for equivariance under compact groups.
- [[weiler-2019-e2-steerable]] — per-irrep steerable kernel constraints, the representation-theoretic alternative to LieConv's algebra-MLP kernel.
- [[thomas-2018-tensor-field-networks]] — irrep features with Clebsch-Gordan coupling, contrasted with LieConv's argument-based equivariance.
- [[cohen-2019-gauge-cnn]] — local gauge equivariance and parallel transport that the VFE transformer adds on top of the algebra-first parameterization.
- [[bronstein-2021-geometric-deep-learning]] — the equivariance blueprint situating LieConv among geometric deep-learning methods.

## See also

- [[Gauge equivariant CNN]]
- [[Group equivariant CNN (G-CNN)]]
- [[Steerable CNN]]
- [[Tensor Field Network]]
- [[Group equivariance]]
- [[Gauge transformation]]
- [[Parallel transport]]
- [[Irreducible representation]]
- [[Clebsch-Gordan coefficients]]
- [[Gauge equivariance and geometric deep learning]]
- [[VFE Transformer Program]]
