---
type: concept
title: "Sparse Attention"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Sparse Attention

Sparse attention restricts each query to attend over only a subset of keys (local windows, dilated/strided patterns, global tokens, or learned/block-sparse masks) so that the attention cost grows sub-quadratically with sequence length, enabling long-context transformers. Longformer (Beltagy et al. 2020) combines sliding-window local attention with a few global tokens; related schemes include Sparse Transformers, BigBird, and Reformer. In the VFE program it bounds the message-passing graph over tokens, a finite-capacity allocation analogous to the Sperling access bottleneck.

## Related
[[Attention mechanisms — theory and positional structure]], [[Self-attention]]

## Sources
[[beltagy2020longformer]]
