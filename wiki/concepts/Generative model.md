---
type: concept
title: "Generative model"
aliases:
  - "generativemodel"
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-21
updated: 2026-07-12
---

# Generative model

A **generative model** is a normalized joint probability law $p_\theta(o,z)$ over observations $o$
and latent variables $z$. Inference conditions this law to obtain $p_\theta(z\mid o)$. Variational
inference chooses a tractable $q(z)$ and minimizes

$$
\mathcal F[q]
=D_{\mathrm{KL}}(q(z)\Vert p_\theta(z\mid o))-\log p_\theta(o)
=\mathbb E_q[\log q(z)-\log p_\theta(o,z)].
$$

The model is fixed while $q$ varies. This quantifier is what turns $-\mathcal F$ into an
[[Evidence lower bound (ELBO)]] rather than merely an energy objective.

## Fixed generative models

For a mean-field family $Q_q(z_{1:N})=\prod_iq_i(z_i)$ and a fixed joint $p_\theta$,

$$
D_{\mathrm{KL}}(Q_q\Vert p_\theta)
=\sum_i\int q_i\log q_i
-\int\left(\prod_iq_i\right)\log p_\theta.
$$

The entropy is factor-separable, and the energy expectation is affine in each factor with all
others fixed. This multilinear structure is a testable signature of a fixed state-level
mean-field model [[wainwright-2008-graphical-models-variational]].

## Population-consensus no-go boundary

The [[Multi-agent variational free energy]] contains terms
$D_{\mathrm{KL}}(q_i\Vert T_{ij}q_j)$. Their denominators are transported variational beliefs,
not fixed model factors. A mixed-third-variation test proves that an active nondegenerate consensus
edge cannot equal the mean-field KL against one fixed joint on an open product family: the
fixed-model variation $D^3_{q_iq_jq_j}$ vanishes, while the consensus-edge variation can be chosen
as a strictly positive variance. [[vfe-population-generative-status-2026-07-12]]

This is a scoped no-go result. It excludes the ordinary fixed joint on the original state variables
under the stated open-family and nondegeneracy assumptions. It does not exclude frozen source
templates, zero coupling, compatible auxiliary variables, restricted families, or a model whose
latent variable is itself a belief configuration.

## Valid enlarged constructions

PIFB2 has three valid probabilistic readings. At zero within-scale coupling, its cross-scale
Gaussian hierarchy is a proper [[Hierarchical generative model]] with an SPD stacked precision and
a unique mean-field optimum. On a finite positive state space, a continuous geometric-pooling map
has a Brouwer fixed point; after selecting it, the source distributions become fixed and define
proper auxiliary row models. Those row models need an additional compatibility or factorization
condition before they become one shared-state joint.

At the higher configuration level, any measurable population energy $\mathcal F(X)$ defines

$$
\frac{dP_{\mathcal F}}{d\rho_0}(X)
=Z_{\mathcal F}^{-1}e^{-\mathcal F(X)/T_{\mathrm{cfg}}}
$$

whenever $\rho_0$ is proper and $0<Z_{\mathcal F}<\infty$. This is an exact energy-based
generative model over belief configurations and gives a meta-level VFE after adding configuration
entropy. It does not convert the original population energy into the excluded state-level ELBO.
Loss-tempered versions have the coherent generalized-Bayes interpretation of
[[bissiri-2016-general-bayesian-updating]].

## Related

[[Variational free energy]], [[Predictive coding]], [[Amortized inference]],
[[Hierarchical generative model]], [[Meta-entropy]]

## Sources

- [[participatory-it-from-bit]]
- [[vfe-population-generative-status-2026-07-12]]
- [[meta-entropy-manuscript]]
- [[wainwright-2008-graphical-models-variational]]
- [[bissiri-2016-general-bayesian-updating]]
