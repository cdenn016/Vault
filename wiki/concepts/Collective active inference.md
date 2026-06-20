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
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Collective active inference

## Definition

**Collective active inference** is the study of populations of active-inference agents whose joint dynamics are governed by a shared or federated free-energy objective, rather than by hand-coded interaction rules. Each member is an ordinary [[Free-energy principle active inference|active-inference]] system minimizing its own [[Variational free energy]] under a generative model of its local world, but the members are coupled: they sense, broadcast, or transport one another's beliefs, so the population's behavior — consensus, fragmentation, flocking, or the emergence of a group-level agent — falls out as a side effect of every member descending free energy. The field has three recurrent moves. First, **belief-sharing**: an agent treats a neighbor's communicated posterior as additional sensory evidence and integrates it by standard variational updating ([[friston-2024-federated-inference]]). Second, **group-level generative models**: a collective that sustains a group-level Markov blanket can itself be described as a single higher-order active-inference agent ([[waade-2025-as-one-and-many]]). Third, **emergent phases**: the same coupled dynamics that yield coherent collective motion ([[heins-2024-surprise-minimization]], [[couzin-2009-collective-cognition]]) can also splinter into self-reinforcing echo chambers ([[albarracin-2022-epistemic-communities]]).

## Why it matters here

Collective active inference is the external literature this project formalizes and extends. The belief-coupling energy of [[Multi-agent variational free energy]], $\sum_{ij}\beta_{ij}\,\mathrm{KL}(q_i\,\|\,\Omega_{ij}[q_j])$, *is* federated inference written as one functional: each agent pays a KL price for disagreeing with its (transported) neighbors, and the attention weights $\beta_{ij}$ decide whom to listen to — the closed-form analogue of "when and to whom to broadcast." The piece this project adds, and the reason it sits inside the participatory program of [[participatory-it-from-bit]], is the gauge transport $\Omega_{ij}$: neighbors hold beliefs in distinct local frames, and the connection re-expresses a broadcast belief in the receiver's frame before disagreement is measured. Standard federated belief-sharing is recovered as the flat-connection ($\Omega_{ij}=I$) special case. This ties directly to two PIFB threads: the consensus-versus-"heat death" phase structure (the project reads both consensus collapse and frozen fragmentation as opposite limits of a single gauge-covariant free-energy descent, with Albarracin's confirmation-biased sampling as the microfoundation of the fragmented limit), and the participatory loop in which an emergent collective becomes the prior on its own constituents.

## Details

Waade et al.'s group-level Markov-blanket criterion is the external counterpart of the project's meta-agent: the Ouroboros tower ([[Ouroboros multi-scale dynamics]]) stacks nested agents, and the coherence weight $w_i\propto\exp(-\mathrm{KL}(q_i\,\|\,\bar q_I))$ in [[Meta-agents and hierarchical emergence]] operationalizes how tightly a cluster must cohere for the group description to be licensed. Heins et al. couple agents *implicitly* through overlapping sensory fields and recover swarming, milling, and schooling as phases of surprise minimization; the project couples belief-carrying agents *explicitly* through transported KL, turning that phase diagram into a distributional, gauge-aware one. Couzin supplies the biological grounding that group cognition emerges from local rules without central control. Together these license reading the model as a sociophysics theory derived from free energy rather than postulated.

## Sources

- [[friston-2024-federated-inference]] — federated inference: belief-sharing as free-energy minimization, the FEP statement of the coupling term.
- [[heins-2024-surprise-minimization]] — collective motion phases from surprise minimization; the FEP-to-sociophysics bridge.
- [[waade-2025-as-one-and-many]] — when a collective is itself a group-level active-inference agent (group Markov blanket); active-inference counterpart of the meta-agent.
- [[albarracin-2022-epistemic-communities]] — confirmation-biased sampling and echo-chamber fragmentation; microfoundation of the "heat death" limit.
- [[couzin-2009-collective-cognition]] — collective cognition from local interactions; biological grounding.

## See also

- [[Multi-agent variational free energy]]
- [[Ouroboros multi-scale dynamics]]
- [[Meta-agents and hierarchical emergence]]
- [[participatory-it-from-bit]]
- [[Free-energy principle active inference]] · [[Variational free energy]]
