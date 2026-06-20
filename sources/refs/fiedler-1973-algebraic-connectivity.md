---
type: reference
title: "Algebraic Connectivity of Graphs"
aliases:
  - "Fiedler 1973"
  - "Fiedler (1973) Algebraic Connectivity"
authors:
  - Miroslav Fiedler
year: 1973
tags:
  - cluster/social-physics
  - cluster/multi-agent
  - project/multi-agent
  - project/social-physics
  - field/mathematics
  - cluster/social-physics/networks-and-contagion
created: 2026-06-19
updated: 2026-06-19
---

# Algebraic Connectivity of Graphs

> [!info] Citation
> Miroslav Fiedler (1973). "Algebraic connectivity of graphs." *Czechoslovak Mathematical Journal* **23**(2), 298–305. DOI: [10.21136/CMJ.1973.101168](https://doi.org/10.21136/CMJ.1973.101168).

## TL;DR

Fiedler introduces the *algebraic connectivity* of a graph: the second-smallest eigenvalue $\lambda_2$ of the graph Laplacian $L = D - A$. He shows $\lambda_2 > 0$ iff the graph is connected, that it lower-bounds vertex and edge connectivity, and that the associated eigenvector (the *Fiedler vector*) orders vertices in a way that exposes the graph's natural bipartition. $\lambda_2(L)$ — the spectral gap — is the quantity behind the project's constrained spectral gap, parent-mass estimate, and spectral cluster detection.

## What it establishes

For the symmetric positive-semidefinite Laplacian $L$, the smallest eigenvalue is always zero (constant eigenvector); the next one, $\lambda_2$, measures how strongly connected the graph is. Fiedler proves $\lambda_2 \le$ the vertex connectivity, so a small spectral gap signals a graph that is nearly disconnected — easily split into two pieces along the sign pattern of the Fiedler vector. This is the spectral foundation of graph partitioning and spectral clustering: the eigenvector of $\lambda_2$ gives the cut that minimizes inter-cluster coupling.

## Why the project cites it

The project detects coherent agent clusters — the blocks to coarse-grain into [[Meta-agents and hierarchical emergence|meta-agents]] — and a small algebraic connectivity $\lambda_2$ of the agent coupling graph is precisely the signal that a population is about to split into sub-communities, with the Fiedler vector giving the cut. The same $\lambda_2$ enters the project's constrained spectral gap and as a proxy for the "parent mass" (how strongly a coarse parent binds its constituents), since a large gap means a tightly bound cluster. This spectral route to clustering is the eigenvalue counterpart of the modularity criterion of [[newman-girvan-2004-community-structure]], and both feed the new [[Community detection and modularity]] page. Manuscript thread: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@article{fiedler1973algebraic,
  author  = {Fiedler, Miroslav},
  title   = {Algebraic connectivity of graphs},
  journal = {Czechoslovak Mathematical Journal},
  volume  = {23},
  number  = {2},
  pages   = {298--305},
  year    = {1973},
  doi     = {10.21136/CMJ.1973.101168}
}
```
