---
type: concept
title: Quotient Bayesian Learning
aliases:
  - QBLR
  - Quotient natural gradient
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-08-10
updated: 2026-08-10
---

# Quotient Bayesian Learning

## Definition

Quotient Bayesian learning performs natural-gradient inference on a statistical model represented by redundant covering parameters. Parameters that induce the same marginal distribution form a fiber; vertical tangent vectors change only the representative, while horizontal vectors change the marginal. Under the hypotheses of [[lukashchuk-2025-quotient-bayesian-learning]], the quotient metric induced from the covering Fisher metric equals the marginal family’s Fisher metric, and a quotient update is the horizontal projection of a covering-space natural gradient.

## Why it matters

Redundant coordinates make the Fisher matrix singular or waste optimization effort along directions that do not change the predictive distribution. Quotient geometry makes the estimand—not its representation—the optimization space and supplies a principled alternative to arbitrary gauge fixing.

## Details

The 2025 construction applies to marginal families arising from minimal regular exponential families under specified moment-parameterized marginalization assumptions. Equal-marginal fibers give the equivalence relation, and the Riemannian-submersion construction transfers the metric and update to the quotient.

Three notions must remain separate:

1. **Marginalization redundancy:** distinct joint-family parameters give the same marginal distribution.
2. **Graphical-model factor gauge:** invertible factor reparameterizations preserve a tensor contraction/partition function, as in [[ahn-2017-gauging-variational-inference]].
3. **Passive principal-bundle frame change:** a group acts on local coordinates while physical sections, connections, and observables transform covariantly.

These are not interchangeable because their objects, equivalence classes, invariants, and group actions differ. An analogy becomes a theorem only after an explicit map proves that the relevant objective and Fisher geometry descend.

## In this work

QBLR motivates projecting marginal-family updates away from provably redundant directions and verifying representative independence numerically. It does **not** establish that a noncompact $\mathrm{GL}(K)$ frame action is free and proper, that its quotient is Hausdorff and smooth, that stabilizer/singular strata are harmless, or that ELBO/natural-gradient flows semiconjugate across coarse scales. Citation alone does not close the quotient-geometry obligation.

## Sources

- [[lukashchuk-2025-quotient-bayesian-learning]]
- [[ahn-2017-gauging-variational-inference]]

## See also

- [[Riemannian Quotient Manifold]]
- [[Fisher information metric]]
- [[Natural gradient]]
- [[Evidence lower bound (ELBO)]]
- [[Gauge transformation]]
