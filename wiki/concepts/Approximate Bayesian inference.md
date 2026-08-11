---
type: concept
title: "Approximate Bayesian inference"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-08-10
---

# Approximate Bayesian inference

Approximate Bayesian inference encompasses methods for approximating intractable posterior distributions, including variational inference (minimizing KL to a tractable family), Monte Carlo dropout, Laplace approximations, and sampling (MCMC). It is the practical engine behind scalable Bayesian deep learning and is the lens through which dropout is reinterpreted as variational inference over network weights. Within the VFE program it is the same machinery as variational free-energy minimization, recast for posterior approximation over parameters or latent beliefs.

The MultiAgentELBO literature interface separates four approximation choices that must not be
collapsed into one label:

- **Family restriction:** mean field, structured families, copula constraints, and quotient families
  choose different normalized recognition spaces. [[senoz-2021-local-constraint-vmp]],
  [[tran-2015-copula-variational-inference]], and [[Quotient Bayesian learning]] are comparators.
- **Local-consistency relaxation:** Bethe/Kikuchi and EP-style methods can optimize
  pseudomarginals that need not be the marginals of one exact global law. See [[Belief Propagation]].
- **Numerical optimizer:** [[wilkinson-2023-bayes-newton]] supplies Newton/natural-gradient
  updates with positive-semidefinite covariance safeguards under its model assumptions.
- **Communication architecture:** [[Decentralized Bayesian inference]] and
  [[Communication-constrained inference]] introduce local objectives, message schedules, prior
  accounting, network mixing, and communication error in addition to posterior approximation.

The current MultiAgentELBO code supplies an exact finite oracle against which such methods can be
tested; it does not yet implement any of these approximate solvers or decentralized protocols.

## Related
[[Variational free energy]], [[Gaussian process]], [[Amortized inference]], [[Mean-Field Approximation]],
[[Process-space variational inference]], [[Decentralized Bayesian inference]]

## Sources
[[gal2016dropout]], [[blundell-2015-weight-uncertainty]], [[senoz-2021-local-constraint-vmp]],
[[tran-2015-copula-variational-inference]], [[wilkinson-2023-bayes-newton]],
[[hasenclever-2017-snep-posterior-server]], [[bagaev-2023-reactive-message-passing]]
