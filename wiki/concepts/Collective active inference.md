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
updated: 2026-08-10
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

## Strategic and decentralized comparators

[[ruiz-serra-2025-factorised-active-inference]] gives each agent explicit factorized beliefs about
other agents in iterated two- and three-player general-sum games. In that model's numerical
analysis, ensemble expected free energy is not necessarily minimized at the aggregate level. This
is a model-specific result about the simulated game and EFE construction, not a theorem that no
collective potential can arise from individual objectives.

[[fukuoka-2026-variational-bayes-naming-game]] provides a different finite comparator: agents with
partial observations exchange discrete signs and use local variational-Bayes updates to approximate
a shared-symbol posterior. The paper compares the decentralized protocol with a centralized VB
topline and a sampling-based naming game. Its categorical/multinomial model and communication
protocol do not establish an exact decomposition for an arbitrary correlated gauge-coupled law.

These two sources should remain distinct. Ruiz-Serra et al. study strategic policy selection with
EFE; Fukuoka et al. study decentralized variational inference for a shared latent sign. Neither is
implemented by the current MultiAgentELBO exact finite evaluator.

> [!important] Current code scope
> MultiAgentELBO has no active-policy engine, game dynamics, naming-game protocol, posterior server,
> or reactive message scheduler. These papers define future comparators and negative controls, not
> current code behavior.

## Sources

- [[friston-2024-federated-inference]] -- federated belief sharing.
- [[heins-2024-surprise-minimization]] -- collective motion from surprise minimization.
- [[waade-2025-as-one-and-many]] -- group-level active-inference agents.
- [[albarracin-2022-epistemic-communities]] -- active confirmation-biased sampling and epistemic-community segregation.
- [[belief-inertia-2026-07-12-theorem-first-revision]] -- passive-attention metastability and kinetic scope.
- [[ruiz-serra-2025-factorised-active-inference]] -- strategic factorized beliefs and model-specific ensemble-EFE dynamics.
- [[fukuoka-2026-variational-bayes-naming-game]] -- decentralized variational inference for shared signs.

## See also

- [[Multi-agent variational free energy]]
- [[Echo chambers and polarization]]
- [[SocialPhysics]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
- [[Ouroboros multi-scale dynamics]]
- [[Meta-agents and hierarchical emergence]]
