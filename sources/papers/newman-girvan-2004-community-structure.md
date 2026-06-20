---
type: paper
title: "Finding and Evaluating Community Structure in Networks"
aliases:
  - "Newman & Girvan 2004"
  - "Newman-Girvan (2004) Modularity"
authors:
  - M. E. J. Newman
  - M. Girvan
year: 2004
arxiv: cond-mat/0308217
tags:
  - cluster/social-physics
  - cluster/multi-agent
  - project/multi-agent
  - project/social-physics
  - field/physics
  - field/cs-ml
  - cluster/social-physics/networks-and-contagion
created: 2026-06-19
updated: 2026-06-19
---

# Finding and Evaluating Community Structure in Networks

> [!info] Citation
> M. E. J. Newman and M. Girvan (2004). "Finding and evaluating community structure in networks." *Physical Review E* **69**(2), 026113. DOI: [10.1103/PhysRevE.69.026113](https://doi.org/10.1103/PhysRevE.69.026113). Preprint: [arXiv:cond-mat/0308217](https://arxiv.org/abs/cond-mat/0308217).

## TL;DR

Newman and Girvan introduce *modularity* $Q$ — a scalar that scores a proposed partition of a network by how many more edges fall inside communities than would be expected by chance under a degree-preserving null model — together with edge-betweenness divisive clustering to find such partitions. Modularity became the standard objective for community detection: partitions that maximize $Q$ are the ones with strong internal cohesion and weak external coupling. This is precisely the quantity the project's cluster-detection and culture-closure machinery re-derives, so this paper is the literature anchor for [[Meta-agents and hierarchical emergence]] and the new page [[Community detection and modularity]].

## Problem & setting

Real networks (social, biological, technological) decompose into densely connected groups with sparse inter-group links. The problem is twofold: how to *find* such a partition, and how to *evaluate* whether a given partition is good. Earlier hierarchical-clustering heuristics gave dendrograms but no principled stopping criterion or quality measure.

## Method

For finding communities they use *edge betweenness* (the number of shortest paths through an edge) as a measure of inter-community bridges, iteratively removing high-betweenness edges to split the graph into a dendrogram. To evaluate a cut they define modularity
$$
Q = \sum_c \left( e_{cc} - a_c^2 \right),
$$
where $e_{cc}$ is the fraction of edges inside community $c$ and $a_c$ is the fraction of edge-endpoints attached to $c$ (so $a_c^2$ is the expected within-community edge fraction under a random rewiring that preserves degrees). $Q>0$ signals more internal structure than chance; the dendrogram level with maximal $Q$ is the preferred partition.

## Key results

Modularity provides an objective, null-model-referenced score that selects the natural number of communities without a tunable threshold. On benchmarks with planted communities and on real networks (collaboration graphs, food webs) the betweenness method plus $Q$-maximization recovers known structure. The paper launched modularity-maximization as the dominant family of community-detection methods.

## Relevance to this research

The project's meta-agent formation rests on detecting which clusters of micro-agents are coherent enough to be coarse-grained into a parent. The "culture-closure ratio" used to decide cluster membership — internal coupling relative to external coupling — is structurally the same comparison modularity makes against a degree-preserving null. Reading `find_clusters` and the closure criterion through Newman-Girvan, the project's cluster acceptance test is a modularity-style score on the agent interaction graph, where edge weights are the belief-coupling strengths ($\beta_{ij}$) rather than binary adjacency. This grounds [[Meta-agents and hierarchical emergence]] in an established, well-understood objective and supplies the new [[Community detection and modularity]] page with its canonical reference.

The connection ties the social-physics aggregation step to the RG picture: choosing which agents form a meta-agent is choosing the coarse-graining blocks of [[Renormalization-group flow of beliefs]], and modularity is the criterion for a *good* blocking. The spectral counterpart — using the Fiedler value $\lambda_2$ of the graph Laplacian to find the cut — connects to [[fiedler-1973-algebraic-connectivity]] and the parent-mass / spectral-gap reading. For the resolution-limit caveats of modularity see [[fortunato-2010-community-detection]]. Manuscript thread: [[participatory-it-from-bit]].

## Cross-links

- Concept: [[Meta-agents and hierarchical emergence]], [[Community detection and modularity]], [[Renormalization-group flow of beliefs]].
- Sources: [[fortunato-2010-community-detection]], [[fiedler-1973-algebraic-connectivity]].
- Manuscript: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@article{newman2004finding,
  author  = {Newman, M. E. J. and Girvan, M.},
  title   = {Finding and evaluating community structure in networks},
  journal = {Physical Review E},
  volume  = {69},
  number  = {2},
  pages   = {026113},
  year    = {2004},
  doi     = {10.1103/PhysRevE.69.026113},
  eprint  = {cond-mat/0308217},
  archivePrefix = {arXiv},
  publisher = {American Physical Society}
}
```
