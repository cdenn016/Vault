---
type: concept
title: Belief inertia
aliases:
  - Epistemic inertia
  - Cognitive momentum
  - Epistemic momentum
  - Belief momentum
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/info-geometry
  - cluster/social-physics
  - project/multi-agent
  - project/social-physics
status: draft
created: 2026-06-18
updated: 2026-11-13
---

# Belief inertia

## Definition

**Belief inertia** is a conditional kinetic interpretation of the local stiffness produced by the gauge-covariant population objective in [[Multi-agent variational free energy]]. The primary inference law is first-order Fisher--Rao [[Natural gradient|natural-gradient]] flow. A second-order reading enters only through this modeling postulate:

> In a reciprocal, frozen-attention, local-consensus regime, a positive restriction of the gauge-VFE stiffness may be adopted as a kinetic metric for belief-configuration change.

The theorem-first revision of the belief-inertia manuscript (2026-07-12) separates three tensors:

- $G(q)$: the intrinsic [[Fisher information metric]] on the statistical manifold;
- $H_F(x)$: the coordinate loss Hessian, interpreted locally as free-energy stiffness;
- $M(x)$: a separately selected positive kinetic metric.

These tensors can agree in a declared local matching regime, but information geometry does not identify them globally. [[martins-2015-opinion-particles]], [[chirco-2022-statistical-bundle-dynamics]], [[girolami-calderhead-2011-riemann-hmc]], [[leok-zhang-2017-information-geometric-mechanics]], and [[pistone-2018-statistical-bundle-lagrangian]] are direct precedents for opinion mechanics, statistical-bundle mechanics, or Fisher-dependent kinetic geometry. The present contribution is the gauge-transported Gaussian KL potential and its four-part local relational stiffness before the kinetic choice is made.

## Local stiffness and the kinetic postulate

At frozen optimized attention and local gauge consensus, the mean-sector diagonal block is

$$
[H_{\mu\mu}]_{ii}
=\alpha_i\bar\Lambda_{p_i}
+\Lambda_{o_i}
+\sum_k\beta_{ik}\widetilde\Lambda_{q_k}
+\sum_j\beta_{ji}\Lambda_{q_i}.
$$

The four terms are prior, sensory, incoming relational, and outgoing relational or recoil **stiffness**. The full stacked Hessian also contains off-diagonal sender/receiver blocks. Away from frozen consensus, optimized attention contributes the reduced-Hessian correction

$$
-\tau^{-1}\operatorname{Cov}_{\beta_i^*}(\nabla E_{ij},\nabla E_{ij}),
$$

so no global positive-definiteness or intrinsic-metric claim follows for $H_F$.

If the kinetic postulate chooses the same tensor as the restoring Hessian at the same equilibrium, the generalized mode equation becomes

$$
H_Fv=\omega^2Mv,
\qquad M=H_F
\Longrightarrow \omega^2=1
$$

up to the declared scale. The same-functional choice therefore has a trivial spectrum and cannot support nontrivial precision-dependent frequency claims. Such claims require an independently specified $M$ and restoring tensor $K$, for example a frozen pre-intervention kinetic metric paired with manipulated evidence curvature.

For a coupled kinetic form, canonical momentum is

$$
\pi_i=\sum_kM_{ik}\dot\mu_k,
$$

with covariance-sector terms where retained. The local formula $\pi_i=M_i\dot\mu_i$ is valid only after an explicit block-diagonal approximation.

## Primary dynamics and force scope

The first-order mean and covariance dynamics are

$$
\dot\mu_i=-\eta_\mu\Sigma_i\nabla_{\mu_i}\mathcal F,
\qquad
\dot\Sigma_i=-2\eta_\Sigma\Sigma_i
(\nabla_{\Sigma_i}\mathcal F)\Sigma_i.
$$

This is Fisher natural-gradient flow, not a Newton or loss-Hessian flow derived from scalar damping. A mechanical overdamped reduction matches it only after a compatible tensor friction, such as $\Gamma=M/\eta$, is declared and the slow-time limit is derived.

Fixed asymmetric attention does not make the complete dynamics nonconservative. With both receiver and sender derivatives retained, the directed edge sum remains one scalar potential. Nonconservative behavior requires a receiver-only/detached truncation, explicit time dependence, damping, or external forcing.

For adaptive prior precision, the complete sector is

$$
\alpha_iD_i+b_0\alpha_i-c_0\log\alpha_i,
\qquad
\alpha_i^*=\frac{c_0}{b_0+D_i}.
$$

The envelope force coefficient $c_0/(b_0+D_i)$ differs from the bare-product derivative $b_0c_0/(b_0+D_i)^2$. These are different objectives and do not generate the same dynamics.

## Social interpretation

