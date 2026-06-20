---
type: concept
title: Precision weighting
aliases:
  - Precision-weighted prediction error
  - Inverse-variance weighting
  - Precision weighting (attention)
tags:
  - cluster/vfe
  - cluster/attention
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Precision weighting

## Definition

**Precision weighting** is the operation of scaling a quantity (typically a [[Prediction error]]) by a **precision** — the inverse of a variance or, in the multivariate case, the inverse covariance matrix. If a belief or observation is modelled as Gaussian with covariance `Sigma`, its precision is `Pi = Sigma^{-1}`, and a precision-weighted prediction error is `Pi (x - mu)` rather than the raw residual `x - mu`. The intuition is statistical optimality: when combining noisy estimates, each should contribute in proportion to how reliable it is, so low-variance (high-precision) channels dominate and high-variance (uncertain) channels are discounted. This is exactly inverse-variance weighting, the rule that minimizes the variance of a combined estimate and that appears whenever Gaussian likelihoods are multiplied (as in Bayesian cue combination or the Kalman gain).

In the Gaussian variational setting that underlies this project, precision weighting is not an add-on but a structural consequence of the objective: minimizing [[Variational free energy]] for Gaussian beliefs produces gradients whose every residual term is multiplied by a precision. Precision is therefore the natural currency in which prediction errors are denominated.

## Why it matters here

The VFE transformer maintains a per-token Gaussian belief `(mu, Sigma)` and trains by minimizing a free-energy / [[Evidence lower bound (ELBO)]] objective. Two design choices make precision weighting central rather than incidental:

1. **It is the gradient of free energy.** For Gaussian beliefs the free-energy gradient with respect to a token's mean is a sum of *precision-weighted* prediction errors, as derived step by step in [[bogacz-2017-free-energy-tutorial]]. The E-step belief relaxation and the M-step precision learning the architecture implements are literally these precision-weighted error dynamics, in the coordinate-ascent form of [[neal-1998-variational-em]]; the textbook account of the variational lower bound and mean-field EM that the transformer instantiates per token is [[bishop-2006-pattern-recognition-machine-learning]] (Ch. 10).

2. **It reshapes attention — structurally, not via a flag.** Attention here is precision-weighted by construction: the attention logit is itself a Gaussian KL, $\beta_{ij}\propto\exp(-D_{\mathrm{KL}}[q_i\|\Omega_{ij}q_j]/\tau)$, whose quadratic term $(\mu_i-\Omega_{ij}\mu_j)^\top S_{ij}^{-1}(\mu_i-\Omega_{ij}\mu_j)$ weights the transported prediction error by the neighbor's precision $S_{ij}^{-1}=(\Omega_{ij}\Sigma_j\Omega_{ij}^\top)^{-1}$. On the live `gaussian_diagonal` family this matrix Mahalanobis is realized as a *per-coordinate inverse-variance* weight — $S_{ij}$ is the diagonal of the transported sandwich $\Omega_{ij}\Sigma_j\Omega_{ij}^\top$ (`families/gaussian.py:102` divides by `sigma_t`) — with the full matrix $S^{-1}$ arising only on the full-covariance and Route B (`gauge_invariant_edge_features`) paths. Confident (high-precision) sources therefore produce sharper logits and dominate the read; uncertain ones are discounted. This is the transformer realization of the predictive-coding circuit of [[rao-1999-predictive-coding]], where feedforward signals carry precision-weighted prediction errors and precision acts as an attentional gain. The config flag literally named `precision_weighted_attention` is a *separate, narrower* device (see the editorial note under "In this work") — not the source of this structural precision weighting, which is always on in the pure path.

Precision weighting thus links the two faces of the system: it is simultaneously the inference update (how beliefs move) and the attentional gating (how tokens read each other).

## Details

**Scalar case.** Combining two unbiased Gaussian estimates `x_1, x_2` with variances `sigma_1^2, sigma_2^2` optimally gives a posterior mean weighted by precisions, `mu = (pi_1 x_1 + pi_2 x_2)/(pi_1 + pi_2)` with `pi_i = 1/sigma_i^2`, and posterior precision `pi_1 + pi_2`. Precision weighting is the multivariate generalization of this rule.

**Free-energy gradient.** Take a Gaussian generative model `x ~ N(g(mu), Sigma_x)` with a Gaussian prior `mu ~ N(m, Sigma_p)`. The variational free energy contains quadratic terms `(x - g(mu))^T Sigma_x^{-1} (x - g(mu))` and `(mu - m)^T Sigma_p^{-1} (mu - m)`. Differentiating, the belief update is driven by
`d mu / dt ∝ -Sigma_p^{-1}(mu - m) + g'(mu)^T Sigma_x^{-1}(x - g(mu))`,
i.e. a balance of *precision-weighted* prior and likelihood errors. Following [[bogacz-2017-free-energy-tutorial]] one introduces explicit error units `epsilon = Sigma^{-1}(x - mu)` carrying the precision-weighted residuals; learning the precisions is itself a gradient step on the same free energy, the M-step. [[millidge-2020-pc-approximates-backprop]] shows that running these local precision-weighted error updates to convergence recovers exact backpropagation gradients, so the inference loop and end-to-end training agree.

