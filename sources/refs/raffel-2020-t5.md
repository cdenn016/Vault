---
type: reference
title: "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5)"
aliases:
  - "Raffel et al. 2020"
  - "T5"
  - "raffel2020t5"
authors:
  - Colin Raffel
  - Noam Shazeer
  - Adam Roberts
  - Katherine Lee
  - Sharan Narang
  - Michael Matena
  - Yanqi Zhou
  - Wei Li
  - Peter J. Liu
year: 2020
arxiv: "1910.10683"
url: https://arxiv.org/abs/1910.10683
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5)

> [!info] Citation
> Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu (2020). "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer." *Journal of Machine Learning Research* 21(140): 1–67. arXiv:1910.10683. <https://arxiv.org/abs/1910.10683>

## TL;DR

T5 casts every NLP task as text-to-text and conducts a large systematic study of transfer-learning choices for an encoder-decoder transformer. Of lasting architectural note for this project, it uses **relative positional encodings via learned bias buckets** added to attention logits.

## Relevance to this research

Cited by PIFB ([[participatory-it-from-bit]]) as architecture furniture, and specifically for its **relative-position bucket biases** — a learned, distance-binned additive bias on attention scores. This is one of the concrete positional schemes the project composes and reinterprets: like ALiBi ([[press-2021-alibi]]) it is an additive log-prior over relative position, organized under [[Attention mechanisms — theory and positional structure]] alongside the multiplicative gauge-frame reading of RoPE ([[su-2021-roformer-rope]]). The transformer codebase's positional handling composes learned $\phi$, RoPE, ALiBi, and T5-style relative buckets.

```bibtex
@article{raffel2020exploring,
  title   = {Exploring the Limits of Transfer Learning with a Unified
             Text-to-Text Transformer},
  author  = {Raffel, Colin and Shazeer, Noam and Roberts, Adam and Lee, Katherine and
             Narang, Sharan and Matena, Michael and Zhou, Yanqi and Li, Wei and
             Liu, Peter J.},
  journal = {Journal of Machine Learning Research},
  volume  = {21},
  number  = {140},
  pages   = {1--67},
  year    = {2020},
  eprint        = {1910.10683},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url     = {https://arxiv.org/abs/1910.10683}
}
```
