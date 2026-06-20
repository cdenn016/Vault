---
type: paper
title: "Isotropic Majority-Vote Model on a Square Lattice"
aliases: ["de Oliveira 1992", "Majority-vote model"]
authors: ["de Oliveira M. J."]
year: 1992
url: https://doi.org/10.1007/BF01060069
tags: [cluster/social-physics, project/social-physics, field/physics, field/sociology, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Isotropic Majority-Vote Model on a Square Lattice

> [!info] Citation
> de Oliveira, M. J. (1992). *Isotropic Majority-Vote Model on a Square Lattice*. Journal of Statistical Physics 66(1-2), 273-281. DOI: [10.1007/BF01060069](https://doi.org/10.1007/BF01060069).

## TL;DR
De Oliveira defines and studies the noisy majority-vote model: spins on a square lattice each tend to align with the majority of their neighbours, but with a tunable noise parameter that, with probability $q$, makes a site adopt the minority state instead. This single noise parameter plays the role of temperature. The model is genuinely nonequilibrium — its dynamics does not derive from any Hamiltonian and violates detailed balance — yet it displays a continuous order-disorder phase transition at a critical noise $q_c$, and de Oliveira's central finding is that the transition belongs to the same (Ising) universality class as the equilibrium two-dimensional Ising model.

## What it establishes
A spin $\sigma_i = \pm 1$ flips at a rate set by the sign of its neighbourhood majority, with the noise $q$ controlling how often it goes against that majority:
$$ w_i(\sigma) = \tfrac{1}{2}\Big[1 - (1-2q)\,\sigma_i\,\mathrm{sgn}\!\Big(\sum_{j \in \partial i}\sigma_j\Big)\Big]. $$
At low noise the system orders (most spins aligned, nonzero magnetization); above a critical $q_c \approx 0.075$ on the square lattice it disorders. By measuring the magnetization, susceptibility, and Binder cumulant, de Oliveira shows the critical exponents match those of the equilibrium Ising model, establishing that this nonequilibrium dynamics nonetheless sits in the Ising universality class. The work is an early, clean demonstration that nonequilibrium spin dynamics with majority interactions can share the critical behaviour of equilibrium systems.

## Relevance to this research
This is the canonical Ising/Potts-type spin model of opinion with majority dynamics and noise — exactly the discrete spin family the program catalogues. Its noise parameter $q$ is the discrete analogue of a temperature-like disorder, paralleling the role the attention temperature $\tau = \kappa\sqrt{K}$ plays in softening the belief coupling: in both, a tunable stochasticity drives the population from an ordered (consensus) phase to a disordered one through a critical point. Honestly, this is a more specialized reference than the voter or Sznajd originals and the machinery (binary spins, neighbourhood majority) is a coarse caricature of gauge-transported Gaussian beliefs, so its value is as a universality-class benchmark for the program's order-disorder claims rather than as a directly used component. See [[Sociophysics]], [[Discrete spin and majority-rule models of opinion]], [[Echo chambers and polarization]].

## Cross-links
- Concept: [[Discrete spin and majority-rule models of opinion]]
- Related sources: [[sznajd-weron-sznajd-2000-closed-community]], [[galam-1986-majority-rule-hierarchical]]

## BibTeX
```bibtex
@article{deoliveira1992isotropic,
  author  = {de Oliveira, M{\'a}rio J.},
  title   = {Isotropic Majority-Vote Model on a Square Lattice},
  journal = {Journal of Statistical Physics},
  year    = {1992},
  volume  = {66},
  number  = {1-2},
  pages   = {273--281},
  doi     = {10.1007/BF01060069}
}
```
