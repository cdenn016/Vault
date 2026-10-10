---
type: run
title: "MultiAgentELBO first fresh N512 native prediction pilot"
aliases: ["Fresh finite-posterior comparison for the selected simultaneous flow"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/info-geometry, cluster/vfe, project/multi-agent, field/statistics, field/mathematics, field/cs-ml]
created: 2026-10-10
updated: 2026-10-10
---

# MultiAgentELBO first fresh N512 native prediction pilot

[Code PR273](https://github.com/cdenn016/MultiAgentELBO/pull/273) publishes the [completed report](https://github.com/cdenn016/MultiAgentELBO/blob/6c424c3446bbb7723c37819edc26b0a2a1c970c9/docs/research/2026-10-03-latent-link-rg-plan/R3-FRESH-NATIVE-PILOT-RESULTS.md) at source revision `6c424c3446bbb7723c37819edc26b0a2a1c970c9`, merged as `3f3d60d233a1aa94718056a4750e20e7ee139091`. The first scientific execution ran from clean producer revision `41b03d0f76196e7ea8228363ee29b766fbe1fa81`. Producer, publication and merge revisions have different roles. This completes the fresh pilot that [[multiagentelbo-2026-10-10-endpoint-field]] recorded as contract-only; that immutable source retains its earlier checkpoint status.

```bibtex
@misc{codex2026freshnativepilot,
  author = {Codex},
  title = {First Fresh N512 Native Prediction Pilot},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/273},
  note = {Producer 41b03d0f; result source 6c424c34; one finite-MCMC preparation}
}
```

## Frozen preparation and comparison

The [frozen contract](https://github.com/cdenn016/MultiAgentELBO/blob/6c424c3446bbb7723c37819edc26b0a2a1c970c9/docs/research/2026-10-03-latent-link-rg-plan/R3-FRESH-NATIVE-PILOT-CONTRACT.md) reuses only the exact N512 model tensors from [[multiagentelbo-2026-10-10-flow-calibration]]. The real GL+(2) periodic 16-by-32 lattice retains four generator episodes, three observed episodes, mass sixteen, width .3, loop coefficient .25 and four original source candidates per receiver. Eight random seed namespaces were frozen before generating data. A newly initialized one-chain nonlinear prior uses 256 burn-in and 64 retained sweeps; its last full history generates new matter, source labels and original records. This is one finite-MCMC preparation, not an exact prior draw. No old calibration realization, fitted endpoint or truth context enters either fit.

The candidate starts from the admitted baseline and retains simultaneous `expected_hessian`, sixteen fixed full-history draws, step .05 and accepted inference time one. It completes twenty accepted steps without backtracks. The comparator is one uninterrupted all-row posterior call with four independently initialized chains, 64 burn-in and 256 retained sweeps. Complete generator histories, shared conditional matter/source labels, ordered scalar traces and acceptance remain saved. Only `observations[:3]` conditions either fit; no future parent context is supplied.

Candidate prediction uses 256 fresh episode-three generator components; reference prediction uses all 1024 ordered retained components. Both use fresh baseline matter, original pi and normalized per-record source mixtures. The response is composite mean negative log density per original record, rather than a full-network joint score. Shared receiver rows remain together in density influences; reference MCSE uses sixteen chronological sixteen-draw batches per chain. Candidate/reference integrations are independent, so their estimated contrast variances add.

## Realized score and necessary screens

| Predictor | Mean loss, nat per record | Conditional MCSE | First/second-half mean-score difference |
| --- | --- | --- | --- |
| Selected product recognition | 3.967656459219018 | .000353504210071 | .000068358175979 |
| Finite all-row posterior reference | 3.968069512280581 | .000240578471504 | .000596241184559 |

Candidate-minus-reference loss is -.000413053061563 nat per record, with conditional MCSE .000427601715957. This small realized contrast lies within twice that estimated conditional MCSE and establishes neither superiority, equivalence nor expected native accuracy. Rows, integration draws and chains are not independently prepared networks.

| Frozen necessary screen | Observed value | Upper bound | Outcome |
| --- | --- | --- | --- |
| Twice contrast MCSE | .000855203431913 | .0025 | Passed |
| Reference half difference | .000596241184559 | .005 | Passed |
| Candidate half difference | .000068358175979 | .0025 | Passed |
| Maximum selected reference scalar/predictive split Rhat | 1.006746129357710 | 1.05 | Passed |

The selected Rhat values cover five posterior scalar traces and the mean predictive-density influence. Finite scalar screens do not certify mixing or bound initialization bias. The comparator remains a finite posterior approximation. No chain, pool, inference interval, seed or tolerance was extended, and the first pilot was neither retried nor replayed. One preparation supplies no between-preparation variance estimate or guarantee of the .01-nat expected native excess-loss target.

## Complete history fields

Four fresh sixty-four-draw full-history pools are shared between the held baseline and endpoint. The original sixteen-draw endpoint fitting field is evaluated once. The complete five-block product-Fisher recipe retains sender/receiver terms, all four generator slices, prior and temporal terms. Per-stored-element RMS follows the existing endpoint convention; cross-block comparisons are not invariant parameterization comparisons, and the MC RMS standard error is conditional sampling uncertainty rather than a norm or trajectory bound.

| Block | Start fresh mean RMS | Start MC RMS standard error | Endpoint fresh mean RMS | Endpoint MC RMS standard error | Endpoint fitting-pool/fresh-mean RMS |
| --- | --- | --- | --- | --- | --- |
| Matter mean | 2.302865 | .031746 | .228967 | .010361 | .043412 |
| Matter precision | 1.149929 | .015939 | .155848 | .003660 | .015381 |
| Source | .025861 | .025981 | .179986 | .010121 | .040847 |
| Link mean | .109200 | .028672 | .032777 | .005241 | .020832 |
| Link precision | .886839 | .006192 | .113333 | .000770 | .003073 |

Signed corrections remain unmodified: the start source noise-debiased mean-square estimate is -6.207455792068737e-6, with no clipping to zero. Endpoint fitting-pool/fresh-mean corrected discrepancies are positive in all five blocks; the link-mean value is .000406514596613. The original pool helped determine the endpoint, so subtracting fresh-mean sampling variance does not make the original pool independent or establish adaptive optimization bias. Endpoint fields remain nonzero and the source field changes substantially. Score agreement and these finite field measurements give no stationarity certificate, population trajectory bound or product-family error bound.

## Cost, saved evidence and arithmetic checks

The CPU float64 run used isolated Anaconda, sequential MKL and one math thread. Total runtime was 645.9959176 seconds: prior sampling 2.2206124 seconds, candidate fitting 175.9407456 seconds and posterior reference 155.6817389 seconds, with prediction, nine field evaluations and persistence comprising the remainder. Peak process working set was 2113970176 bytes; available memory before/after was 40478765056/39273295872 bytes. No GPU workload occurred. These are measured N512 costs, not an N1024 admission or a GPU estimate.

The [producer receipt](https://github.com/cdenn016/MultiAgentELBO/blob/6c424c3446bbb7723c37819edc26b0a2a1c970c9/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-fresh-native-pilot-result-20261010.json), [first actual NumPy reconstruction](https://github.com/cdenn016/MultiAgentELBO/blob/6c424c3446bbb7723c37819edc26b0a2a1c970c9/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-fresh-native-pilot-reconstruction-20261010.json), [six-case JUnit receipt](https://github.com/cdenn016/MultiAgentELBO/blob/6c424c3446bbb7723c37819edc26b0a2a1c970c9/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-fresh-native-pilot-tests-20261010.xml) and [source/packet intake](https://github.com/cdenn016/MultiAgentELBO/blob/6c424c3446bbb7723c37819edc26b0a2a1c970c9/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-fresh-native-pilot-source-intake-20261010.json) retain the first outcome. Their SHA-256 values are respectively `2ed42038059f79f227418af3a18a1607878cca4073bfe56b6c75d5fc43832dae`, `8f1ecedcb71df7fb5cd378786a0cdd3168c741b064cbdce97a3bd8f3a65a1e4b`, `415598e68e9423b46d8bb214671d5141fa5c97818fdce970f4a998e5d8c99196` and `c8fccf7551db2e3c18af02d4de2e81524d17972b6983c408fbe92c562947361a`.

Six tiny CPU tests pass in 1.268 seconds, with zero errors, failures or skips, grounding future-query exclusion, independent initializations, baseline/original-pi prediction and shared-row/ordered-chain precision reductions. Four initial missing-module failures remain separately retained. Only formula docstrings changed after the passing batch; executable tested helpers were unchanged and passing tests were not rerun. The first NumPy-only reader passes 2621440 rebuilt component-density entries and 8135033 scalar comparisons, including mixtures, influences, halves, six reference Rhat values, signed field summaries and the accepted clock. Maximum absolute discrepancy is 8.881784197001252e-15; maximum tolerance-scaled discrepancy is .000037620587677. It imports no Torch and executes no sampling, inference, field or GPU operation. These are arithmetic checks, not derivative, mixing, exact-law or expected-loss certificates.

The complete packet `artifacts/gaussian-fresh-native-pilot/r3-fresh-n512-native-pilot-20261010` contains 55 files totaling 282012582 bytes: 281573796 NPZ bytes, 329777 bytes of thirty-three frozen source copies and 93369 bytes of copied model/intake inputs, with other receipts completing the total. The source intake binds all packet files, forty-two repository sources, five additional ignored files and two live theory sources. The completed CUDA calibration and endpoint diagnostic remain unchanged and unreplayed.

The canonical Code handoff completed on its first invocation. Actual Desktop `main`, `HEAD` and `origin/main` agree at the Code273 merge; forty-two repository bindings, fifty-five packet files plus five ignored evidence files and twenty-five prior receipts are preserved. Seven tracked and twenty-one untracked WIP paths remain protected, with original October 9 log line endings restored. The local receipt `artifacts/r3-fresh-native-pilot-handoff-20261010.json` has SHA-256 `e0dec9abe6e2bf9986aa9df1e4e316a721c35c28afc3720b72057db1ba2a0f63` in both checkouts. This is publication bookkeeping rather than scientific execution.

## Relevance to this research and requested break

[[Staged hierarchy formation and RG composability]] now has an admitted fresh N512 candidate/finite-posterior comparison path and its measured conditional precision/cost, following the selected finite flow reference. The live c08b normalized latent joint, Gaussian Fisher metric and horizon-dependent generator-history kernels remain the fixed-$c_*$ source model. Inference time, episodes and coarse scale stay distinct; no base-manifold transport or physical-time Proca simulation enters this consumer.

The user requests a break after publication, wiki ingestion and actual canonical Desktop synchronization. No further study begins at this checkpoint. On resumption, the independent-preparation native comparison needs its own frozen preparation count, conditional precision and analysis before evaluation. Finite-prior preparation bias, posterior initialization/mixing error, population-field error and product-family approximation remain distinct from between-preparation variation. N1024 posterior cost requires separate admission because conditional matter sampling factors dense 2N-by-2N precision; this N512 result supplies no such admission.

Expected native accuracy, actual-law parent errors, complete retained-state RG, persistent endogenous hierarchy and nonlinear size/depth limits remain open in [[Gauge-Theoretic Multi-Agent VFE Model]]. All four completion gates remain open at approximately 65%; the R4 learner/global reward-law candidate stays unadopted. No manuscript, generative model, active configuration/default, host setting or GPU workload changed during ingestion.
