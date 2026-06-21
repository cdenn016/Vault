---
type: concept
title: "Linear attention"
aliases:
  - "Linear transformer"
  - "Linear-attention transformer"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Linear attention

Linear attention replaces the softmax over query-key dot products with a kernel feature map phi, so that attention becomes phi(Q)(phi(K)^T V). This factorization lets the key-value contraction be computed once and reused, reducing the per-token cost from quadratic to linear in sequence length and enabling an equivalent autoregressive RNN formulation. It trades the expressivity of full softmax attention for scalability.

## Related
[[Kernel feature map]], [[Attention mechanisms — theory and positional structure]], [[Scaled dot-product attention]]

## Sources
[[katharopoulos-2020-linear-transformers]], [[tsai-2019-kernel-attention]]
