---
type: run
title: "MultiAgentELBO square-root parent-budget study, October 2, 2026"
aliases: ["Completed square-root Gaussian parent-budget study"]
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
year: 2026
created: 2026-10-02
---

# Completed square-root parent-budget study

> [!info] Citation
> MultiAgentELBO project (2026). *Square-root parent-budget study*. Code commit [59d01c8](https://github.com/cdenn016/MultiAgentELBO/commit/59d01c89bb7201a7567266375418d0c8493d342b), [PR114](https://github.com/cdenn016/MultiAgentELBO/pull/114). Reports, declarations, executed-source ZIPs, retained numerical outputs and terminal/JUnit receipts are archived in sources/archives/multiagentelbo-2026-10-02-square-root-budget/. This completes the pending validation in [[multiagentelbo-2026-10-02-square-root-conditioning]]. The original dense run in [[multiagentelbo-2026-10-02-continuous-parent-budget]] remains failed with unresolved Cholesky cause.

## Executed calculations

One archived N1024 fine tape completed with square-root conditioning in 74.472238 seconds (76.219018 seconds at the terminal). It contains 130 forecasts, 131 observations, two visible source changes and two two-branch budget probes. Native states and labels reproduce the earlier tape exactly. The maximum covariance-fiber residual across actual and hypothetical conditioning is 1.22005e-15, and independent NumPy reconstruction of the saved budget arithmetic differs by at most 1.42109e-14. Its full source-call rows support separate checks of both self-prefix accumulations. This is one-path arithmetic validation, not certification of the Gaussian approximation.

A separately declared paired-grid study then completed once in 1297.555569 seconds with four single-thread CPU workers: sixteen paths at each of N512 and N1024, K2, block size16, horizon1, maximum steps1/64 and1/128, and two uniform-time probes. It retains the same frozen model, activation and random-stream conventions as the earlier study, selecting the opt-in square-root source backend. No GPU was needed or used.

| Agents | Coarse total | Fine total | Paired fine minus coarse |
| --- | --- | --- | --- |
| 512 | 48.27739 +/- 1.02092 | 48.06318 +/- 0.99252 | -0.21422 +/- 0.08401 |
| 1,024 | 99.08546 +/- 1.27244 | 98.84799 +/- 1.21466 | -0.23747 +/- 0.18346 |

Values are nats per path, with empirical standard errors across sixteen paths. Each size has one model realization. The fine drift contributions are 4.63368 and 10.18806; visible-source contributions are 43.42950 and 88.65993. These descriptive sufficient-budget measurements are not retained-path KL values, confidence upper bounds, continuous-time convergence results or thermodynamic-limit evidence.

## Mechanical checks and reporting correction

An independent NumPy checker passed all 32 paths and 64 grids, reconstructing selected receiver and sender forces, native probe rows, cost arithmetic, six integrals and 36 aggregate estimates. Maximum arithmetic discrepancy is 2.27374e-13. Reported covariance-fiber maxima are 5.23886e-16 and 3.40006e-16; mean-fiber maxima are 3.27429e-16 and 2.91434e-16. The full-study checker consumes retained covariance diagnostics and candidate self logs; it does not regenerate complete covariance histories or candidate prefix rows. All 25 available earlier native tapes match exactly. Every saved fine-grid field of N1024 path001 matches the separate validation exactly.

The original summary routine underflowed the variance of self terms near 1e-216. Its metadata and first checker receipt remain unchanged. A scale-normalized standard-deviation calculation now preserves these tiny uncertainties; three tiny tests passed after one failing tiny-scale case and two passing controls. A saved-array recomputation checked all 36 corrected summaries against an independent scaled math.fsum formula without rerunning any trajectory. Corrected N1024 self standard errors are 4.03623e-216, 8.93365e-216 and 4.89742e-216 for coarse, fine and paired difference. The table above is unchanged at the shown precision. Use continuous-square-root-evidence/scale-stable-summaries.json for corrected summaries. Producer, original checker and reporting-correction sources are stored separately; current source differs from the producer only in the summary calculation. The earlier twelve primitive/consumer checks were not rerun.

## Relevance to this research

[[Gauge-Theoretic Multi-Agent VFE Model]] and [[Staged hierarchy formation and RG composability]] retain O1/O4 as open. The existing error route allows a positive sufficient budget even for an exact conditional decoder; a large auxiliary fine comparison therefore does not establish poor retained prediction. The recorded next task is sharper retained-law error accounting separating conditional hidden-state information from candidate prediction error, followed by evidence for the actual conditional predictor. Small controlled actual-law bounds, both asymptotic horizon regimes, endogenous feedback and recursive formation remain unresolved. No manuscript theorem or base-transport scope changes.

The [full result report](../archives/multiagentelbo-2026-10-02-square-root-budget/continuous-square-root-RESULTS.md.txt) and [one-path report](../archives/multiagentelbo-2026-10-02-square-root-budget/covariance-square-root-path-RESULTS.md.txt) state the numerical and interpretation limits.
