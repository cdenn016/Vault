---
type: paper
title: "MCMC using Hamiltonian Dynamics"
aliases:
  - "neal2011mcmc"
  - "neal-2011-mcmc-hamiltonian"
  - "Neal 2011 MCMC"
authors:
  - "Neal, Radford M."
year: 2011
url: https://arxiv.org/abs/1206.1901
venue: "Handbook of Markov Chain Monte Carlo (Chapman & Hall/CRC)"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/cs-ml
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# MCMC using Hamiltonian Dynamics

> [!info] Citation
> Neal, Radford M. (2011). "MCMC using Hamiltonian Dynamics." Handbook of Markov Chain Monte Carlo (Chapman & Hall/CRC). https://arxiv.org/abs/1206.1901

## TL;DR
The canonical tutorial on Hamiltonian Monte Carlo: introduces momentum augmentation, leapfrog integration, energy conservation, and tuning of step size and trajectory length, with practical guidance for high-dimensional Bayesian inference. The reference text from which most modern HMC/NUTS implementations derive.

## Relevance to this research
Grounds the Hamiltonian-dynamics view of sampling that parallels the program's Hamiltonian belief-dynamics formulation of inference and provides the gradient-driven exploration baseline for variational comparisons.

## Cross-links
[[Hamiltonian Monte Carlo]], [[Hamiltonian belief dynamics]]

## BibTeX
```bibtex
@incollection{neal2011mcmc,
  title={MCMC using Hamiltonian dynamics},
  author={Neal, Radford M.},
  booktitle={Handbook of Markov Chain Monte Carlo},
  editor={Brooks, Steve and Gelman, Andrew and Jones, Galin and Meng, Xiao-Li},
  pages={113--162},
  year={2011},
  publisher={Chapman and Hall/CRC},
  doi={10.1201/b10905}
}
```
