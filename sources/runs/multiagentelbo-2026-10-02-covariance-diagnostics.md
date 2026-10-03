---
type: run
title: "MultiAgentELBO covariance diagnostic checkpoint, October 2, 2026"
aliases: ["Gaussian covariance diagnostic checkpoint"]
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
year: 2026
created: 2026-10-02
---

# Covariance diagnostic checkpoint

> [!info] Citation
> MultiAgentELBO project (2026). *Covariance diagnostic checkpoint*. Executed scientific source is based on a7b2c68a1c18119adbfe8c9dbdf8259f4f4e57ed; the two source ZIPs preserve the exact diagnostic script versions. Full captures, scalar records, declarations, analyses and executed scripts are archived under sources/archives/multiagentelbo-2026-10-02-covariance-diagnostics/. The [checkpoint report](../archives/multiagentelbo-2026-10-02-covariance-diagnostics/covariance-diagnostic-RESULTS.md.txt) preserves the outcome limits. This follows [[multiagentelbo-2026-10-02-continuous-parent-budget]].

## Executed outcomes

The first saved N1024 path001 replay stops on a saved-mean discrepancy of 3.01071e-6 after 44 intervals, while its measured covariance-fiber residual remains at most 9.32414e-17. It does not reproduce the original fiber residual or terminal Cholesky exception. The separately declared local-conditioning prefix captures receiver 293 of the second source event: incoming six-coordinate condition 24.977 becomes about 5.80803e12 under positive cubature weights. This is an outgoing-condition threshold, not nonpositivity or the original failed worker.

A captured-state continuation completes the remaining 730 source receivers. Maximum incoming condition is 418717.1732 and maximum fiber residual 9.32414e-17; no next forecast or observation is run. The raw final capture inherits auxiliary local arrays from receiver 293, while its full pre/post means, covariances and labels refer to receiver 1023. Per-receiver scalar records and metadata retain this distinction.

One captured-operation comparison finds that direct block assembly improves local precision, but no measured full-fiber or hidden-principal spectral improvement. An 80-digit local reference constructed from stored positive weights and rounded offsets retains a tiny covariance eigenvalue near 1.59230e-14. This is a scoped numerical comparison, not exact-real or interval certification. The [analysis](../archives/multiagentelbo-2026-10-02-covariance-diagnostics/covariance-update-analysis.md.txt) retains equivalent block identities, their assumptions, and unexecuted implementation candidates.

The three diagnostic arms took 82.979820, 57.657155 and 22.103375 seconds; the comparison took 2.299293 seconds. They use CPU float64 with one numerical thread, plus 80-digit local arithmetic. No production filter, scientific parameter, tolerance, or native path was changed; no unit tests, full study retry, or GPU calculation was run. Prior focused tests remain historical evidence for unchanged production code.

## Relevance to this research

[[Staged hierarchy formation and RG composability]] and [[Gauge-Theoretic Multi-Agent VFE Model]] retain O1 and O4 as open. The original budget study remains failed; the first damaging operation and score bias are unresolved. This checkpoint supplies captured numerical evidence for a subsequent justified repair, not a completed error-budget study or a general obstruction to renormalization. Near-singularity of one local update does not by itself diagnose a later projected-covariance failure.
