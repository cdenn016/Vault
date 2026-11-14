---
type: concept
title: "Laplace approximation"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-11-13
---

# Laplace approximation

The Laplace approximation models an intractable posterior as a Gaussian centered at the maximum a posteriori (MAP) estimate, with covariance equal to the inverse Hessian (observed Fisher information) of the negative log-posterior at that mode. It yields a closed-form log-evidence (marginal likelihood) approximation whose leading terms recover the BIC penalty (Schwarz 1978), and it is the workhorse that turns variational free energy into a tractable, Gaussian-belief scheme in dynamic expectation maximization (Friston 2008). In the VFE program it justifies the Gaussian-belief parameterization (mu, Sigma) and connects model evidence to the Fisher-information geometry of beliefs.

## Related
[[Variational free energy]], [[Fisher information metric]], [[Predictive coding network]]

## Sources
[[friston-2008-dem]], [[schwarz-1978-bic]], [[dacosta-2025-generalized-coordinates-sde]], [[millidge-2021-mathematical-walkthrough-fep]], [[smithe-2023-compositional-bayesian-brain]]

## Exactness, the mode-level reading, and the Laplace doctrine, November 13, 2026

Three sources sharpen the role of the Laplace step in free-energy schemes. In the generalized filtering of [[dacosta-2025-generalized-coordinates-sde|Da Costa et al. 2025]] the posterior is Gaussian with covariance $\Sigma^*=(\nabla^2_\mu V)^{-1}$, where $V=-\log p(\mathbf y_t,\mathbf x_t)$, and the mean flow carries a correction $-\tfrac{\lambda}{2}\nabla_\mu\log\det\nabla^2_\mu V$. Under the local linear approximation, which drops derivatives of the flow above first order, $\nabla^3_\mu V\equiv0$, so the Laplace free energy is exact and the correction vanishes. This is derived algebraically, and the faithfulness of that approximation for nonlinear flows is not established. [[millidge-2021-mathematical-walkthrough-fep|Millidge, Seth and Buckley 2021]] locate the Laplace-encoded Gaussian in the derivation of the free energy lemma: together with an invertible differentiable synchronization map it turns the surprisal gradient into a free energy gradient for conditional modes, $\dot{\mathbf i}=(\Gamma_\sigma-Q_\sigma)\nabla_{\mathbf i}F$, a correspondence that holds for modes only and whose final identification the source note records as argued in two lines. [[smithe-2023-compositional-bayesian-brain|Smithe 2023]] defines a Laplacian free energy with the energy evaluated at the posterior mean and the covariance equal to the inverse Hessian there, and assembles the Laplace doctrine $\mathsf L_\lambda=\mathrm{Euler}_\lambda\circ\nabla\circ\mathrm{LFE}$, a pseudofunctor from parameterized Gaussian channels to open dynamical systems whose update uses precision-weighted errors. Its functoriality relies on a mean-field form, and the inference system is non-unital.

> [!note] Editorial: bearing on Gaussian beliefs
> These results concern when a Gaussian belief with inverse-Hessian covariance is exact or compositional for one system. They leave open the transport of such beliefs between agents.
