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
updated: 2026-09-23
---

# Entropic regularization

Entropic regularization adds a negative-entropy penalty to an optimization problem (canonically the optimal-transport linear program), making it strictly convex and solvable by the Sinkhorn-Knopp matrix-scaling iteration. This converts expensive transport LPs into fast, GPU-friendly fixed-point iterations, at the cost of a slightly blurred (smoothed) coupling controlled by the regularization weight. The same entropy-smoothing trick recurs across variational inference and softmax-style attention, linking it to the program's precision-weighted, geometry-aware computations.

In attention, the entropy-regularized problem over a single probability vector, without the target-marginal constraint of optimal transport, returns the softmax row with the temperature as the regularization weight ([[litman-2025-entropic-optimal-transport-attention]], Theorem 3.3; [[niculae-2017-regularized-attention]], Section 2.3). Replacing the entropy by a KL divergence to a prior adds $\log\pi$ to the logits ([[litman-2026-attention-priors]], Proposition 3.1). See [[Softmax]].

## Related
[[Optimal transport]], [[Variational free energy and predictive coding]]

## Sources
[[cuturi-2013-sinkhorn]], [[niculae-2017-regularized-attention]], [[litman-2025-entropic-optimal-transport-attention]], [[litman-2026-attention-priors]]
