---
type: concept
title: "Gaussian Belief Propagation"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-08-10
---

# Gaussian Belief Propagation

## Definition

Gaussian belief propagation (GaBP) is sum-product message passing specialized to a Gaussian graphical model. Writing a joint density in information form,

\[
p(x)\propto\exp\!\left(-\tfrac12x^\top Jx+h^\top x\right),
\]

each directed message remains Gaussian and can be represented by a scalar or block precision and information vector. Local updates are therefore sparse linear-algebra operations. On a tree, belief propagation terminates after a finite number of sweeps and returns exact Gaussian marginals. On a loopy graph, convergence and variance correctness require additional conditions.

## Walk-summability

[[malioutov-2006-walk-sums-gabp]] interprets Gaussian moments as sums over weighted walks in the graph. After diagonal normalization \(J=I-R\), a central sufficient condition is

\[
\rho(|R|)<1,
\]

where \(\rho\) is spectral radius and the absolute value is entrywise. This **walk-summability** condition makes the walk series absolutely convergent and guarantees convergence of loopy GaBP. It is stronger than positive definiteness: a valid Gaussian precision matrix can lie outside the walk-summable class.

## Means and variances are different obligations

When GaBP converges under broad conditions, its mean fixed point solves \(J\mu=h\), so the posterior means are exact. On loopy graphs, the belief variances obtained from local messages need not equal the diagonal of \(J^{-1}\), even when the means are correct. Tree exactness, convergence of means, and correctness of variances must therefore be reported separately. Residual convergence alone is not proof of calibrated covariance.

## Why it matters here

GaBP is a concrete decentralized-inference baseline for sparse Gaussian submodels. It connects precision-weighted local messages with the probabilistic population-coding perspective in [[pouget-2013-probabilistic-brains]], but it does not by itself implement nonlinear variational inference, unknown-correlation fusion, or gauge transport. A gauge-valued edge connection would have to be incorporated into a well-defined block Gaussian factorization before ordinary GaBP theorems could be reused.

## In this work

Use an exact sparse solve as the oracle. Test tree graphs, walk-summable loopy graphs, positive-definite but non-walk-summable instances, and near-boundary cases. Log the spectral certificate \(\rho(|R|)\), message residuals, mean error, marginal-variance error, and iteration count separately. Compare against conjugate gradient or a direct Cholesky solve so that communication behavior is not confused with linear-system conditioning.

## Sources

- [[malioutov-2006-walk-sums-gabp]] — walk-sum interpretation, walk-summability, and loopy-GaBP guarantees.
- [[pouget-2013-probabilistic-brains]] — probabilistic population codes and precision-weighted neural inference.

## See also

- [[Decentralized Bayesian inference]]
- [[Conservative information fusion]]
- [[Variational free energy]]
- [[Precision weighting|Precision-weighted attention]]
- [[Predictive coding]]
