---
type: run
title: "MultiAgentELBO first independent matched-time CUDA flow calibration"
aliases: ["Independent CUDA flow calibration at N512 and N1024"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/info-geometry, cluster/vfe, project/multi-agent, field/statistics, field/mathematics, field/cs-ml]
created: 2026-10-10
updated: 2026-10-10
---

# MultiAgentELBO first independent matched-time CUDA flow calibration

[Code PR271](https://github.com/cdenn016/MultiAgentELBO/pull/271) publishes the [result report](https://github.com/cdenn016/MultiAgentELBO/blob/7ef2ba9b52713ab0b5da3cfef9c42db950e9c1f0/docs/research/2026-10-03-latent-link-rg-plan/R1-INDEPENDENT-FLOW-CALIBRATION-RESULTS.md) at source revision `7ef2ba9b52713ab0b5da3cfef9c42db950e9c1f0`, merged as `eb990bfb1cc1f2c3eaf56f0b0b3cb07fe77d4cf4`. The unchanged producer ran once from clean revision `4c44d2bad3d6f9db0c67fd79be1609309065639d`. Publication and producer revisions have different roles.

```bibtex
@misc{codex2026independentcudaflowcalibration,
  author = {Codex},
  title = {First Independent Matched-Time CUDA Flow Calibration},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/271},
  note = {Producer 4c44d2ba; result source 7ef2ba9b}
}
```

## Frozen design and execution

The first registered grid completed sixteen independently seeded finite-MCMC/data preparations: eight at N512 and eight at N1024. Each preparation paired simultaneous finite-width inference, alternating inference and held generator anchors at proposed steps .05, .025 and .0125. All 144 endpoints reached accepted inference time one. The profile retained four episodes, prefix three, mass sixteen, baseline initialization, the `expected_hessian` estimator, sixteen training draws and 256 independent evaluation draws. Float64 execution used `cuda:0`, isolated `C:/anaconda/python.exe`, Torch `2.10.0.dev20251210+cu128`, sequential MKL and one CPU math thread. The two graph aspect ratios remain separate; no size-scaling fit is reported.

Execution took 3311.9052763 seconds. All seven numerical modules matched their prior CUDA-admission hashes before launch. No seed, integration budget, threshold, stopping rule or model changed and the producer was not retried. The 6773 accepted steps include 53 final-clock increments beyond the nominal finite-width and held-anchor counts. Eleven backtracks occurred only in the N512 preparation-4 simultaneous .0125 case, on proposed final increments between 4.440892098500626e-16 and 1.5543122344752192e-15; that case still reached time one. Per-arm accepted clocks and monotone common-sample objective sequences were reconstructed. The held-anchor conditional objective differs from the finite-width objective, so their free energies are not compared.

Peak CUDA allocated/reserved bytes were 280573952/383778816 at N512 and 544104448/719323136 at N1024. The cumulative producer process working-set peak was 1727238144 bytes. GPU use ended at producer termination and the user was notified immediately. Readback, assessment and vault ingestion used CPU/source operations.

## Saved evidence and independent reconstruction

The source revision retains the [producer receipt](https://github.com/cdenn016/MultiAgentELBO/blob/7ef2ba9b52713ab0b5da3cfef9c42db950e9c1f0/docs/research/2026-10-03-latent-link-rg-plan/evidence/r1-independent-flow-calibration-result-20261010.json), [saved-value reconstruction](https://github.com/cdenn016/MultiAgentELBO/blob/7ef2ba9b52713ab0b5da3cfef9c42db950e9c1f0/docs/research/2026-10-03-latent-link-rg-plan/evidence/r1-independent-flow-calibration-reconstruction.json), [frozen assessment](https://github.com/cdenn016/MultiAgentELBO/blob/7ef2ba9b52713ab0b5da3cfef9c42db950e9c1f0/docs/research/2026-10-03-latent-link-rg-plan/evidence/r1-independent-flow-calibration-assessment-20261010.json) and [source/packet intake](https://github.com/cdenn016/MultiAgentELBO/blob/7ef2ba9b52713ab0b5da3cfef9c42db950e9c1f0/docs/research/2026-10-03-latent-link-rg-plan/evidence/r1-independent-flow-calibration-source-intake-20261010.json). Their SHA-256 values are respectively `5d9007c84dce7e0405e1740b4e4ea9e1eb0c75f0d64614b526fd19528619f050`, `fd171107b55e34e080f5cb08157fd9e8b18235dce92e0ad778ae3b63507e77f6`, `25bdf5900f062fa44ceb47b8d7e3085cd6ec80aa159e17a4d3af25041cab9051` and `e0c543efd723b9b9635ae2163dd218df7b99f96e3cc23460c9cb7698340e449f`.

The local packet, `artifacts/gaussian-independent-flow-calibration/r1-independent-flow-calibration-candidate-20261008`, retains 2196591945 NPZ bytes, consumed inputs, endpoints, evaluation draws and original candidate densities. The October 8 suffix is the frozen registration label; execution occurred October 10. The intake binds 388 packet files, 29 repository sources, four additional ignored files and two live theory files. Its dated consulted vault context is separate from those live bindings.

The first reader startup under `C:/Python314/python.exe` failed at `import numpy`, before loading grid data or creating a reconstruction receipt; its original error transcription is retained. The first actual reconstruction used Anaconda's NumPy 2.0.0 on CPU, without importing Torch or allocating GPU memory. It passed in 38.92979360000027 seconds, reconstructing sixteen preparations, 144 endpoints, eighteen exact source copies and 75644928 original Gaussian candidate-density entries. Maximum absolute density discrepancy was 1.7763568394002505e-14; maximum discrepancy scaled by the frozen `1e-9 + 1e-8*abs(saved)` allowance was 9.579413846943815e-8, with one as the boundary. Source support, positive covariances/precisions, held anchors, input copies, evaluation noise and score reductions passed their existing checks. Neither inference nor preparation was replayed.

Forecasts use the prefix-conditioned generator law with fresh matter and the original source prior; fitted past matter/source weights are not reused as future baselines. Truth and prior archives were neither inference nor readback inputs. The response is the original per-record marginal composite loss, rather than a full-network joint log density.

## Frozen assessment and disposition

All 144 conditional scoring screens and 96 step-refinement screens passed their .0025-nat-per-record thresholds. Maximum twice-conditional MCSE was .0007927681452061723; maximum half-pool loss difference was .0013581752371054634. The maximum absolute score-refinement change was .000021647070934882606. The 48 deterministic held-anchor cases have zero evaluation-draw influence, while the 96 stochastic cases also passed. No draws or resolutions were added after the results were observed.

At the finest step, the prespecified paired loss contrasts were:

| Size | First arm minus second arm | Mean loss | Preparation SD | Mean SE |
| --- | --- | ---: | ---: | ---: |
| 512 | simultaneous minus alternating | -3.962532571e-7 | 3.175129543e-6 | 1.122577816e-6 |
| 512 | simultaneous minus held anchor | -.002339110266 | .002773645239 | .000980631679 |
| 512 | alternating minus held anchor | -.002338714013 | .002774210201 | .000980831423 |
| 1024 | simultaneous minus alternating | 1.479807519e-6 | 2.872228347e-6 | 1.015486071e-6 |
| 1024 | simultaneous minus held anchor | -.002809793923 | .002753665345 | .000973567719 |
| 1024 | alternating minus held anchor | -.002811273730 | .002754083814 | .000973715671 |

Each row uses eight complete preparations, and negative values favor the first arm. Receiver rows are dependent and are not independent experimental replicates. Preparation SD/SE describes between-preparation variation separately from conditional evaluation-draw uncertainty. The simultaneous/alternating mean differences are small and change sign with size; finite-width forecasts show modest mean improvements over held anchors. These exploratory contrasts establish neither superiority nor equivalence. Independently seeded finite-MCMC preparations are not exact prior draws.

Select proposed step .05 as the largest tested finite-control reference whose .05/.025 score-refinement comparisons all passed. Retain `expected_hessian`, sixteen training draws, 256 evaluation draws, baseline initialization and inference time one for the later independent-instance comparison. This selects a measured finite approximate control. The screens do not bound mixture bias, rare-component omissions, finite-MCMC preparation error or sixteen-draw training error. Score stabilization does not establish whole-state or population-flow convergence; none of these arms is a native-posterior oracle, so the .01-nat native excess-loss target remains unestablished.

## Relevance to this research

This completes the grid that [[multiagentelbo-2026-10-08-cuda-flow-admission]] left unrun and supplies [[Staged hierarchy formation and RG composability]] with a measured simultaneous-flow reference at fixed $c_*$. The live normalized latent joint and generator-history prior remain the model context; accepted inference time is distinct from learning episodes and coarse scale, and no physical-time Proca simulation or base-manifold transport is introduced. [[Gauge-Theoretic Multi-Agent VFE Model]] next needs native-accuracy/integration and actual-law parent interfaces before persistent endogenous hierarchy and complete retained-state RG closure. Longer inference, fresh-instance confirmation, compatible growing laws and all four RG completion gates remain open. The overall completion estimate remains approximately 65%; the unadopted R4 learner and global reward-law choice stay pending. No manuscript, numerical implementation, scientific default or host setting changed in this result ingestion.
