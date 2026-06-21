---
type: concept
title: "Markov chain Monte Carlo"
aliases:
  - "MCMC"
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Markov chain Monte Carlo

Markov chain Monte Carlo (MCMC) is a family of algorithms that draw samples from an intractable posterior by constructing a Markov chain whose stationary distribution is the target. Methods range from Metropolis-Hastings and Gibbs sampling to gradient-based Hamiltonian Monte Carlo (HMC) and its self-tuning variant NUTS, which scale to high-dimensional continuous parameter spaces. MCMC is the asymptotically-exact counterpart to variational inference: slower but unbiased, it serves as a gold-standard benchmark for the quality of the program's variational free-energy approximations.

## Related
[[Variational free energy]], [[Amortized inference]]

## Sources
[[salvatier2016probabilistic]], [[hoffman2014no]]
