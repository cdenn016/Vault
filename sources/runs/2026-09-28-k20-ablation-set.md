---
type: run
title: "K=20 ablation set, 2026-09-28 to 2026-09-29 (fifteen single-seed runs)"
aliases: [K20 ablation set 2026-09-28]
tags: [cluster/vfe, cluster/gauge-theory, cluster/info-geometry, cluster/attention, project/transformer]
created: 2026-09-29
updated: 2026-09-29
---

# K=20 ablation set (fifteen single-seed runs)

Frozen record of the runs analyzed on 2026-09-29 in `VFE_3.0/vfe3_runs/` (the K=64 full-Gaussian series is excluded). Full analysis, figure, and scripts: `VFE_3.0/docs/experiments/2026-09-29-k20-ablation-analysis.md`. The design and derivations behind the optimizer routes tested here: `VFE_3.0/docs/derivations/2026-09-28-phi-natgrad-link-spectrum.md` and `2026-09-28-phi-natgrad.tex`.

## Protocol and statistical basis

WikiText-103, GPT-2 tokenizer, $K=20$, two blocks of $d=10$, two layers, `projected_predictive`, `gaussian_diagonal`, `block_glk`, moment-matched covariance, no attention residual, model seed 6, data seed 3, 15,000 steps at batch 64 and context 128 (about one epoch), bf16, evaluation stride 32. Every run was dirty at its start SHA and every best-validation checkpoint is the final step. One seed per condition; the user's seed SD is about 1.5 PPL, so a pairwise difference has SD about 2.1 PPL and differences under about 4.2 PPL are not established. All conclusions are one-epoch and step-matched.

## Runs (test perplexity)

| test PPL | label | fields that define the run |
|---|---|---|
| 109.23 | diagonal_chunked_mahal_tau-small | KL-to-bank decoder, $\tau=0.1$, Mahalanobis block norm, coordinate MLP, decays 0.025/0.04/0.05 |
| 110.21 | canon-frame-mlp | as above with `canonical_frame` MLP, mu and sigma decay 0, phi decay 0.1 |
| 114.06 | diag-chunk_mahal_tau=1 | KL decoder $\tau=1$, decays as 110.21, coordinate MLP |
| 114.19 | canFrame-DecRef-optimized | 117.73 with retuned learning rates (m_phi 0.003, mu 0.025, mlp 0.0025, LN 0.005) |
| 117.73 | can-frame-decode-ref | 110.21 with `decode_coordinates='reference'` |
| 120.50 | hidden-mlp-bias | linear decoder, LayerNorm, ALiBi, per-type hidden bias (+10.1M parameters) |
| 121.27 | fisher-log_decCord | 110.21 with `fisher_group`, `group_log`, m_phi_lr 0.005 (decode coordinates local) |
| 126.44 | mahalanobis-local_noAlibi | linear decoder, Mahalanobis norm, causal prior |
| 130.14 | causal_pos-lrn_LNref | linear decoder, LayerNorm, `block_coordinates='reference'`, causal prior |
| 132.02 | LN-block-ref | 130.14 with `causal_alibi` |
| 132.03 | gauge-gate | linear decoder, LayerNorm, `gauge_gate` MLP, ALiBi |
| 132.95 | baseline | linear decoder, LayerNorm, `gaussian_template` MLP, ALiBi |
| 134.46 | decode_cord=reference | 132.95 with `decode_coordinates='reference'` |
| 145.72 | pos_phi=None_LNref | 132.02 without learned positional frames |
| 160.05 | LN-ref_Gauss-Template | reference block, template MLP, no positional frames, causal prior |

## Results that exceed seed noise

- Linear to KL-to-bank decoder: 126.44 to 109.23 (one field, $-17.2$, sign-consistent at every checkpoint). Replacing the decode-bank sigma table post hoc by each class's mean costs $+0.60$ nats in run 109.23 (paired SE at most 0.023), so the gain runs through learned per-class precisions that vary only about 9 percent around their common value.
- Removing learned positional frames: $+13.7$ (one field). Previous-token attention mass 0.15 to 0.06; mean attention distance roughly doubles.
- Reference-coordinate decoder with the KL decoder: $+7.5$ (one field, narrowing from $+11$). With the linear decoder: $+1.5$, inside noise. The covariant `canonical_frame` block MLP shows no measurable cost; MLP type never differs by more than 1 PPL.
- The prior sigma tables have update ratio about $10^{-4}$ (`m_p_sigma_lr=0.001`) and end near initialization plus decay, yet flattening the encode table costs 0.06 to 0.15 nats.
- $\tau=1$ was the best run from 1k to 7.5k steps and finished 4.8 PPL behind $\tau=0.1$; the pair also changes decays, and with decays fixed the late gap is inside noise.
- Belief-Fisher $\varphi$ step: $+11.1$ against the matched AdamW run 110.21 (three coupled differences: stateless, count-normalized, untuned learning rate). Step mechanics were clean (no rejected or off-strip rows, trust radius never binding); natural direction cosine 0.94 with the raw gradient; kernel leak 0.43 to 0.52.
- Belief covariance trace is negatively correlated with per-token CE (Spearman about $-0.3$ in the Mahalanobis runs), so it does not act as calibrated uncertainty.

## Relevance to this research

Bears on [[Natural gradient]] for the frame tables, on the softmax-bottleneck reading of the decoder, and on what the gauge frames contribute beyond position. See [[VFE Transformer Program]] and [[Information geometry and natural gradient]].
