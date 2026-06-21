---
type: paper
title: "Efficient Streaming Language Models with Attention Sinks"
aliases:
  - "Xiao 2024"
  - "StreamingLLM"
authors:
  - Xiao, Guangxuan
  - Tian, Yuandong
  - Chen, Beidi
  - Han, Song
  - Lewis, Mike
year: 2024
arxiv: "2309.17453"
url: https://arxiv.org/abs/2309.17453
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Efficient Streaming Language Models with Attention Sinks

> [!info] Citation
> Xiao, G., Tian, Y., Chen, B., Han, S., & Lewis, M. (2024). "Efficient Streaming Language Models with Attention Sinks." Published as a conference paper at ICLR 2024. arXiv:2309.17453.

## TL;DR
StreamingLLM enables LLMs trained on finite-length sequences to perform stable autoregressive generation over infinite-length input streams without any fine-tuning. The key insight is that initial tokens act as "attention sinks" — they accumulate disproportionate softmax attention mass not because of semantic content but because of positional exposure — and retaining just four such sink tokens alongside a rolling KV window fully recovers window-attention perplexity. On Llama-2 and related models, StreamingLLM achieves up to 22.2x speedup over the only quality-comparable baseline (sliding window with re-computation).

## Problem & setting
Deploying LLMs in streaming applications (multi-round dialogue, continuous generation) requires handling sequences far longer than the pre-training window (e.g., 4K for Llama-2). Dense attention is prohibitively expensive (O(T²) cache growth), while naive window attention catastrophically fails the moment initial tokens are evicted from the KV cache. Prior length-extrapolation work (RoPE interpolation, ALiBi) extends the window only finitely and still collapses well beyond training length.

## Method
StreamingLLM partitions the KV cache into two components: (1) a small set of attention sink tokens (empirically 4 initial tokens suffices) whose KV states are always retained, and (2) a rolling window of the most recent tokens. At each decoding step the cache is indexed by position within the cache rather than by position in the original text, which ensures compatibility with relative positional encodings (RoPE, ALiBi). The full algorithm requires no fine-tuning and plugs into any autoregressive LLM using standard GPU kernels.

The softmax attention normalizer identity drives the sink phenomenon: because softmax must partition unit probability mass across all attended positions, even semantically irrelevant positions accumulate score when no strong key match exists. Since initial tokens are visible to all subsequent positions during autoregressive training, they become the preferred receptacle for this excess probability.

An additional pre-training recommendation: prepending a single learnable "sink token" to every training sample produces a model that needs only that one token (rather than four random initial tokens) to anchor stable streaming behavior. The authors validate this with 160M-parameter models, showing no degradation on seven NLP benchmarks.

Key equations: standard softmax attention (Eq. 1), SoftMax-off-by-One variant SoftMax₁ (Eq. 2, equivalent to a zero-Key/Value prepended token), used as an ablation against the full learnable sink approach.

## Key results
StreamingLLM enables Llama-2-[7,13,70]B, MPT-[7,30]B, Falcon-[7,40]B, and Pythia-[2.9,6.9,12]B to model texts of 4 million tokens with stable perplexity, compared to collapse at the cache-size boundary for window attention. On PG-19 (65K tokens), Llama-2-13B window attention gives PPL 5158; StreamingLLM gives PPL 5.40, matching the oracle sliding-window-with-recomputation baseline (PPL 5.43). Per-token decoding latency is reduced by up to 22.2x over that baseline, while memory usage is identical. Substituting the original four initial tokens with newline "\n" tokens recovers equivalent perplexity, confirming that absolute position rather than semantic content is the operative factor. Pre-training with a learnable sink token achieves stable streaming with cache config 1+1023, whereas the vanilla model needs 4+1020.

## Relevance to this research
StreamingLLM's mechanistic analysis of softmax normalization and attention score distribution has structural parallels with the VFE transformer's treatment of the softmax beta as a variational stationary point. In the GL(K) free-energy framework, the tau*beta*log(beta/pi) entropy term is required precisely so the row-Lagrangian yields softmax rather than a delta — StreamingLLM's "sink" phenomenon is a complementary observation that the same softmax operation forces probability mass to accumulate at structurally accessible positions even absent semantic relevance. This is related to the question of what the attention prior pi_ij encodes: a uniform prior is blind to positional accessibility, whereas the sink phenomenon shows the learned transformer's effective prior is far from uniform. The rolling-KV cache with positional re-indexing is also relevant to sequence-level implementations of the VFE attention kernel, where maintaining O(L) rather than O(T) memory is a practical constraint. The dedicated sink token is analogous in spirit to a learned "null" or "vacuum" belief state that absorbs residual variational probability — a concept worth considering in the multi-agent active inference context.

## Cross-links
- Concepts: [[Attention Mechanism]], [[Softmax]], [[KV Cache]], [[Length Extrapolation]]
- Related sources: [[vaswani2017attention]], [[su2021roformer]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{xiao2024efficient,
  author    = {Guangxuan Xiao and Yuandong Tian and Beidi Chen and Song Han and Mike Lewis},
  title     = {Efficient Streaming Language Models with Attention Sinks},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2024},
  url       = {https://arxiv.org/abs/2309.17453},
}
```
