---
type: paper
title: "RoFormer: Enhanced Transformer with Rotary Position Embedding"
aliases:
  - Su 2024
  - RoPE
  - RoFormer
  - su2021roformer
  - Rotary Position Embedding
  - rotarypositionembedding
  - su-2021-roformer-rope
  - Su et al. 2021
  - Su (2021) RoPE
authors:
  - Su, Jianlin
  - Lu, Yu
  - Pan, Shengfeng
  - Murtadha, Ahmed
  - Wen, Bo
  - Liu, Yunfeng
year: 2024
arxiv: "2104.09864"
url: https://arxiv.org/abs/2104.09864
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# RoFormer: Enhanced Transformer with Rotary Position Embedding

> [!info] Citation
> Su, J., Lu, Y., Pan, S., Murtadha, A., Wen, B., & Liu, Y. (2024). "RoFormer: Enhanced Transformer with Rotary Position Embedding." arXiv:2104.09864. https://arxiv.org/abs/2104.09864

## TL;DR
RoFormer introduces Rotary Position Embedding (RoPE), a multiplicative position encoding scheme that encodes absolute token position via a block-diagonal rotation matrix applied to queries and keys, while ensuring that the resulting attention inner product depends only on the relative position between tokens. RoPE achieves this without modifying additive context representations, is compatible with linear attention, exhibits a long-term decay property by construction, and demonstrates faster pre-training convergence and improved long-text performance relative to sinusoidal and learned absolute embedding baselines.

## Problem & setting
Standard transformer self-attention is position-agnostic: the attention weight between query at position $m$ and key at position $n$ depends on token content but not their sequential relationship unless position information is explicitly injected. Prior work either adds absolute position embeddings to token representations before projection (Vaswani et al. 2017; Devlin et al. 2019) or modifies the expanded QK inner product decomposition to include relative sinusoidal offsets (Shaw et al. 2018; Dai et al. 2019; Raffel et al. 2020). All additive schemes are incompatible with linear attention because the additive position term prevents factoring the kernel. The core challenge is to encode relative position in a way that is theoretically interpretable, computationally cheap, and compatible with linear (kernel) attention.

## Method
RoPE derives from the requirement that the inner product $\langle f_q(x_m, m),\, f_k(x_n, n)\rangle$ be expressible as a function $g(x_m, x_n, m-n)$ of relative position only. In 2D, this uniquely yields the complex-rotation solution:

$$f_q(x_m, m) = (W^q x_m)\,e^{im\theta}, \quad f_k(x_n, n) = (W^k x_n)\,e^{in\theta},$$

so that $q_m^\top k_n = \operatorname{Re}[(W^q x_m)(W^k x_n)^* e^{i(m-n)\theta}]$.

For general even dimension $d$, the embedding space is partitioned into $d/2$ two-dimensional subspaces and a block-diagonal rotation matrix $R^d_{\Theta,m}$ is applied:

$$f_{\{q,k\}}(x_m, m) = R^d_{\Theta,m}\, W^{\{q,k\}} x_m, \quad \Theta = \{\theta_i = 10000^{-2(i-1)/d}\},$$

yielding $q_m^\top k_n = x_m^\top W^q R^d_{\Theta,n-m} W^k x_n$. The rotation is applied after the linear projection; position information enters multiplicatively via element-wise cosine/sine factors, making it norm-preserving and compatible with linear attention by composing $R^d_{\Theta,m}$ with the kernel feature map outputs.

## Key results
The long-term decay property follows from the Abel-transform bound on the summed complex exponential, proving the inner product magnitude decreases as $|m-n|$ grows with $\theta_i = 10000^{-2i/d}$. Empirically: on WMT 2014 English-to-German, RoFormer achieves BLEU 27.5 vs. Transformer-base 27.3. On GLUE fine-tuning, RoFormer outperforms BERT on 3 of 6 tasks with notable gains on STS-B (87.0 vs. 85.8) and QQP (86.4 vs. 71.2). RoFormer shows faster MLM pre-training convergence than BERT. On the Chinese long-document CAIL2019-SCM task, RoFormer-1024 achieves 69.79% test accuracy vs. WoBERT-512 at 68.10%, confirming improved long-range generalization. Performer with RoPE also converges faster and to a lower loss than Performer without RoPE.

## Relevance to this research
RoPE is directly relevant to the VFE transformer's attention prior and position encoding design. The VFE framework supports a T5-style relative position bias table (the `t5_relative_bias` attention prior) as a learned scalar of offset; RoPE offers an alternative multiplicative encoding that is equivariant under rotation of the representation space. More substantively, RoPE's block-diagonal rotation structure is a sub-case of gauge transport: applying $R^d_{\Theta,m}$ to queries and $R^d_{\Theta,n}$ to keys is equivalent to parallel-transporting embeddings to a common "position-zero" reference frame via $\Omega_{mn} = R^d_{\Theta,n-m}$, exactly the GL(K) transport operator structure used in the gauge-equivariant attention. The relative-position-only inner product constraint $\langle f_q(x_m,m), f_k(x_n,n)\rangle = g(x_m,x_n,m-n)$ mirrors the gauge-invariance requirement that attention weights depend only on gauge-invariant comparisons between beliefs. The norm-preserving property of the orthogonal rotation matrix $R^d_{\Theta}$ is also consistent with the SPD/Riemannian belief geometry's isometry requirements. RoPE therefore serves as a concrete, computationally efficient instantiation of gauge-structured relative position encoding compatible with the VFE transformer's pure path.

> [!note] RoPE-as-abelian-gauge-frame framing (from refs/ note): PIFB makes the structural claim that **RoPE is an abelian gauge frame**. The per-block 2D rotation $R_m = \exp(m\,\theta J)$ is the exponential of a fixed antisymmetric generator $J$ scaled by position — exactly the project's gauge-frame construction $\Omega = \exp(\phi)$ specialized to a one-parameter abelian (commuting-rotation) subgroup, with $\phi$ linear in position. Under that reading RoPE's relative-position property is the gauge-covariance identity $\Omega_m \Omega_n^{-1} = \Omega_{m-n}$, i.e. the transport $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ restricted to commuting generators. RoPE is thus the **abelian base case** of the gauge-frame transport that PIFB's learned non-abelian $\phi$-frame generalizes (rotations in fixed planes become general $\mathrm{GL}^+(K)$ transport).

## Cross-links
- Concepts: [[Attention Mechanism]], [[Parallel transport|Gauge Transport]], [[su2024roformer|Rotary Position Embedding]], [[Gauge transformation]], [[Parallel transport]]
- Related sources: [[vaswani-2017-attention|vaswani2017attention]], [[dai2019transformerxl]], [[raffel2020exploring|raffel2020t5]], [[tsai-2019-kernel-attention]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) gauge-equivariant attention|GL(K) Attention]], [[participatory-it-from-bit]], [[Attention mechanisms — theory and positional structure]]

## BibTeX
```bibtex
@article{su2024roformer,
  author    = {Su, Jianlin and Lu, Yu and Pan, Shengfeng and Murtadha, Ahmed and Wen, Bo and Liu, Yunfeng},
  title     = {RoFormer: Enhanced Transformer with Rotary Position Embedding},
  journal   = {Neurocomputing},
  year      = {2024},
  volume    = {568},
  pages     = {127063},
  doi       = {10.1016/j.neucom.2023.127063},
  eprint    = {2104.09864},
  archivePrefix = {arXiv},
}
```
