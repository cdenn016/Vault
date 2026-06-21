---
type: concept
title: "Entropic regularization"
aliases:
  - "Sinkhorn regularization"
  - "Entropy-regularized optimal transport"
tags:
  - cluster/info-geometry
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Entropic regularization

Entropic regularization adds a negative-entropy penalty to an optimization problem (canonically the optimal-transport linear program), making it strictly convex and solvable by the Sinkhorn-Knopp matrix-scaling iteration. This converts expensive transport LPs into fast, GPU-friendly fixed-point iterations, at the cost of a slightly blurred (smoothed) coupling controlled by the regularization weight. The same entropy-smoothing trick recurs across variational inference and softmax-style attention, linking it to the program's precision-weighted, geometry-aware computations.

## Related
[[Optimal transport]], [[Variational free energy and predictive coding]]

## Sources
[[cuturi-2013-sinkhorn]]
