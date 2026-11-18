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
updated: 2026-11-18
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

## Energy-based generative models

Any measurable energy $\mathcal F(X)$ on a configuration space defines

$$
\frac{dP_{\mathcal F}}{d\rho_0}(X)
=Z_{\mathcal F}^{-1}e^{-\mathcal F(X)/T_{\mathrm{cfg}}}
$$

whenever $\rho_0$ is proper and $0<Z_{\mathcal F}<\infty$. This is an exact energy-based
generative model over configurations. Loss-tempered versions have the coherent generalized-Bayes interpretation of
[[bissiri-2016-general-bayesian-updating]].

## Related

[[Variational free energy]], [[Predictive coding]], [[Amortized inference]],
[[Hierarchical generative model]]

## Sources

- [[wainwright-2008-graphical-models-variational]]
- [[bissiri-2016-general-bayesian-updating]]
