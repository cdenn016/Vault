---
type: paper
title: "Pointer Networks"
aliases:
  - "vinyals2015-pointer-networks"
  - "Vinyals 2015"
  - "Pointer Networks"
  - "vinyals2015pointernetworks"
authors:
  - "Vinyals, Oriol"
  - "Fortunato, Meire"
  - "Jaitly, Navdeep"
year: 2015
url: https://arxiv.org/abs/1506.03134
venue: "Advances in Neural Information Processing Systems (NeurIPS) 28"
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Pointer Networks

> [!info] Citation
> Vinyals, Oriol, Fortunato, Meire, Jaitly, Navdeep (2015). "Pointer Networks." Advances in Neural Information Processing Systems (NeurIPS) 28. https://arxiv.org/abs/1506.03134

## TL;DR
Pointer Networks introduce a sequence-to-sequence architecture whose output is a distribution over positions in the input sequence, realized by using attention as a pointer rather than to blend a context vector. This solves combinatorial problems (convex hulls, Delaunay triangulation, TSP) where the output dictionary size varies with the input length, and it underlies copy/pointer mechanisms in later language models.

## Relevance to this research
The pointer/attention-as-selection mechanism is the precursor to the pointer-sentinel copy mechanism and is conceptually adjacent to the GL(K) attention program's treatment of attention as a structured selection/transport operator over tokens.

## Cross-links
[[Attention mechanisms — theory and positional structure]]

## BibTeX
```bibtex
@inproceedings{vinyals2015pointernetworks,
  author    = {Vinyals, Oriol and Fortunato, Meire and Jaitly, Navdeep},
  title     = {Pointer Networks},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  volume    = {28},
  year      = {2015},
  eprint    = {1506.03134},
  archivePrefix = {arXiv}
}
```
