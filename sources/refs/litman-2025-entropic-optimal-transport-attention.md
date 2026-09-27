---
type: reference
title: "Scaled-Dot-Product Attention as One-Sided Entropic Optimal Transport"
aliases:
  - "Litman 2025 attention as entropic optimal transport"
  - "Scaled-Dot-Product Attention as One-Sided Entropic Optimal Transport"
  - "Litman2025EOT"
authors:
  - Elon Litman
year: 2025
arxiv: "2508.08369"
url: https://arxiv.org/abs/2508.08369
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/mathematics
created: 2026-09-23
updated: 2026-09-23
---

# Scaled-Dot-Product Attention as One-Sided Entropic Optimal Transport

> [!info] Citation
> Elon Litman (2025). "Scaled-Dot-Product Attention as One-Sided Entropic Optimal Transport." arXiv preprint [arXiv:2508.08369](https://arxiv.org/abs/2508.08369) (v2, December 2025, read).

## TL;DR

The attention weight vector of scaled dot-product attention is the unique minimizer of a "one-sided" entropic optimal transport problem: expected cost (negative query–key similarity) minus a temperature-weighted Shannon entropy over the simplex, with no target-marginal constraint. The paper also shows that backpropagation through attention has the form of an advantage-based policy gradient, which it relates to the Fisher geometry of the attention distribution.

## What it establishes

Definition 3.2 poses the problem $p^\star=\arg\min_{p\in\Delta^{m-1}}\sum_jp_jC_j-\varepsilon H(p)$ with cost $C_j=-\langle q,k_j\rangle$ (Eqs. 3–6), and Theorem 3.3 proves that when $\varepsilon$ equals the attention temperature $\tau$ the unique solution is the scaled dot-product attention vector. The author notes that "one-sided" is not standard terminology and refers to the absence of a target-marginal constraint. Section 4 varies the regularizer: Shannon entropy gives softmax (Proposition 4.1), a squared $L_2$ penalty gives sparsemax (Proposition 4.2), Tsallis entropy gives $\alpha$-entmax (Proposition 4.3), and adding a linear penalty on attention distance $|i-j|$ gives ALiBi (Proposition 4.4). Section 5 (Theorem 5.2) shows that the gradient computed by backpropagation equals an advantage-based policy-gradient update and interprets its form through the Fisher information matrix of the attention distribution.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript cites this paper, with [[niculae-2017-regularized-attention]] and [[litman-2026-attention-priors]], for the derivation of scaled dot-product attention as an entropy-regularized row optimization. The manuscript's Section 2.6 row objective has the same form with a KL divergence to a prior in place of the entropy. Proposition 4.4 is also a precedent for reading positional biases such as ALiBi as regularizers of the row problem. See [[Softmax]], [[Entropic regularization]], and [[Optimal transport]].

> [!note] Editorial: Without a target marginal the problem has no coupling to solve for, so its solution is the Gibbs distribution of an entropy-regularized linear objective rather than a Sinkhorn transport plan. The optimal-transport vocabulary is therefore a framing, and the underlying identity is the Gibbs variational principle.

## Local full text

The arXiv v2 PDF is stored at `sources/pdfs/Litman2025EOT.pdf` ([local PDF](../pdfs/Litman2025EOT.pdf)). Source: [arXiv:2508.08369](https://arxiv.org/pdf/2508.08369). SHA-256: `1a383c7b50a982bd53ed04f6d8ca077d049ec92b36482ea9946e30b9db547607`.

## BibTeX

```bibtex
@misc{Litman2025EOT,
  author = {Litman, Elon},
  title = {Scaled-Dot-Product Attention as One-Sided Entropic Optimal Transport},
  year = {2025},
  howpublished = {arXiv preprint arXiv:2508.08369},
  eprint = {2508.08369},
  archivePrefix = {arXiv}
}
```
