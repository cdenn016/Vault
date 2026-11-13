---
type: concept
title: "Collective active inference"
aliases:
  - "Collective active inference"
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
updated: 2026-11-13
---

# Collective active inference

## Definition

**Collective active inference** studies coupled active-inference agents whose beliefs, actions, or generative models interact. The literature includes belief sharing ([[friston-2024-federated-inference]]), collective motion from surprise minimization ([[heins-2024-surprise-minimization]]), group-level Markov blankets ([[waade-2025-as-one-and-many]]), and active evidence-selection policies that can segregate epistemic communities ([[albarracin-2022-epistemic-communities]]).

## Relation to gauge-VFE coupling

The engineered consensus energy in [[Multi-agent variational free energy]] compares beliefs after gauge transport and optimizes entropy-retaining attention rows. It is structurally related to federated belief sharing, but its full population energy is not one fixed state-level ELBO over the original agent states. The rowwise source interpretation requires an explicit source-independence assumption.

The primary belief update is Fisher--Rao natural-gradient flow. The optional kinetic extension of the belief-inertia manuscript is a separate modeling postulate and is not implied by collective active inference.

## Active sampling versus passive attention

The polarization mechanisms must remain distinct. [[albarracin-2022-epistemic-communities]] gives each agent both an expression action and a choice of which neighbor to observe. Active confirmation-biased sampling changes the evidence the agent receives within a supplied fixed random graph, allowing information environments to segregate. By contrast, positive finite-temperature Gibbs attention over a fixed candidate set is passive attractive reweighting. In the manuscript's unanchored, symmetric reciprocal two-cluster reduction, its cross-cluster tail remains positive, so separated clusters are metastable and continue to merge.

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

## Exact special cases, shared goals, and emergent collectives (2026-08-20)

The closest exact positive control is [[heins-2023-spin-glass-active-inference]]. Under a deliberately factorized generative model, symmetric pairwise precisions, and asynchronous updates, the agent ensemble reproduces Glauber or Boltzmann sampling. The equivalence is explicitly fragile: it does not license a generic collective free energy when symmetry, update scheduling, or the generative model changes. [[maisto-2024-interactive-inference]] and [[albarracin-2024-shared-protentions]] instead model reciprocal prediction and compositional shared goals. They clarify mechanisms of joint action without proving a fixed-joint ELBO for arbitrary interacting agents.

A second line treats communication as distributed inference over shared representations. [[taniguchi-2024-collective-predictive-coding]] frames symbol emergence as collective predictive coding, while [[hoang-2024-mh-naming-game]] supplies a Metropolis--Hastings naming-game construction. These categorical and communicative models are comparators for decentralized inference; their discrete label alignment is not the same mathematical problem as continuous gauge-frame transport.

Group agency remains conditional. [[palacios-2020-hierarchical-markov-blankets]] supplies possible blanket roles in agents' priors while allowing membership to develop through interaction. [[waade-2025-as-one-and-many]] fits a group-level model with a predefined blanket arrangement. [[maisto-2025-flock-joint-agency]] reports collective-information results and a flock-level blanket interpretation; its spectral boundary assignment is not itself a conditional-independence proof. These constructions do not supply a general emergence theorem. The recent preprints [[bouchaffra-2026-collective-variational-principle]] and [[bouchaffra-2026-coalition-free-energy]] use terminology close to a collective variational principle; they remain an unreviewed watchlist rather than established foundations.

## Communication policies and boundary evidence

[[gwon-2026-evidence-intervention]] is a recent preprint comparator for policies that anticipate a listener's interpretation, while [[beck-2025-dynamic-markov-blanket-detection]] addresses detection of changing boundaries under a structured model. Policy coupling and boundary detection answer separate questions. [[Active inference communication and collective boundaries]] compares these sources with learned communication architectures and records the distinction between supplied role priors, predefined arrangements, spectral communities, and law-specific screening-off.

> [!important] Current code scope
> MultiAgentELBO has no active-policy engine, game dynamics, naming-game protocol, posterior server,
> or reactive message scheduler. These papers define future comparators and negative controls, not
> current code behavior.

## Sources

