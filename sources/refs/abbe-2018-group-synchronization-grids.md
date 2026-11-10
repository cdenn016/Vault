---
type: reference
title: "Group synchronization on grids"
aliases: ["abbe2018group"]
authors: ["Emmanuel Abbe", "Laurent Massoulié", "Andrea Montanari", "Allan Sly", "Nikhil Srivastava"]
year: 2018
venue: "Mathematical Statistics and Learning"
doi: "10.4171/MSL/6"
arxiv: "1706.08561"
url: "https://doi.org/10.4171/MSL/6"
tags: [cluster/multi-agent, project/multi-agent, field/mathematics, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# Group synchronization on grids

> [!info] Citation
> Abbe, E., Massoulié, L., Montanari, A., Sly, A., Srivastava, N. (2018). *Group synchronization on grids*. Mathematical Statistics and Learning, 1(3), 227-256. [DOI](https://doi.org/10.4171/MSL/6), [arXiv](https://arxiv.org/abs/1706.08561)

[Local PDF](../pdfs/abbe-2018-group-synchronization-grids.pdf), 21 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and abstract.

## TL;DR

The paper studies when unknown elements of a compact group, attached to the vertices of a graph, can be recovered from noisy observations of their differences along edges, with the graph taken to be a $d$-dimensional grid. It proves dimension-dependent possibility and impossibility results for weak recovery of distant group differences.

## Problem & setting

Each edge carries a noisy observation of $\theta_u^{-1}\theta_v$ for group elements $\theta_v$ at the vertices. The unknowns are determined only up to a global group action, so the question is weak recovery: whether the group difference between far apart vertices can be estimated better than by random guessing. The introduction gives the $\mathbb{Z}_2$ case with flipped signs and the $O(m)$ case with Gaussian noise, and lists structure from motion, graph localization and some community detection problems as applications.

## Key results

Weak recovery is possible at small enough noise for $d\ge 3$, and for certain finite groups for $d\ge 2$. For some continuous groups it is impossible at $d=2$. At sufficiently strong noise it is always impossible. These are proved statements, as the abstract presents them.

## Relevance to this research

The collective-agents manuscript cites this paper among the synchronization results that consistency of translations between agents resembles, and, in its discussion of disorder, for the grid dimension at which distant group differences can or cannot be recovered. The manuscript states that its holonomy criterion takes its form from the author's own gauge-theoretic work, and treats the synchronization literature as the neighboring problem. See [[Graph synchronization and connection Laplacians]], [[Holonomy]] and [[Critical Phenomena]].

## Cross-links

[[Collective agents literature map]]; [[Graph synchronization and connection Laplacians]]; [[Holonomy]]; [[Critical Phenomena]]; [[aizenman-1989-rounding-first-order]]; [[aizenman-1990-rounding-effects-quenched]].

## BibTeX

```bibtex
@article{abbe2018group,
  author        = {Abbe, Emmanuel and Massouli{\'e}, Laurent and Montanari, Andrea and Sly, Allan and Srivastava, Nikhil},
  title         = {Group synchronization on grids},
  journal       = {Mathematical Statistics and Learning},
  volume        = {1},
  number        = {3},
  pages         = {227--256},
  year          = {2018},
  doi           = {10.4171/MSL/6},
  eprint        = {1706.08561},
  archivePrefix = {arXiv}
}
```
