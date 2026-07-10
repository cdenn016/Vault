---
type: concept
title: Reparameterization trick
aliases:
  - Pathwise gradient estimator
  - Stochastic backpropagation
  - Location-scale reparameterization
  - "rezende2014stochastic"
  - "rezende-2014-stochastic"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
status: draft
created: 2026-06-18
updated: 2026-07-10
---

# Reparameterization trick

## Definition

The **reparameterization trick** is a technique for obtaining low-variance, pathwise gradient estimates of an expectation taken under a parametric distribution, when those parameters are themselves what we wish to differentiate with respect to. Suppose we must compute the gradient with respect to parameters $\phi$ of an objective of the form $\mathbb{E}_{z \sim q_\phi(z)}[f(z)]$. Because the distribution $q_\phi$ over which the expectation is taken *depends* on $\phi$, the gradient cannot simply be pushed inside the expectation. The trick rewrites the random variable $z$ as a deterministic, differentiable transformation $z = g_\phi(\epsilon)$ of an auxiliary noise variable $\epsilon \sim p(\epsilon)$ whose distribution carries no dependence on $\phi$. The expectation then becomes $\mathbb{E}_{\epsilon \sim p(\epsilon)}[f(g_\phi(\epsilon))]$, and because the source of randomness $p(\epsilon)$ is now parameter-free, the gradient and expectation commute:

$$\nabla_\phi \mathbb{E}_{z \sim q_\phi}[f(z)] = \mathbb{E}_{\epsilon \sim p(\epsilon)}\big[\nabla_\phi f(g_\phi(\epsilon))\big].$$

The canonical instance is the Gaussian *location–scale* transform: to sample $z \sim \mathcal{N}(\mu, \Sigma)$ with $\Sigma = L L^\top$, write $z = \mu + L\epsilon$ where $\epsilon \sim \mathcal{N}(0, I)$. The mean $\mu$ and the Cholesky (or square-root) factor $L$ are now differentiable inputs to a sample, so a single Monte-Carlo draw of $\epsilon$ yields an unbiased gradient estimate by ordinary backpropagation through $g_\phi$. This estimator typically has far lower variance than the alternative score-function (REINFORCE / log-derivative) estimator, because it exploits the gradient information in $f$ rather than treating it as a black box.

## Why it matters here

The VFE transformer maintains a diagonal-Gaussian belief $(\mu,\Sigma)$ for every token. When a belief-side expectation is estimated by sampling, reparameterization makes that estimator differentiable with respect to the belief parameters. This statement concerns the belief objective only: the deployed decoder uses a separate cross-entropy objective, and the complete loop is not one ELBO. [[gl-k-attention-2026-07-09-review-revision]]

[[kingma-2013-auto-encoding-variational-bayes]] supplies the differentiable Gaussian-sampling method. The VFE transformer has no neural recognition network, so the connection is the estimator rather than the VAE architecture or its single-objective training theorem.

## Details

**Why the naive gradient fails.** Differentiating $\mathbb{E}_{q_\phi}[f(z)] = \int q_\phi(z) f(z)dz$ produces a term $\int \nabla_\phi q_\phi(z) f(z)dz$. The integrand is no longer an expectation under a probability density (it is a derivative of one), so a plain Monte-Carlo average of $f$ over samples does not estimate the gradient.

**Two unbiased estimators.**
- *Score-function (REINFORCE)* uses the identity $\nabla_\phi q_\phi = q_\phi \nabla_\phi \log q_\phi$ to write the gradient as $\mathbb{E}_{q_\phi}[f(z)\nabla_\phi \log q_\phi(z)]$. It is general (it needs only that $q_\phi$ be differentiable in $\phi$ and that we can evaluate $\log q_\phi$), but high variance.
- *Pathwise (reparameterization)* uses $z = g_\phi(\epsilon)$ and differentiates $f$ through $g_\phi$. It requires $f$ to be differentiable and $q_\phi$ to admit a differentiable sampler, but yields much lower variance because $\nabla f$ enters directly.

**The Gaussian case in detail.** For a diagonal Gaussian, $z_i = \mu_i + \sigma_i\epsilon_i$ with $\epsilon_i \sim \mathcal{N}(0,1)$, so $\partial z_i / \partial \mu_i = 1$ and $\partial z_i / \partial \sigma_i = \epsilon_i$. The KL / divergence term against a Gaussian prior often has a closed form and need not be sampled at all; only the data-fit (reconstruction / prediction-error) term is estimated by reparameterized sampling. This split is what gives the ELBO its characteristic low-variance gradient.

