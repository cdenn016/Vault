---
type: theme
title: "Active inference communication and collective boundaries"
aliases:
  - "Communication policies and collective boundaries"
tags:
  - cluster/vfe
  - cluster/multi-agent
  - cluster/attention
  - cluster/social-physics
  - project/multi-agent
  - project/transformer
  - project/social-physics
status: draft
created: 2026-11-07
updated: 2026-11-13
---

# Active inference communication and collective boundaries

Communication can change what an agent observes, what another agent infers, and which interactions persist. The literature supplies distinct constructions for these effects: active selection of evidence, pragmatic models of a listener, learned message channels, and collective boundaries. They answer different questions. This targeted reading map connects them to [[Collective active inference]], [[Communication-constrained inference]], [[Expected Free Energy]], [[GL(K) gauge-equivariant attention]], and [[Markov Blanket]]. It is not a systematic review or a priority claim.

## Communication as inference and action

[[friston-frith-2015-duet]] studies alternating speaking and listening in agents with a shared generative model. Its generalized synchrony is a result within that construction; the shared-model premise matters when comparing it with agents whose interpretations or preferences differ. [[friston-frith-2015-hermeneutics]] develops the communication account through both state inference and perceptual learning. This separates rapid interpretation of a signal from changes in the parameters used to interpret later signals.

[[albarracin-2022-epistemic-communities]] already gives each agent two simultaneous action choices: which expression to produce and which neighboring agent to observe. The simulations vary epistemic confirmation bias and habits to study polarization. Sections 2.5 and 2.12 of the [primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC9027706/) specify the actions and the supplied Erdős–Rényi neighbor network. Selective observation operates within this network; the formation of epistemic communities is not a demonstration of a collective conditional-independence blanket.

Pragmatic communication makes the receiver's response part of the sender's decision. In [[frank-goodman-2012-pragmatic-reasoning]], a speaker chooses utterances through a model of a listener, and a pragmatic listener reasons about the speaker's selection. [[maisto-2024-interactive-inference]] studies a related mechanism in cooperative joint action: movements can communicate a goal through their legibility to a partner. These models supply semantic, contextual, or cooperative structure rather than deriving unrestricted alignment between arbitrary private models.