For first-order flow linearized at a critical point, $\dot\delta=-\eta G^{-1}H_F\delta$. At fixed $G$ and $\eta$, increasing a positive modal stiffness reduces the matched-force static displacement but increases the relaxation rate. The stiffness theorem therefore does not imply revision latency. Slower revision requires an independently specified mobility or learning rate, damping law, kinetic metric, or slow explanatory state. The conditional kinetic extension can motivate tests of coasting, overshoot, or modal response only when $M$, restoring stiffness, damping, force, and initial conditions are separately identified. Neither result establishes universal confirmation bias, explanatory perseverance, or accumulated social memory. The outgoing recoil term is contemporaneous curvature from occupying a sender role, not a stored moral or psychological trait.

Oscillation alone is not evidence for belief inertia. [[baumann-sokolov-tyloo-2020-second-order-consensus]] produces network resonance under periodic coupling, and [[sampson-porter-restrepo-2025-oscillatory-opinion]] produces oscillatory and excitable opinions through group-state feedback without this kinetic mechanism. [[nevin-mandell-atak-1983-behavioral-momentum]] is an empirical resistance-to-disruption comparator, not validation of opinion-level Hamiltonian dynamics.

> [!note] Editorial: [[dennis-2026-dynamic-links]] (October 3, 2026) derives an inertial mass without a kinetic postulate in one restricted setting: the maximum a posteriori path of a latent link field over depth. There the mass is the precision of a declared increment prior, distinct from the restoring stiffness, and the equation of motion has Euclidean sign, motion in the inverted potential. It produces no oscillation, and it says nothing about belief trajectories unless a path prior over beliefs is declared. See [[Mass as Fisher information]].

## Sources

- [[belief-inertia]] -- immutable historical manuscript note, retained for provenance.
- [[martins-2015-opinion-particles]] -- direct opinion-particle and oscillator predecessor.
- [[chirco-2022-statistical-bundle-dynamics]], [[leok-zhang-2017-information-geometric-mechanics]], [[pistone-2018-statistical-bundle-lagrangian]] -- statistical-bundle and information-geometric mechanics.
- [[girolami-calderhead-2011-riemann-hmc]] -- Fisher/Riemannian kinetic geometry with the metric kept distinct from target curvature.
- [[nevin-mandell-atak-1983-behavioral-momentum]], [[baumann-sokolov-tyloo-2020-second-order-consensus]], [[sampson-porter-restrepo-2025-oscillatory-opinion]] -- behavioral persistence and alternative oscillation mechanisms.
- [[kim-2021-bayesian-mechanics-perceptual-inference]] — generative precisions called neural inertial masses, as a metaphor, in a least-action formulation.
- [[kim-2024-bayesian-mechanics-synaptic-learning]] — mass as inverse noise variance for states and weights, tied to temperature and friction.
- [[sakthivadivel-2023-worked-example-classical-objects]] — mass as a parameter of the mean constraint, separate from the precision multiplier.

## See also

- [[Mass as Fisher information]]
- [[Hamiltonian belief dynamics]]
- [[Multi-agent variational free energy]]
- [[Fisher information metric]]
- [[Natural gradient]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
- [[SocialPhysics]]

## Precision as inertial mass in least-action recognition dynamics, November 13, 2026

Two papers by Kim obtain an inertial term without a kinetic postulate, because velocity enters through a dynamical generative prior. In [[kim-2021-bayesian-mechanics-perceptual-inference|Kim 2021]] the model $\dot\mu=f(\mu)+w$, $\varphi=g(\mu)+z$, with Gaussian white noises of variances $\sigma_w$, $\sigma_z$ and correlation $\rho$, yields a Lagrangian whose coefficients $m_i=1/(\sigma_i(1-\rho^2))$ the author calls neural inertial masses, explicitly as a metaphor. [[kim-2024-bayesian-mechanics-synaptic-learning|Kim 2024]] sets $m_\mu=1/\sigma_\mu^2$ and $m_w=1/\sigma_w^2$ for postsynaptic activity and synaptic weight; its fluctuation-dissipation relation $\sigma_\mu^2=2\gamma_\mu^{-1}k_BT$ then implies $m_\mu=\gamma_\mu/(2k_BT)$. [[sakthivadivel-2023-worked-example-classical-objects|Sakthivadivel 2023]] assigns the two roles to different quantities: the mass of a classical particle is a given parameter inside the mean constraint $E_{p(q)}[q]=\iint F(\eta)/m$, the precision is a separate multiplier $\lambda_1$ with the heuristic $\lambda_1\propto D^{-1}$, and the classical path is placed at the infinite-precision limit, a limit the paper states inconsistently, in an argument that presupposes the classical law.

> [!note] Editorial: comparison with the three-tensor separation
> In Kim's models the mass on the state rate is the precision of a declared transition noise, a specified $M$ distinct from the sensory term and comparable to the increment-prior mass of the editorial above. Its value coincides with a Fisher information for a Gaussian location parameter, a comparison the papers do not draw (see [[Mass as Fisher information]]). The setting is one agent in flat coordinates with no covariance dynamics, fibers or transport, and the linear flows have eigenvalues in opposite-sign pairs, so they do not relax (see [[Hamiltonian belief dynamics]]). Sakthivadivel's construction keeps mass and precision apart and gives no support to a precision-as-inertia reading.
