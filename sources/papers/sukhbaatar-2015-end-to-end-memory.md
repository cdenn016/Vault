---
type: paper
title: "End-To-End Memory Networks"
aliases:
  - "sukhbaatar2015end"
  - "Sukhbaatar 2015"
  - "End-To-End Memory Networks"
authors:
  - "Sukhbaatar, Sainbayar"
  - "Szlam, Arthur"
  - "Weston, Jason"
  - "Fergus, Rob"
year: 2015
url: https://arxiv.org/abs/1503.08895
venue: "Advances in Neural Information Processing Systems (NeurIPS)"
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# End-To-End Memory Networks

> [!info] Citation
> Sukhbaatar, Sainbayar, Szlam, Arthur, Weston, Jason, Fergus, Rob (2015). "End-To-End Memory Networks." Advances in Neural Information Processing Systems (NeurIPS). https://arxiv.org/abs/1503.08895

## TL;DR
Introduces an end-to-end trainable memory network that performs multiple hops of soft attention over an external memory of stored facts, removing the strong supervision required by the original Memory Networks. Each hop computes a softmax attention distribution over memory slots and reads a weighted sum, an architecture that prefigures the multi-head attention of the Transformer.

## Relevance to this research
An early, influential demonstration of stacked soft-attention reads over an external memory — part of the attention/memory lineage feeding the GL(K) attention module and a concrete instance of memory-augmented networks.

## Cross-links
[[Attention mechanisms — theory and positional structure]], [[Memory-Augmented Networks]]

## BibTeX
```bibtex
@inproceedings{sukhbaatar2015end,
  author    = {Sukhbaatar, Sainbayar and Szlam, Arthur and Weston, Jason and Fergus, Rob},
  title     = {End-To-End Memory Networks},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2015},
  eprint    = {1503.08895},
  archivePrefix = {arXiv},
}
```
