---
type: concept
title: "Collective active inference"
aliases:
  - "Collective active inference"
  - "Federated inference"
  - "Group-level active inference"
  - "Multi-agent active inference"
tags:
  - cluster/multi-agent
  - cluster/social-physics
  - cluster/vfe
  - project/multi-agent
  - project/social-physics
status: stable
created: 2026-06-19
updated: 2026-07-12
---

# Collective active inference

## Definition

**Collective active inference** studies coupled active-inference agents whose beliefs, actions, or generative models interact. The literature includes belief sharing ([[friston-2024-federated-inference]]), collective motion from surprise minimization ([[heins-2024-surprise-minimization]]), group-level Markov blankets ([[waade-2025-as-one-and-many]]), and active evidence-selection policies that can segregate epistemic communities ([[albarracin-2022-epistemic-communities]]).

## Relation to gauge-VFE coupling

The engineered consensus energy in [[Multi-agent variational free energy]] compares beliefs after gauge transport and optimizes entropy-retaining attention rows. It is structurally related to federated belief sharing, but its full population energy is not one fixed state-level ELBO over the original agent states. The rowwise source interpretation requires the explicit source-independence fence recorded in [[vfe-population-generative-status-2026-07-12]].

The primary belief update is Fisher--Rao natural-gradient flow. The optional kinetic extension in [[belief-inertia-2026-07-12-theorem-first-revision]] is a separate modeling postulate and is not implied by collective active inference.

## Active sampling versus passive attention

The polarization mechanisms must remain distinct. [[albarracin-2022-epistemic-communities]] uses active confirmation-biased sampling: policy selection changes which evidence enters an agent's candidate set, allowing information environments to segregate. By contrast, positive finite-temperature Gibbs attention over a fixed candidate set is passive attractive reweighting. In the manuscript's unanchored, symmetric reciprocal two-cluster reduction, its cross-cluster tail remains positive, so separated clusters are metastable and continue to merge.

Passive attention therefore does not inherit the persistent-polarization result of an active-sampling model. Exact separation needs severed support, persistent anchors with a proved separated equilibrium, signed influence, or an explicit active selection policy. See [[Echo chambers and polarization]].

## Sources

- [[friston-2024-federated-inference]] -- federated belief sharing.
- [[heins-2024-surprise-minimization]] -- collective motion from surprise minimization.
- [[waade-2025-as-one-and-many]] -- group-level active-inference agents.
- [[albarracin-2022-epistemic-communities]] -- active confirmation-biased sampling and epistemic-community segregation.
- [[belief-inertia-2026-07-12-theorem-first-revision]] -- passive-attention metastability and kinetic scope.

## See also

- [[Multi-agent variational free energy]]
- [[Echo chambers and polarization]]
- [[SocialPhysics]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
- [[Ouroboros multi-scale dynamics]]
- [[Meta-agents and hierarchical emergence]]
