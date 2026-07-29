---
type: run
title: "Token-prior E-step character: a refuted prediction, and the diagnostics made permanent (2026-07-25)"
aliases:
  - "token prior E-step character"
  - "2026-07-25 s_e_step=False checkpoint"
  - "mechanism diagnostics buildout"
tags:
  - cluster/vfe
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-07-25
updated: 2026-07-25
---

# Token-prior E-step character: a refuted prediction, and the diagnostics made permanent (2026-07-25)

> [!info] Provenance and evidence boundary
> Checkpoint-only measurements on
> `V3_Transformer/vfe3_runs/169.48_wikitext-103_K20_block_glk_linear_mix_s6` (run timestamp
> 2026-07-25T19:56:24, 15,153,002 parameters, WikiText-103, seed 6, 15,000 steps). Configuration
> read from the run's own `config.json`: $K=20$, 2 heads, 1 layer, `n_e_steps=1`,
> **`s_e_step=False`**, **`prior_source='token'`**, `e_step_update='mm_exact'`,
> `family='gaussian_diagonal'`, `lambda_beta=1.0`, `lambda_gamma=0.75`,
> `gamma_as_beta_prior=True`, `learnable_r=False`, `r_update_mode='gradient'`, `kl_max=160`,
> `use_prior_bank=False`, `lambda_alpha_mode='state_dependent_per_coord'`,
> `beta_attention_prior='causal_alibi_noself'`. Probes run under `C:/anaconda/python.exe` (CUDA
> build, RTX 5090) against repository revision `4686082`; the diagnostics described in the last
> section merged at `7b27217`. The depth table is the run's own shipped
> `estep_depth_sensitivity.json` (64 sequences); the character table is an 8-sequence probe.

## What this tests

[[2026-07-25-estep-character-and-channel-decomposition]] measured the belief E-step at
`prior_source='model_channel'` with `s_e_step=True`, and closed with two registered predictions for
any checkpoint trained with the model channel OFF. With the $s$-channel attention layer absent and
the prior reduced to a pure token lookup, the belief E-step would have to carry all of the
aggregation, so (i) its pair-precision share "should rise correspondingly", stated as well above
0.30, and (ii) the depth-sensitivity curve "should be nearly FLAT (~0.01-0.02 nats out to depth 8)
rather than showing the ~3.5-nat cliff". Such a checkpoint now exists. One prediction holds
directionally, the other is refuted outright.

## Prediction (ii): flat, but eight times less flat than predicted

The shipped artifact reports `model_channel_live: false` and an empty `model_channel_points`, which
confirms the 2026-07-25 decoupling behaves as designed when the refine is gated off.

| belief depth | CE | free energy / token |
|---|---|---|
| 0 | 5.8840 | 32.1264 |
| **1 (trained)** | **5.1099** | 31.9354 |
| 2 | 5.1466 | 31.9087 |
| 3 | 5.1817 | 31.9029 |
| 5 | 5.2047 | 31.9009 |
| 8 | 5.2090 | 31.9007 |

The cliff is gone: **+0.0992 nats** from depth 1 to depth 8, against the +3.48 the conflated
diagnostic produced and the +3.479 the model channel alone produced. But the prediction of 0.01 to
0.02 nats was wrong by roughly a factor of eight, and the comparison that matters is against the
belief-only arm of the earlier run, which moved +0.012 at the same width. **Removing the model
channel made the belief loop eight times more depth-sensitive, not equally flat.** One belief
E-step is worth 0.774 nats here, against 1.343 nats for the belief channel of the model-channel
model. Free energy is monotone decreasing across the whole sweep, unlike the model-channel
checkpoints, where it bottomed at depth 3 or 5 and rose after.

## Prediction (i): refuted, and the opposite happened

| | token prior, `s_e_step=False` | model channel, $K{=}20$ | model channel, $K{=}300$ |
|---|---|---|---|
| **pair (attention) share of fused precision** | **0.109** | 0.190 | 0.298 |
| prior (residual) share | **0.891** | 0.810 | 0.702 |
| $\lVert\Delta\mu\rVert/\lVert\mu_p\rVert$ | **0.521** | 0.147 | 0.227 |
| $\cos(\text{dir}_8,\text{dir}_1)$ | +0.971 | +0.982 | +0.962 |
| step-1 share of displacement | 99.8% | 73% | 70% |

