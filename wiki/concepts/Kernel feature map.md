---
type: concept
title: "Kernel feature map"
aliases:
  - "Feature map"
  - "Kernel feature maps"
tags:
  - cluster/attention
  - cluster/info-geometry
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Kernel feature map

A kernel feature map phi maps inputs into a (possibly high- or infinite-dimensional) feature space so that an inner product phi(x)·phi(y) reproduces a kernel k(x,y). In the kernel view of attention, the softmax similarity is interpreted as one such kernel; choosing an explicit, finite-dimensional positive feature map (e.g. elu+1, or random features) linearizes attention by making the similarity an explicit inner product, which underlies linear attention.

## Related
[[Linear attention]], [[Attention mechanisms — theory and positional structure]]

## Sources
[[katharopoulos-2020-linear-transformers]], [[tsai-2019-kernel-attention]]
