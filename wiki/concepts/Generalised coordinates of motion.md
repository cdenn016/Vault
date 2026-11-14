---
type: concept
title: "Generalised coordinates of motion"
aliases:
  - "Generalised Coordinates"
  - "Generalized coordinates"
tags:
  - cluster/vfe
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-11-13
---

# Generalised coordinates of motion

In Friston's dynamic expectation maximization and active-inference framework, generalised coordinates of motion represent a trajectory not by its instantaneous value alone but by a vector of its successive temporal derivatives (position, velocity, acceleration, ...). Modeling beliefs and dynamics in this lifted space lets the free-energy functional encode smooth, continuous-time dynamics and colored (analytic) noise, turning filtering of nonlinear continuous systems into a generalised gradient descent on variational free energy.

## Related
[[Variational free energy]], [[Free-energy principle active inference|Free energy principle]], [[Predictive coding]]

## Sources
[[friston-2008-dem]], [[friston-2010-free-energy-principle]], [[dacosta-2025-generalized-coordinates-sde]], [[kim-2021-bayesian-mechanics-perceptual-inference]]

## Pathwise theory for stochastic differential equations and an objection, November 13, 2026

[[dacosta-2025-generalized-coordinates-sde|Da Costa et al. 2025]] give a pathwise theory for equations $\dot x_t=f(x_t)+w_t$ with additive, temporally correlated noise. The generalized state stacks the Taylor coefficients of the solution at a time point in $\mathbb{G}^{d,N}\cong\mathbb{R}^{d(N+1)}$ and evolves under a block shift,

$$
\frac{d}{dt}\mathbf{x}_t=\mathbf{D}\mathbf{x}_t,
$$

with solution $\mathbf{x}_t=\exp(t\mathbf{D})\mathbf{x}_0$, a moving Taylor polynomial. The hypotheses are additive noise, a deterministic initial condition, and a flow and noise paths that are $N-1$ times continuously differentiable. Under these the authors prove a unique local solution with Taylor error $o(|t|^N)$ (Theorem 1.2.2) and exactness on a random interval when flow and noise path are analytic (Theorem 1.2.4), with a radius that can be arbitrarily small. For stationary Gaussian noise with autocovariance $\kappa$, the generalized fluctuations of orders $n$ and $m$ have covariance $(-1)^n\kappa^{(n+m)}(h)$, and the linear equation is solved in closed form. Faithfulness of the local linear approximation for nonlinear flows is not established, and multiplicative and non-stationary noise are left to future work. [[kim-2021-bayesian-mechanics-perceptual-inference|Kim 2021]] objects that higher-order generalized states have no dynamical status in Newtonian mechanics and replaces them with a least-action formulation, which treats white noise only.

> [!note] Editorial: reading for belief dynamics
> The shift $\mathbf{D}$ gives a Gaussian belief temporal depth. Reading it as inertia or as a Hamiltonian structure is interpretive, since $\mathbf{D}$ is nilpotent and carries no symplectic form or mass matrix.
