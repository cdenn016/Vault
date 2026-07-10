---
type: concept
title: Natural gradient
aliases:
  - Natural gradient descent
  - Fisher-preconditioned gradient
  - NGD
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-07-10
---

# Natural gradient

## Definition

The **natural gradient** is the direction of steepest descent of a loss function when the parameter space is treated not as flat Euclidean space but as a Riemannian manifold whose metric is the [[Fisher information metric]]. Concretely, for a loss $L(\theta)$ over parameters $\theta$ that index a family of probability distributions $p_\theta$, the ordinary (Euclidean) gradient $\nabla L$ answers "which way increases $L$ fastest per unit change in the *coordinates* $\theta$" — an answer that depends on how the model happens to be parameterized. The natural gradient instead measures distance in *distribution space* using the Fisher metric $F(\theta)$, and the steepest-descent direction becomes

$$\tilde\nabla L(\theta) = F(\theta)^{-1}\nabla L(\theta).$$

The defining property, established by [[amari-1998-natural-gradient]], is that
the natural-gradient tangent vector is coordinate invariant: a smooth change of
coordinates transforms $F$ and $\nabla L$ in compensating ways. An exact flow
therefore describes the same distribution-space direction. A finite Euler step
is not automatically invariant, because its result also depends on step size
and the chosen integration or retraction map.

## Why it matters here

Natural-gradient claims apply to the Gaussian belief mean/covariance updates, whose statistical family has a Fisher metric. At each recorded source SHA, the committed gate and stored configuration route the audited frame table through AdamW on the outer objective; dirty provenance prevents byte-level reconstruction. Heavy-ball belongs only to the disabled custom outer frame optimizer, BCH/retraction only to disabled in-E-step revision, and the optional Cartan/Killing or exponential-pullback conditioner would not thereby be Fisher, reparameterization invariant, or gauge invariant if enabled. [[gl-k-attention-2026-07-09-review-revision]]

These invariance and efficiency properties hold when the actual Fisher metric of a statistical family is used. They support belief-side updates, not a frame update identified only by analogy. [[gl-k-attention-2026-07-09-review-revision]]

## Details

For a model $p_\theta(x)$, the Fisher information matrix is the expected outer product of the score, $F(\theta) = \mathbb{E}_{p_\theta}\big[\nabla_\theta \log p_\theta \nabla_\theta \log p_\theta^{\top}\big]$, and it is the unique (up to scale) metric on the manifold of distributions invariant under sufficient statistics — the foundational result of [[Fisher information metric]] and the broader apparatus catalogued in [[amari-2000-methods-information-geometry]]. The natural gradient $F^{-1}\nabla L$ is then the Riemannian gradient under this metric.

Several complementary readings of the same object guide the implementation:

- **Second-order view.** [[martens-2020-natural-gradient-insights]] relates the
  Fisher matrix to the Generalized Gauss–Newton matrix under specified
  model-output and loss conditions. Those conditions are general background;
  they have not been established for the frame objective or its conditioner.
- **Tractability via factorization.** The full Fisher matrix is $O(d^2)$ to form
  and $O(d^3)$ to invert. [[martens-2015-kfac]] makes neural-network natural
  gradients tractable by a Kronecker factorization. The transformer's
  block structure does not by itself identify its frame conditioner as K-FAC
  or as an approximation to any frame Fisher matrix.
- **Metric families for nets.** [[ollivier-2015-riemannian-metrics-nn]] derives a spectrum of Fisher-based, reparameterization-invariant training metrics for feedforward networks — full, backpropagated, unitwise, and quasi-diagonal — clarifying how much of the metric one must retain to keep invariance while staying cheap, and supplying the information-geometric counterpart to the model's block-structured updates.
- **Manifold connection.** Natural-gradient steps are Riemannian optimization
  on a statistical manifold. [[absil-2008-optimization-matrix-manifolds]] and
  [[boumal-2023-optimization-smooth-manifolds]] provide general retraction and
  transport machinery, while [[bonnabel-2013-riemannian-sgd]] gives convergence
  under its stated stochastic assumptions. Those results do not automatically
  grant convergence to the deployed finite-step covariance update or to the
  separate plain-AdamW gauge-frame update.

A divergence can induce a local Fisher metric without transferring all of its
global geometry. The configured `renyi` family is an order-$\alpha$ pairwise
discrepancy studied in [[vanerven-2014-renyi-kl]]. The Li–Turner variational
Rényi bound and Amari's alpha-divergences with their alpha-connections are
distinct constructions. A nonlinear monotone relation between divergence
values does not preserve gradients, Hessians, or affine connections, and a
smooth order-Rényi member recovers Fisher locally only up to an order-dependent
positive scale.

