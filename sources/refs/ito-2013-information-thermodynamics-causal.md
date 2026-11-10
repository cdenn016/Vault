---
type: reference
title: "Information Thermodynamics on Causal Networks"
aliases: ["ito2013information"]
authors: ["Sosuke Ito", "Takahiro Sagawa"]
year: 2013
venue: "Physical Review Letters"
doi: "10.1103/PhysRevLett.111.180603"
arxiv: "1306.2756"
url: "https://doi.org/10.1103/PhysRevLett.111.180603"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/physics]
created: 2026-11-10
updated: 2026-11-10
---

# Information Thermodynamics on Causal Networks

> [!info] Citation
> Ito, S., Sagawa, T. (2013). *Information Thermodynamics on Causal Networks*. Physical Review Letters, 111, 180603. [DOI](https://doi.org/10.1103/PhysRevLett.111.180603), [arXiv](https://arxiv.org/abs/1306.2756)

[Local PDF](../pdfs/ito-2013-information-thermodynamics-causal.pdf), 11 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and manuscript reading record.

## TL;DR

The letter describes nonequilibrium dynamics of several interacting fluctuating systems with a causal network (Bayesian network) and derives generalizations of the second law and the fluctuation theorem that include an informational term set by the network topology.

## Problem & setting

With feedback control by a Maxwell's demon the entropy production of a system can be negative, and the second law was known to be generalized by the mutual information exchanged with the demon. A general theory for several systems exchanging information many times was lacking, which the paper addresses.

## Method

Each system's dynamics is represented on a Bayesian network. The informational quantity combines the initial correlation between the target system and the others, the information transferred from the system to the others during the dynamics, and the final correlation. The result reproduces the earlier inequality as a special case and is illustrated with a model of biochemical adaptation.

## Key results

The entropy production of a single system in the presence of other systems is bounded by the information flow between those systems. The manuscript's record adds that a second law with transfer entropy holds on discrete-time causal networks and that the bath entropy change of one node is evaluated at fixed values of the other nodes.

## Relevance to this research

The manuscript cites it for that convention, evaluating the bath entropy of one part at a fixed value of its partner, in its discrete-time second law for one part of a bipartite process. See [[Stochastic Thermodynamics]], [[Mutual information]] and [[Nonequilibrium steady state]].

## Cross-links

[[Collective agents literature map]]; [[Stochastic Thermodynamics]]; [[Mutual information]]; [[Nonequilibrium steady state]]; [[horowitz-2014-thermodynamics-continuous-information]].

## BibTeX

```bibtex
@article{ito2013information,
  author  = {Ito, Sosuke and Sagawa, Takahiro},
  title   = {Information Thermodynamics on Causal Networks},
  journal = {Physical Review Letters},
  volume  = {111},
  pages   = {180603},
  year    = {2013},
  doi     = {10.1103/PhysRevLett.111.180603},
  eprint  = {1306.2756},
  archiveprefix = {arXiv}
}
```
