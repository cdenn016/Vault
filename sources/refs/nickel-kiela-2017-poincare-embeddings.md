---
type: reference
title: "Poincaré Embeddings for Learning Hierarchical Representations"
aliases:
  - "Nickel & Kiela 2017"
  - "Poincaré Embeddings"
authors:
  - Maximilian Nickel
  - Douwe Kiela
year: 2017
arxiv: "1705.08039"
url: https://arxiv.org/abs/1705.08039
tags:
  - cluster/spd-geometry
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/mathematics
created: 2026-06-19
updated: 2026-06-19
---

# Poincaré Embeddings for Learning Hierarchical Representations

> [!info] Citation
> Maximilian Nickel and Douwe Kiela (2017). "Poincaré Embeddings for Learning Hierarchical Representations." *Advances in Neural Information Processing Systems* 30 (NeurIPS 2017). arXiv:1705.08039. <https://arxiv.org/abs/1705.08039>

## TL;DR

This paper embeds hierarchical (tree-like) data into the **Poincaré ball model of hyperbolic space** and learns the embeddings by Riemannian optimization. Hyperbolic space has exponentially growing volume with radius, so it can represent the exponentially branching structure of a tree with low distortion in few dimensions — something Euclidean space cannot do. The learned embeddings simultaneously encode hierarchy (depth toward the boundary) and similarity (angular proximity), and they beat Euclidean embeddings markedly on data with latent hierarchies.

## What it establishes

- Hyperbolic geometry as the natural host for hierarchical/tree-structured data, with distortion bounds Euclidean space cannot match at comparable dimension.
- A Riemannian SGD procedure (gradients pulled back through the hyperbolic metric, with retraction onto the ball) for learning the embeddings.
- Strong empirical gains on taxonomy and graph-hierarchy embedding tasks at low dimensionality.

## Why the project cites it

PIFB ([[participatory-it-from-bit]]) is built on a **hierarchical tower** of agents and meta-agents, and Nickel & Kiela supply the geometric warrant that hierarchical structure is most faithfully represented on a curved, non-Euclidean manifold rather than in flat space. The manuscript cites it in support of representing hierarchy geometrically, which resonates with the project's own use of curved manifolds — belief covariances on the affine-invariant SPD manifold ([[pennec-2006-affine-invariant-tensor]]) and gauge frames on a Lie group — and with the volume-form weighting that integrates each scale's free energy against $\sqrt{|g|}$ on a curved base. The Riemannian-optimization method is the same family as the project's natural-gradient retractions for $(\mu, \Sigma, \phi)$ ([[amari-1998-natural-gradient]], [[absil-2008-optimization-matrix-manifolds]]). Together this connects PIFB's [[Meta-agents and hierarchical emergence]] to the broader case that hierarchy and curvature belong together, complementing the IB/predictive-complexity reading of the same tower ([[bialek-2001-predictability-complexity]]).

```bibtex
@inproceedings{nickel2017poincare,
  title         = {Poincar\'e Embeddings for Learning Hierarchical Representations},
  author        = {Nickel, Maximilian and Kiela, Douwe},
  booktitle     = {Advances in Neural Information Processing Systems 30 (NeurIPS)},
  year          = {2017},
  eprint        = {1705.08039},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  url           = {https://arxiv.org/abs/1705.08039}
}
```
