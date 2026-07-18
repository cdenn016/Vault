---
type: run
title: "K=10 phi pullback-group partial negative result (2026-07-18)"
aliases:
  - "phi pullback-group K10 negative result"
  - "2026-07-18 pullback-group run"
tags:
  - cluster/vfe
  - cluster/gauge-theory
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/mathematics
created: 2026-07-18
updated: 2026-07-18
---

# K=10 phi pullback-group partial negative result (2026-07-18)

> [!info] Provenance and evidence boundary
> This is a point-in-time record of the still-running CUDA experiment
> `V3_Transformer/vfe3_runs/20260718-123141_wikitext-103_K10_block_glk_linear_mix_s6`.
> The snapshot was captured on 2026-07-18 at 12:58 CDT after training step 9,500; the latest
> completed validation was step 9,000. The run artifact does not embed a source commit. The live
> V3 checkout was at `06372e0` at capture time and contained intentional uncommitted experiment
> settings and scaling-artifact changes, which were neither modified nor assigned to this run.
> The run's stored `config.json` is authoritative for the configuration below. No matching K=10
> AdamW `metrics.csv` was present in the workspace, so the exact AdamW gap is user-reported rather
> than independently reconstructable from the retained artifacts.

## Configuration

The run uses WikiText-103 on CUDA with seed 6 and deterministic algorithms, 5,079,182 parameters,
one layer, $K=10$, two $\mathrm{GL}(5)$ blocks, sequence length 64, batch size 128, and a planned
15,000 optimizer steps. The frame parameterization is `phi` with
`m_phi_update_mode="pullback_group"`, `phi_precond_mode="pullback_per_block"`,
`m_phi_lr=0.01`, `e_phi_lr=0`, group trust radius 0.1, and `mass_phi=0`. The serialized
`phi_weight_decay=0.03` is inert on this route because the pullback-group optimizer policy forces
frame weight decay to zero.

The selected optimizer consumes the existing outer supervised covector, solves the regularized
Frobenius pullback system in exponential coordinates, converts the chart direction to a
left-trivialized group velocity, and applies a right-multiplication update through order-four BCH.
It is stateless: it carries no first or second moments and updates only frame rows with a nonzero
current covector. It is therefore a geometric group-descent control, not AdamW and not a
Fisher natural gradient over a specified statistical family.

## Measured partial curve

| step | validation CE | validation PPL |
|---:|---:|---:|
| 1,500 | 6.12319 | 456.32 |
| 3,000 | 6.02302 | 412.82 |
| 4,500 | 5.97216 | 392.35 |
| 6,000 | 5.94707 | 382.63 |
| 7,500 | 5.92179 | 373.08 |
| 9,000 | 5.90146 | 365.57 |

At step 9,500 the training CE was 5.90339 (PPL 366.28) and the scheduled frame learning rate had
fallen to 0.00300. The curve is still improving, but its optimization rate is poor relative to the
user's AdamW comparison.

## Geometry diagnostics

The negative result is not accompanied by an obvious failure of the group update. At step 9,500:

- the pullback direction/raw-covector cosine was 0.99081;
- the median and maximum damped generalized condition numbers were 1.90065 and 2.85504;
- the mean and minimum accepted trust/backtracking scale were both 1.0; and
- the largest candidate chart norm was 0.58175, far below the active noncompact chart bound.

The pullback direction is therefore almost parallel to the raw outer-objective gradient, the local
system is well conditioned, and neither trust-radius clipping nor BCH backtracking is suppressing
the step. The data do not support an exploding or singular group-geometry explanation.

## Interpretation

The leading explanation is an optimizer-scale mismatch. AdamW supplies first-moment averaging,
coordinatewise second-moment normalization, continued momentum on previously active vocabulary
rows, and decoupled frame decay. The pullback-group route supplies none of these and takes a raw
metric-conditioned stochastic step only on currently active rows. Because the measured pullback
direction is nearly collinear with the raw covector, this operating point gives up AdamW's adaptive
dynamics while receiving little directional change from the frame metric.

This mechanism is an inference from the executed code path plus the recorded diagnostics, not a
completed causal ablation. Equal numerical learning rates are not equivalent across AdamW and raw
group descent. The registered follow-up sweep already recognizes this and proposes
`m_phi_lr` in `{0.0005, 0.0015, 0.005, 0.015, 0.05, 0.15}`. The current run uses 0.01 and does not
resolve that sweep. The earlier [[2026-06-27-gauge-transport-ablation-suite]] also found AdamW 144
versus pullback 252, but correctly classified that result as inconclusive because its learning-rate
rescue sweep was incomplete.

## Research status and required control

AdamW remains the production default. This partial run supports retaining `pullback_group` only as
an opt-in geometric research control until a matched experiment shows competitive optimization.
It does not show that the pullback implementation is mathematically wrong, and it does not promote
the pullback metric to a statistical [[Natural gradient]].

A decisive comparison requires the same K=10 configuration and evaluation budget for AdamW and
pullback-group, a short screen over the registered pullback learning-rate grid, and multiple seeds
for the surviving settings. The comparison must report validation curves, accepted update scales,
frame displacement or update norms, and wall-clock cost. If the tuned pullback route remains worse,
the result should be reported as a negative optimizer result rather than as a failure of group
geometry.

## Relevance to this research

This is the first retained run of the rebuilt stateless phi group-descent implementation. It sharpens
the boundary between Gaussian belief-side Fisher geometry and frame optimization in the
[[VFE Transformer Program]]: a well-behaved exponential-coordinate pullback metric can still be a
poor optimizer for outer cross-entropy when its stochastic dynamics do not match AdamW. The result
also preserves the open canonical-objective distinction: the run consumes the existing outer
supervised covector, not a separately selected fixed-returned-state VFE frame M-step.

## Cross-links

- Project: [[VFE Transformer Program]]
- Prior run: [[2026-06-27-gauge-transport-ablation-suite]]
- Theory: [[Natural gradient]]; [[Information geometry and natural gradient]];
  [[Baker-Campbell-Hausdorff formula]]; [[GL(K) gauge group]]
- Roadmap: [[VFE Transformer Research Directions (2026-06-21)]]
