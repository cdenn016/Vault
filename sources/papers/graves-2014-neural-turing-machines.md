---
type: paper
title: "Neural Turing Machines"
aliases:
  - "graves2014neural"
  - "Graves 2014"
  - "Neural Turing Machines"
  - "Neural Turing Machine"
authors:
  - "Graves, Alex"
  - "Wayne, Greg"
  - "Danihelka, Ivo"
year: 2014
url: https://arxiv.org/abs/1410.5401
venue: "arXiv preprint"
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Neural Turing Machines

> [!info] Citation
> Graves, Alex, Wayne, Greg, Danihelka, Ivo (2014). "Neural Turing Machines." arXiv preprint. https://arxiv.org/abs/1410.5401

## TL;DR
Proposes the Neural Turing Machine, a neural controller coupled to an external memory matrix through differentiable read/write heads that use content- and location-based addressing. By making memory access fully differentiable, the model can be trained end-to-end by gradient descent and learns simple algorithmic tasks (copy, sort, associative recall).

## Relevance to this research
The foundational memory-augmented architecture: its differentiable content-based addressing is an early form of attention-as-memory-read, ancestral to the attention routing in the VFE transformer and a canonical instance of memory-augmented networks.

## Cross-links
[[Attention mechanisms — theory and positional structure]], [[Memory-Augmented Networks]]

## BibTeX
```bibtex
@article{graves2014neural,
  author  = {Graves, Alex and Wayne, Greg and Danihelka, Ivo},
  title   = {Neural Turing Machines},
  journal = {arXiv preprint arXiv:1410.5401},
  year    = {2014},
  eprint  = {1410.5401},
  archivePrefix = {arXiv},
  url     = {https://arxiv.org/abs/1410.5401},
}
```
