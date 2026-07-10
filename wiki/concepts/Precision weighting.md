---
type: concept
title: Precision weighting
aliases:
  - Precision-weighted prediction error
  - Inverse-variance weighting
  - Precision weighting (attention)
  - "Attention as Precision-Weighting"
  - "Attention as precision-weighting"
  - "Attention as Precision"
  - "Attention as Inference"
  - "Precision-weighted attention"
tags:
  - cluster/vfe
  - cluster/attention
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-07-09
---

# Precision weighting

## Definition

**Precision weighting** is the operation of scaling a quantity (typically a [[Prediction error]]) by a **precision** — the inverse of a variance or, in the multivariate case, the inverse covariance matrix. If a belief or observation is modelled as Gaussian with covariance `Sigma`, its precision is `Pi = Sigma^{-1}`, and a precision-weighted prediction error is `Pi (x - mu)` rather than the raw residual `x - mu`. The intuition is statistical optimality: when combining noisy estimates, each should contribute in proportion to how reliable it is, so low-variance (high-precision) channels dominate and high-variance (uncertain) channels are discounted. This is exactly inverse-variance weighting, the rule that minimizes the variance of a combined estimate and that appears whenever Gaussian likelihoods are multiplied (as in Bayesian cue combination or the Kalman gain).

In the Gaussian variational setting that underlies this project, precision weighting is not an add-on but a structural consequence of the objective: minimizing [[Variational free energy]] for Gaussian beliefs produces gradients whose every residual term is multiplied by a precision. Precision is therefore the natural currency in which prediction errors are denominated.

## Why it matters here

The VFE transformer maintains a per-token Gaussian belief `(mu, Sigma)`. Its target-blind belief objective and decode cross-entropy are distinct, so precision weighting belongs to the belief and attention channels rather than one shared ELBO. Two design choices make it central rather than incidental: [[gl-k-attention-2026-07-09-review-revision]]

1. **It enters the belief gradient.** Gaussian belief gradients retain their precision-weighted form. The deployed target-blind E-step and cross-entropy M-step descend distinct objectives, so textbook coordinate-ascent EM does not describe their joint schedule. [[gl-k-attention-2026-07-09-review-revision]]

2. **It reshapes attention — structurally, not via a flag.** Attention here is precision-weighted by construction: the attention logit is itself a Gaussian KL, $\beta_{ij}\propto\exp(-D_{\mathrm{KL}}[q_i\|\Omega_{ij}q_j]/\tau)$, whose quadratic term $(\mu_i-\Omega_{ij}\mu_j)^\top S_{ij}^{-1}(\mu_i-\Omega_{ij}\mu_j)$ weights the transported prediction error by the neighbor's precision $S_{ij}^{-1}=(\Omega_{ij}\Sigma_j\Omega_{ij}^\top)^{-1}$. On the live `gaussian_diagonal` family this matrix Mahalanobis is realized as a *per-coordinate inverse-variance* weight — $S_{ij}$ is the diagonal of the transported sandwich $\Omega_{ij}\Sigma_j\Omega_{ij}^\top$ (`families/gaussian.py:102` divides by `sigma_t`) — with the full matrix $S^{-1}$ arising only on the full-covariance and Route B (`gauge_invariant_edge_features`) paths. Confident (high-precision) sources therefore produce sharper logits and dominate the read; uncertain ones are discounted. This is the transformer realization of the predictive-coding circuit of [[rao-1999-predictive-coding]], where feedforward signals carry precision-weighted prediction errors and precision acts as an attentional gain. The config flag literally named `precision_weighted_attention` is a *separate, narrower* device (see the editorial note under "In this work") — not the source of this structural precision weighting, which is always on in the pure path.

Precision weighting thus links the two faces of the system: it is simultaneously the inference update (how beliefs move) and the attentional gating (how tokens read each other).

## Details

**Scalar case.** Combining two unbiased Gaussian estimates `x_1, x_2` with variances `sigma_1^2, sigma_2^2` optimally gives a posterior mean weighted by precisions, `mu = (pi_1 x_1 + pi_2 x_2)/(pi_1 + pi_2)` with `pi_i = 1/sigma_i^2`, and posterior precision `pi_1 + pi_2`. Precision weighting is the multivariate generalization of this rule.

