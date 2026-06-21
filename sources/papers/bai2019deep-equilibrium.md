---
type: paper
title: "Deep Equilibrium Models"
aliases:
  - "Bai 2019"
  - "DEQ"
authors:
  - Bai, Shaojie
  - Kolter, J. Zico
  - Koltun, Vladlen
year: 2019
arxiv: "1909.01377"
url: https://arxiv.org/abs/1909.01377
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Deep Equilibrium Models

> [!info] Citation
> Bai, Shaojie, J. Zico Kolter, and Vladlen Koltun (2019). "Deep Equilibrium Models." NeurIPS 2019. arXiv:1909.01377.

## TL;DR
Deep equilibrium models (DEQs) replace the finite stack of layers in a deep network with the fixed-point equation $z^\star = f_\theta(z^\star; x)$ and solve for this equilibrium directly via root-finding (Broyden's quasi-Newton method), bypassing the need to store intermediate activations. Gradients are computed analytically through the equilibrium via implicit differentiation, yielding a constant-memory backward pass regardless of the effective network depth. On large-scale language modeling (WikiText-103), DEQ-Transformers and DEQ-TrellisNets match or slightly outperform their layer-stacked counterparts while consuming up to 88% less training memory.

## Problem & setting
Standard deep sequence models (Transformers, TCNs, RNNs) must store all $L$ intermediate hidden states during training for backpropagation, making memory cost $O(L)$ and severely limiting depth on a single GPU. Prior remedies — gradient checkpointing ($O(\sqrt{L})$) and reversible networks — still scale with depth. The paper asks: if weight-tied networks empirically converge to a fixed point as depth grows, why not target that fixed point directly?

## Method
Given a weight-tied, input-injected sequence transformation $f_\theta$, the DEQ defines the model output as the fixed point

$$z^\star_{1:T} = f_\theta(z^\star_{1:T};\, x_{1:T}),$$

equivalently the root of $g_\theta(z) = f_\theta(z; x) - z = 0$. The forward pass solves this root-finding problem with Broyden's method, which maintains a low-rank approximation to $J_{g_\theta}^{-1}$ via the Sherman–Morrison update. The backward pass exploits implicit differentiation (Theorem 1): the loss gradient is

$$\frac{\partial \ell}{\partial (\cdot)} = -\frac{\partial \ell}{\partial z^\star} \Bigl(J_{g_\theta}^{-1}\big|_{z^\star}\Bigr) \frac{\partial f_\theta(z^\star; x)}{\partial (\cdot)},$$

which requires only the equilibrium $z^\star$ and one solve of a linear system — no stored activations. The inverse Jacobian factor is again approximated via Broyden applied to the transposed linear system. Two instantiations are provided: DEQ-TrellisNet (weight-tied temporal convolutions with LSTM gating) and DEQ-Transformer (weight-tied multi-head self-attention with Transformer-XL relative positional embeddings and layer normalization).

Theorem 2 (Universality) proves that stacking multiple DEQ modules yields no extra representational power over a single DEQ: any composition of two equilibria $\text{RootFind}(g^v_{\theta_2}; \text{RootFind}(g^f_{\theta_1}; x))$ is equivalent to a single, larger DEQ.

## Key results
- DEQ-Transformer (medium, adaptive embedding) achieves test perplexity 23.2 on WikiText-103, versus 23.6 for the comparable Transformer-XL, using 3.7 GB memory vs. 9.0 GB — a $\approx 59\%$ reduction at equivalent model size.
- DEQ-TrellisNet matches the 70-layer TrellisNet (29.0 vs. 29.2 perplexity on WT103) while using 3.3 GB vs. 24.7 GB (87% reduction), and less than gradient-checkpointing's 5.2 GB.
- On Penn Treebank, DEQ-TrellisNet achieves 57.1 test perplexity using 1.2 GB, matching the 60-layer TrellisNet (57.0) at 8.5 GB.
- Memory complexity is $O(1)$ (constant, independent of effective depth); training runtime is roughly $2.4$–$2.8\times$ slower than the layer-based counterparts due to iterative root-finding.
- The number of Broyden iterations grows gradually with training epochs, consistent with the operator norm of $J_{f_\theta}$ increasing as the model trains.

## Relevance to this research
The DEQ framework is directly relevant to the VFE transformer because the VFE-3 architecture is itself built around iterative minimization rather than layer-by-layer feedforward passes. The VFE E-step iterates belief updates $({\mu}, \Sigma, \phi)$ toward a free-energy minimum, which is structurally analogous to seeking a fixed point $z^\star = f_\theta(z^\star; x)$. The implicit-differentiation gradient formula in Theorem 1 is the formal justification for differentiating through any fixed-point solver without storing intermediate iterates — the same principle that allows backpropagation through VFE minimization loops. The universality theorem (a single equilibrium layer subsumes stacked equilibria) resonates with the VFE hierarchy collapsing to an effective single-level belief propagation at stationarity. Additionally, the Broyden quasi-Newton solver used in DEQs is a natural candidate for accelerating the inner-loop VFE E-step when the Jacobian of the belief-update map is expensive. The memory-efficiency argument is particularly salient for the VFE transformer running on an RTX 5090 with long sequences under full Gaussian (SPD) belief geometry.

## Cross-links
- Concepts: [[Fixed-Point Iteration]], [[Implicit Differentiation]], [[Attention Mechanism]]
- Related sources: [[vaswani2017attention]], [[dai2019transformerxl]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{bai2019deep,
  author    = {Bai, Shaojie and Kolter, J. Zico and Koltun, Vladlen},
  title     = {Deep Equilibrium Models},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2019},
}
```
