---
type: reference
title: "Thermodynamics with Continuous Information Flow"
aliases: ["horowitz2014thermodynamics"]
authors: ["Jordan M. Horowitz", "Massimiliano Esposito"]
year: 2014
venue: "Physical Review X"
doi: "10.1103/PhysRevX.4.031015"
arxiv: "1402.3276"
url: "https://doi.org/10.1103/PhysRevX.4.031015"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/physics]
created: 2026-11-10
updated: 2026-11-10
---

# Thermodynamics with Continuous Information Flow

> [!info] Citation
> Horowitz, J. M., Esposito, M. (2014). *Thermodynamics with Continuous Information Flow*. Physical Review X, 4, 031015. [DOI](https://doi.org/10.1103/PhysRevX.4.031015), [arXiv](https://arxiv.org/abs/1402.3276)

[Local PDF](../pdfs/horowitz-2014-thermodynamics-continuous-information.pdf), 11 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and manuscript reading record.

## TL;DR

The paper gives a thermodynamic formalism for information transfer between two interacting systems, autonomous or driven, within stochastic thermodynamics, in which the entropy balance of one system acquires a term tied to the mutual information rate.

## Problem & setting

Earlier thermodynamic treatments of information used mutual information as a static quantity for step-by-step feedback protocols. The paper addresses autonomous setups where information flows continuously, with two coupled systems modeled as Markov jump processes on a bipartite graph.

## Method

The joint system obeys the second law, while the entropy balance of the relevant subsystem is modified by an information term. The authors recover results previously derived for nonautonomous Maxwell demons and use a cycle decomposition for autonomous systems at steady state, illustrated with a model system.

## Key results

According to the manuscript's reading record, the paper decomposes the entropy production rate into two partial rates, gives a second law with information flow for one part, shows that the two information flows cancel in a steady state, and uses local detailed balance. Diffusions are not treated.

## Relevance to this research

The manuscript cites it in its open-problems discussion of energy and information, as a derivation of information-flow contributions to the entropy production of subsystems under a stated physical reading of the transition rates. Its extension on thermodynamic cost proves a discrete-time counterpart of the one-part second law and uses this paper for comparison only. See [[Stochastic Thermodynamics]], [[Mutual information]] and [[Nonequilibrium steady state]].

## Cross-links

[[Collective agents literature map]]; [[Stochastic Thermodynamics]]; [[Mutual information]]; [[Nonequilibrium steady state]]; [[ito-2013-information-thermodynamics-causal]].

## BibTeX

```bibtex
@article{horowitz2014thermodynamics,
  author  = {Horowitz, Jordan M. and Esposito, Massimiliano},
  title   = {Thermodynamics with Continuous Information Flow},
  journal = {Physical Review X},
  volume  = {4},
  pages   = {031015},
  year    = {2014},
  doi     = {10.1103/PhysRevX.4.031015},
  eprint  = {1402.3276},
  archiveprefix = {arXiv}
}
```
