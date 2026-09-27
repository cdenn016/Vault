---
type: paper
title: "Transformer Feed-Forward Layers Are Key-Value Memories"
aliases:
  - Geva 2021
  - geva2021
  - FFN key-value memories
authors:
  - Geva, Mor
  - Schuster, Roei
  - Berant, Jonathan
  - Levy, Omer
year: 2021
arxiv: "2012.14913"
url: https://aclanthology.org/2021.emnlp-main.446/
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
created: 2026-09-27
---

# Transformer Feed-Forward Layers Are Key-Value Memories

> [!info] Citation
> Geva, M., Schuster, R., Berant, J., & Levy, O. (2021). *Transformer Feed-Forward Layers Are Key-Value Memories*. Proceedings of EMNLP 2021, pp. 5484–5495. doi:10.18653/v1/2021.emnlp-main.446.

## TL;DR
Each hidden unit of a transformer feed-forward layer acts as a key that detects a textual pattern in the input and a value that induces a distribution over output tokens. Lower layers key on shallow surface patterns and upper layers on semantic ones; the layer output is a composition of many such memories, refined across layers through the residual stream.

## Problem & setting
Feed-forward layers hold about two thirds of a transformer's parameters but were far less studied than attention.

## Method
Write the layer as $\mathrm{FF}(x)=f(x K^\top)V$: rows of $K$ are keys, rows of $V$ are values, and $f$ is the activation. The authors collect the training prefixes that most strongly activate each key, annotate the patterns they share, and project values through the output embedding to read off the token distributions they promote.

## Key results
Keys correlate with human-interpretable input patterns; values' output distributions tend to predict the next token of the prefixes their keys detect, more strongly in upper layers; each layer's output combines many memories and is then refined by the residual.

## Relevance to this research
This paper supplies the interpretive vocabulary ("key–value memory") behind [[Template routing]]. In the template construction the keys become Gaussian templates $(\nu_a,\Lambda_a)$ compared to a token belief by KL, the values are the template outputs $w_a$, and the activation $f$ is replaced by a softmax derived from a mixture prior. The finding that values predict what follows the keyed pattern is the empirical counterpart of the untied-value, Gaussian-mixture-regression reading in [[dennis-2026-template-routing]].

## Cross-links
- Concepts: [[Associative Memory]], [[Activation Functions]], [[Mechanistic interpretability of attention]]
- Methods: [[Template routing]]
- Related sources: [[sukhbaatar-2019-persistent-memory]], [[ramsauer2021hopfield]], [[dennis-2026-template-routing]]

## BibTeX
```bibtex
@inproceedings{geva2021transformer,
  author    = {Geva, Mor and Schuster, Roei and Berant, Jonathan and Levy, Omer},
  title     = {Transformer Feed-Forward Layers Are Key-Value Memories},
  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
  pages     = {5484--5495},
  year      = {2021},
  doi       = {10.18653/v1/2021.emnlp-main.446}
}
```
