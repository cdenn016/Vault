---
type: paper
title: "Deep Learning and the Information Bottleneck Principle"
aliases:
  - "Tishby 2015"
  - "Deep IB"
authors:
  - Tishby, Naftali
  - Zaslavsky, Noga
year: 2015
arxiv: "1503.02406"
url: https://arxiv.org/abs/1503.02406
tags:
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/statistics
  - field/physics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Deep Learning and the Information Bottleneck Principle

> [!info] Citation
> Tishby, N. & Zaslavsky, N. (2015). "Deep Learning and the Information Bottleneck Principle." arXiv:1503.02406 [cs.LG].

## TL;DR
This paper proposes analyzing deep neural networks through the lens of the Information Bottleneck (IB) principle, treating each layer as a point on an information plane defined by compression (I(X; h)) versus prediction (I(Y; h)). The optimal DNN architecture — number of layers and units per layer — is conjectured to be determined by the bifurcation points of the IB tradeoff curve, which correspond to structural phase transitions in the data distribution. Finite-sample generalization bounds are derived from the IB framework, providing a theoretically grounded optimality criterion for each hidden layer.

## Problem & setting
Deep Neural Networks achieve remarkable empirical success, yet the theoretical principles governing their design — optimal depth, width, and architecture — remain poorly understood. Prior work (Mehta & Schwab, 2014) established a mapping between variational renormalization group transformations and RBM-based DNNs, but this does not extend to general architectures. The paper seeks a unified, architecture-agnostic information-theoretic framework that can quantify the efficiency of any DNN and provide generalization guarantees.

## Method
The DNN layers form a Markov chain X → h_1 → h_2 → ... → h_m → Ŷ. By the Data Processing Inequality (DPI), information about Y can only be lost as one moves up the hierarchy: I(Y;X) ≥ I(Y;h_j) ≥ I(Y;h_i) ≥ I(Y;Ŷ) for i ≥ j. Each layer h_k is placed on an information plane with axes R = I(h_{k-1}; h_k) (compression/complexity) and I_Y = I(Y; h_k) (relevance/prediction).

The Information Bottleneck Lagrangian for extracting the relevant compression X̂ of X with respect to Y is:

L[p(x̂|x)] = I(X; X̂) - β I(X̂; Y)

with self-consistent optimal solutions of the form p(x̂|x) ∝ p(x̂) exp(-β D_KL[p(y|x) ‖ p(y|x̂)]). The parameter β traces the IB curve and its inverse slope; bifurcation points on this curve correspond to second-order phase transitions governed by the largest eigenvalue of the conditional second-order correlations of p(X,Y|X̂(β)).

Finite-sample generalization bounds from Shamir et al. (2010) bound the true mutual informations from above by their empirical estimates plus O(K|Y|/√n) and O(K/√n), where K = |X̂| ≈ 2^{I(X̂;X)} is the effective description length. This defines an optimal finite-sample operating point (R*(n), D*_IB(n)) on the empirical IB curve that minimizes worst-case generalization error.

## Key results
The IB distortion measure enables evaluation of individual hidden layers (not just the output), comparing each to the theoretical IB limit at the corresponding β. Two quantitative gaps are defined: the generalization gap ΔG = D_N - D*_IB(n) (information about Y not captured by the network) and the complexity gap ΔC = R_N - R*(n) (unnecessary representational complexity). The paper conjectures that optimal DNN layer placement occurs just after the bifurcation transitions on the IB curve, since the bifurcation critical values of β coincide with the breakdown of linear separability — both are determined by the same spectral property (largest eigenvalue of second-order conditional correlations). Stochastic layer mappings are shown to be theoretically required to approach the optimal IB limit.

## Relevance to this research
The IB principle connects directly to the VFE transformer framework in several ways. The free energy functional in this research program balances compression (KL divergences penalizing deviation from priors) against prediction (observation likelihood), which is structurally isomorphic to the IB tradeoff L = I(X;X̂) - β I(X̂;Y). The Markovian hierarchy X → h_1 → ... → Ŷ mirrors the VFE hierarchy h → s → p → q → observations. The role of KL divergence as the IB distortion measure d_IB(x,x̂) = D_KL[p(y|x) ‖ p(y|x̂)] is the same divergence used throughout the VFE belief-coupling terms. The IB phase transitions and their spectral characterization (second-order correlations, eigenvalue bifurcations) are reminiscent of the GL(K) gauge structure and the role of the SPD belief covariance Σ in organizing representations. The finite-sample complexity argument (compression is necessary for generalization) aligns with the VFE prior-bank regularization that prevents beliefs from collapsing to arbitrary precision.

## Cross-links
- Concepts: [[Information Bottleneck]], [[Mutual Information]], [[kullback-1951-kl-divergence|KL Divergence]], [[Data Processing Inequality]]
- Related sources: [[tishby-1999-information-bottleneck]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) gauge-equivariant attention|GL(K) Attention]]

## BibTeX
```bibtex
@article{tishby2015deep,
  author  = {Tishby, Naftali and Zaslavsky, Noga},
  title   = {Deep Learning and the Information Bottleneck Principle},
  journal = {arXiv preprint arXiv:1503.02406},
  year    = {2015},
  url     = {https://arxiv.org/abs/1503.02406},
}
```
