---
type: concept
title: "KV Cache"
aliases:
  - "key-value cache"
  - "kvcache"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# KV Cache

The key-value (KV) cache is the standard autoregressive-decoding optimization in transformers: the key and value projections computed for past tokens are stored and reused at each new generation step, so self-attention costs scale linearly per step rather than recomputing the full prefix. The cache's size grows with sequence length, making it the dominant memory bottleneck for long-context inference and the target of methods such as attention sinks / streaming attention, sliding windows, and KV-cache compression.

## Related
[[Attention mechanisms — theory and positional structure]], [[VFE Transformer Program]]

## Sources
[[xiao2024efficient-streaming-llm]]
