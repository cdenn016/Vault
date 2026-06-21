---
type: paper
title: "e3nn: Euclidean Neural Networks"
aliases:
  - "Geiger 2022"
  - "e3nn"
authors:
  - Geiger, Mario
  - Smidt, Tess
year: 2022
arxiv: "2207.09453"
url: https://arxiv.org/abs/2207.09453
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/physics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# e3nn: Euclidean Neural Networks

> [!info] Citation
> Geiger, Mario and Tess Smidt (2022). "e3nn: Euclidean Neural Networks." arXiv:2207.09453 [cs.LG].

## TL;DR

e3nn is a general-purpose Python library for constructing E(3)-equivariant (Euclidean-group-equivariant) trainable functions on 3D geometric data. Its central abstraction is a parameterizable `TensorProduct` class that realizes any bilinear equivariant operation between irreducible representations (irreps) of O(3) via Clebsch-Gordan coefficients, enabling composable construction of equivariant convolutions, attention mechanisms, and other modules. The framework unifies Tensor Field Networks, 3D Steerable CNNs, SE(3)-Transformers, and Clebsch-Gordan Networks as special cases.

## Problem & setting

Geometric data in 3D (point clouds, vector fields, molecular structures) naturally transforms under the Euclidean group E(3) — rotations, translations, and inversion. Standard neural networks require massive data augmentation to learn 3D patterns in arbitrary orientations, and invariant models (restricted to scalars) cannot predict geometric quantities of order $l > 0$. Prior equivariant works each hand-crafted their own equivariant operations, leading to fragmented and error-prone implementations. The paper addresses the lack of a general, composable framework that cleanly handles all irreps of O(3) including parity.

## Method

The core primitive is the `TensorProduct` class, which implements the most general bilinear equivariant map between two sets of O(3) irreps. Each irrep is indexed by angular momentum $l \in \{0, 1, 2, \ldots\}$ and parity $p \in \{+1, -1\}$. The allowed coupling paths satisfy the triangle rule and parity product:
$$|l_1 - l_2| \le l_3 \le l_1 + l_2, \quad p_1 p_2 = p_3.$$
Path weights $w$ are learnable scalars (invariant under E(3)), and the Clebsch-Gordan coefficients $C^{l_1,l_2,l_3}_{ijk}$ provide the change of basis:
$$(\text{path value})_k = \frac{1}{\sqrt{m_1 m_2}} \sum_{u,v,i,j} w_{uvw} C_{ijk} (\text{in}_1)_{ui} (\text{in}_2)_{vj}.$$
Real-valued irreps are used throughout (exploiting the equivalence of SO(3) irreps to their conjugates), with a basis-change from the complex QuTiP convention. Spherical harmonics $Y^l : \mathbb{R}^3 \to \mathbb{R}^{2l+1}$ serve as the equivariant embedding of geometric inputs, shown to be unique (up to sign) on the sphere and polynomial on $\mathbb{R}^3$. Weight initialization follows the Maximal Update Parametrization ($\mu$P) to ensure all layers learn in the infinite-width limit. Parity-equivariance (O(3) rather than just SO(3)) is handled by tracking even/odd parity of every channel.

## Key results

The `TensorProduct` class is provably universal: it can represent any bilinear equivariant operation between two sets of irreps (Lemma 7.1). The `ReducedTensorProduct` class additionally handles index-symmetry constraints (e.g., symmetric or antisymmetric tensors of arbitrary rank) by intersecting the permutation-symmetric subspace with the irrep decomposition. Empirically, models built with higher-order irreps ($l > 1$) show a better power-law exponent on learning curves (not just a constant shift), implying genuine improvement in data efficiency beyond what coordinate-frame augmentation can achieve. The library subsumes SE(3)-Transformers, Tensor Field Networks, 3D Steerable CNNs, Spherical CNNs, and Clebsch-Gordan Networks as instances of its primitives.

## Relevance to this research

This paper is directly relevant to the GL(K) gauge-equivariant attention architecture of the VFE transformer. The VFE program uses GL(K) as the structure group acting on $K$-dimensional belief means $\mu$; e3nn instantiates analogous structure for O(3)/E(3). The key conceptual bridge is the decomposition of feature channels into irreducible representations and the use of Clebsch-Gordan tensor products as the only permissible bilinear coupling — the same principle underlies the isotypic decomposition and irrep-block structure discussed in the GL(K) manuscript (`GL(K)_attention.tex`) for the Schur-commutant head mixer and the `use_cg_coupling=True` path. The `ReducedTensorProduct` for symmetric tensors is relevant to SPD belief geometry (symmetric positive-definite matrices decompose as $1 \times 0e + 1 \times 2e$ under SO(3)). The treatment of equivariant attention in Section 8 (citing SE(3)-Transformers) provides a worked reference implementation that parallels the gauge-transport attention of the VFE transformer. The $\mu$P initialization discussion is relevant to training stability of the VFE transformer's learned parameters (connection weights, head mixers).

## Cross-links
- Concepts: [[Group equivariance|Gauge Equivariance]], [[Irreducible representation|Irreducible Representations]], [[Clebsch-Gordan Coefficients]], [[GL(K) gauge-equivariant attention|GL(K) Attention]], [[Clebsch-Gordan coefficients|Tensor Product]]
- Related sources: [[fuchs-2020-se3-transformer|fuchs2020se3transformers]], [[kondor-2018-compact-group-conv|kondor2018clebsch]], [[thomas-2018-tensor-field-networks|thomas2018tensor]]
- Manuscript/Project: [[VFE Transformer Program]], [[gl-k-attention|GL(K) Attention Manuscript]]

## BibTeX
```bibtex
@article{geiger2022e3nn,
  author  = {Geiger, Mario and Smidt, Tess},
  title   = {e3nn: {E}uclidean Neural Networks},
  journal = {arXiv preprint arXiv:2207.09453},
  year    = {2022},
  url     = {https://arxiv.org/abs/2207.09453},
}
```