**Free-energy gradient.** Take a Gaussian generative model `x ~ N(g(mu), Sigma_x)` with a Gaussian prior `mu ~ N(m, Sigma_p)`. The variational free energy contains quadratic terms `(x - g(mu))^T Sigma_x^{-1} (x - g(mu))` and `(mu - m)^T Sigma_p^{-1} (mu - m)`. Differentiating, the belief update is driven by
`d mu / dt ∝ -Sigma_p^{-1}(mu - m) + g'(mu)^T Sigma_x^{-1}(x - g(mu))`,
i.e. a balance of *precision-weighted* prior and likelihood errors. Following [[bogacz-2017-free-energy-tutorial]] one introduces explicit error units `epsilon = Sigma^{-1}(x - mu)` carrying the precision-weighted residuals; learning the precisions is itself a gradient step on the same free energy, the M-step. [[millidge-2020-pc-approximates-backprop]] shows that running these local precision-weighted error updates to convergence recovers exact backpropagation gradients, so the inference loop and end-to-end training agree.

**Precision as attentional gain.** In [[rao-1999-predictive-coding]] and the free-energy-principle synthesis of [[friston-2010-free-energy-principle]], attention *is* the optimization of expected precision: raising the precision on a channel amplifies its prediction errors and lets it steer inference, formally identical to an attentional gain. Reading the transformer through the kernel lens of [[tsai-2019-kernel-attention]], precision weighting is a particular choice of kernel/similarity, and through [[wang-2023-riemannian-self-attention-spd]] it connects to SPD-manifold affinities computed with the affine-invariant metric.

**Attention as inference / as precision.** Read the other way round, this is the claim that softmax attention is *not* an ad hoc weighting but the computational signature of probabilistic inference: it implements a posterior over which keys are relevant to a query, equivalent to precision-weighted Bayesian cue combination in which more reliable (higher-precision) sources receive more weight ([[pouget-2013-probabilistic-brains]]). The active-inference reading sharpens this into an *identity* — attention is the gain modulation of ascending prediction-error signals by their estimated reliability, rather than a separate selection mechanism ([[clark-2013-predictive-brains]]) — which grounds neural-network attention weights as precision (Fisher-information) estimates and is what lets the program's gauge/precision-weighted attention inherit Friston's free-energy formulation directly ([[sengupta-2016-neuronal-gauge]]).

**Information-geometric variant.** Precision is the Gaussian Fisher information for the mean, so precision weighting and [[Natural gradient]] preconditioning coincide in this family: the [[Fisher information metric]] of [[amari-1998-natural-gradient]] *is* the precision, and updating `mu` by inverse-Fisher is updating by inverse-covariance. The block-wise Fisher preconditioning of [[martens-2015-kfac]] and the unit/block-diagonal natural gradients of [[ollivier-2015-riemannian-metrics-nn]] are precision weighting carried into parameter space.

> [!note] Editorial: Because the project uses a `gaussian_diagonal` family, the working precision is a diagonal `Sigma^{-1}`, making precision weighting an elementwise rescaling per token; the full-covariance case recovers the matrix form above and the SPD geometry of [[pennec-2006-affine-invariant-tensor]].

## In this work

Precision weighting surfaces at several points in the configured model:

