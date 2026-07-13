---
type: concept
title: Sociophysics
aliases:
  - Physics of social dynamics
tags:
  - cluster/social-physics
  - cluster/multi-agent
  - project/social-physics
  - project/multi-agent
status: stable
created: 2026-06-19
updated: 2026-07-13
---

# Sociophysics

## Definition

**Sociophysics** applies statistical-physics, network, kinetic, and dynamical-systems methods to collective social behavior. Its canonical models isolate different mechanisms: averaging, anchoring, bounded confidence, signed influence, majority rules, contagion, synchronization, and second-order response. The surveys [[castellano-2009-statistical-physics-social-dynamics]], [[galam-2008-sociophysics]], and [[jusup-2022-social-physics]] map this broader field.

## Position of the gauge-VFE program

The [[SocialPhysics]] project contributes an engineered gauge-covariant consensus energy for distribution-valued beliefs in heterogeneous local frames. Entropy-retaining attention optimization gives a canonical log-partition objective, and the local Gaussian loss Hessian separates into prior, sensory, incoming relational, and outgoing relational or recoil stiffness. The primary dynamics are Fisher--Rao [[Natural gradient|natural-gradient]] flow. [[Belief inertia]] is a conditional kinetic extension, not a consequence of sociophysics, VFE, or the [[Fisher information metric]]. The corrected source is [[belief-inertia-2026-07-12-theorem-first-revision]].

The contribution should be compared directly with established opinion and probability mechanics. [[martins-2015-opinion-particles]] already gives Bayesian-inspired opinion particles with inertia and a harmonic example. [[xue-hirche-cao-2020-opinion-port-hamiltonian]] applies port-Hamiltonian methods to controlled opinion networks. [[baumann-sokolov-tyloo-2020-second-order-consensus]] shows network resonance in second-order consensus. [[sampson-porter-restrepo-2025-oscillatory-opinion]] generates self-sustained and excitable opinions through group feedback without the proposed kinetic metric. These comparators make oscillation, resonance, or Hamiltonian terminology non-novel and non-diagnostic by themselves.

## Exact status of the social correspondences

- **DeGroot:** under the primary unweighted product Fisher metric, derived only for fixed symmetric coupling under flat transport and common fixed covariance. Nonuniform reversible DeGroot additionally requires the $\rho$-weighted metric $G_\rho$, a fixed-label joint family, or equivalent agent-specific rates. General directed row-stochastic dynamics are outside the scalar derivation.
- **Friedkin--Johnsen:** a restricted anchored equilibrium correspondence inheriting the same symmetric/weighted-reversible metric scope. Heterogeneous susceptibility requires agent-indexed prior precision or coupling; the general directed iteration is not derived.
- **Bounded confidence:** Gibbs similarity weighting is a soft finite-temperature analog. It is not an exact Hegselmann--Krause ball average or Deffuant update.
- **Polarization:** positive finite-temperature attractive attention yields metastable separation in the stated unanchored, symmetric reciprocal two-cluster reduction. Stable polarization requires added support, anchors, repulsion, or active sampling.
- **Social Impact Theory:** interpretive only. Row-normalized attention redistributes a fixed allocation and does not derive Latan\'e's increasing-number or multiplicative strength--immediacy--number law.
- **Diffusion:** not derived. A population S-curve requires an explicit adoption state and hazard, with [[bass-1969-product-growth]] as the formal comparator.
- **Confirmation bias and perseverance:** selective exposure, first-order stiffness response, kinetic latency, and persistence of an explanatory state are different mechanisms. At fixed Fisher geometry and learning rate, larger positive stiffness speeds linear relaxation; slower revision needs a separate mobility, damping, kinetic, or slow-state mechanism.

## Behavioral and mechanics comparators

[[nevin-mandell-atak-1983-behavioral-momentum]] operationalizes resistance to disruption in conditioned behavior. It is a useful experimental-design precedent, not validation of opinion-level Hamiltonian dynamics. [[chirco-2022-statistical-bundle-dynamics]], [[leok-zhang-2017-information-geometric-mechanics]], [[pistone-2018-statistical-bundle-lagrangian]], and [[girolami-calderhead-2011-riemann-hmc]] establish that information-geometric and statistical-bundle mechanics also predate this program. The residual novelty is the gauge-transported Gaussian KL consensus potential, optimized attention, and four-part local relational stiffness with an explicitly conditional kinetic reading.

## Sources

- [[belief-inertia-2026-07-12-theorem-first-revision]] -- revised theorem and claim-status record.
- [[martins-2015-opinion-particles]] -- direct opinion-particle predecessor.
- [[nevin-mandell-atak-1983-behavioral-momentum]] -- behavioral resistance-to-disruption comparator.
- [[xue-hirche-cao-2020-opinion-port-hamiltonian]] -- port-Hamiltonian opinion-network comparator.
- [[baumann-sokolov-tyloo-2020-second-order-consensus]] -- second-order consensus and parametric resonance.
- [[bass-1969-product-growth]] -- formal population diffusion model.
- [[sampson-porter-restrepo-2025-oscillatory-opinion]] -- alternative non-inertial oscillation mechanism.
- [[castellano-2009-statistical-physics-social-dynamics]], [[galam-2008-sociophysics]], [[jusup-2022-social-physics]] -- field surveys.

## See also

- [[Statistical physics of social systems and collective behavior]]
- [[Opinion dynamics]]
- [[Echo chambers and polarization]]
- [[Belief perseverance and confirmation bias]]
- [[Multi-agent variational free energy]]
- [[Hamiltonian belief dynamics]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
