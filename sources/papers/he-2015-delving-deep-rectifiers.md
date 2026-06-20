---
type: paper
title: "Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification"
aliases:
  - "He et al. 2015 — Delving Deep into Rectifiers"
  - "He initialization"
  - "PReLU"
authors:
  - He K.
  - Zhang X.
  - Ren S.
  - Sun J.
year: 2015
arxiv: "1502.01852"
url: https://arxiv.org/abs/1502.01852
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
created: 2026-06-20
updated: 2026-06-20
---

# Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification

> [!info] Citation
> He, K., Zhang, X., Ren, S., and Sun, J. (2015). "Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification." Proceedings of the IEEE International Conference on Computer Vision (ICCV), pp. 1026–1034. arXiv:1502.01852. <https://arxiv.org/abs/1502.01852>

## TL;DR

This paper introduces two contributions for training very deep rectifier networks: the **Parametric ReLU (PReLU)** activation, which learns the negative-slope coefficient of the rectifier rather than fixing it at zero, and a variance-preserving weight initialization — now called **He (or Kaiming) initialization** — derived specifically for ReLU-family nonlinearities. The initialization keeps the per-layer activation variance stable through depth by drawing weights with variance $2/n_{\text{in}}$ (where $n_{\text{in}}$ is the fan-in), correcting the factor-of-two that the symmetric-activation Xavier/Glorot derivation misses for rectifiers. With these, the authors were the first to report super-human top-5 error on ImageNet classification.

## Relevance to this research

General deep-learning-training context. The VFE transformer is a no-neural-network model — all capacity comes from iterative VFE minimization over Gaussian belief tuples $(\mu, \Sigma, \phi)$, with no `nn.Linear`, no MLP, and no activations — so He initialization and PReLU are not used on any path. The ML-engineer debate lens cites it as the canonical reference for the rectifier-network initialization lineage (alongside Glorot–Bengio Xavier init) when contrasting conventional weight-variance bookkeeping against the project's variance handling, which lives in the SPD covariance $\Sigma$ and precision-weighting rather than in initialized weight matrices.

## Cross-links

- Concepts: [[Mechanistic interpretability of attention]]
- Theme: [[Transformer interpretability and scaling]]
- Sources: [[vaswani-2017-attention]], [[amari-1998-natural-gradient]]
- Project: [[VFE Transformer Program]]

```bibtex
@inproceedings{he2015delving,
  title     = {Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification},
  author    = {He, Kaiming and Zhang, Xiangyu and Ren, Shaoqing and Sun, Jian},
  booktitle = {Proceedings of the IEEE International Conference on Computer Vision (ICCV)},
  pages     = {1026--1034},
  year      = {2015},
  eprint    = {1502.01852},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV},
  url       = {https://arxiv.org/abs/1502.01852}
}
```
