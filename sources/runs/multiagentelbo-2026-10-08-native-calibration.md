---
type: run
title: "MultiAgentELBO native forecast numerical calibration"
aliases: ["R3 native reference precision and timestep calibration"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# MultiAgentELBO native forecast numerical calibration

On one saved N512/T4 instance, the matched all-row posterior reference passes the registered finite diagnostic screen and local timestep score error is small. Matter and link-precision inference residuals remain substantial despite forecast-score agreement within conditional numerical uncertainty. This advances numerical calibration while leaving native parent inference, dynamics and the full RG goal open. It continues [[multiagentelbo-2026-10-08-native-forecast]].

## Source and design

[MultiAgentELBO PR181](https://github.com/cdenn016/MultiAgentELBO/pull/181), revision `e3633c562e0e7db4bd2a28f9c599e2da91f00b5e`, contains the [frozen contract, results and evidence](https://github.com/cdenn016/MultiAgentELBO/blob/e3633c562e0e7db4bd2a28f9c599e2da91f00b5e/docs/research/2026-10-03-latent-link-rg-plan/R3-NATIVE-CALIBRATION-RESULTS.md). The original mass-16, width-.3 nonlinear history, all-row observed prefix of three episodes and unassimilated fourth-episode query are shared by recognition and reference. The current model and manuscripts are unchanged.

```bibtex
@misc{codex2026nativecalibration,
  author = {Codex},
  title = {Conditional Precision and Matched-Time Calibration of Native-History Forecasts},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/181},
  note = {One-instance numerical study; full native predictive accuracy remains open}
}
```

The reference uses four uninterrupted posterior chains, 64 burn-in and 256 retained sweeps. Three inference arms share a starting state and 16 training draws, with dt=.01/.005/.0025 and additional inference time .04. Four fresh 16-draw batches estimate full-history Fisher residuals. Four independent pools of 256 forecast draws are shared across recognition endpoints. Per-draw normalized row densities support a delta-method score variance retaining shared-row dependence. Rows, MCMC draws and optimizer iterations are nested measurements, not independent network instances.

## Executed results and scope

The CPU run completed in 621.6545513 seconds, with peak working set 1,120,210,944 bytes and compressed arrays 228,663,975 bytes. All 4/8/16 inference steps accepted without backtracking. Nine focused tiny tests pass; a separate NumPy reconstruction reproduces five score/MCSE arrays, two paired contrasts and their state differences, and three accepted-time sums. No full suite or GPU work ran.

Reference mean row log density is -4.021898961 with estimated MCSE .000367066 nat/record. Twice the MCSE is below the .0025 numerical target; half-chain scores differ by .000008592 and registered scalar split Rhat values are at most 1.005245. These finite diagnostics do not bound initialization bias or certify posterior-law accuracy. Recognition/reference mean-score differences range from -.000109135 at the start to about -.0000327 at the endpoints, below contrast MCSE around .00046 on this selected record set. This is not an independent-instance expected-loss guarantee.

Paired timestep score differences are 2.4111513e-7 and 1.1877615e-7 nat/record, with paired MCSE 4.7612074e-8 and 2.3416912e-8. State RMS differences approximately halve. This supports local finite-time refinement at a fixed integration batch. At the finest endpoint, matter-mean residual RMS remains 1.64876 versus MC RMS error .04996, and link-precision residual RMS .66590 versus .00774. Source residual rises over this short interval. Close forecasts therefore do not establish recognition stationarity or useful path-law error.

Next distinguish remaining optimization from integration error over a longer interval and increased draw budget, admitting larger timesteps before independent-instance evaluation. The fixed-model replicate can be an independently prepared whole history plus fresh original records; model-parameter variation is not required by the standing contract. Finite prior-MCMC preparation accuracy remains explicit. Full parent memory/error, trajectory control, endogenous second formation and nonlinear operational limits remain open. The GPU stayed occupied and unused; active controls, historical failures and protected WIP were preserved. The full goal remains active.
