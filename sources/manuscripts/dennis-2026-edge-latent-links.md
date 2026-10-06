---
type: manuscript
title: "Edge-Dependent and Latent Content Links: Theory and Implementation"
aliases: ["Edge and latent links note October 2026", "Edge-dependent content links", "Latent receiver factors"]
authors: ["Robert C. Dennis"]
year: 2026
url: "manuscripts/Attention/edge_latent_links.tex"
tags: [cluster/attention, cluster/gauge-theory, cluster/vfe, project/transformer, field/mathematics, field/cs-ml, field/statistics]
created: 2026-10-06
---

# Edge-Dependent and Latent Content Links: Theory and Implementation

## Source and scope

The live source is [edge_latent_links.tex](../../manuscripts/Attention/edge_latent_links.tex), a standalone 13-page working note written on October 6, 2026 at the author's request, as the theory and method record for the edge-dependent and latent content links implemented in `vfe3` on October 5 (VFE_3.0 PR #50, merge `30090ca`). It refers to the main manuscript ([[dennis-2026-glk-attention-v2-rework-2026-10-05]]) and its supplement by theorem and equation numbers through `xr-hyper` cross-references, not by citation, so the note cites no work by the author; compiling it needs the `.aux` files of those two documents. At this ingest the `.tex` had SHA-256 `3546c91e6718598b8127be32ee9653e764deec446024ea8868c68bc1ac1c3e8c` (48,213 bytes) and the PDF `4e641ee76c7498b966a042fef3da90e057a62c95ade743e5e3bd4f7bf839a30a`. It was drafted by Claude Opus 5.5 with no cross-model review of the note itself; the implementation it describes was checked by independent brute-force reference tests. Two bibliography entries were added for it, `Kim2018SemiAmortized` and `OrtegaRheinboldt1970`, entered from memory and not checked against the publishers.

## What the note states

The shared reference link $e^{L}$, $L=OT$, is replaced by $G_{ij}=g_ie^{L}E_{ij}$ with a rank-$r$ edge factor $E_{ij}=I+A_i\Phi_{ij}B_j^\top$ whose factors are linear maps of the RMS-normalized reference state $\hat x=\xi/(K^{-1}\|\xi\|^2+10^{-12})^{1/2}$. In the curved mode (`lowrank`) $\Phi_{ij}=\varphi_1(B_j^\top A_i)$, so $E_{ij}=\exp(A_iB_j^\top)$ by the low-rank exponential identity and $G_{ij}\in\mathrm{GL}^+(K)$. In the pure-gauge control (`pure_gauge`) a shared basis $A$ gives $g_i=\exp(AB_i^\top)$ and $\Phi_{ij}=-\varphi_1(-B_j^\top A)$, so $G_{ij}=g_ie^{L}g_j^{-1}$ and every triangle holonomy is conjugate to $e^{L}$; in the curved mode the holonomy trace changes at first order in $B$, so classes differ between triangles for generic factors. The control is not a frame change (the head projectors stay in the original frame) and is not parameter-matched ($K^2r+Kr$ against $2K^2r$ per layer). With $W_B=0$ at initialization both modes equal the exponential chart exactly.

The message factors as $\tilde m_i=g_i\widetilde O(z_i+TA_iy_i)$ with $y_i=\sum_j\Phi_{ij}c_{ij}$, needing only $r\times r$ matrix functions per edge. The moment-matched covariance is the predictive-kernel covariance of the main manuscript with head maps $G_{ij}\Pi_h$, evaluated through rank-$r$ corrections $\hat A_i\hat X_i^\top+\hat X_i\hat A_i^\top+\hat A_iY_i\hat A_i^\top$; the common-shift trick of the existing code fails with edge links, so the sender coordinates must be formed from unshifted values. Gauge covariance and causality hold, the latter in floating point only because the $\varphi_1$ argument is zeroed on masked pairs. A remark states that at fixed routing the edge message stays positively homogeneous of degree one under common scaling of the states, so its nonlinearity is directional, multiplicative, rank $r$ and cross-token, not a replacement for the position-wise MLP.

For the latent extension the receiver factor $A_i$ gets the prior $\mathcal N(A_i^0,\sigma_L^2I)$ around its amortized value; only the receiver factor can be inferred causally, since a sender factor enters every later receiver. Profiling out the receiver's next-layer state against one transition (a filtering approximation, not the full supplement free energy) reduces the transport energy to $\operatorname{tr}V_i/(2c_i)$, the floor-free predictive covariance trace with $Q_i=c_iI$, $c_i=\operatorname{tr}C_i/K$ (a modeling choice). Its gradient is the supplement's link current pulled back through the factorization. The stationarity condition is the fixed point $A=A_i^0-\sigma_L^2\nabla[\mathcal E_i+\lambda_W\mathcal W_i]$, whose unit step is the natural-gradient step in the prior's Fisher metric; the damped iteration converges locally when $0<\rho(1+\sigma_L^2\lambda_k)<2$ for every Hessian eigenvalue and is repelled when some value leaves $[0,2]$, which gives $\sigma_L^2\lambda_{\max}<1$ for the undamped step. The inference is inactive while $B=0$. In the depth-loop prior $W_{ijk}^\ell$ the upper layer's shared generator cancels, the exponential chart is loop-flat, and to first order $W-I=e^{-L_\ell}A_i^{\ell+1}(B_j^{\ell+1}-B_k^{\ell+1})^\top e^{L_\ell}+(A_j^\ell-A_k^\ell)B_k^{\ell\top}$, a discrete field strength of the factors. As $\sigma_L\to0$ the model returns to the amortized curved mode. A table compares the construction with the per-edge latent generators of the supplement (Section S6, [[dennis-2026-dynamic-links]]).

## Evidence as recorded

The note restates, with the configuration keys and function names of `vfe3/model/edge_links.py`, the four float64 CPU test files at $K\le6$, $N\le4$ (68, 118, 44 and 85 tests, two of them against independent brute-force references) and the CPU costs from `VFE_3.0/docs/2026-10-05.md`: one readout layer at $K=192$, $N=256$, batch 1 takes 0.42/1.35 s (no gradient / forward and backward) for the exponential chart, 0.83/2.74 s curved, 0.54/1.83 s pure gauge and 1.95/6.76 s latent at $T=1$; $\varphi_1$ forward and backward per thousand edges takes about 11.6, 42, 193 and 961 ms at $r=4,8,16,32$; the latent readouts at batch 8 over six layers keep about 62 GB of saved tensors (37 GB with the covariance checkpoint). No training result for the edge or latent arms is reported; the small-size tests validate the implementation and do not set direction.

## Open problems

No step-size safeguard in the latent iteration (unit steps diverged in tiny cases when $\sigma_L^2$ times the curvature exceeded about one); latent inference only for the curved mode; the filtering approximation and isotropic $Q_i$ are not derived; outer gradients go through the unrolled iterate, not implicit differentiation; MAP point estimates give no evidence bound; the post-hoc holonomy analysis refuses edge models; the curved-versus-control experiment is confounded by parameter counts unless controlled.

## Relevance to this research

This is the first implemented route from the shared-generator link of [[GL(K) gauge-equivariant attention]] to a link field with more than one [[Holonomy]] class per layer, and the computable restriction of the latent-link program of [[dennis-2026-dynamic-links]] and [[multiagentelbo-2026-10-04-lie-algebra-links]]. The pure-gauge arm is the designed control that separates curvature beyond the shared class from content-dependent transport. See [[VFE Transformer Program]].
