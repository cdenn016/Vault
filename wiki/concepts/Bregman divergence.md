---
type: concept
title: "Bregman divergence"
tags:
  - cluster/info-geometry
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Bregman divergence

A Bregman divergence D_F(x,y) = F(x) - F(y) - <grad F(y), x-y> is the difference between a strictly convex generator F and its first-order Taylor approximation at y. It generalizes squared Euclidean distance (F = ||.||^2) and KL divergence (F = negative entropy on the simplex), and underlies mirror descent, proximal methods, and the dual-flat structure of information geometry. In Hamiltonian/momentum optimization it supplies the Bregman-Lagrangian kinetic term that drives accelerated methods in non-Euclidean normed spaces.

## Related
[[kullback-1951-kl-divergence|KL divergence]], [[Alpha-divergence]], [[Information geometry and natural gradient]], [[Natural gradient]]

## Sources
[[diakonikolas2021momentum]]
