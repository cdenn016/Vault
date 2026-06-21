---
type: concept
title: "Recurrent networks"
aliases:
  - "recurrentnetworks"
  - "RNN"
tags:
  - cluster/cs-ml
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Recurrent networks

Recurrent neural networks (RNNs) process sequences by maintaining a hidden state that is updated at each step, sharing weights across time. They can in principle model arbitrary temporal dependencies but suffer from the vanishing/exploding gradient problem over long horizons, which gated variants (LSTM, GRU) mitigate via additive memory cells and multiplicative gates. RNNs are the sequential predecessors that attention/transformers replaced with parallel, content-addressable mixing of tokens.

## Related
[[Vanishing gradient problem]], [[Attention mechanisms — theory and positional structure]]

## Sources
[[hochreiter1997long]]