- [[friston-2024-federated-inference]] -- federated belief sharing.
- [[heins-2024-surprise-minimization]] -- collective motion from surprise minimization.
- [[waade-2025-as-one-and-many]] -- group-level active-inference agents.
- [[albarracin-2022-epistemic-communities]] -- active confirmation-biased sampling and epistemic-community segregation.
- [[ruiz-serra-2025-factorised-active-inference]] -- strategic factorized beliefs and model-specific ensemble-EFE dynamics.
- [[fukuoka-2026-variational-bayes-naming-game]] -- decentralized variational inference for shared signs.
- [[heins-2023-spin-glass-active-inference]] -- exact but fragile spin-glass equivalence under explicit structural assumptions.
- [[maisto-2024-interactive-inference]] -- reciprocal prediction and cooperative joint action.
- [[albarracin-2024-shared-protentions]] -- compositional treatment of shared goals.
- [[taniguchi-2024-collective-predictive-coding]] -- collective predictive coding and symbol emergence.
- [[hoang-2024-mh-naming-game]] -- Metropolis--Hastings naming game as decentralized inference.
- [[palacios-2020-hierarchical-markov-blankets]] -- conditional micro-to-macro Markov-blanket construction.
- [[maisto-2025-flock-joint-agency]] -- simulated higher-order blanket and collective information.
- [[bouchaffra-2026-collective-variational-principle]] -- unreviewed collective-variational-principle preprint.
- [[bouchaffra-2026-coalition-free-energy]] -- unreviewed coalition-free-energy preprint.

## See also

- [[Multi-agent variational free energy]]
- [[Echo chambers and polarization]]
- [[SocialPhysics]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
- [[Ouroboros multi-scale dynamics]]
- [[Meta-agents and hierarchical emergence]]

## Fields communication literature and the federated comparison

The Fields collection connects collective inference to physical interfaces, reference alignment, memory, and persistent organization. [[fields-2025-thoughts-and-thinkers-on-the-complementarity-between-objects-and-processes]] interprets biological collectives as interacting systems with memories; [[prentner-2019-using-ai-methods-to-evaluate-a-minimal-model-for-perception]] provides a toy perceptual-network construction but explicitly leaves endogenous embodiment and autonomous fitness feedback open. These sources clarify the difference between a collective pattern and an agent with a defined interface.

> [!warning] Scope correction to an earlier source interpretation
> The immutable note [[friston-2024-federated-inference]] describes the project's transported peer-KL term as exactly federated inference and suggests a flat-connection equivalence. That equivalence is not established by the paper. A reduction requires matching the generative model, communication likelihood, variational family, and treatment of dependent evidence. The current synthesis retains federated inference as a model-specific comparator. The newly retrieved [local PDF](../../sources/pdfs/friston-2024-federated-inference.pdf) is available for direct consultation.

[[Chris Fields and physics as communication]] supplies the complete reading map. Its quantum and thermodynamic strands should not be used to infer a single global ELBO merely from coupled individual objectives.

## Collective agents references, November 10, 2026

[[Collective agents literature map]] groups the references ingested on November 10, 2026. Its sections on communication as action and on active inference, expected free energy and Markov blankets hold the sources closest to this page, among them [[catal-2025-belief-sharing-blessing]], [[kaufmann-2021-active-inference-model]], [[kastel-2023-small-steps-mankind]] and [[nomura-2026-social-reality-construction]].

## Federated inference in detail, November 13, 2026

[[Federated inference]] now holds the detailed account of [[friston-2024-federated-inference]], written from the full published article, and this page keeps a summary. Three sentinel agents with a common generative model and an assumed common allocentric frame infer the location, proximity and pose of a subject that each of them sees only in part. The only action selected by expected free energy is the direction of gaze. Speech is a readout: each agent broadcasts its posterior predictive distribution over every shared factor through an auditory modality, and the others read the broadcast as an observation through an identity or permutation likelihood, which the paper shows for the identity likelihood (and asserts for any permutation) to be formally the addition of the speakers' log posteriors with unit coefficients (its Eqs. 6 to 8). The likelihood from beliefs to words is learned by Dirichlet updates gated by expected free energy, and three naive agents arrive at a common code through Bayesian model reduction. The paper assumes the common frame and constructs no group-level agent. The scope correction recorded above remains in force, and the dedicated page states what a reduction to the transported peer-KL energy would require.
