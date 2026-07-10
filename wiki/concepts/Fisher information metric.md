---
type: concept
title: Fisher information metric
aliases:
  - Fisher information
  - Fisher information matrix
  - FIM
  - Fisher-Rao metric
  - "Fisher Metric"
  - "Fisher metric"
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-07-10
---

# Fisher information metric

## Definition

The **Fisher information metric** is the Riemannian metric that the space of probability distributions carries when each distribution is regarded as a point on a smooth manifold. Consider a parametric family of densities $p(x \mid \theta)$ indexed by a parameter vector $\theta \in \mathbb{R}^n$. The **Fisher information matrix** at $\theta$ is

$$
F(\theta)_{ij} = \mathbb{E}_{p(x\mid\theta)}\left[ \partial_i \log p(x\mid\theta)\partial_j \log p(x\mid\theta) \right]
= -\mathbb{E}_{p(x\mid\theta)}\left[ \partial_i\partial_j \log p(x\mid\theta) \right],
$$

where $\partial_i = \partial/\partial\theta_i$ and the score is $\partial_i \log p$. The two expressions agree under mild regularity conditions. $F(\theta)$ is symmetric and positive semi-definite, and where it is positive definite it defines an inner product on each tangent space, $\langle u, v\rangle_\theta = u^\top F(\theta) v$. This collection of inner products is the Fisher information metric, also called the **Fisher-Rao metric**.

Its defining virtue is that it is *intrinsic*: the metric measures distances between distributions, not between coordinate values, so it is invariant under smooth reparameterizations of $\theta$. Infinitesimally it is the second-order term of the Kullback-Leibler divergence — $\mathrm{KL}\big(p_\theta \| p_{\theta+d\theta}\big) = \tfrac{1}{2}d\theta^\top F(\theta) d\theta + o(\|d\theta\|^2)$ — which is why the Fisher metric is the unique (up to scale) metric compatible with the statistical structure of the manifold. This grounding in information geometry is developed canonically by [[amari-2000-methods-information-geometry]].

## Why it matters here

The exact Fisher-geometric claim in the VFE transformer concerns its Gaussian
belief family. Gauge frames and decoder parameters are separate parameter
spaces and do not acquire a Fisher metric merely because they participate in
the same training schedule.

First, **belief optimization**. The online Gaussian belief update uses the belief-family Fisher metric. The frame M-step is separate and is not an identified Fisher natural gradient. [[gl-k-attention-2026-07-09-review-revision]]

Second, **the divergence family**. A smooth divergence induces a local quadratic
form proportional to Fisher information, but the proportionality can depend on
the convention and order. In the standard order-Rényi convention, the local
Hessian carries an order-dependent positive factor. Nonlinear monotone
transforms preserve value ordering, not gradients, Hessians, affine connections,
or global geometry. Amari's [[Alpha-divergence]] and order-[[Renyi divergence]]
must therefore remain distinct.

> [!note] Editorial (2026-07-10): the frame conditioner is not the Fisher metric,
> and its positive Frobenius form is not full-$\mathrm{GL}(K)$
> adjoint-invariant. Belief Fisher geometry and frame conditioning must remain
> separate. [[gl-k-attention-2026-07-09-review-revision]]

## Details

**Exponential families and dual flatness.** For an exponential family written in
natural parameters, the Fisher information equals the Hessian of the
log-partition function. The Gaussian belief family is exponential, and its full
joint mean-covariance Fisher–Rao geometry is treated by
[[skovgaard-1984-riemannian-geometry-normal-model]]. Amari's alpha-connections
and alpha-divergences describe a dualistic structure on statistical manifolds.
The configured order-Rényi discrepancy is related at the level of a power
integral but does not inherit those connections through a nonlinear monotone
change of divergence value.

**Fisher as curvature, and as Gauss–Newton.**
[[martens-2020-natural-gradient-insights]] relates Fisher and Generalized
Gauss–Newton matrices under specified output-distribution and loss conditions.
This motivates damping in those settings, but the identity is not automatic for
an arbitrary objective and has not been established for the frame M-step.

**Tractable approximations.** K-FAC and related Fisher approximations remain valid general methods. No audited derivation identifies the transformer's frame conditioner with a K-FAC block or a frame Fisher matrix. [[gl-k-attention-2026-07-09-review-revision]]

**Relation to Riemannian optimization.** On a statistical manifold the Fisher
metric defines geodesics, while retractions and vector transports provide local
surrogates as formalized by [[absil-2008-optimization-matrix-manifolds]]. The
convergence result of [[bonnabel-2013-riemannian-sgd]] applies under its stated
assumptions and does not transfer automatically to every configured update. The
SPD-covariance side uses an affine-invariant metric on positive-definite
matrices.

**Quantum extension and a physical reading.** The classical Fisher metric has a quantum counterpart — the [[Quantum information geometry|quantum Fisher information]] — whose statistical-distance origin traces to [[wootters-1981-statistical-distance]], whose canonical form for pure-state estimation is the Bures/SLD metric of [[braunstein-caves-1994-quantum-fisher]], and which sits within the monotone-metric classification of [[petz-1996-monotone-metrics]] over the [[uhlmann-1976-transition-probability]] fidelity. A complementary strand, [[Physics from Fisher information]], runs the implication the other way: [[frieden-1998-physics-fisher]] and [[reginatto-1998-fisher-quantum]] derive dynamical laws (including the Schrodinger equation) from extremizing Fisher information, the same variational template that recurs when [[parr-2020-markov-blankets-thermodynamics]] casts free-energy minimization in thermodynamic terms.

