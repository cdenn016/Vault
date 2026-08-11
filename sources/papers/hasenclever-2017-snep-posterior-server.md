---
type: paper
title: "Distributed Bayesian Learning with Stochastic Natural Gradient Expectation Propagation and the Posterior Server"
aliases:
  - "Hasenclever et al. 2017 SNEP"
  - "Posterior server"
authors:
  - Leonard Hasenclever
  - Stefan Webb
  - Thibaut Lienart
  - Sebastian Vollmer
  - Balaji Lakshminarayanan
  - Charles Blundell
  - Yee Whye Teh
year: 2017
arxiv: 1512.09327
url: https://jmlr.org/papers/v18/16-478.html
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-08-10
---

# Distributed Bayesian Learning with Stochastic Natural Gradient Expectation Propagation and the Posterior Server

> [!info] Citation
> Hasenclever, L., Webb, S., Lienart, T., Vollmer, S., Lakshminarayanan, B., Blundell, C., & Teh, Y. W. (2017). Distributed Bayesian Learning with Stochastic Natural Gradient Expectation Propagation and the Posterior Server. *Journal of Machine Learning Research*, 18(106), 1-37. https://jmlr.org/papers/v18/16-478.html

## TL;DR

The paper introduces stochastic natural-gradient expectation propagation (SNEP) and an asynchronous posterior-server architecture for data-partitioned Bayesian learning. Workers use local data and Monte Carlo estimates of tilted-distribution moments while a server coordinates likelihood approximations targeting one approximate global posterior.

## Problem & setting

Ordinary EP can be unstable, and centralized Bayesian inference becomes a bottleneck when disjoint data shards reside on multiple workers. The desired system must permit asynchronous local computation without treating independently trained subposteriors as independent evidence at fusion time.

## Method

SNEP recasts EP-related updates through stochastic natural-gradient optimization in exponential-family coordinates. Each worker maintains an approximation to its likelihood contribution, samples from a local tilted distribution, and sends asynchronous updates to the posterior server, which combines the global approximation and returns cavity information.

## Key results

The authors give a convergence result for SNEP under the paper's stochastic-approximation conditions, including Monte Carlo moment estimates, and demonstrate the posterior server on Bayesian logistic regression and neural networks. The result is not a guarantee for arbitrary asynchronous message systems, arbitrary approximation families, or peer-to-peer networks without the server's consistency protocol.

## Relevance to this research

SNEP is a useful comparator for any future distributed implementation of [[Multi-agent variational free energy]]. It separates local computation, approximation error, communication, and the centralized global target more carefully than an informal consensus analogy. It does not establish that independently replacing correlated full conditionals defines a joint law, and the present MultiAgentELBO code implements neither a posterior server nor a decentralized protocol.

## Cross-links

- Concepts: [[Natural gradient]], [[Belief Propagation]], [[Multi-agent variational free energy]], [[Collective active inference]]
- Related sources: [[senoz-2021-local-constraint-vmp]]

## BibTeX

```bibtex
@article{hasenclever2017snep,
  author  = {Hasenclever, Leonard and Webb, Stefan and Lienart, Thibaut and Vollmer, Sebastian and Lakshminarayanan, Balaji and Blundell, Charles and Teh, Yee Whye},
  title   = {Distributed Bayesian Learning with Stochastic Natural Gradient Expectation Propagation and the Posterior Server},
  journal = {Journal of Machine Learning Research},
  volume  = {18},
  number  = {106},
  pages   = {1--37},
  year    = {2017},
  url     = {https://jmlr.org/papers/v18/16-478.html}
}
```
