---
type: paper
title: "Social Learning and Distributed Hypothesis Testing"
aliases:
  - "Lalitha, Javidi, and Sarwate 2018"
  - "Network divergence social learning"
authors:
  - Lalitha, Anusha
  - Javidi, Tara
  - Sarwate, Anand D.
year: 2018
arxiv: 1410.4307
doi: 10.1109/TIT.2018.2837050
url: https://doi.org/10.1109/TIT.2018.2837050
tags:
  - cluster/multi-agent
  - cluster/social-physics
  - cluster/social-physics/networks-and-contagion
  - project/multi-agent
  - project/social-physics
  - field/statistics
  - field/cs-ml
  - field/mathematics
created: 2026-08-10
---

# Social Learning and Distributed Hypothesis Testing

> [!info] Citation
> Anusha Lalitha, Tara Javidi, and Anand D. Sarwate (2018). "Social Learning and Distributed Hypothesis Testing." *IEEE Transactions on Information Theory* **64**(9), 6161--6179. DOI: [10.1109/TIT.2018.2837050](https://doi.org/10.1109/TIT.2018.2837050). arXiv: [1410.4307](https://arxiv.org/abs/1410.4307).

## TL;DR

Agents combine private Bayesian evidence with a logarithmic consensus over neighbors' beliefs. Under identifiability and network assumptions, every wrong finite hypothesis is rejected exponentially, with a rate determined jointly by local KL evidence and network influence.

## Problem & setting

A fixed network of agents seeks the true member of a finite hypothesis set. Each agent observes an independent private signal stream whose likelihood model is known locally and may be individually insufficient to identify the truth. Communication is needed to aggregate the distinct information available across the network.

## Method

At each time step, a node performs a Bayesian update using its new private observation, communicates the result, and forms a weighted geometric average of neighbors' beliefs. In log space, the update is a consensus recursion plus cumulative log-likelihood ratios. The analysis separates transient network mixing from asymptotic statistical evidence.

## Key results

Belief in every incorrect hypothesis converges to zero exponentially under the paper's positivity, connectivity, and global-identifiability assumptions. The learning exponent is characterized by a network divergence that combines the stationary influence of nodes with their local KL divergences. The theorem concerns finite hypotheses and conditionally independent signal streams, not arbitrary continuous belief manifolds or correlated messages.

## Relevance to this research

This source supplies a falsifiable scaling comparator for [[Non-Bayesian social learning]] and [[Communication-constrained inference]]. A social-learning experiment should report rejection exponents or centralized-posterior error together with network influence, rather than treating low pairwise disagreement as sufficient evidence of learning. Mapping the result to Gaussian bundle-valued beliefs would require a new continuous-state theorem.

## Cross-links

- Concepts: [[Non-Bayesian social learning]], [[Communication-constrained inference]], [[Decentralized Bayesian inference]]
- Related sources: [[jadbabaie-2012-non-bayesian-social-learning]], [[duchi-2014-distributed-estimation]]

## BibTeX

```bibtex
@article{LalithaJavidiSarwate2018,
  author  = {Lalitha, Anusha and Javidi, Tara and Sarwate, Anand D.},
  title   = {Social Learning and Distributed Hypothesis Testing},
  journal = {IEEE Transactions on Information Theory},
  volume  = {64},
  number  = {9},
  pages   = {6161--6179},
  year    = {2018},
  doi     = {10.1109/TIT.2018.2837050},
  eprint  = {1410.4307},
  archivePrefix = {arXiv}
}
```
