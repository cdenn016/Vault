---
type: paper
title: "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"
aliases:
  - "Dosovitskiy 2020"
  - "ViT"
authors:
  - Dosovitskiy, Alexey
  - Beyer, Lucas
  - Kolesnikov, Alexander
  - Weissenborn, Dirk
  - Zhai, Xiaohua
  - Unterthiner, Thomas
  - Dehghani, Mostafa
  - Minderer, Matthias
  - Heigold, Georg
  - Gelly, Sylvain
  - Uszkoreit, Jakob
  - Houlsby, Neil
year: 2020
arxiv: "2010.11929"
url: https://arxiv.org/abs/2010.11929
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

> [!info] Citation
> Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., & Houlsby, N. (2020). "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale." Published as a conference paper at ICLR 2021. arXiv:2010.11929.

## TL;DR
This paper introduces the Vision Transformer (ViT), which applies a standard Transformer encoder directly to sequences of image patches with minimal image-specific modifications. When pre-trained on sufficiently large datasets (14M–300M images), ViT matches or surpasses state-of-the-art convolutional networks on multiple image classification benchmarks while requiring substantially less compute to train. The central finding is that large-scale training overcomes the lack of CNN-style inductive biases inherent to the pure Transformer architecture.

## Problem & setting
Prior work on applying Transformers to vision either combined them with CNN backbones or introduced specialized attention patterns (local, sparse, axial) to handle the quadratic cost of pixel-level attention. The question is whether a minimal, unmodified Transformer — as used in NLP — can be applied directly to images and achieve competitive performance. The prior art (Cordonnier et al., 2020) applied full self-attention to 2×2 patches but only at small resolution; ViT scales this to practical resolutions and large datasets.

## Method
An image $x \in \mathbb{R}^{H \times W \times C}$ is reshaped into a sequence of $N = HW/P^2$ flattened 2D patches $x_p \in \mathbb{R}^{N \times (P^2 \cdot C)}$. Each patch is linearly projected to a $D$-dimensional embedding:

$$z_0 = [x_\text{class};\, x^1_p E;\, x^2_p E;\, \ldots;\, x^N_p E] + E_\text{pos}, \quad E \in \mathbb{R}^{(P^2 \cdot C) \times D},\; E_\text{pos} \in \mathbb{R}^{(N+1) \times D}$$

A learnable [class] token is prepended (following BERT), and standard learnable 1D position embeddings are added. The resulting sequence is processed by $L$ alternating layers of multihead self-attention (MSA) and MLP blocks with pre-norm and residual connections:

$$z'_\ell = \text{MSA}(\text{LN}(z_{\ell-1})) + z_{\ell-1}, \quad z_\ell = \text{MLP}(\text{LN}(z'_\ell)) + z'_\ell$$

The class token output $y = \text{LN}(z^0_L)$ is used for classification. Three model scales are defined: ViT-Base (86M params, 12 layers, $D=768$, 12 heads), ViT-Large (307M, 24 layers, $D=1024$, 16 heads), and ViT-Huge (632M, 32 layers, $D=1280$, 16 heads). A hybrid variant feeds CNN feature maps into the Transformer in place of raw patches.

## Key results
ViT-H/14 pre-trained on JFT-300M achieves 88.55% top-1 on ImageNet, 90.72% on ImageNet-ReaL, 94.55% on CIFAR-100, and 77.63% on VTAB (19 tasks), matching or exceeding the BiT (ResNet152x4) and Noisy Student baselines while using 4–5× less TPUv3-core-days to pre-train (2.5k vs. 9.9k–12.3k). On smaller datasets (ImageNet alone, without large pre-training), ViT underperforms ResNets, confirming that the lack of convolutional inductive biases requires data scale to compensate. Attention distance analysis shows that some heads in the lowest layers already attend globally across the full image, while others remain localized (analogous to early convolutional filters). Self-supervised masked patch prediction yields 79.9% on ImageNet for ViT-B/16, 2% above training from scratch but 4% below supervised pre-training.

## Relevance to this research
ViT establishes the canonical form of patch-based self-attention that the VFE transformer generalizes. The VFE transformer replaces dot-product softmax attention with variational free-energy minimization over Gaussian belief tuples $(\mu, \Sigma, \phi)$, where the attention weights $\beta_{ij}$ emerge as stationary points of $F$ rather than as softmax of inner products. ViT's MSA equations (Eqs. 5–8) are the flat, non-probabilistic special case that the GL(K) gauge-equivariant attention subsumes: the key-query product $qk^\top / \sqrt{D_h}$ maps onto the KL divergence $\text{KL}(q_i \| \Omega_{ij} q_j)$ under the appropriate Gaussian parameterization, and the softmax corresponds to the entropy-regularized stationary condition for $\beta_{ij}$ in the VFE free energy. The patch embedding linear projection $E$ is also the structural antecedent of the VFE encoder that maps observations into belief-space $(\mu, \Sigma)$. ViT's finding that positional embeddings learn 2D topology from data (without hand-crafted 2D structure) is relevant to the T5 relative-position bias design in the VFE transformer.

## Cross-links
- Concepts: [[Attention Mechanism]], [[Transformer Architecture]], [[Self-Attention]]
- Related sources: [[vaswani-2017-attention]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) Attention]]

## BibTeX
```bibtex
@inproceedings{Dosovitskiy2020,
  author    = {Dosovitskiy, Alexey and Beyer, Lucas and Kolesnikov, Alexander and Weissenborn, Dirk and Zhai, Xiaohua and Unterthiner, Thomas and Dehghani, Mostafa and Minderer, Matthias and Heigold, Georg and Gelly, Sylvain and Uszkoreit, Jakob and Houlsby, Neil},
  title     = {An Image is Worth 16x16 Words: {T}ransformers for Image Recognition at Scale},
  booktitle = {International Conference on Learning Representations},
  year      = {2021},
  note      = {arXiv:2010.11929},
}
```
