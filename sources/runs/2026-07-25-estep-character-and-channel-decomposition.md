---
type: run
title: "The belief E-step is one attention aggregation: channel decomposition and depth attribution (2026-07-25)"
aliases:
  - "E-step character measurement"
  - "2026-07-25 E-step character"
  - "belief vs model channel decomposition"
  - "two-attention-layer finding"
tags:
  - cluster/vfe
  - cluster/attention
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-07-25
updated: 2026-07-25
---

# The belief E-step is one attention aggregation: channel decomposition and depth attribution (2026-07-25)

> [!info] Provenance and evidence boundary
> Checkpoint-only measurements on two trained V3 checkpoints; no model was trained and no
> checkpoint on disk was written to. Repository `V3_Transformer` at `4686082` with a clean
> worktree. Interpreter `C:/anaconda/python.exe` (CUDA build, RTX 5090). Checkpoints:
> `55.41_wikitext-103_K300_block_glk_linear_mix_s6` ($K=300$, 10 heads, 1 layer, 128 context,
> rescored under current HEAD at CE 4.0123 / PPL 55.275) and
> `vfe3_runs/ablations_single_seed/138.40_mstep-phi-norm=5` ($K=20$, 2 heads, validation PPL
> 139.3). Every number below was measured at `prior_source='model_channel'` with `s_e_step=True`,
> `e_step_update='mm_exact'`, and `lambda_gamma=0.75`; the scope limits in the final section are
> not rhetorical. The probe scripts lived in the session scratchpad and were deleted after the
> result JSONs were retained; the write-up of record is
> `V3_Transformer/docs/2026-07-25-state-of-knowledge.md` (sections 3 and 6).

## What was asked

Two questions in sequence. The first arose from a shipped diagnostic, `estep_depth_sensitivity`,
whose curve showed cross-entropy rising steeply with inference depth while free energy fell — read
at the time as evidence that belief inference is anti-aligned with prediction, and the motivation
for the cross-scale shadow-prior proposal refuted in
[[2026-07-25-shadow-prior-refutation]]. The second, once that reading collapsed, was whether the
E-step performs inference at all or has degenerated into a single learned transform. Neither
framing survived measurement intact.

## The depth pathology was a shared configuration field

`cfg.n_e_steps` is read by the belief E-step in `model/block.py` and, independently, by the
model-channel refinement `model/model.py::_refine_s`. Under `prior_source='model_channel'` with
`s_e_step=True` the refined model state $s$ **is** the belief's prior $p_i$, so sweeping the single
field moved the prior and the belief together while the artifact reported one number named
"inference depth". The two `e_step` bindings are independent — `block.py` binds at import while
`_refine_s` imports inside the function — so each loop can be pinned at depth 1 while the other
varies. Change in cross-entropy against each arm's own depth-1 baseline, four fixed test batches:

| depth | $K{=}20$ both | $K{=}20$ belief only | $K{=}20$ $s$ only | $K{=}300$ both | $K{=}300$ belief only | $K{=}300$ $s$ only |
|---|---|---|---|---|---|---|
| 2 | +0.327 | **+0.005** | +0.302 | +0.285 | **+0.004** | +0.236 |
| 3 | +1.147 | **+0.009** | +1.115 | +0.987 | **+0.009** | +0.902 |
| 5 | +2.826 | **+0.012** | +2.808 | +2.657 | **+0.012** | +2.605 |
| 8 | +3.479 | **+0.012** | +3.477 | +3.594 | **+0.013** | +3.584 |

The belief loop supplies 0.3% of the effect; the model channel supplies 99.7%, replicated across
two checkpoints and a fifteenfold difference in width. The mechanism is the model channel behaving
as designed rather than a defect: `r_mu` is a single $(K,)$ vector broadcast to every position
(`r_mu_t.expand_as(s_mu)`), so iterating the $s$ loop pulls every $s_i$ toward one global centroid
and $p_i$ progressively loses token identity. That is consensus in the channel built to be a slow
consensus channel. The defect was diagnostic: a probe named for the belief loop was cranking a
second loop it is not named after. It has since been repaired by a new `s_e_step_n_iter`
configuration field that drives the model-channel loop independently (`None` follows `n_e_steps`
byte-identically), with the artifact emitting two labeled series and recording both depths per
point.

## Four mechanism hypotheses, all refuted

The same sweep tested the four candidate mechanisms proposed for the depth pathology before the
decoupling was found ($K=20$, belief depth varying alone):

