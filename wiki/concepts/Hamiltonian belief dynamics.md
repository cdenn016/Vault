---
type: concept
title: "Hamiltonian belief dynamics"
aliases:
  - "Hamiltonian formulation of belief dynamics"
  - "Second-order belief dynamics"
tags:
  - cluster/multi-agent
  - cluster/social-physics
  - cluster/info-geometry
  - project/multi-agent
  - project/social-physics
status: draft
created: 2026-06-18
updated: 2026-07-12
---

# Hamiltonian belief dynamics

## Definition and status

**Hamiltonian belief dynamics** is the conditional second-order extension of the gauge-covariant population potential in [[Multi-agent variational free energy]]. It is not the primary inference law and is not derived from the [[Fisher information metric]], scalar damping, or the loss Hessian alone. The primary dynamics are Fisher--Rao [[Natural gradient|natural-gradient]] flow. The Hamiltonian regime begins only after selecting a positive kinetic metric $M$:

$$
\mathcal H(\xi,\pi)
=\frac12\langle\pi,M(\xi)^{-1}\pi\rangle
+\mathcal F(\xi).
$$

The theorem-first revision [[belief-inertia-2026-07-12-theorem-first-revision]] separates the intrinsic Fisher metric $G$, the loss Hessian/local stiffness $H_F$, and the kinetic metric $M$. [[chirco-2022-statistical-bundle-dynamics]], [[pistone-2018-statistical-bundle-lagrangian]], [[leok-zhang-2017-information-geometric-mechanics]], and [[girolami-calderhead-2011-riemann-hmc]] show that probability-space mechanics and information-geometric kinetic choices have substantial precedent. [[martins-2015-opinion-particles]] is the closest direct opinion-particle and harmonic-oscillator predecessor.

## Kinetic postulate and spectrum

The conditional postulate permits a positive restriction of local gauge-VFE stiffness to be adopted as kinetic geometry only in a reciprocal, frozen-attention, local-consensus regime. If $M$ is then set equal to the same equilibrium Hessian that supplies the restoring force,

$$
H_Fv=\omega^2Mv,
\qquad M=H_F
\Longrightarrow \omega^2=1
$$

up to the declared scale. Nontrivial modal predictions require operationally independent $M$ and restoring stiffness $K$. Valid examples include a frozen pre-intervention kinetic metric paired with a separately manipulated evidence curvature, or an intrinsic Fisher kinetic metric paired with a distinct loss Hessian.

For coupled coordinates, the canonical momentum is

$$
\pi_i=\sum_kM_{ik}\dot\mu_k,
$$

with cross-sector terms if mean--covariance coupling is retained. The local formula $\pi_i=M_i\dot\mu_i$ applies only after an explicit block-diagonal approximation.

## Damping and first-order reduction

For locally constant positive $M$, independently specified $K$, and tensor friction $\Gamma$, a local mechanical model may be written

$$
M\ddot x+\Gamma\dot x+Kx=f(t).
$$

Its fast-momentum reduction is $\dot x=-\Gamma^{-1}\nabla\mathcal F$. It becomes Fisher natural-gradient flow only when the friction tensor is chosen compatibly, for example $\Gamma=M/\eta$ under the declared local identification. A scalar $\gamma$ does not produce a loss-Hessian/Newton flow in a multivariate system.

The familiar underdamped frequency, resonance, overshoot, and coasting formulas are conditional on constant $M$ and independent $K$. Their interpretation depends on what is held fixed: force, velocity, momentum, stiffness, damping coefficient, or damping ratio. They cannot be converted into precision predictions by silently setting $M=H_F$.

## Conservativity and attention

Fixed asymmetric attention still defines a scalar potential when the complete directed edge sum is differentiated with respect to both receiver and sender coordinates. Its forces remain conservative. The optimized entropy-retaining attention row also stays scalar through the reduced log-partition objective and its envelope gradient. Nonconservative behavior occurs only after a declared receiver-only or detached-source truncation, explicit time dependence, damping, or external ports.

This scope differs from an implementation choice to symmetrize attention before building an approximate local mass. Such symmetrization can be a numerical convention, but it is not required for the complete fixed-attention scalar potential to exist.

## What oscillation can and cannot show

Second-order consensus, network resonance, and Hamiltonian opinion language are not new by themselves. [[xue-hirche-cao-2020-opinion-port-hamiltonian]] analyzes opinion dynamics with port-Hamiltonian and passivity methods. [[baumann-sokolov-tyloo-2020-second-order-consensus]] obtains parametric resonance from periodically modulated network coupling. [[sampson-porter-restrepo-2025-oscillatory-opinion]] obtains self-sustained and excitable opinions from individual--group feedback without a kinetic-inertia term.

Consequently, observing oscillation or overshoot is not mechanism-identifying. A useful test must estimate $M$, $K$, and damping independently, pre-register their predicted modal response, and compare the conditional kinetic model with matched first-order feedback and time-varying-network controls. [[nevin-mandell-atak-1983-behavioral-momentum]] can inform resistance-to-disruption protocols, but it does not validate Hamiltonian opinion mechanics.

## Social interpretation

A force-free kinetic coast can serve as one candidate component of revision latency or perseverance. It does not model the persistence of a causal explanation after evidence withdrawal unless a slow explanatory state is added. Likewise, the outgoing relational stiffness is a contemporaneous property of the scalar potential, not accumulated leadership memory or inevitable social rigidity.

## Sources

- [[belief-inertia-2026-07-12-theorem-first-revision]] -- corrected kinetic postulate, coupled momentum, conservativity, and proof-status record.
- [[martins-2015-opinion-particles]] -- Bayesian-inspired opinion particles with force, inertia, and a harmonic example.
- [[chirco-2022-statistical-bundle-dynamics]], [[pistone-2018-statistical-bundle-lagrangian]], [[leok-zhang-2017-information-geometric-mechanics]] -- probability-space mechanics precedents.
- [[girolami-calderhead-2011-riemann-hmc]] -- Fisher/Riemannian kinetic geometry.
- [[xue-hirche-cao-2020-opinion-port-hamiltonian]], [[baumann-sokolov-tyloo-2020-second-order-consensus]], [[sampson-porter-restrepo-2025-oscillatory-opinion]] -- alternative Hamiltonian, second-order, resonance, and feedback mechanisms.

## See also

- [[Belief inertia]]
- [[Mass as Fisher information]]
- [[Multi-agent variational free energy]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
- [[SocialPhysics]]
