---
type: reference
title: "Bayesian Attention Mechanism: A Probabilistic Framework for Positional Encoding and Context Length Extrapolation"
aliases:
  - "Bianchessi et al. 2026"
  - "Bayesian Attention Mechanism (BAM)"
  - "Bianchessi2026BAM"
authors:
  - Arthur S. Bianchessi
  - Yasmin C. Aguirre
  - Rodrigo C. Barros
  - Lucas S. Kupssinskü
year: 2026
arxiv: "2505.22842"
url: https://arxiv.org/abs/2505.22842
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-09-23
updated: 2026-09-23
---

# Bayesian Attention Mechanism: A Probabilistic Framework for Positional Encoding and Context Length Extrapolation

> [!info] Citation
> Arthur S. Bianchessi, Yasmin C. Aguirre, Rodrigo C. Barros, Lucas S. Kupssinskü (2026). "Bayesian Attention Mechanism: A Probabilistic Framework for Positional Encoding and Context Length Extrapolation." *International Conference on Learning Representations* (ICLR 2026). Preprint: [arXiv:2505.22842](https://arxiv.org/abs/2505.22842) (v1 May 2025; v4, 7 May 2026, read).

## TL;DR

BAM writes self-attention as an expectation of values under a joint distribution over the content and the relative position of the attended token. With additive scores, positional encodings become prior distributions over positions: the causal mask without positional encoding (NoPE) is a uniform prior and ALiBi is a Laplace prior. A generalized Gaussian prior (GGD-BAM) adds fewer than 1,000 parameters and supports passkey retrieval at up to 500 times the training context.

## What it establishes

Definition 1 (Section 2.1) writes attention as $\mathbb E_{j\mid i}[V]=\sum_jp_{ij}v_j$, and Definition 2 makes $p_{ij}$ a joint probability of the content of token $j$ and its position relative to $i$. Theorem 1 shows that an additive score $f_{\mathrm{cont}}(q_i,k_j)+g_{\mathrm{pos}}(i,j)$ makes $p_{ij}$ the product of content and position marginals up to a normalizing scalar, so an additive positional logit is the logarithm of a positional prior. The introduction states that "NoPE and ALiBi correspond explicitly to Uniform and Laplace positional priors, respectively," and Lemmas 1–3 make this precise: the causal mask is a uniform prior, ALiBi is a uniform prior times a Laplace prior over $|j-i|$, and ALiBi becomes local attention at large distances. Section 2.3 replaces the Laplace prior by a generalized Gaussian distribution. Theorems 2–4 show that GGD-BAM with a fractional exponent reaches further context than ALiBi and that a negative exponent, which the authors note is not a valid density parameter, suppresses local context and attends arbitrarily far. Section 3 evaluates long-context passkey retrieval and perplexity against sinusoidal, NoPE, RoPE, local RoPE, and ALiBi encodings, with and without scalable softmax.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript cites BAM as the precedent for its Section 2.6.1 positional priors, which enter the routing logits as $\log\pi_{ij}$. BAM's v1 predates [[litman-2026-attention-priors]], which does not cite it. See [[Attention mechanisms — theory and positional structure]], [[Relative positional encoding]], [[Length extrapolation]], and [[press2022-alibi]] for ALiBi itself.

## Local full text

The arXiv v4 PDF is stored at `sources/pdfs/Bianchessi2026BAM.pdf` ([local PDF](../pdfs/Bianchessi2026BAM.pdf)). Source: [arXiv:2505.22842](https://arxiv.org/pdf/2505.22842). SHA-256: `d2027ea3255305b170a292761eaff8573094519e6fe1f41f823c0535a64db80a`.

## BibTeX

```bibtex
@inproceedings{Bianchessi2026BAM,
  author = {Bianchessi, Arthur S. and Aguirre, Yasmin C. and Barros, Rodrigo C. and Kupssinsk{\"u}, Lucas S.},
  title = {Bayesian Attention Mechanism: A Probabilistic Framework for Positional Encoding and Context Length Extrapolation},
  booktitle = {International Conference on Learning Representations},
  year = {2026},
  eprint = {2505.22842},
  archivePrefix = {arXiv}
}
```