| | depth 0 | depth 1 | depth 3 | depth 8 |
|---|---|---|---|---|
| body-frame dispersion of $U_i^{-1}\mu_i$ | 0.9062 | 0.8798 | 0.8672 | 0.8655 |
| `selfdiv_klmax_frac` | 0.000 | 0.000 | 0.000 | **0.000** |
| $\alpha^{*}=c_0/(b_0+D)$, median | 1.00000 | 0.99988 | 0.99977 | **0.99976** |
| effective rank of $\mu$ (of $K=20$) | 14.71 | 14.47 | 14.38 | 14.37 |
| free energy per token | 32.361 | 32.327 | 32.321 | 32.321 |

There is no consensus collapse in the belief channel (dispersion moves 4.5% over eight iterations),
the $\mathbb 1[D<k_\text{max}]$ anchor gate never fires, the self-anchor coefficient does not decay
because the median self-divergence reaches only 0.012 nats against $k_\text{max}=160$, and there is
no rank collapse of the kind [[dong-2021-rank-collapse]] describes for pure attention stacks.
Repeating the whole sweep at $k_\text{max}=10^6$ reproduced every number byte for byte, so
[[Divergence clamp saturation]] is not involved on this path.

## The first step, decomposed

Turning both loops off and adding one step of each isolates what each channel contributes:

| configuration | $K{=}20$ CE | gain | $K{=}300$ CE | gain |
|---|---|---|---|---|
| belief 0, $s$ 0 | 6.6064 | — | 6.1380 | — |
| belief 1, $s$ 0 | 5.2637 | **1.343** | 4.7062 | **1.432** |
| belief 0, $s$ 1 | 4.7525 | 1.854 | 4.2225 | 1.916 |
| belief 1, $s$ 1 | 4.6592 | 1.947 | 4.1340 | 2.004 |

One belief E-step is worth roughly 1.3 to 1.4 nats standing alone, so the belief loop does
substantial work and simply finishes in one step; the earlier claim that it is neutral holds only
from depth 2 onward. The two channels are also heavily redundant: individually they contribute
$1.343+1.854=3.20$ nats but jointly only 1.947. That redundancy explains why
`prior_source='token'` with `s_e_step=False` reaches comparable perplexity — the removed channel was
largely duplicating the belief loop, and a model trained without it covers the difference.

## What the E-step actually is

A framing correction comes first. `e_step_update='mm_exact'` computes the closed-form stationary
point of the $\beta$-frozen objective, so convergence in one step is by construction and not
evidence of degeneracy; reading "free energy flat after step 1" as suspicious was misplaced.
Measured on both checkpoints with the model channel pinned at its trained depth, eight sequences:

| | $K{=}20$ | $K{=}300$ |
|---|---|---|
| $\lVert\Delta\mu\rVert/\lVert\mu_p\rVert$ after one step | 0.147 | 0.227 |
| after eight steps (converged) | 0.200 | 0.323 |
| share of total displacement taken by step 1 | 73% | 70% |
| $\cos(\text{direction}_8,\text{direction}_1)$ | +0.982 | +0.962 |
| $\mathrm{KL}(q^{*}\Vert p)$ | 0.014 nats | 0.215 nats |
| pair (attention) share of the fused precision | 0.190 | **0.298** |
| prior (residual) share | 0.810 | **0.702** |

It is inference in a precise and unglamorous sense: the E-step computes the exact stationary point
of a well-defined objective, and the iteration is a well-conditioned, nearly straight-line
contraction in which one step covers about 70% of the total displacement and every later step moves
in essentially the same direction. The belief genuinely moves, by 20% of its norm at $K=20$ and 32%
at $K=300$, so this is not a no-op.

The fixed point, however, is a convex blend. The `mm_exact` fusion
$\mu^{*}=\big(a\mu_p/s_p+\sum_j w_{ij}\mu_t/s_t\big)/P$ places 70 to 81% of the fused precision on
the prior and 19 to 30% on the gauge-transported neighbors, so functionally
$\mu^{*}\approx 0.7\mu_p+0.3(\text{attention-weighted transported neighbors})$ — an attention layer
with a strong residual path, computed as a variational stationary point instead of a dot-product
softmax. The premise that capacity comes from *iterative* minimization is not what carries the
model; one aggregation is. The attention share rises with width (0.190 to 0.298 from $K=20$ to
$K=300$), so the aggregation matters more in the larger model.

## Where the context enters

