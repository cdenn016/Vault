---
type: paper
title: "Self-Attention with Relative Position Representations"
aliases:
  - "shaw2018self"
  - "shaw-2018-self-attention-relative-position"
  - "Self-Attention with Relative Position Representations"
authors:
  - "Shaw, P."
  - "Uszkoreit, J."
  - "Vaswani, A."
year: 2018
url: https://arxiv.org/abs/1803.02155
venue: "NAACL-HLT 2018"
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Self-Attention with Relative Position Representations

> [!info] Citation
> Shaw, P., Uszkoreit, J., Vaswani, A. (2018). "Self-Attention with Relative Position Representations." NAACL-HLT 2018. https://arxiv.org/abs/1803.02155

## TL;DR
Extends the Transformer's self-attention to incorporate learned representations of relative positions (clipped pairwise distances) added into the key and value projections, replacing reliance on absolute sinusoidal position embeddings. Improves machine-translation quality and motivates the now-standard family of relative positional schemes.

## Relevance to this research
Seminal source for relative positional encoding in transformers, directly relevant to the program's analysis of how positional structure shapes attention geometry and length generalization.

## Cross-links
[[Relative positional encoding|Relative Position Encoding]], [[kazemnejad-2023-positional-encoding-length-generalization|Positional encoding and length generalization]], [[Attention mechanisms — theory and positional structure]]

## BibTeX
```bibtex
@inproceedings{shaw2018self,
  title={Self-Attention with Relative Position Representations},
  author={Shaw, Peter and Uszkoreit, Jakob and Vaswani, Ashish},
  booktitle={Proceedings of NAACL-HLT 2018},
  pages={464--468},
  year={2018},
  doi={10.18653/v1/N18-2074}
}
```
