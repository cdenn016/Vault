---
type: run
title: "omega_direct gauge parameterization + learnable det-sign (2026-07-08 buildout)"
aliases:
  - "omega_direct"
  - "learnable det-sign"
  - "metropolis det-sign"
  - "omega-direct-detsign-buildout"
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

# omega_direct gauge parameterization + learnable det-sign (2026-07-08 buildout)

**Kind:** implementation / design note (V3_Transformer, `origin/main` @ `24500e9` for omega_direct+detsign; the deterministic-repro toggle is on branch `feat/deterministic-toggle` @ `8f9717c`). No training metrics — this records a capability buildout plus two source-verified findings, not an empirical run.

## Core contribution

A second way to parameterize the [[GL(K) gauge group]] frame, `gauge_parameterization="omega_direct"`, which stores each token's frame as a **group element** $U_i \in \mathrm{GL}(K)$ (`belief.omega`, sourced from a `omega_embed` table) instead of Lie-algebra coordinates $\phi_i$. Transport becomes the stored cocycle $\Omega_{ij}=U_i U_j^{-1}$ directly, rather than $\exp(\phi_i)\exp(-\phi_j)$. Default `omega_reflection="off"` and `gauge_parameterization="phi"` remain byte-identical; `omega_direct` is an opt-in.

The buildout spanned three phases plus a learnable-reflection extension:

- **Phases 1-2** — `omega_direct` across all seven omega-eligible groups (`glk`, `block_glk`, `tied_block_glk`, `so_k`, `so_n`, `sp`, `sp_n`), a group-manifold natural-gradient retraction (`lie_exp`/`cayley`) for the stored element, and compact block storage.
- **Phase 3** — threaded the stored frame through the whole gamma / model-coupling (s) channel so the s-channel transports by $U_iU_j^{-1}$ instead of the $\exp(\phi)$ cocycle (forward gamma loss, the `gamma_as_beta_prior` fold, and the `s_e_step` E-step `_refine_s`), then removed the config gate that had blocked `omega_direct` + an active gamma channel. Unblocks the `omega_direct + lambda_gamma>0 + s_e_step + gamma_as_beta_prior` training config.
- **Learnable det-sign** (`omega_reflection="metropolis"`) — a $\Delta F$-gated Metropolis flip that lets a token's discrete orientation ($\det$ sign) be *learned* during training (see [[GL(K) gauge group]] §discrete component). The straight-through-gradient (STE) alternative is deferred behind a `# TODO(STE)` marker.

## Why the discrete component needs its own mechanism

$\mathrm{GL}(K)$ (and $O(K)$) has two disconnected sheets, $\det U \gtrless 0$, separated by the singular set $\det U = 0$. The $\exp(\phi)$ parameterization can only ever reach the identity component $\mathrm{GL}^+(K)$ ($\det\exp = e^{\operatorname{tr}} > 0$), so the $\det<0$ sheet is unreachable by the continuous frame parameterization — exactly the gap noted on [[GL(K) gauge group]].

The two sheets are walled off not merely topologically but by a **free-energy barrier**: as $\det U \to 0$ the congruence $\Sigma\mapsto U\Sigma U^\top$ collapses a covariance direction, so every $\Sigma^{-1}$ / $\log\det\Sigma$ term in the divergence diverges (clamped to `kl_max`, a flat plateau with vanishing gradient). Continuous VFE descent therefore cannot cross; the frame decomposes as $U = R\,U^0$ with $U^0\in\mathrm{GL}^+(K)$ (continuous, by the retraction) and $R$ a discrete reflection ($\det R=-1$) that must be handled combinatorially. `omega_reflection` offers `"off"` (pure $\det>0$), `"init_seed"` (per-token $\det<0$ fixed at init), and now `"metropolis"` (learned).

## The learnable det-sign as a Metropolis move

