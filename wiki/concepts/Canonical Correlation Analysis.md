---
type: concept
title: "Canonical Correlation Analysis"
aliases:
  - "CCA"
tags:
  - cluster/info-geometry
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Canonical Correlation Analysis

Canonical Correlation Analysis (CCA, Hotelling 1936) finds pairs of linear projections of two random vectors that are maximally correlated, yielding the canonical directions and canonical correlations. For jointly Gaussian variables it is the exact solution of the Gaussian Information Bottleneck: the IB-relevant projection coincides with the leading canonical directions, so CCA is the linear, second-order realization of relevance-preserving compression.

## Reduced-rank regression, October 2, 2026

The canonical correlations are the singular values of the whitened cross-covariance $\Sigma_{ii}^{-1/2}\Sigma_{ij}\Sigma_{jj}^{-1/2}$, and the best rank-$d$ linear predictor of $\xi_i$ from $\xi_j$ in the whitened norm is reduced-rank regression, with excess risk over the full regression equal to the sum of squared discarded canonical correlations ([[dennis-2026-link-curvature]], citing Izenman 1975). The note proposes reading the low-rank channel $OT$ of the projected attention routes as an amortized version of this solution; that identification is a hypothesis to test.

## Related
[[Information bottleneck]], [[Fisher information metric]], [[Variational autoencoder (VAE)]]

## Sources
[[chechik2005information-bottleneck-gaussian]]
