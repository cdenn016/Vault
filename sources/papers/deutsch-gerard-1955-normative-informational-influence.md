---
type: paper
title: "A Study of Normative and Informational Social Influences upon Individual Judgment"
aliases: ["Deutsch & Gerard 1955", "Normative vs informational influence"]
authors: ["Deutsch M.", "Gerard H. B."]
year: 1955
url: https://doi.org/10.1037/h0046408
tags: [cluster/social-physics, project/social-physics, field/psychology, cluster/social-physics/social-influence]
created: 2026-06-19
updated: 2026-06-19
---

# A Study of Normative and Informational Social Influences upon Individual Judgment

> [!info] Citation
> Morton Deutsch and Harold B. Gerard (1955). *A study of normative and informational social influences upon individual judgment*. Journal of Abnormal and Social Psychology, 51(3), 629–636. DOI: 10.1037/h0046408.

## TL;DR
Deutsch and Gerard draw the foundational conceptual distinction between two qualitatively different channels through which other people shape one's judgments. **Informational social influence** is the acceptance of information from others as evidence about reality — treating the group's responses as data about the true state of the world. **Normative social influence** is conformity to the positive expectations of others — going along to gain approval or avoid disapproval, independent of any belief that the others are correct. Using an Asch-style line task with experimental manipulations of anonymity, group commitment, and self-commitment, they show both channels operate and can be dissociated: making responses anonymous (removing the normative pressure of being observed) reduces conformity but does not eliminate it, leaving the informational residue.

## What it establishes
The paper operationalizes the two-channel decomposition and demonstrates that conformity is the sum of separable contributions. When participants commit privately to a judgment before exposure (anchoring their own estimate) or respond anonymously, normative pressure is attenuated and conformity drops; when the stimulus is made more ambiguous, the informational channel strengthens because others' responses carry more evidential weight. Schematically, an agent's update is driven by a weighted combination of an evidential pull toward the group's apparent estimate and a normative pull toward matching expectations, with the relative weights set by stimulus ambiguity and the social-visibility of the response.

## Relevance to this research
The two channels map cleanly onto distinct terms in the VFE functional. Informational influence is the data-like belief coupling $\beta_{ij}\,\mathrm{KL}(q_i \,\|\, \Omega_{ij} q_j)$ — neighbours treated as evidence about the latent state, so their beliefs are absorbed exactly as observations would be. Normative influence is closer to a prior-conformity / attention-entropy pressure: a pull toward matching the group that is not evidentially justified, expressible as anchoring toward a transported group prior or as the entropy regularizer on the attention weights $\tau\,\beta_{ij}\log(\beta_{ij}/\pi_{ij})$. This decomposition is exactly the kind of justification the belief-inertia manuscript needs for keeping the coupling and prior terms conceptually distinct rather than collapsing them. See [[Social influence and conformity]], [[Opinion dynamics]], and [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Social influence and conformity]]
- Related sources: [[asch-1955-opinions-and-social-pressure]], [[festinger-1954-social-comparison-processes]], [[sherif-1936-psychology-social-norms]]

## BibTeX
```bibtex
@article{deutsch1955study,
  author  = {Deutsch, Morton and Gerard, Harold B.},
  title   = {A Study of Normative and Informational Social Influences upon Individual Judgment},
  journal = {Journal of Abnormal and Social Psychology},
  year    = {1955},
  volume  = {51},
  number  = {3},
  pages   = {629--636},
  doi     = {10.1037/h0046408}
}
```
