---
type: reference
title: "Algorithmic Regularization in Learning Deep Homogeneous Models: Layers are Automatically Balanced"
aliases:
  - "Du, Hu and Lee 2018"
  - "Algorithmic Regularization in Learning Deep Homogeneous Models: Layers are Automatically Balanced"
  - "du2018balanced"
authors:
  - Simon S. Du
  - Wei Hu
  - Jason D. Lee
year: 2018
arxiv: "1806.00900"
url: https://arxiv.org/abs/1806.00900
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/mathematics
created: 2026-09-23
updated: 2026-09-23
---

# Algorithmic Regularization in Learning Deep Homogeneous Models: Layers are Automatically Balanced

> [!info] Citation
> Simon S. Du, Wei Hu, Jason D. Lee (2018). "Algorithmic Regularization in Learning Deep Homogeneous Models: Layers are Automatically Balanced." *Advances in Neural Information Processing Systems* **31** (NeurIPS 2018). Preprint: [arXiv:1806.00900](https://arxiv.org/abs/1806.00900) (v2 read).

## TL;DR

For networks with homogeneous activations (linear, ReLU, leaky ReLU), gradient flow exactly preserves the differences between the squared norms of consecutive layers, so layers initialized with small, nearly equal norms stay balanced without explicit regularization. Between two linear layers the invariant is a matrix identity. A discretization argument extends approximate balance to gradient descent with positive step size on asymmetric low-rank matrix factorization.

## What it establishes

Section 2 treats fully connected networks with homogeneous activations. Theorem 2.1 shows that gradient flow preserves, at every hidden neuron, the difference between the squared norms of its incoming and outgoing weights. Summing over neurons, Corollary 2.1 shows that $\lVert W^{(h)}\rVert_F^2-\lVert W^{(h+1)}\rVert_F^2$ is invariant over time. Theorem 2.2 strengthens this when no nonlinearity separates two consecutive layers: $W^{(h)}W^{(h)\top}-W^{(h+1)\top}W^{(h+1)}$ is invariant, which needs only those two layers to be linear. The results extend to convolutional layers and to arbitrary sparsity and weight-sharing patterns. Section 3 proves that gradient descent with positive step size approximately preserves the invariance for asymmetric matrix factorization and, with random initialization, converges to a global minimum without regularization.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript cites this paper, with [[kunin-2021-neural-mechanics]], for layer-balance conservation under gradient flow. The sending and receiving content maps enter only through the product $O_hT_h$, which is unchanged under $T_h\mapsto AT_h$, $O_h\mapsto O_hA^{-1}$. This is the two-linear-layer setting of Theorem 2.2 with $W^{(h)}=T_h$ and $W^{(h+1)}=O_h$, so gradient flow would conserve $T_hT_h^\top-O_h^\top O_h$. The individual maps are defined only up to this redundancy, so their raw spectra depend on the basis, and the reported run used AdamW ([[loshchilov-hutter-2019-adamw]]), which does not follow gradient flow. See [[Natural gradient]] and [[GL(K) gauge-equivariant attention]].

## Local full text

The arXiv v2 PDF is stored at `sources/pdfs/du2018balanced.pdf` ([local PDF](../pdfs/du2018balanced.pdf)). Source: [arXiv:1806.00900](https://arxiv.org/pdf/1806.00900). SHA-256: `dbc8fdd73cd0fb99ea4ee7f5ef0a4265e25bdb03a7a173577ecceabdc0185ce0`.

## BibTeX

```bibtex
@inproceedings{du2018balanced,
  author    = {Du, Simon S. and Hu, Wei and Lee, Jason D.},
  title     = {Algorithmic Regularization in Learning Deep Homogeneous Models: Layers are Automatically Balanced},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {31},
  year      = {2018}
}
```
