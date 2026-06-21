---
type: concept
title: "Relative positional encoding"
aliases:
  - "Relative position bias"
  - "Relative position embeddings"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Relative positional encoding

Relative positional encoding makes attention depend on the offset between query and key rather than on absolute token indices, improving length generalization and translation invariance. Variants include Shaw/T5-style learned per-offset biases, the Transformer-XL segment-recurrence relative scheme, rotary embeddings (RoPE), and ALiBi's linear distance penalty. Through the kernel view of attention these are interchangeable positional kernels layered on the similarity smoother, and the VFE Transformer composes several of them with its gauge-algebra positional signal.

## Related
[[Attention mechanisms — theory and positional structure]], [[Positional encoding and length generalization]]

## Sources
[[dai2019transformerxl]]
