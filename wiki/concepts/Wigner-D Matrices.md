---
type: concept
title: "Wigner-D Matrices"
aliases:
  - "Wigner D-matrices"
  - "Wigner D matrix"
tags:
  - cluster/gauge-theory
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Wigner-D Matrices

The Wigner D-matrices are the irreducible unitary representations of the rotation group SO(3) (and SU(2)): for each angular-momentum degree l they give a (2l+1)x(2l+1) matrix D^l(R) describing how spherical-harmonic / type-l feature vectors rotate under R. They are the building blocks of steerable and equivariant networks - the SE(3)-Transformer rotates its type-l features by D^l(R) so that attention and message passing are exactly SO(3)-equivariant - making them the concrete representation-theoretic machinery behind gauge/rotation equivariance in this program.

## Related
[[Group equivariance|Gauge equivariance]], [[Spherical harmonics]], `SO(3)`

## Sources
[[fuchs-2020-se3-transformer]], [[cohen-2018-spherical-cnns]]
