---
type: paper
title: "Non-Bayesian Social Learning"
aliases:
  - "Jadbabaie et al. 2012 social learning"
authors:
  - Jadbabaie, Ali
  - Molavi, Pooya
  - Sandroni, Alvaro
  - Tahbaz-Salehi, Alireza
year: 2012
arxiv: null
doi: 10.1016/j.geb.2012.06.001
url: https://doi.org/10.1016/j.geb.2012.06.001
tags:
  - cluster/social-physics
  - cluster/social-physics/networks-and-contagion
  - cluster/social-physics/evolutionary-and-cultural
  - cluster/multi-agent
  - project/social-physics
  - project/multi-agent
  - field/economics
  - field/mathematics
  - field/statistics
created: 2026-08-10
---

# Non-Bayesian Social Learning

> [!info] Citation
> Ali Jadbabaie, Pooya Molavi, Alvaro Sandroni, and Alireza Tahbaz-Salehi (2012). "Non-Bayesian social learning." *Games and Economic Behavior* **76**(1), 210--225. DOI: [10.1016/j.geb.2012.06.001](https://doi.org/10.1016/j.geb.2012.06.001).

## TL;DR

Agents can aggregate dispersed information without maintaining the full joint Bayesian model of everyone else's signals and actions. They update their own private evidence in a Bayesian way, then use a simple linear rule to combine that posterior with neighbors' beliefs; under the paper's assumptions, the network still learns the true parameter.

## Problem & setting

No individual has all information needed to identify an unknown parameter. Agents repeatedly receive private observations and communicate beliefs over a finite state space through a social network. Fully Bayesian social inference would require a detailed and growing model of the entire observation and communication history, so the paper studies a deliberately naive alternative.

## Method

Each agent first applies Bayes' rule to its own prior belief and new private signal. It then forms a weighted arithmetic combination of that personal posterior and its neighbors' current beliefs. The network weights describe social influence, while the private likelihoods supply fresh statistical evidence.

## Key results

Repeated interaction leads agents to learn the true parameter under the stated signal-identifiability, weighting, and network conditions, despite the non-Bayesian social aggregation step and unfavorable initial beliefs. The result does not assert exact centralized posteriors, calibrated uncertainty, or learning under arbitrary correlated signals and changing networks.

## Relevance to this research

This paper is the canonical source for [[Non-Bayesian social learning]]. It prevents an engineered attractive interaction energy from being described as distributed Bayes merely because beliefs converge. MultiAgentELBO should distinguish exact inference in one normalized joint law, approximate neighbor aggregation, and the weaker property of asymptotic truth learning under a specified signal model.

## Cross-links

- Concepts: [[Non-Bayesian social learning]], [[Decentralized Bayesian inference]], [[Common knowledge and Bayesian agreement]], [[Opinion dynamics]]
- Related sources: [[lalitha-2018-distributed-hypothesis-testing]], [[aumann-1976-agreeing-disagree]]

## BibTeX

```bibtex
@article{JadbabaieMolaviSandroniTahbazSalehi2012,
  author  = {Jadbabaie, Ali and Molavi, Pooya and Sandroni, Alvaro and Tahbaz-Salehi, Alireza},
  title   = {Non-Bayesian Social Learning},
  journal = {Games and Economic Behavior},
  volume  = {76},
  number  = {1},
  pages   = {210--225},
  year    = {2012},
  doi     = {10.1016/j.geb.2012.06.001}
}
```
