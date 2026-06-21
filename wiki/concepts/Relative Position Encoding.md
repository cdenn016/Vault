---
type: concept
title: "Relative Position Encoding"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Relative Position Encoding

Relative position encoding injects positional information into self-attention as a function of the offset between query and key positions (i-j) rather than via absolute position embeddings added to the input. Introduced by Shaw et al. (2018), it adds learned relative-position biases into the key (and optionally value) terms of the attention score, improving translation quality and generalization to sequence lengths unseen in training. The relative formulation underlies later schemes (T5 relative bias, rotary embeddings, ALiBi) and is central to the program's interest in how positional structure interacts with attention geometry and length generalization.

## Related
[[Positional encoding and length generalization]], [[Attention mechanisms — theory and positional structure]]

## Sources
[[raffel-2020-t5]]
