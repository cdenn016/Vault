---
type: paper
title: "Generalizing Convolutional Neural Networks for Equivariance to Lie Groups on Arbitrary Continuous Data"
aliases:
  - "Finzi et al. 2020 — LieConv"
authors:
  - Marc Finzi
  - Samuel Stanton
  - Pavel Izmailov
  - Andrew Gordon Wilson
year: 2020
arxiv: "2002.12880"
url: https://arxiv.org/abs/2002.12880
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/mathematics
status: stable
created: 2026-06-18
updated: 2026-06-20
---

# Generalizing Convolutional Neural Networks for Equivariance to Lie Groups on Arbitrary Continuous Data

> [!info] Citation
> Marc Finzi, Samuel Stanton, Pavel Izmailov, and Andrew Gordon Wilson (2020). *Generalizing Convolutional Neural Networks for Equivariance to Lie Groups on Arbitrary Continuous Data.* ICML 2020. arXiv:2002.12880.

## TL;DR

LieConv builds convolutional layers that are equivariant to *any* Lie group possessing a surjective exponential map, rather than only the translation group of ordinary CNNs. The trick is to lift raw inputs onto the group, parameterize all geometry through the Lie-algebra logarithm, and integrate a learned kernel over local neighborhoods measured in algebra coordinates. A single implementation works across images, molecular point clouds, and Hamiltonian dynamical systems simply by swapping in the group's `exp`/`log` maps; for dynamics this yields exact conservation of linear and angular momentum.

## Problem & setting

Standard convolution is equivariant to translations, which is why CNNs generalize across spatial position. Many domains, however, carry richer symmetry — rotations, scalings, the special Euclidean group SE(n), the affine group — and live on irregular, continuous point sets rather than pixel grids. Prior equivariant networks (see [[cohen-2016-gcnn]], [[cohen-2019-gauge-cnn]], [[weiler-2019-e2-steerable]]) typically commit to one symmetry group and often to a discretized domain. The paper asks: can one express a convolution whose equivariance group is a *parameter* of the construction, applicable to arbitrary continuous data?

## Method

The core move is to reformulate group convolution entirely in terms of the Lie algebra. Each input element is *lifted* to one or more group elements whose action carries a canonical origin to the data point. The relative displacement between two lifted points is then taken not in the ambient space but on the group, and mapped into the algebra via the logarithm. A learnable kernel (an MLP) consumes these algebra-valued displacements, so the kernel sees a coordinate that is invariant under the group action — the source of equivariance. Convolution becomes a Monte-Carlo integral over sampled local neighborhoods defined by an algebra-space metric, making the operator a true continuous convolution discretized by point sampling rather than by a grid.

Crucially, adapting LieConv to a new symmetry requires implementing only the group exponential `exp` and logarithm `log`; the abstraction handles SO(2), SO(3), SE(2), SE(3), the scaling/translation group, and others uniformly. Equivariance follows because the algebra coordinates of relative transformations are unchanged when the same group element acts on both arguments.

## Key results

- A single architecture, re-instantiated with different `exp`/`log` pairs, is competitive on rotated-MNIST style image tasks, on molecular property prediction over 3D point clouds, and on modeling Hamiltonian systems.
- For dynamical systems, baking in the relevant symmetry produces *exact* conservation of linear and angular momentum, a concrete demonstration that the equivariance is genuine and not merely approximate.
- The method scales to continuous, non-gridded data without resampling, by treating convolution as integration over sampled neighborhoods in algebra coordinates.

## Relevance to this research

LieConv is the closest geometric-deep-learning analogue to how the VFE transformer treats its gauge group. The project's `gauge_group` is `block_glk` — a block general-linear group GL(k) — and its frames are parameterized in the Lie algebra through a "phi" field, with the group exponential (and a Baker-Campbell-Hausdorff retraction) mapping algebra elements back to the group. LieConv validates exactly this design pattern: represent the group abstractly, do all learning and all metric computation in algebra (`log`) coordinates, and recover group elements via `exp`. The paper's insight that relative displacements measured in the algebra are the natural equivariant coordinate is directly the mechanism behind the project's [[Parallel transport]] and [[Holonomy]] bookkeeping, where transformations between token frames are composed on the group and read off in the algebra.

> [!note] Editorial: LieConv targets compact and Euclidean-motion groups with surjective `exp`; GL(k) is non-compact and its exponential is not globally surjective, so the project's BCH retraction is the practical substitute for the clean `exp`/`log` round-trip LieConv assumes. The conceptual parameterization transfers even though the convergence guarantees differ.

It also supplies the geometric-deep-learning framing — convolution as integration over a group with a learned, symmetry-respecting kernel — that connects to the project's Clebsch-Gordan coupling and irreducible-representation structure, themes shared with [[thomas-2018-tensor-field-networks]] and surveyed in [[bronstein-2021-geometric-deep-learning]]. Where LieConv quotients out symmetry to gain generalization, the VFE transformer instead *tracks* the gauge degrees of freedom as belief-carrying structure, but both rest on the same algebra-first treatment of a continuous Lie group.

## Cross-links

- [[Gauge transformation]] — LieConv's equivariance is invariance of the algebra coordinate under the group action.
- [[Group equivariance]] — the central property the construction guarantees.
- [[Parallel transport]] — composing relative transformations on the group, as the project does between token frames.
- [[Holonomy]] — the closed-loop residual of such transport.
- [[Irreducible representation]] and [[Clebsch-Gordan coefficients]] — shared machinery with steerable/tensor-field approaches.
- Related sources: [[cohen-2016-gcnn]], [[cohen-2019-gauge-cnn]], [[weiler-2019-e2-steerable]], [[kondor-2018-compact-group-conv]], [[thomas-2018-tensor-field-networks]], [[bronstein-2021-geometric-deep-learning]].
- Method pages: [[LieConv]], [[Gauge equivariant CNN]], [[Steerable CNN]], [[Group equivariant CNN (G-CNN)]], [[Tensor Field Network]].
- Project: [[VFE Transformer Program]].

```bibtex
@inproceedings{finzi2020generalizing,
  title     = {Generalizing Convolutional Neural Networks for Equivariance to Lie Groups on Arbitrary Continuous Data},
  author    = {Finzi, Marc and Stanton, Samuel and Izmailov, Pavel and Wilson, Andrew Gordon},
  booktitle = {Proceedings of the 37th International Conference on Machine Learning (ICML)},
  year      = {2020},
  eprint    = {2002.12880},
  archivePrefix = {arXiv},
  primaryClass  = {stat.ML},
  url       = {https://arxiv.org/abs/2002.12880}
}
```
