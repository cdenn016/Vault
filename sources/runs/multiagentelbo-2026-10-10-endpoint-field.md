---
type: run
title: "MultiAgentELBO selected endpoint training-field diagnostic"
aliases: ["Independent endpoint Fisher-field measurements at N512 and N1024"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/info-geometry, cluster/vfe, project/multi-agent, field/statistics, field/mathematics, field/cs-ml]
created: 2026-10-10
updated: 2026-10-10
---

# MultiAgentELBO selected endpoint training-field diagnostic

[Code PR272](https://github.com/cdenn016/MultiAgentELBO/pull/272) publishes the [completed report](https://github.com/cdenn016/MultiAgentELBO/blob/e7877b3ea5bddbeb329e30d763afb63dc8545a66/docs/research/2026-10-03-latent-link-rg-plan/R1-ENDPOINT-FIELD-RESULTS.md) at source revision `e7877b3ea5bddbeb329e30d763afb63dc8545a66`, merged as `ae018c5ee447a5a1bf39ec83accbcbe5936f8203`. The scientific producer ran from clean revision `d22c8016d17d464a53e7fc0cafdd0d1bed2f157a`. These producer, publication and merge revisions have different roles. The consumer follows [[multiagentelbo-2026-10-10-flow-calibration]] and its selection of simultaneous step .05 as the finite predictive-score reference.

```bibtex
@misc{codex2026selectedendpointfield,
  author = {Codex},
  title = {Selected Endpoint Training-Field Diagnostic},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/272},
  note = {Producer d22c8016; result source e7877b3e; conditional held-endpoint diagnostic}
}
```

## Frozen design and execution

The [preregistered contract](https://github.com/cdenn016/MultiAgentELBO/blob/e7877b3ea5bddbeb329e30d763afb63dc8545a66/docs/research/2026-10-03-latent-link-rg-plan/R1-ENDPOINT-FIELD-CONTRACT.md) consumes the selected .05 simultaneous endpoints from eight finite-prior preparations each at N512 and N1024. It holds each endpoint fixed, recomputes its original sixteen-draw fitting-pool field once, then evaluates four fresh independent sixteen-draw full-history pools. The result comprises sixteen endpoints and eighty complete fields. It preserves four generator slices, prefix three, mass sixteen, original source support and `expected_hessian`. Only the first three observed episodes enter diagnostic coefficients. No truth/prior-chain archive, refit, new forecast score, preparation replay or earlier scientific-study replay enters this consumer.

The first execution used isolated Anaconda, CPU float64, sequential MKL and one CPU math thread. Runtime was 1116.731880 seconds; peak process working set was 1435422720 bytes, with 34422452224 bytes of available CPU memory afterward. The GPU had been released after the preceding calibration and was unused here. No timestep, threshold, estimator, fitting budget or longer inference was selected after observing these measurements.

## Measurements and interpretation

The full existing `history_direction` retains receiver and sender forces, every generator slice, analytic prior corrections and temporal mean/Hessian terms. For Gaussian precision $P=LL^T$, it records $L^{-1}g$ and $2^{-1/2}L^{-1}(H-P)L^{-T}$; the source component is the row-centered field weighted by the square root of its source probabilities. The five arrays therefore follow the complete product-Fisher recipe. RMS per stored array element is a declared reporting convention; RMS across different blocks is not an invariant comparison between parameterizations.

Each interval below is the minimum and maximum over eight separately prepared networks of its stated size. These are descriptive ranges, not confidence intervals. Fresh MC RMS standard error estimates uncertainty of the coordinatewise four-pool mean; it is not a bound on the norm, derivative implementation, population field or fitted trajectory.

| Agents | Field block | Fresh mean RMS | Fresh MC RMS standard error | Original-pool minus fresh-mean RMS |
| --- | --- | --- | --- | --- |
| 512 | Matter mean | .213530–.229352 | .020270–.021168 | .043256–.047194 |
| 512 | Matter precision | .155836–.156299 | .007216–.007414 | .015734–.016559 |
| 512 | Source | .167081–.180977 | .018997–.020206 | .042290–.044618 |
| 512 | Link mean | .032152–.034596 | .010326–.010573 | .022084–.022657 |
| 512 | Link precision | .113286–.113378 | .001527–.001564 | .003237–.003364 |
| 1024 | Matter mean | .217814–.228314 | .020289–.020799 | .045284–.046688 |
| 1024 | Matter precision | .155971–.156282 | .007216–.007364 | .016073–.016452 |
| 1024 | Source | .171100–.178899 | .019633–.020027 | .042990–.044621 |
| 1024 | Link mean | .032767–.034434 | .010423–.010511 | .022352–.022880 |
| 1024 | Link precision | .113308–.113397 | .001540–.001561 | .003282–.003388 |

All saved blocks have positive raw noise-debiased fitting-pool/fresh-mean discrepancy mean square, with signed estimates retained and no clipping. Link-mean discrepancy mean square ranges from .000378928 to .000401529 at N512 and .000390481 to .000413461 at N1024. The correction subtracts the estimated variance of the independent fresh mean, conditional on the held endpoint and original fitting pool. That original pool helped determine the endpoint; the correction does not make it independent or establish adaptive optimization bias. Receiver rows, coordinates, pools and optimizer steps are not independent network preparations.

Fresh mean fields retain nonzero components at accepted time one. The calibration's small predictive-score refinement therefore gives no stationarity certificate or whole-state convergence result. Four fresh pools likewise supply no finite-time population trajectory bound, product-family error bound, exact-prior preparation guarantee, posterior mixing guarantee or native-prediction accuracy. The older [[multiagentelbo-2026-10-08-native-calibration]] already separates close forecast scores from substantial field residuals on a different fitted-start single instance; this diagnostic measures the newly selected baseline-start endpoints instead.

## Saved evidence and arithmetic checks

The publication retains the [producer receipt](https://github.com/cdenn016/MultiAgentELBO/blob/e7877b3ea5bddbeb329e30d763afb63dc8545a66/docs/research/2026-10-03-latent-link-rg-plan/evidence/r1-selected-endpoint-field-result-20261010.json), [first actual NumPy reconstruction](https://github.com/cdenn016/MultiAgentELBO/blob/e7877b3ea5bddbeb329e30d763afb63dc8545a66/docs/research/2026-10-03-latent-link-rg-plan/evidence/r1-selected-endpoint-field-reconstruction-20261010.json), [four-case JUnit receipt](https://github.com/cdenn016/MultiAgentELBO/blob/e7877b3ea5bddbeb329e30d763afb63dc8545a66/docs/research/2026-10-03-latent-link-rg-plan/evidence/r1-endpoint-field-tests-20261010.xml) and [source/packet intake](https://github.com/cdenn016/MultiAgentELBO/blob/e7877b3ea5bddbeb329e30d763afb63dc8545a66/docs/research/2026-10-03-latent-link-rg-plan/evidence/r1-selected-endpoint-field-source-intake-20261010.json). Their SHA-256 values are respectively `1db98f63248dc0ed17e406d6cc6b99a16cc49f8aa1ebc22cb4263a21c43afe99`, `3fc9df04d26a5d45944142408ea3f8eed058aa3f2232a6961bb48538f66e029a`, `2bbc36ffd7553a8001abdfaf5ded666690d335cb7c2d1f7d0586d172904b18bc` and `37e671379f78aae7527a193f5a36b7fcdcb7797bd30712b61f436fb2b7158f35`.

Four tiny CPU tests passed in 1.266 seconds with zero failures, errors or skips. They ground the copied-input/prefix consumer, future generator prior and temporal terms, discrepancy reduction and independent-reader fixture. The large diagnostic is a scientific script rather than a unit test. The first NumPy-only reader passed eighty saved blocks and 880 scalar comparisons; maximum absolute difference was 5.551115123125783e-17 under `1e-10 + 1e-9*abs(saved)`. It imported no Torch and executed no field, inference, sampling or GPU operation. This checks reduction arithmetic, not derivatives or population bias. Neither these passing checks nor the producer was rerun during ingestion.

The complete ignored packet `artifacts/gaussian-flow-field-diagnostic/r1-selected-endpoint-field-20261010` contains 209 files and 597286043 bytes, including consumed input copies, four-pool noise, fixed/replicate fields, summaries and fifteen frozen source copies. The intake binds all packet files, twenty-four repository sources, five additional ignored files and two live theory sources. The old 388-file CUDA calibration remains a separate consumed packet. The preceding Code271 canonical handoff briefly stopped when Git changed protected October 9 log line endings; its retained administrative continuation restored exact WIP bytes after checking normalized content. The first partial receipt remains preserved separately from that completed continuation.

## Relevance to this research and next dependency

[[Staged hierarchy formation and RG composability]] now has conditional endpoint measurements of the selected finite flow reference. The live c08b normalized latent joint (`eq:link-latent-joint`), Gaussian Fisher metric (`eq:link-gaussian-fisher`) and horizon-dependent history prior (`eq:link-history-prior`) remain the source model at fixed $c_*$. Inference time, learning episodes and coarse scale stay separate; no base-manifold transport or physical-time Proca simulation is introduced.

The next [fresh N512 native prediction pilot contract](https://github.com/cdenn016/MultiAgentELBO/blob/e7877b3ea5bddbeb329e30d763afb63dc8545a66/docs/research/2026-10-03-latent-link-rg-plan/R3-FRESH-NATIVE-PILOT-CONTRACT.md) is frozen but unimplemented and unrun at this checkpoint. It declares one fresh finite-prior preparation, unchanged simultaneous .05/train16/time-one candidate, and the existing all-row posterior comparator, with separate conditional precision, cost and full-history field reporting. That contract supplies no pilot outcome; even one successful pilot would not estimate between-preparation variation or establish the .01-nat expected native excess-loss target. A later independent multi-preparation comparison requires its own frozen design.

Native prediction, actual-law parent errors, complete retained-state updates, persistent endogenous hierarchy and nonlinear size/depth limits remain open in [[Gauge-Theoretic Multi-Agent VFE Model]]. All four RG completion gates remain open at approximately 65%. R4's conjugate learner and global reward-law candidate remain unadopted. No theory manuscript, generative model, active configuration/default or host setting changed in this ingestion, and no GPU workload was allocated.