Randomizing the prefix while holding the final token fixed, and measuring the relative $L^2$
displacement of that position's mean:

| stage | $K{=}20$ | $K{=}300$ |
|---|---|---|
| raw prior ($s=0$, belief $=0$) — the control | **0.00000** | **0.00000** |
| after model-channel refine ($s=1$, belief $=0$) | 0.521 | 0.812 |
| after the belief E-step ($s=1$, belief $=1$) | 0.584 | 0.872 |

The control lands exactly on zero, which confirms the raw prior is a pure per-token lookup and
validates the measurement. The belief is emphatically not context-blind, but by the time the belief
E-step runs its input already carries most of the context dependence: the model channel injects it,
taking the representation from 0.000 to 0.812 at $K=300$, and the belief E-step raises it to 0.872.

An earlier measurement of this quantity was flawed and was rewritten. Using the refined prior as the
"prior" control moved 0.556, because under `s_e_step=True` the prior *is* the refined $s$; pinning
the control with `s_e_step_n_iter=0` returned the exact zero above.

## The structural consequence

`_refine_s` is itself an attention aggregation. It runs an E-step with `lambda_gamma` coupling under
`gamma_attention_prior='causal_alibi_noself'` and its own temperature, and its output becomes the
belief's prior. Despite `n_layers=1`, the trained model is therefore

    token lookup -> s-channel attention -> belief attention (70-81% residual) -> linear decode

a two-attention-layer network rather than one. That reframes the channel redundancy above: the two
"channels" are two attention layers doing overlapping work, which is why removing one costs little
once the other is trained to compensate.

## Corrections issued in the course of this work

Recorded so they are not re-derived from stale notes. "Free energy falls monotonically while
cross-entropy rises" was wrong twice over: depth 0 exists and is the worst cross-entropy in both
runs, so the first E-step lowers free energy *and* cross-entropy and the two are aligned on the step
the model was trained to take; and free energy is not monotone, bottoming at depth 3 ($K=20$) or 5
($K=300$) and rising after, so the largest cross-entropy damage occurs where free energy is flat or
rising. "The token enters as an initial condition, not a force" was also wrong: `mm_exact` fuses
$\mu^{*}=(a\mu_p/s_p+\text{pair mean})/P$ with prior precision $a/s_p$, so the prior anchors every
iteration. Separately, the shipped artifact computed free energy on sequence 0 while cross-entropy
covered the whole batch, which is now recorded explicitly rather than silently mixed.

## Scope

Everything above holds at `prior_source='model_channel'` with `s_e_step=True`. Under
`prior_source='token'` with `s_e_step=False` the first attention layer is absent and the prior is a
pure lookup, so the belief E-step must carry all of the aggregation and its pair-precision share
should rise well above 0.30; the depth-sensitivity curve should also be nearly flat, about 0.01 to
0.02 nats out to depth 8, rather than showing the 3.5-nat cliff. Both are free checks on any such
checkpoint and neither has been run. These are single-checkpoint measurements at each width with no
seed-variance estimate, and the E-step character result is specific to the `mm_exact` update rule.

## Relevance to this research

This is the most consequential structural measurement the [[VFE Transformer Program]] has produced
about its own inference loop, and it cuts against the program's stated premise that capacity comes
from iterative variational minimization. What the loop delivers at the trained operating point is
one precision-weighted aggregation with a dominant residual — an attention layer derived from a
free-energy stationary point rather than posited, which is exactly the identification
[[GL(K) gauge-equivariant attention]] makes analytically, now with the mixing coefficient measured.
The depth attribution also retires a diagnostic artifact that had motivated an architectural
proposal, and supplies the empirical half of the refutation recorded in
[[2026-07-25-shadow-prior-refutation]].

## Cross-links

- Project: [[VFE Transformer Program]]
- Companion results the same day: [[2026-07-25-shadow-prior-refutation]] ·
  [[2026-07-25-exact-congruence-truncation-tension]] ·
  [[2026-07-25-phi-table-and-beta-channel-measurements]]
- Theory: [[GL(K) gauge-equivariant attention]] · [[Precision weighting]] ·
  [[Iterative amortized inference]] · [[Variational EM]] · [[Fixed-point iteration]] ·
  [[Divergence clamp saturation]]
- Literature: [[marino-2018-iterative-amortized-inference]] · [[dong-2021-rank-collapse]]
- Roadmap: [[VFE Transformer Research Directions (2026-06-21)]]
