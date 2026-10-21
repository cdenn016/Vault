---
type: concept
title: "Graphon limits of agent networks"
aliases:
  - "Graphon mean-field limits"
  - "Graph limits for heterogeneous agents"
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
status: draft
created: 2026-08-10
updated: 2026-10-20
---

# Graphon limits of agent networks

## Definition

A graphon is a measurable symmetric kernel \(W:[0,1]^2\to[0,1]\) that represents the limit of a sequence of dense graphs, up to measure-preserving relabeling. In interacting-agent models, a type \(u\in[0,1]\) indexes an agent or population class and \(W(u,v)\) weights its interaction with type \(v\). A graphon limit retains structured heterogeneity that a single homogeneous mean field would erase.

## Two distinct routes

[[bayraktar-2023-graphon-mean-field-systems]] studies weakly interacting stochastic systems on graphon-sampled networks. Its limit is a graphon-indexed McKean--Vlasov family, and propagation of chaos connects finite agents with the continuum law under the paper's assumptions.

[[caines-huang-2021-graphon-mean-field-games]] studies a noncooperative control problem. Graphon-indexed Hamilton--Jacobi--Bellman and forward equations characterize an equilibrium, and an epsilon-Nash result bridges the infinite game back to large finite games. This strategic equilibrium route is not equivalent to the uncontrolled interacting-diffusion route.

## Scope conditions

Classical graphons are naturally dense-graph limits. Sparse networks require rescaling, graphexes, graphings, local weak limits, or another explicitly chosen theory. Exchangeable graph sampling is also stronger than an arbitrary observed network. Gauge transport on graph edges does not itself imply graphon convergence, and a graphon captures limiting connectivity weights rather than holonomy or connection data unless those are separately incorporated into a typed kernel.

## Sources

- [[bayraktar-2023-graphon-mean-field-systems]] — stochastic graphon mean-field systems and propagation of chaos.
- [[caines-huang-2021-graphon-mean-field-games]] — graphon mean-field games, existence/uniqueness, and epsilon-Nash approximation.
- [[sznitman-1991-propagation-chaos]] — foundational criterion and methods for propagation of chaos.

## See also

- [[Mean-field games and continuum limits]]
- [[Propagation of chaos]]
- [[Graph Laplacian]]
- [[Multi-agent variational free energy]]
