---
type: concept
title: Fisher information metric
aliases:
  - Fisher information
  - Fisher information matrix
  - FIM
  - Fisher-Rao metric
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Fisher information metric

## Definition

The **Fisher information metric** is the Riemannian metric that the space of probability distributions carries when each distribution is regarded as a point on a smooth manifold. Consider a parametric family of densities $p(x \mid \theta)$ indexed by a parameter vector $\theta \in \mathbb{R}^n$. The **Fisher information matrix** at $\theta$ is

$$
F(\theta)_{ij} \;=\; \mathbb{E}_{p(x\mid\theta)}\!\left[\, \partial_i \log p(x\mid\theta)\,\partial_j \log p(x\mid\theta) \,\right]
\;=\; -\,\mathbb{E}_{p(x\mid\theta)}\!\left[\, \partial_i\partial_j \log p(x\mid\theta) \,\right],
$$

where $\partial_i = \partial/\partial\theta_i$ and the score is $\partial_i \log p$. The two expressions agree under mild regularity conditions. $F(\theta)$ is symmetric and positive semi-definite, and where it is positive definite it defines an inner product on each tangent space, $\langle u, v\rangle_\theta = u^\top F(\theta)\, v$. This collection of inner products is the Fisher information metric, also called the **Fisher-Rao metric**.

Its defining virtue is that it is *intrinsic*: the metric measures distances between distributions, not between coordinate values, so it is invariant under smooth reparameterizations of $\theta$. Infinitesimally it is the second-order term of the Kullback-Leibler divergence — $\mathrm{KL}\big(p_\theta \,\|\, p_{\theta+d\theta}\big) = \tfrac{1}{2}\,d\theta^\top F(\theta)\, d\theta + o(\|d\theta\|^2)$ — which is why the Fisher metric is the unique (up to scale) metric compatible with the statistical structure of the manifold. This grounding in information geometry is developed canonically by [[amari-2000-methods-information-geometry]].

## Why it matters here

The VFE transformer treats every internal quantity as living on a statistical or geometric manifold rather than in flat Euclidean coordinates, and the Fisher information metric is the object that supplies the *correct local geometry* for moving on those manifolds. Two model components depend on it directly.

First, **optimization**. Steepest descent in raw parameter coordinates depends arbitrarily on how the model happens to be parameterized. [[amari-1998-natural-gradient]] showed that the true steepest-descent direction on a statistical manifold is the ordinary gradient *preconditioned by the inverse Fisher metric*, $F^{-1}\nabla\mathcal{L}$ — the [[Natural gradient]]. The VFE transformer's M-step (parameter update) and its online belief updates are natural-gradient steps, so the Fisher metric is the preconditioner that makes those updates reparameterization-invariant and statistically efficient.

Second, **the divergence family**. The model's training objective uses a [[Renyi divergence]] / [[Alpha-divergence]] family, and the Fisher metric is exactly the common second-order limit shared by every member of that family (KL, the $\alpha$-divergences, the Renyi orders): all of them induce the *same* Fisher-Rao geometry infinitesimally, differing only in their higher-order, "dual" structure. This is why a single metric coherently underlies an objective that interpolates across $\alpha$.

> [!note] Editorial: The architecture's [[Killing form|Killing-form]] per-block preconditioning on the GL(k) gauge group plays the structural role that the Fisher metric plays on the statistical manifold — a natural, group-intrinsic inner product used to precondition updates. The two are conceptually parallel "right metrics," one from information geometry and one from Lie-group geometry, and the model uses both side by side.

## Details

**Exponential families and dual flatness.** For an exponential family written in natural parameters, the Fisher information equals the Hessian of the log-partition function, making the manifold *dually flat*: it carries two flat affine connections (the $e$-connection and $m$-connection) that are mutually dual with respect to the Fisher metric. The Gaussian beliefs $(\mu, \Sigma)$ that the model maintains per token are exponential-family distributions, so their belief space is precisely such a dually flat manifold. The family of [[amari-2000-methods-information-geometry]] $\alpha$-connections interpolates between these duals and is the geometric backbone of the alpha/Renyi machinery.

**Fisher as curvature, and as Gauss-Newton.** [[martens-2020-natural-gradient-insights]] recasts the natural gradient as a second-order method in which the Fisher matrix coincides with the Generalized Gauss-Newton matrix and stands in for the Hessian. This gives the metric an optimization reading — it is a positive semi-definite curvature surrogate — and motivates the damping and trust-region heuristics used when $F$ is near-singular.

