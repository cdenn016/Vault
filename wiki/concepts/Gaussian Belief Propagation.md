---
type: concept
title: "Gaussian Belief Propagation"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Gaussian Belief Propagation

Gaussian belief propagation (GaBP) is the specialization of the sum-product message-passing algorithm to Gaussian graphical models (Gaussian Markov random fields). Because all messages and beliefs stay Gaussian, each is summarized by a mean and precision (or covariance), and the updates reduce to closed-form linear-algebraic operations that, on tree-structured graphs, converge exactly to the marginal means and (locally) the marginal variances of a joint Gaussian — equivalently solving a sparse linear system Ax=b. On loopy graphs it is an iterative approximate inference scheme whose fixed points recover the correct posterior means when it converges. It is the natural inference primitive for distributed precision-weighted belief updating, linking probabilistic-population-coding and predictive-coding accounts of cortical inference to the program's precision-weighted attention.

## Related
[[Variational free energy]], [[Precision-weighted attention]], [[Predictive coding]]

## Sources
[[pouget-2013-probabilistic-brains]]
