---
type: reference
title: "Sparse coupling and Markov blankets: A comment on \"How particular is the physics of the Free Energy Principle?\" by Aguilera, Millidge, Tschantz and Buckley"
aliases: ["heins2022sparse"]
authors: ["Conor Heins", "Lancelot Da Costa"]
year: 2022
venue: "Physics of Life Reviews"
doi: "10.1016/j.plrev.2022.06.001"
url: "https://doi.org/10.1016/j.plrev.2022.06.001"
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/physics, field/neuroscience]
created: 2026-11-10
updated: 2026-11-10
---
# Sparse coupling and Markov blankets: A comment on "How particular is the physics of the Free Energy Principle?" by Aguilera, Millidge, Tschantz and Buckley

> [!info] Citation
> Heins, C., Da Costa, L. (2022). *Sparse coupling and Markov blankets: A comment on "How particular is the physics of the Free Energy Principle?" by Aguilera, Millidge, Tschantz and Buckley*. Physics of Life Reviews, 42, 33-39. [DOI](https://doi.org/10.1016/j.plrev.2022.06.001)

[Local PDF](../pdfs/heins-2022-sparse-coupling-markov.pdf), 11 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

A commentary on a critique of the free energy principle that derives conditions under which sparse causal coupling does or does not give a Markov blanket in the steady-state density, for Gaussian steady states.

## Problem & setting

The target article analyzed sparsely coupled stochastic differential equations whose non-equilibrium steady-state densities are claimed in earlier free energy principle literature to have a Markov blanket, and showed that in general a blanket does not follow from sparse coupling. The commentary says the relation between sparse coupling and conditional independence was not rigorously defined in the earlier work, and that later work restricted the solenoidal coupling to obtain it.

## Method

The authors write the flow of an Ito stochastic differential equation as a sum of dissipative and conservative terms by a Helmholtz decomposition, with the conservative part governed by a solenoidal operator, and assume constant, diagonal diffusion. They derive the conditions in the Gaussian steady-state case, for both linear and nonlinear equations.

## Key results

The abstract states that the derivations give conditions under which causal coupling leads, or does not lead, to Markov blankets. The introduction says the relation depends on the form of the solenoidal flow and is strengthened when the state dependence of that flow is local, so that the coupling of two states depends on no others. The authors suggest this may apply to spatially local interactions and leave verification in realistic models to future work.

## Relevance to this research

The manuscript cites the paper in its open problems and related work as part of the foundational dispute over which independence a blanket means, and says the replies concede that sparse coupling does not imply a blanket in general. The reading record describes these positions as known secondarily. See [[Markov Blanket]], [[Markov blanket interpretation debate]], [[Free-energy principle active inference]] and [[Nonequilibrium steady state]].

## Cross-links

[[Collective agents literature map]]; [[Markov Blanket]]; [[Markov blanket interpretation debate]]; [[Free-energy principle active inference]]; [[Nonequilibrium steady state]].

## BibTeX

```bibtex
@article{heins2022sparse,
  author  = {Heins, Conor and Da Costa, Lancelot},
  title   = {Sparse coupling and {Markov} blankets: A comment on ``How particular is the physics of the Free Energy Principle?'' by Aguilera, Millidge, Tschantz and Buckley},
  journal = {Physics of Life Reviews},
  volume  = {42},
  pages   = {33--39},
  year    = {2022},
  doi     = {10.1016/j.plrev.2022.06.001}
}
```