> [!note] Editorial (2026-07-10): For zero-mean Gaussians, the covariance Fisher
> metric is one-half the conventional affine-invariant SPD metric,
> $g_\Sigma(U,V)=\tfrac12\operatorname{tr}(\Sigma^{-1}U\Sigma^{-1}V)$. The
> constant factor preserves geodesic paths but changes gradient scale. This
> covariance-only identity does not identify the full mean-covariance geometry
> or the gauge-frame optimizer with AIRM. [[gl-k-attention-2026-07-09-review-revision]]

## In this work

The Fisher information metric surfaces wherever the configuration declares an information-geometric or natural-gradient operation:

- **Frame updates.** These use a separate optimizer/optional conditioner and carry no Fisher or K-FAC identification. [[gl-k-attention-2026-07-09-review-revision]]
- **Belief (E-step) updates.** The per-token Gaussian beliefs are refined by natural-gradient / [[Natural gradient]] steps, whose metric is the Fisher information of the diagonal-Gaussian belief family.
- **Rényi objective.** The `divergence_family "renyi"` term is an order-Rényi
  pairwise discrepancy with KL at order one. Its local quadratic form is
  proportional to Fisher; it does not supply Amari alpha-connections or the
  Li–Turner variational bound.
- **SPD covariance geometry.** The `spd_affine` retraction operates under AIRM.
  On the zero-mean Gaussian covariance factor, Fisher is one-half conventional
  AIRM.

Blockwise frame conditioning should not be called Fisher preconditioning. The established Fisher metric is the one on the Gaussian belief family; optional gauge-frame conditioners are separate optimizer preconditioners. The audited frame table uses plain AdamW, with those conditioners and the heavy-ball field inactive. [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[amari-1998-natural-gradient]] — establishes the Fisher metric as the preconditioner of the natural (steepest-descent) gradient on a statistical manifold.
- [[amari-2000-methods-information-geometry]] — canonical treatment of the Fisher metric, dual connections, $\alpha$-connections, and dually flat exponential-family geometry.
- [[nielsen-2020-elementary-introduction-information-geometry]] — pedagogical grounding for KL geometry and Gaussian belief natural gradients. [[gl-k-attention-2026-07-09-review-revision]]
- [[cover-thomas-2006-elements-information-theory]] — defines entropy, KL/relative entropy, and mutual information underpinning the free-energy KL and attention-entropy terms.
- [[khan-rue-2023-bayesian-learning-rule]] — natural-gradient descent on exponential-family natural parameters as one learning rule unifying Adam, Newton, VI, and online learning; the Fisher-preconditioned Gaussian belief update.
- [[martens-2020-natural-gradient-insights]] — Fisher/Generalized Gauss–Newton relation under specified output-distribution and loss conditions; natural gradient as a curvature method.
- [[martens-2015-kfac]] — block-Kronecker approximation of neural-network Fisher matrices; no frame-Fisher or frame-K-FAC identification is asserted here.
- [[ollivier-2015-riemannian-metrics-nn]] — family of Fisher-based, reparameterization-invariant training metrics for neural networks.
- [[zhang-2004-divergence-duality-convex]] — an $\alpha$-divergence family built from one convex potential, each inducing a common Fisher-type metric plus dual $\alpha$-connections, recovering Bregman/KL at $\alpha=\pm1$.
- [[skovgaard-1984-riemannian-geometry-normal-model]] — Fisher-Rao Riemannian geometry of the full Gaussian model (mean and covariance jointly), with geodesic ODEs and Rao distance for the $(\mu,\Sigma)$ manifold.
- [[vanerven-2014-renyi-kl]], [[li-turner-2016-renyi-vi]] — respectively order-Rényi divergence and the variational Rényi bound; neither is Amari's alpha-connection construction.
- [[pennec-2006-affine-invariant-tensor]] — affine-invariant SPD metric; the zero-mean Gaussian covariance Fisher metric is one-half this conventional AIRM.
- [[absil-2008-optimization-matrix-manifolds]], [[bonnabel-2013-riemannian-sgd]] — retractions and Riemannian SGD for moving under a manifold metric.
- [[wootters-1981-statistical-distance]] — statistical distance between quantum states, the origin of the quantum Fisher metric.
- [[braunstein-caves-1994-quantum-fisher]] — symmetric-logarithmic-derivative / Bures quantum Fisher information as the bound on quantum parameter estimation.
- [[petz-1996-monotone-metrics]] — classification of monotone (contractive) Riemannian metrics on quantum states, the quantum analogue of the Fisher uniqueness theorem.
- [[uhlmann-1976-transition-probability]] — transition probability / fidelity underlying the Bures geometry of quantum states.
- [[frieden-1998-physics-fisher]] — derivation of physical laws by extremizing Fisher information (extreme physical information).
- [[reginatto-1998-fisher-quantum]] — the Schrodinger equation obtained from a Fisher-information variational principle.
- [[parr-2020-markov-blankets-thermodynamics]] — free-energy minimization read thermodynamically, the same extremal-information template applied to self-organizing systems.

## See also

- [[Natural gradient]]
- [[Renyi divergence]]
- [[Alpha-divergence]]
- [[Variational free energy]]
- [[Evidence lower bound (ELBO)]]
- [[Information geometry and natural gradient]]
- [[SPD-manifold geometry and Riemannian optimization]]
- [[Quantum information geometry]]
- [[Physics from Fisher information]]
