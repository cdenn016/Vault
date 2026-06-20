---
type: paper
title: Gauge Equivariant Convolutional Networks and the Icosahedral CNN
aliases:
  - Cohen et al. 2019 — Gauge Equivariant CNN
authors:
  - Taco S. Cohen
  - Maurice Weiler
  - Berkay Kicanaoglu
  - Max Welling
year: 2019
arxiv: "1902.04615"
url: https://arxiv.org/abs/1902.04615
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/mathematics
status: stable
created: 2026-06-18
updated: 2026-06-18
---

# Gauge Equivariant Convolutional Networks and the Icosahedral CNN

> [!info] Citation
> Taco S. Cohen, Maurice Weiler, Berkay Kicanaoglu, Max Welling (2019). *Gauge Equivariant Convolutional Networks and the Icosahedral CNN*. ICML 2019. arXiv:1902.04615. https://arxiv.org/abs/1902.04615

## TL;DR

This paper generalizes the equivariance principle of convolutional networks from *global* symmetries (translations, rotations of the whole input) to *local* **gauge transformations** — arbitrary, position-dependent changes of the reference frame in which features are expressed. On a curved manifold there is no canonical way to choose a coordinate frame at each point, so any well-posed convolution must transform predictably when those frames are re-chosen. The authors define a convolution that is gauge equivariant, show it requires kernels constrained by group-representation theory and feature transport via **parallel transport**, and instantiate it efficiently on the icosahedron (a discretized sphere) using a single `conv2d` call.

## Problem & setting

Standard CNNs exploit *translation* equivariance, and group-equivariant CNNs (see [[cohen-2016-gcnn]], [[kondor-2018-compact-group-conv]]) extend this to global groups such as rotations. But on a general manifold there is no global symmetry group acting transitively, and — crucially — no globally consistent choice of tangent-space basis (a *frame* or *gauge*). To process signals on such a manifold one must (i) pick a local frame at every point to express feature vectors numerically, and (ii) guarantee that the network's output does not depend on this arbitrary choice. A change of local frame is a **gauge transformation**, valued in the structure group of the tangent bundle (e.g. SO(2) for an oriented surface). The paper's setting is therefore the differential geometry of feature fields on manifolds: features are sections of an associated vector bundle, transforming under a chosen group [[Irreducible representation]] when the gauge is changed.

## Method

A *gauge equivariant convolution* is a local operator whose output, when the input gauge is transformed by a position-dependent group element, transforms by the same element acted through the output representation. The authors derive that this requirement imposes a **linear constraint on the convolution kernel** (a representation-theoretic / Clebsch-Gordan-type condition relating input and output [[Irreducible representation]]s), exactly analogous to the steerability constraints of [[weiler-2019-e2-steerable]]. Because a kernel at point *p* must combine feature vectors sampled at neighboring points *q*, and those neighbors carry features in *their own* frames, the operator must first **parallel transport** neighboring features into the frame at *p* before contracting them with the kernel. Different paths of transport on a curved manifold accumulate a frame rotation — the **holonomy** — so the construction is intrinsically tied to the manifold's connection and curvature.

Concretely, the authors specialize the manifold to the **icosahedron**, whose near-regular hexagonal structure lets them unfold the surface to a flat grid; the gauge-equivariant convolution then reduces to a standard padded `conv2d` with the kernel constraint enforced by weight sharing across the six orientation channels. This yields an architecture that is fast and scalable while remaining equivariant to the icosahedral symmetry group and to local gauge changes.

## Key results

- A general theory: gauge equivariant CNNs are well-defined on any manifold with a chosen connection, and they subsume earlier global group-equivariant and [[Steerable CNN]] constructions as special cases — a perspective later folded into the broader program of [[bronstein-2021-geometric-deep-learning]].
- The kernel constraint and the parallel-transport rule are derived from first principles, making the [[Gauge transformation]] behavior exact rather than approximate.
- The Icosahedral CNN achieves strong results on spherical/omnidirectional tasks — omnidirectional image segmentation (climate pattern segmentation, 2D-to-3D shape tasks) — at a fraction of the cost of spherical-harmonic spherical CNNs, validating that an intrinsic, gauge-equivariant design is both principled and practical.

## Relevance to this research

This is the canonical reference for the **gauge-theoretic core** of the VFE-transformer program (see [[VFE Transformer Program]]). Several model ingredients map directly onto its constructions:

- **Gauge frames and the block-GL(k) group.** The model expresses per-token quantities in learned local frames and acts on them with a block general-linear group. The paper supplies the precise meaning of a position-dependent [[Gauge transformation]] and the requirement that all operations be equivariant to re-choosing those frames — the design discipline the transformer inherits from token to token.
- **Transport of per-token beliefs.** The model parallel-transports per-token Gaussian beliefs (mu, Sigma) between positions and accumulates holonomy. This paper is the deep-learning source for using [[Parallel transport]] to move feature vectors between frames before they interact, and for treating path-dependent frame rotation as [[Holonomy]] — exactly the machinery behind transporting beliefs along the token sequence.
- **Representation structure and Clebsch-Gordan coupling.** The kernel constraint here is a representation-theoretic coupling between input and output [[Irreducible representation]]s, the same algebra invoked by the model's Clebsch-Gordan coupling and irreps. It tells us how features in different irreps may be combined while preserving [[Group equivariance]].

> [!note] Editorial: This paper treats *deterministic* feature fields, not probabilistic beliefs; the VFE-transformer's extension is to transport a full Gaussian belief (mean and SPD covariance) rather than a point feature. The gauge-equivariance and parallel-transport scaffolding carries over, but the SPD-covariance transport law is an additional ingredient supplied elsewhere in the program.

## Cross-links

- Concepts: [[Gauge transformation]], [[Parallel transport]], [[Holonomy]], [[Irreducible representation]], [[Group equivariance]], [[Clebsch-Gordan coefficients]]
- Methods: [[Gauge equivariant CNN]], [[Steerable CNN]], [[Group equivariant CNN (G-CNN)]]
- Related sources: [[cohen-2016-gcnn]], [[weiler-2019-e2-steerable]], [[kondor-2018-compact-group-conv]], [[thomas-2018-tensor-field-networks]], [[bronstein-2021-geometric-deep-learning]]
- Theme: [[Gauge equivariance and geometric deep learning]]

```bibtex
@inproceedings{cohen2019gauge,
  title     = {Gauge Equivariant Convolutional Networks and the Icosahedral {CNN}},
  author    = {Cohen, Taco S. and Weiler, Maurice and Kicanaoglu, Berkay and Welling, Max},
  booktitle = {Proceedings of the 36th International Conference on Machine Learning (ICML)},
  year      = {2019},
  eprint    = {1902.04615},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/1902.04615}
}
```
