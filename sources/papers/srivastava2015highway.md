---
type: paper
title: "Training Very Deep Networks"
aliases:
  - "Srivastava 2015"
  - "Highway Networks"
authors:
  - Srivastava, Rupesh Kumar
  - Greff, Klaus
  - Schmidhuber, Jürgen
year: 2015
arxiv: "1507.04025"
url: https://arxiv.org/abs/1507.04025
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Training Very Deep Networks

> [!info] Citation
> Srivastava, R. K., Greff, K., & Schmidhuber, J. (2015). "Training Very Deep Networks." *Advances in Neural Information Processing Systems (NIPS)*, 28. https://arxiv.org/abs/1507.04025

## TL;DR
Highway Networks introduce gated shortcut connections that allow gradients and information to flow across many layers with little attenuation, enabling the training of networks with hundreds of layers. The key mechanism is a learned transform gate T and carry gate C = 1 − T that interpolate between a nonlinear transformation and the identity at each layer. This work directly preceded and inspired the residual network (ResNet) architecture.

## Problem & setting
Training very deep feedforward networks (dozens to hundreds of layers) was practically infeasible due to vanishing/exploding gradients and the degradation problem — adding more layers would hurt rather than help performance. Prior approaches (careful initialization, batch normalization) offered partial relief but did not fundamentally solve depth scalability. The paper asks: can an architecture be designed so that optimization difficulty does not grow with depth?

## Method
Each Highway layer transforms an input **x** via:

$$\mathbf{y} = H(\mathbf{x}, \mathbf{W}_H) \cdot T(\mathbf{x}, \mathbf{W}_T) + \mathbf{x} \cdot C(\mathbf{x}, \mathbf{W}_C)$$

where $H$ is an arbitrary nonlinear transform, $T = \sigma(\mathbf{W}_T^\top \mathbf{x} + \mathbf{b}_T)$ is the transform gate (sigmoid), and $C = 1 - T$ is the carry gate. Initializing $\mathbf{b}_T$ to a large negative value biases the network toward carrying the input early in training, providing an easy gradient path from which the network can gradually learn to use its nonlinear transforms. The gates are learned end-to-end via backpropagation; no change to the optimizer is required.

## Key results
- Networks with 20, 50, and 100 highway layers were successfully trained end-to-end, achieving state-of-the-art results on MNIST and CIFAR-10 at the time.
- Depth (number of highway layers) consistently improved performance, demonstrating that the architecture genuinely exploits depth rather than merely tolerating it.
- Analysis of gate activations showed that different layers learn to use the transform vs. carry path selectively depending on input, suggesting the network dynamically routes information.
- The carry-gate mechanism provides an adaptive identity shortcut that keeps gradients non-vanishing throughout training.

## Relevance to this research
Highway Networks are background context for understanding residual/skip connections and gating mechanisms in deep architectures, which are ancestral to the transformer's residual stream. The gated interpolation $y = H(x) \cdot T + x \cdot (1-T)$ is structurally related to the VFE transformer's belief update equations, where a token's belief state is updated by blending prior beliefs with new evidence — a soft carry/transform decomposition analogous to the highway gate. More specifically, in the GL(K) gauge-equivariant attention framework, the E-step belief update $\mu_i \leftarrow \mu_i + \Delta\mu_i$ can be seen as a highway-like residual where the "carry" is the prior belief and the "transform" is the VFE gradient step; the gate magnitude is controlled by learning rates / step sizes rather than a learned sigmoid. This paper is primarily relevant as architectural background for the `project/transformer` line and does not directly bear on the gauge-theoretic or variational machinery.

## Cross-links
- Concepts: [[Residual Connections]], [[Gating Mechanisms]], [[Deep Networks]]
- Related sources: [[he-2016-resnet|he2016resnet]], [[vaswani-2017-attention|vaswani2017attention]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{srivastava2015highway,
  author    = {Srivastava, Rupesh Kumar and Greff, Klaus and Schmidhuber, J{\"{u}}rgen},
  title     = {Training Very Deep Networks},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {28},
  year      = {2015},
  url       = {https://arxiv.org/abs/1507.04025},
  eprint    = {1507.04025},
  archivePrefix = {arXiv},
}
```
