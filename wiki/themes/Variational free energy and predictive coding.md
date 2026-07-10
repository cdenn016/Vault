---
type: theme
title: Variational free energy and predictive coding
aliases:
  - Free energy and predictive coding
tags:
  - cluster/vfe
  - project/transformer
status: stable
created: 2026-06-18
updated: 2026-07-10
---

# Variational free energy and predictive coding

## The big picture

Variational free energy is the organizing objective of this entire research program. The idea is deceptively simple: when a model cannot compute the true posterior over latent causes of its observations, it instead posits a tractable approximate belief and minimizes a single scalar — the *variational free energy* — that upper-bounds the negative log evidence of the data. Minimizing that bound simultaneously pulls the approximate belief toward the true posterior and improves the model's account of the data. In machine learning the same quantity is read with the opposite sign and called the [[Evidence lower bound (ELBO)]]; in computational neuroscience it is read as an upper bound on *surprise* and called free energy. The [[VFE Transformer Program]] uses this framework for its per-token Gaussian belief objective, but the deployed decoder is trained by a separate cross-entropy objective rather than one literal shared VFE/ELBO.

Textbook VEM factors one functional into E and M coordinates. The deployed transformer instead has a target-blind belief objective and a separate decode cross-entropy objective. Its filtering step is one natural-gradient belief update, not a CAVI argmin, and textbook monotonicity does not transfer. [[gl-k-attention-2026-07-09-review-revision]]

Gaussian predictive-coding models weight observation-prediction errors by
precision. The deployed transformer borrows this as an analogy, but its
target-blind belief filter contains precision-weighted pairwise belief
mismatches rather than observation/likelihood prediction errors. Covariance
therefore modulates belief interactions without turning the filter into the
Rao–Ballard predictive-coding update.

## Key threads

**Free energy as one functional, two textbook steps.** Neal–Hinton incremental EM remains valid for a shared functional. See [[Variational EM]] for the explicit structural-EM disclosure showing why the deployed transformer falls outside that guarantee. [[gl-k-attention-2026-07-09-review-revision]]

**The neuroscience lineage: predictive coding.** [[rao-1999-predictive-coding]] introduced hierarchical predictive coding in which feedback carries predictions and feedforward pathways carry precision-weighted errors. [[friston-2010-free-energy-principle]], [[bogacz-2017-free-energy-tutorial]], and [[buckley-2017-fep-mathematical-review]] provide free-energy and Gaussian belief-relaxation interpretations. These sources motivate the transformer's belief-side precision-weighting analogy. They do not make its one-step target-blind filter a converged predictive-coding E-step, or its separate decode update the M-step of the same functional. [[gl-k-attention-2026-07-09-review-revision]]

**The machine-learning lineage: iterative variational refinement.** [[kingma-2013-auto-encoding-variational-bayes]] and [[marino-2018-iterative-amortized-inference]] provide Gaussian reparameterization and repeated-refinement precedents. The pure VFE transformer has no neural recognition network or learned optimizer, so these are comparison points rather than a literal amortized-inference blueprint, and no VAE amortization-gap result is established. [[winn-2005-variational-message-passing]] supplies related factor-graph background without determining the deployed update. [[gl-k-attention-2026-07-09-review-revision]]

**The bridge to backpropagation.** [[millidge-2020-pc-approximates-backprop]] proves exact-gradient recovery for the source model under its convergence and scheduling assumptions. The result is relevant background, but it does not certify the transformer's truncated two-objective loop as the same computation. [[gl-k-attention-2026-07-09-review-revision]]

**Cross-cluster reach.** Joint Gaussian belief updates use Fisher geometry; the
covariance block is one-half conventional AIRM. The frame M-step is not an
identified per-block Fisher natural gradient.
[[gl-k-attention-2026-07-09-review-revision]]

## How it lands in this work

In the [[VFE Transformer Program]], the belief filter and decode optimizer are structurally coupled but do not optimize one ELBO. Neither incremental-EM monotonicity nor converged predictive-coding/backprop equivalence certifies this truncated two-objective loop. [[gl-k-attention-2026-07-09-review-revision]]

The deployed attention uses precision-informed pairwise belief discrepancies,
with covariance modulating each token's interaction. This is formally analogous
to reliability weighting in predictive coding, not an observation-prediction
error in the Rao–Ballard sense. Kernel and entropy-regularization references
provide comparisons, but they do not merge the target-blind belief objective
with decode cross-entropy.

