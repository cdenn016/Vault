---
type: run
title: "Learnable reflection on the phi path — R.exp(phi) (2026-07-08 buildout)"
aliases:
  - "phi_reflection"
  - "R exp(phi) reflection"
  - "phi-path learnable reflection"
  - "phi-reflection-buildout"
tags:
  - cluster/gauge-theory
  - cluster/spd-geometry
  - project/transformer
  - field/cs-ml
  - field/mathematics
  - field/physics
created: 2026-07-08
updated: 2026-07-08
---

# Learnable reflection on the phi path — R.exp(phi) (2026-07-08 buildout)

**Kind:** implementation / design note (V3_Transformer, `origin/main` @ `7ffb68e`). No training metrics. Companion to [[2026-07-08-omega-direct-detsign-buildout]] — the same learnable discrete orientation, but for the DEFAULT phi parameterization instead of the stored-element `omega_direct` one.

## Core contribution

A cheap second route to the `det<0` orientation component of the [[GL(K) gauge group]], on the default `phi` parameterization. Instead of storing the frame as a group element (`omega_direct`), keep `exp(φ)` for the continuous part and **prepend a learnable per-token reflection**:

$$ g_i = R_i\,\exp(\phi_i), \qquad \det g_i = \det(R_i)\,e^{\operatorname{tr}\phi_i} = -\,e^{\operatorname{tr}\phi_i} < 0 \ \text{ when } R_i \text{ is a reflection}. $$

`det exp(φ) = e^{tr φ} > 0` is always positive — that is exactly why `exp(φ)` alone is confined to `GL^+(K)`. The sign flip comes entirely from the prefactor `R_i` (`det R = -1`), realizing the coset decomposition `GL(K) = {I, R}·GL^+(K)`: `R` picks the orientation sheet, `exp(φ)` moves within it. Config surface `phi_reflection = "off" | "init_seed" | "metropolis"`; default `"off"` is byte-identical.

`R_i` is a single per-token sign bit stored as a `(V,)` buffer (NOT a learned parameter — a non-differentiable discrete state), learned by the SAME ΔF-gated Metropolis flip as the `omega_direct` det-sign. Transport stays flat: `Ω_{ij} = g_i g_j^{-1} = R_i\exp(φ_i)\exp(-φ_j)R_j`, and the cocycle `Ω_{ij}Ω_{jk}Ω_{ki} = I` holds for any `g` (`R` is an orthogonal involution). Mechanically the reflection folds into the transport as `Ω_{ij} → R_i Ω_{ij} R_j` — negate row 0 of the query factor by `s_i`, column 0 of the key factor by `s_j` — group-agnostic over the eligible groups (`glk`, `block_glk`, `so_k`). Threaded through every channel (belief E-step, gamma / model-coupling s-channel, decode, and the free-energy evaluation the Metropolis move scores against).

## Reach: two routes to det<0, and what each buys

The det<0 component is now reachable **two** ways (see [[GL(K) gauge group]] §"Reaching the other orientation"):

- **`omega_direct` (store the element `U`)** — reaches the FULL `GL(K)`, including the non-exp interior of `GL^+(K)` (matrices with odd-multiplicity negative real eigenvalues, which `exp` cannot produce). Costs a `K×K` element per token.
- **`R·exp(φ)` (this note)** — reaches `R·image(exp)`, i.e. the two sheets' exp-images. It MISSES the non-exp interior (the honest theoretical difference), but is far lighter: `n_gen` params + **1 sign bit** per token, and it reuses the mature φ machinery (BCH composition, Killing-form preconditioning, positional-φ). It is the more elegant home for a learnable orientation *bit* when the non-exp interior is not needed.

## Findings carried over + one usability fact

- The **gauge-covariance vs frame-use** distinction ([[2026-07-08-omega-direct-detsign-buildout]]) applies identically: a gauge-invariance test certifies covariance, not which covariant transport is used; frame-use is pinned by direct frame-perturbation / exact-ΔF tests. The discrete `±1` sign additionally has NO continuous `g`-action, so it cannot be co-transformed at all — a gauge-invariance test over it is empirically inert (honestly documented).
- The **diagonal-family near-inertness** also carries over: under `family="gaussian_diagonal"` the reflection leaves the (squared) diagonal covariance invariant, so ΔF is mean-only (~1e-3) and the sign random-walks at ~100% acceptance. It bites the covariance only under a full family. Usability fact (verified live): `s_e_step=True` rejects `gaussian_full` at config, so a meaningful reflection run is **`gaussian_full` + `s_e_step=False`** (gamma via `lambda_gamma` / `gamma_as_beta_prior` is still available).
- The buildout **incidentally fixed a latent `omega_direct` bug**: `block.py`'s post-E-step transforms (`head_mixer` / `cg_coupling` / `block_norm`) reconstructed the belief with a bare constructor that dropped the stored frame (`.omega` and now `.reflection`) for layers past the first when those toggles were active with `n_layers>1`; switched to `_replace`, which preserves the frame.

## Validation

Spec → plan → 5 TDD tasks, per-task adversarial review, plus a 2-lens whole-branch review with a **live `train()` smoke** (8 steps finite, loss monotone; `reflection_sign` flips across steps; `off` inert). MCMC validity checked from source (symmetric involution proposal, correct acceptance, ΔF genuinely reflects, `omega_direct` move byte-identical). The fold verified `Ω → R_i Ω R_j` bit-identical on `glk` / `block_glk` / `so_k`; the Metropolis exact-ΔF anchor bit-identical. STE variant deferred (`# TODO(STE)`).

## Relevance to this research

Completes the story on [[GL(K) gauge group]]: the orientation-reversing component that `exp(φ)` structurally cannot reach is now available on BOTH the stored-element path (`omega_direct`, full group) and the default φ path (`R·exp(φ)`, cheap, two exp-image sheets), each learnable. For the [[VFE Transformer Program]] this makes discrete-orientation learning a default-path capability rather than an `omega_direct`-only one, at the cost of one bit per token.
