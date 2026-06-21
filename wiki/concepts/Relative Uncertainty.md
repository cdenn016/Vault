---
type: concept
title: "Relative Uncertainty"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/multi-agent
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Relative Uncertainty

Relative uncertainty (RU), tau_t, is the fraction of total predictive uncertainty attributable to imprecision in the agent's current estimate rather than to irreducible observation noise — a Kalman-filter-like quantity. It is the second normative driver of the adaptive learning rate alpha_t = Omega_t + (1 - Omega_t) tau_t: when the belief is uncertain, new evidence is weighted more heavily. RU maps onto the variance Sigma of the Gaussian belief tuple in the VFE model and dissociates neurally (anterior PFC / parietal) from the surprise-driven change-point signal.

## Related
[[Change-Point Detection]], [[Bayesian Belief Updating]], [[Variational Free Energy]], [[Mass as Fisher information]]

## Sources
[[mcguire2014-adaptive-learning]], [[nassar2010-approximately-bayesian]]
