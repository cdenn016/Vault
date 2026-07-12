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
updated: 2026-07-12
---

# Fixed-point iteration

A fixed-point iteration applies $z_{n+1}=f(z_n)$ in search of a state $z^\ast=f(z^\ast)$. If $f$
is a contraction on a complete invariant metric space, Banach's theorem gives existence,
uniqueness, and geometric convergence. Brouwer's theorem gives existence for a continuous self-map
of a compact convex set but gives neither uniqueness nor convergence of the iteration. Keeping these
results separate matters in iterative variational inference.

In deep equilibrium models the forward pass solves a layer equilibrium rather than evaluating a
fixed stack, linking implicit depth to repeated belief refinement. The VFE programs use finite
unrolled structural updates in their deployed routes; a stationary point or continuous response map
does not by itself make those finite schedules convergent fixed-point solvers.

## PIFB2 fixed-point status

At zero raw within-scale coupling, the finite cross-scale PIFB2 Gaussian tree has an SPD stacked
precision. Its mean-field coordinate updates are Gauss-Seidel sweeps and converge to a unique
optimum. This is the exact [[Hierarchical generative model]] regime.

For the within-scale finite-state construction, positive source floors make the geometric-pooling
response continuous on a compact product simplex, so a self-consistent equilibrium exists by
Brouwer. For frozen covariances and attention weights with orthogonal transports, an anchored mean
map has neighbor-operator norm strictly below one. Assuming a complete invariant set, Banach then
supplies global convergence within that frozen restricted subsystem.

The live state-dependent softmax system with unrestricted $\mathrm{GL}^+(K)$ frames is outside
those proofs. Noncompact frame directions defeat the direct compactness argument, and attention,
covariance, and frame responses alter the contraction constant. Existence of a restricted symmetric
mean stationary point does not establish a fixed point of every coordinate. Global existence,
uniqueness, and convergence of the fully coupled Gaussian gauge iteration remain open.
[[vfe-population-generative-status-2026-07-12]]

## Related

[[Amortized inference]], [[Variational free energy]], [[Natural gradient]],
[[Hierarchical generative model]]

## Sources

- [[bai2019deep-equilibrium]]
- [[participatory-it-from-bit]]
- [[vfe-population-generative-status-2026-07-12]]
