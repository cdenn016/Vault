---
type: reference
title: "You Need Better Attention Priors"
aliases:
  - "Litman and Guo 2026"
  - "You Need Better Attention Priors"
  - "GOAT attention prior"
  - "Litman2026AttentionPriors"
authors:
  - Elon Litman
  - Gabe Guo
year: 2026
arxiv: "2601.15380"
url: https://arxiv.org/abs/2601.15380
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
created: 2026-09-23
updated: 2026-09-23
---

# You Need Better Attention Priors

> [!info] Citation
> Elon Litman and Gabe Guo (2026). "You Need Better Attention Priors." arXiv preprint [arXiv:2601.15380](https://arxiv.org/abs/2601.15380) (v2, 23 August 2026, read). Code: `github.com/elonlit/goat`.

## TL;DR

Standard attention is read as an entropic optimal-transport row problem with an implicit uniform prior. Replacing the entropy by a KL divergence to a prior $\pi$ gives $\operatorname{softmax}(s/\tau+\log\pi)$. The paper then learns that prior (GOAT: a Fourier series in $i-j$ plus a key-only bias), realizes it inside unmodified FlashAttention calls, and explains attention sinks as collapse of the row to its prior when content signal is weak.

## What it establishes

Proposition 3.1 minimizes $-\langle p,s\rangle+\tau\mathrm{KL}(p\Vert\pi)$ over the simplex and obtains $p^\star_j=\operatorname{softmax}_j(s_j/\tau+\log\pi_j)$ (Eqs. 4–5); a uniform $\pi$ returns standard attention. Section 4 parameterizes the unnormalized log-prior as $K_{ij}=K^{\mathrm{rel}}_{ij}+u(j)$. The relative part is a truncated Fourier series $K^{\mathrm{rel}}_{ij}=\sum_{r=1}^R[\alpha_r\cos\omega_r(i-j)+\beta_r\sin\omega_r(i-j)]$ with learnable $\alpha_r,\beta_r$ and fixed geometric frequencies $\omega_r=B^{-(r-1)/\max(R-1,1)}$, $B=10^4$ (Eqs. 12–13). The key-only part is $u_h(j)=\lambda_hj+g_h(\phi_{\mathrm{abs}}(j))+b_h\mathbf 1\{j=0\}$, a learned slope, a small absolute-position MLP, and a first-token bump (Eq. 21). Both parts are written as inner products of reserved positional query and key coordinates, so the prior enters one standard SDPA or FlashAttention call (Algorithm 1). The authors state that this additive prior "is isomorphic to an additive positional encoding" and argue for the parameterization on grounds of disentanglement. Theorem 5.1 bounds the row by its prior, $\pi_{ij}e^{-\omega_i}\le p_{ij}\le\pi_{ij}e^{\omega_i}$ with $\omega_i$ the dynamic range of the content scores, so the row collapses to the prior as $\omega_i\to0$; this is their account of attention sinks. Section 6 reports 125M-parameter C4 language models (1.55 perplexity points below ALiBi in distribution, with extrapolation where RoPE degrades), matched 1.23B-parameter FineWeb models (GOAT matches RoPE at the training length and extrapolates better), long-context retrieval, ImageNet vision transformers, and DNA modeling.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript cites this paper in Section 2.6.1 as concurrent work. Proposition 3.1 is the same identity as the manuscript's Section 2.6 row objective. GOAT is a learned relative-plus-key-only prior realized inside FlashAttention, and the paper reads attention sinks as collapse of the row to its prior (Theorem 5.1). The revision also places the relative prior in the function class of term (d) of [[dai2019transformerxl]]. See [[Attention mechanisms — theory and positional structure]], [[Relative positional encoding]], and [[Length extrapolation]].

> [!note] Editorial: The term (d) comparison checks directly. Term (d) of Transformer-XL (Section 3.3), $v^\top W_{k,R}R_{i-j}$, which that paper calls a "global positional bias", is a learned linear combination of $\cos\omega_r(i-j)$ and $\sin\omega_r(i-j)$ because $R_{i-j}$ is a fixed sinusoid encoding, which is the form of $K^{\mathrm{rel}}_{ij}$. The identity of Proposition 3.1 is the Gibbs variational principle. Entropy-regularized or prior-shifted versions of it appear for attention in [[niculae-2017-regularized-attention]], in [[litman-2025-entropic-optimal-transport-attention]] (Proposition 4.4), and in the positional-prior reading of [[bianchessi-2026-bayesian-attention-mechanism]], whose v1 dates from May 2025.

## Local full text

The arXiv v2 PDF is stored at `sources/pdfs/Litman2026AttentionPriors.pdf` ([local PDF](../pdfs/Litman2026AttentionPriors.pdf)). Source: [arXiv:2601.15380v2](https://arxiv.org/pdf/2601.15380v2). SHA-256: `0800b53962c955653efe8af1c88fcdcb1ffedc6754a49a5f9e4b9977bfc051b9`.

## BibTeX

```bibtex
@misc{Litman2026AttentionPriors,
  author = {Litman, Elon and Guo, Gabe},
  title = {You Need Better Attention Priors},
  year = {2026},
  howpublished = {arXiv preprint arXiv:2601.15380},
  eprint = {2601.15380},
  archivePrefix = {arXiv}
}
```