**Precision as attentional gain.** In [[rao-1999-predictive-coding]] and the free-energy-principle synthesis of [[friston-2010-free-energy-principle]], attention *is* the optimization of expected precision: raising the precision on a channel amplifies its prediction errors and lets it steer inference, formally identical to an attentional gain. Reading the transformer through the kernel lens of [[tsai-2019-kernel-attention]], precision weighting is a particular choice of kernel/similarity, and through [[wang-2023-riemannian-self-attention-spd]] it connects to SPD-manifold affinities computed with the affine-invariant metric.

**Information-geometric variant.** Precision is the Gaussian Fisher information for the mean, so precision weighting and [[Natural gradient]] preconditioning coincide in this family: the [[Fisher information metric]] of [[amari-1998-natural-gradient]] *is* the precision, and updating `mu` by inverse-Fisher is updating by inverse-covariance. The block-wise Fisher preconditioning of [[martens-2015-kfac]] and the unit/block-diagonal natural gradients of [[ollivier-2015-riemannian-metrics-nn]] are precision weighting carried into parameter space.

> [!note] Editorial: Because the project uses a `gaussian_diagonal` family, the working precision is a diagonal `Sigma^{-1}`, making precision weighting an elementwise rescaling per token; the full-covariance case recovers the matrix form above and the SPD geometry of [[pennec-2006-affine-invariant-tensor]].

## In this work

Precision weighting surfaces at several points in the configured model:

- **Structural precision weighting (always on, the pure path)** — the attention logit is the Gaussian KL $-D_{\mathrm{KL}}(q_i\|\Omega_{ij}q_j)/\tau$, so the precision $S_{ij}^{-1}$ weights every prediction error inside the softmax (`vfe3/families/gaussian.py`: `mahal_term = ((mu_t - mu_q)**2 / sigma_t)`, then `div = 0.5*(trace + mahal - K + logdet)`); active whenever `divergence_family="renyi"` at order $\alpha=1$ (= KL), the default. Predictive-coding ancestor [[rao-1999-predictive-coding]]; kernel reading [[tsai-2019-kernel-attention]].
- **The `precision_weighted_attention` config flag (default OFF) is NOT this** — it is a detached, key-only scalar *reliability* bias $-\log(b_0+\operatorname{tr}\Sigma_j)$ added to the attention log-prior (`vfe3/model/model.py`: `_precision_key_bias` / `_fold_precision_bias`), uniformly down-weighting high-variance keys. It is query-independent, detached (so the closed-form belief kernel stays exact), and does not alter the KL logit. The name is a trap: the substantive precision weighting lives in the divergence, not in this flag.
- **E-step / M-step (`gradient_mode: filtering`)** — the belief relaxation and parameter updates are precision-weighted free-energy gradients in the coordinate-ascent form of [[neal-1998-variational-em]], derived explicitly in [[bogacz-2017-free-energy-tutorial]].
- **`family: gaussian_diagonal`** — the precision is a per-token diagonal `Sigma^{-1}`; the covariance itself lives on the SPD cone and is updated with the `spd_affine` retraction of [[pennec-2006-affine-invariant-tensor]].
- **M-step preconditioning** — [[Killing form|Killing-form]] / Fisher per-block preconditioning is precision weighting in parameter space, in the spirit of [[martens-2015-kfac]] and [[amari-1998-natural-gradient]].

> [!note] Editorial (2026-06-18): The config flag named `precision_weighted_attention` is a naming trap. Verified against the code (`vfe3/config.py:309` default `False`; `vfe3/model/model.py:34–57,1192–1215`), it gates only a detached, query-independent reliability prior $-\log(b_0+\operatorname{tr}\Sigma_j)$ on the attention keys — it never enters the KL logit. The substantive precision weighting is the inverse-covariance Mahalanobis term *inside* the Gaussian KL divergence (`vfe3/families/gaussian.py:99–104` — the `abs(alpha-1)<1e-6` KL branch opens at line 99) and is always on in the theoretically-pure path. Established by multi-agent derivation + code reconciliation, 2026-06-18 (see [[log|Operations Log]]).

See [[VFE Transformer Program]] for the concrete configuration in which these terms appear and the program-level framing.

## Sources

- [[bogacz-2017-free-energy-tutorial]] — explicit precision-weighted E-step/M-step Gaussian updates.
- [[rao-1999-predictive-coding]] — precision-weighted prediction errors as the cortical/attentional template.
- [[friston-2010-free-energy-principle]] — precision optimization as attention within the free-energy principle.
- [[neal-1998-variational-em]] — coordinate-ascent free-energy view justifying the belief/parameter steps.
- [[bishop-2006-pattern-recognition-machine-learning]] — Ch. 10 variational inference / ELBO / mean-field EM that the VFE transformer instantiates per token.
- [[millidge-2020-pc-approximates-backprop]] — local precision-weighted errors recover backprop.
- [[amari-1998-natural-gradient]] — precision as Fisher information; precision weighting as natural gradient.
- [[martens-2015-kfac]] — block-Fisher (precision) preconditioning in parameter space.
- [[ollivier-2015-riemannian-metrics-nn]] — block/unit-diagonal Fisher metrics for neural nets.
- [[tsai-2019-kernel-attention]] — attention as a kernel, precision weighting as a kernel choice.
- [[wang-2023-riemannian-self-attention-spd]] — SPD affinities bridging precision and attention.
- [[pennec-2006-affine-invariant-tensor]] — SPD geometry for the covariances whose inverse is the precision.

## See also

- [[Prediction error]]
- [[Variational free energy]]
- [[Evidence lower bound (ELBO)]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[Predictive coding network]]
- [[Variational EM]]
- [[Free-energy principle active inference]]
