---
type: concept
title: Reparameterization trick
aliases:
  - Reparameterisation trick
  - Pathwise gradient estimator
  - Stochastic backpropagation
  - Location-scale reparameterization
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
status: draft
created: 2026-06-18
updated: 2026-06-18
---

# Reparameterization trick

## Definition

The **reparameterization trick** is a technique for obtaining low-variance, pathwise gradient estimates of an expectation taken under a parametric distribution, when those parameters are themselves what we wish to differentiate with respect to. Suppose we must compute the gradient with respect to parameters $\phi$ of an objective of the form $\mathbb{E}_{z \sim q_\phi(z)}[f(z)]$. Because the distribution $q_\phi$ over which the expectation is taken *depends* on $\phi$, the gradient cannot simply be pushed inside the expectation. The trick rewrites the random variable $z$ as a deterministic, differentiable transformation $z = g_\phi(\epsilon)$ of an auxiliary noise variable $\epsilon \sim p(\epsilon)$ whose distribution carries no dependence on $\phi$. The expectation then becomes $\mathbb{E}_{\epsilon \sim p(\epsilon)}[f(g_\phi(\epsilon))]$, and because the source of randomness $p(\epsilon)$ is now parameter-free, the gradient and expectation commute:

$$\nabla_\phi\, \mathbb{E}_{z \sim q_\phi}[f(z)] = \mathbb{E}_{\epsilon \sim p(\epsilon)}\big[\nabla_\phi\, f(g_\phi(\epsilon))\big].$$

The canonical instance is the Gaussian *location–scale* transform: to sample $z \sim \mathcal{N}(\mu, \Sigma)$ with $\Sigma = L L^\top$, write $z = \mu + L\,\epsilon$ where $\epsilon \sim \mathcal{N}(0, I)$. The mean $\mu$ and the Cholesky (or square-root) factor $L$ are now differentiable inputs to a sample, so a single Monte-Carlo draw of $\epsilon$ yields an unbiased gradient estimate by ordinary backpropagation through $g_\phi$. This estimator typically has far lower variance than the alternative score-function (REINFORCE / log-derivative) estimator, because it exploits the gradient information in $f$ rather than treating it as a black box.

## Why it matters here

The VFE transformer maintains, for every token, a **Gaussian belief** described by a mean $\mu$ and a symmetric-positive-definite covariance $\Sigma$ (the family is `gaussian_diagonal`). Training minimizes a [[Variational free energy]] / [[Evidence lower bound (ELBO)]] objective, which is an expectation of a prediction-error-like quantity *taken under that belief distribution*. The reparameterization trick is precisely what makes this expectation differentiable end-to-end with respect to the belief parameters $(\mu, \Sigma)$: it converts "differentiate through a sampling step over $q_\phi$" into "differentiate a deterministic function of fixed Gaussian noise." Without it, optimizing per-token Gaussian beliefs by gradient descent would rely on high-variance score-function estimates that are impractical at transformer scale.

This is the same mechanism that made the variational autoencoder trainable: [[kingma-2013-auto-encoding-variational-bayes]] introduced the trick together with an amortized Gaussian recognition network as the blueprint for gradient-based optimization of Gaussian latent variables, which is exactly the structure the VFE transformer reuses at the per-token level. The trick therefore sits at the junction between the model's variational machinery (the E-step that updates beliefs) and its gradient-based learning, complementing the local, predictive-coding-style updates that [[millidge-2020-pc-approximates-backprop]] shows can themselves recover backpropagation.

## Details

**Why the naive gradient fails.** Differentiating $\mathbb{E}_{q_\phi}[f(z)] = \int q_\phi(z) f(z)\,dz$ produces a term $\int \nabla_\phi q_\phi(z)\, f(z)\,dz$. The integrand is no longer an expectation under a probability density (it is a derivative of one), so a plain Monte-Carlo average of $f$ over samples does not estimate the gradient.

**Two unbiased estimators.**
- *Score-function (REINFORCE)* uses the identity $\nabla_\phi q_\phi = q_\phi \nabla_\phi \log q_\phi$ to write the gradient as $\mathbb{E}_{q_\phi}[f(z)\,\nabla_\phi \log q_\phi(z)]$. It is general (it needs only that $q_\phi$ be differentiable in $\phi$ and that we can evaluate $\log q_\phi$), but high variance.
- *Pathwise (reparameterization)* uses $z = g_\phi(\epsilon)$ and differentiates $f$ through $g_\phi$. It requires $f$ to be differentiable and $q_\phi$ to admit a differentiable sampler, but yields much lower variance because $\nabla f$ enters directly.

