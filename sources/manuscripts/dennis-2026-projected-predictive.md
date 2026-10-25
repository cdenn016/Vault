---
type: manuscript
title: "The Projected Predictive Route: Theory and Computational Path"
aliases: ["Projected predictive route note", "Projected Predictive Manuscript"]
authors: ["Robert C. Dennis"]
year: 2026
url: "manuscripts/Attention/projected_predictive.tex"
tags: [cluster/attention, cluster/gauge-theory, cluster/vfe, project/transformer, field/cs-ml, field/mathematics]
created: 2026-09-27
---

# The Projected Predictive Route: Theory and Computational Path

## Source and scope

The live source is [projected_predictive.tex](../../manuscripts/Attention/projected_predictive.tex) (7 pages, compiled PDF beside it), a technical note dated September 2026, drafted by Claude Opus 5.5 at the author's request on 2026-09-27. It walks the `vfe3` computation under `attention_mode="projected_predictive"` from encoding to loss, maps every configuration toggle to its equation, and documents the new opt-in `predictive_covariance="moment_matched"`. It restates results of [[dennis-2026-glk-projected-matrix-links-v2]] for this route; the only new mathematics is the implementation contract of the moment-matched covariance (the formula itself is item (2) of that manuscript's exact-status theorem). It reports no training result with the new option. The local file may change after this dated record.

## Route summary

Token agents carry $q_i=\mathcal N(\mu_i,\Sigma_i)$ and block-diagonal frames $U_i=\exp(X_{x_i})\exp(Y_i)$ (token and positional factors), with reference moments $\xi_i=U_i^{-1}\mu_i$, $C_i=U_i^{-1}\Sigma_iU_i^{-\top}$. Per layer and head: query/key laws $\mathcal N(S_Q\xi_i,S_QC_iS_Q^\top)$ and $\mathcal N(S_K\xi_j,S_KC_jS_K^\top)$; exact Gaussian KL cost (or the noisy-query cost); Gibbs routing $\beta_{ij}^h=\mathrm{softmax}_j(-D_{ij}^h/\tau_h+\log\pi_{ij}^h)$ with $\tau_h=\kappa\sqrt d$ and causal/ALiBi priors; content through the matrix link $L_{ij}^h=U_iO_hT_hU_j^{-1}$; predictive mean $\mu_i^+=r\mu_i+\sum_{h,j}\beta_{ij}^hL_{ij}^h\mu_j$ ($r=1$ under `attention_residual`). Between layers: optional head mixer, CG coupling, mean-only norms, and the block MLP (coordinate GELU, or [[Template routing]]). Decode: linear Gibbs readout of the mean, or prior-bank KL decoding whose exponent contains $\mathrm{Tr}(\Sigma_{p,v}^{-1}\Sigma_i)$. No E-step descent runs; `n_e_steps=1`.

## The covariance

**Passthrough (default, all evaluated runs):** $\Sigma_i^+=\Sigma_i$, so the covariance is the encoded token-type lookup at every depth.

**Moment matched (new, opt-in):** under the predictive kernel $k_i'\mid k,J\sim\mathcal N(rk_i+\sum_hL_{iJ^h}^hk_{J^h},Q_i)$ with independent head labels and independent sources,
$$C_i^{\mathrm{att}}=\widetilde Q_i+r\Big[C_i+\sum_h\beta_{ii}^h(M_hC_i+C_iM_h^\top)\Big]+\sum_j\sum_{h,h'}c_{ij}^{hh'}M_hC_jM_{h'}^\top+\sum_h\Big[\sum_j\beta_{ij}^hn_{ij}^hn_{ij}^{h\top}-\bar n_i^h\bar n_i^{h\top}\Big],$$
$M_h=O_hT_h$, $c^{hh}=\beta^h$, $c^{hh'}=\beta^h\beta^{h'}$, $n_{ij}^h=M_h\xi_j$, reference floor $\widetilde Q_i=\epsilon(\mathrm{Tr}\,C_i/K)I$ (covariant because $\mathrm{Tr}\,C_i$ is frame-invariant), and $\Sigma_i^+=U_iC_i^{\mathrm{att}}U_i^\top$. Properties: $\Sigma_i^+\succeq Q_i\succ0$; passive law $\Sigma_i^+\mapsto g_i\Sigma_i^+g_i^\top$; context dependence through the between-source spread; cross-head terms kept (an earlier 2026-09-23 plan dropped them); no depth monotonicity in general. With the residual on at identity initialization, a self-routing token's covariance quadruples per layer (exact for the kernel; no ceiling applied); with the residual off the trace stays flat. A relative floor $\epsilon C_i$ was tried first and rejected: it compounds as $\epsilon^\ell$ without the residual and lost float32 definiteness in a sweep with rank-one content maps. Diagonal families store the diagonal (the KL(p‖q) moment projection); `gaussian_frame_diagonal` stores the diagonal in its intrinsic value frame.

## Implementation record

VFE_3.0 working copy, 2026-09-27: config `predictive_covariance` ("passthrough" | "moment_matched", projected_predictive only) and `predictive_covariance_floor` (1e-4); `RelationalOperators.predictive_covariance_update`; `relational_predictive_readout(..., return_covariance=True)`; E-step predictive branch assigns both moments under the toggle; config notices, `covariance_frozen_at_encode`, and run-artifact labels updated. `tests/test_predictive_covariance.py` (39 tests) checks the implementation against brute-force enumeration of every head-label tuple in local coordinates (all input/output scopes × residual × compact/dense frames × diagonal/full Σ, float64, 1e-10), the passive law, positive definiteness with zero content maps, gradcheck, validation and serialization, and forward/backward for every admissible family and decoder. A float32 twelve-layer recursion with rank-one content maps stays positive definite (the relative floor fails at layer two). The 39 existing projected-route test files pass unchanged. A four-agent configuration sweep (about 6,000 tiny-model combinations over routing, geometry, block seams, decoders, training loop, checkpoints, diagnostics, reporting, sampling, CPU AMP) found no configuration that runs under passthrough and fails under moment matching after the floor change; CPU overhead about 1.5x at K=64.

## Open

No training run with `moment_matched`; its effect on loss, on the calibration gate (CV > 0.10 with positive ρ(tr Σ, CE)), on the prior-bank decoder, and on template routing is untested.

## Related

[[Projected predictive attention]], [[GL(K) gauge-equivariant attention]], [[Template routing]], [[VFE Transformer Program]], [[dennis-2026-glk-projected-matrix-links-v2]], [[dennis-2026-template-routing]]
