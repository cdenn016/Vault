---
type: concept
title: "Softmax"
aliases:
  - "softmax function"
  - "softmax normalization"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Softmax

The softmax function maps a real vector to a probability simplex via exponentiation and normalization, sigma(z)_i = exp(z_i) / sum_j exp(z_j). In transformer attention it converts query-key scores into a normalized attention distribution over keys, and it is equivalently the Gibbs/Boltzmann distribution at unit temperature. Softmax attention is the operation that modern Hopfield networks and streaming-LLM caches reinterpret, and within the VFE program its temperature/precision weighting connects to Fisher-information-based precision.

## Related
[[Mechanistic interpretability of attention]], [[Attention mechanisms — theory and positional structure]], [[Precision weighting|Precision-weighted attention]]

## Sources
[[ramsauer2021hopfield]], [[xiao2024efficient-streaming-llm]]
