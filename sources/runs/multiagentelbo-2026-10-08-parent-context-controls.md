---
type: run
title: "MultiAgentELBO native parent-context precision and matched history controls"
aliases: ["R3 direct conditional reference and R1 history controls"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# MultiAgentELBO native parent-context precision and matched history controls

The direct native parent-context sampler is implemented, and its fixed N512 calculation completed with the prescribed score precision still inconclusive. Alternating full-history and conditional held-anchor controls now execute on the same saved input as the simultaneous reference. This continues [[multiagentelbo-2026-10-08-native-bridge-convergence]]; all four full RG gates remain open.

## Sources and model

[MultiAgentELBO PR183](https://github.com/cdenn016/MultiAgentELBO/pull/183), merged revision `91b0aaec061da04b3d76fdab085530d28423571a`, contains the [conditional target construction](https://github.com/cdenn016/MultiAgentELBO/blob/91b0aaec061da04b3d76fdab085530d28423571a/docs/research/2026-10-03-latent-link-rg-plan/R3-PARENT-CONTEXT-TARGET.md), [frozen contract](https://github.com/cdenn016/MultiAgentELBO/blob/91b0aaec061da04b3d76fdab085530d28423571a/docs/research/2026-10-03-latent-link-rg-plan/R3-PARENT-CONTEXT-CONTRACT.md), [executed results](https://github.com/cdenn016/MultiAgentELBO/blob/91b0aaec061da04b3d76fdab085530d28423571a/docs/research/2026-10-03-latent-link-rg-plan/R3-PARENT-CONTEXT-RESULTS.md) and [control implementation/admission](https://github.com/cdenn016/MultiAgentELBO/blob/91b0aaec061da04b3d76fdab085530d28423571a/docs/research/2026-10-03-latent-link-rg-plan/R1-HISTORY-CONTROL-ARMS.md). Both runs retain the existing N512/T4, mass-16, width-.3 nonlinear model and all-row observed prefix of episodes 0 through 2. No model, manuscript or active launcher configuration changes.

```bibtex
@misc{codex2026parentcontextcontrols,
  author = {Codex},
  title = {Native Parent-Context Precision and Matched History Controls},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/183},
  note = {Finite CPU implementation and calibration; conditional precision remains inconclusive}
}
```

## Direct conditional reference

The native target conditions on the past original records and all 128 raw future parents. Fresh future matter is integrated into normalized Gaussian parent factors. Positive root channel weight supplies the construction's finite upper density bound. Past source and shared-matter Gibbs conditionals stay unchanged; whole-history link proposals include the context density change and additional parent-tree conflicts. Prediction averages the conditional decoder without multiplying the context likelihood twice. The queried future records, future fine matter and future labels are excluded from sampling. This is p(O3 | Y3, prefix), with additional information relative to a prefix-only forecast.

Four chains use 256 burn-in and 1,024 retained sweeps each. Direct joint log density divided by two queried original rows is -4.687649096901775, conditional batch-means MCSE .003559941982086572, twice MCSE .007119883964173144, and half-chain difference .005160072976784669. Both precision measures exceed the frozen .0025 threshold. All recorded scalar split Rhat values are at most 1.001449523; this does not override the failed score diagnostics or certify full-state mixing.

The reused earlier reweighted ensemble gives per-row score -4.937387527717036, MCSE .07126375076675323 and half difference .17230620743293912. Direct minus earlier is .2497384308152606 with combined conditional MCSE .07135261284817637. Neither initialization bias is certified, and the different budgets prevent a matched-cost efficiency conclusion. The conditional accuracy gate remains open. The fixed run was not extended or retried.

Total CPU time is 843.691 seconds, peak working set 2,549,927,936 bytes, and retained NPZ storage 648,093,298 bytes. Whole histories and past latent states, exact context/query inputs, all decoder values, traces and source metadata are retained. Independent NumPy reconstruction reproduces source marginalization, density ratios, chain/half scores and MCSE without new sampling.

## Matched control admission and remaining work

The alternating control uses categorical, matter, then generator blocks with one full-history acceptance and whole-sweep backtracking. The held-anchor arm is an explicit point-link conditional counterfactual with no generator precision or finite generator KL. It is not compared through unlike free-energy values. All arms forecast original episode 3 using fresh matter and source priors.

One common-input dt=.05 step per arm completes in 26.538 seconds, peak working set 934,977,536 bytes, without backtracking. Simultaneous and alternating losses both equal 4.02123340794 nats per original row; held-anchor loss is 4.02880893655. The finite-width forecasts are exactly equal because their first unobserved-slice generator coefficients coincide; observed-state updates differ. This admission cannot distinguish their longer predictive behavior or establish an independent-instance advantage. Saved-value reconstruction confirms scores, shared Gaussian noise and exact held anchors. Twenty-two distinct tiny CPU cases pass across the focused packets; no full suite or GPU workload ran.

Continue the registered independent-preparation flow comparison after N1024 and free-GPU admission. Use the retained conditional precision gap to design the next estimator without repeatedly extending this selected context. Native parent dynamics and moving-geometry feedback, endogenous second formation and the complete nonlinear growing-size/depth law remain unresolved. The goal stays active.

## Relevance to this research

The batch supplies the direct conditional law and matched controls needed by [[Staged hierarchy formation and RG composability]] and [[Renormalization-group flow of beliefs]]. It advances the finite implementation in [[Gauge-Theoretic Multi-Agent VFE Model]] while preserving the distinction between an exact conditional construction, finite-chain precision, trajectory control and the full renormalization target.
