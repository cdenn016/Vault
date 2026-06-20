---
type: paper
title: "The Dissemination of Culture: A Model with Local Convergence and Global Polarization"
aliases: ["Axelrod 1997", "Axelrod culture-dissemination model"]
authors: ["Axelrod R."]
year: 1997
url: https://doi.org/10.1177/0022002797041002001
tags: [cluster/social-physics, project/social-physics, field/sociology, field/physics, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# The Dissemination of Culture: A Model with Local Convergence and Global Polarization

> [!info] Citation
> Axelrod, R. (1997). *The Dissemination of Culture: A Model with Local Convergence and Global Polarization*. Journal of Conflict Resolution 41(2), 203-226. DOI: [10.1177/0022002797041002001](https://doi.org/10.1177/0022002797041002001).

## TL;DR
Axelrod introduces an agent-based model in which each agent on a lattice carries a vector of $F$ cultural features, each taking one of $q$ discrete traits. Interaction is homophilous: the probability that two neighbours interact is proportional to their cultural similarity (the fraction of features on which they already agree), and when they do interact one copies a trait from the other on a feature where they currently differ. The surprising emergent outcome is that this purely convergent, similarity-gated rule does not drive the population to global uniformity. Instead it freezes into a patchwork of internally homogeneous but mutually incompatible cultural regions — local convergence coexists with stable global polarization, with the number of surviving distinct cultures depending sharply on the number of traits per feature.

## What it establishes
The model couples two ingredients that pull in opposite directions: influence (agents become more alike when they interact) and homophily (only already-similar agents interact at all). Formally, the interaction probability between neighbours $i$ and $j$ is the overlap
$$ p_{ij} = \frac{1}{F}\sum_{f=1}^{F} \mathbf{1}[\sigma_i^f = \sigma_j^f], $$
and agents whose overlap is zero can never interact, producing absorbing cultural boundaries. The system always reaches an absorbing state in which every neighbour pair is either identical or completely incompatible. The key control parameter is $q$, the number of possible traits per feature: small $q$ yields a single dominant culture (consensus), while large $q$ yields many frozen domains (fragmentation), with a sharp crossover between the two regimes. The result is the canonical demonstration that similarity-biased local influence generically preserves diversity rather than erasing it.

## Relevance to this research
This is the seminal multi-trait discrete model showing that confidence- or similarity-gated influence produces persistent heterogeneity rather than uniform consensus — precisely the qualitative outcome the belief-inertia VFE functional must reproduce in its overdamped limit. Axelrod's homophily-gated copy rule is a discrete, hard-classification ancestor of the soft attention weighting $\beta_{ij} = \mathrm{softmax}(-\mathrm{KL}(q_i \| \Omega_{ij}[q_j])/\tau)$: when transported divergence is large the coupling vanishes, severing the edge exactly as zero cultural overlap severs interaction here. It is therefore a direct conceptual progenitor of the bounded-confidence and echo-chamber phenomena the program targets, though its binary trait-matching is a coarsened limit of the continuous gauge-transported KL coupling rather than a piece of machinery the functional literally uses. See [[Axelrod model of cultural dissemination]], [[Echo chambers and polarization]], [[Bounded confidence]], [[Opinion dynamics]].

## Cross-links
- Concept: [[Axelrod model of cultural dissemination]]
- Related sources: [[castellano-marsili-vespignani-2000-axelrod-transition]], [[lorenz-2007-bounded-confidence-survey]]

## BibTeX
```bibtex
@article{axelrod1997dissemination,
  author  = {Axelrod, Robert},
  title   = {The Dissemination of Culture: A Model with Local Convergence and Global Polarization},
  journal = {Journal of Conflict Resolution},
  year    = {1997},
  volume  = {41},
  number  = {2},
  pages   = {203--226},
  doi     = {10.1177/0022002797041002001}
}
```
