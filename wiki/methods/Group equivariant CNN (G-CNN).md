---
type: method
title: "Group equivariant CNN (G-CNN)"
aliases:
  - G-CNN
  - Group equivariant convolutional network
  - Group convolution
tags:
  - cluster/gauge-theory
  - project/transformer
status: stable
created: 2026-06-18
updated: 2026-07-09
---

# Group equivariant CNN (G-CNN)

## What it is

A **Group equivariant CNN (G-CNN)** is a convolutional network whose layers are provably equivariant to a discrete symmetry group larger than the translation group, introduced by Cohen and Welling in [[cohen-2016-gcnn]]. Where an ordinary CNN guarantees only that a shift of the input produces a corresponding shift of every feature map (translation equivariance), a G-CNN extends this guarantee to additional symmetries such as 90-degree rotations and reflections: transforming the input by a group element transforms the feature maps by the same element in a predictable, structure-preserving way. It is the foundational statement of the broader program now called geometric deep learning ([[bronstein-2021-geometric-deep-learning]]), namely that a *declared symmetry group* should dictate the architecture of a network rather than being learned from data.

## How it works

The mechanism is **group convolution**. Ordinary convolution slides a filter over an input by translating it; group convolution replaces the translation group with a larger group $G$ and accumulates an inner product of the input with a *group-transformed* copy of the filter for every element $g \in G$. The result is a feature map defined as a function on the group itself rather than on the spatial grid alone. Because the convolution sums over the full group orbit, applying any $g$ to the input merely permutes (acts on) the output feature map by that same $g$ — this is the formal equivariance property. Stacking such layers, with pointwise nonlinearities and group-pooling that respect the action, yields a network that is equivariant end to end while sharing weights across the entire symmetry group, which sharply improves sample efficiency and built-in generalization to transformed inputs.

[[kondor-2018-compact-group-conv]] later proved the deeper claim that group convolution is not merely *one* way to obtain equivariance but is **necessary and sufficient**: any linear layer equivariant to a compact group must be a group convolution, and admissible operations are organized by the group's [[Irreducible representation|irreducible representations]] via harmonic analysis. This representation-theoretic view connects G-CNNs to the [[Steerable CNN]] line ([[weiler-2019-e2-steerable]]), which reduces the general kernel constraint to a per-irrep constraint and a reusable steerable basis, and to continuous-group constructions such as [[LieConv]] ([[finzi-2020-lieconv]]) and [[Tensor Field Network|Tensor Field Networks]] ([[thomas-2018-tensor-field-networks]]), where features live in irreps and are combined through the [[Clebsch-Gordan coefficients|Clebsch-Gordan]] tensor product. The generalization from *global* group symmetry to *local* symmetry — where the group acts independently in each tangent frame and features must be carried between frames by [[Parallel transport]] — is the [[Gauge equivariant CNN]] of [[cohen-2019-gauge-cnn]].

## Strengths / limitations

The principal strength is a hard architectural guarantee: equivariance holds exactly, by construction, so the network need not waste capacity learning symmetries from augmented data, and it generalizes provably to group-transformed inputs. Weight sharing across the group also improves data efficiency. The matching property captured by [[Group equivariance]] makes the inductive bias interpretable and composable across layers.

The limitations are equally concrete. The original G-CNN handles only *discrete* groups (rotations by fixed angles, reflections); extending to continuous groups requires either the irrep machinery of steerable networks or the Lie-algebra/exponential-map approach of [[LieConv]]. The feature maps become functions on the group, raising memory and compute cost roughly in proportion to the group order. The guarantee is also rigid: it presumes the chosen symmetry is exactly present in the data, and a symmetry that holds only approximately or *locally* is not captured — the motivation for moving to gauge equivariance ([[cohen-2019-gauge-cnn]], [[bronstein-2021-geometric-deep-learning]]).

## Relation to this work

The VFE transformer does not perform image convolution, so it does not use a G-CNN layer directly. What it borrows is the **founding principle** that G-CNN crystallized: that a network's structure should be organized around a declared symmetry group whose action is respected throughout. In this project that group is the block general-linear group GL(k), a continuous (Lie) gauge group rather than a finite rotation group, so the relevant lineage runs from this page through [[Gauge equivariant CNN]] (local rather than global symmetry; [[Parallel transport]] of per-token beliefs between frames), [[LieConv]] (Lie-algebra "phi" parameterization with recovery by the exponential map), and the irrep/[[Clebsch-Gordan coefficients|Clebsch-Gordan]] bookkeeping of [[Steerable CNN|steerable]] and [[Tensor Field Network|tensor-field]] networks.

> [!note] Editorial (2026-07-10): the VFE transformer targets local frame covariance in its forward construction. Its optimizer does not certify exact equivariance: the audited frame table uses plain AdamW, while the optional Cartan/Killing and pullback conditioners are inactive and are neither full-$\mathrm{GL}(K)$ invariant nor Fisher natural gradients. [[gl-k-attention-2026-07-09-review-revision]]

The comparison is architectural: global discrete image symmetry versus local continuous token-frame covariance. No stronger optimizer-equivariance claim is made. [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[cohen-2016-gcnn]] — original Group Equivariant Convolutional Networks paper.
- [[kondor-2018-compact-group-conv]] — group convolution is necessary and sufficient for compact-group equivariance.
- [[weiler-2019-e2-steerable]] — per-irrep reduction of the kernel constraint.
- [[cohen-2019-gauge-cnn]] — generalization to local gauge equivariance.
- [[finzi-2020-lieconv]] — Lie-group equivariance via algebra coordinates.
- [[thomas-2018-tensor-field-networks]] — irrep features with Clebsch-Gordan coupling.
- [[bronstein-2021-geometric-deep-learning]] — the symmetry/equivariance blueprint situating G-CNNs.

## See also

- [[Group equivariance]]
- [[Gauge equivariant CNN]]
- [[Steerable CNN]]
- [[LieConv]]
- [[Tensor Field Network]]
- [[Irreducible representation]]
- [[Clebsch-Gordan coefficients]]
- [[Parallel transport]]
- [[Gauge transformation]]
- [[Gauge equivariance and geometric deep learning]]
