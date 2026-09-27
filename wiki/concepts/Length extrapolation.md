---
type: concept
title: "Length extrapolation"
aliases:
  - "Length generalization"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-09-23
---

# Length extrapolation

Length extrapolation is a transformer's ability to handle sequences longer at inference than any seen during training, generalizing its positional handling beyond the trained context window. It is largely governed by the positional-encoding scheme: relative biases such as ALiBi and rotary embeddings (RoPE), plus attention-sink / streaming tricks, extrapolate far better than learned absolute positions. It is a central evaluation axis for positional structure in attention and for the program's gauge-theoretic treatment of positional information.

Probabilistic positional priors are a recent route to extrapolation. The generalized Gaussian prior of [[bianchessi-2026-bayesian-attention-mechanism]] supports passkey retrieval at up to 500 times the training context, and the learned prior of [[litman-2026-attention-priors]] extrapolates where RoPE degrades in its 125M- and 1.23B-parameter language-model experiments.

## Related
[[Attention mechanisms — theory and positional structure]], [[Mechanistic interpretability of attention]]

## Sources
[[press2022-alibi]], [[xiao2024efficient-streaming-llm]], [[su2024roformer]], [[bianchessi-2026-bayesian-attention-mechanism]], [[litman-2026-attention-priors]]