**Interaction with the covariance manifold.** Because $\Sigma$ lives on the SPD cone, the reparameterization must produce a valid factor $L$ with $\Sigma = LL^\top$, and gradients then flow into a parameterization of $\Sigma$ that respects positive-definiteness — a concern shared with the #cluster/spd-geometry machinery (the `spd_affine` retraction, the affine-invariant metric of [[pennec-2006-affine-invariant-tensor]], and the SPD calculus surveyed in [[bhatia-2007-positive-definite-matrices]]). Equivalently, one may parameterize through the matrix logarithm in the [[arsigny-2006-log-euclidean]] sense, sampling in a flat tangent coordinate and mapping back, which keeps the sampler differentiable while guaranteeing an SPD result.

**Relation to natural-gradient optimization.** The reparameterization trick produces a Euclidean gradient in chosen coordinates and is silent about parameter-space geometry. Belief-side Gaussian updates may then use the inverse [[Fisher information metric]] to obtain a [[Natural gradient]] ([[amari-1998-natural-gradient]]). This does not make the frame or decode M-step Fisher-natural; the audited frame table uses plain AdamW and leaves the configured geometric/heavy-ball frame path inactive. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Editorial (2026-07-10): The trick is a differentiation device, not an
> inference principle. It can estimate sampled expectations in many objectives,
> including the Li–Turner variational Rényi bound, but the transformer's
> configured pairwise order-Rényi term is a different construction and has a
> Gaussian closed form. [[gl-k-attention-2026-07-09-review-revision]]

**Variants.** Beyond the location–scale Gaussian: the *implicit* reparameterization extends the trick to distributions whose CDF, rather than whose sampler, is differentiable; the *iterative amortized* setting of [[marino-2018-iterative-amortized-inference]] repeatedly refines reparameterized beliefs by following free-energy gradients, narrowing the amortization gap left by a single-pass encoder.

## In this work

The trick surfaces wherever the model takes an expectation under a per-token Gaussian belief and needs a gradient for it:

- **Belief updates.** Where the target-blind belief objective contains a sampled expectation, reparameterization differentiates that expectation. The `gradient_mode "filtering"` step is not a Neal–Hinton incremental-EM update because the decode objective is separate.
- **Separate decode objective.** Reparameterization does not turn the decode cross-entropy and belief objective into one negative ELBO.
- **Covariance handling.** Reparameterized samples must respect the SPD structure of $\Sigma$, tying the trick to the model's `spd_affine` retraction and Riemannian covariance optimization.

The trick should be read alongside [[Amortized inference]] as a general
comparison, [[Precision weighting]], and the predictive-coding view in
[[rao-1999-predictive-coding]]. The deployed architecture has no neural
recognition map, so amortized-inference results do not describe its belief
initialization or establish a shared ELBO.

## Sources

- [[kingma-2013-auto-encoding-variational-bayes]] — origin of the reparameterization trick and amortized Gaussian inference for the ELBO.
- [[marino-2018-iterative-amortized-inference]] — iterative refinement of reparameterized variational beliefs.
- [[neal-1998-variational-em]] — shared-functional variational EM background; its incremental guarantee does not apply to the deployed two-objective loop.
- [[friston-2010-free-energy-principle]] — free-energy background for the belief-side interpretation.
- [[bogacz-2017-free-energy-tutorial]] — explicit Gaussian-belief free-energy updates.
- [[millidge-2020-pc-approximates-backprop]] — relation between local predictive-coding updates and backprop gradients.
- [[amari-1998-natural-gradient]] — Fisher preconditioning for the belief-side gradient.
- [[li-turner-2016-renyi-vi]] — the Rényi-bound objectives the trick can estimate.
- [[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]], [[arsigny-2006-log-euclidean]] — SPD-aware parameterization of the sampled covariance.

## See also

- [[Variational free energy]]
- [[Evidence lower bound (ELBO)]]
- [[Amortized inference]]
- [[Precision weighting]]
- [[Prediction error]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[Renyi divergence]]
- [[Alpha-divergence]]
- [[Variational autoencoder (VAE)]]
- [[Variational EM]]
- [[Iterative amortized inference]]
- [[Predictive coding network]]
