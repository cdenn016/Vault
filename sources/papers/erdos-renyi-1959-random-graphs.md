---
type: reference
title: "On Random Graphs I"
aliases: ["Erdos & Renyi 1959", "G(n,p) random graph model"]
authors: ["Erdos P.", "Renyi A."]
year: 1959
tags: [cluster/social-physics, project/social-physics, field/mathematics, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# On Random Graphs I

> [!info] Citation
> Erdos, P., & Renyi, A. (1959). *On Random Graphs I*. Publicationes Mathematicae Debrecen, 6, 290-297.

## TL;DR
Erdos and Renyi found the modern theory of random graphs by studying ensembles of graphs on $n$ labelled vertices in which edges are present independently. The companion ensembles $G(n,M)$ (a graph chosen uniformly among those with exactly $M$ edges) and $G(n,p)$ (each of the $\binom{n}{2}$ possible edges present independently with probability $p$) become the universal null models of network science. Their signature discovery is the abrupt *emergence of a giant connected component* as the edge density crosses a critical threshold — the first of many sharp phase-transition phenomena that make random-graph theory a probabilistic analogue of statistical mechanics.

## What it establishes
In $G(n,p)$ with $p = c/n$, the structure of the largest connected component undergoes a sharp transition at $c = 1$ (equivalently average degree $\langle k \rangle = 1$). For $c < 1$ all components are small, of size $O(\ln n)$; at $c = 1$ a critical component of size $\Theta(n^{2/3})$ appears; and for $c > 1$ a unique *giant component* containing a positive fraction $S$ of all vertices emerges, with $S$ the nonzero solution of
$$S = 1 - e^{-cS}.$$
Subsequent thresholds govern full connectivity (at $p = (\ln n)/n$) and the appearance of subgraphs, establishing the template of threshold functions for monotone graph properties. The degree distribution is Poisson with mean $c$, sharply concentrated — the very opposite of the heavy tails of real networks, which is precisely why $G(n,p)$ serves as the baseline against which structured models are judged.

## Relevance to this research
$G(n,p)$ is the null model and percolation baseline against which any structured influence graph — small-world, scale-free — is compared, and the giant-component threshold is the condition that decides whether a global belief-sharing component, and therefore a global consensus, can exist at all. If the attention/influence graph falls below the percolation threshold the population necessarily fragments regardless of the belief dynamics. The relevance is an adjacent mathematical foundation: it sets the connectivity stage on which the VFE dynamics run, without entering the inertia machinery. See [[Network structure — small-world and scale-free]] and [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Network structure — small-world and scale-free]]
- Related sources: [[watts-strogatz-1998-small-world]], [[barabasi-albert-1999-scale-free]], [[newman-2003-structure-function]]

## BibTeX
```bibtex
@article{erdos1959random,
  author  = {Erd{\H{o}}s, Paul and R{\'e}nyi, Alfr{\'e}d},
  title   = {On Random Graphs I},
  journal = {Publicationes Mathematicae Debrecen},
  year    = {1959},
  volume  = {6},
  pages   = {290--297}
}
```
