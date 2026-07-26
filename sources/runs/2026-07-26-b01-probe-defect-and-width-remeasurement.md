---
type: run
title: "The E-step character probe measured the wrong channel: B-01 defect, re-measurement, and the width comparison re-established (2026-07-26)"
aliases:
  - "B-01 re-measurement"
  - "2026-07-26 E-step character re-measurement"
  - "pair-precision share correction"
  - "width comparison re-measured"
tags:
  - cluster/vfe
  - cluster/attention
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-07-26
updated: 2026-07-26
---

# The E-step character probe measured the wrong channel: B-01 defect, re-measurement, and the width comparison re-established (2026-07-26)

> [!info] Provenance and evidence boundary
> Repository `V3_Transformer`, corrected probe merged at `0b9013d`. Interpreter
> `C:/anaconda/python.exe` (CUDA build, RTX 5090). Two checkpoints:
> `55.41_wikitext-103_K300_block_glk_linear_mix_s6` ($K=300$, 10 heads, 1 layer, 128 context) —
> the SAME checkpoint the 2026-07-25 measurement used, re-measured here — and
> `vfe3_runs/138.40_wikitext-103_K20_block_glk_linear_mix_s6` ($K=20$, 2 heads, test PPL 138.40,
> validation PPL 139.30), trained 2026-07-26 to replace a deleted checkpoint. Probe replica error
> `recompute_max_abs_err = 0.0` on every measurement, so the probe's reconstruction of the kernel
> fusion is exact. Raw record: `docs/2026-07-26-b01-remeasurement.json` in the repository.

## The defect

`collect_estep_character` decomposes the `mm_exact` precision fusion
$\mu^{*}=\big(a\mu_p/s_p+\sum_j w_{ij}\mu_t/s_t\big)/P$ into a PAIR (attention) share and a PRIOR
(residual) share. It installed a spy on `mm_exact_update` and read `recorded[0]` — the first fusion
call of the forward pass.

Under `s_e_step=True` that first call is **not the belief's**. `_refine_s` threads
`cfg.e_step_update` into its own E-step and runs BEFORE the belief stack, so the model channel's
fusion was recorded first and read as the belief's. Its anchor is also wrong: the model channel's
prior is the token-uniform centroid $r$, not the belief's prior. Direct call-order instrumentation at
`n_layers=2, s_e_step=True` gives the sequence
`['S_CHANNEL','S_CHANNEL','S_CHANNEL','belief','belief','belief','belief']`.

Every fusion call is now tagged with the channel and layer that produced it, and the probe reads the
belief channel of layer 0 only. The record publishes `measured_channel` and `measured_layer` so a
reader cannot be misled about what was measured.

## What the numbers become

All shares at 64 sequences (the protocol the in-run probe uses); see the sampling note below.

| quantity | published 2026-07-25 | re-measured 2026-07-26 |
|---|---|---|
| PAIR (attention) share, $K=300$ | 0.298 | **0.196** |
| PRIOR (residual) share, $K=300$ | 0.702 | **0.804** |
| displacement after 1 step, $K=300$ | 0.227 | **0.299** |
| displacement at depth 8, $K=300$ | 0.323 | **0.319** |
| step-1 share of displacement, $K=300$ | 70% | **94%** |
| $\cos(\text{dir}_8,\text{dir}_1)$, $K=300$ | +0.962 | **+0.965** |
| PAIR share, $K=20$ | 0.190 | **0.153** |
| PRIOR share, $K=20$ | 0.810 | **0.847** |

The correction moves the structural reading FURTHER in the direction the original argued, not
against it: step 1 takes 94% of the total displacement at $K=300$ rather than 70%, and the residual
dominates the fusion more heavily than published (0.80 rather than 0.70 at $K=300$, 0.85 at $K=20$).
The trajectory is a near-straight-line contraction at both widths ($\cos$ +0.965 and +0.984).

## The $K=20$ checkpoint was deleted, and what replaced it

