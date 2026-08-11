---
type: paper
title: "Optimality Guarantees for Distributed Statistical Estimation"
aliases:
  - "Duchi et al. 2014 communication limits"
authors:
  - Duchi, John C.
  - Jordan, Michael I.
  - Wainwright, Martin J.
  - Zhang, Yuchen
year: 2014
arxiv: 1405.0782
url: https://arxiv.org/abs/1405.0782
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/statistics
  - field/cs-ml
  - field/mathematics
created: 2026-08-10
---

# Optimality Guarantees for Distributed Statistical Estimation

> [!info] Citation
> John C. Duchi, Michael I. Jordan, Martin J. Wainwright, and Yuchen Zhang (2014). "Optimality guarantees for distributed statistical estimation." arXiv: [1405.0782](https://arxiv.org/abs/1405.0782). An earlier version appeared at NIPS 2013 under the title "Information-theoretic lower bounds for distributed statistical estimation with communication constraints."

## TL;DR

Distributed statistical accuracy has an information cost. Duchi and colleagues develop minimax lower bounds and quantitative data-processing inequalities that characterize how much communication is required to match centralized statistical risk in several estimation problems.

## Problem & setting

A data set is split among machines that cannot send their raw samples freely. The paper compares the minimax risk of a communication-limited estimator with the risk of a centralized estimator. It distinguishes simultaneous or independent messages from interactive protocols in which a server can rebroadcast earlier messages.

## Method

The authors refine minimax risk to include a protocol and bit budget, then use information-theoretic reductions and quantitative data-processing inequalities to control how much separation between statistical experiments survives a communication channel. The resulting lower bounds are proved for location and regression families under explicit distributional assumptions.

## Key results

For the studied problems, achieving centralized minimax risk requires a nontrivial minimum number of communicated bits, and interaction does not erase every lower bound. The results quantify model-specific tradeoffs; they do not provide one universal bit law for arbitrary Bayesian messages, topologies, or shared-information structures.

## Relevance to this research

This paper anchors [[Communication-constrained inference]]. Any future claim that a MultiAgentELBO protocol scales better than centralized inference should report message count, bit budget, interaction pattern, and error relative to a centralized oracle. A continuous interaction energy with no encoded message alphabet or channel model has no communication-complexity claim to compare with these bounds.

## Cross-links

- Concepts: [[Communication-constrained inference]], [[Decentralized Bayesian inference]]
- Related sources: [[campbell-how-2014-decentralized-bayes]], [[bandyopadhyay-chung-2018-logop-filtering]], [[lalitha-2018-distributed-hypothesis-testing]]

## BibTeX

```bibtex
@misc{DuchiJordanWainwrightZhang2014,
  author        = {Duchi, John C. and Jordan, Michael I. and Wainwright, Martin J. and Zhang, Yuchen},
  title         = {Optimality Guarantees for Distributed Statistical Estimation},
  year          = {2014},
  eprint        = {1405.0782},
  archivePrefix = {arXiv},
  primaryClass  = {stat.ML}
}
```
