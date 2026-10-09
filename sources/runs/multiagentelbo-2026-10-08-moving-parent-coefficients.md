---
type: run
title: "Saved moving-parent drift, joint bracket and mean-noise defect"
aliases: ["N512 moving-parent coefficient replay"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# Saved moving-parent drift, joint bracket and mean-noise defect

[Code PR209](https://github.com/cdenn016/MultiAgentELBO/pull/209), merged at `36f77e5ba5119ea33ce987bf0af3283b67452fd5`, publishes instantaneous moving-parent coefficients from the existing four old order-9 field states. It continues [[multiagentelbo-2026-10-08-discarded-mean-stationary-bound]] and [[multiagentelbo-2026-10-08-moving-parents-bond-factor]]. The producer ran once from clean published `c3b947b8d7ffe9372d185b9573dca22d075dfdcf`; a separately published reader repair at `a52684f02afd30d175328f35108608919a4e196a` completed the independent replay. No field, moment, sample, noise, observation, trajectory or GPU allocation was generated. This intake records the completed calculation and source derivation, without assigning a formal adjudication state.

```bibtex
@misc{codex2026movingparentcoefficients,
  author = {Codex},
  title = {Saved Moving-Parent Drift, Joint Bracket and Mean-Noise Defect},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/209},
  note = {Merge 36f77e5b; once-run producer c3b947b8; separately frozen reader a52684f0; instantaneous saved-state diagnostic}
}
```

## Frozen inputs and shared-driver calculation

The [contract](https://github.com/cdenn016/MultiAgentELBO/blob/36f77e5ba5119ea33ce987bf0af3283b67452fd5/docs/research/2026-10-03-latent-link-rg-plan/R3-MOVING-PARENT-CONTRACT.md) fixes N512/E1024, real GL(2), mass 16 and temperature $T=1/20$. Observed matter slice 2 at the initial state and checkpoints 1, 2 and 3 is paired with its corresponding saved order-9 field. Checkpoint 4 has no matching field and is excluded. The original fixed Gaussian probe, 384-edge first forest, 96-edge upper forest and 480-edge direct union remain unchanged. Both 128-parent and 32-parent maps use all 512 matter nodes. This fixed-probe temporal coupling is the already-declared moving-readout convention, rather than a new episode-history law.

The [analytic jets](https://github.com/cdenn016/MultiAgentELBO/blob/36f77e5ba5119ea33ce987bf0af3283b67452fd5/docs/research/2026-10-03-latent-link-rg-plan/R3-MOVING-PARENT-JETS.md) differentiate the precision-Cholesky probe, ordered matrix exponentials and shared-driver products/inverses. Native covariance-driver orientation is retained when converting generator covariance to precision coordinates. Primitive labels are shared through upper-tree dressing and repeated products before contraction. Drift includes the complete old history field and covariance/precision thermal corrections. These are finite-rule coefficients at the saved states, rather than population-accuracy certificates.

For $Y=(M,\operatorname{svec}V)$, each parent contributes two mean and three symmetric covariance coordinates. The two depths together give 800 rows and 9,280 active fine-driver columns in a common normalized factor $Z$, with physical bracket $d[Y]_t=2TZZ^Tdt$. The saved full matrix includes cross-depth mean/covariance blocks. Separate indexed factors retain all 1,024 slice-2 generators and 512 matter covariances, reconstructing parent-generator and parent-matter covariance cross entries. Direct source/other-episode cross blocks are zero; their objective effects remain in the slice-2 drift. Per-node transport values, first-flow and curvature contractions are saved for the next lifted-field comparison. The 9,280 active parent columns are not the total storage for every original-copy coefficient.

## Independent replay and nonzero noise substitution

The [result](https://github.com/cdenn016/MultiAgentELBO/blob/36f77e5ba5119ea33ce987bf0af3283b67452fd5/docs/research/2026-10-03-latent-link-rg-plan/R3-MOVING-PARENT-RESULTS.md) and [completed reader receipt](https://github.com/cdenn016/MultiAgentELBO/blob/36f77e5ba5119ea33ce987bf0af3283b67452fd5/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-moving-parent-readback-r1.json) report 253 passing comparisons over 10,475,718 entries, maximum absolute discrepancy $3.197442310920451\times10^{-14}$ against unchanged allowance $10^{-8}$. The reader uses independent local 14-coordinate Torch Jacobians/Hessians and its own forest/inverse/readout composition. Values match the original parent archives; staged/direct values, flow, curvature and aligned common-index noise agree. These binary64 comparisons establish the recorded arithmetic replay, without certifying interval arithmetic or native population error.

For the existing centered lift, $r_i=\mu_i-\widehat\mu_i$ gives normalized mean-noise substitution defect $\Delta Z_{M,\alpha}=\sum_i w_iDT_i[\xi_\alpha]r_i$, retaining each original geometry driver $\xi_\alpha$. The physical squared norm is $2T\|\Delta Z_M\|_F^2$. Saved values are:

| Old field state | Parents | Normalized squared norm | Physical squared norm |
|---|---:|---:|---:|
| Initial | 128 | 2.8101554475865917 | 0.2810155447586592 |
| Initial | 32 | 0.52760099948309258 | 0.052760099948309262 |
| Checkpoint 1 | 128 | 2.8090936820483767 | 0.28090936820483769 |
| Checkpoint 1 | 32 | 0.52786647680409882 | 0.052786647680409887 |
| Checkpoint 2 | 128 | 2.8095125298927361 | 0.28095125298927365 |
| Checkpoint 2 | 32 | 0.52828178417305227 | 0.052828178417305229 |
| Checkpoint 3 | 128 | 2.8076435074937462 | 0.28076435074937461 |
| Checkpoint 3 | 32 | 0.52779430412172257 | 0.052779430412172257 |

The defect is nonzero and varies little over this short path. Different depths have different dimensions/geometry, so these norms are not a matched depth-error comparison. Covariance and other retained noise rows do not change under mean substitution at fixed geometry. Generator/source forces do change: complete lifted field and drift residual remain pending. These values are neither a time-integrated expectation nor evidence of activation failure, late convergence, forecast error or parent autonomy.

## Preserved first-reader failure and separate repair

The [first reader receipt](https://github.com/cdenn016/MultiAgentELBO/blob/36f77e5ba5119ea33ce987bf0af3283b67452fd5/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-moving-parent-readback.json) retains a TypeError from subtracting Boolean digest-identity values before any comparison was recorded. No coefficient disagreement was reached. Original reader bytes remain in the producer source snapshot. Four tiny comparison fixtures then passed, and the separately frozen repair uses exact Boolean inequality while preserving numeric operations, shapes, labels and allowances. The repaired reader wrote a unique r1 receipt. The producer was not retried; the first failure is retained.

## Resources and provenance

The [producer receipt](https://github.com/cdenn016/MultiAgentELBO/blob/36f77e5ba5119ea33ce987bf0af3283b67452fd5/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-moving-parent.json) records 7.33618740004022 seconds and a 216,035,328-byte process peak; available RAM before the 2GiB guard was 30,852,386,816 bytes. The completed reader takes 8.53633269993588 seconds and peaks at 1,530,679,296 bytes. Both use isolated Anaconda CPU float64, sequential MKL and one math thread. Three tiny jet fixtures pass in 2.399 seconds; no broader suite ran for this diagnostic.

Derived arrays occupy 33,334,512 logical bytes and 7,548,284 compressed NPZ bytes. Exact inputs occupy 9,811,556 snapshot bytes and original sources 117,331 bytes. Named per-state workspaces include a 59,392,000-byte joined factor, 5,120,000-byte joint bracket, 1,605,632-byte native generator factors, 36,864-byte matter covariance factors, 215,040-byte local Jacobian and 3,010,560-byte local Hessian. Autograd, BLAS and compression temporaries are covered by measured peak, not these logical totals.

Root matched 34 input and eight source snapshot bindings, all 43 revised reader input bindings, and executing reader/revised contract/first-receipt digests. The [replay manifest](https://github.com/cdenn016/MultiAgentELBO/blob/36f77e5ba5119ea33ce987bf0af3283b67452fd5/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-moving-parent-package.json) retains 62 files totaling 17,597,880 bytes. The complete package was copied to the actual Desktop code artifact directory with every length and SHA256 matched. Live receipt hashes read for this intake are producer `0ddf97a2c9f182aba8e2b70c7b448d2ae6fac2b360a804ac5443a68243e199eb` and completed reader `8bce52a53abc969d49c171646b68c912c979703eda401a26672722474c170bd2`.

## Relevance to this research

[[Natural gradient]], [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] gain a saved instantaneous moving-map drift/bracket diagnostic with original shared drivers and a nonzero centered-lift mean-noise residual. This extends frozen matter-force reconstruction rather than closing a parent process. Next compute the complete field change at the supplied centered lift, holding its mean fixed during generator differentiation, then combine it with these transport contractions/noise factors. A path bound still needs stopped residual expectations, compatible local stability/exits and numerical/population accuracy; four truth-path snapshots cannot supply those integrals. Original-record feedback, posterior accuracy, endogenous formation, growing size/depth, stationarity of the saved states and all four RG gates remain open. The 144-case CUDA calibration remains unrun while the user owns the GPU. This intake changes no manuscript/model and runs no new science.