**Tractable approximations.** The full Fisher matrix is $n \times n$ in the parameter count and cannot be inverted directly for large models. [[martens-2015-kfac]] (K-FAC) approximates it as a block of Kronecker products, one block per layer, so that inversion factorizes. This block structure is the practical template for the VFE transformer's **per-block GL(k) Fisher preconditioning**: the gauge group decomposes parameters into $k\times k$ blocks, and each block carries its own metric to be inverted independently. [[ollivier-2015-riemannian-metrics-nn]] derives a graded family of Fisher-based, reparameterization-invariant metrics for neural networks — full, backpropagated, unitwise, and quasi-diagonal — that name exactly the spectrum of approximations between the intractable full metric and a cheap diagonal one.

**Relation to Riemannian optimization.** On the parameter and belief manifolds the Fisher metric defines geodesics, but exact geodesic steps are expensive; first-order surrogates (retractions and vector transports) stand in for them, as formalized by [[absil-2008-optimization-matrix-manifolds]], with almost-sure convergence guarantees for the stochastic case given by [[bonnabel-2013-riemannian-sgd]]. The SPD-covariance side of the model uses an *affine-invariant* Riemannian metric on the cone of positive-definite matrices.

**Quantum extension and a physical reading.** The classical Fisher metric has a quantum counterpart — the [[Quantum information geometry|quantum Fisher information]] — whose statistical-distance origin traces to [[wootters-1981-statistical-distance]], whose canonical form for pure-state estimation is the Bures/SLD metric of [[braunstein-caves-1994-quantum-fisher]], and which sits within the monotone-metric classification of [[petz-1996-monotone-metrics]] over the [[uhlmann-1976-transition-probability]] fidelity. A complementary strand, [[Physics from Fisher information]], runs the implication the other way: [[frieden-1998-physics-fisher]] and [[reginatto-1998-fisher-quantum]] derive dynamical laws (including the Schrodinger equation) from extremizing Fisher information, the same variational template that recurs when [[parr-2020-markov-blankets-thermodynamics]] casts free-energy minimization in thermodynamic terms.

> [!note] Editorial: That the affine-invariant SPD metric *is* the Fisher metric of the zero-mean Gaussian family — tying the [[pennec-2006-affine-invariant-tensor]] covariance geometry back to the same information-geometric source — is a bridge this wiki draws; the cited sources do not state the identity explicitly (see [[pennec-2006-affine-invariant-tensor]]).

## In this work

The Fisher information metric surfaces wherever the configuration declares an information-geometric or natural-gradient operation:

- **M-step preconditioning.** Parameter updates are preconditioned by a (blockwise) Fisher metric, realized as the Killing-form / per-block GL(k) preconditioner — the K-FAC-style block-Kronecker template of [[martens-2015-kfac]] applied to the gauge blocks.
- **Belief (E-step) updates.** The per-token Gaussian beliefs are refined by natural-gradient / [[Natural gradient]] steps, whose metric is the Fisher information of the diagonal-Gaussian belief family.
- **Renyi/alpha objective.** The `divergence_family "renyi"` loss and its $\alpha$-connections share the Fisher metric as their common infinitesimal limit, with KL recovered as $\alpha \to 1$ ([[vanerven-2014-renyi-kl]], [[li-turner-2016-renyi-vi]]).
- **SPD covariance geometry.** The `spd_affine` retraction operates under the affine-invariant metric, which is the Gaussian Fisher metric on the covariance factor.

The reference block-GL(k) configuration with $k=20$ (see [[VFE Transformer Program]]) is where the per-block Fisher preconditioning becomes concrete: the metric is inverted one $20\times20$ gauge block at a time rather than across the full parameter vector.

## Sources

- [[amari-1998-natural-gradient]] — establishes the Fisher metric as the preconditioner of the natural (steepest-descent) gradient on a statistical manifold.
- [[amari-2000-methods-information-geometry]] — canonical treatment of the Fisher metric, dual connections, $\alpha$-connections, and dually flat exponential-family geometry.
- [[martens-2020-natural-gradient-insights]] — Fisher matrix as Generalized Gauss-Newton / curvature surrogate; natural gradient as a second-order method.
- [[martens-2015-kfac]] — block-Kronecker approximation of the Fisher matrix, template for per-block GL(k) preconditioning.
- [[ollivier-2015-riemannian-metrics-nn]] — family of Fisher-based, reparameterization-invariant training metrics for neural networks.
- [[vanerven-2014-renyi-kl]], [[li-turner-2016-renyi-vi]] — the Renyi/alpha family whose common second-order limit is the Fisher metric.
- [[pennec-2006-affine-invariant-tensor]] — affine-invariant SPD metric, the Gaussian Fisher metric on covariances.
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
