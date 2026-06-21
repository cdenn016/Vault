---
type: paper
title: "Gaussian Error Linear Units (GELUs)"
aliases:
  - "Hendrycks 2016"
  - "GELU"
authors:
  - Hendrycks, Dan
  - Gimpel, Kevin
year: 2016
arxiv: "1606.08415"
url: https://arxiv.org/abs/1606.08415
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Gaussian Error Linear Units (GELUs)

> [!info] Citation
> Hendrycks, Dan and Gimpel, Kevin (2016). "Gaussian Error Linear Units (GELUs)." arXiv:1606.08415. https://arxiv.org/abs/1606.08415.

## TL;DR
This paper introduces the Gaussian Error Linear Unit (GELU), a smooth nonlinear activation function defined as $\text{GELU}(x) = x \Phi(x)$, where $\Phi(x)$ is the standard Gaussian CDF. The GELU combines properties of dropout, zoneout, and ReLU by stochastically gating inputs based on their magnitude, and its smooth, non-monotone shape consistently outperforms ReLU and ELU across a range of NLP and vision tasks.

## Problem & setting
Prior activation functions such as ReLU and ELU apply deterministic, threshold-based gating that does not take into account the distribution of the input. The authors seek an activation that bridges stochastic regularization (dropout) and deterministic nonlinearity, producing a unit that weights inputs by how likely they are to be greater than other inputs drawn from the same distribution.

## Method
The GELU is defined as:
$$\text{GELU}(x) = x \cdot \Phi(x) = x \cdot P(X \le x), \quad X \sim \mathcal{N}(0,1).$$
This can be interpreted as a stochastic regularizer: in expectation over a Bernoulli mask $m \sim \text{Bernoulli}(\Phi(x))$, the output is $m \cdot x$, so the unit drops inputs with probability $1 - \Phi(x)$. A practical approximation is:
$$\text{GELU}(x) \approx 0.5 x \left(1 + \tanh\!\left[\sqrt{2/\pi}(x + 0.044715\, x^3)\right]\right).$$
The function is smooth, non-monotone (it has a local minimum near $x \approx -0.17$), and converges to the identity for large positive $x$ and to zero for large negative $x$.

## Key results
- GELU outperforms ReLU and ELU on MNIST classification (including corrupted MNIST variants), TIMIT speech modeling, and document classification benchmarks.
- The non-monotone, smooth shape is argued to be the key advantage: unlike ReLU, the GELU does not have a zero gradient region, allowing gradient flow even for negative pre-activations near zero.
- The GELU was subsequently adopted as the default activation in BERT, GPT-2/3, and most large transformer models.

## Relevance to this research
The GELU is mentioned here primarily for completeness as a standard transformer component. The VFE transformer (V3) is explicitly no-neural-network (no `nn.Linear`, no MLP activations) — all capacity comes from iterative VFE minimization over Gaussian belief tuples `(mu, Sigma, phi)`, and GELUs play no role in the pure path. However, the Gaussian gating interpretation ($x \Phi(x)$) is conceptually adjacent to the Gaussian belief geometry central to the SPD/VFE framework: the soft thresholding by the Gaussian CDF can be read as a single-neuron approximation of belief-weighted gating, which is the continuous limit of dropout regularization. If hybrid ablations ever reintroduce MLP components (e.g., feed-forward sublayers for comparison baselines), GELU would be the natural activation choice consistent with the broader transformer literature.

## Cross-links
- Concepts: [[Gaussian Beliefs]], [[Transformer Architecture]], [[Activation Functions]]
- Related sources: [[vaswani-2017-attention|vaswani2017attention]], [[devlin-2018-bert|devlin2018bert]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{hendrycks2016gaussian,
  author  = {Hendrycks, Dan and Gimpel, Kevin},
  title   = {Gaussian Error Linear Units ({GELUs})},
  journal = {arXiv preprint arXiv:1606.08415},
  year    = {2016},
  url     = {https://arxiv.org/abs/1606.08415},
}
```
