---
type: concept
title: "Exponential map (Riemannian)"
aliases:
  - "Exponential Map"
tags:
  - cluster/spd-geometry
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Exponential map (Riemannian)

The exponential map of a Riemannian manifold sends a tangent vector at a point to the endpoint of the geodesic that starts at that point with that initial velocity, providing the canonical local chart (normal coordinates) and the inverse of the logarithm map. On the SPD cone under the affine-invariant metric it has the closed form exp_Sigma(V) = Sigma^{1/2} expm(Sigma^{-1/2} V Sigma^{-1/2}) Sigma^{1/2}; on a Lie group it coincides with the matrix/group exponential. In practice it is the exact geodesic step that retractions cheaply approximate, and it underlies both SPD-covariance updates and the GL(k) gauge-frame map exp(phi) in this program.

## Related
[[SPD-manifold geometry and Riemannian optimization]], [[Parallel transport]], [[karcher-1977-center-of-mass|Karcher mean]], [[Symmetric spaces and the SPD cone]], [[Baker-Campbell-Hausdorff formula]]

## Sources
[[pennec-2009-riemannian-computing]], [[docarmo-1992-riemannian-geometry|do carmo (1992) riemannian geometry]], [[karcher-1977-center-of-mass]]
