---
type: concept
title: "Laplace approximation"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Laplace approximation

The Laplace approximation models an intractable posterior as a Gaussian centered at the maximum a posteriori (MAP) estimate, with covariance equal to the inverse Hessian (observed Fisher information) of the negative log-posterior at that mode. It yields a closed-form log-evidence (marginal likelihood) approximation whose leading terms recover the BIC penalty (Schwarz 1978), and it is the workhorse that turns variational free energy into a tractable, Gaussian-belief scheme in dynamic expectation maximization (Friston 2008). In the VFE program it justifies the Gaussian-belief parameterization (mu, Sigma) and connects model evidence to the Fisher-information geometry of beliefs.

## Related
[[Variational free energy]], [[Fisher information metric]], [[Predictive coding network]]

## Sources
[[friston-2008-dem]], [[schwarz-1978-bic]]
