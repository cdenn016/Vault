---
type: paper
title: "Improving Neural Language Models with a Continuous Cache"
aliases:
  - "Grave 2017"
  - "Neural Cache Model"
authors:
  - Grave, Edouard
  - Joulin, Armand
  - Usunier, Nicolas
year: 2017
arxiv: "1612.04426"
url: https://arxiv.org/abs/1612.04426
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Improving Neural Language Models with a Continuous Cache

> [!info] Citation
> Grave, E., Joulin, A., & Usunier, N. (2017). "Improving Neural Language Models with a Continuous Cache." ICLR 2017. arXiv:1612.04426.

## TL;DR
The Neural Cache Model augments any pre-trained recurrent neural network language model with a lightweight external memory that stores recent hidden activations as keys, retrieving them via dot-product similarity with the current hidden state. This continuous analogue of the classical n-gram cache requires no additional training and scales to cache sizes in the thousands, yielding substantial perplexity reductions (up to 30% over the LSTM baseline on WikiText-2) and near-human performance gains on the LAMBADA long-range coreference benchmark.

## Problem & setting
Standard recurrent neural network language models (LSTMs) are trained on a fixed corpus and cannot adapt their predictions to the immediate document context at test time. Classical n-gram cache models addressed this for count-based models, but no analogous mechanism existed that exploited the rich distributed representations learned by neural networks. Prior memory-augmented networks (Memory Networks, Neural Turing Machines) can adapt dynamically but require learning parameterized read/write operators, limiting scalable cache sizes and imposing fine-tuning cost.

## Method
At each time step t the model maintains a cache of pairs (h_i, x_{i+1}) — past hidden states paired with the word they generated. The cache distribution over vocabulary word w is:

    p_cache(w | h_{1..t}, x_{1..t}) ∝ Σ_i 1{w = x_{i+1}} exp(θ h_t^⊤ h_i)

where θ controls the sharpness of the dot-product retrieval. The final prediction interpolates the static vocabulary distribution p_vocab with the cache:

    p(w) = (1 − λ) p_vocab(w | h_t) + λ p_cache(w | h_{1..t}, x_{1..t})

Alternatively, a global softmax normalization jointly scores vocabulary logits and cache matches. No gradient flows through the cache at training time; hyperparameters θ and λ are selected on the validation set. Because there is no learned lookup operator, cache sizes of 500–10,000 tokens are tractable.

## Key results
On Penn Treebank (PTB), the Neural Cache Model on top of an LSTM baseline of perplexity 82.3 reaches test perplexity 72.1, competitive with the Pointer Sentinel LSTM (70.9) and Variational LSTM (73.4). On WikiText-2 with a cache of 2,000 tokens, perplexity drops from 99.3 to 68.9 (30% reduction), matching the Pointer Sentinel LSTM at cache size 100 and substantially surpassing it at larger caches. On text8 the model achieves 99.9 vs. a baseline of 121.8. On LAMBADA, the neural cache reduces development perplexity from 4,088 to 138, a dramatic improvement over all count-based and vanilla LSTM baselines.

## Relevance to this research
The Neural Cache Model implements a form of non-parametric, dot-product-based retrieval over past hidden states that is structurally adjacent to the VFE transformer's attention mechanism: the softmax over hidden-state dot products is exactly the attention operation, while the interpolation parameter λ corresponds to a belief-coupling weight. The cache distribution p_cache is a normalized mixture of point masses selected by inner-product similarity, analogous to how the VFE attention weights β_{ij} are formed from KL-based or dot-product scores. The distinction that this model requires no training of the retrieval operator parallels the VFE program's preference for closed-form, analytically derived attention kernels rather than learned projections. The LAMBADA results illustrate that long-range associative retrieval (capturing a referent introduced many sentences prior) can be achieved by simple dot-product memory, which is relevant to the question of whether gauge-equivariant VFE attention can replicate or exceed such long-range coherence without learned key/query projections.

## Cross-links
- Concepts: [[Attention Mechanism]], [[Memory-Augmented Networks]], [[Language Modeling]]
- Related sources: [[merity2016pointer]], [[sukhbaatar2015end]], [[graves2014neural]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{grave2017improving,
  author    = {Grave, Edouard and Joulin, Armand and Usunier, Nicolas},
  title     = {Improving Neural Language Models with a Continuous Cache},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2017},
  eprint    = {1612.04426},
  archivePrefix = {arXiv},
}
```
