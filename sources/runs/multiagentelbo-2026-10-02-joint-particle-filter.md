---
type: run
title: "MultiAgentELBO joint particle filter, October 2, 2026"
aliases: ["Joint retained particle-filter checkpoint"]
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
year: 2026
created: 2026-10-02
---

# Joint retained particle-filter checkpoint

> [!info] Citation
> MultiAgentELBO project (2026). *Joint retained particle-filter construction and saved-path study*. Code base bc2c338b75e7f44059131927a125cbcaa6d5617a; Research base 08c76ffd04289628080dfad82724394c1f8c2b20. Exact executed source, run metadata, score arrays and JUnit accompany the immutable archive. This continues [[multiagentelbo-2026-10-02-joint-retained-parent]].

## Exact target and executable approximation

The research contract derives the hidden conditional law given the full observed history of block means and source assignments for the existing finite-grid switching law. Each predictor integrates the normalized global hold/redraw source kernel and the projected Gaussian density against its hidden law. Both observed factors reweight the particles before independent multinomial ancestor draws and exact Gaussian propagation conditional on the next block means. Conditional noise uses shared Gaussian innovations to retain the required within-block correlations.

For each fixed independent algorithmic tape, the sequential predictor defines a normalized path law. Averaging its log scores estimates expected tape-conditioned path KL differences. This is generally different from the KL of the tape-marginalized parent; the contract derives the missing nonnegative tape-posterior term. Fixed-history weak consistency follows under the stated positive bounded continuous potentials and multinomial sampling assumptions. It gives no finite-cloud error certificate, dimension-uniform rate, or expected-log-loss convergence without further integrability control. The finite empirical hidden cloud is singular relative to the continuous hidden law, despite its full-support observation predictor.

The live theory continuity is Chapter 11's regular finite-filter definition and pointwise-parent open problem, together with the retained-law and covariance distinctions in pifb2/09_section.tex. The supplied schedule, random resampling and fine-configuration-sized cloud do not meet that regular autonomous reduced-filter obligation. No manuscript theorem was changed.

## Declared experiment and result

One CPU float64 replay used the first 128 saved independent native paths at each of N=512 and 1,024, K=2, block size 16, 64 microsteps over horizon one, and the previously saved activation and structural schedule. It compared persistent clouds of 16 and 64 particles and a fresh activation-conditional reset cloud of 64 particles. The published lifted-source/recognition-drift baseline was reevaluated with pointwise normalized densities on the same observations. Every prediction was scored before assimilation. Native trajectories and learning were not repeated.

All contrasts below are nats per complete path, mean +/- empirical paired standard error. Positive favors the comparator. Relative to the static-lift baseline, persistent16 loses 44.4247 +/- 3.6320 and 97.5648 +/- 7.7971; persistent64 loses 35.5919 +/- 2.9571 and 85.8359 +/- 7.0453; reset64 loses 32.2539 +/- 2.8501 and 80.8525 +/- 6.9838, respectively at N=512 and 1,024. Increasing the persistent cloud from 16 to 64 helps by 8.8328 +/- 1.6137 and 11.7289 +/- 2.2755, but persistent64 still loses to reset64 by 3.3380 +/- 1.1297 and 4.9834 +/- 1.8801.

The mean effective sample size at observed assignment changes is only 1.751 and 1.458 out of 64 for the persistent64 cloud. Hold rows make the all-step median much larger. This is evidence of concentrated particle weights, consistent with approximation error; it does not prove the unique cause of the score deficit. The comparison provides no empirical history advantage for this approximation. It does not rule out a better conditional predictor or useful parent memory.

## Validation and scope

Eight distinct tiny CPU checks passed in two disjoint JUnit packets: four dense-reference Gaussian-conditioning checks and four mixture, full-retention, prefix/tape and baseline-density checks. Initial RED results and the superseded systematic-resampling GREEN are retained separately without double-counting. One study completed in 616.507218 seconds with finite outputs and maximum conditional-projection residual 2.77556e-16. Its pass status means those mechanical gates passed, not that the scientific comparison was favorable.

The immutable archive is sources/archives/multiagentelbo-2026-10-02-joint-particle-filter/. Its two research records use .md.txt filenames; evidence includes source.zip, JSON, score/ESS arrays, logs, test sources and JUnit. Large native predecessor inputs remain local at the locations recorded in metadata. The CUDA-capable interpreter was used for CPU execution; the occupied GPU was not needed. No full suite, historical heavy replay, active configuration or protected WIP was changed.

[[Staged hierarchy formation and RG composability]] and [[Gauge-Theoretic Multi-Agent VFE Model]] retain regular reduced filtering with actual-law error control, endogenous structural feedback, intrinsic recursive formation and general size/depth limits as open obligations. The user requested a break after this phase is ingested, committed, pushed, merged and fast-forwarded. Execution pauses at that checkpoint; this source does not claim completion of the overall renormalization goal.
