---
type: method
title: "Projected gradient attention"
aliases:
  - projected_gradient
  - Projected gradient route
  - Channel-likelihood receiver
tags:
  - cluster/attention
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
status: draft
created: 2026-10-02
updated: 2026-10-25
---

# Projected gradient attention

## Main-manuscript derivation and first training run, October 4, 2026

The channel-likelihood receiver and its closed form now appear in the main GL(K) manuscript as Section 7 of [[dennis-2026-glk-lie-algebra-links-v2]]. With the tied measurement $\mathsf P_h=\widetilde O_h^\top$ of the active content-link chart, channel covariance $R_{hj}=T_h\bar C_jT_h^\top+Q_h^{\mathrm{ch}}$ and the routing weights as likelihood powers, the minimizer $\xi^\star=\Lambda^{-1}\eta$, $C^\star=\lambda_\alpha\Lambda^{-1}$ is the Gaussian power posterior.

## Unified receiver interpretation, October 3, 2026

[[dennis-2026-attention-unified]] reconciles the receiver note with the implemented channel-likelihood and closed-form paths. Its frozen expected-log-likelihood energy has a normalized generalized-posterior or variational-coordinate interpretation. It generally differs from the receiver marginal obtained by conditioning on each source separately and mixing those normalized posteriors, so the earlier blanket phrase "exact cut inference" requires that distinction. Full-family natural-parameter interpolation has the stated frozen-objective descent result. Diagonal damping lacks that guarantee; covariance clamps also qualify an unconstrained minimizer claim. The active launcher remains predictive, so these are reachable alternatives rather than the selected receiver.

The attention route of the [[VFE Transformer Program|vfe3 transformer]] selected by `attention_mode="projected_gradient"`. It shares routing and matrix links with [[Projected predictive attention]] but, instead of assigning a predictive readout, moves each receiving token's Gaussian state against a receiver energy with the incoming snapshot frozen. The theory is [[dennis-2026-projected-gradient]]; the implementation history is `VFE_3.0/docs/2026-10-02.md`. As of October 2, 2026 it is one of the two executable routes.

## Routing and the cut model

Routing is the same as on the predictive route: exact partial query and key laws $\mathcal N(S_Q\xi_i,S_QC_iS_Q^\top)$, $\mathcal N(S_K\xi_j,S_KC_jS_K^\top)$, their KL $D_{ij}^h$, and Gibbs weights $\beta_{ij}^h=\mathrm{softmax}_j(\log\pi_{ij}^h-D_{ij}^h/\tau_h)$ ([[GL(K) gauge-equivariant attention]], [[Softmax]]). [[dennis-2026-projected-gradient]] shows that routing by $D$ alone while content moves the receiver is not coordinate descent of any single content-informed functional affine in $\beta$, but is exact inference in a declared cut model, where the content likelihood is not allowed to update the source label. Under the cut, freezing $\beta$ during the receiver episode is exact, and the routing entropy and comparison force are absent from the receiver gradient. Joint routing, in which $\beta$ also sees content and the gradient carries the comparison force, is a separate model not implemented.

## Receiver laws

Both receivers are quadratic in $(\xi,C)$ with an entropy coefficient $\kappa$, minimizer $(\Lambda^{-1}\eta,\kappa\Lambda^{-1})$ and Euler bound $\varepsilon<2/\kappa$ at the covariance optimum.

- **`ambient_alignment`** (the PR #30 energy) aligns the receiver to each head's message lifted to a $K$-dimensional law $\mathcal N(M_h\bar\xi_j,M_h\bar C_jM_h^\top+\nu I_K)$. The noise is needed for finiteness, each head pins its unwritten coordinates to zero, and the receiver entropy is counted $c=\alpha+\sum_h\lambda_h$ times. At launcher scale the Euler step was unstable, which the October 1 audit reported.
- **`channel_likelihood`** (default since PR #34) scores the measurement $O_h^\top x$ against the sender's $d$-dimensional message $T_h\bar\xi_j$ through a channel with noise $\nu I_d$ as an expected log-likelihood. It counts the entropy once ($\kappa=\alpha$), its minimizer is the exact tempered Gaussian posterior, unobserved directions keep the prior, and pooling is $d\times d$. With orthonormal disjoint heads, source-independent channel covariance and a vanishing prior it reproduces the residual-free predictive head sum, so the two routes agree in a stated limit. Away from it the gradient route fuses precision-weighted messages where the predictive route adds.

The update is either `euler` (the PR #30 step) or `closed_form` (default): the exact natural-parameter Fisher flow $J^+=(1-\rho)J+\rho\Lambda/\kappa$, $h^+=(1-\rho)h+\rho\eta/\kappa$, which is SPD and monotone for every damping $\rho$ in the full family ([[Natural gradient]], [[Fisher information metric]]). For the diagonal family $\rho=1$ is the exact restricted minimizer, but damped diagonal steps have no descent guarantee: an explicit two-dimensional instance raises the frozen energy from 1.500 to 2.503 at $\rho=1/2$.

## Profiled self-coupling

Since PR #38 the self-coupling $\alpha$ may be state dependent, $\alpha^\star=c_0/(b_0+\mathrm{KL}(q\Vert p))$, recomputed at each iteration. The profiled energy is $c_0\log(b_0+D)+G$; its gradient is the frozen-$\alpha$ force by the envelope theorem, and the closed-form step at frozen $\alpha$ is a majorize-minimize step because the logarithm lies below its tangent, so the profiled energy does not increase at $\rho=1$. A per-coordinate form is exact on the diagonal family but tied to the local basis; its full-family closed form is derived and checked at $K=4$ but not implemented.

> [!note] Editorial: The profiled rule is the same $\alpha^\star=c_0/(b_0+D)$ anchor that appears in the multi-agent model; on the transformer route it is a receiver-level choice whose effect on training is untested; a matched multi-seed comparison with the predictive route is the deciding experiment.

## Fusion residual and the exponential link, October 2026

At finite precision the channel-likelihood receiver yields a partial residual in the observed directions: for an isotropic prior of precision $\alpha$ and message evidence of precision $\lambda$ on the written subspace $W$, $\xi_i^+=(I-P_W)\xi_i+P_W(\alpha\xi_i+\lambda m_i)/(\alpha+\lambda)$, full residual on unobserved directions and $\alpha/(\alpha+\lambda)$ on observed ones. The complement-only residual of the exponential link in [[dennis-2026-link-origin]] is the limit $\lambda/\alpha\to\infty$, and with tiled heads both give no residual at flat prior. The additive $r=1$ residual of the predictive route is neither. This is a note-level derivation with a float64 identity check at small dimension; no training result.

## Related

[[Projected predictive attention]], [[GL(K) gauge-equivariant attention]], [[Precision weighting]], [[Multi-head attention]], [[Variational free energy]], [[VFE Transformer Program]]

## Sources

[[dennis-2026-glk-lie-algebra-links-v2]], [[dennis-2026-link-origin]], [[dennis-2026-projected-gradient]], [[dennis-2026-projected-predictive]], [[dennis-2026-glk-projected-matrix-links-v2]], [[blei-2017-variational-inference]], [[bishop-2006-pattern-recognition-machine-learning]]
