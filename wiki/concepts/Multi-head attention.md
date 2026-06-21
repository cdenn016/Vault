---
type: concept
title: "Multi-head attention"
aliases:
  - "multiheadattention"
  - "MHA"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Multi-head attention

The transformer mechanism (Vaswani et al. 2017) that runs several scaled-dot-product attention operations ('heads') in parallel on linearly projected subspaces of the queries, keys, and values, then concatenates and projects the results. Different heads specialize to distinct relational/positional patterns, though many are prunable with little loss (Voita 2019). It is the architectural baseline the program's gauge-covariant attention generalizes.

## Related
[[Attention mechanisms — theory and positional structure]], [[GL(K) gauge-equivariant attention]], [[Mechanistic interpretability of attention]]

## Sources
[[voita-2019-attention-heads]], [[clark-2019-bert-attention]]
