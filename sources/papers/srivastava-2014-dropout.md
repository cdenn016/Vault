---
type: paper
title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
aliases:
  - "Srivastava et al. 2014 — Dropout"
  - "Dropout"
authors:
  - Nitish Srivastava
  - Geoffrey Hinton
  - Alex Krizhevsky
  - Ilya Sutskever
  - Ruslan Salakhutdinov
year: 2014
url: https://jmlr.org/papers/v15/srivastava14a.html
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
created: 2026-06-20
updated: 2026-06-20
---

# Dropout: A Simple Way to Prevent Neural Networks from Overfitting

> [!info] Citation
> Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). "Dropout: A Simple Way to Prevent Neural Networks from Overfitting." *Journal of Machine Learning Research*, 15(56), 1929-1958. <https://jmlr.org/papers/v15/srivastava14a.html>

## TL;DR

Dropout regularizes a neural network by randomly zeroing each unit with probability $1-p$ on every training step, so the network cannot rely on fixed co-adapted feature combinations. Training under this noise approximates sampling from an exponentially large ensemble of thinned subnetworks that share weights; at test time the full network with weights scaled by $p$ approximates averaging that ensemble. The technique reduced overfitting and set records on several supervised vision and speech benchmarks, and became a standard ingredient of the transformer block (residual and attention dropout).

## Relevance to this research

General deep-learning regularization context; the VFE transformer is a no-neural-network model (all capacity comes from iterative free-energy minimization over Gaussian belief tuples), so it does not use dropout as an architectural layer. The conventional-transformer baseline it is positioned against — Vaswani-style blocks ([[vaswani-2017-attention]]) — applies residual and attention dropout, and the ML-engineer debate lens cites this paper as the regularization furniture of that baseline. Its ensemble-averaging reading also offers a loose conceptual contrast with the project's belief-precision weighting under [[Transformer interpretability and scaling]], where confidence is represented explicitly in $\Sigma$ rather than injected as multiplicative noise.

## Cross-links

- Themes: [[Transformer interpretability and scaling]]
- Related sources: [[vaswani-2017-attention]], [[clark-2019-bert-attention]], [[dong-2021-rank-collapse]]
- Project: [[VFE Transformer Program]]

```bibtex
@article{srivastava2014dropout,
  title   = {Dropout: A Simple Way to Prevent Neural Networks from Overfitting},
  author  = {Srivastava, Nitish and Hinton, Geoffrey and Krizhevsky, Alex and
             Sutskever, Ilya and Salakhutdinov, Ruslan},
  journal = {Journal of Machine Learning Research},
  volume  = {15},
  number  = {56},
  pages   = {1929--1958},
  year    = {2014},
  url     = {https://jmlr.org/papers/v15/srivastava14a.html}
}
```