The 2026-07-25 $K=20$ column came from `vfe3_runs/ablations_single_seed/138.40_mstep-phi-norm=5`
(recorded in [[2026-07-25-estep-character-and-channel-decomposition]]). That directory has since been
cleared, and no run before 2026-07-26 persisted an `estep_character.json`, so `0.190` cannot be
re-measured or tied to any artifact on disk. It is **withdrawn, not corrected**.

The replacement run reaches validation PPL **139.30** against the deleted cell's **139.3** and carries
the same `phi_mstep_max_matrix_norm=5` that named that ablation cell, so it reproduces the original
configuration rather than merely resembling it.

> [!note] Editorial: the equivalence of the replacement run to the deleted cell rests on the PPL
> match and the shared `mstep-phi-norm` setting; the deleted cell's `config.json` cannot be diffed
> directly. Treat `0.190 → 0.153` as a like-for-like pair under that caveat, not as a certainty.

## Sampling sensitivity — quote the sample size

The share is computed on a single batch, and the draw matters at the larger width:

| probe sample | $K=20$ pair share | $K=300$ pair share | gap |
|---|---|---|---|
| 8 sequences | 0.1476 | 0.2130 | +0.065 |
| 64 sequences | 0.1533 | 0.1964 | +0.043 |

$K=20$ is stable across draws (0.148 / 0.153); $K=300$ is not (0.213 / 0.196). No pair-precision
share should be quoted without its sample size.

## The width comparison: direction survives, isolation does not

The direction the 2026-07-25 finding asserted — the neighbor share rises with width — **survives
re-measurement at both sample sizes**, at roughly half the published magnitude (0.153 → 0.196 at 64
sequences, 0.148 → 0.213 at 8).

It is not a controlled width experiment. The two runs differ in twelve config fields. `kl_max`
(160 vs 2400) is dismissed — `guard_energy_klmax_frac` is 0.0 in both, so the clamp never fires and
the pair mask is untouched by it. What remains uncontrolled: training length (15k vs 180k steps,
12×), head count (2 vs 10, hence $d_\text{head}$ 10 vs 30, which sets
$\tau=\kappa\sqrt{d_\text{head}}$ and therefore the softmax sharpness the share depends on
directly), batch size (64 vs 16), `pos_phi_compose` (`group_product` vs `bch`),
`phi_mstep_max_matrix_norm`, and the code revision.

Head count is structurally confounded: `n_heads` must divide `embed_dim`, so 10 heads is unavailable
at $K=20$ and $d_\text{head}$ cannot be held fixed while width varies in this family. Separating them
requires a sweep at fixed $d_\text{head}$ (varying `n_heads` with $K$) or at fixed `n_heads`.

## Relevance to this research

The pair/prior split is the quantitative core of the claim that the V3 belief E-step is **one
attention aggregation with a dominant residual** rather than iterative inference
([[2026-07-25-estep-character-and-channel-decomposition]]). The defect did not overturn that reading —
it strengthened it — but it did invalidate every published share, and it retired the width claim from
"measured" to "supported by two points, confounded with training depth and head geometry."

It also carries a methodological lesson for the program: the 2026-07-25 shares were produced by an
ad-hoc probe session that persisted no artifact, which is why the $K=20$ number became untraceable
once its checkpoint was deleted. Runs now write `estep_character.json` into the run directory, so a
published number has a file behind it. See [[Precision weighting]] and
[[VFE Transformer Program]].

## Scope limits

- Everything here is at `s_e_step=True`, `prior_source='model_channel'`, `e_step_update='mm_exact'`,
  `n_layers=1`. The `prior_source='token'` arm is a separate measurement
  ([[2026-07-25-token-prior-estep-character-and-diagnostics]]) and its `0.109` share was independently
  assessed as unaffected by B-01 (single channel, so no cross-channel misattribution is possible).
- The precision split exists only on the `mm_exact` route; on `e_step_update='gradient'` the fusion
  is never computed and the shares are correctly reported as absent.
- Displacement and $\cos$ are now measured route-independently (from the block boundary) rather than
  only inside the `mm_exact` spy; the `mm_exact` window remains primary where it exists.
