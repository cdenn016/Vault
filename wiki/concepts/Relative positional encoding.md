---
type: concept
title: "Relative positional encoding"
aliases:
  - "Relative position bias"
  - "Relative position embeddings"
  - "Relative Position Encoding"
  - "Relative position encoding"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-09-23
---

# Relative positional encoding

Relative positional encoding makes attention depend on the offset between query and key (i-j) rather than on absolute token indices, improving length generalization and translation invariance. Introduced by Shaw et al. (2018), the original scheme adds learned relative-position biases into the key (and optionally value) terms of the attention score, improving translation quality and generalization to unseen sequence lengths. Later variants include T5-style learned per-offset biases ([[raffel2020exploring|raffel-2020-t5]]), the Transformer-XL segment-recurrence relative scheme, rotary embeddings (RoPE), and ALiBi's linear distance penalty. Through the kernel view of attention these are interchangeable positional kernels layered on the similarity smoother, and the VFE Transformer composes several of them with its gauge-algebra positional signal.

Additive positional biases can be read as log-priors over the attended position. [[bianchessi-2026-bayesian-attention-mechanism]] shows that with additive scores the attention weight factors into content and position terms, so that NoPE is a uniform prior and ALiBi a Laplace prior, and it proposes a generalized Gaussian prior. [[litman-2026-attention-priors]] learns a relative log-prior $\sum_r[\alpha_r\cos\omega_r(i-j)+\beta_r\sin\omega_r(i-j)]$ plus a key-only sink term. That relative prior has the same function class as the global positional bias of Transformer-XL ([[dai2019transformerxl]], Section 3.3, term (d)).

## Related
[[Attention mechanisms — theory and positional structure]], [[kazemnejad-2023-positional-encoding-length-generalization|Positional encoding and length generalization]]

## Sources
[[dai2019transformerxl]], [[raffel2020exploring|raffel-2020-t5]], [[bianchessi-2026-bayesian-attention-mechanism]], [[litman-2026-attention-priors]]
