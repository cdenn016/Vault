---
type: run
title: "VFE_3.0 link charts and channel receiver at K=20, October 3, 2026"
aliases: ["vfe3 link charts 2026-10-03", "K=20 content-link chart runs"]
tags: [cluster/attention, cluster/gauge-theory, cluster/vfe, project/transformer, field/cs-ml]
year: 2026
created: 2026-10-04
---

# VFE_3.0 link charts and channel receiver at K=20, October 3, 2026

> [!info] Scope
> Four single-seed WikiText-103 training runs in `VFE_3.0/vfe3_runs/10-3-2026_Experiments/`, executed on the RTX 5090 (`cuda:0`, torch `2.10.0.dev20251210+cu128`) on October 3, 2026, and reported in Section 9.3 of [[dennis-2026-glk-lie-algebra-links-v2]]. The directories are `121.77_wikitext-103_K20_affine`, `121.98_wikitext-103_K20_first-order`, `121.53_wikitext-103_K20_exponential` and `124.93_wikitext-103_K20_exponential_gradient`. Each saved configuration differs from the exponential arm in exactly one key: `content_link_chart` (`affine`, `first_order`) or `attention_mode="projected_gradient"`. They are the first training runs of the `content_link_chart` selector and of the channel-likelihood receiver.

## Configuration

All four runs use $K=20$ with two heads of width 10 and block-diagonal $\mathrm{GL}(10)\times\mathrm{GL}(10)$ frames, two layers, the diagonal Gaussian family, no attention residual ($r=0$), moment-matched predictive covariance with floor $10^{-4}$, affine LayerNorm followed by a coordinate GELU MLP of expansion eight, and the linear decoder. Positions enter through rotary rotations of the routing frame (base 100, not applied to values); there is no learned positional frame, and the source prior is uniform on the causal support. Training used seed 6 with the same data order in every arm, 15,000 AdamW updates of batch 64 at context 128 (about 1.05 passes over the training tokens) and bfloat16 automatic mixed precision. With `relational_output_init="identity"` and $T=I$, the stored factor starts at $O=I$, $0$ and $0$ in the affine, first-order and exponential charts, so all arms begin from the same effective receiving map $\widetilde O=I$. The receiver arm uses `relational_receiver_law="channel_likelihood"`, `relational_receiver_update="closed_form"`, damping 1, channel noise 1 and `lambda_alpha_mode="state_dependent_per_coord"` with $b_0=c_0=1$. Evaluation used context 128, stride 32 and 280,541 scored test targets. Each model has 13,133,478 parameters, of which 16,401 lie outside the per-type tables.

## Results

| Arm | Content update | Test CE (nats) | Test PPL | Best validation PPL | Final validation CE | Wall time (s) |
|---|---|---|---|---|---|---|
| Affine, $\widetilde O=O$ | predictive mean | 4.80216 | 121.77 | 121.41 | 4.79920 | 1344 |
| First order, $\widetilde O=T^{-1}+O$ | predictive mean | 4.80390 | 121.98 | 122.38 | 4.80716 | 1372 |
| Exponential, $\widetilde O=e^{OT}T^{-1}$ | predictive mean | 4.80016 | 121.53 | 121.69 | 4.80144 | 1464 |
| Exponential, receiver | closed-form channel receiver | 4.82773 | 124.93 | 124.98 | 4.82818 | 1677 |

The best validation step was the final step (15,000) in every arm. The three predictive arms differ by at most 0.0037 nats per token on test and 0.0080 on validation, and their order differs between the splits. The receiver arm is 0.0276 nats above the exponential predictive arm on test. The receiver arm also passes the covariance through instead of moment matching it, so that gap does not isolate the receiver. Its layer prior equals the incoming state at every episode start, so the profiled coupling stays at $c_0/b_0=1$ and each layer applies a Kalman update of the incoming mean. These are single-seed differences; the author's earlier estimate of the seed-to-seed standard deviation for $K=20$ configurations, about 1.5 perplexity points near perplexity 120, was not measured on these arms.

## Trained link geometry

Computed in float64 from the twelve saved map snapshots per run (steps 0 to 15,000) by `manuscripts/Attention/glk_lie_links_checks/trained_link_geometry.py`, for the stacked transfer $M=\widetilde OT$. The layer-0 determinant of the first-order arm was negative at steps 1000 to 3000 and positive from step 4500 on, so that link crossed the singular set at least twice; the affine arm's layer-0 minimum singular value after step 1000 was $8.7\times10^{-3}$ (final condition number 677), and the first-order arm's was $8.5\times10^{-3}$. Both exponential arms kept a positive determinant by construction and a minimum singular value above 0.11 after step 1000, with final condition numbers 12 to 42. The final trained generators $X=OT$ have spectral norms 1.9 to 3.0, where the first-order polynomial differs from $e^X$ by 33 to 58 percent in relative spectral norm. These are properties of four trained models at $K=20$.

## Provenance

All runs recorded dirty source trees and saved an archive of the start-of-run source (`source_archive.zip`). The affine and first-order arms ran at VFE_3.0 commit `f89448f2` with stable git and code identity. The exponential arm started at `0f05ec92` and ended at `f89448f2`, a recorded git-identity drift, while its process code identity matched the archive and showed no code drift. The receiver arm ran at `f89448f2`, but its dirty fingerprint and its source tree changed during training (`code_identity_drift` and `source_archive_drift` true); its process code identity matched the archived start tree. Data hashes: train `d0c97b5ccf40a3cf911921150fc734aa3f96ba832370d9cab32bbf96287b827e`, validation `292074c56d586340490eb0dbba30065844213e1f43eec01860e071557c5156de`, test `d2a72d019f850fc7dbcb080944a8c251b7670fecb385ae853fac4809e178ae6d`; tokenizer ranks `be5c03b8b3757737fd6803c3096005756b803985ef1fd8b1a9c788b35a3e8a11`.

The same folder holds four further runs made at commit `f35c573a`, before the chart selector existed, with different configurations: `114.72_wikitext-103_K20_baseline-adjusted` (four layers, attention residual, learned positional frame, different learning rates), `54.73_wikitext-103_K64_depth-scaled` and `54.39_wikitext-103_K64_identity` (four layers at $K=64$), and `46.42_wikitext-103_K64_gradient_4epoch` (six layers, `projected_gradient`, 120,000 steps). They are not part of this matched comparison and no comparison is recorded from them here.

## Relevance to this research

The runs test the prediction of [[dennis-2026-glk-lie-algebra-links-v2]] that the three charts, which share one function class up to the real-logarithm domain, should not differ in held-out loss by themselves, and they show where the charts do differ: in the singular-set crossing and conditioning of the trained links. See [[Projected predictive attention]], [[Projected gradient attention]], [[GL(K) gauge-equivariant attention]] and [[VFE Transformer Program]]. The open item recorded in [[vfe3-2026-10-02-projected-route-consolidation]], that no training run of the projected-gradient receiver existed, is answered here for one configuration in which the profiled coupling is inert.
