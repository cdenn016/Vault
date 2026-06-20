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
updated: 2026-06-19
---

# LieConv

## What it is

LieConv is a convolutional layer, introduced by Finzi, Stanton, Izmailov, and Wilson in [[finzi-2020-lieconv]], that is provably equivariant to the action of an arbitrary Lie group with a surjective exponential map and that operates on arbitrary continuous data (point clouds, sets, irregularly sampled signals) rather than on a regular grid. Its defining move is to express all geometry in *Lie-algebra (logarithmic) coordinates*: group elements are represented through their logarithms, the convolution kernel is a function on the algebra, and group elements are recovered when needed via the matrix exponential. This is the same algebra-first parameterization the VFE transformer adopts for its GL(k) gauge group.

## How it works

A standard convolution sums weighted neighbour contributions; a group convolution generalizes this so that the weight depends only on the *relative group element* between two points, which is what makes the output [[Group equivariance|group-equivariant]]. LieConv realizes this in three steps. First, each data point is lifted from the input space to (a coset of) the group, so that the relative transformation taking one point to another is a concrete group element. Second, rather than parameterize the kernel as a function of group elements directly — which is awkward for curved, high-dimensional groups — LieConv maps that relative element through the logarithm into the Lie algebra, a flat vector space, and evaluates a learned MLP kernel there. Third, the exponential map recovers group elements as required. Because the log/exp pair is a bijection wherever the exponential is surjective, the kernel is a well-defined function of the relative group element, and the resulting layer is equivariant by construction for any such Lie group — translations, rotations, scalings, the special Euclidean group, and so on — selected simply by swapping in the group's exp/log. A Monte Carlo estimate of the integral over neighbours, together with a local neighbourhood restriction, keeps the operation tractable on continuous, unstructured inputs.

This construction sits alongside the discrete-group convolutions of [[cohen-2016-gcnn]] and the compact-group theory of [[kondor-2018-compact-group-conv]], extending equivariance from finite or compact symmetry groups to continuous Lie groups, and it is one of the concrete instances of the broader equivariance blueprint surveyed in [[bronstein-2021-geometric-deep-learning]].

## Strengths / limitations

The principal strength is generality: a single layer template covers a whole catalogue of symmetry groups, chosen by supplying the group's exp/log maps, and it applies to genuinely irregular data where grid-based [[Group equivariant CNN (G-CNN)|G-CNNs]] do not. Working in algebra coordinates avoids hand-derived, group-specific kernel constraints such as those that [[weiler-2019-e2-steerable|steerable CNNs]] solve per-irrep, trading representation-theoretic bookkeeping for a learned MLP on the tangent space.

The limitations follow from the same assumptions. Equivariance is exact only when the exponential map is surjective; for groups where exp fails to cover the group (or is not injective on the relevant region) the log coordinates are ambiguous and the guarantee weakens. The Monte Carlo neighbourhood integral introduces sampling variance, and the lifting and pairwise-relative computation cost grows with neighbourhood size. Unlike [[thomas-2018-tensor-field-networks|tensor field networks]] or steerable approaches, LieConv does not natively decompose features into [[Irreducible representation|irreps]] coupled by [[Clebsch-Gordan coefficients]]; its equivariance is enforced through the kernel's argument rather than through the representation type of its features.

## Relation to this work

The VFE transformer's gauge sector is built on the same algebra-first idea that LieConv pioneered. Its declared gauge group is the block general-linear group GL(k); rather than parameterize gauge frames as group matrices, the architecture carries a Lie-algebra "phi" parameterization and reconstructs group elements through a retraction — a [[Baker-Campbell-Hausdorff formula|Baker-Campbell-Hausdorff]] (BCH) composition that plays the role LieConv's exponential plays, mapping algebra coordinates back to the group. In both cases the algebra is the flat space where parameters live and learning happens, and exp/BCH is the bridge to the curved group.

> [!note] Editorial: LieConv supplies the parameterization pattern (learn in the log, act through exp) rather than the layer itself. The VFE transformer does not perform a LieConv-style spatial convolution; it borrows the algebra-first treatment of a continuous group and applies it to gauge frames and to positional encodings, where a learned phi is composed via BCH before being combined with RoPE, ALiBi, and T5 relative-position priors.

Where LieConv stops at equivariance of a convolution, this work extends the geometric machinery in directions LieConv does not address: it transports per-token Gaussian beliefs across gauge frames via [[Parallel transport]] and [[Holonomy]] in the sense of [[cohen-2019-gauge-cnn]], couples block features through [[Clebsch-Gordan coefficients]] and [[Irreducible representation|irreps]] in the manner of [[thomas-2018-tensor-field-networks]], and ties the group-geometric updates to a [[Variational free energy]] objective with [[Natural gradient]] M-step updates. LieConv contributes the foundational discipline — do the geometry in log coordinates and recover the group by exponentiation — that makes the GL(k) gauge parameterization well-posed.

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
