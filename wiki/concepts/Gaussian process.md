---
type: concept
title: "Gaussian process"
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Gaussian process

A Gaussian process (GP) is a distribution over functions such that any finite set of function values is jointly Gaussian, fully specified by a mean and covariance (kernel) function. GPs provide a nonparametric Bayesian model with calibrated predictive uncertainty. They are central to Gal & Ghahramani's interpretation of dropout as approximate Bayesian inference: a deep network with dropout is shown to be mathematically equivalent to a variational approximation to a deep Gaussian process, connecting GP uncertainty to practical neural-network regularization.

## Related
[[Approximate Bayesian inference]], [[Variational free energy]], [[Amortized inference]]

## Sources
[[gal2016dropout]]