> [!note] Editorial (2026-07-10): The joint Gaussian belief update uses Fisher
> geometry; its covariance block is one-half conventional AIRM. The architecture
> also uses a configurable order-Rényi pairwise discrepancy.
> It does not sweep Amari alpha-connections, and the audited frame table remains
> on plain AdamW. [[gl-k-attention-2026-07-09-review-revision]]

## In this work

Natural gradient surfaces wherever the VFE transformer optimizes a distribution:

- **Frame M-step.** The committed gate at each recorded SHA routes the frame table through AdamW, subject to the dirty-provenance caveat. Optional per-block conditioning and heavy-ball are inactive fields, not an identified Fisher/K-FAC natural gradient; the BCH retraction dispatcher is a separate optional in-E-step route. [[gl-k-attention-2026-07-09-review-revision]]
- **E-step / online belief updates.** The per-token Gaussian beliefs $(\mu,\Sigma)$ are refined with the belief-family Fisher geometry. [[khan-rue-2023-bayesian-learning-rule]] supplies a related exponential-family natural-parameter update, but it does not identify the entire program or its separate decode/frame M-steps with one Bayesian learning rule. Adaptive-optimizer cautions must therefore be assessed per optimizer rather than transferred from the belief update to every channel. [[gl-k-attention-2026-07-09-review-revision]]
- **SPD covariance geometry.** The covariance $\Sigma$ lives on the SPD
  manifold under the `spd_affine` retraction. For a zero-mean Gaussian, the
  covariance block of the Fisher metric is one-half the conventional AIRM; the
  constant factor changes gradient scale but not the underlying geodesic paths.
  This covariance-only statement must not be extended to the full joint
  mean-covariance manifold or to gauge frames. Spectral differentiation and its
  repeated-eigenvalue hazards are treated in
  [[ionescu-2015-matrix-backpropagation]], and the SPD cone as a symmetric space
  is developed in [[Symmetric spaces and the SPD cone]].
- **Invariance as a design principle.** The exact natural-gradient vector field
  is coordinate invariant on a specified statistical manifold. Finite discrete
  trajectories also depend on step size and the chosen integration or retraction
  scheme. This statistical-coordinate statement is an analogy to gauge
  invariance, not a proof of the model's gauge equivariance.

The operative natural-gradient claim in the reference configuration is the Gaussian belief update, not per-block Fisher preconditioning of the frame M-step. [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[amari-1998-natural-gradient]] — the natural gradient as Fisher-preconditioned steepest descent; reparameterization invariance and Fisher efficiency.
- [[amari-2000-methods-information-geometry]] — Fisher metric and Amari alpha-connections; order-Rényi divergence is a distinct family.
- [[martens-2020-natural-gradient-insights]] — natural gradient as a Gauss–Newton-related curvature method under matching output/loss conditions; damping.
- [[martens-2015-kfac]] — Kronecker-factored Fisher approximation as general background; no frame-Fisher identification is asserted here. [[gl-k-attention-2026-07-09-review-revision]]
- [[ollivier-2015-riemannian-metrics-nn]] — families of Fisher-based, invariant metrics for neural networks.
- [[absil-2008-optimization-matrix-manifolds]] — retractions and vector transports for the Riemannian realization of natural-gradient steps.
- [[bonnabel-2013-riemannian-sgd]] — convergence of stochastic Riemannian descent.
- [[li-turner-2016-renyi-vi]], [[vanerven-2014-renyi-kl]] — respectively the variational Rényi bound and order-Rényi divergence; both recover KL-related limits but are not interchangeable.
- [[sra-hosseini-2015-conic-geometric-optimization]] — conic geometric optimization on the SPD cone as a symmetric space; geodesic convexity and affine-invariant descent.
- [[nielsen-2020-elementary-introduction-information-geometry]] — pedagogical grounding for KL geometry and Gaussian belief natural gradients. [[gl-k-attention-2026-07-09-review-revision]]
- [[martens-2010-hessian-free-optimization]] — truncated-Newton background; no audited frame-Fisher M-step is inferred.

## See also

- [[Fisher information metric]]
- [[Variational EM]]
- [[Variational free energy]]
- [[Renyi divergence]]
- [[Alpha-divergence]]
- [[Precision weighting]]
- [[Prediction error]]
- [[Gauge transformation]]
- [[Information geometry and natural gradient]]
- [[SPD-manifold geometry and Riemannian optimization]]
- [[Physics from Fisher information]]
- [[Symmetric spaces and the SPD cone]]

## Related sources (ingested 2026-06-20)

- [[kingma-ba-2015-adam]] — Adaptive first-order optimizer;
- [[loshchilov-hutter-2019-adamw]] — Decoupled weight decay;
- [[yang-2022-tensor-programs-v-mup]] — muP (maximal-update parametrization): width-stable init and learning-rate scaling, bearing on whether $\phi$/$\sigma$ init and $\kappa$ in $\tau=\kappa\sqrt{\dim_h}$ transfer across the K-sweep;
