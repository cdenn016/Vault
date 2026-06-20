---
type: reference
title: "Lie Groups, Lie Algebras, and Representations: An Elementary Introduction"
aliases:
  - "Hall 2015"
  - "Hall, Lie Groups"
authors:
  - "Brian C. Hall"
year: 2015
tags:
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
  - field/mathematics
created: 2026-06-18
updated: 2026-06-18
---

# Lie Groups, Lie Algebras, and Representations: An Elementary Introduction

> [!info] Citation
> Brian C. Hall (2015). *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*, 2nd edition. Graduate Texts in Mathematics, Vol. 222. Springer, Cham. ISBN 978-3-319-13466-6. DOI: 10.1007/978-3-319-13467-3.

## TL;DR

A rigorous but elementary graduate textbook that develops the theory of matrix Lie groups, their Lie algebras, and their representations using primarily linear algebra. It covers the matrix exponential, the Lie-algebra correspondence, the Baker–Campbell–Hausdorff formula, root systems, weights, and the representation theory of compact Lie groups, providing the standard structural results this project relies on whenever beliefs, gauge frames, or symmetries live on a Lie group.

## What it establishes

Working concretely with matrix Lie groups, the text establishes the core machinery linking a Lie group to its Lie algebra and back:

- The matrix exponential and logarithm, and the exp/log correspondence between a matrix Lie group and its Lie algebra, including the derivative of the exponential map.
- The [[Baker-Campbell-Hausdorff formula]], expressing $\log(e^X e^Y)$ as an iterated series of nested commutators, and its role in recovering group multiplication from the bracket.
- Representation theory: definitions of representations, the notion of an [[Irreducible representation]], complete reducibility for compact groups, characters, and the decomposition of tensor products via [[Clebsch-Gordan coefficients]].
- Structure theory of semisimple and compact Lie groups: root systems, weights, the Cartan subalgebra, the [[Killing form]] as an invariant bilinear form, and the Weyl character formula.
- The relationship between a Lie group's topology (connectedness, simple connectedness, covering groups) and the integrability of Lie-algebra representations to group representations.

The second edition adds a dedicated treatment of the structure and representation theory of compact Lie groups, a full derivation of root-system properties, and universal enveloping algebras with the Poincaré–Birkhoff–Witt theorem, Weyl character formula, and Kostant multiplicity formula.

## Why the project cites it

The gauge-theoretic, variational-free-energy program treats agents and their beliefs in terms of Lie-group symmetry, so Hall supplies the foundational vocabulary and theorems on which several constructions rest.

- **Gauge structure.** A [[Gauge transformation]] is a (local) Lie-group action on belief frames, and [[Agents as fibre-bundle sections]] move belief states between fibres whose structure group is a Lie group. Hall's exp/log correspondence and [[Baker-Campbell-Hausdorff formula]] are the concrete tools for composing such transformations and for relating infinitesimal generators (Lie algebra) to finite group elements used in [[Parallel transport]] and [[Holonomy]].

- **Equivariance.** [[Group equivariance]] and the equivariant-network methods cited by the manuscripts — [[Group equivariant CNN (G-CNN)]], [[Steerable CNN]], [[Gauge equivariant CNN]], and [[LieConv]] — are built on representation theory: feature spaces decompose into [[Irreducible representation]]s and couple via [[Clebsch-Gordan coefficients]] (as in [[Tensor Field Network]]s). Hall is the standard reference grounding these representation-theoretic prerequisites.

- **Information geometry of group-structured beliefs.** Where the project links curvature, mass, and inference — e.g. [[Mass as Fisher information]] and the [[Fisher information metric]] — the [[Killing form]] provides the canonical invariant metric on a semisimple Lie algebra, connecting the group's intrinsic geometry to the metric structure used in [[Natural gradient]] reasoning.

These uses align with the broader [[Gauge equivariance and geometric deep learning]] theme and the [[Gauge-Theoretic Multi-Agent VFE Model]] project. Hall is cited as a foundational mathematical reference rather than a source of specific empirical results.

> [!note] Editorial: This note summarizes the textbook's scope from its published description and standard contents; it does not attribute any project-specific result to Hall.

## BibTeX

```bibtex
@book{hall2015lie,
  title     = {Lie Groups, Lie Algebras, and Representations: An Elementary Introduction},
  author    = {Hall, Brian C.},
  year      = {2015},
  edition   = {2nd},
  series    = {Graduate Texts in Mathematics},
  volume    = {222},
  publisher = {Springer},
  address   = {Cham},
  isbn      = {978-3-319-13466-6},
  doi       = {10.1007/978-3-319-13467-3}
}
```
