---
type: paper
title: "Learning Fast Approximations of Sparse Coding"
aliases:
  - Gregor 2010
  - gregor2010learning
  - Learned ISTA
authors:
  - Gregor, Karol
  - LeCun, Yann
year: 2010
url: https://icml.cc/Conferences/2010/papers/449.pdf
pdf: sources/pdfs/gregor-2010-lista.pdf
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
created: 2026-10-24
---

# Learning Fast Approximations of Sparse Coding

> [!info] Citation
> Gregor, K., & LeCun, Y. (2010). *Learning fast approximations of sparse coding*. Proceedings of the 27th International Conference on Machine Learning (ICML 2010), pp. 399–406. PDF from the author's site.

## TL;DR
Sparse coding infers a code by minimizing a quadratic reconstruction error plus an $L_1$ penalty, usually with the iterative shrinkage-thresholding algorithm (ISTA). Learned ISTA (LISTA) unrolls a fixed small number of ISTA steps into a feed-forward network with a coordinate-wise shrinkage nonlinearity and trains its matrices to approximate the optimal code; a learned coordinate-descent variant reaches the same approximation error as Li and Osher's method with ten times less computation.

## Method
One ISTA step is $z\leftarrow h_\alpha(W_ex+Sz)$ with $W_e$ derived from the dictionary, $S=I-W_d^\top W_d/L$, and $h_\alpha$ a soft threshold (Figure 1, Algorithm 1). LISTA keeps this block diagram, truncates it to a few steps, and learns $W_e$ and $S$ by backpropagation. The mutual-inhibition matrix $S$ implements an approximate "explaining away" between code units.

## Relevance to this research
One ISTA step from zero is a one-hidden-layer network whose activation is the proximal map of the prior, with input weights tied to the dictionary: an MLP read as one step of MAP inference in a factorial sparse linear-Gaussian model. This is the factorial, many-units-active counterpart of the one-of-$M$ mixture reading of the prototype block MLP, and the one-sweep mean-field version replaces the threshold by a posterior-mean activation, which is always monotone. CRATE ([[yu-2023-white-box-transformers-sparse-rate-reduction]]) uses the same step as its MLP ([[Template routing]]).

## Cross-links
- Methods: [[Template routing]]
- Concepts: [[Associative Memory]]
- Related sources: [[yu-2023-white-box-transformers-sparse-rate-reduction]], [[hendrycks2016gaussian]], [[geva-2021-ffn-key-value-memories]]

## BibTeX
```bibtex
@inproceedings{gregor2010learning,
  author    = {Gregor, Karol and LeCun, Yann},
  title     = {Learning Fast Approximations of Sparse Coding},
  booktitle = {Proceedings of the 27th International Conference on Machine Learning},
  pages     = {399--406},
  year      = {2010}
}
```
