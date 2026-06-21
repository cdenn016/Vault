---
type: concept
title: "Masked language modeling"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Masked language modeling

Masked language modeling (MLM) is the self-supervised pretraining objective introduced for BERT: a fraction of input tokens are replaced with a [MASK] symbol and the model is trained to reconstruct the original tokens from bidirectional context. Unlike left-to-right (causal) language modeling, MLM conditions each prediction on both left and right context, yielding deep bidirectional representations. It is the canonical pretraining task for encoder transformers.

## Related
[[Bidirectional attention]], [[Attention mechanisms — theory and positional structure]]

## Sources
[[devlin-2018-bert]]