The 2026 preprint [[gwon-2026-evidence-intervention]] is a close comparator for communication selected by anticipated interpretation. The listener's utterance likelihood is an attributed speaker policy, including its state-dependent normalizer. The construction distinguishes current pragmatic-state inference, learning about a partner, and prospective policy evaluation. An utterance can influence a partner and provide evidence about that partner. The [paper's Sections 3.6–3.7 and 3.10–3.12](https://arxiv.org/pdf/2610.04347) should be consulted before treating this policy-level coupling as a new feature. The preprint does not establish a gauge-geometric channel or autonomous collective-boundary formation.

## Individual objectives and policy scope

[[ruiz-serra-2025-factorised-active-inference]] permits distinct preferences in general-sum games by giving agents factorized beliefs about other agents' policy states. Its simulated ensemble EFE need not decrease. That observation concerns the paper's games and objective; it is not a theorem excluding every collective potential. Conversely, coupling several individually defined objectives does not itself supply a common descent function.

[[millidge-2021-whence-expected-free-energy]] explains why future-directed policy selection requires its own declared construction. Carrying present-time VFE into the future does not uniquely produce the epistemic term used in EFE. A comparison between communication mechanisms must therefore identify the predictive law, preferences, policy set, and posterior assumptions. A softmax form alone does not identify the functional being optimized. See [[Expected Free Energy]] for the conventional decompositions and their scope.

## Learning content, access, and interpretation

[[das-2019-tarmac]] learns message values, targeting signatures, and receiver queries, with multiple communication rounds available before action. Its main training objective is task return with a centralized critic. [[kim-2019-schednet]] separates message encoding from access to a scarce channel: learned priorities feed a prescribed scheduler, and selected senders broadcast. Pair-specific targeting and allocation of broadcast access are different communication decisions.

[[wang-2020-information-bottleneck-communication]] combines learned stochastic messages, recipient aggregation, and information-bottleneck penalties. Its task-return objective is not automatically EFE. [[lin-2021-autoencoder-communication]] instead uses reconstruction of an agent's own observation to ground outgoing symbols while agents learn independently. The auxiliary decoder supplies an encoding objective; it is not the receiving agent's interpretation model. Together these papers distinguish learning what to express, learning when an exchange is useful, and learning how a recipient responds.

[[hansen-ghrist-2021-discourse-sheaves]] is a geometric comparator for selective expression. Private vector spaces communicate through edge-specific discourse spaces and restriction maps, with constructions that adapt opinions or expression maps. Its discrepancy dynamics do not supply independent EFE policies. [[taniguchi-2024-collective-predictive-coding]] connects learned symbols to decentralized inference over shared latent representations. Its constructive naming-game examples retain their model assumptions, while the broader collective predictive coding claim is presented as a hypothesis.

> [!note] Editorial: Channel rank, channel capacity, and semantic agreement require separate specifications. A lower-dimensional real-valued message is not a bit budget without an alphabet, noise law, precision, or coding convention. A learned encoder is also not evidence that two agents attach the same meaning to its outputs. [[Communication-constrained inference]] records the statistical resource distinction; the papers above provide different choices of learning objective and communication protocol.

## Supplied roles and collective formation

[[palacios-2020-hierarchical-markov-blankets]] is a direct precedent for formation when agents have priors about possible roles. Elements use short-range signaling and infer their roles in a higher-level internal, sensory, active, or external arrangement. Membership is not fixed in advance, but possible roles are supplied by the model. Its simulations do not establish that arbitrary private objectives produce a blanket. [[heins-2024-surprise-minimization]] provides a collective-motion mechanism based on local active inference; coordinated movement is a different result from screening-off under a specified joint law.

[[waade-2025-as-one-and-many]] fits a group-level generative description to a collective with a predefined sensory/internal/active arrangement. This is useful for relating group and individual descriptions once the boundary is supplied. It should not be cited as a demonstration of autonomous role formation or as validation of an arbitrary coherence-based coarse-graining.

The flock preprint [[maisto-2025-flock-joint-agency]] reports collective responses and synergistic information alongside a blanket interpretation. [Appendix A.4 of version 2](https://arxiv.org/html/2511.10835v2) constructs a graph from shared headings over a time window and assigns boundary labels by thresholding a Fiedler vector. This is the paper's stated spectral identification procedure.

> [!note] Editorial: The spectral procedure supplies candidate boundary labels; it does not by itself demonstrate conditional independence under the simulation's joint probability law. The immutable flock source note's statement that the method tests conditional-dependence structure is stronger than this procedure supports. The collective-information results and the blanket interpretation should be assessed separately.

## Detection and the law being screened off

The preprint [[beck-2025-dynamic-markov-blanket-detection]] infers changing internal, boundary, and environment labels using a structured generative model. It explicitly distinguishes path statistics from steady-state statistics in [Section 2.1](https://arxiv.org/html/2502.21217v1). Its detection model constrains latent dynamics and label transitions. A successful fit therefore needs comparison with alternatives; it is not an explanation of why agents' EFE policies create that structure.

[[biehl-2021-technical-critique]] shows that particular FEP arguments use inequivalent blanket conditions and require additional assumptions. Drift sparsity and instantaneous conditional independence must be distinguished. This restricts the inference from interaction structure to statistical screening-off; it does not prohibit constructing agents with explicitly specified EFE objectives. See [[Markov blanket interpretation debate]].

> [!note] Editorial: A collective-boundary claim must identify the variables, partition, probability law, and time scope of the claimed independence. A community in a similarity graph, an interaction boundary, a steady-state blanket, and a path blanket are different objects. Neither a coordinate-frame convention nor low message rank supplies those missing statistical conditions. The geometric communication framework and the formation claim must be connected by an explicit model and evidence.

## Error terms when a collective is only approximately closed

The sources above ask when a set of agents has a boundary and a model of its own. A separate question is what such a collective loses when the coarse variables it models do not close. In a linear-Gaussian model of communicating agents, [[dennis-2026-collective-agents-approximate-meta-agent]] bounds the expected relative entropy from the exact predictive law to the belief of a collective that filters a non-closed coarse exterior with a Markov model, with no smallness condition, and assembles the bound with an exact coarse blanket and an exactly closed coarse internal state into an approximate form of the meta-agent theorem; for members that fuse literally it bounds the memory of their average. The blanket conditions are kept exact in these statements, so they complement the detection and critique literature of the preceding section and do not answer it. See [[Approximate meta-agent theorem]].

## Error terms when the coarse blanket conditions fail, November 11, 2026

The section on error terms above records statements in which the blanket conditions of the collective are exact. [[dennis-2026-collective-agents-approximate-blanket-conditions]] adds a theorem for the same linear-Gaussian model without them. It allows sensors that read hidden exterior coordinates, a coarse sensory state formed with other weights, sensors with memory or reafference, and an exterior that reads the members one by one, and it requires only the canonical partition, in which no internal and no active variable reads the exterior and the exterior reads no internal variable, per-channel noise, a stable joint process and members that run a consensus filter. In the terms of the editorial note of the preceding section, the theorem names its variables, law and time scope: the law that is computed exactly is that of the exterior given the paths of the members' sensory channels, and the belief of the collective is measured against it. The theorem does not establish that the coarse sensory state and the coarse act screen off, and it gives no bound on their leak through the defects of the declared models; it relates the leak on a window to the difference between measuring the belief against the members' channels and against a coarse record. It therefore still does not answer the detection and critique literature, and it adds to it one case in which an agent-like description with stated error terms survives the failure of the coarse blanket. See [[Approximate meta-agent theorem]] and [[Markov Blanket]].

## Federated inference and belief sharing, November 13, 2026

Where [[friston-frith-2015-duet]] and [[friston-frith-2015-hermeneutics]] treat two agents that take turns, [[friston-2024-federated-inference]] treats three that broadcast continuously, with a common generative model and an assumed common allocentric frame; [[Federated inference]] has the details. On the three questions separated above, what to express, when an exchange is useful and how a recipient responds, the paper fixes the first two by construction and learns the third only as a code. Expression is a readout of the posterior predictive distribution over each shared factor, and the only policy selected by expected free energy is the direction of gaze. There is no choice of partner, in contrast to [[albarracin-2022-epistemic-communities]]: every speaker enters with coefficient one. Interpretation is observation through a likelihood from beliefs to words. What the paper adds is learning of that likelihood by Dirichlet updates gated by expected free energy, and its emergence among naive agents through Bayesian model reduction. The paper states that a code that emerged in one simulated group would not let its agents communicate with agents from the earlier simulations (it runs no cross-group test), an instance of the distinction drawn in the editorial note of the section on learning content, access, and interpretation between a learned code and agreement on meaning.

## Reading route

Start with [[albarracin-2022-epistemic-communities]] for expression and selective observation, then [[das-2019-tarmac]] and [[hansen-ghrist-2021-discourse-sheaves]] for message architecture and partial expression. Read [[ruiz-serra-2025-factorised-active-inference]] with [[gwon-2026-evidence-intervention]] for distinct preferences and pragmatic policy coupling. Compare [[palacios-2020-hierarchical-markov-blankets]], [[waade-2025-as-one-and-many]], [[maisto-2025-flock-joint-agency]], and [[beck-2025-dynamic-markov-blanket-detection]] as four different treatments of roles and boundaries, keeping the conditions in [[biehl-2021-technical-critique]] explicit.

## Related

[[Collective active inference]] · [[Expected Free Energy]] · [[Communication-constrained inference]] · [[GL(K) gauge-equivariant attention]] · [[Markov Blanket]] · [[Meta-agents and hierarchical emergence]] · [[Decentralized Bayesian inference]] · [[Partial information decomposition]] · [[Collective agents literature map]]
