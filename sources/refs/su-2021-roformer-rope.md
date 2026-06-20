---
type: reference
title: "RoFormer: Enhanced Transformer with Rotary Position Embedding"
aliases:
  - "Su et al. 2021"
  - "Su (2021) RoPE"
authors:
  - Jianlin Su
  - Yu Lu
  - Shengfeng Pan
  - Ahmed Murtadha
  - Bo Wen
  - Yunfeng Liu
year: 2021
arxiv: "2104.09864"
url: https://arxiv.org/abs/2104.09864
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# RoFormer: Enhanced Transformer with Rotary Position Embedding

> [!info] Citation
> Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu (2021). "RoFormer: Enhanced Transformer with Rotary Position Embedding." *Neurocomputing* 568 (2024): 127063. arXiv:2104.09864. <https://arxiv.org/abs/2104.09864>

## TL;DR

RoPE (Rotary Position Embedding) injects position into attention by **rotating** the query and key vectors by an angle proportional to their absolute position, dividing the feature space into 2D blocks and applying a position-dependent planar rotation to each. Because rotations compose by subtraction of angles, the resulting query-key inner product depends only on the **relative** position $m - n$, so RoPE encodes absolute position while making attention scores relative — and it does so multiplicatively, with no added bias term and graceful behavior as sequence length grows.

## What it establishes

- A closed-form position encoding via block-diagonal 2D rotations applied to $q$ and $k$ before the dot product.
- The inner product $\langle R_m q,\, R_n k\rangle$ depends only on $m-n$, giving exact relative-position dependence from an absolute-position construction.
- Each frequency block rotates at its own rate (a geometric spectrum of wavelengths), and the scheme is compatible with linear-attention variants.
- Strong empirical performance and length-extrapolation behavior, now standard in many large language models.

## Why the project cites it

PIFB ([[participatory-it-from-bit]]) makes the structural claim that **RoPE is an abelian gauge frame**. The per-block 2D rotation $R_m = \exp(m\,\theta J)$ is the exponential of a fixed antisymmetric generator $J$ scaled by position — exactly the project's gauge-frame construction $\Omega = \exp(\phi)$ specialized to a one-parameter abelian (commuting-rotation) subgroup, with $\phi$ a linear function of position. Under that reading RoPE's relative-position property is the gauge-covariance identity $\Omega_m \Omega_n^{-1} = \Omega_{m-n}$, which is precisely the transport $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ specialized to commuting generators. This is the concrete, established positional scheme that PIFB's learned non-abelian $\phi$-frame generalizes (rotations in fixed planes become general $\mathrm{GL}^+(K)$ transport), so Su et al. is cited as the abelian base case of the gauge-frame transport in [[Attention mechanisms — theory and positional structure]]. The kernel-composition view ([[tsai-2019-kernel-attention]]) records the same fact from the smoother side: RoPE is a multiplicative position kernel.

```bibtex
@article{su2024roformer,
  title         = {RoFormer: Enhanced Transformer with Rotary Position Embedding},
  author        = {Su, Jianlin and Lu, Yu and Pan, Shengfeng and Murtadha, Ahmed and
                   Wen, Bo and Liu, Yunfeng},
  journal       = {Neurocomputing},
  volume        = {568},
  pages         = {127063},
  year          = {2024},
  eprint        = {2104.09864},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2104.09864}
}
```
