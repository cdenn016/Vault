---
type: concept
title: "Implicit differentiation"
aliases:
  - "implicitdifferentiation"
  - "Implicit function theorem"
tags:
  - cluster/vfe
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Implicit differentiation

A technique, grounded in the implicit function theorem, for differentiating through an equation g(z, x) = 0 that defines z implicitly as a function of x, without an explicit closed form. In deep equilibrium models it gives exact gradients of the fixed point z*(x) by solving a single linear system involving the Jacobian at equilibrium, enabling O(1)-memory backpropagation through an effectively infinite-depth iterative solver.

## Related
[[Fixed-point iteration]], [[Natural gradient]]

## Sources
[[bai2019deep-equilibrium]]
