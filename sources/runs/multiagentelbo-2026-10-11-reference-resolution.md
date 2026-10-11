---
type: run
title: "MultiAgentELBO fresh two-size posterior reference resolution"
aliases: ["N512 and N1024 conditional burn sensitivity at 1024 retained histories"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/statistics, field/mathematics, field/cs-ml]
created: 2026-10-11
updated: 2026-10-11
---

# MultiAgentELBO fresh two-size posterior reference resolution

Both first frozen cases pass the .0004-nat burn-sensitivity screen: absolute burn-in contrast and twice conditional MCSE are below the allowance at N512 and N1024. This admits conditional resolution on one new preparation per size, without initialization-bias or mixing bounds. The earlier [[multiagentelbo-2026-10-11-n1024-posterior-admission]] precision miss remains unchanged.

[Code PR277](https://github.com/cdenn016/MultiAgentELBO/pull/277) publishes the [result](https://github.com/cdenn016/MultiAgentELBO/blob/e7a5c8c0896559422e5b7e8ae80622abb0771136/docs/research/2026-10-03-latent-link-rg-plan/R3-REFERENCE-RESOLUTION-RESULTS.md) at source revision `e7a5c8c0896559422e5b7e8ae80622abb0771136`, merged as `2a38c04cd01725a4094ff47446fa3f601e4174cb`. The contract, runner and readers were committed before either preparation existed at clean producer revision `6547b908a8bdf7f6c4de7e794cafb31fd08d15b3`; publication and production have separate roles.

```bibtex
@misc{codex2026referenceresolution,
  author = {Codex},
  title = {Fresh Two-Size Posterior Reference Resolution},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/277}
}
```

## Frozen comparison and results

Only the declared calibration models were consumed. Real GL+(2), K2/D4, zero anchors, width .3, loop weight .25 and mass sixteen remain at fixed $c_*$ on 16-by-32 and 32-by-32 agent lattices. Each size independently prepares fresh prior/data records with burn256/retain64; these are finite-MCMC preparations, not exact prior draws. At each size, independent burn64 and burn256 posterior calls use four fresh chains and 1024 retained complete histories per chain. Only the first three observed episodes condition either call. Fourth-episode prediction uses fresh baseline matter and original pi, without parent context or candidate fitting. No old packet or chain is extended.

| Quantity | N512 | N1024 |
| --- | ---: | ---: |
| Long burn minus baseline loss, nat per original row | +.000050303538 | -.000234561953 |
| Conditional contrast MCSE | .000181086496 | .000114265824 |
| Twice conditional contrast MCSE | .000362172992 | .000228531648 |
| Largest selected scalar/predictive split Rhat | 1.001414244 | 1.002368914 |
| Case seconds | 175.427132 | 320.729534 |
| Process peak working set, bytes | 2508582912 | 4335583232 |

The broad precision, chronological-half and selected-Rhat screens also pass at both sizes. MCSE preserves shared-row influence and ordered chains, with 32 chronological batches of 32 draws per chain. Each forecast half pools 2048 complete components. Rows, draws and chains are not independent network preparations, and a size's pass does not replace the other's screen.

The sequential CPU float64 process takes 496.282136 seconds, with zero dense fallbacks in all four posterior calls. N1024's peak is the process high-water mark including the earlier N512 case, not an independently measured incremental allocation. The complete packet has 103 files and 5021034711 bytes. These costs describe the declared realizations/budgets, not a scaling law. No GPU allocation or host change occurs; the GPU is now in the user's use.

## Saved arithmetic and provenance

Three tiny tests pass in two JUnit batches, .459 and .044 seconds; their initial red receipts remain preserved. The first NumPy readers both pass without sampling, fitting or differentiation. [N512 readback](https://github.com/cdenn016/MultiAgentELBO/blob/e7a5c8c0896559422e5b7e8ae80622abb0771136/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-reference-resolution-n512-readback-20261011.json) reconstructs 16777216 densities, 40960 state traces and 58776643 scalar comparisons; [N1024 readback](https://github.com/cdenn016/MultiAgentELBO/blob/e7a5c8c0896559422e5b7e8ae80622abb0771136/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-reference-resolution-n1024-readback-20261011.json) reconstructs 33554432 densities, 40960 traces and 117504067 comparisons. Maximum absolute differences are 4.5474735e-13 and 9.0949470e-13. Each binds 38 frozen source copies and recovers complete-state marks/energies, mixtures, producer-float32 acceptance, scores and screens. These checks concern saved arithmetic, not derivatives or posterior-law accuracy.

The [packet intake](https://github.com/cdenn016/MultiAgentELBO/blob/e7a5c8c0896559422e5b7e8ae80622abb0771136/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-reference-resolution-intake-20261011.json) binds every file under `artifacts/gaussian-reference-resolution/r3-reference-resolution-20261011`. Vault intake separately binds ten Code files: result, contract, PLAN, packet intake, both readers and four green/red JUnit receipts. Canonical Code refs agree at the merge; its 889-byte handoff has SHA-256 `09f0c7fc5b112f750f36f8f54cbcc275154136e42bf09c9a93ef4b1739090190`. No science, completed reader or passing test is replayed during ingestion.

## Relevance and next dependency

[[Staged hierarchy formation and RG composability]] now has conditional reference resolution at both sizes, while native expected accuracy and between-preparation variation remain open. For the next prospectively frozen candidate comparison, working judgment selects fixed accepted time four as primary and time one as paired sensitivity after the user deferred the choice. This is not a rule selected by the user or a convergence/equilibrium claim; the stopping-time result records a precision transient at time one and continuing link-mean motion at time four. Preserve the expected-Hessian flow, .05 proposed step, sixteen fitting draws and 256 evaluation draws unless a separately frozen contract changes them. Count, seeds, clock routing, analysis and each preparation's first reference diagnostics still need freezing before evaluation.

The normalized latent/history model, distinct inference/episode/coarse clocks and fixed-$c_*$ scope remain. No base transport or theory edit follows. Expected native accuracy, actual-law parents, complete retained-state RG, persistent formation and growing size/depth limits remain open in [[Gauge-Theoretic Multi-Agent VFE Model]]. All four gates remain open; the subjective completion estimate stays near 65%. The goal is active, and R4/reward adoption remains pending.
