---
type: paper
title: "Complex Contagions and the Weakness of Long Ties"
aliases: ["Centola & Macy 2007", "Weakness of long ties"]
authors: ["Centola D.", "Macy M."]
year: 2007
url: https://doi.org/10.1086/521848
tags: [cluster/social-physics, project/social-physics, field/sociology, field/cs-ml, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Complex Contagions and the Weakness of Long Ties

> [!info] Citation
> Centola, D., & Macy, M. (2007). *Complex Contagions and the Weakness of Long Ties*. American Journal of Sociology, 113(3), 702-734. doi:10.1086/521848.

## TL;DR
Centola and Macy draw a sharp distinction between *simple* contagions, which can transmit through a single exposure (information, disease), and *complex* contagions, which require reinforcement from multiple distinct sources before an individual adopts (costly, risky, or norm-laden behaviors). For complex contagions the Granovetter "strength of weak ties" logic *reverses*: long bridging ties, which connect an ego to a single distant adopter, fail to deliver the multiple independent confirmations adoption demands. What matters is the *width* of a bridge — how many parallel ties span two communities — not its length, so wide bridges, not long ones, carry complex contagions across social distance.

## What it establishes
Modeling adoption with a threshold rule (an ego adopts only after a critical number or fraction $T$ of its neighbors have adopted), the authors show analytically and by simulation that a single long-range shortcut, which suffices to propagate a simple contagion, cannot by itself trigger a complex contagion in a new region because it provides only one of the $T$ required signals. Propagation across clusters then requires a *wide bridge* — several edges connecting the same pair of neighborhoods so that a foothold receives reinforcement from multiple sides. This reframes the role of network topology: clustering and redundancy, normally dismissed as inefficient, become the very structures that enable complex spread, while the random rewiring that accelerates simple contagion can stall complex contagion entirely.

## Relevance to this research
Belief change in this model typically requires social reinforcement — accumulated gauge-transported KL pressure from several neighbors rather than a single contact — which makes it a complex contagion in Centola and Macy's sense. The wide-bridge requirement reframes which attention-graph topologies can sustain collective belief shifts versus localize them: a lone weak tie carrying high $\beta_{ij}$ is insufficient if the receiving agent needs concordant pressure from a quorum. This is strong and directly interpretive for the model's multi-neighbor coupling structure. See [[Threshold models and complex contagion]], [[Echo chambers and polarization]], and [[Opinion dynamics]].

## Cross-links
- Concept: [[Threshold models and complex contagion]]
- Related sources: [[centola-2010-online-experiment]], [[granovetter-1973-weak-ties]], [[watts-2002-global-cascades]]

## BibTeX
```bibtex
@article{centola2007complex,
  author  = {Centola, Damon and Macy, Michael},
  title   = {Complex Contagions and the Weakness of Long Ties},
  journal = {American Journal of Sociology},
  year    = {2007},
  volume  = {113},
  number  = {3},
  pages   = {702--734},
  doi     = {10.1086/521848}
}
```
