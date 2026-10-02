---
type: run
title: "VFE_3.0 projected-route consolidation, October 1 to 2, 2026 (implementation record)"
aliases: ["vfe3 projected route consolidation 2026-10-02", "VFE_3.0 PRs 34 to 39"]
tags: [cluster/attention, cluster/gauge-theory, cluster/vfe, project/transformer, field/cs-ml]
year: 2026
created: 2026-10-02
---

# VFE_3.0 projected-route consolidation (implementation record)

> [!info] Scope
> An implementation record, not a training result. It summarizes `VFE_3.0/docs/2026-10-02.md` and the merges of GitHub `cdenn016/VFE_3.0` PR #34 (`f369760`), #35 (`2adaafc`), #36 (`ab4293d`), #37 (`842302d`), #38 (`2a83983`) and #39 (`f35c573`), all on 2026-10-02. The motivating audit is `VFE_3.0/docs/audits/projected-gradient-pr30-32-audit-2026-10-01.md`. All verification was on CPU with tiny models and one thread; no GPU workload or production training ran.

## Motivating audit (October 1)

The audit of PR #30 (`attention_mode="projected_gradient"`), PR #31 and PR #32 (retirement of transported and `projected_conditional` attention) was run by nine Opus investigators plus a completeness critic, with no adjudication. It found the PR #30 kernel correct against its specification but its explicit Fisher mean step unstable at launcher rates: at initialization ($\sigma=15$, receiving noise 1, $H=2$) stable only for `e_q_mu_lr` below about 0.12, at covariance stationarity below $2/c=0.667$, and at 0.9 overshooting the frozen minimizer about 14-fold with sign reversal (F1). Isotropic receiving noise made each head pin the complement of its output range to zero, keeping about 6.5% of the incoming mean (F2). It also reported a policy conflict: after PR #32 no configuration executes the canonical free energy or its gauge-KL routing $\beta=\mathrm{softmax}(\log\pi-\mathrm{KL}(q_i\Vert\Omega_{ij}q_j)/\tau)$, and `projected_gradient` descends a frozen-router energy without an attention-entropy block. The theory answering F1 and F2 is [[dennis-2026-projected-gradient]].

## What changed

**PR #34, projected_gradient receiver laws and updates, plus remaining audit fixes.** New fields `relational_receiver_law` (`"channel_likelihood"` default, or `"ambient_alignment"`, the PR #30 energy), `relational_receiver_update` (`"closed_form"` default, or `"euler"`), and `relational_receiver_damping` $\rho\in(0,1]$. The closed form applies $J^+=(1-\rho)\Sigma^{-1}+\rho\Lambda/c$, $h^+=(1-\rho)\Sigma^{-1}\mu+\rho\eta/c$: the exact Fisher flow for `gaussian_full`, the restricted minimizer at $\rho=1$ for the diagonal family. Under the channel law $c=\alpha$, so `lambda_alpha > 0` is required. Serialized configs without the fields reload as ambient/euler. Remaining audit items on both projected routes were fixed (validation of `n_e_steps=0`, separated mean and covariance cost deltas and a distance-to-minimizer ratio, hardened Cholesky with float64 retry, precision and diagnostic contract fixes, resume provenance).

**PR #35, configuration simplification.** After PR #32 only `projected_predictive` and `projected_gradient` remain. Removed fields include `e_step_update`/`mm_damping` (mm_exact), `mu_trust_mode`, `divergence_family`, `renyi_order`, `include_attention_entropy`, `gradient_mode`, `oracle_unroll_grad`, `e_phi_lr`, `transport_mode`, `cross_couplings` and others. Retired: the `gaussian_diagonal_exact` family (renamed `gaussian_diagonal` on load), the `gaussian_frame_diagonal` family, the canonical-content encoders, the dense decode modes, and the `glk`, `tied_block_glk`, `so_k`, `sp_n` and `sp` gauge groups. The free-energy, mm_exact, hand-kernel gradient, oracle and transported scorer code was deleted. The gauge-equivariance report figure now tests the projected score: routing score, $\beta$, and the predictive readout or receiver force, update and energy under a random passive frame action, with residuals about $10^{-13}$ in float64. `gauge_group='so_n'` was reconnected to both projected routes, with the constraint of `n_heads` equal irrep blocks, one per head; so_n equivariance residuals about $1.5\times10^{-13}$ and a finite-difference check on $\varphi$ to about $10^{-10}$.