> [!note] Editorial (2026-07-10): The program compares beliefs across learned
> frames by transport. In realized Regime I,
> $\Omega_{ij}=U_iU_j^{-1}$ is pure gauge and has trivial loop holonomy, so
> nontrivial holonomy is not supplied by the frame parameterization alone.
> [[gl-k-attention-2026-07-09-review-revision]]

## Open questions / gaps

- **Structural filtering.** The prior question is superseded: even at KL order, the deployed belief and decode steps use distinct objectives, so Neal–Hinton monotonicity does not apply. [[gl-k-attention-2026-07-09-review-revision]]
- **Backprop-equivalence in a future shared objective.** Extending the source theorem to manifold-valued beliefs would first require a shared predictive-coding/decode objective and a converged schedule. The deployed two-objective filter lacks that premise before curvature is considered.
- **Precision learning vs. attention learning.** Predictive coding learns precisions explicitly ([[bogacz-2017-free-energy-tutorial]]); transformers learn attention weights implicitly. The architecture conflates the two via precision-weighted attention, but the digest contains no source quantifying when learned attention faithfully recovers the optimal precisions.
- **Depth of the inner loop.** Filter depth remains an empirical relaxation-versus-compute choice. Marino et al.'s amortization-gap result concerns a learned amortized optimizer and does not establish when this target-blind filter makes the separate decode gradient trustworthy.

## Sources synthesized

- [[neal-1998-variational-em]] — EM as coordinate ascent on one negative-free-energy functional; incremental or partial E-steps retain that license only in the shared-functional setting.
- [[friston-2010-free-energy-principle]] — Free-energy principle; perception/attention/learning/action as free-energy minimization.
- [[rao-1999-predictive-coding]] — Hierarchical predictive coding; precision-weighted prediction errors as the ancestor of precision-weighted attention.
- [[bogacz-2017-free-energy-tutorial]] — Explicit Gaussian-belief derivation of the precision-weighted E-step and precision-learning M-step.
- [[buckley-2017-fep-mathematical-review]] — Self-contained mathematical review of the continuous-state FEP; Laplace-encoded VFE and gradient-descent E-step bridging ELBO canon and FEP claims.
- [[smith-2022-active-inference-tutorial]] — Step-by-step discrete (POMDP) active-inference tutorial; explicit VFE/EFE updates and mean-field factorization as an E-step/M-step template.
- [[kingma-2013-auto-encoding-variational-bayes]] — VAE; ELBO via reparameterization and amortized Gaussian recognition.
- [[marino-2018-iterative-amortized-inference]] — Iterative amortized inference; learned optimizer closing the amortization gap.
- [[winn-2005-variational-message-passing]] — Mean-field VI on conjugate-exponential models as factor-graph message passing; the message-routing structure behind gauge-VFE attention.
- [[millidge-2020-pc-approximates-backprop]] — converged predictive-coding updates recover backpropagation under the source paper's schedule; the deployed one-step filter is outside that result.
- [[vaswani-2017-attention]] (cross-cluster) — Softmax-attention baseline the precision-weighted variant modifies.
- [[tsai-2019-kernel-attention]] (cross-cluster) — Kernel view of attention; precision weighting as an uncertainty-aware kernel.
- [[li-turner-2016-renyi-vi]] (cross-cluster) — variational Rényi bounds generalizing the ELBO, distinct from the configured pairwise order-Rényi discrepancy.
- [[vanerven-2014-renyi-kl]] (cross-cluster) — KL as the order-one limit of Renyi divergence.
- [[amari-1998-natural-gradient]] (cross-cluster) — Fisher-preconditioned natural gradient grounding the Gaussian belief update, not the audited plain-AdamW frame or decode M-step.
- [[friston-2023-fep-simpler]] — Streamlined statement of the free-energy principle and its [[Bayesian mechanics]] reading.
- [[bissiri-2016-general-bayesian-updating|bissiri-holmes-walker-2016-general-bayes]] — General Bayesian updating from a loss-based coherence argument, motivating divergence choices beyond KL.

## See also

- [[Bayesian mechanics]]
- [[Markov blanket interpretation debate]]
- [[Information bottleneck]]

## Related sources (ingested 2026-06-20)

- [[bishop-2006-pattern-recognition-machine-learning]] — Ch.
- [[wainwright-2008-graphical-models-variational|wainwright-jordan-2008-graphical-models-variational-inference]] — Exponential-family / convex-duality foundation of variational inference;
- [[beal-2003-variational-bayesian|beal-2003-variational-algorithms-approximate-bayesian-inference]] — Beal's thesis - variational Bayesian EM and the free-energy lower bound for latent-variable models;
