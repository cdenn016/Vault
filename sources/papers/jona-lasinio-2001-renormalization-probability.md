---
type: paper
title: "Renormalization Group and Probability Theory"
aliases:
  - "Jona-Lasinio 2001"
  - "RG and Probability"
authors:
  - Jona-Lasinio, G.
year: 2001
arxiv: cond-mat/0009219
url: https://arxiv.org/abs/cond-mat/0009219
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/physics
  - field/mathematics
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Renormalization Group and Probability Theory

> [!info] Citation
> Jona-Lasinio, G. (2001). "Renormalization Group and Probability Theory." *Physics Reports* 352, 439–458. arXiv:cond-mat/0009219.

## TL;DR
This paper provides a concise probabilistic interpretation of the renormalization group (RG), showing that the RG is fundamentally a theory of limit theorems for strongly correlated random variables. The Central Limit Theorem emerges as convergence to a Gaussian fixed point of a renormalization transformation, and critical universality at phase transitions corresponds to new, non-Gaussian fixed points governing the large-scale statistics of strongly correlated fields. The paper synthesizes results from 1975–1985 on the connections between RG fixed points, self-similar random fields, and critical indices.

## Problem & setting
The renormalization group was developed to explain universality and scaling laws near critical points of phase transitions. While standard probability theory (CLT) governs weakly correlated systems converging to Gaussian distributions, strongly correlated systems near criticality require new limit theorems. The paper asks: what is the probabilistic content of RG fixed points and critical universality? Prior work (Bleher–Sinai, Wilson, Kadanoff) had noted the connection informally; this paper synthesizes the rigorous probabilistic framework developed by Sinai, Gallavotti, Jona-Lasinio and collaborators during 1975–1985.

## Method
The approach recasts RG transformations as nonlinear maps on probability distributions. A renormalization transformation $R$ acts on distributions $p_n$ via block-spin averaging and rescaling:
$$p_{n+1}(x) = (Rp_n)(x) = \sqrt{2}\int dy\, p_n(\sqrt{2}x - y)\,p_n(y)$$
Fixed points of $R$ are stable distributions; the Gaussian family $p_{G,\sigma}$ forms one class of fixed points. Stability analysis uses linearization: writing $p_\eta = p_G(1 + \eta h)$ and computing the linearized operator $L$ with eigenvalues $\lambda_k = 2^{1-k/2}$ and Hermite polynomial eigenfunctions. Since $\lambda_k < 1$ for $k > 2$, all non-Gaussian perturbations (beyond centering and variance) contract to zero, proving the CLT as a stable-manifold theorem.

For hierarchical models with ferromagnetic dependence, the modified transformation $\hat{R}$ introduces an exponential coupling $g_n(x^2) = L_n e^{\beta(c/2)^n x^2}$ and the Gaussian fixed point can lose stability when $c < 2^{1/2}$, forcing a bifurcation to a non-Gaussian fixed point $p_{NG}(x) \approx e^{-r^*(ε)x^2/2 - u^*(ε)x^4/4}$. Critical indices such as the susceptibility exponent are given by ratios of logarithms of the rescaling parameter $c$ and the unstable eigenvalue $\lambda$: $\nu_\chi = \log(c/2)/\log\lambda$.

For self-similar random fields on $\mathbb{Z}^d$, the linearized RG at a Gaussian fixed point acts as a conditional expectation $E(h|\{\xi^n_j\})$, with eigenvectors being infinite-dimensional Hermite polynomial generalizations satisfying $E(H_k|\{\xi^n_j\}) = n^{[k(\alpha/2-1)+1]d} H_k(\{\xi^n_j\})$.

## Key results
Fixed points of the renormalization transformation on probability distributions correspond exactly to universality classes of statistical mechanical systems. The CLT is the simplest instance: the Gaussian is an attracting fixed point, and convergence to it is governed by the spectral gap of the linearized RG operator (all eigenvalues below unity for $k > 2$ Hermite components). At a critical temperature $\beta_{cr}$, variance diverges under standard normalization, requiring anomalous rescaling $\sum \xi_i / 2^{n(c/2)^{n/2}}$, and the critical manifold is a non-trivial submanifold in the space of probability distributions. Non-Gaussian fixed points (of $\phi^4$-type) exist for hierarchical models with $c < 2^{1/2}$, obtained by bifurcation from the unstable Gaussian, and have non-empty domains of attraction. The susceptibility critical index is $\nu_\chi = \log(c/2)/\log\lambda$ where $\lambda$ is the lone unstable eigenvalue of the linearized RG at the non-Gaussian fixed point.

## Relevance to this research
The probabilistic RG framework has several structural parallels with the VFE transformer program. The fixed-point / domain-of-attraction structure mirrors the belief-state convergence under iterated VFE minimization: both identify a manifold of stationary distributions (Gaussian beliefs in the SPD geometry) that are attractors under a contraction map. The linearized RG operator, acting via conditional expectations on function spaces, is closely analogous to the attention mechanism as a conditional-expectation operator in the GL(K) equivariant attention framework. The role of Hermite polynomial eigenfunctions in the RG spectral theory connects to the irrep decomposition underlying the GL(K) gauge structure. The anomalous scaling at criticality (departure from Gaussian fixed points) is conceptually related to the non-Gaussian generalized families (Student-t, exponential power) considered as belief distributions in the VFE hierarchy. More broadly, the paper provides a mathematical foundation for understanding universality in hierarchical probabilistic models, which is the formal setting of the VFE hyper-prior hierarchy $h \to s \to p \to q \to \text{observations}$.

## Cross-links
- Concepts: [[Renormalization group flow|Renormalization Group]], [[Central Limit Theorem]], [[Fixed Points]], [[Information Geometry]], [[Gaussian Beliefs]]
- Related sources: [[sinai-1982-theory-phase-transitions]], [[wilson-1971-rg-critical-phenomena|wilson-1971-renormalization-group]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) gauge-equivariant attention|GL(K) Attention]]

## BibTeX
```bibtex
@article{JonaLasinio2001,
  author  = {Jona-Lasinio, G.},
  title   = {Renormalization Group and Probability Theory},
  journal = {Physics Reports},
  volume  = {352},
  pages   = {439--458},
  year    = {2001},
  eprint  = {cond-mat/0009219},
  archivePrefix = {arXiv},
}
```
