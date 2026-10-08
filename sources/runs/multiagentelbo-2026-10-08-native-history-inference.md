---
type: run
title: "MultiAgentELBO native nonlinear history inference"
aliases: ["R3 prefix-only augmented history inference"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# MultiAgentELBO native nonlinear history inference

The R3 runtime now evaluates and descends the original finite nonlinear generator-history objective using only an observed record prefix. It retains every latent generator slice, including unobserved future slices, with original anchors, nonlinear spatial loops and analytic Gaussian increment expectations. Matter and source recognition exist only for observed slices. All directions use one old state and one jointly accepted step. This implements a native-history inference dependency; accurate posterior prediction remains open.

## Source and execution scope

[MultiAgentELBO PR179](https://github.com/cdenn016/MultiAgentELBO/pull/179), code revision `4176c2eb00e94241d8d86d8a9869c5d8b0b00ce1`, contains the [implementation/results](https://github.com/cdenn016/MultiAgentELBO/blob/4176c2eb00e94241d8d86d8a9869c5d8b0b00ce1/docs/research/2026-10-03-latent-link-rg-plan/R3-HISTORY-INFERENCE-RESULTS.md), [continuous-prior and augmented-objective derivation](https://github.com/cdenn016/MultiAgentELBO/blob/4176c2eb00e94241d8d86d8a9869c5d8b0b00ce1/docs/research/2026-10-03-latent-link-rg-plan/R3-CONTINUOUS-PREDICTIVE-PRIOR.md), and final disjoint JUnit/resource evidence. The live source is c08b's normalized history with Gaussian increments, c12's episode joint, and the existing R0 contract. Manuscripts are unchanged.

```bibtex
@misc{codex2026nativehistoryinference,
  author = {Codex},
  title = {Prefix-Only Inference under the Nonlinear Generator-History Law},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/179},
  note = {MultiAgentELBO implementation and scoped CPU admission}
}
```

A separate normalized full Gaussian prior input now reaches the R1 objective, both estimators and acceptance. It retains cross-edge mean coupling and the complete normalization. Dense history elimination and backward partition constants validate it as an exact quadratic reference; it is not the large-network nonlinear storage choice. In the augmented native objective, each slice instead retains the original Gaussian anchor once and the temporal energy explicitly. Adding a backward root correction on top would double count it. The omitted fixed additive constant is log Z_hist of the complete nonlinear history, not only the Gaussian temporal normalizer.

## Executed evidence

The final disjoint packets contain 35 passing tiny CPU cases: 15 new prior/history checks and 20 existing regression cases. They cover full normalized Gaussian KL, filtered prediction, backward boundary constants, common-state derivatives, finite-difference tangents, dense kinetic energy, T=1 recovery, prefix-only shapes and acceptance. They also reproduce a positive minimum product-family Gaussian history KL gap, distinguishing correct code from exact posterior inference.

One N512 CPU admission with 1,024 primitive copies, T=4, one observed slice, mass 16 and 16 integration draws completed in 8.9239552 seconds. The finite-draw relative objective changed from 22063.2719462586 to 21530.4837587017, accepting dt=.01 without backtracking. Future mean RMS changed by 0.0003089957. Returned recognition tensors use 696,320 bytes, integration noise 2,097,152 bytes and observed offsets 32,768 bytes; these exclude the separately retained source/model payload. Peak process working set was 899,219,456 bytes. The saved one-episode input is an admission fixture, not a new native history ensemble or forecast-accuracy study. GPU was occupied and unused.

## Approximation and continuation

The product recognition family omits temporal and cross-edge covariance. Its exact augmented KL decomposes into the queried marginal KL and a nonnegative conditional-bridge gap. A decreasing sampled objective does not establish native forward predictive loss or a vanishing approximation error. The derived direct continuous predictive-density option integrates the original tilt under a Gaussian conditional history; its regularized forward-error bound depends on evidence mass and has not been shown useful at N512. That option is unimplemented.

Next implement causal forecast-then-assimilate using original native episode records and the existing fitted-parent adapter, with an assessed reference under the same observation design and the declared original-record/memory budget. Full native trajectory control, growing operational limits and endogenous second formation remain open. CUDA calibration awaits resources; no historical numerical failure was retried.

## Relevance to this research

This advances [[Gauge-Theoretic Multi-Agent VFE Model]], [[Staged hierarchy formation and RG composability]] and [[Renormalization-group flow of beliefs]] beyond [[multiagentelbo-2026-10-08-recognition-activation]]: actual temporal coupling now enters simultaneous inference without resetting the one-episode prior. The full fixed-c_* RG goal remains active, with all four gates still open.
