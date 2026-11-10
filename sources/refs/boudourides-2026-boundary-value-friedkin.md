---
type: reference
title: "Boundary-Value Friedkin-Johnsen Dynamics and Influence-Based Centralities on Networks"
aliases: ["boudourides2026boundary"]
authors: ["Moses Boudourides"]
year: 2026
arxiv: "2602.08704"
url: "https://arxiv.org/abs/2602.08704"
tags: [cluster/social-physics, cluster/social-physics/opinion-dynamics, project/multi-agent, project/social-physics, field/sociology, field/mathematics, field/cs-ml]
created: 2026-11-10
updated: 2026-11-10
---

# Boundary-Value Friedkin-Johnsen Dynamics and Influence-Based Centralities on Networks

> [!info] Citation
> Boudourides, M. (2026). *Boundary-Value Friedkin-Johnsen Dynamics and Influence-Based Centralities on Networks*. arXiv preprint. [arXiv](https://arxiv.org/abs/2602.08704)

[Local PDF](../pdfs/boudourides-2026-boundary-value-friedkin.pdf), 43 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

A preprint that casts Friedkin-Johnsen opinion dynamics on directed weighted networks as a discrete boundary-value problem, with fully stubborn agents as boundary nodes, and derives influence-based broadcasting and reception measures from a Green operator.

## Problem & setting

The introduction poses the question of which nodes transmit influence most effectively and which are most receptive to externally fixed sources, and notes that topology-only centralities ignore heterogeneous susceptibility to influence. The Friedkin-Johnsen model is described as a balance between an agent's initial private belief and interpersonal influence, extending DeGroot averaging.

## Method

Fully stubborn agents are treated as boundary nodes and the remaining agents as interior nodes. The formulation yields a Green operator and an all-source steady-state response matrix whose entry gives the steady response of one target to a unit fixed opinion at one source. Broadcasting and reception measures are defined from that matrix.

## Key results

The abstract states that the paper establishes conditions for existence and uniqueness of the steady state, derives transient and steady-state representations, characterizes sensitivity to susceptibility parameters and to perturbations of the network, and gives a spectral analysis for the undirected homogeneous-susceptibility case. It also reports computational experiments on benchmark networks, which are the authors' own and are not used here.

## Relevance to this research

The collective-agents manuscript cites this preprint in its related-work discussion as an instance of Friedkin-Johnsen dynamics written with a Green operator, in order not to present a Green-operator description of influence decay as new. The connection to the vault is the opinion-dynamics side of the program, where influence with stubborn or anchored members is compared with a lattice Green's function, see [[Opinion dynamics]], [[Graph Laplacian]], [[Non-Bayesian social learning]] and [[Sociophysics]].

## Cross-links

[[Collective agents literature map]]; [[Opinion dynamics]]; [[Graph Laplacian]]; [[Non-Bayesian social learning]]; [[Sociophysics]].

## BibTeX

```bibtex
@misc{boudourides2026boundary,
  author        = {Boudourides, Moses},
  title         = {Boundary-Value {Friedkin-Johnsen} Dynamics and Influence-Based Centralities on Networks},
  year          = {2026},
  eprint        = {2602.08704},
  archivePrefix = {arXiv}
}
```
