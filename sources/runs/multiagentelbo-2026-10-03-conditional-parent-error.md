---
type: run
title: "MultiAgentELBO conditional parent error and frozen lift contrast, October 3, 2026"
aliases: ["Conditional characteristic error and frozen lift comparison"]
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
year: 2026
created: 2026-10-03
---

# Conditional parent error and frozen lift contrast

> [!info] Citation
> MultiAgentELBO project (2026). *Conditional parent error and frozen lift contrast*. Code [01ac805](https://github.com/cdenn016/MultiAgentELBO/commit/01ac80597de94b0a455a63321687a009c3a92972), [PR115](https://github.com/cdenn016/MultiAgentELBO/pull/115). The research record, declaration, postprocessor and numerical evidence are archived in sources/archives/multiagentelbo-2026-10-03-conditional-parent-error/. This follows [[multiagentelbo-2026-10-02-square-root-budget]].

## Conditional error identity

For the frozen continuous switching law, project the native drift and visible assignment intensities onto the predictable retained-history filtration. Conditional quadratic and Bregman identities decompose the earlier fine-state budget as B=G+C. The term G is candidate-independent hidden information; C compares candidate predictions with the true retained predictable characteristics. The whole-assignment conditional intensity is the conditional expectation of the product of receiver probabilities, not the product of their conditional expectations. Invisible self-proposals are excluded and survival compensation is retained.

Under the explicit assumption that the Gaussian candidate's auxiliary budget has finite expectation on a fixed finite horizon, the record identifies C with forward retained path KL. It first obtains absolute continuity from the previous fine-lift bound, then proves the candidate's likelihood representation by local equivalence to a Brownian/finite-chain reference and removes localization using finite entropy. This is a conditional application of established information-estimation principles. The primary sources are Jiao, Venkat and Weissman, [Lemma4 and Theorem2](https://arxiv.org/html/1704.05199), and Leonard, [Theorems2.4 and2.11](https://leonard.perso.math.cnrs.fr/papers/2012-Leonard-Girsanov%20theory%20under%20a%20finite%20entropy%20condition.pdf). The former paper's almost-sure bounded-energy hypothesis is not presumed for this model.

Consequently matched candidate budget differences cancel G. The true conditional hidden covariance is needed to evaluate G; the candidate Gaussian covariance cannot substitute. The derivation supplies no small-error, epsilon-uniform or growing-horizon estimate, and finite empirical values do not prove the finite-expectation hypothesis. The full [derivation](../archives/multiagentelbo-2026-10-03-conditional-parent-error/conditional-characteristic-error.md.txt) retains these assumptions.

## Saved-data comparison

A posthoc comparison, selected after observing the original budgets, used all sixteen saved paths at each of512/1,024 agents and both grids. The comparator is the frozen activation-conditional affine lift, used directly to define smooth retained drift and positive product source rates; it is an ordinary Markov parent, not a claimed singular regular-density decoder. One CPU postprocessing invocation completed in4.100971 seconds with no new trajectories, Gaussian-message propagation or GPU use.

| Agents | Fine Gaussian minus lift | Coarse Gaussian minus lift | Fine minus coarse contrast |
| --- | --- | --- | --- |
| 512 | -8.39344 +/- 1.08005 | -8.27006 +/- 1.04560 | -0.12338 +/- 0.05641 |
| 1,024 | -15.28922 +/- 1.90772 | -15.24126 +/- 1.89376 | -0.04797 +/- 0.10588 |

Values are nats per path with empirical paired standard errors. Fine drift differences are-2.61063 +/-0.85237 and-4.21980 +/-0.94870; visible-source differences are-5.78281 +/-0.75988 and-11.06942 +/-2.02894. Both components favor the evolving Gaussian recipe in this sample. This compares entire recipes and does not isolate a causal effect of memory. Each size has one model realization, and this uses the same native paths as the preceding study rather than an independent replication.

Checks cover32 paths,64 grids and108 standard-error calculations. Independent drift polarization and source log-ratio calculations agree with subtraction; maximum recorded arithmetic discrepancy is1.13687e-13. Lift-fiber and source-row normalization discrepancies are at most2.77556e-16 and2.22045e-16. The [result report](../archives/multiagentelbo-2026-10-03-conditional-parent-error/frozen-lift-comparison-RESULTS.md.txt) links the exact source and full per-path outputs.

## Relevance to this research

[[Gauge-Theoretic Multi-Agent VFE Model]] and [[Staged hierarchy formation and RG composability]] retain O1/O4 as open. The finite-grid auxiliary contrast is not a continuous retained-path KL estimate or a confidence certificate. Its Euler mesh includes proposal times, including invisible self-proposals. The sharper target is quantitative control of true retained prediction error, with candidate integrability, discretization and the required horizon regimes established. Endogenous structural feedback and recursive formation remain separate obligations. No manuscript theorem, active launcher or historical failed run was changed.
