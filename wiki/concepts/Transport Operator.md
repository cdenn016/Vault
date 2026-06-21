---
type: concept
title: "Transport Operator"
tags:
  - cluster/gauge-theory
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Transport Operator

A transport operator is a linear map that carries a geometric or feature object from one point/frame to another while respecting an underlying symmetry, generalizing parallel transport along a connection. In equivariant deep learning (e.g. the SE(3)-Transformer) the operator mediating message passing between points must intertwine the group action, so that features transform consistently under rotations and translations; concretely it is built from steerable kernels and Wigner-D matrices acting on irreducible-representation features. This is the discrete attention-mechanism analogue of gauge parallel transport in the gauge-theoretic VFE program.

## Related
[[Parallel transport]], [[Holonomy]], [[Gauge equivariance]]

## Sources
[[fuchs-2020-se3-transformer]]
