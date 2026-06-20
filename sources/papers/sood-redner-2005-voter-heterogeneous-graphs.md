---
type: paper
title: "Voter Model on Heterogeneous Graphs"
aliases: ["Sood & Redner 2005", "Voter model on heterogeneous graphs"]
authors: ["Sood V.", "Redner S."]
year: 2005
url: https://doi.org/10.1103/PhysRevLett.94.178701
tags: [cluster/social-physics, project/social-physics, field/physics, field/cs-ml, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Voter Model on Heterogeneous Graphs

> [!info] Citation
> Sood, V., & Redner, S. (2005). *Voter Model on Heterogeneous Graphs*. Physical Review Letters 94(17), 178701. DOI: [10.1103/PhysRevLett.94.178701](https://doi.org/10.1103/PhysRevLett.94.178701). arXiv:cond-mat/0412599.

## TL;DR
Sood and Redner solve the voter model on networks with broad degree distributions, where the classic lattice analysis breaks down. The key move is to recognize that the naive magnetization is not conserved on a heterogeneous graph; instead a degree-weighted magnetization is the right conserved quantity. Working in this variable, they obtain the consensus (exit) time and show that it is controlled by the moments of the degree distribution rather than by the system size alone. For scale-free networks with a heavy-tailed degree distribution, this makes the time to reach unanimity depend sharply on how fat the tail is, with qualitatively different scaling than on regular lattices.

## What it establishes
The conserved order parameter on a graph with degree distribution $P(k)$ is the degree-weighted opinion density $\omega = \sum_k k\, P(k)\, n_k / \langle k\rangle$, not the plain mean. Using this, the mean time to consensus on a network of $N$ nodes scales as
$$ T_N \sim N\,\frac{\langle k\rangle^2}{\langle k^2\rangle}, $$
so that highly heterogeneous (broad-$P(k)$) networks, with large second moment $\langle k^2\rangle$, reach consensus faster relative to their size. The analysis also exposes the role of high-degree hubs as effective opinion reservoirs and clarifies how the interplay between degree heterogeneity and the conservation law sets the route to fixation. The result establishes that network topology, through the moments of the degree distribution, is a primary control parameter for discrete agreement dynamics.

## Relevance to this research
This paper connects discrete agreement dynamics to network structure and degree heterogeneity, bridging the voter model to the community-detection and graph-spectral machinery the program already tracks. It makes explicit that relational topology — who is connected to whom, and how unevenly — controls when and how fast a population reaches consensus, which is directly relevant to how the attention graph $\beta_{ij}$ and the emergence of meta-agents depend on the connectivity of the belief population rather than on agent count alone. Honestly, this is an adjacent network-theoretic extension rather than core machinery of the belief-inertia functional, but it supplies the quantitative link between graph heterogeneity and consensus that the program's network-structured and hierarchical claims will need. See [[Community detection and modularity]], [[Voter model]], [[Opinion dynamics]].

## Cross-links
- Concept: [[Voter model]]
- Related sources: [[holley-liggett-1975-voter-model-ergodic]], [[clifford-sudbury-1973-spatial-conflict]]

## BibTeX
```bibtex
@article{sood2005voter,
  author  = {Sood, Vishal and Redner, Sidney},
  title   = {Voter Model on Heterogeneous Graphs},
  journal = {Physical Review Letters},
  year    = {2005},
  volume  = {94},
  number  = {17},
  pages   = {178701},
  doi     = {10.1103/PhysRevLett.94.178701}
}
```
