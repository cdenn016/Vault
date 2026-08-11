---
type: concept
title: "Singular statistical models"
aliases:
  - "Singular learning models"
  - "Statistical singularities"
tags:
  - cluster/info-geometry
  - cluster/vfe
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-08-10
updated: 2026-08-10
---

# Singular statistical models

## Definition

A **singular statistical model** is a parameterized family in which the map from parameters to probability laws fails to be locally identifiable at some points. Equivalent parameters, redundant hidden units, component collisions, or changing stabilizers can make the [[Fisher information metric|Fisher information]] rank deficient. At such points the parameter space is not described by one regular positive-definite Fisher metric and one ordinary quadratic likelihood expansion.

## Why it matters here

Gauge orbits and latent meta-agent symmetries can generate exactly this distinction between parameter coordinates and identifiable laws. Quotienting the null tangent directions can give a useful local identifiable geometry, but it does not automatically produce a smooth global quotient. Stabilizers may change, orbit dimensions may jump, and the quotient may need a stratified rather than a manifold description.

## Details

### Nonidentifiability and Fisher degeneracy

If $p_{\theta}=p_{\theta'}$ for distinct nearby parameters, movement along the equivalent-parameter direction changes no law and has zero Fisher length. A Moore-Penrose inverse can define a minimum-norm step on a selected identifiable tangent subspace, but regular natural-gradient and asymptotic arguments must state how that subspace varies.

### Learning consequences

[[watanabe-2002-singularities]] studies a concrete hidden-variable setting and shows that regular relations between training and generalization error can fail even when the true parameter is near rather than exactly on a singularity. The paper is evidence that regular asymptotics are unsafe near singular strata; it is not, by itself, a theorem about every gauge quotient or latent-agent architecture.

### Geometric obligations

To replace a singular parameterization by a regular quotient manifold, one still needs an appropriate group action and proofs of freeness/properness or a controlled stratification, a well-behaved quotient topology, and descent of the statistical tensors. A local rank calculation does not close those obligations.

## In this work

The finite information-history machinery uses identifiable tangent directions and pseudoinverses as diagnostics. This is compatible with singular-model awareness, but it should not be reported as a proof that the full passive-frame or coarse-history quotient is free, proper, Hausdorff, or globally smooth. [[ay-2025-natural-gradient-elbo]] adds a related warning: constrained ELBO and target-KL natural gradients agree only under additional geometric compatibility.

## Sources

- [[watanabe-2002-singularities]]
- [[ay-2025-natural-gradient-elbo]]

## See also

- [[Fisher information metric]]
- [[Statistical manifold]]
- [[Natural gradient]]
- [[Model Complexity]]
- [[Meta-agents and hierarchical emergence]]
