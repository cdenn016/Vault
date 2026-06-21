---
type: concept
title: "Dimensionality reduction"
tags:
  - cluster/info-geometry
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Dimensionality reduction

Dimensionality reduction maps high-dimensional data to a low-dimensional representation that preserves salient structure, via linear methods (PCA) or nonlinear manifold/embedding methods (UMAP, t-SNE, autoencoders). In systems neuroscience, Gao & Ganguli (2017) show that high-dimensional neural population activity often lies on a low-dimensional manifold whose dimensionality is set by task complexity and smoothness, justifying low-dimensional analyses of recordings. In the VFE program it is the lens for inspecting learned belief representations (mu, Sigma), gauge frames, and per-layer hidden states, and connects to the intrinsic low-dimensionality of belief manifolds.

## Related
[[Fisher information metric]], [[VFE Transformer Program]]

## Sources
[[gao-2017-neural-dimensionality]], [[gao-2017-neural-dimensionality|gao-2017-neuroscience-dimensionality]], [[ganguli-2012-compressed-sensing-neuroscience]]
