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
updated: 2026-06-19
---

# Natural gradient

## Definition

The **natural gradient** is the direction of steepest descent of a loss function when the parameter space is treated not as flat Euclidean space but as a Riemannian manifold whose metric is the [[Fisher information metric]]. Concretely, for a loss $L(\theta)$ over parameters $\theta$ that index a family of probability distributions $p_\theta$, the ordinary (Euclidean) gradient $\nabla L$ answers "which way increases $L$ fastest per unit change in the *coordinates* $\theta$" — an answer that depends on how the model happens to be parameterized. The natural gradient instead measures distance in *distribution space* using the Fisher metric $F(\theta)$, and the steepest-descent direction becomes

$$\tilde\nabla L(\theta) \;=\; F(\theta)^{-1}\,\nabla L(\theta).$$

The defining property, established by [[amari-1998-natural-gradient]], is that this preconditioned direction is **reparameterization-invariant**: a smooth change of coordinates $\theta \mapsto \psi(\theta)$ transforms $F$ and $\nabla L$ in exactly compensating ways, so the resulting *update to the distribution* is unchanged. The Euclidean gradient lacks this property — it is an artifact of the chosen coordinates, whereas the natural gradient follows the geometry of the statistical model itself.

## Why it matters here

The VFE transformer is, at every level, an optimizer over *statistical objects* — per-token Gaussian beliefs $(\mu,\Sigma)$ in the E-step and distribution-defining parameters in the M-step (see [[Variational EM]]). Because both steps move probability distributions rather than arbitrary vectors, the meaningful notion of "steepest descent" on the free-energy objective is the natural one, not the coordinate-bound Euclidean one. This is the central reason information geometry, and not merely vanilla gradient descent, sits at the architecture's core: the model declares a `gradient_mode` of filtering and learns by descending [[Variational free energy]], and natural-gradient preconditioning is what makes that descent invariant to how $\mu$, $\Sigma$, and the gauge parameters $\phi$ are coordinatized.

The payoff is threefold. First, **invariance**: the same logical update results whether a covariance is stored as $\Sigma$, as its Cholesky factor, or in log-Euclidean coordinates — a property the project relies on when moving beliefs between the curved SPD chart and tangent space. Second, **conditioning**: by dividing out the Fisher metric, natural gradient corrects the wildly different curvatures of the belief manifold, so that, e.g., a unit step in a near-degenerate $\Sigma$ direction is scaled appropriately. Third, **efficiency**: Amari's analysis shows the natural gradient achieves the asymptotically optimal (Fisher-efficient) convergence rate for online learning. These three properties are precisely what the M-step needs to update GL(k) gauge blocks and SPD covariances stably.

## Details

For a model $p_\theta(x)$, the Fisher information matrix is the expected outer product of the score, $F(\theta) = \mathbb{E}_{p_\theta}\!\big[\nabla_\theta \log p_\theta \,\nabla_\theta \log p_\theta^{\top}\big]$, and it is the unique (up to scale) metric on the manifold of distributions invariant under sufficient statistics — the foundational result of [[Fisher information metric]] and the broader apparatus catalogued in [[amari-2000-methods-information-geometry]]. The natural gradient $F^{-1}\nabla L$ is then the Riemannian gradient under this metric.

Several complementary readings of the same object guide the implementation:

- **Second-order view.** [[martens-2020-natural-gradient-insights]] shows that for the common losses used here the Fisher matrix coincides with the *Generalized Gauss-Newton* matrix, so natural gradient is effectively a curvature (second-order) method substituting $F$ for the Hessian. This justifies damping and trust-region treatments when $F$ is ill-conditioned.
- **Tractability via factorization.** The full Fisher matrix is $O(d^2)$ to form and $O(d^3)$ to invert. [[martens-2015-kfac]] (K-FAC) approximates $F$ as a block Kronecker product, making natural-gradient training feasible at scale; this is the direct template for the project's *per-block* Fisher preconditioning, applied one GL(k) block at a time rather than across the whole parameter vector.
- **Metric families for nets.** [[ollivier-2015-riemannian-metrics-nn]] derives a spectrum of Fisher-based, reparameterization-invariant training metrics for feedforward networks — full, backpropagated, unitwise, and quasi-diagonal — clarifying how much of the metric one must retain to keep invariance while staying cheap, and supplying the information-geometric counterpart to the model's block-structured updates.
- **Manifold connection.** Performing natural-gradient steps is formally Riemannian optimization on the statistical manifold; the retraction-based machinery of [[absil-2008-optimization-matrix-manifolds]] — and its computation-forward successor [[boumal-2023-optimization-smooth-manifolds]], which makes second-order retraction error and step conditioning on the SPD and Stiefel manifolds explicit enough to assess whether `spd_affine` and GL(k) BCH steps stay well-conditioned in fp32 — together with the convergence theory of [[bonnabel-2013-riemannian-sgd]] (Riemannian SGD) provide the stepping rule and almost-sure convergence guarantee that the same updates inherit when applied to SPD covariances and gauge parameters.

A key generalization in this work is that the divergence underlying the metric need not be the KL divergence. The architecture's `divergence_family` is `renyi`, an order-$\alpha$ family ([[Renyi divergence]], [[Alpha-divergence]]) studied in [[vanerven-2014-renyi-kl]] and exploited as a variational objective by [[li-turner-2016-renyi-vi]]. In the information geometry of [[amari-2000-methods-information-geometry]], varying $\alpha$ selects among the **alpha-connections** — a one-parameter family of dual affine connections — with the Fisher metric held fixed and KL recovered as the $\alpha\to 1$ limit. The natural gradient is the gradient with respect to this fixed Fisher metric; the $\alpha$ parameter shapes *which* divergence is being minimized along that geometry rather than the metric itself.

