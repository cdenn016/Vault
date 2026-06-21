---
type: concept
title: "Divergence clamp saturation"
aliases: [kl_max clamp, kl_max saturation, K-width clamp problem, divergence saturation, divergence clamp]
tags: [cluster/vfe, cluster/info-geometry, project/transformer]
status: draft
created: 2026-06-21
updated: 2026-06-21
---

# Divergence clamp saturation

## Definition

A failure mode in which a **dimension-independent** numerical clamp on a divergence — the `kl_max` ceiling applied by
`safe_kl_clamp` — collides with a divergence whose magnitude **grows with the belief dimension K**. For diagonal
Gaussian beliefs the KL / Rényi divergence is a sum over the K coordinates, so at a roughly constant per-coordinate
rate $r$ nats/coord the total is $\approx rK$. The clamp $\mathrm{KL}\mapsto\min(\mathrm{KL},\,k_\text{max})$ therefore
**binds for all beliefs once $K \gtrsim k_\text{max}/r$**. Because the clamp is *hard* (`kl.clamp(min=0, max=kl_max)`),
its derivative is zero above the ceiling — the clamped term becomes a **constant with no gradient**, silently
disabling whatever it was meant to regularize. The pathology is monotone in K: the larger the width, the larger the
fraction of beliefs in the dead region.

## Why it matters here

`kl_max` is documented as a **numerical safety net** (it sits beside `eps`, mapping NaN/+inf → `kl_max`), not a
modeling hyperparameter. The default `kl_max=100` was generous at the early K=20 configuration (5 nats/coord of
headroom) but becomes the *routine operating point* at K=160 (0.625 nats/coord), where the trained per-coordinate rate
(~0.79) exceeds it. Sitting at the safety-net clamp for the bulk of training is a misuse of the clamp regardless of
which term it bites — and it bites the **full-K self-couplings first**: $\mathrm{KL}(q_i\|p_i)$ (the [[Renyi divergence|self-coupling]])
and the hyper-prior $\mathrm{KL}(s_i\|r)$. This is the concrete mechanism behind the program's **width-scaling
difficulty**: regularizers that should strengthen with width instead switch off.

## Details

**Gradient death, faithfully reproduced by the kernel.** The analytic "filtering" belief-gradient kernel mirrors the
hard clamp exactly: it masks the self-coupling gradient wherever the raw divergence saturates,
`self_mask = ((raw_self > 0) & (raw_self < kl_max))`, so the kernel stays bit-equal to the autograd oracle (which
differentiates *through* the clamp, derivative 0 above the ceiling). A term whose only gradient route saturates is
therefore inert — and if a *learnable* prior/centroid (e.g. `r`) appears only inside that term, it is **gradient-frozen**
while saturated.

**What still moves.** Only the *self* term is masked; pairwise coupling terms carry their own (separately masked) energy
gradient, so beliefs can keep training through coupling and the likelihood even while a self-coupling is pinned. Escape
from saturation is then driven indirectly — weight decay and the likelihood pulling means together until a belief drops
back under the ceiling — not by the saturated regularizer itself. The regularizer can only act once it is already inside
the basin it was supposed to create.

**Per-head energies saturate later.** Pairwise belief/gamma energies are computed per irrep block over
$d_\text{head}=K/H$, not full K, so they cross the same ceiling only at $K\approx H\cdot k_\text{max}/r$ (≈455–600 at
H=4) — well above where the full-K self-couplings die. Raising H with K holds $d_\text{head}$ fixed and they never
saturate.

**Remedies.**
1. **Scale the clamp with K** (recommended): set $k_\text{max}=cK$ ($c\sim3\text{–}8$) so it binds only on genuine
   blowups. Provably theory-neutral — `safe_kl_clamp` is the identity below the ceiling, so the free energy,
   $\beta^\*=\mathrm{softmax}(B-E/\tau)$, $\gamma^\*$, and every gradient are independent of `kl_max` throughout their
   intended domain; raising a non-binding ceiling cannot move a stationary point. The softmax temperature
   $\tau=\kappa\sqrt{d_\text{head}}$ never reads `kl_max`, and un-clamping a saturated key only sharpens attention.
2. **Normalize divergences by $1/K$** (rejected as a drop-in): makes F dimensionless so the clamp never binds, but it
   silently rescales the energy that feeds the softmax, shifting the effective temperature from $\kappa\sqrt{K}$ to
   $\kappa K^{3/2}$ (flattening attention by a factor of K) unless $\tau$ and every $\lambda$ are co-scaled — at which
   point it collapses to "scale the clamp plus a $\lambda$ rescale." Contradicts the manuscript's dimensionless
   $\tau=\kappa\sqrt{K}$ convention.
3. **Soft clamp** (rejected): a smooth saturating map keeps a gradient above threshold but deforms the *value* of every
   energy and so the $\beta^\*/\gamma^\*$ distributions and the $-\tau\log Z$ envelope reduction; no toggle recovers
   exact F (a hard clamp with $k_\text{max}\to\infty$ does), breaking the pure-path doctrine.

> [!note] Editorial: items 1–3 are an engineering/theory analysis grounded in the code and the manuscripts
> ([[participatory-it-from-bit]], [[gl-k-attention]]), not a published external result; the empirical numbers come from
> [[2026-06-21-k160-hyperprior-saturation]].

## In this work

Controlled by the single global `cfg.kl_max` (`vfe3/config.py`), threaded to every divergence consumer — the
self-coupling, the per-head pairwise energy, the hyper-prior $\mathrm{KL}(s\|r)$, and decode. There is no per-block
seam. Applied fix: `config["kl_max"] = 8 * embed_dim` in `train_vfe3.py`, so the safety net auto-tracks width. First
observed in [[2026-06-21-k160-hyperprior-saturation]] (the hyper-prior block pinned at 100 for K=160).

## Sources
- [[2026-06-21-k160-hyperprior-saturation]] — empirical measurement at K=160
- [[participatory-it-from-bit]] · [[gl-k-attention]] — the $\tau=\kappa\sqrt{K}$ convention and the free-energy functional

## See also
- [[Renyi divergence]] · [[Belief coupling]] · [[Natural gradient]] · [[Precision weighting]] · [[VFE Transformer Program]]
