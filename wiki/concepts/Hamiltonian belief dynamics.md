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
updated: 2026-11-13
---

# Hamiltonian belief dynamics

## Definition and status

**Hamiltonian belief dynamics** is the conditional second-order extension of the gauge-covariant population potential in [[Multi-agent variational free energy]]. It is not the primary inference law and is not derived from the [[Fisher information metric]], scalar damping, or the loss Hessian alone. The primary dynamics are Fisher--Rao [[Natural gradient|natural-gradient]] flow. The Hamiltonian regime begins only after selecting a positive kinetic metric $M$:

$$
\mathcal H(\xi,\pi)
=\frac12\langle\pi,M(\xi)^{-1}\pi\rangle
+\mathcal F(\xi).
$$

The theorem-first revision of the belief-inertia manuscript (2026-07-12) separates the intrinsic Fisher metric $G$, the loss Hessian/local stiffness $H_F$, and the kinetic metric $M$. [[chirco-2022-statistical-bundle-dynamics]], [[pistone-2018-statistical-bundle-lagrangian]], [[leok-zhang-2017-information-geometric-mechanics]], and [[girolami-calderhead-2011-riemann-hmc]] show that probability-space mechanics and information-geometric kinetic choices have substantial precedent. [[martins-2015-opinion-particles]] is the closest direct opinion-particle and harmonic-oscillator predecessor.

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

- [[martins-2015-opinion-particles]] -- Bayesian-inspired opinion particles with force, inertia, and a harmonic example.
- [[chirco-2022-statistical-bundle-dynamics]], [[pistone-2018-statistical-bundle-lagrangian]], [[leok-zhang-2017-information-geometric-mechanics]] -- probability-space mechanics precedents.
- [[girolami-calderhead-2011-riemann-hmc]] -- Fisher/Riemannian kinetic geometry.
- [[xue-hirche-cao-2020-opinion-port-hamiltonian]], [[baumann-sokolov-tyloo-2020-second-order-consensus]], [[sampson-porter-restrepo-2025-oscillatory-opinion]] -- alternative Hamiltonian, second-order, resonance, and feedback mechanisms.
- [[dacosta-2023-entropy-production-stationary-diffusions]] — underdamped Langevin with the Hamiltonian vector field as irreversible drift; infinite unflipped entropy production.
- [[barp-2021-measure-preserving-diffusions]] — underdamped Langevin on a tangent bundle with an Ornstein-Uhlenbeck fiber process (Theorem 9.1).
- [[barp-2022-geometric-methods-sampling]] — conformal Hamiltonian systems and gradient flow as the high-friction limit, argued informally.
- [[friston-2012-free-energy-value-attractors]] — state-space example of Newtonian motion and friction from the Ao decomposition.
- [[kim-2021-bayesian-mechanics-perceptual-inference]] — least-action recognition dynamics; momentum as precision-weighted prediction error; saddle-or-center spectrum.
- [[kim-2024-bayesian-mechanics-synaptic-learning]] — synaptic extension of the least-action formulation with a traceless linear flow.
- [[heins-2022-particular-flows-attracting-sets]] — numerical example sorting solenoidal couplings by their effect on the attracting set (cited as analogy).

## See also

- [[Belief inertia]]
- [[Mass as Fisher information]]
- [[Multi-agent variational free energy]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
- [[SocialPhysics]]

## Langevin, conformal and least-action precedents in the Bayesian mechanics literature, November 13, 2026

The Bayesian mechanics literature supplies reference forms for a Hamiltonian sector. [[dacosta-2023-entropy-production-stationary-diffusions|Da Costa and Pavliotis 2023]] show that for underdamped Langevin dynamics the time-irreversible drift is the Hamiltonian vector field, $b_{\mathrm{irr}}=Q\nabla\log\rho$ with $Q$ proportional to the canonical symplectic matrix, while the noise acts on the momenta only; the entropy production is proved infinite under the unflipped definition and is zero under the momentum-flipped one. [[barp-2021-measure-preserving-diffusions|Barp et al. 2021]] (Theorem 9.1) construct such dynamics on a tangent bundle, with an Ornstein-Uhlenbeck fiber process preserving a metric-dependent Gaussian. [[barp-2022-geometric-methods-sampling|Barp et al. 2022]] state the conformal Hamiltonian system $\dot q^i=g^{ij}p_j$, $\dot p_i=-\partial_iV-\gamma p_i$ and argue informally that gradient flow is its high-friction limit. A state-space precursor in [[friston-2012-free-energy-value-attractors|Friston and Ao 2012]] obtains Newtonian motion from the canonical antisymmetric $Q$ and a friction term from diffusion on the velocity. [[kim-2021-bayesian-mechanics-perceptual-inference|Kim 2021]] takes the Laplace-encoded free energy as a Lagrangian, making the conjugate momentum a precision-weighted [[Prediction error|prediction error]]; its linear flow has a traceless relaxation matrix, hence only saddles or centers, with bounded orbits found numerically only in a narrow window that needs negative noise covariance and an added tuning parameter. [[kim-2024-bayesian-mechanics-synaptic-learning|Kim 2024]] extends the action to synaptic weights, again with zero trace.

> [!note] Editorial: bearing on the kinetic postulate
> None of these papers places a kinetic metric on a statistical manifold; reading $g$ or the fiber Gaussian as the $M$ of this page is an analogy and not a theorem. Kim's spectrum shows that a conservative flow derived from a free-energy action does not relax, in line with the requirement here that damping be declared separately. By analogy only, the one numerical example of [[heins-2022-particular-flows-attracting-sets|Heins 2022]] suggests that solenoidal coupling between blanket and internal states keeps the attracting set on the conditional modes, while coupling between external and blanket states rotates it.
