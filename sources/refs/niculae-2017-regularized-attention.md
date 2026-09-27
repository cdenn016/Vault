---
type: reference
title: "A Regularized Framework for Sparse and Structured Neural Attention"
aliases:
  - "Niculae and Blondel 2017"
  - "A Regularized Framework for Sparse and Structured Neural Attention"
  - "Niculae2017Regularized"
authors:
  - Vlad Niculae
  - Mathieu Blondel
year: 2017
arxiv: "1705.07704"
url: https://arxiv.org/abs/1705.07704
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/mathematics
created: 2026-09-23
updated: 2026-09-23
---

# A Regularized Framework for Sparse and Structured Neural Attention

> [!info] Citation
> Vlad Niculae and Mathieu Blondel (2017). "A Regularized Framework for Sparse and Structured Neural Attention." *Advances in Neural Information Processing Systems* **30** (NeurIPS 2017). Preprint: [arXiv:1705.07704](https://arxiv.org/abs/1705.07704) (v3 read, which corrects an error in Proposition 2 of the conference version).

## TL;DR

Attention mappings are obtained as gradients of a regularized max operator over the probability simplex. A strongly convex regularizer gives a smooth max whose gradient maps scores to probabilities. Negative entropy yields softmax, a squared norm yields sparsemax, and structured penalties yield new sparse, segment-aware mechanisms (fusedmax and oscarmax).

## What it establishes

Section 2.2 defines the regularized max operator $\max_\Omega(x)=\sup_{y\in\Delta^d}\big(y^\top x-\gamma\Omega(y)\big)$ for a strongly convex $\Omega$ (Eq. 1), and its gradient $\Pi_\Omega(x)=\arg\max_{y\in\Delta^d}\big(y^\top x-\gamma\Omega(y)\big)$ is the attention mapping. Strong convexity of $\Omega$ makes $\max_\Omega$ smooth and $\Pi_\Omega$ Lipschitz. Section 2.3 recovers softmax, $\Pi_\Omega(x)=e^{x/\gamma}/\sum_ie^{x_i/\gamma}$, from the negative entropy, and a slight generalization of sparsemax, the Euclidean projection of $x/\gamma$ onto the simplex, from $\Omega(y)=\tfrac12\lVert y\rVert_2^2$. Section 3 gives forward and backward (Jacobian) computations for general and structured regularizers and introduces fusedmax (fused lasso) and oscarmax (OSCAR). Section 4 evaluates them as drop-in attention on textual entailment, machine translation, and sentence summarization. The arXiv errata note that the composition used for oscarmax in Proposition 2 is only an approximation in general.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript cites this framework as the attention-specific precedent for its entropy-regularized Gibbs routing: the softmax row is the maximizer of a linear score plus an entropy term, and the temperature is the regularization weight $\gamma$. The manuscript's Section 2.6 row objective replaces the entropy by a KL divergence to a prior, the form written out for attention in [[litman-2026-attention-priors]]. See [[Softmax]], [[Entropic regularization]], and [[Attention mechanisms — theory and positional structure]].

## Local full text

The arXiv v3 PDF is stored at `sources/pdfs/Niculae2017Regularized.pdf` ([local PDF](../pdfs/Niculae2017Regularized.pdf)). Source: [arXiv:1705.07704](https://arxiv.org/pdf/1705.07704). SHA-256: `00a13345354af12c313dd49b0372f361198fa1402e6552b823a818574f5b50b5`.

## BibTeX

```bibtex
@inproceedings{Niculae2017Regularized,
  author = {Niculae, Vlad and Blondel, Mathieu},
  title = {A Regularized Framework for Sparse and Structured Neural Attention},
  booktitle = {Advances in Neural Information Processing Systems},
  volume = {30},
  year = {2017},
  eprint = {1705.07704},
  archivePrefix = {arXiv}
}
```