`metropolis` is a **coordinate-descent split** on the shared free energy $F$: gradient descent already minimizes $F$ over the continuous $\mathrm{GL}^+(K)$ coordinates; the Metropolis move minimizes the *same* $F$ over the discrete $\pi_0(\mathrm{GL}(K))=\mathbb{Z}/2$ det-sign. Per training step, after the gradient M-step, a single-site sequential sweep over the batch's unique tokens proposes $U_i\to R\,U_i$; since $R$ is an orthogonal involution the proposal is symmetric (plain Metropolis acceptance $\min(1,e^{-\Delta F/T})$, no Hastings ratio); the exact $\Delta F$ is evaluated at **fixed** converged beliefs (a Metropolis-within-Gibbs block move), and the accept draw is seeded for reproducibility. This is the program's **first operationalization of *learning* the discrete gauge component** — the continuous retraction never crosses $\det=0$, so the det-sign changes only through this move.

## Two source-verified findings

> [!note] Finding — gauge-covariance vs frame-USE are distinct certifications. A gauge-*invariance* test (co-transform every prior table by a global $g$, assert decode invariance) certifies **covariance** — that the pipeline adds no gauge-breaking term — but **cannot** distinguish *which* covariant transport is used ($U_iU_j^{-1}$ vs the $\exp(\phi)$ cocycle), because **both are gauge-covariant**. With identity base frames a global $g$ makes the relative transport $\Omega_{ij}=g g^{-1}=I$, so reverting the frame-threading changes nothing the invariance test sees. The frame's actual **USE** must be pinned by direct frame-perturbation tests (vary $U$ at fixed $\phi$, assert the output changes). A capstone "gauge-invariance-with-gamma-on" test initially over-claimed to certify frame-use; it was corrected to an honest covariance-regression guard.

> [!note] Finding — under a diagonal covariance family the det-sign move is near-inert. For `family="gaussian_diagonal"` the reflection $R=\operatorname{diag}(-1,1,\dots)$ leaves the read-off diagonal covariance **exactly invariant**: the transported diagonal covariance is $\sum_l \Omega_{ijkl}^2\,\sigma_{jl}$, which **squares** $\Omega$, so flipping the sign of row/col 0 cancels. The only channel that bites is the sign of component 0 of the transported *mean* (tiny near zero-mean init). Live smoke (K=4, glk, $T=1$): $\Delta F\in[-3\mathrm{e}{-5},2\mathrm{e}{-4}]$, acceptance $\approx 100\%$, det-signs *thrash* every step — a valid MCMC on a flat target that does no useful sheet selection. The move bites only with a **full / off-diagonal covariance family** (where $R$ breaks the congruence invariance) or a **low temperature** / annealing. Guarded by a construction-time `UserWarning`.

## Validation

Built spec → plan → TDD, task-by-task with per-task adversarial review and a final multi-lens whole-branch review including a **live `train()` smoke** (runs finite with gamma off and $\lambda_\gamma=0.5$; det-signs flip across steps; `off` inert). MCMC validity checked from source (symmetric proposal, correct acceptance sign, $e^{-\Delta F/T}$ numerically safe, detailed balance at fixed beliefs). One real defect caught + fixed: `metropolis` under `gauge_parameterization="phi"` used to construct then crash (`belief.omega` is None on the phi path) — now rejected at config, since the reflection is meaningless without a stored $U$ (`phi` only ever represents $\det>0$).

## Relevance to this research

This extends the [[GL(K) gauge group]] structure of the [[VFE Transformer Program]] from the identity component $\mathrm{GL}^+(K)$ (all the $\exp(\phi)$ theory realizes) to the **full group, both orientation components**, and supplies the first mechanism for *learning* the discrete $\pi_0$ gauge coordinate. The gauge-covariance-vs-frame-use distinction is a reusable methodological caution for validating any frame-threading change; the diagonal-family finding says the discrete-orientation degree of freedom only carries information when the belief covariance is full, connecting the det-sign capability to the choice of covariance family ([[Symmetric spaces and the SPD cone]] congruence action).
