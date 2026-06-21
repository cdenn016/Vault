---
type: concept
title: "Schild's Ladder"
aliases:
  - "Schilds Ladder"
  - "schildsladder"
tags:
  - cluster/spd-geometry
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Schild's Ladder

Schild's ladder is a first-order numerical scheme for approximating parallel transport of a vector along a curve on a manifold using only geodesics and midpoints, without needing the Christoffel symbols of the connection explicitly. By iterating a construction of geodesic parallelograms ('rungs'), it transports a tangent vector step by step along a path, making it a practical discretization of parallel transport on curved spaces such as the SPD covariance manifold. It connects to the program's use of connections, holonomy, and gauge transport of beliefs across positions/layers.

## Related
[[Parallel transport]], [[Holonomy]], [[SPD-manifold geometry and Riemannian optimization]], [[Riemannian geometry|Riemannian Manifold]]

## Sources
[[sengupta2017gauge]], [[docarmo-1992-riemannian-geometry]]
