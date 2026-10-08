---
type: run
title: "MultiAgentELBO retained-input CUDA flow admission and calibration preparation"
aliases: ["Retained-input CUDA flow admission"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/info-geometry, cluster/vfe, project/multi-agent, field/statistics, field/mathematics]
created: 2026-10-08
updated: 2026-10-08
---

# MultiAgentELBO retained-input CUDA flow admission and calibration preparation

[Code PR196](https://github.com/cdenn016/MultiAgentELBO/pull/196), admission/preparation revision `e5c91e2c44ce01a767b2ef31f328eba2f51f3360`, contains the [admission report](https://github.com/cdenn016/MultiAgentELBO/blob/e5c91e2c44ce01a767b2ef31f328eba2f51f3360/docs/research/2026-10-03-latent-link-rg-plan/R1-CUDA-ADMISSION-RESULTS.md) and [calibration execution contract](https://github.com/cdenn016/MultiAgentELBO/blob/e5c91e2c44ce01a767b2ef31f328eba2f51f3360/docs/research/2026-10-03-latent-link-rg-plan/R1-CUDA-CALIBRATION-EXECUTION.md). Both CUDA producers ran from clean `d93ea395585620261a68b18206c239ff8716f97c`; result ingestion does not change their producer revision.

```bibtex
@misc{codex2026cudaflowadmission,
  author = {Codex},
  title = {Retained-Input CUDA Flow Admission and Calibration Preparation},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/196},
  note = {Producer d93ea395; admission and prepared-runtime revision e5c91e2c}
}
```

## Execution and evidence

Two single attempts reused the exact completed CPU inputs for N512/N1024 and the separate N2048 resource instance. All nine simultaneous, alternating and held-anchor arms reached accepted inference time .1 in two .05 steps without backtracking. All recorded acceptance routes matched the CPU references. State and original-record score arrays passed `1e-9 + 1e-8*abs(CPU)` allowances; the largest scaled difference was 1.1987614960233908e-6, where one is the boundary. Topology, reversals, hard-zero support and consumed inputs matched exactly.

The N512/N1024 producer took 9.739880 seconds and retained 111753757 NPZ bytes; N2048 took 10.853907 seconds and retained 148987568 NPZ bytes. Maximum CUDA allocated/reserved peaks across the arms were 1071165440/1426063360 bytes. Both separate NumPy-only saved-value reconstructions passed once, including covariance positivity, source normalization, clocks, score reductions, future-noise recovery and independent CPU/CUDA comparisons. No CPU inference or preparation was repeated. Canonical Desktop copies of both CUDA archives were checked against every source file byte.

Fifteen distinct tiny routing, numeric-reference, independent-density and unchanged-default-gate checks passed in retained JUnit packets. The prepared CUDA calibration profile preserves selected-entrypoint isolated restart, source/prerequisite byte copies and memory reporting while leaving the core CPU/disabled defaults unchanged. A new saved-only checker independently reconstructs original Gaussian component densities and the complete 144-case grid; its production reconstruction remains unrun.

The registered target-time-one calibration remains unrun because the user reclaimed the GPU before launch. Its unique output directory is absent and no calibration process was started. Existing seeds, sixteen preparations, step resolutions, budgets, score screens and assessment contrasts remain frozen. The user was notified that our GPU work finished; CPU/source work continues under the active goal.

Short-interval device agreement does not establish population-flow or native-posterior accuracy, predictive superiority, formation or a thermodynamic limit. The independent grid and its assessment remain separate next work. All four scientific RG gates and the global reward-law choice remain open; neither historical N8192 readback failure was retried. Manuscripts and earlier immutable sources were not edited.

## Relevance to this research

[[Gauge-Theoretic Multi-Agent VFE Model]] now has measured CUDA numerical/resource admission for the retained finite-width control shapes. [[Renormalization-group flow of beliefs]] still requires actual-law prediction, compatible complete retained state, nonlinear size/depth limits and endogenous persistent hierarchy. This continues [[multiagentelbo-2026-10-08-n2048-cpu-capacity]] and [[multiagentelbo-2026-10-08-nonlinear-decoder-bound]] without treating capacity evidence as scientific closure.
