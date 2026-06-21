---
type: concept
title: "Transformer Architecture"
aliases:
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Transformer Architecture

The Transformer is a sequence model built from stacked self-attention and position-wise feed-forward blocks with residual connections and layer normalization, dispensing with recurrence in favor of fully attention-based token mixing. Positional information enters via encodings rather than sequence order. It is the architectural substrate the VFE/gauge-theoretic program reinterprets: self-attention as precision-weighted message passing / gauge transport over a token graph.

## Related
[[Attention mechanisms — theory and positional structure]], [[gl-k-attention|Attention as gauge-theoretic variational inference]], [[VFE Transformer Program|Gauge-Theoretic VFE Transformer]], [[VFE Transformer Program]]

## Sources
[[vaswani-2017-attention]], [[dosovitskiy-2020-vit]], [[radford2019-gpt2]], [[clark-2019-bert-attention]], [[hoffmann-2022-chinchilla]]
