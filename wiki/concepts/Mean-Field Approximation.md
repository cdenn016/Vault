---
type: concept
title: "Mean-Field Approximation"
aliases:
  - "Mean Field Approximation"
  - "Mean-field variational family"
  - "Factorized variational approximation"
  - "Mean Field Theory"
tags:
  - cluster/vfe
  - project/transformer
  - project/social-physics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Mean-Field Approximation

In variational inference, the mean-field approximation restricts the variational family to fully factorized distributions q(z) = prod_i q_i(z_i), decoupling latent variables so the ELBO can be optimized by coordinate ascent over each factor in closed form (for conditionally conjugate models). It trades exactness for tractability — ignoring posterior correlations and typically underestimating variance — and is the workhorse of variational Bayes / variational EM. The same factorization, borrowed from statistical physics, underlies mean-field treatments of interacting-agent and opinion-dynamics systems.

## Related
[[Variational free energy]], [[Evidence lower bound (ELBO)]], [[Variational EM]], [[Mean-field games and continuum limits]]

## Sources
[[blei-2017-variational-inference]], [[pilgrim-2023-confirmation]]
