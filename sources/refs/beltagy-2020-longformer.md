---
type: reference
title: "Longformer: The Long-Document Transformer"
aliases:
  - "Beltagy et al. 2020"
  - "Longformer"
authors:
  - Iz Beltagy
  - Matthew E. Peters
  - Arman Cohan
year: 2020
arxiv: "2004.05150"
url: https://arxiv.org/abs/2004.05150
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# Longformer: The Long-Document Transformer

> [!info] Citation
> Iz Beltagy, Matthew E. Peters, and Arman Cohan (2020). "Longformer: The Long-Document Transformer." arXiv:2004.05150. <https://arxiv.org/abs/2004.05150>

## TL;DR

Longformer replaces dense $O(n^2)$ self-attention with a **sparse attention pattern** — a sliding local window plus a few global tokens — making attention scale linearly in sequence length and enabling long-document processing.

## Relevance to this research

Cited by PIFB ([[participatory-it-from-bit]]) as long-context architecture furniture: a representative efficient-attention scheme. Its local-window-plus-global pattern is a hard, hand-designed version of the distance-decaying coupling prior that PIFB derives softly (the entropy-regularized consensus prior behind ALiBi, [[press-2021-alibi]]) — a sparse special case of the project's belief-coupling structure under [[Attention mechanisms — theory and positional structure]].

```bibtex
@article{beltagy2020longformer,
  title         = {Longformer: The Long-Document Transformer},
  author        = {Beltagy, Iz and Peters, Matthew E. and Cohan, Arman},
  journal       = {arXiv preprint arXiv:2004.05150},
  year          = {2020},
  eprint        = {2004.05150},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2004.05150}
}
```
