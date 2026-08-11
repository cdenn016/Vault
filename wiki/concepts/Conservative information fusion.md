---
type: concept
title: "Conservative information fusion"
aliases:
  - "Fusion under unknown correlation"
  - "Covariance intersection"
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
status: draft
created: 2026-08-10
updated: 2026-08-10
---

# Conservative information fusion

## Definition

Conservative information fusion combines estimates without claiming more precision than the available dependence information justifies. Its canonical use case is two unbiased Gaussian estimates of the same state with known marginal covariances but unknown cross-correlation. Multiplying them as independent likelihoods can count shared evidence twice and produce an overconfident covariance.

For covariance intersection (CI), an admissible weight \(\omega\in[0,1]\) gives

\[
P_{\mathrm{CI}}^{-1}=\omega P_1^{-1}+(1-\omega)P_2^{-1},
\qquad
P_{\mathrm{CI}}^{-1}\hat x_{\mathrm{CI}}
=\omega P_1^{-1}\hat x_1+(1-\omega)P_2^{-1}\hat x_2.
\]

The weight is usually chosen to minimize a scalar measure such as determinant or trace of the fused covariance. The guarantee is consistency under unknown correlation, not equality to the optimal fusion result that would be available if the cross-covariance were known.

## Why it matters here

Repeated information exchange creates hidden common information even when agents' original measurements were independent. A future decentralized MultiAgentELBO implementation needs evidence lineage or a conservative fallback; otherwise a product-of-experts update can make precision grow simply by circulating the same evidence. [[julier-uhlmann-1997-covariance-intersection]] supplies a baseline for Gaussian beliefs when cross-correlations cannot be tracked.

## Distinctions

- **Exact Bayesian fusion** uses the joint likelihood and all relevant dependence information.
- **KL-average or logarithmic pooling** chooses a distributional consensus target; it is not automatically conservative for an unknown common-information history.
- **Covariance intersection** guarantees a covariance bound under its estimation assumptions, generally at the cost of a broader estimate.
- **Covariance union** addresses a different problem, disagreement about which estimate is valid, and should not be conflated with CI.

Unknown correlation is not the same failure as dropped communication, approximation error, model mismatch, or incompatible coordinate frames. Those errors require separate diagnostics.

## In this work

Tests should construct two agents whose local estimates share a tunable fraction of evidence. Compare naive independent fusion, fusion with known cross-covariance, CI, and a lineage-aware Bayesian oracle. Report calibration or coverage as well as nominal covariance volume. Gauge transport should be applied before comparing tensors in a common frame, but transport itself does not reveal whether evidence is duplicated.

## Sources

- [[julier-uhlmann-1997-covariance-intersection]] — original CI formulation for unknown correlation.
- [[battistelli-chisci-2014-kl-density-consensus]] — KL-average density consensus, a related but distinct target.
- [[campbell-how-2014-decentralized-bayes]] — prior correction and approximation alignment in decentralized posterior fusion.

## See also

- [[Decentralized Bayesian inference]]
- [[Communication-constrained inference]]
- [[Probabilistic opinion pooling]]
- [[Gaussian Belief Propagation]]
