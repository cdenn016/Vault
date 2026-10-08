---
type: run
title: "MultiAgentELBO causal native-history forecasts"
aliases: ["R3 all-row native posterior and forecast protocol"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# MultiAgentELBO causal native-history forecasts

The R3 runtime now predicts each original episode before assimilating it, including inference from an empty observed prefix. A new native-history posterior reference conditions on every row in exactly the same revealed prefix and keeps the same finite generator horizon. This supplies the missing matched reference and causal protocol. It does not establish prediction accuracy, reference mixing, a useful compressed parent or full renormalization.

## Source and model

[MultiAgentELBO PR180](https://github.com/cdenn016/MultiAgentELBO/pull/180), revision `679363dde97749f64464213cdc2edd80faa9bd7d`, contains the [implementation, results and evidence](https://github.com/cdenn016/MultiAgentELBO/blob/679363dde97749f64464213cdc2edd80faa9bd7d/docs/research/2026-10-03-latent-link-rg-plan/R3-NATIVE-FORECAST-RESULTS.md). It continues [[multiagentelbo-2026-10-08-native-history-inference]] under the original c08b normalized history and c12 episode-joint model. Manuscripts are unchanged.

```bibtex
@misc{codex2026nativeforecast,
  author = {Codex},
  title = {Causal Native-History Forecasts and an All-Row Conditional Reference},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/180},
  note = {MultiAgentELBO implementation and scoped CPU protocol admission}
}
```

The posterior sampler alternates normalized source-label conditionals, full joint Gaussian matter conditionals and colored whole-edge history Metropolis updates. Matter precision includes every selected record's receiver and sender. Link proposal ratios include the observed records even when spatial-loop weights vanish. Shared matter is held fixed during each link sweep, and reversed records share their original primitive generator. The returned finite chains have an explicit unresolved mixing status.

Future episode prediction integrates fresh baseline matter and source prior pi. Past fitted matter, responsibilities and offsets do not become future generative factors. Original simulation matter and source labels remain diagnostics. Row densities are normalized marginal mixtures; their sum is a composite score rather than the full-network joint density. The older T16/two-row reference is inapplicable to this T4/all-row conditioning problem.

## Executed evidence and remaining work

Seventeen distinct tiny CPU cases pass in the final disjoint JUnit packets: ten new posterior/causal cases and seven existing history cases. They cover independent dense Gaussian conditional formulas, proposal differences/flux, hard source support, empty-prefix inference with both estimators and forecast-before-assimilation behavior. No full suite ran.

The N512/T4, mass-16, width-.3 admission generated four original episodes from one saved native-history draw. Each prefix received one dt=.01 update with 16 integration draws; future scores used 256 separate draws. Posterior references used two chains, two burn-in sweeps and four retained sweeps. All five updates accepted without backtracking. Total time was 48.1477894 seconds, peak working set 995,672,064 bytes and compressed arrays 41,206,702 bytes. Artifact bytes exclude additional model/source/decoder memory. The archived truth and prior-reference histories are finite MCMC samples, not certified independent native draws.

These short budgets validate execution and resources only. Score proximity cannot assess the .01 nat/record target or .0025 conditional numerical tolerance. Next calibrate optimization and integration convergence and conditional reference precision, then freeze independent-instance evaluation budgets and apply the existing fitted-parent adapter. The product-family gap, native trajectory control, persistent second formation and nonlinear operational growing law remain open. All four full RG gates and the full goal remain active. The occupied GPU was not used; active controls and historical failures were preserved.
