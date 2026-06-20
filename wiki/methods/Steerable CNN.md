---
type: method
title: Steerable CNN
aliases:
  - Steerable CNNs
  - E(2)-Steerable CNN
  - Steerable convolutional network
  - Equivariant steerable network
tags:
  - cluster/gauge-theory
  - project/transformer
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Steerable CNN

## What it is

A **steerable CNN** is a convolutional network whose feature maps transform as
*fields of group representations* rather than as bare scalar activations, so that
a symmetry acting on the input induces a known, structured (and usually
fibre-wise) transformation of every intermediate feature. The decisive design
move is to decompose each feature space into **irreducible representations**
(irreps) of the symmetry group and to constrain every convolution kernel to be
**equivariant** per irrep. The most general and practically influential statement
of the idea is the **General E(2)-Equivariant Steerable CNN** of Weiler and Cesa
([[weiler-2019-e2-steerable]]), which gives a unified theory for convolutions
equivariant to the Euclidean group of the plane and its subgroups. It builds on
the broader equivariant-CNN program seeded by [[cohen-2016-gcnn]] and formalized
representation-theoretically by [[kondor-2018-compact-group-conv]]. See
[[Group equivariance]] and [[Irreducible representation]] for the underlying
concepts.

## How it works

The mechanism rests on three coupled ideas.

**Feature fields typed by representations.** Instead of treating a feature map as
`C` independent scalar channels, a steerable CNN assigns to each feature a
*field type* — a group representation `rho` under which the channel block
transforms. A scalar field transforms trivially; a vector field rotates with the
input; higher irreps rotate with higher angular frequency. Concretely, when the
group element `g` acts on the domain, the feature map transforms as the input is
moved *and* its channels are mixed by `rho(g)`. This is the network-internal
realization of the [[Gauge transformation]] picture: the representation tells you
exactly how the "frame" attached to each point rotates.

**The kernel constraint, solved per irrep.** Equivariance of a convolution is
equivalent to a linear constraint on the kernel relating input-type `rho_in` and
output-type `rho_out`. The central technical contribution of
[[weiler-2019-e2-steerable]] is that this constraint *decouples* into independent
constraints on each pair of irreps, each of which is solved analytically once and
reused. The solution space is a finite-dimensional **steerable basis** indexed by
angular frequency; learning then amounts to choosing coefficients in that fixed
basis. This is what makes "steerable" literal: a basis filter at one orientation
generates the whole orbit of oriented filters by a closed-form linear
recombination, so the network never has to store or learn rotated copies. The
necessity-and-sufficiency backbone — that group convolution is *the* equivariant
linear map for a compact group, organized by irreps — comes from
[[kondor-2018-compact-group-conv]].

**Coupling fields via tensor products and Clebsch-Gordan.** When two
representation-typed features interact nonlinearly or multiplicatively, their
combined type is a tensor product of representations, which is reducible. The
**Clebsch-Gordan** decomposition re-expresses that tensor product back into a
direct sum of irreps, keeping every layer's features in the canonical
irrep-typed form. This bookkeeping is most explicit in the SO(3) setting of
[[thomas-2018-tensor-field-networks]], where spherical-harmonic filters and the
Clebsch-Gordan tensor product couple irrep features in 3D; the planar steerable
construction of [[weiler-2019-e2-steerable]] is the E(2) analogue. See
[[Clebsch-Gordan coefficients]].

Steerable CNNs are best read as the *global-symmetry* specialization of the more
general **gauge-equivariant** construction of [[cohen-2019-gauge-cnn]]: a
steerable CNN fixes a global representation choice and a flat domain, whereas a
gauge CNN allows the frame (gauge) to vary from point to point on a curved
manifold and carries features between points by [[Parallel transport]]. Both sit
inside the Erlangen-Program synthesis of [[bronstein-2021-geometric-deep-learning]],
which casts CNNs, GNNs, and Transformers as instances of one
symmetry/equivariance blueprint.

## Strengths / limitations

**Strengths.** Equivariance is *exact and built in*, not learned from
augmentation, which yields strong sample efficiency and guarantees on how
predictions transform. Reducing the kernel constraint to per-irrep solutions
([[weiler-2019-e2-steerable]]) makes a single library cover an entire family of
groups (rotations, reflections, their finite subgroups) with provable
correctness, and the steerable basis is parameter-light because orientations are
generated analytically rather than stored.

