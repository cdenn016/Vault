---
type: paper
title: "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation"
aliases:
  - Press 2022
  - ALiBi
  - press2022train
  - press-2021-alibi
  - Press et al. 2021
  - Press (2021) ALiBi
authors:
  - Press, Ofir
  - Smith, Noah A.
  - Lewis, Mike
year: 2022
arxiv: "2108.12409"
url: https://arxiv.org/abs/2108.12409
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation

> [!info] Citation
> Press, O., Smith, N. A., & Lewis, M. (2022). "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation." *ICLR 2022*. arXiv:2108.12409.

## TL;DR
This paper introduces Attention with Linear Biases (ALiBi), a positional encoding method for transformers that replaces positional embeddings with a static, non-learned penalty added directly to attention scores, proportional to the distance between query and key tokens. ALiBi enables length extrapolation — the ability to perform well at inference on sequences longer than those seen during training — without additional runtime cost or parameters. A 1.3B-parameter model trained on sequences of length 1024 with ALiBi matches the perplexity of a sinusoidal model trained on length 2048, while training 11% faster and using 11% less memory.

## Problem & setting
Standard transformer language models fail to extrapolate to sequences longer than those seen during training; sinusoidal positional embeddings degrade rapidly beyond the training context length. The T5 relative-position bias (Raffel et al., 2020) allows better extrapolation but is substantially slower (at least 2x) than the sinusoidal approach. Prior alternatives such as rotary embeddings (Su et al., 2021) offer only modest improvements. The problem is to achieve efficient length extrapolation without runtime or parameter overhead.

## Method
ALiBi eliminates positional embeddings entirely. For each attention head, it adds a static scalar bias to the query-key dot product before the softmax, penalizing attention to distant tokens linearly:

$$\text{softmax}\!\left(q_i K^\top + m \cdot [-(i-1), \ldots, -1, 0]\right)$$

where $m$ is a head-specific, fixed (non-learned) slope. For $n$ heads, the slopes form a geometric sequence starting at $2^{-8/n}$ with ratio $2^{-8/n}$: for 8 heads this gives $\tfrac{1}{2^1}, \tfrac{1}{2^2}, \ldots, \tfrac{1}{2^8}$. The bias is implemented by modifying the causal mask matrix, adding no operations and incurring negligible memory overhead ($\le 100$ MB). Position information is injected at every layer (into keys and queries only, not values), analogously to the T5 bias and rotary methods. The slopes are fixed before training and not tuned per dataset or model size.

## Key results
On WikiText-103, ALiBi trained on $L = 512$ tokens achieves perplexity 18.40 extrapolating to $L_\text{valid} = 3072$, outperforming the sinusoidal baseline trained directly on $L = 3072$ (18.67), while being 1.84x faster to train. ALiBi outperforms all tested position methods (sinusoidal, rotary, T5 bias) at every training length even when not extrapolating. On the CC100+RoBERTa corpus with a 1.3B-parameter model, ALiBi trained on $L = 1024$ outperforms the sinusoidal model trained on $L = 2048$ by 0.09 perplexity when evaluating at $L_\text{valid} = 2048$, while using 3.1 GB less memory and reaching a given perplexity 11% faster. Extrapolation performance peaks at roughly $2L$ tokens and degrades gradually thereafter, but ALiBi maintains strong results even at $L_\text{valid} = 10000$ tokens.

## Relevance to this research
ALiBi is directly relevant to the VFE transformer's T5 relative-position attention prior channel. The VFE3 codebase implements a `t5_relative_bias` attention prior that adds a learned (or fixed) per-bucket scalar bias $b_{i-j}$ to attention scores — the same structural mechanism as ALiBi but with a learnable table and bucket discretization. The ALiBi paper establishes that non-learned, analytically defined position biases (linear distance penalties with geometric slope schedules) can match or exceed learned variants and enable extrapolation, supporting the design choice to keep `t5_learnable_bias=False` as the default (fixed $-\log(1 + \text{bucket})$ initialization). The insight that position information should be injected into queries and keys but not values — which ALiBi inherits from the T5 bias and rotary methods — is consistent with VFE3's gauge-theoretic treatment, where attention weights (arising from transport/KL terms) carry relational structure while value-like quantities (the transported beliefs $\Omega_{ij} q_j$) are position-free. The paper's analysis of the "early token curse" also provides empirical grounding for the recency-biased inductive structure built into ALiBi's linear penalty, which is structurally analogous to the distance-decaying attention priors in the VFE framework.

## Cross-links
- Concepts: [[Attention Mechanism]], [[Positional Encoding]], [[Length Extrapolation]], [[Attention mechanisms — theory and positional structure]]
- Related sources: [[vaswani2017attention]], [[raffel2020t5]], [[su2021roformer]]
- Manuscript/Project: [[VFE Transformer Program]], [[participatory-it-from-bit]]

> [!note] Editorial: In the PIFB reading, ALiBi is *derived* rather than an engineering trick: with an entropy-regularized consensus prior $\tau\,\beta_{ij}\log(\beta_{ij}/\pi_{ij})$ on belief coupling, taking the prior $\pi_{ij}$ to decay with distance shifts each attention logit by $\log\pi_{ij}$, and a log-prior linear in distance is exactly ALiBi's additive linear bias — the per-head slope $m$ reading as the strength of the distance prior. This is the additive log-prior complement to the multiplicative gauge-frame reading of RoPE ([[su2021roformer]]).

## BibTeX
```bibtex
@inproceedings{press2022train,
  author    = {Press, Ofir and Smith, Noah A. and Lewis, Mike},
  title     = {Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2022},
  url       = {https://arxiv.org/abs/2108.12409},
  note      = {arXiv:2108.12409}
}
```