> [!note] Editorial: The registry sources establish (i) the natural gradient and Fisher metric, (ii) the Renyi/alpha-divergence family with KL as its limit, and (iii) the alpha-connections of information geometry separately. The synthesis that the model fixes the Fisher metric while sweeping $\alpha$ over connections is the consistent reading of those three facts for this architecture, not a claim made verbatim in any single source.

## In this work

Natural gradient surfaces wherever the VFE transformer optimizes a distribution:

- **M-step parameter updates.** The block GL(k) gauge group means parameters are organized into blocks; following [[martens-2015-kfac]], each block carries its own Fisher ([[Killing form|Killing-form]]) preconditioner, so the M-step is a *per-block natural-gradient* step rather than a global one. This is the practical realization of "Killing-form per-block preconditioning" in the config.
- **E-step / online belief updates.** The per-token Gaussian beliefs $(\mu,\Sigma)$ are refined by descending free energy; because $(\mu,\Sigma)$ parameterize a distribution, the Fisher-efficient online updates of [[amari-1998-natural-gradient]] are the correct form for these belief-relaxation steps, dovetailing with the precision-weighted error dynamics inherited from predictive coding ([[Prediction error]], [[Precision weighting]]). This is exactly the closed-form belief update of [[khan-rue-2023-bayesian-learning-rule]], whose Bayesian Learning Rule casts the whole program as natural-gradient descent on the natural parameters of an exponential-family posterior — reading the update off the expectation-parameter gradient and unifying Adam, Newton, and variational inference as special cases. Because both this E-step and the M-step are adaptive-preconditioner updates by construction with no LayerNorm module to lean on, the early-training variance pathology that [[liu-2020-variance-adaptive-radam]] diagnoses for adaptive learning rates — and fixes with warmup as variance reduction — is the relevant optimizer-side stability caution.
- **SPD covariance geometry.** The covariance $\Sigma$ lives on the SPD manifold under the `spd_affine` retraction; natural-gradient descent on the Gaussian belief and Riemannian descent on the SPD cone are two views of the same affine-invariant geometry (the Gaussian-Fisher = affine-invariant identity is flagged as editorial on [[Fisher information metric]]), with retractions and transports from [[absil-2008-optimization-matrix-manifolds]] standing in for exact geodesics. Differentiating the spectral operations these steps rely on (matrix-log, ReEig/LogEig) goes through the adjoint-matrix backpropagation of [[ionescu-2015-matrix-backpropagation]], whose eigendecomposition/SVD derivation exposes the eigenvalue-gap denominator $1/(\lambda_i-\lambda_j)$ that diverges to NaN when eigenvalues coincide — the precise `eigh`-backward failure mode the codebase pins for SPD operators. The SPD cone's status as a Riemannian symmetric space under this affine-invariant metric — and the conic-geometric optimization machinery that exploits it ([[sra-hosseini-2015-conic-geometric-optimization]]) — is developed in [[Symmetric spaces and the SPD cone]].
- **Invariance as a design principle.** The reparameterization invariance of the natural gradient is the optimization-side analogue of the model's gauge invariance: just as a [[Gauge transformation]] must leave physical content unchanged, the natural gradient leaves the learning trajectory unchanged under recoordinatization, a parallel made explicit in [[ollivier-2015-riemannian-metrics-nn]].

The reference $k=20$ block-GL(k) linear-mixing configuration (see [[VFE Transformer Program]]) exercises exactly this regime, in which per-block Fisher preconditioning of the M-step is the operative use of the natural gradient.

## Sources

- [[amari-1998-natural-gradient]] — the natural gradient as Fisher-preconditioned steepest descent; reparameterization invariance and Fisher efficiency.
- [[amari-2000-methods-information-geometry]] — Fisher metric, dual affine connections, and alpha-connections underlying both the natural gradient and the Renyi/alpha machinery.
- [[martens-2020-natural-gradient-insights]] — natural gradient as a Gauss-Newton / second-order method; damping.
- [[martens-2015-kfac]] — Kronecker-factored Fisher approximation; template for per-block GL(k) preconditioning.
- [[ollivier-2015-riemannian-metrics-nn]] — families of Fisher-based, invariant metrics for neural networks.
- [[absil-2008-optimization-matrix-manifolds]] — retractions and vector transports for the Riemannian realization of natural-gradient steps.
- [[bonnabel-2013-riemannian-sgd]] — convergence of stochastic Riemannian descent.
- [[li-turner-2016-renyi-vi]], [[vanerven-2014-renyi-kl]] — Renyi/alpha divergences and KL as the $\alpha\to1$ limit.
- [[sra-hosseini-2015-conic-geometric-optimization]] — conic geometric optimization on the SPD cone as a symmetric space; geodesic convexity and affine-invariant descent.
- [[nielsen-2020-elementary-introduction-information-geometry]] — pedagogical information-geometry survey grounding the KL divergences and the natural-gradient M-step.
- [[martens-2010-hessian-free-optimization]] — truncated-Newton (Hessian-free) antecedent of the curvature-aware Fisher M-step preconditioning lineage.

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
