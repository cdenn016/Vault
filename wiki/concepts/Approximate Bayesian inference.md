---
type: concept
title: "Approximate Bayesian inference"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Approximate Bayesian inference

Approximate Bayesian inference encompasses methods for approximating intractable posterior distributions, including variational inference (minimizing KL to a tractable family), Monte Carlo dropout, Laplace approximations, and sampling (MCMC). It is the practical engine behind scalable Bayesian deep learning and is the lens through which dropout is reinterpreted as variational inference over network weights. Within the VFE program it is the same machinery as variational free-energy minimization, recast for posterior approximation over parameters or latent beliefs.

## Related
[[Variational free energy]], [[Gaussian process]], [[Amortized inference]]

## Sources
[[gal2016dropout]], [[blundell-2015-weight-uncertainty]]
