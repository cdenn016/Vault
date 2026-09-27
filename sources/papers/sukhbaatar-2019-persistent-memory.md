---
type: paper
title: "Augmenting Self-attention with Persistent Memory"
aliases:
  - Sukhbaatar 2019
  - sukhbaatar2019
  - All-attention layer
  - Persistent memory attention
authors:
  - Sukhbaatar, Sainbayar
  - Grave, Edouard
  - Lample, Guillaume
  - Jegou, Herve
  - Joulin, Armand
year: 2019
arxiv: "1907.01470"
url: https://arxiv.org/abs/1907.01470
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
created: 2026-09-27
---

# Augmenting Self-attention with Persistent Memory

> [!info] Citation
> Sukhbaatar, S., Grave, E., Lample, G., Jégou, H., & Joulin, A. (2019). *Augmenting Self-attention with Persistent Memory*. arXiv:1907.01470.

## TL;DR
The paper removes the feed-forward sublayer of a transformer and instead appends a set of learned, input-independent "persistent" key and value vectors to every self-attention layer. Each token then attends jointly over the context and the persistent vectors in one softmax. The resulting all-attention layer reaches language-modeling results on par with a standard transformer, supporting the reading of the feed-forward sublayer as attention over a fixed learned memory.

## Problem & setting
A transformer block alternates self-attention with a position-wise feed-forward network. The feed-forward network holds a large share of the parameters, but its role was not explained in the same terms as attention.

## Method
A feed-forward layer $W_2\,\sigma(W_1x)$ is read as attention of the query $x$ over keys (rows of $W_1$) and values (columns of $W_2$), with $\sigma$ in place of softmax. The authors replace it with $N$ persistent key/value pairs concatenated to the context keys/values in each attention head, so a single softmax normalizes over context and memory together.

## Key results
Per the abstract, the feed-forward layer can be removed "without degrading the performance of a transformer", with results at parity on character- and word-level language modeling benchmarks. The evidence is parity, not a gain.

## Relevance to this research
This is the closest empirical precedent for [[Template routing]], the proposed replacement of the vfe3 block MLP by Gibbs routing to learned Gaussian templates. Template routing differs in three ways: its keys are Gaussian templates compared by KL rather than vectors compared by dot product, its routing weights are derived from a mixture-prior free energy, and it keeps a separate normalization after the attention step rather than one joint softmax over peers and memory. The joint-softmax variant studied here corresponds to a single mixture prior over both peers and concepts.

## Cross-links
- Concepts: [[Attention Mechanism]], [[Associative Memory]], [[Memory-Augmented Networks]], [[Softmax]]
- Methods: [[Template routing]]
- Related sources: [[geva-2021-ffn-key-value-memories]], [[ramsauer2021hopfield]], [[sukhbaatar-2015-end-to-end-memory]], [[dennis-2026-template-routing]]

## BibTeX
```bibtex
@article{sukhbaatar2019persistent,
  author  = {Sukhbaatar, Sainbayar and Grave, Edouard and Lample, Guillaume and J{\'e}gou, Herv{\'e} and Joulin, Armand},
  title   = {Augmenting Self-attention with Persistent Memory},
  journal = {arXiv preprint arXiv:1907.01470},
  year    = {2019}
}
```
