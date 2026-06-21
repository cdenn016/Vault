---
type: concept
title: "Relative positional encoding"
aliases:
  - "Relative position bias"
  - "Relative position embeddings"
  - "Relative Position Encoding"
  - "Relative position encoding"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Relative positional encoding

Relative positional encoding makes attention depend on the offset between query and key (i-j) rather than on absolute token indices, improving length generalization and translation invariance. Introduced by Shaw et al. (2018), the original scheme adds learned relative-position biases into the key (and optionally value) terms of the attention score, improving translation quality and generalization to unseen sequence lengths. Later variants include T5-style learned per-offset biases ([[raffel-2020-t5]]), the Transformer-XL segment-recurrence relative scheme, rotary embeddings (RoPE), and ALiBi's linear distance penalty. Through the kernel view of attention these are interchangeable positional kernels layered on the similarity smoother, and the VFE Transformer composes several of them with its gauge-algebra positional signal.

## Related
[[Attention mechanisms — theory and positional structure]], [[Positional encoding and length generalization]]

## Sources
[[dai2019transformerxl]], [[raffel-2020-t5]]
