---
type: reference
title: "The Lipschitz Constant of Self-Attention"
aliases:
  - "Kim, Papamakarios and Mnih 2021"
  - "The Lipschitz Constant of Self-Attention"
  - "Kim2021Lipschitz"
authors:
  - Hyunjik Kim
  - George Papamakarios
  - Andriy Mnih
year: 2021
arxiv: "2006.04710"
url: https://arxiv.org/abs/2006.04710
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/mathematics
created: 2026-09-23
updated: 2026-09-23
---

# The Lipschitz Constant of Self-Attention

> [!info] Citation
> Hyunjik Kim, George Papamakarios, Andriy Mnih (2021). "The Lipschitz Constant of Self-Attention." *Proceedings of the 38th International Conference on Machine Learning*, PMLR **139**, 5562–5571. Preprint: [arXiv:2006.04710](https://arxiv.org/abs/2006.04710) (v2 read).

## TL;DR

Dot-product multi-head self-attention is not Lipschitz on an unbounded input domain. The paper introduces L2 self-attention, whose logits are negative squared Euclidean distances between projected queries and keys. With tied query and key projections it is Lipschitz, with an explicit bound, and it can be used to build invertible self-attention.

## What it establishes

Theorem 3.1 proves that dot-product multi-head attention is not Lipschitz for any $p$-norm with $p\in[1,\infty]$, because some Jacobian entries grow without bound. Section 3.2 defines L2 self-attention by
$$P_{ij}\propto\exp\left(-\frac{\lVert x_iW^Q-x_jW^K\rVert_2^2}{\sqrt{D/H}}\right)$$
with softmax normalization over $j$ (Eq. 8), which the authors liken to a squared-exponential kernel with row normalization. The multi-head map (L2-MHA) requires $W^{Q,h}=W^{K,h}$ in each head; Lemma F.1 shows that L2-MHA is not Lipschitz for arbitrary untied projections and that tying suffices. Theorem 3.2 bounds $\mathrm{Lip}_p(F)$ for $p=2,\infty$. Section 4 uses the bound to build invertible (contractive) self-attention, and Section 5 checks the asymptotic tightness of the bound, the numerical invertibility of the residual map, and character-level language modeling on the Penn Treebank.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript identifies the isotropic case of its Section 4 shared-covariance reduction with L2 self-attention. L2 attention, not dot-product attention, is therefore the natural transformer limit of Gaussian-KL routing. See [[GL(K) gauge-equivariant attention]], [[Attention mechanisms — theory and positional structure]], and [[nguyen-2022-probabilistic-attention-keys]], whose Gaussian-kernel keys give a score of the same kind.

> [!note] Editorial: For equal isotropic covariances, $D_{\mathrm{KL}}\big(\mathcal N(a,\sigma^2I)\Vert\mathcal N(b,\sigma^2I)\big)=\lVert a-b\rVert^2/(2\sigma^2)$, so the Gaussian-KL logit is an L2 logit up to scale. The correspondence concerns the score function. Kim et al.'s Lipschitz theorem additionally needs tied query and key projections, a constraint that the manuscript's independent comparison maps $S_Q,S_K$ do not satisfy in general.

## Local full text

The arXiv v2 PDF is stored at `sources/pdfs/Kim2021Lipschitz.pdf` ([local PDF](../pdfs/Kim2021Lipschitz.pdf)). Source: [arXiv:2006.04710](https://arxiv.org/pdf/2006.04710). SHA-256: `e768730af470059d5e92e3d642f0e470a4b437b1d5792faeec5c269cec46e9ea`.

## BibTeX

```bibtex
@inproceedings{Kim2021Lipschitz,
  author = {Kim, Hyunjik and Papamakarios, George and Mnih, Andriy},
  title = {The {L}ipschitz Constant of Self-Attention},
  booktitle = {Proceedings of the 38th International Conference on Machine Learning},
  series = {Proceedings of Machine Learning Research},
  volume = {139},
  pages = {5562--5571},
  year = {2021},
  eprint = {2006.04710},
  archivePrefix = {arXiv}
}
```
