---
type: paper
title: "Transformer Dissection: A Unified Understanding of Transformer's Attention via the Lens of Kernel"
aliases:
  - "Tsai 2019"
  - "Tsai et al. 2019 — Kernel View of Attention"
authors:
  - Tsai, Yao-Hung Hubert
  - Bai, Shaojie
  - Yamada, Makoto
  - Morency, Louis-Philippe
  - Salakhutdinov, Ruslan
year: 2019
arxiv: "1908.11775"
url: https://arxiv.org/abs/1908.11775  # arXiv (EMNLP 2019; no public DOI)
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-18
updated: 2026-06-20
---

# Transformer Dissection: A Unified Understanding of Transformer's Attention via the Lens of Kernel

> [!info] Citation
> Yao-Hung Hubert Tsai, Shaojie Bai, Makoto Yamada, Louis-Philippe Morency, and Ruslan Salakhutdinov. "Transformer Dissection: A Unified Understanding of Transformer's Attention via the Lens of Kernel." EMNLP 2019. arXiv:1908.11775. <https://arxiv.org/abs/1908.11775>

## TL;DR

This paper recasts the attention mechanism of the Transformer (see [[vaswani-2017-attention]]) as a **non-parametric kernel smoother**: each output is a weighted average of value vectors, where the weights are the values of a kernel function measuring similarity between a query and each key. This single reinterpretation absorbs the softmax scores, the scaling, and the positional encoding into the *design of the kernel itself*, turning ad-hoc architectural choices into explicit modelling decisions over (i) which similarity function to use and (ii) how to inject positional structure. The framework exposes a large design space of attention variants and motivates a symmetric-kernel-product variant that is competitive at lower cost.

## Problem & setting

Standard scaled dot-product attention computes, for a query $q$ and a set of key/value pairs $\{(k_j, v_j)\}$,
$$
\mathrm{Attn}(q) = \sum_j \frac{\exp(\langle q, k_j\rangle / \sqrt{d})}{\sum_{j'} \exp(\langle q, k_{j'}\rangle/\sqrt{d})}\, v_j .
$$
The exponentiated inner products, the $1/\sqrt d$ temperature, and the various positional-encoding schemes (absolute additive, relative, etc.) are usually treated as separate engineering choices with no unifying account. The paper asks: is there a single mathematical object from which all of these fall out as special cases, so that they can be reasoned about and varied principledly?

## Method

The key observation is that attention has exactly the form of a **kernel smoother** (Nadaraya–Watson regression). Define a non-negative kernel $\kappa(q, k)$ that scores the similarity between a query and a key. Then attention is
$$
\mathrm{Attn}(q) = \sum_j \frac{\kappa(q, k_j)}{\sum_{j'} \kappa(q, k_{j'})}\, v(k_j),
$$
i.e. a kernel-weighted average of values, with the denominator acting as the normalizer of a probability distribution over positions. Softmax dot-product attention is recovered by the exponential-of-inner-product kernel $\kappa(q,k) = \exp(\langle q,k\rangle/\sqrt d)$, which is (up to normalization) an asymmetric exponential kernel.

Two consequences follow:

- **Positional information lives inside the kernel.** Rather than adding a position vector to the token embedding before attention, one can define the kernel on the *product space* of content and position, $\kappa\big((f_q, p_q), (f_k, p_k)\big)$, and factor it — often as a product of a content kernel and a position kernel, $\kappa_f \cdot \kappa_p$. Different existing schemes (absolute, relative, Transformer-XL-style) correspond to different choices and placements of $\kappa_p$. This makes positional structure a first-class, composable part of the similarity measure.
- **A larger design space of attentions.** Because any valid kernel induces a valid attention, one can swap in symmetric kernels, exponential kernels, or products of kernels. The authors propose a variant built from a **product of symmetric kernels** that achieves competitive accuracy with reduced computation on neural machine translation and sequence prediction.

## Key results

- A unified kernel formulation that subsumes softmax dot-product attention and most published positional-encoding variants as particular kernel choices.
- A principled recipe for embedding positional structure directly into the similarity kernel via kernel composition on the content–position product space.
- An empirically validated symmetric-kernel-product attention variant that matches baseline Transformer quality on machine translation and sequence prediction with lower compute.

## Relevance to this research

This paper supplies the theoretical bridge underneath two ingredients of the VFE-transformer program:

- **Precision-weighted attention as a metric/kernel.** The project's `precision_weighted_attention` weights interactions by a learned precision (inverse-covariance) rather than a raw dot product. The kernel view makes this rigorous: replacing $\langle q,k\rangle$ with a Mahalanobis-type form $q^\top \Lambda\, k$ (or an [[Fisher information metric]]-/SPD-induced bilinear form) is simply choosing a different similarity kernel inside the same smoother. Since the per-token belief carries a covariance $\Sigma$ on the SPD manifold (see [[pennec-2006-affine-invariant-tensor]], [[wang-2023-riemannian-self-attention-spd]]), the affine-invariant metric on $\Sigma$ becomes a natural kernel, and the attention-entropy term is exactly the entropy of the normalized kernel distribution this framework defines. This connects [[Precision weighting]] in predictive coding to attention weights.
- **Learned positional $\phi$ inside the kernel.** The project composes positional encodings from a learned Lie-algebra element $\phi$ (via BCH retraction) together with RoPE, ALiBi, and T5 relative buckets. Tsai et al. show that all such positional signals can be folded into a *position kernel* $\kappa_p$ multiplied against the content kernel — giving a clean justification for treating learned $\phi$, rotary, and relative-bucket biases as composable factors of one similarity measure rather than as unrelated patches. This grounds the project's positional-$\phi$-composed-with-BCH design in attention theory.

> [!note] Editorial: The paper itself does not discuss precision matrices, SPD geometry, or gauge structure; the connections above extend its kernel formulation to the project's metric-based and Lie-algebraic settings.

## Cross-links

- Concepts: [[Precision weighting]], [[Fisher information metric]]
- Sources: [[vaswani-2017-attention]], [[pennec-2006-affine-invariant-tensor]], [[wang-2023-riemannian-self-attention-spd]]
- Project: [[VFE Transformer Program]]

```bibtex
@inproceedings{tsai2019transformer,
  title     = {Transformer Dissection: A Unified Understanding of Transformer's Attention via the Lens of Kernel},
  author    = {Tsai, Yao-Hung Hubert and Bai, Shaojie and Yamada, Makoto and Morency, Louis-Philippe and Salakhutdinov, Ruslan},
  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  year      = {2019},
  eprint    = {1908.11775},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/1908.11775}
}
```