- **Structural precision weighting (always on, the pure path)** — the attention logit is the Gaussian KL $-D_{\mathrm{KL}}(q_i\|\Omega_{ij}q_j)/\tau$, so the precision $S_{ij}^{-1}$ weights every prediction error inside the softmax (`vfe3/families/gaussian.py`: `mahal_term = ((mu_t - mu_q)**2 / sigma_t)`, then `div = 0.5*(trace + mahal - K + logdet)`); active whenever `divergence_family="renyi"` at order $\alpha=1$ (= KL), the default. Predictive-coding ancestor [[rao-1999-predictive-coding]]; kernel reading [[tsai-2019-kernel-attention]].
- **The `precision_weighted_attention` config flag (default OFF) is NOT this** — it is a detached, key-only scalar *reliability* bias $-\log(b_0+\operatorname{tr}\Sigma_j)$ added to the attention log-prior (`vfe3/model/model.py`: `_precision_key_bias` / `_fold_precision_bias`), uniformly down-weighting high-variance keys. It is query-independent, detached (so the closed-form belief kernel stays exact), and does not alter the KL logit. The name is a trap: the substantive precision weighting lives in the divergence, not in this flag.
- **E-step / M-step (`gradient_mode: filtering`)** — the belief update is a one-step filter on its own objective; the decode M-step minimizes cross-entropy separately. [[gl-k-attention-2026-07-09-review-revision]]
- **`family: gaussian_diagonal`** — the precision is a per-token diagonal `Sigma^{-1}`; the covariance itself lives on the SPD cone and is updated with the `spd_affine` retraction of [[pennec-2006-affine-invariant-tensor]].
- **No data precision in the belief covariance (2026-06-29 finding).** Inverse-variance combination would set a posterior precision `Pi_post = Pi_prior + Pi_data`, but the deployed vfe3 belief E-step has **no `Pi_data` channel**: its $\nabla_\Sigma$ is only the self-coupling and belief-coupling KL terms — the observation/likelihood term is a gated stub with no live caller (a [[Variational EM|target-blind E-step]]). So `Sigma_q` is never contracted by per-token evidence; it stays pinned to a near-constant learned prior table (shrunk toward one shared centroid), collapsing the gate that would license $\sigma$ as an epistemic signal ([[2026-06-29-sigma-gate-fail-and-collapse]]). Precision here is *learned into the tables*, not *inferred per token from data* — the perceptual gain modulation above operates on the means, while the covariance is effectively static.
- **Frame M-step** — the audited frame table uses plain AdamW; optional frame conditioning is inactive and is not Fisher precision weighting. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Editorial (2026-06-18): The config flag named `precision_weighted_attention` is a naming trap. Verified against the code (`vfe3/config.py:309` default `False`; `vfe3/model/model.py:34–57,1192–1215`), it gates only a detached, query-independent reliability prior $-\log(b_0+\operatorname{tr}\Sigma_j)$ on the attention keys — it never enters the KL logit. The substantive precision weighting is the inverse-covariance Mahalanobis term *inside* the Gaussian KL divergence (`vfe3/families/gaussian.py:99–104` — the `abs(alpha-1)<1e-6` KL branch opens at line 99) and is always on in the theoretically-pure path. Established by multi-agent derivation + code reconciliation, 2026-06-18 (see [[log|Operations Log]]).

See [[VFE Transformer Program]] for the concrete configuration in which these terms appear and the program-level framing.

## Sources

- [[bogacz-2017-free-energy-tutorial]] — explicit precision-weighted E-step/M-step Gaussian updates.
- [[rao-1999-predictive-coding]] — precision-weighted prediction errors as the cortical/attentional template.
- [[friston-2010-free-energy-principle]] — precision optimization as attention within the free-energy principle.
- [[neal-1998-variational-em]] — coordinate ascent on one free-energy functional; it justifies incremental steps only when both coordinates optimize that same functional, not the deployed two-objective schedule.
- [[bishop-2006-pattern-recognition-machine-learning]] — Ch. 10 variational inference / ELBO / mean-field EM as belief-side background, not a shared-functional description of the deployed loop.
- [[millidge-2020-pc-approximates-backprop]] — local precision-weighted errors recover backprop.
- [[amari-1998-natural-gradient]] — precision as Fisher information; precision weighting as natural gradient.
- [[martens-2015-kfac]] — block-Fisher (precision) preconditioning in parameter space.
- [[ollivier-2015-riemannian-metrics-nn]] — block/unit-diagonal Fisher metrics for neural nets.
- [[tsai-2019-kernel-attention]] — attention as a kernel, precision weighting as a kernel choice.
- [[wang-2023-riemannian-self-attention-spd]] — SPD affinities bridging precision and attention.
- [[pennec-2006-affine-invariant-tensor]] — SPD geometry for the covariances whose inverse is the precision.
- [[pouget-2013-probabilistic-brains]] — probabilistic-population-code account of precision-weighted Bayesian cue combination, the inference reading of attention.
- [[clark-2013-predictive-brains]] — predictive-processing account in which attention is the optimization of expected precision on prediction errors.
- [[sengupta-2016-neuronal-gauge]] — neuronal gauge theory linking precision-weighted attention to the free-energy formulation.

## See also

- [[Prediction error]]
- [[Variational free energy]]
- [[Evidence lower bound (ELBO)]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[Predictive coding network]]
- [[Variational EM]]
- [[Free-energy principle active inference]]
