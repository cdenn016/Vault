---
type: project
title: "SocialPhysics"
aliases:
  - "Social Physics"
  - "Social Physics Program"
  - "Sociophysics VFE"
  - "Belief Dynamics Program"
tags:
  - cluster/social-physics
  - cluster/vfe
  - cluster/multi-agent
  - project/social-physics
status: draft
created: 2026-06-19
updated: 2026-07-13
---

# SocialPhysics

## Goal

SocialPhysics develops a mathematical sociophysics model for distribution-valued beliefs in heterogeneous local frames. Its theorem-level contribution is an engineered gauge-covariant consensus energy with entropy-retaining optimized attention and a local Gaussian loss Hessian that separates prior, sensory, incoming relational, and outgoing relational or recoil stiffness. Fisher--Rao [[Natural gradient|natural-gradient]] flow is the primary dynamics. A second-order [[Belief inertia]] interpretation is conditional on a separately declared positive kinetic metric.

The current manuscript is recorded in [[belief-inertia-2026-07-12-theorem-first-revision]], with the final metric, stiffness, and hash reconciliation in [[belief-inertia-2026-07-13-final-verification-addendum]]. The historical [[belief-inertia]] note remains immutable and should not be used for the revised proof statuses where the records differ.

## Mathematical core

For transported edge energies $E_{ij}=D_{\mathrm{KL}}(q_i\|\Omega_{ij\#}q_j)$, the canonical social row retains both expected edge energy and categorical relative entropy:

$$
\sum_j\left[
\beta_{ij}E_{ij}
+\tau\beta_{ij}\log\frac{\beta_{ij}}{\pi_{ij}}
\right].
$$

Row optimization gives $\beta_{ij}^*=\pi_{ij}e^{-E_{ij}/\tau}/Z_i$, reduced value $-\tau\log Z_i$, and envelope gradient $\sum_j\beta_{ij}^*dE_{ij}$. The construction is an engineered consensus energy. A source-mixture interpretation requires the stated rowwise source-independence assumption; the entire population functional is not presented as one fixed generative-model ELBO over the original agent states.

At frozen optimized attention and local gauge consensus,

$$
[H_{\mu\mu}]_{ii}
=\alpha_i\bar\Lambda_{p_i}+\Lambda_{o_i}
+\sum_k\beta_{ik}\widetilde\Lambda_{q_k}
+\sum_j\beta_{ji}\Lambda_{q_i}.
$$

This is local stiffness $H_F$, not automatically the intrinsic Fisher metric $G$ or kinetic mass $M$. If a conditional kinetic model sets $M=H_F$ while the same $H_F$ supplies the restoring force, the generalized spectrum is $\omega^2=1$ up to scale. Nontrivial modal predictions require independently identified kinetic and restoring tensors.

For the first-order linearization $\dot\delta=-\eta G^{-1}H_F\delta$, fixed $G$ and $\eta$ make larger positive modal stiffness reduce the matched-force static displacement and increase the relaxation rate. Slower revision requires a separate mobility or learning rate, damping law, kinetic metric, or slow explanatory state.

## Social claim-status map

- **DeGroot:** under the primary unweighted product Fisher metric, derived only for fixed symmetric coupling. Nonuniform reversible coupling requires the additional $\rho$-weighted metric, a fixed-label joint family, or equivalent agent-specific rates. General directed row-stochastic influence is excluded.
- **Friedkin--Johnsen:** restricted anchored stationary equilibrium of the reversible scalar energy, independent of the positive flow metric; matching its standard transient requires $G_\rho$ or agent-specific rates; heterogeneous susceptibility requires agent-indexed anchor precision or coupling.
- **Bounded confidence:** Gibbs attention is a soft finite-temperature analog, not an exact hard-threshold recovery.
- **Polarization:** positive finite-temperature attractive coupling gives metastable separation in the stated unanchored, symmetric reciprocal two-cluster reduction. Exact persistence needs additional support, anchors, repulsion, or active sampling.
- **Social Impact Theory:** interpretive only; normalized attention does not reproduce Latan\'e's number law.
- **Diffusion:** not derived. An adoption variable and hazard are required, with [[bass-1969-product-growth]] as the direct population comparator.
- **Confirmation bias:** only similarity-weighted selective exposure conditional on the kernel is represented.
- **Belief perseverance:** a conditional kinetic coast is a candidate mechanism; first-order stiffness alone does not produce latency, and explanatory perseverance requires a slow explanatory state.
- **Leadership/recoil:** contemporaneous source-role curvature, not accumulated social memory or inevitable rigidity.

## Direct comparison set

[[martins-2015-opinion-particles]] is the closest direct predecessor for inertial opinion particles and a harmonic example. [[nevin-mandell-atak-1983-behavioral-momentum]] operationalizes resistance to disruption but does not establish opinion-level Hamiltonian mechanics. [[xue-hirche-cao-2020-opinion-port-hamiltonian]] applies port-Hamiltonian systems and passivity to opinion networks. [[baumann-sokolov-tyloo-2020-second-order-consensus]] provides a second-order network-resonance baseline. [[sampson-porter-restrepo-2025-oscillatory-opinion]] demonstrates oscillatory and excitable opinions without the proposed kinetic mechanism. [[bass-1969-product-growth]] is the required diffusion comparator.

Probability-space mechanics is also prior art: [[chirco-2022-statistical-bundle-dynamics]], [[girolami-calderhead-2011-riemann-hmc]], [[leok-zhang-2017-information-geometric-mechanics]], and [[pistone-2018-statistical-bundle-lagrangian]]. The residual novelty is the gauge-transported Gaussian KL consensus potential, optimized attention, four-part local relational stiffness, and a conditional kinetic reading.

## Relationship to sibling projects

The [[Gauge-Theoretic Multi-Agent VFE Model]] supplies the broader multi-agent computational architecture, and the [[VFE Transformer Program]] supplies the language-model instantiation of related gauge-transported VFE machinery. SocialPhysics is the focused social-dynamics interpretation. It does not import the broader participatory-physics scope of [[participatory-it-from-bit]].

## Status and next tests

The theorem-first revision makes no new empirical-data or validation claim. The next discriminating experiments should estimate or manipulate Fisher geometry, restoring stiffness, any kinetic metric, damping, candidate-set selection, and slow explanatory state separately. Oscillation alone is insufficient because time-varying coupling and group feedback supply alternative mechanisms. The detailed literature map is [[Statistical physics of social systems and collective behavior]].

## Concepts

[[Opinion dynamics]] · [[Bounded confidence]] · [[Sociophysics]] · [[Echo chambers and polarization]] · [[Belief perseverance and confirmation bias]] · [[Belief inertia]] · [[Mass as Fisher information]] · [[Hamiltonian belief dynamics]] · [[Multi-agent variational free energy]] · [[Fisher information metric]] · [[Natural gradient]] · [[Collective active inference]]