**Limitations.** The clean theory is tied to *known, compact, well-understood*
symmetry groups with tractable irrep tables; it does not directly handle
non-compact or data-dependent symmetries, and extending beyond the chosen group
requires re-deriving bases. Strict equivariance can also over-constrain a model
when the true task symmetry is only approximate. Continuous-group generality is
better served by Lie-algebra/log-coordinate approaches such as
[[finzi-2020-lieconv]], and curved-domain generality by the gauge formulation
([[cohen-2019-gauge-cnn]]).

## Relation to this work

The VFE transformer is gauge-theoretic, and steerable CNNs supply the cleanest
template for the representation-theoretic plumbing it adopts.

> [!note] Editorial: The connections below map the steerable-CNN machinery onto
> the VFE transformer's declared ingredients (GL(k) gauge group, irreps,
> Clebsch-Gordan coupling, BCH-composed positional encodings). The cited sources
> establish each mechanism; the architectural mapping is this wiki's reading.

**What it borrows.** The project's **irrep**-indexed feature organization and
**Clebsch-Gordan** block coupling are exactly the steerable-CNN/tensor-field
discipline of [[weiler-2019-e2-steerable]] and [[thomas-2018-tensor-field-networks]]:
features carry representation types, interactions live in tensor products, and the
Clebsch-Gordan decomposition restores canonical irrep form. The per-irrep
*reduction* of the kernel constraint is the conceptual ancestor of the
architecture's per-block treatment of its `block_glk` (block GL(k)) gauge group —
each block handled by its own representation-aware rule rather than a monolithic
constraint.

**What it differs from / improves.** Steerable CNNs fix a *global* representation
on a flat grid; the VFE transformer instead carries *local* gauge frames and
transports per-token Gaussian beliefs between positions, which is the
gauge-equivariant generalization of [[cohen-2019-gauge-cnn]] rather than the
global-symmetry steerable case — bringing [[Parallel transport]] and
[[Holonomy]] into play. Its gauge group GL(k) is the general linear group, broader
than the compact orthogonal groups the classic steerable theory is built for, so
the project leans on Lie-algebra ("phi") parameterization with a
[[Baker-Campbell-Hausdorff formula|Baker-Campbell-Hausdorff]] retraction (the log-coordinate philosophy of
[[finzi-2020-lieconv]]) instead of fixed orthogonal-group irrep tables. Steerable
positional structure also reappears in the attention layer: learned positional
`phi` composed via BCH (alongside RoPE, ALiBi, and T5 buckets) plays, for the
[[Group equivariance|equivariant]] Transformer, the role the steerable basis plays
for convolutions, modifying the softmax-attention baseline of
[[vaswani-2017-attention]]. Finally, where steerable CNNs are point estimators of
deterministic feature fields, the VFE transformer attaches a variational
[[Variational free energy|free-energy]] objective and SPD-manifold belief
covariances to each token, so the equivariant scaffolding inherited here is
wrapped in inference machinery the original steerable framework does not address.

## Sources

- [[weiler-2019-e2-steerable]] — General E(2)-equivariant steerable CNNs; the
  per-irrep kernel constraint and reusable steerable basis.
- [[cohen-2016-gcnn]] — Group-equivariant CNNs; the foundational
  declared-symmetry-structures-architecture statement.
- [[kondor-2018-compact-group-conv]] — Representation-theoretic proof that group
  convolution is necessary and sufficient for compact-group equivariance.
- [[thomas-2018-tensor-field-networks]] — SO(3) irrep features coupled by
  spherical harmonics and the Clebsch-Gordan tensor product.
- [[cohen-2019-gauge-cnn]] — Gauge-equivariant generalization to curved manifolds
  with parallel transport.
- [[finzi-2020-lieconv]] — Lie-group equivariance via log/exp coordinates.
- [[bronstein-2021-geometric-deep-learning]] — Erlangen-Program synthesis placing
  steerable CNNs in the broader equivariance blueprint.
- [[vaswani-2017-attention]] — The Transformer baseline the equivariant positional
  machinery modifies.

## See also

- [[Group equivariant CNN (G-CNN)]]
- [[Gauge equivariant CNN]]
- [[LieConv]]
- [[Tensor Field Network]]
- [[Group equivariance]]
- [[Irreducible representation]]
- [[Clebsch-Gordan coefficients]]
- [[Gauge transformation]]
- [[Parallel transport]]
- [[Holonomy]]
- [[Gauge equivariance and geometric deep learning]]
