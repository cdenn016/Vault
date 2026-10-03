---
type: run
title: "MultiAgentELBO source-adapted Gaussian parent, October 2, 2026"
aliases: ["Source-adapted Gaussian parent checkpoint"]
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
year: 2026
created: 2026-10-02
---

# Source-adapted Gaussian parent checkpoint

> [!info] Citation
> MultiAgentELBO project (2026). *Source-adapted Gaussian parent and path-error records*. Executed snapshots record code base 868cf239f9c2972ef66962e10ad33eda02d595e8; their implementation was published in code PR109 at 727b14750beb28fe4d3ebf4fa782ba748c7e81d7. Research publication base 208e44d includes the intervening link-origin work. Exact executed source, declared profile, metadata, pointwise scores and JUnit are retained in sources/archives/multiagentelbo-2026-10-02-source-adapted-gaussian/. This continues [[multiagentelbo-2026-10-02-joint-particle-filter]] after the user resumed the autonomous goal.

## Predictor and comparison

The saved particle-loss decomposition locates most of the predecessor deficit in source prediction. The new predictor processes receiver labels in ascending order with shared positive spherical cubature, adapting a Gaussian mean and full covariance after each label. Regression retains residual covariance. Frozen-assignment propagation includes sender forces and full propagated covariance; the next block means condition that Gaussian exactly. This is a normalized assumed-density approximation, not the native hidden posterior.

The global source law includes hold and same-assignment refresh. The economical convention uses the unchanged hold Gaussian whenever the complete assignment stays unchanged. Changed assignments use source adaptation. A declared old-matching-prefix cutoff of 1e-12 freezes only sufficiently rare matching prefixes and supplies normalized point-source suffix rows. Its path total-variation bound below 1e-12 compares two candidate algorithms, not either candidate to the native law. Zero disables the cutoff; the hard cutoff can break smoothness.

One CPU float64 replay used the first 32 existing native paths at each of N=512 and 1,024, K=2, blocks of 16, and all 64 steps over horizon one. Activation, mobility, model, rate-one refresh and externally supplied structural schedule are unchanged. The matched reset Gaussian uses the same algorithm but restarts at the activation conditional for each R_t. The graph has source offsets 1 and 17 modulo N with independent GL+(2,R) comparison maps, declared link scale 0.2 and temperature 0.5. No native path, learning schedule or algorithmic random tape was regenerated.

| Agents | Gaussian minus baseline | Gaussian minus reset Gaussian |
| --- | --- | --- |
| 512 | -5.0089 +/- 1.4985 | -5.4287 +/- 1.6054 |
| 1024 | -9.8744 +/- 1.9771 | -10.8093 +/- 2.1081 |

Entries are nats per complete path, mean +/- empirical paired standard error; positive favors the second arm. The same first-32 subset is used for the older particle64/reset64 comparisons in the archive. Source and conditional-configuration contributions are recorded separately. Each size has one model and learned schedule (declared model seed 20261002; base path seed 20261004), so this is [underpowered] for generalization across model/link realizations. Choosing this candidate after predecessor scores does not make the reused data an independent held-out validation.

## Analytical continuation and remaining error

The existing augmented upper functional can be estimated from saved native source likelihoods, candidate joint scores and the known projected Gaussian noise entropy. For a fixed candidate its expectation is retained joint-path KL plus a candidate-independent nonnegative information gap. Its finite-sample estimate is not a confidence upper bound or the KL with that gap removed. The Gaussian functional estimates are 49.7826 +/- 11.9686 and 79.4122 +/- 18.5936 nats per path at 512 and 1,024 agents. The posthoc calculation requires no fine-state replay; particle comparisons retain tape-conditioned risk semantics.

A separate construction supplies an autonomous continuous-time Gaussian-message parent for frozen coefficients and fixed projection. Correlated-noise propagation, positive covariance, smooth uncut source jumps, nonexplosion, a deterministic retained-history functional and an L1-smooth Gaussian decoder establish the stated regular-filter conditions. Its Gaussian propagation omits the native no-change survival correction, and its source jumps use projection and cubature. It is a related full-covariance candidate, not a proved limit of the scheduled cutoff replay.

The continuous actual-law budget follows by lifting this parent to a comparison fine law with identical retained marginal, changing only projected drift and visible assignment intensities. A stopped likelihood argument and entropy contraction yield a path-KL bound with projected drift cost and visible-jump likelihood plus survival compensation. The expected budget may be infinite; no small or uniform asymptotic error follows. The earlier discrete residual route applies to exact integrated Kq, with a different scope from the sequential cubature replay.

## Validation and scope

Thirteen distinct tiny CPU checks passed in three disjoint final JUnit packets: four propagation/conditioning checks in 0.573 seconds, eight source/integration checks in 1.901 seconds, and one serial-versus-spawn transport check in 2.012 seconds. The transport packet confirms exact output equality for both deterministic arms. They check normalized source rows by tiny exact enumeration, dense Gaussian regression and propagation formulas, sender contributions, full-retention native joint density, and causal replay. Historical RED/fixture/sender-accumulation failures remain preserved. The serial run completed its 512-agent case and part of its 1,024-agent case before a documented runtime scheduling continuation. Four single-threaded CPU workers evaluated only missing arm/path pairs, retaining completed results. The continuation took 3365.530982 seconds; pass denotes all declared scores complete and finite with observed-fiber residuals below 1e-9. The interrupted original status, source and elapsed records remain archived; no completed pair was rerun.

The dense covariance scales quadratically with fine dimension and is larger than a fine configuration vector; all source labels remain retained. The profile does not establish computational state reduction, endogenous structural learning, intrinsic recursive formation, or the general size/depth limit. No GPU, full suite, historical heavy node or active configuration change was used. [[Staged hierarchy formation and RG composability]] and [[Gauge-Theoretic Multi-Agent VFE Model]] retain O1 actual-law error control on the required windows and O4 as open obligations.
