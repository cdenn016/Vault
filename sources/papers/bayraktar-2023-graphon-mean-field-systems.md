---
type: paper
title: "Graphon Mean Field Systems"
aliases:
  - "Bayraktar, Chakraborty, and Wu 2023"
  - "Graphon particle systems"
authors:
  - Bayraktar, Erhan
  - Chakraborty, Suman
  - Wu, Ruoyu
year: 2023
arxiv: 2003.13180
doi: 10.1214/22-AAP1901
url: https://doi.org/10.1214/22-AAP1901
tags:
  - cluster/multi-agent
  - cluster/social-physics
  - cluster/social-physics/networks-and-contagion
  - project/multi-agent
  - project/social-physics
  - field/mathematics
  - field/physics
created: 2026-08-10
---

# Graphon Mean Field Systems

> [!info] Citation
> Erhan Bayraktar, Suman Chakraborty, and Ruoyu Wu (2023). "Graphon mean field systems." *The Annals of Applied Probability* **33**(5), 3587--3619. DOI: [10.1214/22-AAP1901](https://doi.org/10.1214/22-AAP1901). arXiv: [2003.13180](https://arxiv.org/abs/2003.13180).

## TL;DR

The paper gives a rigorous large-population limit for heterogeneous interacting diffusions whose interaction weights converge to a graphon. The limit is not one exchangeable representative particle: it is a continuum of independent but heterogeneous nonlinear diffusions whose laws remain coupled through the graphon.

## Problem & setting

Classical mean-field limits often replace an all-to-all symmetric population by one McKean--Vlasov law. Here the finite agents have nonexchangeable interaction weights encoded by a graph. The problem is to identify a stable limit when the graph sequence converges and to determine whether a suitably thinned network has the same macroscopic behavior.

## Method

Agents are indexed by points in $[0,1]$, and a graphon $G(u,v)$ weights the law-dependent drift coupling between types. The authors establish well-posedness, continuity, and stability of the graphon mean-field system, then compare finite interacting diffusions with the limiting independent projection. They also analyze percolated, not-so-dense graphs under vanishing edge probabilities and an explicit interaction rescaling.

## Key results

A law of large numbers holds as the finite graphons converge to the limiting graphon. The finite heterogeneous particle system converges to the graphon mean-field system, and a suitably scaled not-so-dense analogue has the same limit under the paper's assumptions. These results require a declared stochastic diffusion family, graphon convergence, coefficient regularity, independence assumptions, and the stated density scaling; they do not apply to every growing deterministic agent network.

## Relevance to this research

This is the primary source for [[Graphon limits of agent networks]] and a modern heterogeneous route to [[Propagation of chaos]]. It gives precise prerequisites for one possible population-limit extension of MultiAgentELBO. The current finite Gaussian interaction laboratory has no $N$-indexed stochastic diffusion, graphon-convergent family, or proved coefficient assumptions, so this paper is a design target rather than closure of the existing continuum obligations.

## Cross-links

- Concepts: [[Graphon limits of agent networks]], [[Propagation of chaos]], [[Mean-field games and continuum limits]]
- Related sources: [[sznitman-1991-propagation-chaos]], [[caines-huang-2021-graphon-mean-field-games]]

## BibTeX

```bibtex
@article{BayraktarChakrabortyWu2023,
  author  = {Bayraktar, Erhan and Chakraborty, Suman and Wu, Ruoyu},
  title   = {Graphon Mean Field Systems},
  journal = {The Annals of Applied Probability},
  volume  = {33},
  number  = {5},
  pages   = {3587--3619},
  year    = {2023},
  doi     = {10.1214/22-AAP1901},
  eprint  = {2003.13180},
  archivePrefix = {arXiv}
}
```
