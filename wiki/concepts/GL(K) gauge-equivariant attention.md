---
type: concept
title: "GL(K) gauge-equivariant attention"
aliases:
  - "glkgaugeequivariantattention"
tags:
  - cluster/gauge-theory
  - cluster/attention
  - cluster/info-geometry
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# GL(K) gauge-equivariant attention

The central construction of the program's GL(K)_attention manuscript: an attention mechanism made equivariant under the general linear group GL(K) acting on the K-dimensional feature/frame space, with the symmetric space GL(K)/O(K) (the SPD manifold) as the belief/covariance geometry. Per-token gauge frames transform the query-key inner product via a congruence (sandwich) action so that attention scores are invariant to local GL(K) changes of basis, generalizing standard dot-product attention to a frame-covariant, information-geometric form. This is the manuscript's proposed reduction of dot-product vs. structured attention to a single gauge-covariant scheme.

## Related
[[Attention mechanisms — theory and positional structure]], [[Gauge equivariant CNN]], [[Gauge equivariance and geometric deep learning]], [[Variational free energy]], [[VFE Transformer Program]]

## Sources
[[cohen-2019-gauge-cnn]], [[bonnabel-2009-spd-fixed-rank]]
