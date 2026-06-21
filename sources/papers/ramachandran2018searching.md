---
type: paper
title: "Searching for Activation Functions"
aliases:
  - "Ramachandran 2018"
  - "Swish"
authors:
  - Ramachandran, Prajit
  - Zoph, Barret
  - Le, Quoc V.
year: 2018
arxiv: "1710.05941"
url: https://arxiv.org/abs/1710.05941
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Searching for Activation Functions

> [!info] Citation
> Ramachandran, P., Zoph, B., & Le, Q. V. (2018). "Searching for Activation Functions." ICLR 2018 (workshop). arXiv:1710.05941.

## TL;DR
This paper proposes using automated search — combining exhaustive enumeration and reinforcement learning with an RNN controller — to discover novel scalar activation functions for deep networks. The best discovered function, Swish ($f(x) = x \cdot \sigma(\beta x)$), consistently matches or outperforms ReLU across image classification and machine translation benchmarks on deep models. The work demonstrates that hand-designed activation functions can be surpassed by search-discovered alternatives and that the non-monotonic smooth structure of Swish is advantageous for modern architectures.

## Problem & setting
ReLU is the dominant activation function, but hand-designed alternatives (Leaky ReLU, PReLU, ELU, SELU, GELU) have failed to achieve consistent gains over it. The question is whether automated search techniques — analogous to neural architecture search — can discover activation functions that are more generally better than ReLU. Prior work on neural architecture search (Zoph & Le, 2016) motivated the use of RL-based search; the activation function search space is simpler (scalar-to-scalar functions) but still admits a combinatorial explosion ($\sim 10^{12}$ possibilities for multi-core-unit compositions).

## Method
The search space is built by composing "core units" of the form $b(u_1(x_1), u_2(x_2))$, where $u_i$ are scalar unary functions (e.g., $x$, $\sigma(x)$, $\tanh(x)$, $\sin(x)$, $x^2$) and $b$ is a binary function (e.g., multiplication, addition, $\max$). For small search spaces, exhaustive enumeration is used; for large spaces, an RNN controller trained with Proximal Policy Optimization proposes activation functions, and child networks (ResNet-20 on CIFAR-10) are trained to provide reward signals. The best discovered function is Swish:
$$f(x) = x \cdot \sigma(\beta x)$$
where $\beta$ is either a fixed constant or a per-channel learnable parameter. When $\beta \to 0$, Swish approaches $x/2$; as $\beta \to \infty$, it approaches ReLU. Swish is smooth, non-monotonic, unbounded above, and bounded below — properties that distinguish it from ReLU.

## Key results
Across CIFAR-10, CIFAR-100, and ImageNet (five architectures: Inception-ResNet-v2, Inception-v3, Inception-v4, MobileNet, Mobile NASNet-A) and WMT English-to-German translation (Transformer), Swish outperforms or matches ReLU and six other baseline activation functions in 9 of 9 comparisons against ReLU and most comparisons against the others. Specific gains: +0.9% top-1 ImageNet accuracy on Mobile NASNet-A, +0.6% on Inception-ResNet-v2, +2.2% on MobileNet. In Table 3 aggregate comparison, Swish strictly outperforms every baseline on more configurations than it underperforms, with statistical significance under a one-sided paired sign test. Trainable $\beta$ values concentrate around $\beta \approx 1$ but spread between 0 and 1.5, suggesting the model exploits the additional flexibility.

## Relevance to this research
This paper has peripheral relevance to the VFE transformer program. The V3 transformer explicitly excludes neural-network components including activation functions (the hard constraint is no `nn.Linear`, no MLP, no activations), so Swish is not used in the VFE architecture. However, the paper is relevant as background on the standard Transformer architecture (Vaswani et al., 2017), which uses ReLU in its feed-forward sublayers and which this program aims to replace with a VFE-minimization-based attention mechanism. Additionally, GELU (Hendrycks & Gimpel, 2016) — a close relative of Swish — appears in many modern transformer variants the VFE program compares against. Understanding the activation function landscape clarifies what the VFE architecture is deliberately moving away from: parameterized nonlinearities are replaced by iterative belief updates governed by a free-energy functional.

## Cross-links
- Concepts: [[Attention Mechanism]]
- Related sources: [[vaswani2017attention]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{ramachandran2018searching,
  author  = {Ramachandran, Prajit and Zoph, Barret and Le, Quoc V.},
  title   = {Searching for Activation Functions},
  journal = {arXiv preprint arXiv:1710.05941},
  year    = {2018},
}
```