The share was predicted to rise above 0.30. It **fell to 0.109**, so the residual path grew to 89%
rather than shrinking. The belief E-step did not take over the aggregation when the $s$-channel was
removed. The share is also flat in depth, moving only 0.1088 to 0.1096 out to eight iterations.

The decomposition is bit-certified rather than inferred: it is recomputed from the same public
helpers the kernel uses and then reproduces the kernel's own returned `mu_star`, with a maximum
absolute residual of exactly `0.000e+00`. (The doubled call count observed while instrumenting is
the bfloat16-to-float32 autocast island recursing into itself once with identical arguments, not a
second call site.)

**Weight and displacement decoupled, which resolves the apparent contradiction.** The pair weight
fell while the belief moved 3.5 times further. Displacement measures how far the prior sat from the
answer, not how much work attention is doing: with a raw token lookup, $\mu_p$ is far from the
neighbor consensus, so even an 11% weight produces a large move; with the $s$-refined prior, $\mu_p$
already sits near the consensus because the $s$-channel performed the aggregation, so a 19% weight
barely moves it. The two quantities should not be read as proxies for one another, and the earlier
note's framing of a rising share as the signature of "carrying the aggregation" was too simple.

## Perplexity: an upper bound, not an attribution

Minimum logged `val_ppl` is **172.05** for this run against **139.30** for the model-channel arm at
the same width, seed and step budget.

> [!warning] Do not read this as the model channel's worth. The 139.30 arm is the winner of a tuned
> ablation grid; this token-prior arm is a first configuration whose learning rates and coupling
> weights have not been swept. The 33-PPL difference therefore confounds architecture with
> optimization effort and is an **upper bound** on the architectural cost, not a measurement of it.
> Closing it requires tuning the token-prior arm over comparable grid dimensions and comparing
> best against best. Recorded on the author's correction, 2026-07-25.

This also retires an unsupported sentence in the earlier note, which offered channel redundancy as
the explanation for `prior_source='token'` reaching "comparable perplexity". At matched budget the
untuned arm is 24% worse, and the comparison is open in both directions rather than settled either
way.

## What was made permanent

The operative lesson is not any single number. Every measurement in this investigation came from a
throwaway script, which is the same condition under which the shipped depth probe reported the model
channel under the belief loop's name for weeks. Three probes were therefore promoted into the
end-of-run artifact path, each persisting JSON, rendering a figure, and printing its headline to the
run log: an E-step character probe (displacement, trajectory straightness, and the pair/prior
precision split), a $\beta$ channel decomposition (positional prior against content energy), and a
context-sensitivity probe (prefix randomization, staged by channel). Only the last is expensive and
it is the only one behind a toggle, default off; gating the cheap tier would recreate the condition
being fixed.

The character probe carries its own falsification hook. It reproduces the kernel's `mu_star` from
the decomposition it reports and logs a warning if that residual ever leaves zero, so a probe that
silently stops matching the kernel becomes visible in the artifact rather than in a later
investigation. Two defects were caught by its tests before merge, both of the same family as the
original diagnostic bug: `inference/e_step.py` binds the update kernel at import, so patching only
the definition module left the live call site untouched while the probe reported success; and the
$\beta$ decomposition is not specific to one update rule, since both belief routes read the same
attention binding.

## Relevance to this research

Two registered predictions were tested against a new checkpoint and one failed, which is the
[[VFE Transformer Program]]'s intended discipline working. The substantive correction is that the
prior/pair precision split is not a measure of how much aggregation a channel performs: the token
prior configuration moves its belief much further while weighting its neighbors much less. Any
future reading of that share, including the rising-with-width trend recorded for the model-channel
checkpoints, must account for where the prior sits relative to the consensus rather than treating
the share as an aggregation strength. The perplexity comparison is explicitly not closed, and the
tuning-versus-architecture confound is the obstacle to closing it.

## Cross-links

- Project: [[VFE Transformer Program]]
- Supersedes the two registered predictions and the "comparable perplexity" reading of:
  [[2026-07-25-estep-character-and-channel-decomposition]]
- Companion results the same day: [[2026-07-25-phi-table-and-beta-channel-measurements]] ·
  [[2026-07-25-exact-congruence-truncation-tension]] · [[2026-07-25-shadow-prior-refutation]]
- Theory: [[Precision weighting]] · [[Iterative amortized inference]] ·
  [[GL(K) gauge-equivariant attention]] · [[Variational EM]]
