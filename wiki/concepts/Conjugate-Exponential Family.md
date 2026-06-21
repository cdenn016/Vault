---
type: concept
title: "Conjugate-Exponential Family"
aliases:
  - "Conjugate Exponential Family"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Conjugate-Exponential Family

A conjugate-exponential model is a latent-variable model in which the complete-data likelihood is in the exponential family and the prior over parameters is its conjugate prior, also exponential-family. Beal (2003) shows this is the structural condition under which Variational Bayesian EM yields closed-form, tractable update equations: the variational posteriors stay in the same exponential family, and the VBEM updates generalize ordinary EM. The exponential-family form ties directly into information geometry (natural vs. expectation parameters, the Fisher metric) underpinning natural-gradient variational inference.

## Related
[[Variational free energy]], [[Amortized variational inference]], [[Fisher information metric]], [[Natural gradient]]

## Sources
[[beal-2003-variational-bayesian]], [[wainwright-jordan-2008-graphical-models-variational-inference]]
