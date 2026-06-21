---
type: paper
title: "Collective Behavior from Surprise Minimization"
aliases:
  - "Heins et al. 2024"
  - "Heins (2024) Surprise Minimization"
authors:
  - Heins, Conor
  - Millidge, Beren
  - Da Costa, Lancelot
  - Mann, Richard P.
  - Friston, Karl J.
  - Couzin, Iain D.
year: 2024
arxiv: "2307.14804"
url: https://doi.org/10.1073/pnas.2320239121
tags:
  - cluster/vfe
  - cluster/multi-agent
  - cluster/social-physics
  - cluster/social-physics/social-influence
  - project/multi-agent
  - project/social-physics
  - field/biology
  - field/neuroscience
  - field/physics
  - field/cs-ml
status: stable
created: 2026-06-19
updated: 2026-06-20
---

# Collective Behavior from Surprise Minimization

> [!info] Citation
> Heins, C., Millidge, B., Da Costa, L., Mann, R. P., Friston, K. J., & Couzin, I. D. (2024). "Collective behavior from surprise minimization." *Proceedings of the National Academy of Sciences* **121**(17), e2320239121. DOI: [10.1073/pnas.2320239121](https://doi.org/10.1073/pnas.2320239121). Preprint: [arXiv:2307.14804](https://arxiv.org/abs/2307.14804).

## TL;DR

The canonical demonstration that collective motion — flocking, schooling, milling, swarming — emerges from individual agents each minimizing variational free energy (surprise) under a generative model of their local sensory world, with no explicit alignment, attraction, or repulsion forces imposed by hand. Each particle infers the hidden causes of its sensations (the positions and motions of visible neighbors) and acts to make its sensations conform to predictions; the familiar phases of collective behavior fall out as emergent consequences of this single imperative. It is the load-bearing bridge between the free-energy principle (FEP) and sociophysics: classic self-propelled-particle phenomenology is recovered from active inference rather than postulated.

## Problem & setting

Standard models of collective motion (Vicsek, Couzin zonal models, Boids) hard-code the interaction rules — alignment within one radius, attraction within another, repulsion at short range — and tune their weights to produce observed phases. The paper asks whether those rules can instead be derived from a first principle. Each agent is an active-inference particle with a generative model relating its hidden states (relative positions and headings of neighbors it can sense) to noisy sensory observations, and it both updates beliefs (perception) and moves (action) to minimize expected free energy.

## Method

Agents carry partially observed generative models over a local visual field. Perception is belief updating that minimizes variational free energy given current sensations; action selects movements that minimize expected free energy, i.e. that are expected to make future sensations least surprising under the model. The interaction structure is implicit: an agent's free energy depends on what it can sense of its neighbors, so coupling arises through shared, overlapping sensory fields rather than through a fixed force law. Sweeping the parameters of the generative model (sensory precision, field of view, preferred states) traces out a phase diagram of collective outcomes.

## Key results

- Swarming, milling (rotational vortices), and coherent directed schooling all emerge as distinct phases of a single surprise-minimizing dynamics, recovering the canonical collective-motion phenomenology without prescribed alignment/attraction/repulsion rules.
- The phases are organized by the agents' generative-model parameters (notably sensory precision and field of view), giving a first-principles re-derivation of what zonal models impose by hand.
- The work establishes a concrete, simulated FEP-to-sociophysics mapping: collective order is a side effect of each agent maximizing the evidence for its own model of its neighbors.

## Relevance to this research

This is the reference that licenses reading the [[Gauge-Theoretic Multi-Agent VFE Model]] as a sociophysics model derived from free-energy minimization rather than from hand-set interaction rules — the same move the project makes, generalized. Where Heins et al. couple agents implicitly through overlapping sensory fields, the project couples belief-carrying agents explicitly through the $\beta_{ij}\,\mathrm{KL}(q_i \| \Omega_{ij} q_j)$ term of [[Multi-agent variational free energy]], with the gauge transport $\Omega_{ij}$ supplying the piece this paper lacks: a frame-covariant way to compare beliefs held in different local reference frames before measuring their disagreement. PIFB (see [[participatory-it-from-bit]]) extends the surprise-minimization-as-collective-behavior thesis with that connection, so that emergent order is not just free-energy descent but gauge-covariant free-energy descent, and consensus, fragmentation, and the "heat death" of belief diversity become readable as phases of the coupled dynamics — the distributional, gauge-aware analogue of the phase diagram this paper draws. It also grounds the project's claim that meta-scale order ([[Meta-agents and hierarchical emergence]]) is emergent rather than imposed.

## Cross-links

- Concepts: [[Multi-agent variational free energy]], [[Meta-agents and hierarchical emergence]], [[Variational free energy]]
- Related sources: [[friston-2024-federated-inference]], [[waade-2025-as-one-and-many]], [[albarracin-2022-epistemic-communities]], [[couzin-2009-collective-cognition]], [[galam-2008-sociophysics]]
- Manuscript: [[participatory-it-from-bit]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{heins2024collective,
  author        = {Heins, Conor and Millidge, Beren and Da Costa, Lancelot and Mann, Richard P. and Friston, Karl J. and Couzin, Iain D.},
  title         = {Collective behavior from surprise minimization},
  journal       = {Proceedings of the National Academy of Sciences},
  volume        = {121},
  number        = {17},
  pages         = {e2320239121},
  year          = {2024},
  doi           = {10.1073/pnas.2320239121},
  eprint        = {2307.14804},
  archivePrefix = {arXiv},
  primaryClass  = {q-bio.NC}
}
```
