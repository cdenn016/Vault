---
type: method
title: Gauge equivariant CNN
aliases:
  - Gauge CNN
  - Gauge-equivariant CNN
  - Gauge equivariant convolutional network
  - Icosahedral CNN
tags:
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Gauge equivariant CNN

## What it is

A gauge equivariant CNN is a convolutional network that operates on features
defined over a curved manifold and remains equivariant not only to global
symmetries but to *local* changes of reference frame — that is, to **gauge
transformations**. It was introduced by Cohen, Weiler, Kicanaoglu and Welling
in [[cohen-2019-gauge-cnn]], where the flagship instance is the Icosahedral CNN
for signals on the sphere. It generalizes the global-symmetry [[Group equivariant CNN (G-CNN)]]
of [[cohen-2016-gcnn]] from a single group acting everywhere to a structure
group acting independently in each tangent space, making it the most direct
geometric-deep-learning ancestor of the gauge ideas in the
[[VFE Transformer Program]].

## How it works

On a flat domain a convolution is equivariant to translations because there is a
single global coordinate frame. On a curved manifold there is no canonical way to
choose a frame in each tangent space, and any choice is a **gauge**. The central
demand of [[cohen-2019-gauge-cnn]] is that the network's output transform
consistently — covariantly — whenever this local frame is rotated, so that the
predictions do not depend on the arbitrary choice of coordinates. Features are
modeled as fields whose values live in a chosen group representation; under a
local gauge rotation by an element of the structure group, a feature vector is
acted on by that representation (an [[Irreducible representation]] or a sum of
irreps).

Two ingredients make this precise. First, a **kernel constraint**: the
convolution filter must satisfy a linear equivariance condition relating the
representations carried by its input and output fields. This is the same
representation-theoretic constraint later systematized per-irrep by the
[[Steerable CNN]] theory of [[weiler-2019-e2-steerable]] and, for compact groups
in general, proved necessary and sufficient for linear equivariance by
[[kondor-2018-compact-group-conv]]. Second, because features at neighboring
points live in different tangent spaces with different gauges, comparing or
aggregating them requires **[[Parallel transport]]** along the manifold: the
network transports a neighbor's feature into the local frame before applying the
kernel, using the connection of the manifold. Transporting a feature around a
closed loop generally returns it rotated — the network's **[[Holonomy]]** — which
is exactly the curvature signature that distinguishes the gauge-equivariant
setting from the flat one. The whole construction is one face of the broader
"5G" blueprint (grids, groups, graphs, geodesics, gauges) of
[[bronstein-2021-geometric-deep-learning]], which recasts CNNs, GNNs and
Transformers as instances of a single [[Group equivariance]] principle.

## Strengths / limitations

The principal strength is correctness by construction: a declared symmetry, made
local, is baked into the architecture rather than learned from data or augmentation,
yielding provable equivariance, better sample efficiency on symmetric domains, and
a principled basis (the constrained, irrep-indexed kernels) instead of an
unconstrained one. The gauge formulation is also intrinsic — it needs only a
manifold with a connection, not a globally consistent coordinate system — which is
what lets it run on spheres, meshes and other curved domains.

The limitations are equally concrete. The kernel constraint and the bookkeeping of
representations, parallel transport and (for nonlinear interactions) coupling rules
are intricate to implement and to reason about. The structure group in the original
work is compact (rotations of the tangent frame); non-compact groups such as the
general linear group sit outside the cleanest part of the theory. And, like other
equivariant designs, the inductive bias only pays off when the assumed symmetry
genuinely holds in the data — an over-strong constraint can cost expressivity.
A Lie-algebra-first alternative that sidesteps some kernel-constraint machinery is
[[LieConv]] ([[finzi-2020-lieconv]]), which builds convolutions for any Lie group
with a surjective exponential map by working in log coordinates.

## Relation to this work

The VFE transformer borrows the *gauge* stance of [[cohen-2019-gauge-cnn]] but
relocates it from image features on a manifold to the per-token latent geometry of
a sequence model. Its declared structure group is a block general-linear group,
GL(k) — a non-compact analogue of the tangent-frame rotations used here — and it
parameterizes gauge elements in the Lie algebra (the "phi" parameterization), in
the same algebra-first spirit as [[finzi-2020-lieconv]]. The two concepts this page
makes precise, [[Parallel transport]] and [[Holonomy]], reappear directly: the
transformer transports per-token Gaussian beliefs (mean and an SPD covariance)
between positions, and its cocycle-relaxation and holonomy terms measure the
frame mismatch accumulated around loops, exactly as transport-around-a-loop does
on a curved manifold. Nonlinear coupling of features carried by different
[[Irreducible representation]]s is handled, as in [[thomas-2018-tensor-field-networks]]
and the [[Steerable CNN]] line, via [[Clebsch-Gordan coefficients]].

It also differs in important ways. Where a gauge equivariant CNN enforces exact
equivariance through a hard kernel constraint, the VFE transformer treats
gauge-consistency as a *soft*, learned objective folded into a variational
[[Variational free energy]] loss — equivariance is relaxed (a cocycle penalty)
rather than imposed. The geometry the transformer transports is not a generic
feature field but a probability belief on the SPD cone, so transport and
preconditioning are governed by Riemannian SPD machinery (the affine-invariant
metric and a [[Killing form|Killing-form]] per-block conditioner) and by information-geometric
[[Natural gradient]] updates, rather than by the Euclidean kernels of the original
CNN. In short, the gauge equivariant CNN supplies the *conceptual scaffolding*
— local frames, transport, holonomy, irrep coupling — that the VFE transformer
reinterprets probabilistically and optimizes variationally.

> [!note] Editorial: The mapping from a compact tangent-frame structure group to a
> non-compact GL(k) gauge group, and from hard kernel constraints to a soft
> cocycle penalty, is this project's reinterpretation; the cited sources establish
> the gauge/transport/holonomy machinery but do not themselves make these moves.

## Sources

- [[cohen-2019-gauge-cnn]] — introduces gauge equivariant CNNs and the Icosahedral CNN; the kernel constraint and parallel-transport rule.
- [[cohen-2016-gcnn]] — the global-symmetry G-CNN that gauge equivariance localizes.
- [[weiler-2019-e2-steerable]] — per-irrep kernel constraints and the steerable basis.
- [[kondor-2018-compact-group-conv]] — convolution as necessary and sufficient for compact-group equivariance.
- [[thomas-2018-tensor-field-networks]] — irrep-valued features coupled by the Clebsch-Gordan tensor product.
- [[finzi-2020-lieconv]] — Lie-algebra-first equivariant convolution for general Lie groups.
- [[bronstein-2021-geometric-deep-learning]] — the unifying gauge/equivariance blueprint.

## See also

- [[Group equivariant CNN (G-CNN)]]
- [[Steerable CNN]]
- [[LieConv]]
- [[Tensor Field Network]]
- [[Gauge equivariance and geometric deep learning]]
- [[Gauge transformation]]
- [[Parallel transport]]
- [[Holonomy]]
- [[Group equivariance]]
- [[Irreducible representation]]
- [[Clebsch-Gordan coefficients]]
- [[VFE Transformer Program]]
