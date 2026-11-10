---
type: reference
title: "Stochastic Chaos and Markov Blankets"
aliases: ["friston2021stochastic"]
authors: ["Karl Friston", "Conor Heins", "Kai Ueltzhöffer", "Lancelot Da Costa", "Thomas Parr"]
year: 2021
venue: "Entropy"
doi: "10.3390/e23091220"
url: "https://doi.org/10.3390/e23091220"
tags: [cluster/vfe, cluster/multi-agent, project/multi-agent, field/physics, field/mathematics, field/neuroscience]
created: 2026-11-10
updated: 2026-11-10
---
# Stochastic Chaos and Markov Blankets

> [!info] Citation
> Friston, K., Heins, C., Ueltzhöffer, K., Da Costa, L., Parr, T. (2021). *Stochastic Chaos and Markov Blankets*. Entropy, 23(9), 1220. [DOI](https://doi.org/10.3390/e23091220)

[Local PDF](../pdfs/friston-2021-stochastic-chaos-markov.pdf), 33 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper takes the Lorenz system as a random dynamical system with a nonequilibrium steady-state density and tries to derive, rather than assume, a Markov blanket partition for it. Blankets are identified through the Hessian of the surprisal, and the coupling between internal and external states is read as a generalized synchrony conditioned on blanket states.

## Problem & setting

The free energy principle rests on a partition of states in which internal and external states are conditionally independent given blanket states. The introduction states that the existence and functional form of the densities behind such a partition are usually assumed without proof. The authors therefore ask for a procedure that returns the nonequilibrium steady-state density from given equations of motion and noise statistics.

## Method

The authors apply the Helmholtz decomposition to the steady-state solution of the Fokker-Planck equation, writing the flow as a flow operator acting on the gradient of a scalar field that is the self-information. Parameterizing that field with polynomial expansions gives a density for the Lorenz system. The Hessian of the surprisal then indicates which states are directly coupled, and hence which partitions form blankets.

## Key results

According to the abstract, the construction shows how Markov blankets can be identified for stochastic chaos and how the internal-external coupling takes the form of a conditional synchronization map. The authors close by suggesting that this synchronization may be a mathematical basis for an elemental form of active sentience; this is stated as a suggestion, not a result.

## Relevance to this research

The manuscript cites this paper as the Hessian-based treatment that certified a blanket in coupled Lorenz systems, which it contrasts with later direct tests that find no blanket out of equilibrium. The manuscript knows that exchange through secondary accounts, so the note above rests on the paper's own text only for what the paper claims, not for the rebuttal. The paper belongs to the debate over what a blanket is and which independence is meant, treated in [[Markov blanket interpretation debate]] and [[Markov Blanket]], and it concerns steady states as in [[Nonequilibrium steady state]] and [[Generalised synchrony]].

## Cross-links

[[Collective agents literature map]]; [[Markov Blanket]]; [[Markov blanket interpretation debate]]; [[Nonequilibrium steady state]]; [[Generalised synchrony]]; related notes: friston-2022-very-particular-comment, friston-2023-path-integrals-particular.

## BibTeX

```bibtex
@article{friston2021stochastic,
  author  = {Friston, Karl and Heins, Conor and Ueltzh{\"o}ffer, Kai and Da Costa, Lancelot and Parr, Thomas},
  title   = {Stochastic Chaos and {Markov} Blankets},
  journal = {Entropy},
  volume  = {23},
  number  = {9},
  pages   = {1220},
  year    = {2021},
  doi     = {10.3390/e23091220}
}
```
