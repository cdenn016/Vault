---
type: reference
title: "Improving Transformers with Probabilistic Attention Keys"
aliases:
  - "Nguyen et al. 2022 Transformer-MGK"
  - "Improving Transformers with Probabilistic Attention Keys"
  - "Transformer-MGK"
  - "Nguyen2022MGK"
authors:
  - Tam Nguyen
  - Tan M. Nguyen
  - Dung D. Le
  - Duy Khuong Nguyen
  - Viet-Anh Tran
  - Richard G. Baraniuk
  - Nhat Ho
  - Stanley J. Osher
year: 2022
arxiv: "2110.08678"
url: https://arxiv.org/abs/2110.08678
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-09-23
updated: 2026-09-23
---

# Improving Transformers with Probabilistic Attention Keys

> [!info] Citation
> Tam Nguyen, Tan M. Nguyen, Dung D. Le, Duy Khuong Nguyen, Viet-Anh Tran, Richard G. Baraniuk, Nhat Ho, Stanley J. Osher (2022). "Improving Transformers with Probabilistic Attention Keys." *Proceedings of the 39th International Conference on Machine Learning*, PMLR **162**, 16595–16621. Preprint: [arXiv:2110.08678](https://arxiv.org/abs/2110.08678) (v2 read).

## TL;DR

The paper reads each attention score as the posterior responsibility of a key for a query in a Gaussian mixture model and then replaces every key with a mixture of Gaussians (Transformer-MGK). Four-head MGK models match or beat eight-head softmax baselines with fewer parameters and FLOPs, and a linear-attention variant (Transformer-MLK) is also given.

## What it establishes

Section 2.1 models a query $q_i$ with the mixture $p(q_i)=\sum_j\pi_j\mathcal N(q_i\mid k_j,\sigma_j^2I)$ (Eq. 3) and computes the posterior $p(t_j=1\mid q_i)$ that key $k_j$ generated $q_i$. With normalized queries and keys, a uniform prior, and $\sigma_j^2=\sigma^2$, the posterior becomes $\operatorname{softmax}_j(q_i^\top k_j/\sigma^2)$ (Eq. 4), which is the attention score when $\sigma^2=\sqrt D$. The paper therefore identifies the attention score with the responsibility that key $k_j$ takes for explaining $q_i$. Remark 1 defends the normalization assumption. Section 2.2 replaces each key by a Gaussian mixture, $P(q_i\mid t_j=1)=\sum_r\pi_{jr}\mathcal N(q_i\mid k_{jr},\sigma_{jr}^2I)$ (Eq. 5), motivated by a density-approximation result (Theorem 1). It then drops the normalization assumption, so the MGK score uses Gaussian kernels $\exp(-\lVert q_i-k_{jr}\rVert^2/2\sigma_{jr}^2)$ between queries and keys instead of dot products (Eq. 7). The experiments cover WikiText-103 language modeling and the Long Range Arena, where Transformer-MGK with four heads is comparable to or better than an eight-head baseline.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript cites Transformer-MGK as a point-query precedent for reading routing weights as mixture responsibilities. The manuscript's Gaussian-KL routing scores Gaussian query and key states rather than point queries against Gaussian keys. In Section 2.1 the norm terms of the Gaussian likelihood are removed by assuming normalized queries and keys. The MGK score of Eq. 7 keeps them and is a distance-based score of the kind studied in [[kim-2021-lipschitz-self-attention]]. The manuscript treats the key-norm term explicitly; [[movellan-2020-probabilistic-transformers]] gives the point-query compensating prior. See [[Attention mechanisms — theory and positional structure]].

## Local full text

The arXiv v2 PDF is stored at `sources/pdfs/Nguyen2022MGK.pdf` ([local PDF](../pdfs/Nguyen2022MGK.pdf)). Source: [arXiv:2110.08678](https://arxiv.org/pdf/2110.08678). SHA-256: `7c7506993d4b34658530ef9965749f0fee972a48b9bc3fc6cd0b42a24ebaf9e4`.

## BibTeX

```bibtex
@inproceedings{Nguyen2022MGK,
  author = {Nguyen, Tam and Nguyen, Tan M. and Le, Dung D. and Nguyen, Duy Khuong and Tran, Viet-Anh and Baraniuk, Richard G. and Ho, Nhat and Osher, Stanley J.},
  title = {Improving Transformers with Probabilistic Attention Keys},
  booktitle = {Proceedings of the 39th International Conference on Machine Learning},
  series = {Proceedings of Machine Learning Research},
  volume = {162},
  pages = {16595--16621},
  year = {2022},
  eprint = {2110.08678},
  archivePrefix = {arXiv}
}
```
