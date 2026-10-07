---
type: run
title: "VFE_3.0 per-type read-table transformer baseline at K=128, October 6, 2026"
aliases: ["vfe3 block_read baseline 55.10", "K=128 per-type read-table baseline"]
tags: [cluster/attention, cluster/vfe, project/transformer, field/cs-ml, field/statistics]
year: 2026
created: 2026-10-07
---

# VFE_3.0 per-type read-table transformer baseline at K=128, October 6, 2026

> [!info] Scope
> Read-only record of the conventional-transformer control run on October 6, 2026 for the GL(K) attention manuscript. Run directories: `D:/DATA_KEEP/10-6-2026_Baselines/` (first learning-rate sweep and the 3e-3 full-length run) and `VFE_3.0/vfe3_runs/baselines/` (the same runs plus the extended sweep and the 5e-3 full-length run). Numbers come from each run's `config.json`, `summary.json`, `provenance.json`, `resources.json` and the two `lr_sweep.json` files, read on October 7, 2026. No training was run for this note. The author identified this study as the careful baseline study for the paper, superseding the earlier pairs recorded in [[vfe3-2026-10-05-k128-exponential-and-parameter-accounting]] (39.77 against 90.15 at $K=128$, 52.91 against 117.63 at $K=64$), which are not paper results.

## The control

A conventional transformer of width 128 (four layers, four heads of width 32, feed-forward expansion as in the realization) whose input table adds a learned $4\times32\times32$ block read map per vocabulary entry (`per_type_table='block_read'`, zero-initialized), applied to the attention input, so that its per-type storage (212.3M numbers, 4,224 per entry) nearly equals the frame table of the evaluated realization (218.7M, 4,352 per entry). Non-embedding parameters are 1,317,632 in both; the baseline totals 220,086,353 parameters. It was trained under the protocol of the $K=128$ exponential-chart run `34.48_wikitext-103_K128_block_glk_linear_mlp_s6`: 150,000 updates at batch 32, context 128, evaluation stride 32, 614.4M token presentations, model seed 6 and data-order seed 3.

## Learning-rate selection

A first 6,000-step sweep over $3\times10^{-4}$, $6\times10^{-4}$, $10^{-3}$, $2\times10^{-3}$ and $3\times10^{-3}$ selected $3\times10^{-3}$ on validation (best validation perplexity 186.4, 141.3, 121.8, 107.4 and 102.25 respectively). An extended sweep adding $4\times10^{-3}$, $5\times10^{-3}$ and $7\times10^{-3}$ selected $5\times10^{-3}$ (100.34). At full length the $3\times10^{-3}$ run reached best validation perplexity 53.65 and test perplexity 55.10 (test cross-entropy 4.0091 nats), and the $5\times10^{-3}$ run 55.09 and 56.58 (4.0357 nats). The reported rate, $3\times10^{-3}$, is the first sweep's validation choice and the better of the two full-length runs on validation and test.

## Comparison with the realization

The evaluated realization reached test perplexity 34.48 (3.5404 nats), so the baseline trails it by 0.47 nats in one seed. The control is partial: its table reads but does not write (no frame after the receiving map, none on content, no positional frames); it uses ALiBi where the realization uses a uniform causal prior with learned positional frames; its AdamW uses $\beta_2=0.95$ and weight decay 0.1 on the token embedding and the table, where the realization uses $\beta_2=0.999$ and no decay on the prior means; both full-length baseline runs reached their best validation at the final step, while the realization's validation loss had turned upward; and the baseline trained in 5,238 s against 58,897 s for the realization on the same RTX 5090.

## What is not established

One seed per arm, so no seed variability; no write-side table analogue; no frozen-frame or identity-frame realization; no $K=64$ replica; no optimizer-matched pair. The comparison shows that a read-side per-type table of nearly equal size does not by itself reach the realization's perplexity under this protocol, not that frame geometry is the cause.

## Relevance to this research

This is the control that the GL(K) manuscript ([[dennis-2026-glk-attention-v2-review-2026-10-07]]) now reports in its parameter-accounting table, and the reference for the retraction rule it states in advance for the frame claim at $K=128$. It bears on the [[VFE Transformer Program]] question of whether learned frames act through geometry or through per-type table size; see [[GL(K) gauge-equivariant attention]].
