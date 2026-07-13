---
type: concept
title: "Mass as Fisher information"
aliases:
  - "Hessian mass"
  - "Epistemic mass"
  - "Inertial mass tensor"
  - "Mass-precision correspondence"
tags:
  - cluster/multi-agent
  - cluster/info-geometry
  - cluster/social-physics
  - project/multi-agent
  - project/social-physics
status: draft
created: 2026-06-18
updated: 2026-07-13
---

# Mass as Fisher information

## Corrected scope

The phrase **mass as Fisher information** now names a conditional modeling choice, not an identity theorem. The theorem-level object in [[belief-inertia-2026-07-12-theorem-first-revision]] is the local free-energy loss Hessian or **stiffness** $H_F$. The intrinsic statistical geometry is the [[Fisher information metric]] $G(q)$. A positive kinetic metric $M$ is introduced only if the modeler elects to study a conditional second-order extension.

$$
G(q)\neq H_F(x)\neq M(x)
$$

in general. They may coincide in a specifically identified local matching regime, but Chentsov's theorem selects the intrinsic Fisher metric; it does not identify the total free-energy Hessian with Fisher information or force that Hessian to become kinetic mass. [[girolami-calderhead-2011-riemann-hmc]] provides a precedent for choosing Fisher/Riemannian geometry in a kinetic term while keeping the target curvature conceptually separate.

## Four-part local stiffness

At fixed optimized attention and local gauge consensus, the mean-sector diagonal block of the full stacked Hessian is

$$
[H_{\mu\mu}]_{ii}
=\alpha_i\bar\Lambda_{p_i}
+\Lambda_{o_i}
+\sum_k\beta_{ik}\widetilde\Lambda_{q_k}
+\sum_j\beta_{ji}\Lambda_{q_i}.
$$

The four terms are:

1. prior stiffness;
2. sensory stiffness;
3. incoming relational stiffness;
4. outgoing relational or recoil stiffness.

The outgoing term arises because agent $i$ also appears as a source in other agents' directed edge energies. It is contemporaneous sender-role curvature. It is not accumulated memory, a moral cost of influence, or inertia by itself. The full stacked $H_F$ includes off-diagonal sender/receiver blocks; the displayed diagonal block should not be treated as an autonomous mass for each agent.

Away from frozen consensus, optimized attention adds

$$
-\tau^{-1}\operatorname{Cov}_{\beta_i^*}(\nabla E_{ij},\nabla E_{ij})
$$

to the reduced row Hessian, along with residual-dependent cross-couplings. The clean positive local block therefore does not establish that the fully reduced Hessian is globally positive definite or coordinate-invariant under arbitrary nonlinear reparameterization.

## Conditional kinetic reading and degeneracy

The [[Belief inertia]] postulate permits a positive local restriction of $H_F$ to be adopted as $M$ in a reciprocal, frozen-attention, local-consensus regime. That choice must be declared. If the same tensor supplies both inertia and restoring stiffness at the same equilibrium,

$$
H_Fv=\omega^2Mv,
\qquad M=H_F
\Longrightarrow \omega^2=1
$$

up to scale. Thus the same-functional choice cannot yield a nontrivial stiffness-dependent spectrum. A meaningful test must identify $M$ independently of the manipulated restoring tensor $K$.

For a coupled kinetic metric, momentum is

$$
\pi_i=\sum_kM_{ik}\dot\mu_k.
$$

Only a block-diagonal approximation licenses $\pi_i=M_i\dot\mu_i$.

## Adaptive prior sector

For $D_i=D_{\mathrm{KL}}(q_i\|p_i)$, the complete adaptive sector is

$$
\Psi_i(\alpha_i,D_i)=\alpha_iD_i+b_0\alpha_i-c_0\log\alpha_i,
\qquad
\alpha_i^*=\frac{c_0}{b_0+D_i}.
$$

Two derivatives that were previously conflated are

$$
\frac{d}{dD}(\alpha^*D)=\frac{b_0c_0}{(b_0+D)^2},
\qquad
\frac{d}{dD}\Psi(\alpha^*(D),D)=\frac{c_0}{b_0+D}.
$$

The first is the derivative of the bare product; the second is the envelope derivative of the complete optimized sector. They differ except at $D=0$ and produce different forces. With a fixed or envelope-selected coefficient, $\alpha_i$ must multiply the prior contribution in both mean and covariance gradients and in the corresponding frozen-coefficient Hessian blocks.

## Comparative context

Mechanics on probability spaces predates this program. [[chirco-2022-statistical-bundle-dynamics]], [[leok-zhang-2017-information-geometric-mechanics]], and [[pistone-2018-statistical-bundle-lagrangian]] show explicit statistical-bundle or divergence-to-mechanics constructions. [[martins-2015-opinion-particles]] supplies a direct inertial opinion-particle predecessor. These sources support a carefully scoped kinetic construction while ruling out novelty or necessity claims based only on using precision-like quantities as mass.

Under the primary first-order linearization, $\dot\delta=-\eta G^{-1}H_F\delta$. At fixed $G$ and $\eta$, a larger positive modal stiffness produces a smaller static displacement under matched constant forcing and a faster relaxation rate. It does not itself create revision latency. Slower revision requires an independently specified mobility or learning rate, damping law, kinetic metric, or slow explanatory state. The four-part stiffness also does not by itself derive confirmation bias, belief perseverance, expertise rigidity, or validation of Hamiltonian opinion dynamics.

## Sources

- [[belief-inertia-2026-07-12-theorem-first-revision]] -- corrected source for the stiffness theorem, three-geometry distinction, and kinetic degeneracy.
- [[belief-inertia]] -- immutable historical manuscript note.
- [[girolami-calderhead-2011-riemann-hmc]] -- position-dependent Fisher/Riemannian kinetic geometry.
- [[chirco-2022-statistical-bundle-dynamics]], [[leok-zhang-2017-information-geometric-mechanics]], [[pistone-2018-statistical-bundle-lagrangian]] -- statistical-bundle and geometric-mechanics precedents.
- [[martins-2015-opinion-particles]] -- direct opinion-inertia comparator.

## See also

- [[Belief inertia]]
- [[Hamiltonian belief dynamics]]
- [[Fisher information metric]]
- [[Natural gradient]]
- [[Multi-agent variational free energy]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
