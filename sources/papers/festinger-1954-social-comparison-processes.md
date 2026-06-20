---
type: paper
title: "A Theory of Social Comparison Processes"
aliases: ["Festinger 1954", "Social comparison theory"]
authors: ["Festinger L."]
year: 1954
url: https://doi.org/10.1177/001872675400700202
tags: [cluster/social-physics, project/social-physics, field/psychology, field/sociology, cluster/social-physics/social-influence]
created: 2026-06-19
updated: 2026-06-19
---

# A Theory of Social Comparison Processes

> [!info] Citation
> Leon Festinger (1954). *A theory of social comparison processes*. Human Relations, 7(2), 117–140. DOI: 10.1177/001872675400700202.

## TL;DR
Festinger proposes that people have a drive to evaluate their opinions and abilities, and that when objective, non-social means of evaluation are unavailable they do so by comparing themselves to other people. Critically, comparison is biased toward *similar* others: one evaluates an opinion against those whose opinions and abilities are close to one's own, because comparison with very divergent others is uninformative. The theory derives a set of hypotheses about the resulting dynamics — most importantly that comparison generates pressures toward uniformity within a group, and that these pressures grow with the similarity of members and the attractiveness/cohesiveness of the group.

## What it establishes
The framework states a series of hypotheses linking similarity, comparison, and influence. The drive for self-evaluation produces a tendency to reduce discrepancies with comparison others, yielding pressures toward uniformity of opinion within a group; the strength of the pressure on any individual increases with how similar that individual is to the others and how attractive the group is. When uniformity cannot be reached, the group tends to narrow its comparison range (rejecting or ceasing to compare with the most divergent members), a mechanism that prefigures echo-chamber and out-group-rejection dynamics. The key structural prediction is that influence weight is a decreasing function of belief distance.

## Relevance to this research
This supplies the psychological mechanism behind the attention weights $\beta_{ij}$: comparison, and hence influence, is stronger toward more similar agents, which is precisely what $\beta_{ij} = \mathrm{softmax}(-\mathrm{KL}(q_i\|\Omega_{ij}q_j)/\tau)$ encodes — a small divergence (similar belief) yields a large coupling weight, a large divergence yields a vanishing one. Festinger's "pressure toward uniformity" is the social-coupling gradient that drives consensus in the overdamped flow, and his prediction that groups narrow their comparison range when uniformity fails is the qualitative seed of the model's polarization/echo-chamber regime, where the $\beta$ graph fragments into coherent blocks. This is strong, mechanism-level grounding for the attention construction. See [[Social influence and conformity]], [[Opinion dynamics]], and [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Social influence and conformity]]
- Related sources: [[festinger-1957-cognitive-dissonance]], [[deutsch-gerard-1955-normative-informational-influence]], [[sherif-1936-psychology-social-norms]]

## BibTeX
```bibtex
@article{festinger1954theory,
  author  = {Festinger, Leon},
  title   = {A Theory of Social Comparison Processes},
  journal = {Human Relations},
  year    = {1954},
  volume  = {7},
  number  = {2},
  pages   = {117--140},
  doi     = {10.1177/001872675400700202}
}
```
