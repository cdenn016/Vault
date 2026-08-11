---
type: paper
title: "Kullback-Leibler Average, Consensus on Probability Densities, and Distributed State Estimation with Guaranteed Stability"
aliases:
  - "Battistelli and Chisci 2014 density consensus"
  - "KLA density consensus"
authors:
  - Battistelli, Giorgio
  - Chisci, Luigi
year: 2014
arxiv: null
doi: 10.1016/j.automatica.2013.11.042
url: https://doi.org/10.1016/j.automatica.2013.11.042
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

# Kullback-Leibler Average, Consensus on Probability Densities, and Distributed State Estimation with Guaranteed Stability

> [!info] Citation
> Giorgio Battistelli and Luigi Chisci (2014). "Kullback--Leibler average, consensus on probability densities, and distributed state estimation with guaranteed stability." *Automatica* **50**(3), 707--718. DOI: [10.1016/j.automatica.2013.11.042](https://doi.org/10.1016/j.automatica.2013.11.042).

## TL;DR

The paper turns logarithmic pooling into a distributed consensus algorithm on entire probability densities. Its target is the weighted Kullback--Leibler average, a normalized geometric mean of local densities. In the linear-Gaussian filtering case, the construction yields a networked estimator with mean-square bounded errors under stated connectivity and collective-observability conditions.

## Problem & setting

Sensor nodes repeatedly combine local posterior densities with those of their neighbors. The objective is scalable distributed state estimation without a fusion center. The relevant question is density agreement under a communication graph, not whether a set of local posteriors is conditionally independent evidence whose product equals a centralized Bayesian posterior.

## Method

For weights summing to one, the Kullback--Leibler average is
$$
\bar p=\arg\min_p\sum_i w_i\,\mathrm{KL}(p\Vert p_i)
\propto\prod_i p_i^{w_i}.
$$
The nodes iteratively apply geometric pooling with consensus weights. In the Gaussian case, natural parameters average linearly. A single consensus step has the form of covariance intersection, while repeated steps drive the local densities toward a common KLA.

## Key results

The authors establish convergence of the density-consensus procedure under network assumptions and prove stability of the associated linear distributed state estimator: estimation-error covariances remain bounded at all nodes under connectivity and collective observability, for any positive number of consensus steps. The guarantee concerns the proposed filtering model and does not make logarithmic pooling an exact centralized Bayes rule when inputs reuse common information.

## Relevance to this research

This source anchors the dynamic side of [[Probabilistic opinion pooling]], [[Decentralized Bayesian inference]], and [[Conservative information fusion]]. It supplies an implementable comparator for the present engineered symmetric Gaussian interaction energy: run actual density-consensus iterations and report mixing, nodewise error, and divergence from a centralized oracle. It also forces a semantic distinction between convergence to a variational KLA and recovery of a centralized posterior.

## Cross-links

- Concepts: [[Probabilistic opinion pooling]], [[Decentralized Bayesian inference]], [[Conservative information fusion]]
- Related sources: [[bandyopadhyay-chung-2018-logop-filtering]], [[julier-uhlmann-1997-covariance-intersection]]

## BibTeX

```bibtex
@article{BattistelliChisci2014,
  author  = {Battistelli, Giorgio and Chisci, Luigi},
  title   = {Kullback--Leibler Average, Consensus on Probability Densities, and Distributed State Estimation with Guaranteed Stability},
  journal = {Automatica},
  volume  = {50},
  number  = {3},
  pages   = {707--718},
  year    = {2014},
  doi     = {10.1016/j.automatica.2013.11.042}
}
```
