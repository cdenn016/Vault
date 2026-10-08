---
type: run
title: "MultiAgentELBO native parent bridge and longer inference"
aliases: ["R2 native factored bridge and R3 convergence comparison"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# MultiAgentELBO native parent bridge and longer inference

The complete empirical all-parent/record bridge now has a factored representation that agrees with the dense construction while avoiding repeated all-parent covariance arrays. A separate longer-inference comparison reduces the main recognition residuals but does not reach stationarity. These results continue [[multiagentelbo-2026-10-08-native-calibration]] and advance finite implementation and numerical calibration; all four full RG gates remain open.

## Sources and common model

[MultiAgentELBO PR182](https://github.com/cdenn016/MultiAgentELBO/pull/182), merged revision `4587db5d031f41e965ef4c5388eb72a3b9e1b0ff`, records the [bridge derivation](https://github.com/cdenn016/MultiAgentELBO/blob/4587db5d031f41e965ef4c5388eb72a3b9e1b0ff/docs/research/2026-10-03-latent-link-rg-plan/R2-NATIVE-PREDICTIVE-BRIDGE.md), [frozen bridge contract](https://github.com/cdenn016/MultiAgentELBO/blob/4587db5d031f41e965ef4c5388eb72a3b9e1b0ff/docs/research/2026-10-03-latent-link-rg-plan/R2-NATIVE-BRIDGE-EXECUTION-CONTRACT.md), [bridge results](https://github.com/cdenn016/MultiAgentELBO/blob/4587db5d031f41e965ef4c5388eb72a3b9e1b0ff/docs/research/2026-10-03-latent-link-rg-plan/R2-NATIVE-BRIDGE-RESULTS.md), [frozen inference contract](https://github.com/cdenn016/MultiAgentELBO/blob/4587db5d031f41e965ef4c5388eb72a3b9e1b0ff/docs/research/2026-10-03-latent-link-rg-plan/R3-INFERENCE-CONVERGENCE-CONTRACT.md) and [inference results](https://github.com/cdenn016/MultiAgentELBO/blob/4587db5d031f41e965ef4c5388eb72a3b9e1b0ff/docs/research/2026-10-03-latent-link-rg-plan/R3-INFERENCE-CONVERGENCE-RESULTS.md). Both studies reuse the fixed N512/T4, mass-16, width-.3 nonlinear model and all-row observed prefix of episodes 0 through 2. The model, manuscripts and active controls are unchanged.

```bibtex
@misc{codex2026nativebridgeconvergence,
  author = {Codex},
  title = {Factored Native Parent Bridges and Longer History Inference},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/182},
  note = {Finite empirical identity and one-instance numerical comparison; native conditional accuracy remains open}
}
```

## Complete empirical bridge

All 1,024 episode-3 generator components from the completed four-chain posterior reference are retained with their original identities and uniform empirical masses. Future matter has fresh baseline moments and source labels have the generative prior. The hard lattice channel retains 128 parents and 1,024 original primitive copies. Two prescribed original record rows give 16 source assignments. Conditional on a whole component, all-parent Gaussian block factors and a local affine record decoder reconstruct the dense joint. Record conditioning retains its induced cross-parent covariance through an exact low-rank downdate; subsequent linear projection preserves that covariance.

The 128 streamed chunks compare all component means/covariances, geometric marks, mixture weights and both conditional directions. The maximum discrepancy is 1.5631940186722204e-13, below the frozen 1e-8 tolerance. Measured unique retained tensor storage is 104,937,904 bytes, including primitive generators, geometry, baseline state, model and decoder. The full dense-equivalent estimate is 8,992,790,800 bytes; its accounting exactly matches an actually materialized eight-component chunk. The full dense bank was never allocated. Total bridge comparison time is 67.059 seconds, with process peak 1,207,820,288 bytes. Ten focused tiny CPU tests pass.

The context uses the saved future matter/link realization and therefore queries p(O3 | Y3, prefix), with future parent Y3 as additional information. This is not a prefix-only forecast evaluation. Full-context weighting leaves maximum component mass .564666 and effective component count 2.720826. That concentration does not itself prove an accuracy failure, but neither empirical representation equivalence nor the earlier marginal row-score precision bounds error against the continuous context-conditioned native law. Complete-history memory for future native updates is not hidden in the future-slice-only bank.

## Longer finite-time inference

The three arms share the saved starting state and reach additional accepted inference time 1: 16 draws at dt=.1, 16 draws at dt=.05, and 64 draws at dt=.05. The first 16 training draws are shared; additional draws and residual/score pools use separately declared seeds. The existing posterior reference is reused, not resampled. All arms complete in 1374.669 seconds total, with peak working set 1,899,323,392 bytes. A NumPy saved-value reconstruction reproduces five score/MCSE arrays, two paired contrasts, endpoint state differences and three accepted-time sums.

The timestep score contrast is -2.9164e-5 nat/record (paired MCSE 1.4887e-6); the 16-minus-64 training-draw contrast at dt=.05 is -4.4570e-5 (paired MCSE 1.2768e-5). These are small relative to the .0025 numerical target on this selected instance. They do not establish expected excess loss over independent preparations. Matter-mean residual RMS falls from 2.0034 to .20649 in the 64-draw arm, and link-precision residual RMS falls from .76299 to .10733; both remain above their Monte Carlo errors. The source residual rises during joint motion. Finite-time flow and equilibrium convergence remain distinct.

## Remaining work

Carry the measured cheaper finite-time arm as a candidate into the registered independent-preparation calibration, preserving simultaneous/alternating/held-link and matched-time comparisons. Do not extend optimization on this instance repeatedly merely to chase an already insensitive forecast score. Separately establish an assessed native parent-context target and conditional approximation error. Useful parent memory/dynamics, endogenous second formation and nonlinear growing-size/depth control remain unresolved. The GPU was unused; this CPU batch does not establish CUDA behavior. Protected WIP and historical failures were preserved, and the full goal remains active.
