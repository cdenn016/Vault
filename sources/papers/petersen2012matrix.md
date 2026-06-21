---
type: paper
title: "The Matrix Cookbook"
aliases:
  - "Petersen 2012"
  - "Matrix Cookbook"
authors:
  - Petersen, Kaare Brandt
  - Pedersen, Michael Syskind
year: 2012
arxiv: null
url: https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The Matrix Cookbook

> [!info] Citation
> Petersen, Kaare Brandt and Pedersen, Michael Syskind (2012). "The Matrix Cookbook." Technical University of Denmark. Version November 15, 2012. https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf

## TL;DR
A freely distributed technical reference compiling identities, derivatives, and decompositions for matrices and matrix-valued functions. It is the standard desk reference for matrix calculus in machine learning, statistics, and applied mathematics, covering topics from basic products and inverses to matrix exponentials, Gaussian integrals, and Kronecker products. It does not prove results but provides organized, citable formula tables.

## Problem & setting
Researchers in ML, statistics, and engineering frequently need matrix derivative identities (gradients of traces, determinants, quadratic forms, etc.) and cannot easily look them up in standard calculus texts. Prior to this compendium such identities were scattered across textbooks on linear algebra, numerical analysis, and statistics. The cookbook assembles them in one indexed reference, versioned and updated by the authors over many years.

## Method
The document is an annotated formula compendium, not an algorithmic paper. It is organized into chapters covering: basic algebra and products; complex matrices; Kronecker and Hadamard products; matrix norms; functions of matrices (exponential, logarithm, square root); matrix derivatives (including the vec operator and chain rule for matrix functions); decompositions (SVD, eigendecomposition, Cholesky); statistics of Gaussians (expectations, conditional distributions, the Woodbury identity, matrix-normal and Wishart distributions); and transforms. Proofs are generally omitted; results are stated with references.

## Key results
Key identities directly relevant to the VFE transformer include: derivatives of quadratic forms $\partial_x (x^T A x) = (A + A^T)x$ and log-determinants $\partial_A \log|A| = A^{-T}$; the matrix inversion lemma (Woodbury identity) $(A + UCV)^{-1} = A^{-1} - A^{-1}U(C^{-1}+VA^{-1}U)^{-1}VA^{-1}$; derivatives through matrix exponentials; Kronecker product identities; and the entropy and KL divergence for the multivariate Gaussian $\mathcal{N}(\mu, \Sigma)$. The Gaussian section (Chapter 8) gives closed-form conditionals and marginals used throughout Bayesian and variational inference.

## Relevance to this research
This is a low-level utility reference that underpins virtually every matrix calculation in the VFE transformer codebase and manuscripts. Specifically: (1) derivatives of $\log|\Sigma|$ and quadratic forms in $\Sigma^{-1}$ appear directly in the VFE free-energy gradient $\nabla_\Sigma F$ used in the M-step / belief update; (2) the Woodbury identity appears whenever the $(K \times K)$ precision matrix is updated with a rank-1 or rank-$r$ correction during E-step coupling; (3) the matrix exponential identities are relevant to the GL(K) transport / parallel transport computation $\Omega_{ij} = \exp(\Delta_{ij})$; (4) Gaussian marginal and conditional identities underpin the SPD belief geometry and the derivation of the KL divergence between Gaussians used throughout the free-energy functional. The GL(K) attention manuscript (`Manuscripts-Theory/GL(K)_attention.tex`) and the supplementary implicitly rely on these results in every gradient derivation.

## Cross-links
- Concepts: [[Matrix calculus]], [[SPD-manifold geometry and Riemannian optimization|SPD manifold]], [[Gaussian beliefs]], [[kullback-1951-kl-divergence|KL divergence]]
- Related sources: [[bhatia-2007-positive-definite-matrices]], [[absil-2008-optimization-matrix-manifolds]], [[amari-2000-methods-information-geometry]], [[pennec-2006-affine-invariant-tensor]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@techreport{petersen2012matrix,
  author      = {Petersen, Kaare Brandt and Pedersen, Michael Syskind},
  title       = {The Matrix Cookbook},
  institution = {Technical University of Denmark},
  year        = {2012},
  note        = {Version November 15, 2012},
  url         = {https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf},
}
```
