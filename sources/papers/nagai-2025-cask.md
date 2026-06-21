---
type: paper
title: "CASK: A Gauge Covariant Transformer for Lattice Gauge Theory"
aliases:
  - "Nagai 2025"
  - "CASK"
authors:
  - Nagai, Yuki
  - Ohno, Hiroshi
  - Tomiya, Akio
year: 2025
arxiv: "2501.16955"
url: https://arxiv.org/abs/2501.16955
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/physics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# CASK: A Gauge Covariant Transformer for Lattice Gauge Theory

> [!info] Citation
> Nagai, Y., Ohno, H., and Tomiya, A. (2025). "CASK: A Gauge Covariant Transformer for Lattice Gauge Theory." The 41st International Symposium on Lattice Field Theory (LATTICE2024), PoS. arXiv:2501.16955 [hep-lat].

## TL;DR
CASK (Covariant Attention with Stout Kernel) is a Transformer architecture for lattice QCD that is gauge covariant/equivariant and spacetime-symmetry equivariant by construction. The attention matrix is built from Frobenius inner products between smeared link variables (queries/keys) and extended staples (Wilson loops), making it gauge-invariant and hence the full architecture gauge covariant. CASK outperforms gauge covariant convolutional networks in self-learning Hybrid Monte Carlo (SLHMC) simulations of SU(2) lattice gauge theory with dynamical fermions.

## Problem & setting
Lattice QCD simulations are computationally expensive, motivating the use of neural surrogate models. However, such models must respect gauge symmetry (a local symmetry under SU(N_c) transformations) and spacetime symmetry, must be fermion-friendly, and must be fully differentiable for gradient-based training. Prior gauge-covariant neural networks (based on stout smearing / residual flows) capture only local/convolutional correlations; extending these to a Transformer with non-local (all-to-all) attention while preserving exact gauge covariance is the central challenge.

## Method
The key construction is a gauge-invariant attention matrix built from the Frobenius inner product tr(A†B), which is invariant under A → ω₁Aω₂ and B → ω₁Bω₂ for ω₁, ω₂ ∈ SU(N_c). Query, key, and value gauge links U^(Q), U^(K), U^(V) are produced by independent stout-type gauge covariant smearing layers with trainable weights ρ^(α). The attention weight between link U^(Q)_μ(n) and link U^(K) along a rectangular Wilson loop of size s is:

ã_{n,μ,ν,s} = Re Tr[U^(Q)_μ(n) V_{ν,n+μ̂;s}({U^(K)})] − Re Tr[U_μ(n) V_{ν,n+μ̂;s}({U})]

with a_{n,μ,ν,s} = tan(4/N_c · ã_{n,μ,ν,s}) for signal amplification. In practice sparse attention is used (1×1, 1×2, 1×3 rectangular Wilson loops). The CASK update rule is an exponential map update U^(l+1) = e^{iQ^A} U^(l), analogous to stout smearing but driven by the attention-weighted sum over value links. Training uses backpropagation adapted for matrix-valued (SU(N_c)) variables, with the Adam optimizer.

The design is motivated by the O(3) equivariant Transformer for spin systems (Nagai & Tomiya 2024), where the attention matrix is an inner product of block-spin queries and keys — here upgraded from global O(3) to local gauge symmetry by replacing inner products with Wilson-loop traces.

## Key results
On a 4^4 SU(2) lattice at β = 2.7 with naive staggered fermions (mass m = 0.3), CASK is used in SLHMC where the effective action employs m_eff = 0.4 and CASK smeared links. Without any training the acceptance rate is nearly zero; after training, CASK achieves a systematically higher acceptance rate and lower loss than the gauge covariant convolutional network ("adaptive stout"), and continues improving at late epochs where CovNet saturates. Physical observables (plaquette distribution) remain consistent with the exact theory throughout, confirming the surrogate action does not distort physics.

## Relevance to this research
CASK is a direct analog in lattice-QCD language of the GL(K) gauge-equivariant attention developed in the VFE transformer program. Both build gauge-invariant attention weights from inner products that are invariant under the local group action, then use those weights to transport and aggregate "value" objects covariantl. Key structural parallels: (1) CASK's Frobenius inner product tr(U^(Q)†U^(K)·staple) as gauge-invariant attention score maps precisely onto the VFE program's parallel-transport inner product used to form β_{ij}; (2) CASK's update rule (exponential map driven by attention-weighted values) mirrors the VFE Ω_{ij}-transport used to couple beliefs; (3) CASK's sparse Wilson-loop attention is a physics instantiation of the locality structure that the VFE framework accommodates via the sparsity of the transport graph. CASK provides an existence proof and empirical validation that gauge-equivariant Transformer attention can outperform purely convolutional gauge-equivariant architectures, directly supporting the motivation for the GL(K) attention architecture.

## Cross-links
- Concepts: [[Group equivariance|Gauge Equivariance]], [[Attention Mechanism]], [[Lattice gauge theory|Wilson Loop]], [[Parallel Transport]]
- Related sources: [[kanwar-2020-equivariant-flow]] [[boyda-2021-su-n-flows]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) gauge-equivariant attention|GL(K) Attention]]

## BibTeX
```bibtex
@article{nagai2025cask,
  author  = {Nagai, Yuki and Ohno, Hiroshi and Tomiya, Akio},
  title   = {{CASK}: A Gauge Covariant Transformer for Lattice Gauge Theory},
  year    = {2025},
  eprint  = {2501.16955},
  archivePrefix = {arXiv},
  primaryClass  = {hep-lat},
  note    = {Talk at LATTICE2024, PoS},
}
```
