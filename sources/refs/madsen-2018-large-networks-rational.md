---
type: reference
title: "Large networks of rational agents form persistent echo chambers"
aliases: ["madsen2018large"]
authors: ["Jens Koed Madsen", "Richard M. Bailey", "Toby D. Pilditch"]
year: 2018
venue: "Scientific Reports"
doi: "10.1038/s41598-018-25558-7"
url: "https://doi.org/10.1038/s41598-018-25558-7"
tags: [cluster/multi-agent, cluster/social-physics, cluster/social-physics/opinion-dynamics, project/multi-agent, project/social-physics, field/sociology, field/psychology]
created: 2026-11-10
updated: 2026-11-10
---

# Large networks of rational agents form persistent echo chambers

> [!info] Citation
> Madsen, J. K., Bailey, R. M., Pilditch, T. D. (2018). *Large networks of rational agents form persistent echo chambers*. Scientific Reports, 8(1), 12391. [DOI](https://doi.org/10.1038/s41598-018-25558-7)

[Local PDF](../pdfs/madsen-2018-large-networks-rational.pdf), 8 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

An agent-based simulation study showing that echo chambers can form among agents that update their beliefs by Bayes' rule without cognitive error, and that larger networks promote rather than reduce their growth.

## Problem & setting

The paper asks whether echo chambers require cognitive or social biases, or whether they can arise from idealized rational agents, and why they persist when contrary information is available. Most earlier theoretical treatments, the authors say, use simplified analytical models in which agents do not interact directly.

## Method

Each agent holds a Gaussian belief about a fixed true value, with its own mean and uncertainty. Agents are honest, have identical cognitive capacities and trust senders fully. At each step an agent searches a fraction of the population, controlled by a search parameter, and accepts the views that fall within a range around its own mean whose width is a multiple of its own uncertainty. As confidence grows, previously acceptable partners can fall outside the range and are dropped, which the authors call pruning. Simulations vary the search fraction, the pruning parameter and the network structure, with random connections as one option.

## Key results

According to the abstract, echo chambers emerge among error-free Bayesian agents, larger networks encourage their growth, and biases are not necessary conditions. Stylized interventions in the form of truthful system-wide broadcasts reduce the effect without removing it, and work better on agents newer to the network. The evidence is simulation, not analytic proof.

## Relevance to this research

The manuscript cites the paper as a comparison case in its treatment of misreading and echo chambers. It reads the model as one in which receivers take each received belief as fresh evidence and withdraw from partners outside a confidence window, and it contrasts this with its own result that echo chambers require misspecification. The note rests on the model description in the open-access text. Related pages are [[Echo chambers and polarization]], [[Bounded confidence]], [[Opinion dynamics]] and [[Bayesian Inference]].

## Cross-links

[[Collective agents literature map]]; [[Echo chambers and polarization]]; [[Bounded confidence]]; [[Opinion dynamics]]; [[Bayesian Inference]].

## BibTeX

```bibtex
@article{madsen2018large,
  author  = {Madsen, Jens Koed and Bailey, Richard M. and Pilditch, Toby D.},
  title   = {Large networks of rational agents form persistent echo chambers},
  journal = {Scientific Reports},
  volume  = {8},
  number  = {1},
  pages   = {12391},
  year    = {2018},
  doi     = {10.1038/s41598-018-25558-7}
}
```
