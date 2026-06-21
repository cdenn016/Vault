---
type: concept
title: "Fixed-point iteration"
aliases:
  - "fixedpointiteration"
  - "Fixed point iteration"
tags:
  - cluster/vfe
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Fixed-point iteration

An iterative scheme that finds a solution z* of z = f(z) by repeatedly applying the map z_{k+1} = f(z_k) until convergence, guaranteed when f is a contraction (Banach fixed-point theorem). In deep equilibrium models the forward pass is itself a fixed-point solve of a layer's equilibrium equation rather than a fixed stack of layers, linking implicit-depth networks to iterative inference and to the converged solutions of variational belief updates.

## Related
[[Amortized inference]], [[Variational free energy]]

## Sources
[[bai2019deep-equilibrium]]
