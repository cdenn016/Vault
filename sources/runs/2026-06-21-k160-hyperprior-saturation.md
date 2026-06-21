---
type: run
title: "K=160 runs — hyper-prior KL(s‖r) saturates the kl_max clamp"
aliases: [K160 hyper-prior clamp saturation, kl_max saturation run 2026-06-21]
tags: [cluster/vfe, cluster/info-geometry, project/transformer, field/cs-ml]
created: 2026-06-21
updated: 2026-06-21
---

# K=160 runs — hyper-prior KL(s‖r) saturates the kl_max clamp

> [!info] Provenance
> `V3_Transformer` repo, branch `vfe3-per-layer-figures`. Two wikitext-103 runs at **K = embed_dim = 160**:
> `vfe3_runs/76.53_wikitext-103_K160_block_glk_linear_mix_s6` (test ppl **76.53**) and
> `vfe3_runs/66.48_wikitext-103_K160_block_glk_linear_mix_s6-2epochs` (test ppl **66.48**, 2 epochs).
> Measured directly from each `best_model.pt`. Full analysis: `V3_Transformer/docs/2026-06-21-edits.md`.

## Configuration (frozen)

1-layer `block_glk` transformer, `n_heads=4`, `d_head = K/H = 40`, `max_seq_len=128`, `vocab_size=50257`.
`divergence_family='renyi'`, `renyi_order=1.0` (= KL), `family='gaussian_diagonal'`, `gradient_mode='filtering'`.
`kl_max=100.0`, `eps=1e-6`. Model channel active: `lambda_h=0.25`, `lambda_h_mode='constant'`, `lambda_gamma=0.75`,
`lambda_beta=1.0`, `prior_source='model_channel'`, `s_e_step=True`, `learnable_r=True`, `r_update_mode='gradient'`,
`weight_decay=0.02`, `n_e_steps=1`.

## Observation

The hyper-prior free-energy block — the model-fiber self-coupling $\lambda_h\,\mathrm{KL}(s_i\|r)$ — is **pinned at
exactly the `kl_max=100` clamp**. The figure `model_channel_terms.png` shows $\mathrm{KL}(s_i\|r)$ rising to 100 by
~5k steps and holding there through all 60k steps; `free_energy_decomposition.png` reports the block at exactly
$0.25 \times 100 = 25.0$ nats/token.

## Measured (unclamped) divergence over the vocab

Per-token diagonal $\mathrm{KL}(s_v\|r)=\tfrac12\sum_{k}\big[\sigma^{s}_k/\sigma^{r}_k+(\mu^{s}_k-\mu^{r}_k)^2/\sigma^{r}_k-1+\log(\sigma^{r}_k/\sigma^{s}_k)\big]$
over all $V=50257$ rows, computed from the trained `s_mu_embed`, `s_sigma_log_embed`, `r_mu`, `r_sigma_log`:

| run | median KL | mean KL | max KL | % vocab ≥ 100 (gradient masked) | nats/coord | μ-term | σ-term |
|-----|-----------|---------|--------|----------------------------------|------------|--------|--------|
| ppl 76.53 (1 ep) | 124.7 | 126.6 | 584 | **100.0%** | 0.791 | 72.2 | 54.4 |
| ppl 66.48 (2 ep) | 25.4 | 26.9 | 176 | **0.1%** | 0.168 | 3.9 | 22.9 |

The clamp budget per coordinate is $100/160 = 0.625$ nats; the trained rate (0.791) exceeds it, so the saturation
threshold is $K^\* = 100/0.791 \approx 126$. At the old default K=20 the budget was 5 nats/coord and the block never
saturated — the pathology appears only at large K.

## Mechanism (verified in code)

`safe_kl_clamp` is a **hard** clamp `kl.clamp(min=0, max=kl_max)` (`vfe3/families/base.py:26`), so
$d(\text{clamped})/d(\cdot)=0$ above the ceiling. The active config takes the closed-form filtering kernel
(`uses_kernel_route(...)=True`, `vfe3/gradients/kernels.py:168`), whose self-mask
`self_mask = ((raw_self > 0) & (raw_self < kl_max))` (`kernels.py:129`) **zeroes the hyper-prior self-coupling
gradient** wherever the raw divergence saturates; the autograd oracle is no escape (it differentiates through the
clamp, derivative 0). The only live gradient route to the learnable `r` is that same self term, so during the pinned
phase `r` is **gradient-frozen** ($d\,\text{grad}_\mu/d\,r_\mu = 0$ when saturated). Under `s_e_step=True` the
hyper-prior term is gated **out** of the scored M-step loss (`vfe3/model/model.py:890`) and acts only as the s-E-step
descent direction, so this is a *silently disabled regularizer + frozen r*, not corrupted training: the gamma
pair-coupling term stays live (`kernels.py:136`), so `s` keeps training, and the ppl 66.48 run escapes saturation —
but via weight-decay/CE dragging $\mu^s,\mu^r\to 0$ (μ-term 72→4), **not** via the masked hyper-prior.

The per-head pairwise belief/gamma energies are computed per irrep block over $d_\text{head}=40$
(`vfe3/free_energy.py:139`), not full K, so they saturate the same clamp only at $K\approx 455\text{–}600$ (H=4) — well
above where the full-K self-divergences die. The full-K self-couplings $\mathrm{KL}(q\|p)$ and $\mathrm{KL}(s\|r)$ are
the first and immediate saturators.

## Remedy applied

`kl_max` is the numerical safety-net clamp (next to `eps`), not an operating ceiling. Fix: scale it with K so it binds
only on genuine NaN/inf/Cholesky blowups. Applied in `train_vfe3.py` as `config["kl_max"] = 8 * config["embed_dim"]`
(≈1280 at K=160; auto-tracks K). Provably theory-neutral — `safe_kl_clamp` is the identity below the ceiling, so F,
$\beta^\*$, $\gamma^\*$, and every gradient are `kl_max`-independent there; $\tau=\kappa\sqrt{d_\text{head}}$ never reads
`kl_max`. Normalizing divergences by $1/K$ was rejected: it silently detunes the softmax temperature from
$\kappa\sqrt{K}$ to $\kappa K^{3/2}$. Per-coordinate `lambda_h` was previously rejected (re-linearizes the K-sum).

## Relevance to this research

First persisted results-level finding for the [[VFE Transformer Program]] and the empirical basis for
[[Divergence clamp saturation]]. It is the concrete failure mode behind the program's width-scaling difficulty: the
fixed divergence clamp silently disables self-coupling regularizers (and freezes a learnable centroid) as K grows.
Touches [[Renyi divergence]], [[Belief coupling]], [[Natural gradient]], [[Precision weighting]].

## Cross-links
- Concept: [[Divergence clamp saturation]]
- Project: [[VFE Transformer Program]]
- Related: [[Renyi divergence]] · [[Belief coupling]] · [[gl-k-attention]] · [[participatory-it-from-bit]]
