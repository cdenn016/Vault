---
type: paper
title: "Attention Is All You Need"
aliases:
  - "Vaswani 2017"
  - "Transformer"
  - "Scaled dot-product attention"
  - "vaswani2017attention"
  - "vaswani2017-attention"
  - "vaswani2017"
  - "vaswani2017-attention-all-you-need"
authors:
  - Vaswani, Ashish
  - Shazeer, Noam
  - Parmar, Niki
  - Uszkoreit, Jakob
  - Jones, Llion
  - Gomez, Aidan N.
  - Kaiser, Lukasz
  - Polosukhin, Illia
year: 2017
arxiv: "1706.03762"
url: https://arxiv.org/abs/1706.03762
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
status: stable
created: 2026-06-18
updated: 2026-06-20
---

# Attention Is All You Need

> [!info] Citation
> Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). "Attention Is All You Need." *Advances in Neural Information Processing Systems (NeurIPS)*, 30. https://arxiv.org/abs/1706.03762

## TL;DR

This paper introduces the Transformer, a sequence-transduction architecture built entirely from attention, dispensing with recurrence and convolution. Its core primitive is scaled dot-product attention — a softmax-normalized weighting of value vectors by query–key inner products scaled by $1/\sqrt{d_k}$ — packaged into multi-head attention so several attention subspaces are computed in parallel. Position information, absent from the permutation-symmetric attention operator, is injected by sinusoidal positional encodings. The model set new BLEU records on English-to-German (28.4) and English-to-French (41.8) translation while training in a fraction of the time of prior recurrent and convolutional systems.

## Problem & setting

Before this work, the dominant sequence models were recurrent (LSTM/GRU) or convolutional encoder–decoder networks, optionally augmented with attention. Recurrence forces sequential computation along the sequence length, which caps parallelism and lengthens the gradient path between distant tokens. The paper asks whether attention alone — a mechanism that directly relates any two positions in $O(1)$ sequential steps regardless of their distance — can replace recurrence and convolution entirely. The setting is supervised sequence-to-sequence learning, evaluated primarily on WMT machine translation and on English constituency parsing.

## Method

The Transformer is an encoder–decoder stack. Each layer is composed of two sublayers — a multi-head self-attention sublayer and a position-wise feed-forward network — each wrapped in a residual connection followed by layer normalization.

**Scaled dot-product attention.** Given queries $Q$, keys $K$, and values $V$, the operator computes $\mathrm{softmax}(QK^\top / \sqrt{d_k})\,V$. The $1/\sqrt{d_k}$ factor counteracts the growth of dot products in high dimension, which would otherwise push the softmax into low-gradient saturated regions. The softmax row is a probability distribution over source positions; attention is thus a convex, data-dependent averaging of value vectors.

**Multi-head attention.** Queries, keys, and values are linearly projected into $h$ lower-dimensional subspaces; attention is computed independently in each head; the outputs are concatenated and projected back. Different heads can specialize to different relational patterns.

**Self-attention vs. cross-attention.** Encoder self-attention attends over the source; decoder self-attention is causally masked so each position attends only to earlier positions; encoder–decoder attention lets the decoder query the encoded source.

**Positional encodings.** Because attention is invariant to input permutation, fixed sinusoidal functions of position are added to token embeddings to supply order information; learned embeddings were found to perform comparably.

**Position-wise feed-forward and regularization.** A two-layer MLP applied identically at every position, plus residual dropout and label smoothing, complete the block.

## Key results

- New state-of-the-art BLEU on WMT 2014 English-to-German (28.4) and English-to-French (41.8), surpassing prior single models and ensembles.
- Substantially reduced training cost relative to the best recurrent and convolutional models, owing to full parallelization across sequence positions.
- Successful transfer to English constituency parsing, evidencing generality beyond translation.
- Ablations established the value of multiple heads and of the scaling factor, and characterized the favorable computational complexity of self-attention versus recurrence for typical sequence lengths.

## Relevance to this research

The gauge-theoretic VFE transformer treats this architecture as the baseline it deforms, so several of its ingredients are best understood as modifications of the scaled dot-product operator defined here.

**Precision-weighted attention.** The softmax weighting $\mathrm{softmax}(QK^\top/\sqrt{d_k})$ is the object that `precision_weighted_attention` generalizes: instead of a uniform $1/\sqrt{d_k}$ temperature, the VFE model weights query–key compatibility by the per-token belief precision (the inverse of the Gaussian covariance $\Sigma$), tying attention strength to inferred confidence in the spirit of [[Precision weighting]]. The attention-entropy regularizer in the VFE model also acts directly on the softmax distribution this paper introduces.

**Positional structure.** The sinusoidal positional encodings here are the seed of a whole family of position priors the VFE model layers in — RoPE rotary phases, ALiBi distance biases, and T5 relative-position buckets — and ultimately of the learned Lie-algebra phase $\phi$ composed via the Baker–Campbell–Hausdorff retraction. Each of these reshapes how query–key scores depend on relative position, the degree of freedom this paper first made explicit and modular.

**Multi-head structure and block geometry.** The split into independent projection subspaces (heads) is the structural ancestor of the block-$GL(k)$ gauge group's per-block organization: where this paper concatenates independent linear heads, the gauge model attaches a general-linear frame to each block and transports it.

**Causal masking.** The decoder's causal mask underlies the causal beta/gamma attention priors of the VFE model.

> [!note] Editorial: The connections to precision weighting, the SPD covariance, and the gauge frame are interpretive bridges drawn by this research program; this paper itself frames attention purely as softmax-weighted value averaging with sinusoidal positions.

For the kernel-theoretic reading of softmax attention that this baseline invites, see [[tsai-2019-kernel-attention]]; for a Riemannian attention operator that acts directly on SPD-valued tokens, see [[wang-2023-riemannian-self-attention-spd]]. The program-level synthesis lives in [[VFE Transformer Program]].

## Cross-links

- Concepts: [[Precision weighting]], [[Prediction error]]
- Themes: [[Attention mechanisms — theory and positional structure]]
- Related sources: [[tsai-2019-kernel-attention]], [[wang-2023-riemannian-self-attention-spd]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@inproceedings{Vaswani2017,
  author        = {Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and
                   Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N. and
                   Kaiser, Lukasz and Polosukhin, Illia},
  title         = {Attention Is All You Need},
  booktitle     = {Advances in Neural Information Processing Systems (NeurIPS)},
  volume        = {30},
  year          = {2017},
  eprint        = {1706.03762},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/1706.03762}
}
```
