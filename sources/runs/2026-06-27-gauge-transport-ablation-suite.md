---
type: run
title: "vfe3 ablation suite (2026-06-27) — gauge-transport causal ablation, 3-seed scaling, and mechanism sweeps"
aliases: [gauge transport on off frozen ablation, vfe3 ablation suite 2026-06-27, grow_K_GL10 scaling]
tags: [cluster/vfe, cluster/gauge-theory, cluster/info-geometry, cluster/attention, project/transformer, field/cs-ml]
created: 2026-06-27
updated: 2026-06-27
---

# vfe3 ablation suite (2026-06-27)

> [!info] Provenance
> `V3_Transformer` repo. Fourteen `ablation.py` sweeps under `vfe3_ablation_results/` plus the
> three-seed `scaling.py` route `grow_K_GL10` under `vfe3_scaling_results/`. WikiText-103, `train_vfe3.py`
> pipeline. Ablations: 1 layer, `embed_dim=20`, `block_glk`, `gaussian_diagonal`, `use_prior_bank=False`,
> 15k steps, **single seed=6**, operating point near test PPL 144. Scaling: 60k steps, `use_head_mixer=True`,
> **3 seeds (6/23/64)**. Full digest + manuscript-fit recommendation: `V3_Transformer/docs/2026-06-27-ablation-manuscript-digest.md`.

## Headline findings

**Gauge transport is the source of the advantage (the central causal claim).** Holding the architecture
fixed and toggling only the GL(K) gauge frame: a learned frame reaches test PPL **154**, a frame frozen at
random initialization **~279**, and the exact identity frame $\Omega_{ij}=I$ **~268**. The learned-vs-frozen
contrast is exactly parameter-matched and architecture-identical (both allocate the same 15,152,998 parameters;
only the frame learning rate differs), so the **~45% perplexity reduction** measures learning the transport
geometry rather than added capacity. A frozen random frame is worse than the identity, so an arbitrary transport
actively harms inference. (The identity arm additionally drops the learned positional gauge — `pos_phi='none'` —
so on/off conflates transport with positional encoding; the param-matched learned-vs-frozen contrast is the clean
test.) This answers the question the [[gl-k-attention]] manuscript previously named as "not yet run."

**Embedding-dimension scaling and the noise floor (only multi-seed result).** At fixed gauge-block size
$d_{\text{head}}=10$, mean test PPL over 3 seeds: 219.0 (K=10), 135.7, 113.1, 101.4, 94.1, 88.9 (K=60), 83.9
(K=70, single seed). An offset power law $\mathrm{PPL}(K)=aK^{b}+c$ fits with $b\approx-1.15$, floor $c\approx70$,
$R^2=0.999$ (a pure power law is markedly worse, $R^2=0.977$). Across-seed coefficient of variation is **0.6–1.1%**
(max–min spread up to ~2.1%) — the empirical noise floor below which single-seed ablation differences are not
interpretable.

**Canonical attention-entropy term is load-bearing only where the covariance gap is large.** Comparing the
envelope (canonical) gradient against the entropy-suppressed surrogate on the same belief trajectory: at the
lower-temperature, sharper-attention setting $\kappa=0.25$ the surrogate is **14% worse** (167 vs 146 PPL); at the
higher-temperature, more diffuse $\kappa=1$ they agree within the noise floor (146 vs 144). This matches the
$-\tau^{-1}\mathrm{Cov}_{\beta^*}(E,\partial E/\partial x)$ prediction vanishing as $\tau\to\infty$ — the first
empirical confirmation of the envelope-vs-surrogate distinction.

**Divergence order: KL is the empirical optimum.** Rényi-order sweep: 147.5, 145.4, **144.5** ($\alpha=1$, KL),
148.7, 222.1, 267.2 at $\alpha=0.5,0.8,1.0,1.2,1.5,2.0$. Flat near $\alpha=1$ (within noise), catastrophic for
$\alpha\geq1.5$ (partly numerical-clamp saturation of the non-PD covariance blend). Consistent with the
forward-KL conditional-uniqueness result.

**Positional priors: absolute fails to extrapolate, offset/relative hold.** Train at $N=128$, evaluate to
$N=512$: the absolute learned prior degrades **+11.4%** in CE, while ALiBi ($-0.4\%$), T5 relative bias ($+0.8\%$),
and RoPE ($-0.02\%$) all stay flat. In-distribution ordering is the reverse of extrapolation robustness (learned
best at train length, worst extrapolator; RoPE worst in-distribution, stable out-of-distribution).

**Supporting, lower-weight.** Under unrolled gradients PPL is flat across `n_e_steps` {1,2,3,5,8} while
straight-through degrades monotonically (300→527) — the non-Neal–Hinton EM signature. Fisher (natural-gradient)
$\mu$-preconditioning is stable across E-step counts where the raw Euclidean $\mu$-gradient blows up at 5 steps.

## Null / inconclusive (not manuscript material)

Clebsch-Gordan coupling (1.7% gain, inside the noise floor), per-head temperature dispersion (null), and
prior-anchoring vs rank collapse at depth 4 (no collapse, no anchor effect) are within-noise or shallow-depth
nulls. The gauge M-step optimizer sweep (AdamW 144 vs Killing 272 / pullback 252) is **inconclusive** because the
natural-gradient LR-rescue sweep is incomplete — it must not be read as overturning the manuscript's stated
Killing-form choice without a matched-LR sweep. Tied-vs-untied equivariance (367 vs 341 PPL) is confounded by a
55% parameter gap. Single-seed tuning sweeps (`m_p_sigma_lr`, `phi_weight_decay`) are operating-point tuning.

## Manuscript inclusion (applied 2026-06-27)

Added to [[gl-k-attention]] (vault WIPs): the gauge-transport and canonical-vs-surrogate ablations as a new
main-text paragraph in the Results section (replacing the "not yet run" sentence), and a new Supplementary
Appendix~J ("Empirical Ablations of the Gauge VFE Language Model") with the 3-seed scaling law, the Rényi-order
sweep, and the positional-extrapolation result, each cross-referenced to the derivation it corroborates.

## Relevance to this research

Second persisted results-level finding for the [[VFE Transformer Program]], and the first to test its **central
causal claim**: that the perplexity advantage comes from the learned GL(K) gauge transport rather than from
diagonal-covariance beliefs or KL attention alone. Discharges the highest-priority item of
[[VFE Transformer Research Directions (2026-06-21)]] (the gauge on/off/frozen ablation) and supplies the measured
seed-noise floor that gates every other single-seed ablation. Touches [[GL(K) gauge-equivariant attention]],
[[Holonomy]], [[Parallel transport]], [[Renyi divergence]], [[Natural gradient]], [[Relative positional encoding]].

## Cross-links
- Project: [[VFE Transformer Program]] · roadmap [[VFE Transformer Research Directions (2026-06-21)]]
- Manuscript: [[gl-k-attention]]
- Related run: [[2026-06-21-k160-hyperprior-saturation]]
- Concepts: [[GL(K) gauge-equivariant attention]] · [[Holonomy]] · [[Parallel transport]] · [[Renyi divergence]] · [[Natural gradient]] · [[Divergence clamp saturation]]
