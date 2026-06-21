---
type: concept
title: "Optimal transport"
aliases:
  - "Wasserstein distance"
  - "Earth mover's distance"
  - "Monge-Kantorovich problem"
tags:
  - cluster/info-geometry
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Optimal transport

Optimal transport (the Monge-Kantorovich problem) seeks the cheapest coupling that moves one probability measure onto another given a ground cost, yielding the Wasserstein distances as a geometry on probability distributions. Unlike pointwise divergences it accounts for the metric on the underlying space, making it natural for comparing belief distributions and for geometry-aware attention affinities. Entropic regularization (the Sinkhorn variant) makes it efficiently computable; it is distinct from parallel transport, which moves vectors along a connection.

## Related
[[Entropic regularization]], [[Information geometry and natural gradient]], [[Fisher information metric]]

## Sources
[[cuturi-2013-sinkhorn]], [[villani-2009-optimal-transport]]
