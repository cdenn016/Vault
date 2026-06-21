---
type: paper
title: "Dense Associative Memory for Pattern Recognition"
aliases:
  - "krotov2016dense"
  - "Krotov 2016"
  - "Dense Associative Memory"
authors:
  - "Krotov, Dmitry"
  - "Hopfield, John J."
year: 2016
url: https://arxiv.org/abs/1606.01164
venue: "Advances in Neural Information Processing Systems (NeurIPS)"
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/physics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Dense Associative Memory for Pattern Recognition

> [!info] Citation
> Krotov, Dmitry, Hopfield, John J. (2016). "Dense Associative Memory for Pattern Recognition." Advances in Neural Information Processing Systems (NeurIPS). https://arxiv.org/abs/1606.01164

## TL;DR
Introduces dense associative memory (DAM), generalizing classical Hopfield networks with higher-order polynomial interaction (energy) functions F(x)=x^n that raise storage capacity from O(d/log d) to O(d^{n-1}) patterns. Establishes a duality between these memory models and feedforward neural networks with polynomial/rectified activations, and shows strong robustness to adversarial inputs.

## Relevance to this research
Direct precursor to modern Hopfield networks: the higher-capacity energy functions here lead to the exponential-capacity, attention-equivalent update used in the VFE program's associative-memory reading of attention. Cited from the Hopfield note.

## Cross-links
[[Associative Memory]], [[Energy-Based Models]], [[Attention Mechanism]]

## BibTeX
```bibtex
@inproceedings{krotov2016dense,
  author    = {Krotov, Dmitry and Hopfield, John J.},
  title     = {Dense Associative Memory for Pattern Recognition},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2016},
  url       = {https://arxiv.org/abs/1606.01164}
}
```
