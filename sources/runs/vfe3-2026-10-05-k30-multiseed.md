---
type: run
title: "VFE_3.0 three-seed noise floor at K=30, October 5, 2026"
aliases: ["vfe3 multiseed 2026-10-05", "K=30 three-seed noise floor"]
tags: [cluster/attention, cluster/vfe, project/transformer, field/cs-ml, field/statistics]
year: 2026
created: 2026-10-05
---

# VFE_3.0 three-seed noise floor at K=30, October 5, 2026

> [!info] Scope
> Three WikiText-103 training runs of one configuration that differ in the model seed (6, 54, 271), in `VFE_3.0/vfe3_runs/multiseed_20261005-112404/`, run on the RTX 5090 (`cuda:0`, torch `2.10.0.dev20251210+cu128`) on October 5, 2026, and digested by `multiseed_analysis.py` with `allow_mixed_code_identity=True`. The directories are `87.36_wikitext-103_K30_block_glk_linear_mlp_s6`, `86.82_wikitext-103_K30_block_glk_linear_mlp_s54` and `87.40_wikitext-103_K30_block_glk_linear_mlp_s271`. The request manifest `multiseed_request.json` lists the three seeds as complete. This is the vault's current multi-seed measurement for the VFE_3.0 line and replaces the earlier informal seed SD of about 1.5 PPL quoted in [[2026-09-28-k20-ablation-set]] for noise-floor purposes.

## Configuration

$K=30$ with two heads of width 15 and block-diagonal $\mathrm{GL}(15)\times\mathrm{GL}(15)$ frames (`block_glk`, gauge transport on), four layers, `projected_predictive` attention with `gaussian_kl` relational routing and the `exponential` content-link chart, the diagonal Gaussian family, moment-matched predictive covariance with floor $10^{-4}$, an attention residual, a learned positional frame (`pos_phi=learned`, no rotary rotation), causal source prior, affine LayerNorm followed by a coordinate GELU block MLP of expansion eight with passthrough covariance, no head mixer, and the linear decoder. Training: 15,000 steps at batch 64 and context 128 (122.88M token presentations, about 1.05 epochs of the 116.84M-token training split), warmup 100, bf16, one E-step, evaluation stride 32. Data seed 3 is shared by all three runs, so they see the same batch order; the across-seed spread measures initialization and optimization noise only.

## Results

| metric | seed 6 | seed 54 | seed 271 | mean | SD (ddof=1) |
|---|---|---|---|---|---|
| test PPL | 87.364 | 86.818 | 87.400 | 87.194 | 0.326 |
| best validation PPL | 86.341 | 85.950 | 86.455 | 86.249 | 0.265 |
| test CE (nats/token) | 4.47009 | 4.46381 | 4.47050 | 4.46815 | 0.00375 |

Further across-seed summaries (mean, SD): test bits per token 6.4462, 0.0054; test bits per character 1.4136, 0.0012; fixed training-sample CE 4.4395, 0.0017; ECE 0.0070, 0.0006; wall time 3238 s, 18 s. Frequency-stratified test CE: rare 10.323 (SD 0.098), mid 8.278 (0.025), frequent 4.005 (0.008). The covariance diagnostics vary much more across seeds: `sigma_trace_cv` 0.33 (CV 35%) and `sigma_ce_spearman` $-0.063$ (CV 70%). The best validation step was the final step (15,000) in every run. The per-layer channel was withheld by the digest as incomplete; per-step curve bands and 14 figures were written.

## Noise floor

With $n=3$ the test-PPL SD estimate is 0.33 PPL (0.0037 nats). A difference between two single-seed runs then has SD about $\sqrt2\times0.33=0.46$ PPL (0.0053 nats), so single-seed differences smaller than about 0.9 PPL (0.011 nats) at this configuration are not established at two standard deviations. Two degrees of freedom make the SD estimate itself loose: the 95% chi-square interval for the population SD is about $[0.52s, 6.3s]$, that is 0.17 to 2.1 PPL, which still contains the earlier informal 1.5 PPL figure. The floor is specific to this $K=30$, four-layer, one-epoch configuration and shared data order; it is not measured for other widths, depths or token budgets.

## Provenance

The seeds do not share one code identity. Seed 6 ran at VFE_3.0 commit `891cb1ab` (merge of PR #44, frame precision) and seeds 54 and 271 at `389413b2` (merge of PR #45, removal of head mixers), each with a different dirty-tree fingerprint (`991895fd`, `274e8759`, `616c8193`). Seed 6 and seed 271 record code- and source-archive drift during training; seed 54 records git- and source-identity drift but no code drift. The user states that the code differences are unrelated to this configuration; the active configuration has `use_head_mixer=False`. The across-seed SD includes any effect of those differences. Data hashes, shared by all three: train `d0c97b5ccf40a3cf911921150fc734aa3f96ba832370d9cab32bbf96287b827e` (116,840,318 tokens), validation `292074c56d586340490eb0dbba30065844213e1f43eec01860e071557c5156de` (245,021), test `d2a72d019f850fc7dbcb080944a8c251b7670fecb385ae853fac4809e178ae6d` (280,542); tokenizer tag `tiktoken`.

The digest (`MULTISEED_ANALYSIS.md`, `multiseed_summary.json`, `multiseed_summary.csv`, `multiseed_request.json` and three figures) is archived in [the run archive](../archives/vfe3-2026-10-05-k30-multiseed/MULTISEED_ANALYSIS.md.txt).

## Relevance to this research

This is the first multi-seed noise floor in the VFE_3.0 line with frozen data identity and a request manifest. Every single-seed comparison in [[2026-09-28-k20-ablation-set]] and [[vfe3-2026-10-03-link-charts-and-channel-receiver]] needs a seed floor to be read; this note supplies one for a neighboring configuration ($K=30$, four layers) rather than for those $K=20$, two-layer runs, so transferring it to them is an assumption. See [[VFE Transformer Program]] and [[Projected predictive attention]].
