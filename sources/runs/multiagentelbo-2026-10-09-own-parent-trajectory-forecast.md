---
type: run
title: "Own-retained parent trajectories and original future forecasts"
aliases: ["N512 own-retained parent path and forecast comparison"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Own-retained parent trajectories and original future forecasts

[Code PR211](https://github.com/cdenn016/MultiAgentELBO/pull/211), merged at `4dfbae9ce96a3fc4f3124526c218dea0a2f34f46`, records completed own-state continuations following [[multiagentelbo-2026-10-08-lifted-parent-field]]. Two alternative 128/32-parent candidates each advance for four steps from their own retained state, once from clean published `cd3f4730477b58ec700674116c647248d3d46049`. Independent trajectory replay passes 911 comparisons over 22,734,861 entries, maximum absolute discrepancy $1.0658141036401503\times10^{-13}$ against the frozen $10^{-8}$ allowance. [Code PR212](https://github.com/cdenn016/MultiAgentELBO/pull/212), merged at `d5190d5006f21b2e99bb13ef1a42c4a29b60f59e`, records the subsequent once-run original-forecast consumer: 390 independent comparisons over 5,238,382 entries, maximum discrepancy $1.0658141036401503\times10^{-14}$. This supplies one short coupled recurrence and a terminal recognition-reference comparison. Continuous accuracy, hidden-parameter filtering and all four RG gates remain open.

```bibtex
@misc{codex2026ownparenttrajectoryforecast,
  author = {Codex},
  title = {Own-Retained Parent Trajectories and Original Future Forecasts},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/212},
  note = {Trajectory PR211, merge 4dfbae9c, execution cd3f4730; forecast PR212, merge d5190d50, execution 4dfbae9c; finite N512 recognition-reference comparisons}
}
```

## Own-state reconstruction and complete fields

The [trajectory contract](https://github.com/cdenn016/MultiAgentELBO/blob/4dfbae9ce96a3fc4f3124526c218dea0a2f34f46/docs/research/2026-10-03-latent-link-rg-plan/R3-RETAINED-PARENT-TRAJECTORY-CONTRACT.md) preserves the original N512/E1024 real GL(2), mass-16 model, source support, order-nine rule with 6,561 nodes, fixed probe/trees and observed prefix slices zero through two. Each candidate retains parent mean M, the two earlier fine means, all three matter-covariance/source slices and all four original generator-mean/full-precision slices. The selected fine mean is absent from its persistent state.

At every old retained state, its own signed moments give the complete receiver/sender quadratic K, information h0 and center $u=K^{-1}h_0$. Its own precision-Cholesky probe and rooted tree give A, while $C=\operatorname{diag}(\Sigma_i)$. The retained-only reconstruction is

$$
\widehat\mu=u+CA^T(ACA^T)^{-1}(M-Au).
$$

This numerical mean is held as an independent matter coordinate during the full original-objective field differentiation. Original record, ordered-loop, Gaussian/source-prior and history-kinetic forces remain active. The original five-family raw Brownian tuple drives the positive Fisher proposal at $h=1/40000$, $T=1/20$. The new geometry/covariance coarsens the proposal, and its selected fine mean is discarded before the next step. Later fine checkpoints supply comparisons only; no truth-state reset, new draw, observation, clipping or scientific retry enters either recurrence.

There are eight reconstruction moment banks, eight full fields/proposals and 64 explicit signed-moment banks before autograd checkpoint replay. The separate reader performs 32 signed-value and 32 complete generator-derivative passes, checking 131,072 generator mean entries and 327,680 independent symmetric precision coordinates, as well as complete matter/source fields, proposals, maps and every retained recurrence. Original copy identities and staged/direct composition are preserved. These are separate candidates with supplied memberships, rather than two levels of one evolving or endogenously formed hierarchy.

The candidate-specific mean radius three was frozen before execution because the older lifts exceeded radius two. Every reconstruction and raw proposal passes that candidate box with zero allowance; the older native radius-two exit certificate remains unchanged. The separate rational same-state component budget gives q=$4.221719719741383\times10^{-7}$ and delta=$3.588461761780176\times10^{-5}$, excluding computed/input arithmetic, lift sensitivity and continuous containment. At the endpoint, parent-mean RMS differences from the common-driver native trajectory are $3.591012445641124\times10^{-4}$ and $2.561320995346368\times10^{-4}$. These different maps/dimensions do not rank compression or prediction. The inference window is only $10^{-4}$ and supplies no nonstationary population or expected-path claim.

Retained M is a recognition parameter, rather than an observed draw of latent matter. The lift and its reconstruction covariance do not define the conditional law of hidden recognition means given retained observations. A causal recognition filter cannot be replaced by a latent-matter Gaussian reversal on that basis.

## Original future kernel and terminal comparisons

The consumer under the [forecast contract](https://github.com/cdenn016/MultiAgentELBO/blob/d5190d5006f21b2e99bb13ef1a42c4a29b60f59e/docs/research/2026-10-03-latent-link-rg-plan/R3-RETAINED-PARENT-FORECAST-CONTRACT.md) ran once from clean published `4dfbae9ce96a3fc4f3124526c218dea0a2f34f46`; the [published result](https://github.com/cdenn016/MultiAgentELBO/blob/d5190d5006f21b2e99bb13ef1a42c4a29b60f59e/docs/research/2026-10-03-latent-link-rg-plan/R3-RETAINED-PARENT-FORECAST-RESULTS.md) retains its scope. Each terminal future generator slice three supplies the product law $q_G^+=\bigotimes_e\mathcal N(m_{3,e},\Lambda_{3,e}^{-1})$. Its common original-record kernel uses fresh matter $\bigotimes_i\mathcal N(a_i,J_{0,i}^{-1})$, independent source labels from pi and original positive record noise. Fitted prefix beta, retained observed-slice M and training offsets are absent from that future kernel. No missing fine mean is reconstructed for forecasting.

The existing common-kernel contraction from [[multiagentelbo-2026-10-08-product-moment-fisher]] bounds the full correlated all-row forecast KL by the product-generator KL in exact arithmetic. Every one of the 1,024 distinct original primitives enters once. Separately, the finite two-row decoder retains all 256 original standardized future vectors with equal masses, all 16 source patterns for receivers zero/one and their shared-sender/reversal covariance. All three laws and four directed Gaussian comparisons are fixed before the unchanged episode-three query is scored; no future observation enters inference or parameter selection.

| Candidate | Direction | Computed whole-generator KL | Computed KL per original receiver | Finite two-row matched-component upper |
| --- | --- | ---: | ---: | ---: |
| 128 parents | Native to candidate | 1.908609358251294e-16 | 3.727752652834558e-19 | 7.399280198395505e-21 |
| 128 parents | Candidate to native | 1.908609358251294e-16 | 3.727752652834558e-19 | 7.399280197652087e-21 |
| 32 parents | Native to candidate | 2.077069306326806e-16 | 4.056775988919544e-19 | 8.416774123220390e-21 |
| 32 parents | Candidate to native | 2.077069306326806e-16 | 4.056775988919544e-19 | 8.416774122339992e-21 |

The unchanged .001-nat-per-receiver computational target passes in both directions. The last column averages component Gaussian KL under the same component/label masses and bounds these finite two-row mixtures in exact arithmetic; it is a different law from the continuous all-row recognition forecast. The independent covariance-factor/eigenspectrum calculation reconstructs all 4,096 directed primitive Gaussians, 16,384 matched component Gaussians, generator factors, full future vectors, catalogs, joints and scores. Zero negative KL/covariance-term counts are recorded, with no clipping.

These tiny floating values are computed diagnostics, not interval-certified bounds at their displayed magnitude. The exact Gaussian statement uses a real symmetric precision interpretation; archived precision asymmetry, inverse/Cholesky, symmetrization and matrix/contraction rounding remain excluded. Extremely small scalar-series tails do not bound those matrix errors. The KL replay allowance is $10^{-12}$, larger than the reported whole-generator totals. The short inference window and common future kernel also prevent interpreting agreement as useful longer-horizon closure, native-posterior accuracy or convergence.

Native joint log density is -6.916718561539034. Candidate-minus-native changes are $5.257483337572921\times10^{-11}$ and $4.996270064339115\times10^{-11}$, with both original marginal row scores independently reconstructed. One heldout vector with differences this small establishes no predictive improvement.

## Receipts, resources and scope

The [trajectory result](https://github.com/cdenn016/MultiAgentELBO/blob/4dfbae9ce96a3fc4f3124526c218dea0a2f34f46/docs/research/2026-10-03-latent-link-rg-plan/R3-RETAINED-PARENT-TRAJECTORY-RESULTS.md) records producer/reader times of 877.1818988999585/371.2907084999606 seconds and process peaks of 1,227,857,920/175,140,864 bytes. Its [replay manifest](https://github.com/cdenn016/MultiAgentELBO/blob/4dfbae9ce96a3fc4f3124526c218dea0a2f34f46/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-retained-parent-package.json) preserves 95 files totaling 34,099,937 bytes with canonical length/SHA256 parity. Trajectory focused JUnits record four/two passes in 2.525/1.349 seconds, zero failures/errors/skips. [Producer](https://github.com/cdenn016/MultiAgentELBO/blob/4dfbae9ce96a3fc4f3124526c218dea0a2f34f46/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-retained-parent-trajectory.json)/[reader](https://github.com/cdenn016/MultiAgentELBO/blob/4dfbae9ce96a3fc4f3124526c218dea0a2f34f46/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-retained-parent-trajectory-readback.json) receipt SHA256 values are `d34ada53445e4daca7ecb33303bd0889768fcc38c03b77b060535cfd03c6f219` and `b7f531cf09a19e527b8b673c867ffc32c158e7dbc4def4f8165a55970d71714e`.

Forecast [producer](https://github.com/cdenn016/MultiAgentELBO/blob/d5190d5006f21b2e99bb13ef1a42c4a29b60f59e/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-retained-parent-forecast.json)/[reader](https://github.com/cdenn016/MultiAgentELBO/blob/d5190d5006f21b2e99bb13ef1a42c4a29b60f59e/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-retained-parent-forecast-readback.json) times are 1.2956715000327677/.5478213999886066 seconds, with process peaks 592,842,752/109,273,088 bytes. Its 25 derived NPZs contain 39,200,472 logical and 34,833,053 compressed bytes; input/source snapshots contain 17,126,870/202,399 bytes. The complete canonical [replay package](https://github.com/cdenn016/MultiAgentELBO/blob/d5190d5006f21b2e99bb13ef1a42c4a29b60f59e/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-retained-parent-forecast-package.json) has 53 files totaling 52,180,386 bytes. Root matched all input/source/reader bindings and canonical length/SHA256 parity. Producer/reader focused JUnits each record three passes, in 1.866/.344 seconds, zero failures/errors/skips. Producer/reader receipt SHA256 values are `5959d60bea641e6f2b8266fa9671b3adfcc9088e5388440be57106354fb09f21` and `80fb9d772a6e3d8f1169e8d9ddda81f09cc5400b3805da25f8c085ad8d5721c5`.

All calculations used isolated Anaconda CPU float64, sequential MKL and one math thread. No GPU allocation, new field, trajectory or scientific retry accompanied the saved-only forecast consumer. Persistent candidate tensors remain 772,096/770,560 bytes, with all original generators, fine covariances/source rows and tree geometry. This is O(N) state; excluding one fine mean has not supplied compact messages or a scaling result. Complete replay, dense inference workspaces, component banks, snapshots and logging remain charged separately.

## Relevance to this research

[[Natural gradient]], [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] gain an executed own-state mean closure and its original-kernel terminal consumer. The next same-law obligation is the conditional filter/transition for hidden recognition parameters needed by causal forcing/downward feedback. Existing finite latent-matter reversals do not discharge it. Continuous candidate residual expectations/stability/exits, native posterior transfer, intrinsic persistent second formation, growing size/depth and all four RG gates remain open. The goal remains active; the user retains the GPU and the 144-case CUDA calibration remains unrun. This intake edits no manuscript, model or older immutable source and launches no scientific calculation.

PR212's separate [source-face domain proof](https://github.com/cdenn016/MultiAgentELBO/blob/d5190d5006f21b2e99bb13ef1a42c4a29b60f59e/docs/research/2026-10-03-latent-link-rg-plan/R5-SOURCE-FACE-DOMAIN.md) refutes the recorded compact-interior source algebra's dense-generator-range route for the same native form. An enlarged source test domain and full-past stationary-law identification remain open; the existing conservative realization is not refuted.