**The Gaussian case in detail.** For a diagonal Gaussian, $z_i = \mu_i + \sigma_i\,\epsilon_i$ with $\epsilon_i \sim \mathcal{N}(0,1)$, so $\partial z_i / \partial \mu_i = 1$ and $\partial z_i / \partial \sigma_i = \epsilon_i$. The KL / divergence term against a Gaussian prior often has a closed form and need not be sampled at all; only the data-fit (reconstruction / prediction-error) term is estimated by reparameterized sampling. This split is what gives the ELBO its characteristic low-variance gradient.

**Interaction with the covariance manifold.** Because $\Sigma$ lives on the SPD cone, the reparameterization must produce a valid factor $L$ with $\Sigma = LL^\top$, and gradients then flow into a parameterization of $\Sigma$ that respects positive-definiteness — a concern shared with the #cluster/spd-geometry machinery (the `spd_affine` retraction, the affine-invariant metric of [[pennec-2006-affine-invariant-tensor]], and the SPD calculus surveyed in [[bhatia-2007-positive-definite-matrices]]). Equivalently, one may parameterize through the matrix logarithm in the [[arsigny-2006-log-euclidean]] sense, sampling in a flat tangent coordinate and mapping back, which keeps the sampler differentiable while guaranteeing an SPD result.

**Relation to natural-gradient optimization.** The reparameterization trick produces a *Euclidean* gradient in the chosen coordinates; it is silent about the geometry of the parameter space. In this work that gradient is subsequently preconditioned by the inverse [[Fisher information metric]] to obtain the [[Natural gradient]], following [[amari-1998-natural-gradient]]. The two are complementary: reparameterization makes the expectation differentiable; natural gradient makes the resulting descent direction reparameterization-*invariant* and Fisher-efficient.

> [!note] Editorial: The trick is a variance-reduction and differentiability device, not an inference principle. It says nothing about *which* divergence is minimized — that role belongs to the [[Renyi divergence]] / [[Alpha-divergence]] objective family the model adopts. Reparameterized sampling can estimate any of these bounds, including the variational Rényi bound of [[li-turner-2016-renyi-vi]].

**Variants.** Beyond the location–scale Gaussian: the *implicit* reparameterization extends the trick to distributions whose CDF, rather than whose sampler, is differentiable; the *iterative amortized* setting of [[marino-2018-iterative-amortized-inference]] repeatedly refines reparameterized beliefs by following free-energy gradients, narrowing the amortization gap left by a single-pass encoder.

## In this work

The trick surfaces wherever the model takes an expectation under a per-token Gaussian belief and needs a gradient for it:

- **E-step / belief updates.** When the variational E-step refines $(\mu, \Sigma)$ by descending the free energy (cf. [[neal-1998-variational-em]] and the explicit Gaussian relaxation of [[bogacz-2017-free-energy-tutorial]]), the expectation defining the per-token free energy is differentiated via reparameterized samples of the belief. The `gradient_mode "filtering"` setting performs these as incremental, partial updates — the incremental-EM regime justified by [[neal-1998-variational-em]].
- **ELBO training objective.** The overall training loss is a free-energy / negative-ELBO functional grounded in [[friston-2010-free-energy-principle]]; the reparameterization trick is the estimator that lets its sampling-based terms be optimized by backprop, exactly as in [[kingma-2013-auto-encoding-variational-bayes]].
- **Covariance handling.** Reparameterized samples must respect the SPD structure of $\Sigma$, tying the trick to the model's `spd_affine` retraction and Riemannian covariance optimization.

The trick should be read alongside [[Amortized inference]] (which supplies the recognition map that *produces* $\mu, \Sigma$ from each token), [[Precision weighting]] (which scales the prediction-error terms whose expectation is being estimated), and the predictive-coding view in [[rao-1999-predictive-coding]].

## Sources

- [[kingma-2013-auto-encoding-variational-bayes]] — origin of the reparameterization trick and amortized Gaussian inference for the ELBO.
- [[marino-2018-iterative-amortized-inference]] — iterative refinement of reparameterized variational beliefs.
- [[neal-1998-variational-em]] — the negative-free-energy/ELBO functional and incremental (filtering) E/M updates the trick differentiates.
- [[friston-2010-free-energy-principle]] — the free-energy / negative-ELBO objective the estimator serves.
- [[bogacz-2017-free-energy-tutorial]] — explicit Gaussian-belief free-energy updates.
- [[millidge-2020-pc-approximates-backprop]] — relation between local predictive-coding updates and backprop gradients.
- [[amari-1998-natural-gradient]] — Fisher preconditioning applied to the resulting gradient.
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
