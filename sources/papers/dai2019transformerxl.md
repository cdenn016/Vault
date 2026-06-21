---
type: paper
title: "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context"
aliases:
  - "Dai 2019"
  - "Transformer-XL"
  - "TransformerXL"
authors:
  - Dai, Zihang
  - Yang, Zhilin
  - Yang, Yiming
  - Carbonell, Jaime
  - Le, Quoc V.
  - Salakhutdinov, Ruslan
year: 2019
arxiv: "1901.02860"
url: https://arxiv.org/abs/1901.02860
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context

> [!info] Citation
> Dai, Z., Yang, Z., Yang, Y., Carbonell, J., Le, Q. V., & Salakhutdinov, R. (2019). "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context." *Proceedings of ACL 2019*. https://arxiv.org/abs/1901.02860

## TL;DR
Transformer-XL introduces a segment-level recurrence mechanism that allows transformer models to attend beyond a fixed-length context window by caching and reusing hidden states from previous segments. To remain coherent with this recurrence under shifted inputs, a novel relative positional encoding scheme replaces the standard absolute positional embeddings, enabling the model to generalize to sequences of arbitrary length at inference time. The result is a language model that captures long-range dependencies more effectively than standard transformers and vanilla RNNs, achieving state-of-the-art perplexity on several word-level and character-level benchmarks.

## Problem & setting
Standard transformer language models process fixed-length context segments and discard all context across segment boundaries during training. This fragmentation prevents the model from learning dependencies that span longer contexts, and at inference time the fixed-size context window also limits predictive range. Recurrent networks handle variable-length sequences but struggle to propagate gradients over many steps. Transformer-XL is designed to overcome the fixed-context limitation without sacrificing the parallelism and representation power of self-attention.

## Method
The core contribution is a **segment-level recurrence** mechanism: when processing segment $\tau+1$, the hidden states $\mathbf{h}_\tau^{n}$ from the previous segment $\tau$ at each layer $n$ are cached (detached from the computation graph) and concatenated with the current segment's keys and values before attention is computed. This extends the effective context without backpropagating through cached history.

Because cached tokens shift relative positions with each new segment, absolute positional encodings become inconsistent. The paper replaces them with **relative positional encodings**: instead of adding a fixed positional vector to each token embedding, the attention logit between query at position $i$ and key at position $j$ is decomposed as

$$
\mathbf{A}_{i,j} = \mathbf{q}_i^\top \mathbf{W}_Q^\top \mathbf{W}_{K,E} \mathbf{k}_j + \mathbf{q}_i^\top \mathbf{W}_Q^\top \mathbf{W}_{K,R} \mathbf{r}_{i-j} + u^\top \mathbf{W}_{K,E} \mathbf{k}_j + v^\top \mathbf{W}_{K,R} \mathbf{r}_{i-j},$$

where $\mathbf{r}_{i-j}$ is a fixed sinusoidal encoding of the relative offset $i-j$ and $u, v$ are learned global bias vectors. This four-term decomposition separates content-to-content, content-to-position, position-to-content, and position-to-position attention scores.

## Key results
- Achieves 0.99 bits-per-character on enwiki8 and 1.08 on text8 (state-of-the-art at time of publication).
- Word-level perplexity of 54.5 on WikiText-103 and 21.8 on Penn Treebank, outperforming all previous models.
- The effective context captured during evaluation extends to 1,600+ tokens (recurrence over multiple cached segments), compared to 450 tokens for a standard transformer with the same total computation.
- Inference is up to 1,800x faster than a standard transformer baseline because the cached states eliminate recomputation of overlapping context.

## Relevance to this research
Transformer-XL's **relative positional encoding** is the direct ancestor of the T5 relative-position bias used in the VFE transformer (`train_vfe3.py`, `t5_relative_bias` attention prior channel, `t5_learnable_bias` toggle). The four-term decomposition in the Transformer-XL score is the mathematical origin of the T5 simplification that retains only the relative-offset scalar bias added to attention logits. Understanding this lineage clarifies what the T5 positional prior is approximating — a content-independent, offset-only summary of the Transformer-XL relative score — and informs interpretation of `t5_learnable_bias` as learning exactly that scalar table $b_{i-j}$.

The segment-level recurrence is less directly used in the current VFE3 architecture but is conceptually related to the belief-propagation across sequence positions: the VFE attention mechanism iteratively updates belief tuples $(\mu, \Sigma, \phi)$ through transport operators $\Omega_{ij}$, and the question of how context window length versus recurrence affects free-energy minimization is an open architectural question for longer sequences. The relative-encoding ideas here also inform how positional structure enters the attention prior $\pi_{ij}$ without breaking gauge equivariance (since the T5 bias is a scalar offset added after the gauge-invariant KL transport term, leaving the gauge structure intact).

## Cross-links
- Concepts: [[Relative Positional Encoding]], [[Attention mechanisms — theory and positional structure|Self-Attention]], [[Language Modeling]]
- Related sources: [[vaswani-2017-attention|vaswani2017attention]], [[raffel2020exploring|raffel2020t5]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{dai2019transformerxl,
  author    = {Dai, Zihang and Yang, Zhilin and Yang, Yiming and Carbonell, Jaime and Le, Quoc V. and Salakhutdinov, Ruslan},
  title     = {Transformer-{XL}: Attentive Language Models Beyond a Fixed-Length Context},
  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  year      = {2019},
  pages     = {2978--2988},
  url       = {https://arxiv.org/abs/1901.02860},
}
```
