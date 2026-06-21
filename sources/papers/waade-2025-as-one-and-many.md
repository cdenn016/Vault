---
type: paper
title: "As One and Many: Relating Individual and Emergent Group-Level Generative Models in Active Inference"
aliases:
  - "Waade et al. 2025"
  - "Waade (2025) As One and Many"
authors:
  - Waade, Peter Thestrup
  - Olesen, Christoffer Lundbak
  - Laursen, Jonathan Ehrenreich
  - Nehrer, Sebastian Werner
  - Heins, Conor
  - Friston, Karl
  - Mathys, Christoph
year: 2025
arxiv: null
url: https://doi.org/10.3390/e27020143
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/social-physics
  - cluster/social-physics/opinion-dynamics
  - project/multi-agent
  - project/social-physics
  - field/neuroscience
  - field/psychology
  - field/philosophy
  - field/statistics
status: stable
created: 2026-06-19
updated: 2026-06-20
---

# As One and Many: Relating Individual and Emergent Group-Level Generative Models in Active Inference

> [!info] Citation
> Waade, P. T., Olesen, C. L., Laursen, J. E., Nehrer, S. W., Heins, C., Friston, K., & Mathys, C. (2025). "As One and Many: Relating Individual and Emergent Group-Level Generative Models in Active Inference." *Entropy* **27**(2), 143. https://doi.org/10.3390/e27020143

## TL;DR

Develops the claim that a collective of active-inference agents can itself constitute a single higher-level active-inference agent, provided the collective maintains a group-level Markov blanket. The paper offers a data-driven methodology for characterizing the relationship between the generative model of the emergent group-level agent and the dynamics of its constituent individuals — when does a group "have a mind of its own," and how does the group model relate to the models nested inside it. This is the active-inference counterpart of the project's meta-agent: a principled account of when and how coarse-graining a cluster of agents yields a well-defined agent at the next scale up.

## Problem & setting

The free-energy principle is scale-free: anything maintaining a Markov blanket can be described as minimizing free energy. So a group of agents might be describable as a single agent — but only under conditions. The paper asks when the group-level description is licensed (when there is a genuine group-level Markov blanket separating the collective's internal states from its environment) and how to recover the group generative model empirically from the joint dynamics of the members, using tools from computational cognitive modeling and computational psychiatry.

## Method

The authors set up nested active-inference systems: individual agents with their own generative models, and a candidate group-level model whose states are functions of the members' states. They propose fitting and characterizing the group-level model from simulated or observed individual trajectories, testing whether the group's behavior is well-described as a single generative model and how the group's parameters map onto the constituents'. The methodology is presented as applicable beyond active inference to other modeling frameworks for emergent collective cognition.

## Key results

- A collective constitutes a bona fide group-level active-inference agent exactly when it sustains a group-level Markov blanket; otherwise the single-agent description of the group is not licensed.
- The group-level generative model can be related quantitatively to the dynamics of its constituent agents — the "one and many" relation is made tractable rather than purely conceptual.
- The construction is genuinely hierarchical and recursive: group-agents can themselves be constituents of still-higher agents.

## Relevance to this research

This paper is the active-inference theory underwriting the project's [[Meta-agents and hierarchical emergence]] and [[Ouroboros multi-scale dynamics]]. The Ouroboros tower is precisely a stack of nested agents in which a scale-$(s{+}1)$ meta-agent is a coarse-graining of a cluster of scale-$s$ agents, and Waade et al. supply the criterion — a group-level Markov blanket — for when such a meta-agent is well-defined rather than an artifact of pooling. The project's meta-agent formation (gauge-covariant pooling of constituent $(\mu,\Sigma,\phi)$ into a meta belief, with coherence weights $w_i$) is one concrete realization of "relating the group model to its constituents"; the coherence weight $w_i \propto \exp(-\mathrm{KL}(q_i \| \bar{q}_I))$ operationalizes how tightly the cluster must cohere for the group description to hold, which is the project's quantitative stand-in for the Markov-blanket condition. The recursive nesting Waade et al. license is exactly the Ouroboros' apex closure and cross-scale shadow priors. Where this paper diagnoses when a group is an agent, PIFB (see [[participatory-it-from-bit]]) additionally specifies how beliefs transport between scales via the gauge connection $\Omega_{i,I}$, so the parent's beliefs become the constituents' priors covariantly. This reference is the most direct external validation that the project's multi-scale agent tower is a legitimate active-inference construction.

## Cross-links

- Concepts: [[Ouroboros multi-scale dynamics]], [[Meta-agents and hierarchical emergence]], [[Collective active inference]], [[Multi-agent variational free energy]]
- Related sources: [[friston-2024-federated-inference]], [[heins-2024-surprise-minimization]], [[albarracin-2022-epistemic-communities]]
- Manuscript: [[participatory-it-from-bit]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{waade2025asone,
  author    = {Waade, Peter Thestrup and Olesen, Christoffer Lundbak and Laursen, Jonathan Ehrenreich and Nehrer, Sebastian Werner and Heins, Conor and Friston, Karl and Mathys, Christoph},
  title     = {As One and Many: Relating Individual and Emergent Group-Level Generative Models in Active Inference},
  journal   = {Entropy},
  volume    = {27},
  number    = {2},
  pages     = {143},
  year      = {2025},
  doi       = {10.3390/e27020143},
  publisher = {MDPI}
}
```
