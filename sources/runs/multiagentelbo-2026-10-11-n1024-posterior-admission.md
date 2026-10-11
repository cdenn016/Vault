---
type: run
title: "MultiAgentELBO N1024 sparse posterior cost and burn-in admission"
aliases: ["N1024 posterior resource admission and unresolved finer burn sensitivity"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/statistics, field/mathematics, field/cs-ml]
created: 2026-10-11
updated: 2026-10-11
---

# MultiAgentELBO N1024 sparse posterior cost and burn-in admission

The first N1024 CPU execution admits measured cost for the declared sparse posterior profile, with zero dense fallbacks. Its finer burn-in sensitivity screen fails on conditional precision: twice the contrast MCSE exceeds the frozen .0004-nat allowance. The completed packet remains unchanged; this result supplies no candidate fit, stopping-rule decision or mixing certificate.

[Code PR276](https://github.com/cdenn016/MultiAgentELBO/pull/276) publishes the [result report](https://github.com/cdenn016/MultiAgentELBO/blob/7308664d28ae05cabab02f32e7c4332c04bc38db/docs/research/2026-10-03-latent-link-rg-plan/R3-N1024-POSTERIOR-ADMISSION-RESULTS.md) at source revision `7308664d28ae05cabab02f32e7c4332c04bc38db`, merged as `cf8b31480894def94a8c08fbf25ffb3d15037e65`. The scientific producer and prospective contract were committed before execution at clean revision `301caa15b4bc273d4602507e90b4e9c54f2f1161`; the final reader correction is `bcb103be`. These producer, reader, result-publication and merge revisions have separate roles. This follows the N1024 cost obligation left open by [[multiagentelbo-2026-10-10-fresh-native-pilot]].

```bibtex
@misc{codex2026n1024posterioradmission,
  author = {Codex},
  title = {N1024 Sparse Posterior Cost and Burn-In Admission},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/276},
  note = {Producer 301caa15; final reader bcb103be; result source 7308664d}
}
```

## Frozen model and two posterior calls

The [contract](https://github.com/cdenn016/MultiAgentELBO/blob/7308664d28ae05cabab02f32e7c4332c04bc38db/docs/research/2026-10-03-latent-link-rg-plan/R3-N1024-POSTERIOR-ADMISSION-CONTRACT.md) consumes only the exact N1024/preparation-0 model from [[multiagentelbo-2026-10-10-flow-calibration]]: 29506 bytes, SHA-256 `8e2ad527000b4ac5e7387f6a73ca2286b1bd0dce87fdfd06b8a632d3d00fa784`. The 32-by-32 periodic agent lattice has 1024 agents, 2048 primitive edges, real GL+(2) maps, four generator episodes, mass sixteen, width .3 and loop coefficient .25. All source candidates, matter records and normalized generator history remain at fixed $c_*$. Sparse CPU matter factorization retains the declared conditional Gaussian target; these newly generated draws have their own numerical trajectory, and historical packets stay separate.

A fresh one-chain prior preparation uses 256 burn-in and 64 retained sweeps, taking its last complete history to generate four observation episodes. It is a finite-MCMC preparation, not an exact prior draw. Two independent all-row posterior calls use fresh Gaussian-reference initializations and independent chain seeds. Each has four chains and 256 retained sweeps; burn-in is 64 for the baseline and 256 for the sensitivity call. Both condition only on all rows of the first three episodes and retain complete four-episode generators, shared conditional matter and selected source labels. There is no archived realization, fitted candidate or future parent context.

Prediction uses every retained episode-three generator component, fresh baseline matter and original pi. Saved source-component densities and row mixtures retain the original observation channel. The response is composite mean negative log density per original row, rather than full-network joint log density. Shared-row predictive influence, chronological retained halves, disjoint within-chain batches and six selected split-Rhat channels determine the conditional diagnostics. Calls share records and model, but their independent integration variances add in the burn-in contrast.

## Scores and the precision miss

| Quantity | Baseline, burn64 | Long burn, burn256 |
| --- | ---: | ---: |
| Mean original-row loss, nat | 3.971532550080 | 3.971167701505 |
| Conditional score MCSE, nat | .000176058532 | .000168489680 |
| Absolute retained-half score difference, nat | .000019780421 | .000036041554 |
| Largest selected scalar/predictive split Rhat | 1.019448091 | 1.006887619 |
| Posterior seconds, including initialization | 26.644581 | 42.900490 |
| Prediction seconds | 2.352464 | 2.627499 |
| Retained generator/matter/label bytes | 343932928 | 343932928 |
| Sparse-factor dense fallbacks | 0 | 0 |

Long-burn-minus-baseline mean loss is -.0003648485746095 nat per original row, with conditional MCSE .000243691155020589 and twice-MCSE .000487382310041178. The broad contrast-precision, retained-half and selected-Rhat operating screens pass. The finer burn-in screen requires both the absolute contrast and twice-MCSE to be at most .0004. Its observed absolute contrast is within that allowance, while its precision condition fails. This leaves sensitivity unresolved at the preceding pilot contrast's scale; it is not evidence that bias exceeds the allowance or that either call has reached the target posterior. No chain, seed, draw count or completed call is extended or replayed.

## Measured CPU resources

Total elapsed time is 100.7268114 seconds on isolated Anaconda, CPU float64, sequential MKL and one intra/inter-op thread. Prior sampling takes 3.608372 seconds, excluding initialization and persistence; source/input/array persistence takes 22.397277 seconds, excluding final JSON accounting. Process peak working set is 1422082048 bytes, with available system memory 40339107840 bytes before and 38698577920 bytes after. The packet has fifty files totaling 856625309 bytes, including 856110775 NPZ bytes. Both posterior calls incur zero dense fallbacks. These are measured costs for one realization and fixed budgets, not an asymptotic resource bound, speed comparison or GPU estimate. No GPU workload ran.

## Checks, reader stops and retained evidence

Eight tiny CPU tests pass across three recorded batches: five producer tests in .255 seconds, two reader fixtures in .045 seconds and one literal 1/3 acceptance fixture in .032 seconds, with zero errors, failures or skips in each green JUnit receipt. The three red XML receipts remain preserved with their original whitespace. No old test suite or passing batch is replayed during ingestion.

The first actual NumPy reader [stops at acceptance arithmetic](https://github.com/cdenn016/MultiAgentELBO/blob/7308664d28ae05cabab02f32e7c4332c04bc38db/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n1024-posterior-admission-readback-20261011.json): the Torch producer's integer true division rounds to default float32, whereas the reader originally used float64. The maximum discrepancy is 2.3841858e-8 and reconstructing the float32 arithmetic matches exactly. An indentation error in that correction causes the [second stop](https://github.com/cdenn016/MultiAgentELBO/blob/7308664d28ae05cabab02f32e7c4332c04bc38db/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n1024-posterior-admission-readback-float32-20261011.json), recorded as `AttributeError: 'NoneType' object has no attribute 'open'`. Both first outcomes remain retained. Reader corrections leave the scientific packet unchanged; no sampler is rerun.

The final [complete saved-value readback](https://github.com/cdenn016/MultiAgentELBO/blob/7308664d28ae05cabab02f32e7c4332c04bc38db/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n1024-posterior-admission-readback-complete-20261011.json) passes in 15.3271755 seconds. It binds all 37 retained source copies to the scientific producer; reconstructs 8388608 original Gaussian component densities, 10240 complete-state trace entries and 29386819 scalar comparisons; and recovers losses, influences, halves, MCSEs, selected Rhat values and all screen outcomes. Trace reconstruction uses saved generators, shared matter and selected labels, including reversal maps and every observed-prefix row. Maximum absolute difference is 9.094947017729282e-13; maximum tolerance-scaled difference is 3.54488335730712e-5. This checks saved arithmetic without sampling, fitting or differentiating; it supplies no mixing, derivative or native-accuracy certificate.

The [packet intake](https://github.com/cdenn016/MultiAgentELBO/blob/7308664d28ae05cabab02f32e7c4332c04bc38db/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n1024-posterior-admission-intake-20261011.json) binds all fifty files under `artifacts/gaussian-posterior-admission/r3-n1024-posterior-admission-20261011`. Its SHA-256 is `d2f882ca3ed412e1d4318598310ed999d4eb1f5056546890e1e91a83ee128297`. First-stop, correction-stop and complete-reader receipts have SHA-256 values `661dc43cbe19a38f1581df1abe40c6320819a4f0c2b9dc68f9fe442625611697`, `0e43984cfc1db0c8d3534a03bd045687e1c7f71d52039d16016f32776bad0929` and `8718323e5af3a1f8b2abc6f09bd14b7ed868ef517f75eee989bba67992a52f04`, respectively. All three green JUnit files and their red counterparts remain beside these receipts in the Code evidence directory.

Actual canonical Desktop Code `main`, `HEAD` and `origin/main` agree at merge `cf8b31480894def94a8c08fbf25ffb3d15037e65`; the canonical checkout is clean and all fifty packet files are byte/hash checked. The administrative handoff `artifacts/r3-n1024-posterior-admission-handoff-20261011.json` is 840 bytes with SHA-256 `9a54260a0ba02a12b5bba7a735939344e293aee6b9736a844d107cb7442d0507`. Publication bookkeeping does not replay the study.

## Relevance to this research and next dependency

[[Staged hierarchy formation and RG composability]] now has measured N1024 posterior CPU admission, while finer burn-in control remains unresolved. The live c08b normalized latent joint (`eq:link-latent-joint`), Gaussian Fisher metric (`eq:link-gaussian-fisher`) and horizon-dependent generator-history prior/kernels remain the source model. Inference time, generative episodes and coarse scale stay separate. No base transport or physical-time Proca simulator enters this cost study.

Before the independent-preparation candidate comparison, the user must choose the inference stopping rule recorded in [PLAN](https://github.com/cdenn016/MultiAgentELBO/blob/7308664d28ae05cabab02f32e7c4332c04bc38db/docs/research/2026-10-03-latent-link-rg-plan/PLAN.md). This admission selects no candidate stopping time. A later posterior design needs independently frozen counts, seeds and analysis to resolve the finer burn-in precision, preserving this first packet and its miss. The inverse-square-root MCSE projection for a doubled retained count is only a budgeting heuristic, not guaranteed precision or bias control; no new count or study is adopted here.

One preparation and finite scalar diagnostics establish neither posterior mixing nor expected native accuracy, between-preparation variation or candidate superiority. Actual-law parents, complete retained-state RG, persistent hierarchy and nonlinear size/depth laws retain their existing obligations in [[Gauge-Theoretic Multi-Agent VFE Model]]. All four RG gates remain open; approximately 65% remains a subjective overall completion estimate. The autonomous goal is active, with no pause requested in this resumed run. R4 learner/global reward-law adoption remains pending. The user confirmed GPU availability, but this study and ingestion allocate none; no theory, model, active configuration/default or host setting changes.
