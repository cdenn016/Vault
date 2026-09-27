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
updated: 2026-09-27
---

# Projected predictive attention

The attention route of the [[VFE Transformer Program|vfe3 transformer]] selected by `attention_mode="projected_predictive"`, behind the current best results (validation perplexity about 53 at K=64, four layers, WikiText-103). It is the route of [[GL(K) gauge-equivariant attention]] in which a layer replaces the belief mean by a predictive readout instead of taking a gradient step. The full walk-through, with every toggle mapped to its equation, is [[dennis-2026-projected-predictive]]; the general theory is [[dennis-2026-glk-projected-matrix-links-v2]].

## The layer

Each token agent has a Gaussian state and an invertible frame $U_i$; everything is computed from reference moments $\xi_i=U_i^{-1}\mu_i$, $C_i=U_i^{-1}\Sigma_iU_i^{-\top}$, so costs are invariant and messages covariant under passive frame changes. Per head, learned comparison maps $S_Q,S_K$ push the states to query and key Gaussians; the exact Gaussian KL between them is the routing cost, and Gibbs weights $\beta_{ij}^h=\mathrm{softmax}_j(-D_{ij}^h/\tau_h+\log\pi_{ij}^h)$ select sources ([[Softmax]], [[Attention Mechanism]]). The weights are an exact posterior under a declared binary compatibility record. Content travels through the matrix link $L_{ij}^h=U_iO_hT_hU_j^{-1}$, and the new mean is $r\mu_i+\sum_{h,j}\beta_{ij}^hL_{ij}^h\mu_j$, with $r=1$ under `attention_residual` (numerically inert after training in the reported run). The message is linear in the states; the only state nonlinearity inside the layer is the dependence of $\beta$ on the states. The block MLP after attention supplies the rest (see [[Template routing]] for a derived replacement).

## Covariance: passthrough versus moment matched

By default the layer keeps the incoming covariance, so $\Sigma$ is the encoded token-type lookup at every depth and cannot register context: the saved probes of the K=64 runs record CV(tr Σ) of 0.02 to 0.03 and label it input-token variance. The opt-in `predictive_covariance="moment_matched"` (2026-09-27) replaces it by the exact moment-matched covariance of the same predictive kernel whose mean the layer computes: pushed source covariances $M_hC_jM_{h'}^\top$ with cross-head weights, the between-source spread, the residual persistence and self-edge terms, and a covariant reference floor $\epsilon(\mathrm{Tr}\,C_i/K)I$. The result is positive definite, obeys the passive law, and is context dependent. Diagonal families store its diagonal, the KL moment projection. With `attention_residual=True` at identity initialization a self-routing token's covariance quadruples per layer (the exact kernel; no ceiling), while with the residual off it stays flat. It feeds the next layer's routing costs, the prior-bank decoder (through $\mathrm{Tr}(\Sigma_{p,v}^{-1}\Sigma_i)$), and template routing.

> [!note] Editorial: Moment matching makes the covariance consistent with the declared kernel. It does not make the whole stack a single free-energy minimization, and the collapse of the layer's mixture output to one Gaussian is a declared approximation. Whether a context-dependent covariance improves loss is untested; the matched comparison against passthrough with several seeds is the deciding experiment.

## Related

[[GL(K) gauge-equivariant attention]], [[Template routing]], [[Precision weighting]], [[Multi-head attention]], [[VFE Transformer Program]]

## Sources

[[dennis-2026-projected-predictive]], [[dennis-2026-glk-projected-matrix-links-v2]], [[dennis-2026-template-routing]], [[vaswani-2017-attention]], [[vilnis-2015-gaussian-embeddings]]
