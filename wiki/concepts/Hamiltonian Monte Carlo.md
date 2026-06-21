---
type: concept
title: "Hamiltonian Monte Carlo"
aliases:
  - "HMC"
  - "hamiltonianmontecarlo"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Hamiltonian Monte Carlo

Hamiltonian (Hybrid) Monte Carlo is an MCMC method that augments the target distribution with auxiliary momentum variables and simulates Hamiltonian dynamics (via leapfrog integration) to propose distant, high-acceptance states, suppressing the random-walk behavior of Metropolis. It exploits the gradient of the log-density to move along constant-energy contours, making it efficient in high dimensions; the No-U-Turn Sampler (NUTS) adaptively tunes its trajectory length. It is the natural sampling counterpart to the program's Hamiltonian belief-dynamics view of inference.

## Related
[[Hamiltonian belief dynamics]], [[Variational free energy]]

## Sources
[[hoffman2014no]], [[neal-2011-mcmc-hamiltonian|neal2011mcmc]]
