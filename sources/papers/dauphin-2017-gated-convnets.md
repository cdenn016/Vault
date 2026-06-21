---
type: paper
title: "Language Modeling with Gated Convolutional Networks"
aliases:
  - "Dauphin 2017"
  - "GLU"
  - "GCNN"
  - "Gated Linear Unit"
authors:
  - Dauphin, Yann N.
  - Fan, Angela
  - Auli, Michael
  - Grangier, David
year: 2017
arxiv: "1612.08083"
url: https://arxiv.org/abs/1612.08083
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Language Modeling with Gated Convolutional Networks

> [!info] Citation
> Dauphin, Y. N., Fan, A., Auli, M., & Grangier, D. (2017). "Language Modeling with Gated Convolutional Networks." Proceedings of the 34th International Conference on Machine Learning (ICML), PMLR 70. arXiv:1612.08083.

## TL;DR
This paper introduces Gated Convolutional Networks (GCNNs) for language modeling, replacing recurrent connections with stacked temporal convolutions controlled by a novel Gated Linear Unit (GLU). The GLU takes the form $h(X) = (X * W + b) \otimes \sigma(X * V + c)$, where the sigmoid-gated branch controls information flow while preserving a linear gradient path that alleviates vanishing gradients. The approach achieves state-of-the-art perplexity on WikiText-103 and competitive results on Google Billion Word with an order-of-magnitude improvement in responsiveness over LSTM baselines.

## Problem & setting
Statistical language models must estimate $P(w_0, \ldots, w_N) = \prod_i P(w_i | w_0, \ldots, w_{i-1})$. The dominant approach at the time of writing was LSTM-based recurrent networks, which are inherently sequential and cannot be parallelized over positions. Convolutional approaches existed (e.g., Oord et al. 2016 PixelCNN) but used LSTM-style $\tanh \otimes \sigma$ gating that re-introduces vanishing gradients. The authors ask whether a purely convolutional, parallelizable architecture can match or exceed LSTM perplexity.

## Method
The core architectural unit is the Gated Linear Unit (GLU):

$$h_l(X) = (X * W + b) \otimes \sigma(X * V + c)$$

where $X \in \mathbb{R}^{N \times m}$ is the layer input, $W, V \in \mathbb{R}^{k \times m \times n}$ are learned convolutional kernels, and $\sigma$ is the sigmoid. The gradient of the GLU is

$$\nabla[X \otimes \sigma(X)] = \nabla X \otimes \sigma(X) + X \otimes \sigma'(X)\nabla X,$$

which contains the path $\nabla X \otimes \sigma(X)$ without any compressive nonlinearity — a multiplicative skip connection. In contrast, the LSTM-style Gated Tanh Unit (GTU) $\tanh(X) \otimes \sigma(X)$ has gradient proportional to $\tanh'(X)\sigma(X) + \sigma'(X)\tanh(X)$, both of which saturate and shrink the gradient. Multiple GLU layers are wrapped in pre-activation residual blocks with optional bottleneck structure ($1 \times 1$ projections bracketing a $k > 1$ convolution). Causal masking is achieved by left-padding with $k-1$ zeros so that $h_i$ depends only on $w_0, \ldots, w_{i-1}$. Output uses adaptive softmax to reduce vocabulary computation cost.

## Key results
- On Google Billion Word (single GPU, adaptive softmax), GCNN-13 reaches 38.1 test perplexity vs. 39.8 for a comparable 2-layer LSTM (Grave et al. 2016); GCNN-14 Bottleneck on 8 GPUs reaches 31.9 vs. 30.6 for the much larger Jozefowicz et al. (2016) model trained on 32 GPUs for 3 weeks.
- On WikiText-103, GCNN-8 reaches 44.9 perplexity vs. 48.7 for LSTM-1024; GCNN-14 reaches 37.2 (state-of-the-art at time of publication).
- Responsiveness (tokens/s, single-sequence, GPU): GCNN with bottleneck achieves 45,878 vs. 2,282 for LSTM — a 20x improvement — because all positions can be computed in parallel.
- Ablation of gating: GLU $>$ ReLU $>$ GTU $>$ Tanh in both final perplexity and convergence speed. GLU outperforms GTU by approximately 5 perplexity points on GBW, comparable to the LSTM-vs-RNN gap.
- Context size ablation: perplexity continues to improve up to context $\approx 40$ tokens, then diminishes rapidly, suggesting unbounded recurrent context is not necessary for strong language model performance.
- Non-linearity ablation: bilinear layers ($\otimes$ without sigmoid) suffice to beat KN 5-gram (61 vs. 67.6 PPL); adding the sigmoid gate (GLU) improves another ~20 PPL points.

## Relevance to this research
The GLU is directly relevant to gating in transformer-style attention: the mechanism $A \otimes \sigma(B)$ with element-wise multiplicative control is structurally analogous to the information-flow gating implicit in VFE belief updates, where $\sigma_q$ (precision) gates how strongly incoming messages modulate a belief mean. The linear-path gradient argument parallels the rationale for keeping the VFE update equations differentiable through the Gaussian parameterization rather than through saturating nonlinearities. The paper's demonstration that finite-context hierarchical (convolutional) models can match unbounded-context recurrent models is also conceptually relevant to the VFE transformer's use of finite attention windows over belief states. The GLU's element-wise gating $\otimes \sigma(\cdot)$ reappears in many modern gated attention variants (e.g., gated MLP blocks in PaLM, gated linear attention) that inform architectural choices around the attention score computation in the GL(K) framework.

## Cross-links
- Concepts: [[Attention Mechanisms]] [[Gated Linear Unit]] [[Vanishing Gradient]]
- Related sources: [[vaswani-2017-attention]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{dauphin2017language,
  author    = {Dauphin, Yann N. and Fan, Angela and Auli, Michael and Grangier, David},
  title     = {Language Modeling with Gated Convolutional Networks},
  booktitle = {Proceedings of the 34th International Conference on Machine Learning},
  series    = {Proceedings of Machine Learning Research},
  volume    = {70},
  pages     = {933--941},
  year      = {2017},
  publisher = {PMLR},
  url       = {https://arxiv.org/abs/1612.08083},
}
```
