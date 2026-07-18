---
type: theme
title: Information geometry and natural gradient
aliases:
  - Fisher-Rao geometry
  - Natural-gradient optimization
  - "Dual connections"
  - "Dual connection"
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-18
updated: 2026-07-18
---

# Information geometry and natural gradient

## The big picture

Information geometry is the differential geometry of probability distributions. Rather than treating a parametric family — say all diagonal Gaussians indexed by their means and variances — as a flat Euclidean parameter space, it equips that space with a Riemannian metric derived from the distributions themselves. That metric is the [[Fisher information metric]]: the local quadratic form measuring how distinguishable two nearby distributions are, as quantified by the curvature of the [[Renyi divergence|Kullback-Leibler divergence]] near the diagonal. Once the parameter space carries this metric, "downhill" stops meaning "opposite the raw gradient" and starts meaning "opposite the gradient corrected by the inverse metric." That corrected direction is the [[Natural gradient]], and it is the organizing object of this theme.

For the VFE transformer, the exact information-geometric claim concerns Gaussian beliefs: their mean/covariance family has a Fisher metric and corresponding natural gradient. Gauge-frame parameters are not themselves a statistical family merely because they are matrices; their optional conditioner has no established Fisher or full-$\mathrm{GL}(K)$ invariance. [[gl-k-attention-2026-07-09-review-revision]]

The canonical reference frame here is Amari's program. [[amari-1998-natural-gradient]] derives Fisher-preconditioned steepest descent on a statistical manifold. [[amari-2000-methods-information-geometry]] develops the Fisher metric, dual affine connections, Amari alpha-connections, and dually-flat exponential-family geometry. Amari alpha-divergences, order-Rényi divergence, and the Li–Turner variational Rényi bound are related but distinct constructions; the configured pairwise Rényi discrepancy does not inherit one common alpha-connection interpretation merely by name. [[gl-k-attention-2026-07-09-review-revision]]

A second, equally important thread reads the natural gradient not as exotic geometry but as practical second-order optimization. [[martens-2020-natural-gradient-insights]] shows that under standard conditions the Fisher information matrix coincides with the Generalized Gauss-Newton matrix, so the natural gradient is a curvature-aware update that substitutes the Fisher for the Hessian — with the bonus that the Fisher is positive-semidefinite by construction and pairs naturally with damping. This perspective makes the whole apparatus implementable: it tells you exactly which matrix to approximate, why approximating it is principled, and how to stabilize the result.

## Key threads

**Natural gradient as Fisher-preconditioned, invariant descent.** Amari's result applies to a statistical family with a specified Fisher metric ([[amari-1998-natural-gradient]]). [[ollivier-2015-riemannian-metrics-nn]] and [[khan-rue-2023-bayesian-learning-rule]] provide neural-network and exponential-family optimization precedents. In this project the established application is the Gaussian belief update; these sources do not identify the gauge-frame M-step or decode optimizer as Fisher-natural. [[gl-k-attention-2026-07-09-review-revision]]

**Making Fisher methods tractable.** Gauss-Newton and K-FAC remain relevant general methods, but the block structure of $\mathrm{GL}(K)$ does not by itself make the configured frame conditioner a Fisher/K-FAC approximation. [[gl-k-attention-2026-07-09-review-revision]]

**Dual connections and divergence families.** [[amari-2000-methods-information-geometry]] and [[zhang-2004-divergence-duality-convex]] describe Amari-style alpha-divergences and their dual connections. [[vanerven-2014-renyi-kl]] describes order-Rényi divergence, whose standard local quadratic form is an order-dependent multiple of Fisher and whose order-one limit is KL. [[li-turner-2016-renyi-vi]] defines a variational Rényi bound. These are not interchangeable: selecting `divergence_family: "renyi"` supplies a pairwise belief discrepancy, not the Li–Turner bound, a decode loss, or an Amari alpha-connection for the full training loop. [[gl-k-attention-2026-07-09-review-revision]]

**Connection to the variational machinery.** Gaussian free-energy gradients and
Gaussian natural gradients are related but not identical by terminology alone.
Predictive-coding derivations such as [[bogacz-2017-free-energy-tutorial]] use
specified precision-weighted ordinary-gradient dynamics, whereas a natural
gradient preconditions by the inverse Fisher matrix. Equating the two requires
an explicit objective, coordinate choice, and calculation; the cited
predictive-coding sources do not establish that equality for the deployed
filter. The implemented belief update can still be assessed directly against
its joint Gaussian Fisher formula, whose covariance block is one-half
conventional AIRM. Broader links to statistical mechanics,
physics from Fisher information, and quantum monotone metrics remain comparison
themes rather than optimizer identities.

## How it lands in this work

In the VFE transformer, Gaussian belief updates use information geometry. At each recorded source SHA, the committed gate and stored configuration route the frame table through AdamW; every provenance record marks a dirty worktree, so the exact executed optimizer cannot be reconstructed. Heavy-ball belongs only to the disabled custom outer optimizer. The exponential-coordinate pullback can condition either optional frame route, but both are off; BCH/retraction belongs only to the disabled in-E-step route. Optional Cartan/Killing or pullback conditioning is extrinsic and is not a Fisher, K-FAC, or reparameterization-invariant natural gradient. [[gl-k-attention-2026-07-09-review-revision]]

