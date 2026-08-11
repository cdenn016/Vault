---
type: paper
title: "Distributed Bayesian Filtering Using Logarithmic Opinion Pool for Dynamic Sensor Networks"
aliases:
  - "Bandyopadhyay and Chung 2018 LogOP filtering"
  - "Distributed Bayesian Filtering (DBF)"
authors:
  - Bandyopadhyay, Saptarshi
  - Chung, Soon-Jo
year: 2018
arxiv: 1712.04062
doi: 10.1016/j.automatica.2018.07.013
url: https://doi.org/10.1016/j.automatica.2018.07.013
tags:
  - cluster/multi-agent
  - cluster/social-physics
  - cluster/social-physics/networks-and-contagion
  - project/multi-agent
  - project/social-physics
  - field/cs-ml
  - field/statistics
  - field/mathematics
created: 2026-08-10
---

# Distributed Bayesian Filtering Using Logarithmic Opinion Pool for Dynamic Sensor Networks

> [!info] Citation
> Saptarshi Bandyopadhyay and Soon-Jo Chung (2018). "Distributed Bayesian Filtering Using Logarithmic Opinion Pool for Dynamic Sensor Networks." *Automatica* **97**, 7--17. DOI: [10.1016/j.automatica.2018.07.013](https://doi.org/10.1016/j.automatica.2018.07.013). arXiv: [1712.04062](https://arxiv.org/abs/1712.04062).

## TL;DR

This distributed Bayesian filter combines normalized local likelihoods, rather than repeatedly multiplying whole posteriors, using logarithmic pooling and dynamic average consensus over a time-varying network. Each node's aggregate likelihood converges exponentially to an explicitly bounded neighborhood of the centralized joint likelihood, with the bound exposing dynamics, modeling error, and communication error.

## Problem & setting

Heterogeneous sensors observe a common dynamic target and communicate over a periodically strongly connected, time-varying graph. Nodes can exchange information with neighbors only once per filtering time step. The paper asks how closely a distributed nonlinear, non-Gaussian filter can track the Bayesian posterior available to a centralized multisensor estimator.

## Method

Each sensor separates its common predictive prior from its new normalized likelihood. Dynamic average consensus and the logarithmic opinion pool combine those likelihoods across the network. After consensus, each node applies the resulting aggregate likelihood to its local prediction. This separation is important: indiscriminate posterior pooling can recycle the common prior and shared past information.

## Key results

The estimated likelihood at every node converges globally exponentially to an error ball around the centralized joint likelihood. The paper gives an explicit admissible time-step bound depending on target time scale, desired approximation error, and modeling and communication errors, and derives a modified Kalman information-filter form for linear-Gaussian systems. These guarantees rely on the declared connectivity and bounded-error assumptions; they are not generic guarantees for arbitrary asynchronous peer beliefs.

## Relevance to this research

The work supplies the strongest communication-aware baseline for [[Decentralized Bayesian inference]] and [[Communication-constrained inference]]. A future MultiAgentELBO communication layer should report centralized-posterior KL, graph mixing, message frequency, model error, and channel error, not only an interaction energy or final agreement. Its likelihood/posterior distinction also belongs in [[Probabilistic opinion pooling]] and [[Conservative information fusion]].

## Cross-links

- Concepts: [[Decentralized Bayesian inference]], [[Communication-constrained inference]], [[Probabilistic opinion pooling]], [[Conservative information fusion]]
- Related sources: [[battistelli-chisci-2014-kl-density-consensus]], [[duchi-2014-distributed-estimation]]

## BibTeX

```bibtex
@article{BandyopadhyayChung2018,
  author  = {Bandyopadhyay, Saptarshi and Chung, Soon-Jo},
  title   = {Distributed Bayesian Filtering Using Logarithmic Opinion Pool for Dynamic Sensor Networks},
  journal = {Automatica},
  volume  = {97},
  pages   = {7--17},
  year    = {2018},
  doi     = {10.1016/j.automatica.2018.07.013},
  eprint  = {1712.04062},
  archivePrefix = {arXiv}
}
```
