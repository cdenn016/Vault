---
type: concept
title: "Bidirectional attention"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Bidirectional attention

Bidirectional attention is the unmasked self-attention pattern used by encoder transformers (e.g. BERT), in which every token attends to all other tokens in the sequence, both preceding and following. This contrasts with the causal (masked) attention of autoregressive decoders, where each token may attend only to earlier positions. Bidirectional attention enables fully context-dependent token representations and is paired with the masked-language-modeling objective.

## Related
[[Masked language modeling]], [[Attention mechanisms — theory and positional structure]]

## Sources
[[devlin-2018-bert]]