**PR #36, decode temperature, jitter and transport chart.** `decode_temperature_learned` and `safe_cholesky_jitter_mode` were retired (the decode log-scale is always frozen; the Cholesky ridge is always relative, $\epsilon10^t\max(1,|\text{diag mean}|)$). `transport_chart_max_norm` (default 20.0, the old clamp radius) became one fail-closed domain radius: the transport exponential raises on any frame with $\|M\|_F$ above it instead of rescaling it through the former surrogate clamp, and the clamp diagnostics were deleted. `exp_fp64_norm_threshold` was removed, and the condition-certified float64 rebuild of the frame pair ($\max\kappa_F(U)\epsilon_{32}\le10^{-4}$, otherwise rebuild in float64) is now unconditional.

**PR #37, hardcoded numerical policies.** `decode_ce_stable_reduction` (centered chunked CE always), `decode_ranking_refinement` (candidate refinement always), `min_lr` (floor is `min_lr_frac` times base), and `predictive_covariance_centering` were removed. The moment-matched covariance now always shifts source means by token 0's before forming the between-source spread, which is exact because every $\beta$ row sums to one and token 0 is in every causal support.

**PR #38, profiled state-dependent self-coupling on projected_gradient.** `lambda_alpha_mode` in `{"state_dependent","state_dependent_per_coord"}` is accepted on the gradient route, implementing the profiled section of [[dennis-2026-projected-gradient]]: $\alpha^\star=c_0/(b_0+D)$ recomputed per E-step iteration against the exact unclamped KL, envelope force under `euler`, MM step under `closed_form`; per-coordinate on the diagonal family only. $\alpha^\star$ keeps its autograd graph. Predictive-only knobs (`predictive_covariance`, `attention_residual`, `predictive_covariance_floor`) are now accepted and marked inactive on the gradient route; `noisy_query` routing and `block_coordinates="reference"` stay restricted.

**PR #39, loader fix.** A saved `transport_chart_max_norm=None` loads as the literal 20.0.

## Current state after October 2

Attention routes: `projected_predictive` and `projected_gradient` only. Structure groups: `block_glk` and `so_n` (one equal irrep block per head). Belief families: `gaussian_diagonal` and `gaussian_full`. Checkpoint parameter names are unchanged throughout. No SU(N), complex, or non-compact group beyond `block_glk` is implemented; per the user's plan SU(N) is deferred.

> [!note] Editorial: on the "pure path". The audit's policy conflict stands as reported: the canonical single-functional free energy with gauge-KL routing is no longer executable, and both retained routes use learned comparison maps. The closest pure objects now are the declared models of [[dennis-2026-projected-gradient]]: the channel-likelihood receiver is an exact tempered Gaussian posterior under cut routing, and the profiled self-coupling closed form is an MM descent of a stated energy. These are exact for declared models, not a reinstatement of the canonical functional.

## Verification as reported

PR #34: 27 new receiver tests (channel kernel against a literal expected-likelihood sum, entropy multiplicity, stationarity, monotone damped descent, closed form against RK4 integration of the Fisher flow, predictive limit, prior retention); a launcher-derived tiny bf16 step measured a distance-to-minimizer ratio of $1.5\times10^{-7}$ for channel/closed_form versus 3.0 for ambient/euler. The publication-tree suite recorded 3,369 cases with 0 failures. PR #35: on seven tiny configs, loss, parameter names and parameter and gradient sums identical to `f369760`; final suite 2,946 cases, 0 failures (the drop is deleted tests of deleted code). PR #36: on ten tiny configs, loss and every gradient `torch.equal` to the pre-change tree; suite 2,949 cases, 0 failures. PR #37: four tiny configs `torch.equal` on loss and all gradients against the old settings (one comparison against the old default False differed by at most $4.7\times10^{-10}$ in a gradient); suite rerun after fixes. PR #38: constant $\alpha$ bitwise unchanged (304 tensors `torch.equal` against `842302d`); 32 new tests including force versus central differences of the profiled energy to $1.6\times10^{-9}$, MM monotonicity, full-family damped descent, and the diagonal damping counterexample; suite 2,979 cases, 0 failures.

## Open

No GPU or training run of the new projected_gradient receiver (channel likelihood, closed form, or profiled $\alpha$) exists, so its loss relative to `projected_predictive` is unknown. `so_n` supports only equal irrep blocks matched to heads; unequal irrep towers would need heads decoupled from irrep blocks. SU(N) is not implemented. Damped diagonal closed-form steps have no descent guarantee (explicit counterexample $1.500\to2.503$), and the full-family per-coordinate closed form is derived but not implemented. Left as reported in the record: batch-global float64 escalation still breaks bitwise causality; historical configs reload with live defaults; cross-mode resume warns rather than refuses.

## Relevance to this research

This record fixes which constructions of [[VFE Transformer Program|the vfe3 program]] are executable as of October 2, 2026, and retires the transported attention that much of the historical wiki describes. See [[Projected gradient attention]], [[Projected predictive attention]], [[GL(K) gauge-equivariant attention]].
