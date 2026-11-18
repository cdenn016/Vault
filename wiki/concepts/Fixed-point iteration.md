---
type: concept
title: "Fixed-point iteration"
aliases:
  - "fixedpointiteration"
  - "Fixed point iteration"
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-11-18
---

# Fixed-point iteration

A fixed-point iteration applies $z_{n+1}=f(z_n)$ in search of a state $z^\ast=f(z^\ast)$. If $f$
is a contraction on a complete invariant metric space, Banach's theorem gives existence,
uniqueness, and geometric convergence. Brouwer's theorem gives existence for a continuous self-map
of a compact convex set but gives neither uniqueness nor convergence of the iteration. Keeping these
results separate matters in iterative variational inference.

In deep equilibrium models the forward pass solves a layer equilibrium rather than evaluating a
fixed stack, linking implicit depth to repeated belief refinement. The VFE transformer uses finite
unrolled structural updates in its deployed routes; a stationary point or continuous response map
does not by itself make those finite schedules convergent fixed-point solvers.

## Related

[[Amortized inference]], [[Variational free energy]], [[Natural gradient]],
[[Hierarchical generative model]]

## Sources

- [[bai2019deep-equilibrium]]
