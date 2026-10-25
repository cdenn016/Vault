---
type: method
title: "Projected predictive attention"
aliases:
  - projected_predictive
  - Projected predictive route
  - Predictive content attention
tags:
  - cluster/attention
  - cluster/gauge-theory
  - project/transformer
status: draft
created: 2026-09-27
updated: 2026-10-25
---

# Projected predictive attention

## Content-link charts, October 4, 2026

The stored content maps are now applied through one of three charts, selected by `content_link_chart` and derived in Section 3 of [[dennis-2026-glk-lie-algebra-links-v2]]. The layer uses an effective receiving map $\widetilde O_h$ in place of $O_h$: $\widetilde O=O$ (affine, which is how the stored maps were applied before the selector existed), $\widetilde O=T^{-1}+O$ (first order: a head-routed flat transport plus the value path) or $\widetilde O=e^{OT}T^{-1}$ (exponential: the resummed message of the shared exponential link $\exp(OT)$). Every statement on this page that involves the content maps holds with $M_h=\widetilde O_hT_h$, including the moment-matched covariance. The three charts represent the same tiled mean maps up to the real-logarithm domain. The same derivation shows that with tiled heads complement-preserving aggregation leaves no residual, so the $r=1$ residual of this route has no counterpart in the exponential construction.

## Unified implementation scope, October 3, 2026

[[dennis-2026-attention-unified]] connects this route to the author's primary Option A exponential-link construction while preserving the distinction between a group link and a weighted multi-source message. The inspected launcher now selects `moment_matched` with `gaussian_diagonal`; passthrough statements below describe the earlier evaluated configuration or the default field. The exact covariance belongs to the declared independent-source/independent-label kernel. Diagonal projection, output floors, and coordinate nonlinear blocks require their stated approximation and symmetry qualifications. The current routing score includes the configured smooth KL cap before division by `kappa_beta * sqrt(d)`.

The attention route of the [[VFE Transformer Program|vfe3 transformer]] selected by `attention_mode="projected_predictive"`. It is the route of [[GL(K) gauge-equivariant attention]] in which a layer replaces the belief mean by a predictive readout instead of taking a gradient step. The full walk-through, with every toggle mapped to its equation, is [[dennis-2026-projected-predictive]]; the general theory is [[dennis-2026-glk-lie-algebra-links-v2]] (earlier record: [[dennis-2026-glk-projected-matrix-links-v2]]).

## The layer

Each token agent has a Gaussian state and an invertible frame $U_i$; everything is computed from reference moments $\xi_i=U_i^{-1}\mu_i$, $C_i=U_i^{-1}\Sigma_iU_i^{-\top}$, so costs are invariant and messages covariant under passive frame changes. Per head, learned comparison maps $S_Q,S_K$ push the states to query and key Gaussians; the exact Gaussian KL between them is the routing cost, and Gibbs weights $\beta_{ij}^h=\mathrm{softmax}_j(-D_{ij}^h/\tau_h+\log\pi_{ij}^h)$ select sources ([[Softmax]], [[Attention Mechanism]]). The weights are an exact posterior under a declared binary compatibility record. Content travels through the matrix link $L_{ij}^h=U_iO_hT_hU_j^{-1}$, and the new mean is $r\mu_i+\sum_{h,j}\beta_{ij}^hL_{ij}^h\mu_j$, with $r=1$ under `attention_residual` (numerically inert after training in the reported run). The message is linear in the states; the only state nonlinearity inside the layer is the dependence of $\beta$ on the states. The block MLP after attention supplies the rest (see [[Template routing]] for a derived replacement).

## Covariance: passthrough versus moment matched

By default the layer keeps the incoming covariance, so $\Sigma$ is the encoded token-type lookup at every depth and cannot register context. The opt-in `predictive_covariance="moment_matched"` (2026-09-27) replaces it by the exact moment-matched covariance of the same predictive kernel whose mean the layer computes: pushed source covariances $M_hC_jM_{h'}^\top$ with cross-head weights, the between-source spread, the residual persistence and self-edge terms, and a covariant reference floor $\epsilon(\mathrm{Tr}\,C_i/K)I$. The result is positive definite, obeys the passive law, and is context dependent. Diagonal families store its diagonal, the KL moment projection. With `attention_residual=True` at identity initialization a self-routing token's covariance quadruples per layer (the exact kernel; no ceiling), while with the residual off it stays flat. It feeds the next layer's routing costs, the prior-bank decoder (through $\mathrm{Tr}(\Sigma_{p,v}^{-1}\Sigma_i)$), and template routing.

> [!note] Editorial: Moment matching makes the covariance consistent with the declared kernel. It does not make the whole stack a single free-energy minimization, and the collapse of the layer's mixture output to one Gaussian is a declared approximation. Whether a context-dependent covariance improves loss is untested; the matched comparison against passthrough with several seeds is the deciding experiment.

## The gradient counterpart, October 2026

Since the retirement of transported attention, this route and [[Projected gradient attention]] are the only executable attention modes (`VFE_3.0/docs/2026-10-02.md`). Both route by the same comparison KL and use the same matrix links; they differ in what the layer does with the routed content. The predictive route adds the routed messages to the mean (with residual $r$), while the gradient route minimizes a receiver energy with the routing frozen. Under the default channel-likelihood receiver that minimizer is a tempered Gaussian posterior that fuses messages by their channel precision, and [[dennis-2026-projected-gradient]] proves it reduces to the residual-free head sum of this route when heads are orthonormal and disjoint, the channel covariance is source independent, and the prior precision vanishes. Both routes route by the comparison divergence alone, which that note reads as exact inference in a declared cut model, so freezing $\beta$ is not an approximation on either route. The predictive route keeps its moment-matched covariance; the gradient route's posterior covariance $\alpha\Lambda^{-1}$ omits the between-source spread. Since PR #37 the moment-matched spread always centers source means on token 0, which changes only rounding. Predictive-only knobs (`predictive_covariance`, `attention_residual`, `predictive_covariance_floor`) are marked inactive on the gradient route.

## Residual: complement only, October 2026

[[dennis-2026-link-origin]] derives what a residual should be if the layer is the exponential link with only sent content crossing between agents. The receiver carries the complement of the written subspace, so the flat term is a residual on the unsent directions only, $U_i(I-P)U_i^{-1}\mu_i$ with $P$ the projector onto $\operatorname{im}O$ along $\ker T$, and it vanishes when the heads tile the fiber ($Hd=K$), leaving the residual-free head sum with receiving maps $OE_{:,h}$, $E=e^{TO}(TO)^{-1}$. The $r=1$ additive residual of this route is therefore not implied by that construction, and its justification in the note is optimization ([[Residual Connections]]), not inference. A projected residual stream needs $Hd<K$ and has not been trained here. The Gaussian-fusion residual of [[Projected gradient attention]] is the finite-precision counterpart. Agent-drafted note, small-dimension float64 checks, no training.

## Related

[[Projected gradient attention]], [[GL(K) gauge-equivariant attention]], [[Template routing]], [[Precision weighting]], [[Multi-head attention]], [[VFE Transformer Program]]

## Sources

[[dennis-2026-glk-lie-algebra-links-v2]], [[dennis-2026-link-origin]], [[dennis-2026-projected-predictive]], [[dennis-2026-projected-gradient]], [[dennis-2026-glk-projected-matrix-links-v2]], [[dennis-2026-template-routing]], [[vaswani-2017-attention]], [[vilnis-2015-gaussian-embeddings]]
