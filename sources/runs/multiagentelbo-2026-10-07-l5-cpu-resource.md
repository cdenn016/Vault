---
type: run
title: "MultiAgentELBO L5 nonlinear history CPU resource baseline, October 7, 2026"
aliases: ["MultiAgentELBO L5 CPU resources October 7"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, project/multi-agent, field/mathematics, field/statistics, field/physics, field/cs-ml]
created: 2026-10-07
---

# MultiAgentELBO L5 nonlinear history CPU resource baseline

MultiAgentELBO project (2026). *Nonlinear history CPU resource baseline through N8192*. Published as [PR164](https://github.com/cdenn016/MultiAgentELBO/pull/164), merge [a21775218c0501c12853ab6f5e37556349c92bb5](https://github.com/cdenn016/MultiAgentELBO/commit/a21775218c0501c12853ab6f5e37556349c92bb5). Producer revision ae79c28935ac51f6cc0a94e7986232f17e639ec5; saved-only checker bb0f972; results 9701bd06d232a101955a68e95508994413ef7f1f. See the [report](https://github.com/cdenn016/MultiAgentELBO/blob/a21775218c0501c12853ab6f5e37556349c92bb5/docs/research/2026-10-03-latent-link-rg-plan/L5-CPU-BASELINE-RESULTS.md), [frozen CPU contract](https://github.com/cdenn016/MultiAgentELBO/blob/a21775218c0501c12853ab6f5e37556349c92bb5/docs/research/2026-10-03-latent-link-rg-plan/L5-CPU-BASELINE-CONTRACT.md), [producer](https://github.com/cdenn016/MultiAgentELBO/blob/a21775218c0501c12853ab6f5e37556349c92bb5/docs/research/2026-10-03-latent-link-rg-plan/evidence/l5-cpu-producer.json) and [readback](https://github.com/cdenn016/MultiAgentELBO/blob/a21775218c0501c12853ab6f5e37556349c92bb5/docs/research/2026-10-03-latent-link-rg-plan/evidence/l5-cpu-readback.json).

```bibtex
@misc{multiagentelbo2026l5cpuresource,
  author = {{MultiAgentELBO project}},
  title = {Nonlinear history CPU resource baseline through N8192},
  year = {2026},
  howpublished = {MultiAgentELBO PR164, producer revision ae79c28},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/164}
}
```

## Law, runtime and complete output

This separately frozen computational baseline continues the L5 sequence after [[multiagentelbo-2026-10-07-soft-sector-mass]] and [[multiagentelbo-2026-10-07-graded-retention]]. At fixed c_* it retains the existing periodic right/down GL(2,R) generator-history prior, shared primitive reversals, ordered based plaquettes, identity reference metrics, positive anchor precision .3^-2, c=.25, Gaussian episode-increment mass m=16 and horizon T16. The nonlinear factor is exp(-S) relative to the normalized temporal Gaussian reference; its partition constant is not estimated. No matter likelihood, recognition optimization, spectral metric, loop-family change or base transport is introduced.

Use C:/anaconda/python.exe, torch 2.10.0.dev20251210+cu128, NumPy 2.0.0 and CPU float64 with one math thread. Four dispersed chains each take four burn-in and four postburn sweeps, retaining every postburn complete history. Processing order was N8192, N512, N2048. These are short initialized-chain outputs. The GPU was available but occupied, so no GPU run was launched. The CPU calculation supplements the pending CUDA capacity/timing measurement.

| Agents | Sampler seconds | Final checks seconds | Save seconds | Retained history tensor bytes |
| ---: | ---: | ---: | ---: | ---: |
| 512 | .649015 | .062546 | .346980 | 8,388,608 |
| 2,048 | 2.662270 | .266860 | 1.350194 | 33,554,432 |
| 8,192 | 11.079382 | 1.206204 | 5.383513 | 134,217,728 |

Compressed state archives were 13,541,899, 54,173,666 and 216,695,757 bytes respectively. Full initial/final states, all retained histories, raw scalar traces, common noise, topology, metadata and loaded source copies are retained in the canonical `MultiAgentELBO/artifacts/gaussian-latent-history/l5-resource-cpu-20261007` archive. Host working-set peaks and CUDA allocator peaks are unmeasured. Named tensor bytes may overlap through aliases. One case per size gives observed costs, not a confidence interval, scaling exponent or universal capacity claim.

## Saved-value reconstruction and limits

A separate NumPy checker imports no producer or scientific package. It reconstructs matrix exponentials from Cayley–Hamilton in all real discriminant branches, the normalized temporal reference from a dense covariance inverse, ordered loop products, scalar channels, finite diagnostics, topology and counts. One tiny SciPy branch-oracle test passed (JUnit .241 seconds); the intended missing-module red result was preserved. Previously passing tests and the scientific producer were not repeated.

Saved-only reconstruction passed 195 array comparisons over 11,161,356 entries in 4.695725 seconds. Maximum discrepancy was 2.9103830457e-11. All 48 retained and twelve initial complete histories were checked, covering 3,440,640 based plaquette products. All postburn scalar channels and reported diagnostics agree with the independent arithmetic. Four unsaved burn-in states per chain cannot be reconstructed; their traces were checked only for finite values and counts. This is finite-instance numerical consistency, not proof adjudication or a continuous-law certificate.

Split Rhat reached 2.860500 and estimated ESS fell to 6.308316, with a sixteen-draw cap. The short resource budget therefore does not meet the older 200-draw accuracy screen or resolve initialization bias. Final generator maxima and link singular extrema are descriptive initialized-state measurements, not stationary noncompact tails, rare-region frequencies, O5 connection-eigenvalue scaling or formation evidence.

## Relevance and continuation

The CPU execution path now has measured evidence through N8192 for [[Gauge-Theoretic Multi-Agent VFE Model]] and [[Staged hierarchy formation and RG composability]]. This does not resolve the support/relaxation/prediction distinction in [[Meta-agents and hierarchical emergence]] or [[Cellular sheaves and sheaf Laplacians]]. Nonlinear sampling accuracy and tail/rare-event observables require a separately frozen study; CUDA profiling waits for a free compute slot. Strong O1 non-isometry, O3 metric choice, graph-family S1, original collective dynamics, continuous-target accuracy, independent-instance prediction and thermodynamic closure remain open. The full RG goal is active. Navigation: [[Mathematics MOC]], [[Statistics MOC]], [[Physics MOC]] and [[CS-ML MOC]].
