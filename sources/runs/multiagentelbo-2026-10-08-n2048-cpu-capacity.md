---
type: run
title: "MultiAgentELBO four-episode N2048 CPU capacity admission"
aliases: ["N2048 four-episode CPU capacity"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/info-geometry, cluster/vfe, project/multi-agent, field/statistics, field/mathematics]
created: 2026-10-08
updated: 2026-10-08
---

# MultiAgentELBO four-episode N2048 CPU capacity admission

[Code PR194](https://github.com/cdenn016/MultiAgentELBO/pull/194), result revision `56c2996885cc11714ac7e6633338d382616c49dd`, records one fresh resource preparation and three CPU controls at fixed $c_*$. The numerical producers executed once at clean revision `e650bdbd845b03e162a0d8150bc31a5f3da0d60c`, following the implementation checkpoint in PR193. This continues [[multiagentelbo-2026-10-08-discarded-energy-device-admission]] and [[multiagentelbo-2026-10-08-filter-boundary-learning-domain]]. The [result report](https://github.com/cdenn016/MultiAgentELBO/blob/56c2996885cc11714ac7e6633338d382616c49dd/docs/research/2026-10-03-latent-link-rg-plan/R1-N2048-CAPACITY-RESULTS.md) links the frozen contract, producer receipts and two independent NumPy saved-value readbacks.

```bibtex
@misc{codex2026n2048cpucapacity,
  author = {Codex},
  title = {Four-Episode N2048 CPU Capacity Admission},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/194},
  note = {Result revision 56c2996885cc11714ac7e6633338d382616c49dd; producer revision e650bdbd845b03e162a0d8150bc31a5f3da0d60c}
}
```

## Preparation and execution

The positively anchored real GL+(2) model uses a 32-by-64 periodic graph, 4096 shared primitive links, original nonlinear plaquettes, temporal mass 16, four generator episodes and a three-episode observed prefix. The existing sixteen-episode N2048 archives cannot supply this finite-horizon law by truncation. One chain therefore executes 256 burn-in and 64 retained sweeps with thinning one, selecting whole history 63 before outcomes. Its prior/data/training/forecast seeds are 202610132, 202610133, 202611116 and 202612116. This is one resource realization outside the sixteen-instance N512/N1024 calibration population; finite-MCMC prior approximation and initialization bias remain uncertified.

Preparation takes 9.132816 seconds, including 7.085312 seconds of sampling, and retains 74,337,463 preparation NPZ bytes. Its cumulative process peak is 713,416,704 bytes. Simultaneous, alternating and held-anchor controls then start from identical saved baseline inputs, with sixteen common training draws and 256 separate forecast draws. All reach accepted inference time .1 in two .05 steps without backtracking. Total flow duration is 172.358929 seconds, cumulative process peak is 1,981,579,264 bytes and retained flow NPZ storage is 148,986,867 bytes. These are CPU float64 measurements under isolated Anaconda, sequential MKL and one math thread. The held-anchor objective is a separate conditional counterfactual.

Future marginal original-row losses are 3.997045295598, 3.997045171263 and 3.999952113506 nats for simultaneous, alternating and held-anchor respectively. The finite-width future generator means differ by at most 1.19745093e-4, while their future precisions coincide. The mean simultaneous-minus-alternating log score is -1.24335350e-7. These descriptive values establish execution of the second-step feedback difference, without a predictive-advantage or convergence claim. Receiver count is not an independent-instance count; the score is composite, not the whole-network likelihood.

## Evidence and limits

Both NumPy-only saved-value reconstructions pass once. They reconstruct topology and coefficients, full-history selection and trace alignment, baseline state, diagnostic/input separation, byte accounting, source/input copies, accepted clocks, descent diagnostics, positive-definite endpoint covariance/precision, normalized source rows, exact held anchors, score reductions and Gaussian forecast-noise recovery. Maximum score and noise discrepancies are 1.77635684e-15. No sampler or inference is rerun for these checks. The earlier fifteen tiny routing/helper tests belong to the implementation checkpoint and are not rerun here. This realization has no hard-zero source entries.

The result admits the declared N2048 CPU shape and budget. It establishes neither posterior accuracy, stationarity, independent-instance predictive improvement, endogenous formation nor a nonlinear growing-size/depth limit. CUDA remains unrun while another Python workload occupies the GPU; the N512/N1024 and N2048 device comparisons are still required before enabling the full independent calibration. Both historical N8192 readback failures and all four RG completion gates remain open. No reward alternative is adopted, manuscript is edited, full suite is run or historical study is retried.

## Relevance to this research

[[Gauge-Theoretic Multi-Agent VFE Model]] gains the missing CPU capacity endpoint needed to budget the simultaneous finite-width reference. [[Renormalization-group flow of beliefs]] continues to distinguish finite numerical admission from the complete operational retained-state and thermodynamic obligations. The frozen paired assessment can consume the full matched-time calibration after device admission; capacity alone supplies no scientific gate closure.
