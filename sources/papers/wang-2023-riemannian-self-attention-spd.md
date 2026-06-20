---
type: paper
title: Riemannian Self-Attention Mechanism for SPD Networks
aliases:
  - "Wang 2023 — Riemannian Self-Attention for SPD"
  - SMSA
authors:
  - Rui Wang
  - Xiao-Jun Wu
  - Hui Li
  - Josef Kittler
year: 2023
arxiv: "2311.16738"
url: https://arxiv.org/abs/2311.16738
tags:
  - cluster/spd-geometry
  - project/transformer
  - field/cs-ml
  - field/mathematics
status: draft
created: 2026-06-18
updated: 2026-06-18
---

# Riemannian Self-Attention Mechanism for SPD Networks

> [!info] Citation
> Rui Wang, Xiao-Jun Wu, Hui Li, Josef Kittler (2023). *Riemannian Self-Attention Mechanism for SPD Networks*. arXiv:2311.16738. https://arxiv.org/abs/2311.16738

## TL;DR

The paper builds a self-attention mechanism that operates directly on data living on the manifold of symmetric positive-definite (SPD) matrices, rather than on flat Euclidean vectors. Instead of dot-product similarity and weighted vector sums, the proposed **SPD manifold self-attention (SMSA)** module computes affinities and aggregates values using genuinely Riemannian operations — the affine-invariant Riemannian metric, the Riemannian (Karcher/Fréchet) mean as the geometry-aware analogue of a weighted average, and Riemannian optimization for training. This makes it, to date, the closest existing bridge between [[SPD-manifold geometry and Riemannian optimization]] and [[Attention mechanisms — theory and positional structure]].

## Problem & setting

SPD matrices — covariance descriptors, second-order statistics, region covariances — are widely used because they compactly encode spatiotemporal correlation structure. Crucially, they do not live in a vector space: the set of SPD matrices is a curved Riemannian manifold, and naively applying Euclidean operations (ordinary averaging, Euclidean distances) distorts distances and can even leave the manifold. A family of SPD networks (e.g. [[huang-2017-spdnet|huang-2017-spdnet]]) already learns hierarchical SPD features through bilinear (BiMap) and nonlinear (ReEig/LogEig) layers, but the authors argue these architectures do not explicitly model the *geometric dependencies between features across layers*, leading to what they call an **information degradation problem**: discriminative second-order structure is progressively washed out as it passes through the network. The goal is an attention mechanism that re-weights and re-aggregates SPD features while respecting the manifold geometry.

## Method

The core contribution is the **SPD manifold self-attention (SMSA)** mechanism, built from three manifold-valued ingredients:

- **Riemannian metric.** Pairwise affinities between SPD tokens are measured with a Riemannian distance (the affine-invariant metric, $d(P,Q)=\lVert \log(P^{-1/2} Q P^{-1/2})\rVert_F$, in the spirit of [[pennec-2006-affine-invariant-tensor|pennec-2006-affine-invariant-tensor]] and [[bhatia-2007-positive-definite-matrices|bhatia-2007-positive-definite-matrices]]). This replaces the Euclidean dot product that defines attention scores in standard transformers.
- **Riemannian mean.** Value aggregation — the attention-weighted "sum" — is realized as a *weighted Riemannian mean* (Karcher/Fréchet barycenter) of the value SPD matrices, the geometry-correct analogue of $\sum_j \alpha_j v_j$ on a curved space. The attention weights derived from the metric supply the barycentric coefficients.
- **Riemannian optimization.** The whole module is trained with manifold-aware optimization, keeping parameters and intermediate features valid SPD matrices throughout (cf. [[absil-2008-optimization-matrix-manifolds|absil-2008-optimization-matrix-manifolds]], [[bonnabel-2013-riemannian-sgd|bonnabel-2013-riemannian-sgd]]).

These are assembled into an **SMSA-based geometric learning module (SMSA-GLM)** that is stacked to enhance the discriminative power of the learned SPD representations and counteract information degradation.

## Key results

Across three benchmark datasets the SMSA-equipped network improves classification accuracy over baseline SPD architectures, with the authors attributing the gain to the geometry-aware attention's ability to preserve discriminative second-order structure that ordinary SPD networks lose between layers.

## Relevance to this research

This paper is the most direct prior art for a key move in the VFE-transformer program: attention over **manifold-valued beliefs**. In our architecture each token carries a Gaussian belief $(\mu, \Sigma)$ with $\Sigma$ an SPD covariance, retracted via `spd_affine` under the affine-invariant Riemannian metric — exactly the manifold and metric SMSA uses for its affinities and means. Several concrete connections:

- **Precision-weighted attention.** Our `precision_weighted_attention` weights token interactions by belief precision $\Sigma^{-1}$. SMSA shows how to define attention *scores* from a Riemannian distance between SPD matrices rather than a Euclidean inner product, which is the natural way to compare precisions/covariances without leaving the manifold.
- **Aggregation as a Riemannian mean.** Where a standard transformer forms a convex combination of value vectors, SMSA's weighted Riemannian mean is the principled aggregator when the "values" are covariances/precisions — directly applicable to combining per-token $\Sigma$'s in the E-step of our [[Variational EM|variational-em]] / filtering update.
- **SPD optimization machinery.** SMSA's reliance on Riemannian optimization mirrors our `spd_affine` retraction and Riemannian-SGD style updates for $\Sigma$.

> [!note] Editorial: SMSA does not address precision *weighting from a variational objective*, Renyi/alpha divergences, or the gauge structure (GL(k) frames, BCH retraction) central to our program; it treats SPD attention as a discriminative feature-learning device, not as inference over Gaussian beliefs. It is best read as the SPD-geometry "attention primitive" we adapt, with the variational and gauge layers supplied separately.

## Cross-links

- Manifold and metric: [[SPD-manifold geometry and Riemannian optimization]], [[pennec-2006-affine-invariant-tensor|pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices|bhatia-2007-positive-definite-matrices]], [[arsigny-2006-log-euclidean|arsigny-2006-log-euclidean]]
- Optimization: [[absil-2008-optimization-matrix-manifolds|absil-2008-optimization-matrix-manifolds]], [[bonnabel-2013-riemannian-sgd|bonnabel-2013-riemannian-sgd]]
- SPD networks: [[huang-2017-spdnet|huang-2017-spdnet]]
- Attention: [[Attention mechanisms — theory and positional structure]], [[vaswani-2017-attention|vaswani-2017-attention]], [[tsai-2019-kernel-attention|tsai-2019-kernel-attention]]
- Program: [[VFE Transformer Program]]

```bibtex
@article{wang2023riemannian,
  title   = {Riemannian Self-Attention Mechanism for {SPD} Networks},
  author  = {Wang, Rui and Wu, Xiao-Jun and Li, Hui and Kittler, Josef},
  journal = {arXiv preprint arXiv:2311.16738},
  year    = {2023},
  eprint  = {2311.16738},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV},
  url     = {https://arxiv.org/abs/2311.16738}
}
```
