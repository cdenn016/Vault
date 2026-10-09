---
type: run
title: "Complete reconstructed-state field and moving-parent residuals"
aliases: ["N512 complete centered-lift coefficient replay"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# Complete reconstructed-state field and moving-parent residuals

[Code PR210](https://github.com/cdenn016/MultiAgentELBO/pull/210), merged at `60e56d0afcb552a856a3ea6bafadf2477eb50bda`, completes the field substitution following [[multiagentelbo-2026-10-08-moving-parent-coefficients]]. The frozen CPU producer and independent reader each ran once from `0feab90da45af819e4ae6d90999b818ee1abb06c`. Independent replay passes 594 comparisons over 6,119,490 entries, maximum absolute discrepancy $3.410605131648481\times10^{-13}$ against unchanged allowance $10^{-8}$. This supplies complete instantaneous residuals, without a parent path-error bound or formal adjudication state.

```bibtex
@misc{codex2026liftedparentfield,
  author = {Codex},
  title = {Complete Reconstructed-State Field and Moving-Parent Coefficient Residuals},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/210},
  note = {Merge 60e56d0a; once-run producer and reader 0feab90d; retained-only reconstruction added afterward and unrun scientifically}
}
```

## Frozen substitution and independent derivatives

The [contract](https://github.com/cdenn016/MultiAgentELBO/blob/60e56d0afcb552a856a3ea6bafadf2477eb50bda/docs/research/2026-10-03-latent-link-rg-plan/R3-LIFTED-PARENT-FIELD-CONTRACT.md) retains the existing N512/E1024 real GL(2), mass-16, $T=1/20$, order-9 rule, original probe/trees and observed slice 2. Initial/checkpoints 1, 2 and 3 each have two separate 128/32-parent centered-lift substitutions. Only that slice's matter mean changes; all other means, covariances, generator coordinates and source rows stay fixed. The supplied mean is held independent during generator differentiation. These are not one jointly evolved hierarchy. No observation, latent/Brownian sample or state advance was generated.

Exactly eight selected-slice signed moment evaluations and eight geometry vector-Jacobian products retain both link signs, all receiver/sender records, matter prior, original rule weights and scale. Generator prior, loop and history-kinetic derivative differences cancel. The unchanged native metrics make thermal differences zero. All complete history-shaped direction and fine drift differences are saved; covariance-target changes and unselected/unsupported entries are zero. Generator covariance and precision are alternative charts, with actual inverse response retained in computed arrays.

The [result](https://github.com/cdenn016/MultiAgentELBO/blob/60e56d0afcb552a856a3ea6bafadf2477eb50bda/docs/research/2026-10-03-latent-link-rg-plan/R3-LIFTED-PARENT-FIELD-RESULTS.md) uses 3,456 first-only precision-Cholesky/exponential responses and saved old transport flow/curvature to include the complete parent mean/covariance drift change. Original common driver labels give the mean-noise change; covariance-noise difference is zero. Every retained generator/source row carries its full drift change. Parent values agree within $2.498001805406602\times10^{-16}$.

The reader independently assembles both signed record coefficient banks. Four NumPy entire-function derivative passes check all 32,768 generator mean entries and 81,920 independent symmetric precision coordinates; full symmetric arrays contain 131,072 entries. Independent local first Jacobians and tree/inverse composition then reconstruct the parent residuals. This complete substitution-gradient check does not broaden the old trajectory's selected-tangent check of its full generator gradient. Real-arithmetic primitive truncation bounds exclude floating evaluation, input representation, Cholesky/contraction amplification and population quadrature accuracy.

## Frozen tangent increments

Let $a$ be the squared complete retained drift residual in parent mean/svec-covariance, original generator mean/svec-precision and source probability coordinates. Discarded fine means and duplicate generator covariance coordinates are excluded. Let $b$ be the squared normalized common-driver noise residual, with only parent mean rows. At $h=1/40000$, exact conditional frozen tangent-increment mean-square difference is $h^2a+2Thb$. Its common Gaussian innovation is integrated analytically and was not drawn.

| Old step | Parents | Complete retained a | Normalized noise b | Frozen increment mean-square difference |
|---|---:|---:|---:|---:|
| 0 | 128 | 762.77166571379291 | 2.8101554475865917 | 7.5021209100376002e-06 |
| 0 | 32 | 927.37030947494316 | 0.52760099948309258 | 1.898608942129571e-06 |
| 1 | 128 | 762.95716519158475 | 2.8090936820483767 | 7.499582433365683e-06 |
| 1 | 32 | 927.61343407868605 | 0.52786647680409882 | 1.899424588309426e-06 |
| 2 | 128 | 762.79866324321642 | 2.8095125298927361 | 7.5005304892588511e-06 |
| 2 | 32 | 927.69061939879361 | 0.52828178417305227 | 1.9005110975568769e-06 |
| 3 | 128 | 762.7013861579278 | 2.8076435074937462 | 7.4957971350830717e-06 |
| 3 | 32 | 927.65195142507071 | 0.52779430412172257 | 1.8992682299449758e-06 |

These coordinate norms differ in dimension/geometry and do not rank predictive performance or matched compression. They measure neither positive-retraction error, accumulated path error, forecast KL nor stopped time-integrated expectation. Nearly unchanged values on this short correlated path establish no stationarity or convergence.

## Receipts, costs and later preparation

The [producer receipt](https://github.com/cdenn016/MultiAgentELBO/blob/60e56d0afcb552a856a3ea6bafadf2477eb50bda/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-lifted-parent.json) records 174.123331899988 seconds, 1,152,532,480-byte peak and 28,130,938,880 available RAM bytes above its 6GiB guard. The [reader](https://github.com/cdenn016/MultiAgentELBO/blob/60e56d0afcb552a856a3ea6bafadf2477eb50bda/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-lifted-parent-readback.json) takes 66.6075639999472 seconds and peaks at 740,855,808 bytes. Both use isolated Anaconda CPU float64, sequential MKL and one math thread; no GPU allocation. Producer/reader focused JUnits report three passes in .254 seconds and six in 1.281 seconds, zero failures/errors/skips. No broader suite, producer retry or historical replay occurred; prior moving-reader failure/success receipts remain intact.

Derived arrays occupy 32,184,640 logical and 8,693,156 compressed NPZ bytes; inputs/sources occupy 17,387,125/230,011 snapshot bytes. Named oracle arrays include 655,360-byte coefficient banks, 65,536-byte mean covectors, 262,144-byte precision covectors and 215,040-byte local Jacobian. A 32-primitive sample chunk is 6,718,464 logical bytes; two-lift node covectors are 13,436,928 bytes. Broadcast views/backing and process temporaries remain separately charged.

Root matched 43 inputs, 20 source/current snapshots, 88 reader bindings and the executing checker. The [manifest](https://github.com/cdenn016/MultiAgentELBO/blob/60e56d0afcb552a856a3ea6bafadf2477eb50bda/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-lifted-parent-package.json) retains 93 files totaling 26,528,220 bytes, copied to canonical Desktop code artifacts with exact length/SHA256 parity. Live receipt hashes read for this intake are producer `18148870c62c7745690925ea6d725f900d6ce314addc98bd3c5cdaf81dc6fdd1` and reader `119d09f513139526cfeb9b974c1c34af53e2b076929912207acd3f88172c9665`.

PR210 also adds a retained-only reconstruction adapter after the frozen producer revision. It accepts retained parent mean and current covariance/center/map, independently of discarded means. Four tiny cases pass in 1.429 seconds. It was not used in the frozen producer, and no own-state candidate trajectory has run. Such a candidate must reevaluate its complete field at its own reconstructed states, use the original common Brownian tuple, coarsen its proposal and discard the ephemeral fine mean, rather than reset along the truth path.

## Relevance to this research

[[Natural gradient]], [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] gain the complete finite-rule reconstructed-state drift/noise residual, including generator/source feedback omitted by frozen matter-force substitution. Continuous coupling still needs stopped residual expectations, lifted-segment containment, local stability, exits and numerical/population accuracy; a stationary theorem cannot replace nonstationary initialization. Own-state candidate dynamics, conditional original-record forecasts, downward feedback, persistent formation, growing size/depth and all four RG gates remain open. No manuscript/model or new science execution accompanies this intake; the GPU remains occupied and the 144-case calibration unrun.
