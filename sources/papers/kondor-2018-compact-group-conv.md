---
type: paper
title: On the Generalization of Equivariance and Convolution in Neural Networks to the Action of Compact Groups
aliases:
  - "Kondor & Trivedi 2018 — Compact Group Convolution"
authors:
  - Risi Kondor
  - Shubhendu Trivedi
year: 2018
arxiv: "1802.03690"
url: https://arxiv.org/abs/1802.03690
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/mathematics
status: draft
created: 2026-06-18
updated: 2026-06-18
---

# On the Generalization of Equivariance and Convolution in Neural Networks to the Action of Compact Groups

> [!info] Citation
> Risi Kondor and Shubhendu Trivedi (2018). *On the Generalization of Equivariance and Convolution in Neural Networks to the Action of Compact Groups.* ICML 2018. arXiv:1802.03690. https://arxiv.org/abs/1802.03690

## TL;DR

Kondor and Trivedi prove that for a feed-forward network whose layers are linear and equivariant to the action of a compact group, the layer operation is *necessarily* a (generalized group) convolution — and conversely that group convolution is sufficient. The argument runs through the representation theory of compact groups and noncommutative harmonic analysis: equivariant linear maps decompose over the group's [[Irreducible representation]]s, so the only admissible weight-sharing scheme is convolution on the group (or its homogeneous spaces). This elevates convolution from a convenient engineering choice to a structural theorem, and supplies the theoretical license for building attention and feature transforms out of group-structured, irrep-indexed operations.

## Problem & setting

Convolutional networks owe much of their success to translation [[Group equivariance]]: shifting the input shifts the feature maps correspondingly. The translation group is abelian and the construction is classical, but it was not clear what the right generalization is when the symmetry of interest is a richer, possibly *noncommutative* compact group — rotations, permutations, or the structured groups that act on graphs and manifolds.

The paper asks a precise question: given a network layer that is linear and required to be equivariant to a compact group $G$ acting on its inputs and outputs, what form must that layer take? The setting is a single linear map between feature spaces on which $G$ acts (via possibly different representations), and the desideratum is equivariance — the layer commutes with the group action.

## Method

The analysis is harmonic-analytic. By the Peter–Weyl theorem, square-integrable functions on a compact group $G$ decompose into a direct sum of [[Irreducible representation]]s (irreps), and the same holds for functions on the homogeneous spaces $G$ acts on. The group action on a feature space therefore block-diagonalizes into irreducible pieces. Schur's lemma then constrains any $G$-equivariant linear map: between two copies of the same irrep it may only act as a scalar (or, with multiplicities, a small matrix), and between inequivalent irreps it must vanish.

Translating this constraint back from the Fourier (irrep) domain to the spatial domain shows that an equivariant linear map is exactly a *generalized convolution*: a correlation of the input against a learned filter, integrated over the group. The result is stated as a necessity-and-sufficiency theorem — convolutional weight sharing is not just one way to obtain equivariance, it is the only way for linear layers under a compact-group symmetry. The framework subsumes ordinary CNNs (translations), spherical and rotation-equivariant networks, and convolution on graphs and manifolds as special cases.

## Key results

- **Equivariance $\Leftrightarrow$ convolution.** For compact $G$, a linear layer is $G$-equivariant if and only if it is a generalized group convolution. Necessity is the novel half; sufficiency recovers the familiar story.
- **Irrep block structure.** The admissible filters and their action are organized by the irreducible representations of $G$; learning happens within the multiplicity spaces of each irrep, with no cross-irrep mixing permitted by a single equivariant linear map.
- **Unifying scope.** The theorem provides a common foundation for group-equivariant architectures across domains — images, spheres, graphs, manifolds — clarifying what earlier equivariant-CNN constructions were implicitly assuming.

## Relevance to this research

The VFE-transformer program is explicitly built on group structure — a block general-linear gauge group, a Lie-algebra "phi" parameterization, Clebsch–Gordan coupling, and explicit irrep decompositions — and Kondor & Trivedi supply the theorem that justifies organizing computation this way. Three connections are concrete:

- **License for irrep-structured operations.** The project decomposes features into irreps and couples them with Clebsch–Gordan coefficients. This paper proves that, under a group symmetry, equivariant linear maps *must* respect the irrep block structure (Schur's lemma), so the irrep bookkeeping is not optional decoration but the canonical form of any symmetric linear transform. See [[Clebsch-Gordan coefficients]] and [[Irreducible representation]].
- **Group-structured attention.** Insofar as the attention and feature-mixing layers are meant to be equivariant to the gauge action, the necessity result says the symmetric part of those operations is forced into group-convolutional form. This is the theoretical backbone for treating attention as a group-convolution / steerable operation rather than an unconstrained mix.
- **Caveat on the gauge group.** The theorem is stated for *compact* groups, whereas the project's gauge group is the (noncompact) block general-linear group GL(k). The harmonic-analytic machinery and the strict "convolution is necessary" conclusion do not transfer verbatim to noncompact groups.

> [!note] Editorial: For the noncompact GL(k) gauge group used in the project, this result applies cleanly only to compact subgroups (e.g., the orthogonal/rotation part), or as a guiding principle rather than a literal theorem. The companion local/gauge-equivariance papers in the registry are the more direct license for the full construction.

## Cross-links

- Concepts: [[Group equivariance]] · [[Irreducible representation]] · [[Clebsch-Gordan coefficients]] · [[Parallel transport]] · [[Holonomy]]
- Methods: [[Group equivariant CNN (G-CNN)]] · [[Gauge equivariant CNN]] · [[Steerable CNN]] · [[Tensor Field Network]] · [[LieConv]]
- Related sources: [[cohen-2016-gcnn]] · [[cohen-2019-gauge-cnn]] · [[weiler-2019-e2-steerable]] · [[thomas-2018-tensor-field-networks]] · [[bronstein-2021-geometric-deep-learning]] · [[finzi-2020-lieconv]]
- Themes: [[Gauge equivariance and geometric deep learning]]
- Project: [[VFE Transformer Program]]

```bibtex
@inproceedings{kondor2018generalization,
  title     = {On the Generalization of Equivariance and Convolution in Neural Networks to the Action of Compact Groups},
  author    = {Kondor, Risi and Trivedi, Shubhendu},
  booktitle = {Proceedings of the 35th International Conference on Machine Learning (ICML)},
  series    = {Proceedings of Machine Learning Research},
  volume    = {80},
  pages     = {2747--2755},
  year      = {2018},
  eprint    = {1802.03690},
  archivePrefix = {arXiv},
  primaryClass  = {stat.ML},
  url       = {https://arxiv.org/abs/1802.03690}
}
```