The rebuilt opt-in `pullback_group` route now supplies a cleaner empirical separation. Its first
retained K=10 run used a stateless Frobenius-pullback direction and BCH group update on the existing
outer cross-entropy covector. Through validation step 9,000, PPL improved from 456.32 to 365.57, but
the user observed substantially poorer performance than AdamW. The geometry diagnostics remained
benign: direction cosine 0.991, median damped generalized condition number 1.90, and accepted update
scale 1.0. Thus this partial result points toward stochastic optimizer dynamics and learning-rate
scale rather than a singular pullback solve. It is not yet a controlled AdamW comparison because no
matching K=10 AdamW artifact is retained and the registered pullback learning-rate sweep is
incomplete. [[2026-07-18-phi-pullback-group-k10-partial-negative-result]]

The configured `renyi` family supplies a pairwise belief-side Rényi discrepancy with KL at order one. It is not, without an additional derivation, the variational Rényi bound of [[li-turner-2016-renyi-vi]], the separate decode cross-entropy, or an Amari alpha-divergence connection. The Gaussian belief update independently retains its Fisher geometry. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Editorial (2026-07-10): the zero-mean Gaussian covariance Fisher metric
> is one-half conventional AIRM. The frame conditioner is a different object,
> not the same metric in other coordinates. Its Frobenius pullback through
> $\exp$ is positive definite only where $D\exp$ has full rank and is neither
> left invariant nor Fisher. [[gl-k-attention-2026-07-09-review-revision]]

## Open questions / gaps

The main gap is not a missing proof that one joint natural gradient covers the
whole model; the deployed system uses different optimizers for different
objects. Joint Gaussian Fisher geometry is established for the belief update,
with a covariance block equal to one-half conventional AIRM. The frame M-step
is routed through AdamW by the committed gate at the recorded SHAs, subject to the dirty-provenance caveat, and the decode optimizer is separate. Any future claim
that the frame conditioner is Fisher, K-FAC, or reparameterization invariant
would require a statistical frame family and a derivation of its Fisher matrix.
Likewise, changing an order-Rényi discrepancy changes its local Fisher scale but
does not sweep Amari alpha-connections. Fisher-equals-Gauss–Newton statements
still require the output-distribution and loss-matching hypotheses specified by
[[martens-2020-natural-gradient-insights]].

For the frame route, the immediate empirical gap is now a matched optimizer study: preserve the
same K=10 model and outer objective, compare AdamW against the registered pullback learning-rate
grid, and carry only surviving settings to multiple seeds. Until that control is complete, the
current negative signal supports AdamW as the default without establishing that tuned group descent
is intrinsically inferior. [[2026-07-18-phi-pullback-group-k10-partial-negative-result]]

## Sources synthesized

- [[amari-1998-natural-gradient]] — the natural gradient as inverse-Fisher-preconditioned, Fisher-efficient, reparameterization-invariant descent.
- [[amari-2000-methods-information-geometry]] — the Fisher metric, dual/alpha-connections, and dually-flat exponential-family geometry for Amari divergences; order-Rényi is distinct.
- [[martens-2020-natural-gradient-insights]] — Fisher/Generalized Gauss–Newton relation under matching output-distribution and loss conditions; damping.
- [[martens-2015-kfac]] — Kronecker-factored neural-network Fisher approximation; no frame-Fisher or frame-K-FAC identification follows for this model.
- [[ollivier-2015-riemannian-metrics-nn]] — Fisher-based invariant training metrics for neural nets (full, unitwise, quasi-diagonal), the block-preconditioning ancestor.
- [[khan-rue-2023-bayesian-learning-rule]] — natural-gradient descent on exponential-family natural parameters as one learning rule unifying Adam, Newton, VI, and online learning; the program's Fisher-preconditioned Gaussian belief update.
- [[zhang-2004-divergence-duality-convex]] — convex-analytic construction of the alpha-divergence family from one potential, with a common Fisher metric, dual alpha-connections, and KL recovered at alpha = ±1.
- [[li-turner-2016-renyi-vi]] — the variational Renyi bound interpolating from the ELBO toward the log marginal likelihood.
- [[vanerven-2014-renyi-kl]] — definitive survey of order-alpha Renyi divergence with KL as the alpha to 1 limit.
- [[bogacz-2017-free-energy-tutorial]] — precision-weighted ordinary-gradient Gaussian free-energy updates; comparison material, not an equality with the deployed natural-gradient filter.
- [[petz-1996-monotone-metrics]] — classification of a non-unique family of monotone metrics on quantum states, replacing classical Fisher uniqueness.
- [[reginatto-1998-fisher-quantum]] — derivation of the Schrodinger equation from a Fisher-information variational principle, tying quantum dynamics to information geometry.
- [[jaynes-1957-information-statistical-mechanics]] — the maximum-entropy foundation of statistical mechanics, the information-theoretic root of the exponential-family geometry used here.
- [[nielsen-2020-elementary-introduction-information-geometry]] — pedagogical grounding for KL geometry and Gaussian belief natural gradients. [[gl-k-attention-2026-07-09-review-revision]]
- [[cover-thomas-2006-elements-information-theory]] — defines entropy, KL/relative entropy, and mutual information underpinning the free-energy KL and attention-entropy terms.

## See also

- [[Quantum information geometry]] — the noncommutative extension of the Fisher-Rao metric, where the uniqueness theorem becomes Petz's family of monotone metrics.
- [[Physics from Fisher information]] — physical laws recovered from Fisher-information variational principles.
- [[Information bottleneck]] — the rate-distortion / information-theoretic view of representation learning, adjacent to the maximum-entropy and divergence machinery here.
