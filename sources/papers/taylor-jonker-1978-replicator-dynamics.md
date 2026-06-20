---
type: paper
title: "Evolutionarily Stable Strategies and Game Dynamics"
aliases: ["Taylor & Jonker 1978", "Derivation of the replicator equation"]
authors: ["Taylor P. D.", "Jonker L. B."]
year: 1978
url: https://doi.org/10.1016/0025-5564(78)90077-9
tags: [cluster/social-physics, cluster/info-geometry, project/social-physics, field/biology, field/mathematics, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# Evolutionarily Stable Strategies and Game Dynamics

> [!info] Citation
> Taylor, P. D., & Jonker, L. B. (1978). *Evolutionarily Stable Strategies and Game Dynamics*. Mathematical Biosciences 40(1–2):145–156. DOI: [10.1016/0025-5564(78)90077-9](https://doi.org/10.1016/0025-5564(78)90077-9).

## TL;DR
Taylor and Jonker supply the dynamical foundation that Maynard Smith's ESS concept initially lacked. Where ESS is a static uninvadability criterion, this paper derives the continuous-time selection dynamics — now called the replicator equation — describing how the frequencies of competing strategies change over time under differential reproductive success. They then establish the relationship between the dynamic rest points of this flow and the static ESS, showing that an ESS is an asymptotically stable equilibrium of the replicator dynamics (the converse does not hold in general).

## What it establishes
The replicator equation governs the strategy-frequency vector $x = (x_1, \dots, x_n)$ on the simplex:
$$\dot{x}_i = x_i\left[(Ax)_i - x^\top A x\right],$$
where $A$ is the payoff matrix, $(Ax)_i$ is the fitness of strategy $i$, and $x^\top A x$ is the population mean fitness. A strategy grows when its fitness exceeds the population average and shrinks when it falls below — selection as a frequency-weighted comparison to the mean. The key theorem links these dynamics to equilibrium concepts: every ESS is an asymptotically stable rest point of this flow, embedding ESS within a genuine dynamical-systems picture.

## Relevance to this research
The replicator dynamics is the prototypical first-order (overdamped) population-flow equation, structurally analogous to the program's overdamped opinion-dynamics limit of VFE gradient flow. The link is stronger than mere analogy: the replicator equation is a natural-gradient / Fisher flow on the probability simplex — a gradient ascent of mean fitness with respect to the Shahshahani metric, which is the simplex restriction of the Fisher information metric. That places it close to the program's information-geometric core, where belief updates are natural-gradient flows on a statistical manifold. The remaining gap is that the replicator metric lives on the discrete simplex, whereas the program flows on the SPD/Gaussian manifold of $(\mu, \Sigma)$, so it is a genuine relative rather than the same equation. See [[Replicator dynamics]], [[Fisher information metric]], and [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Replicator dynamics]]
- Related sources: [[hofbauer-sigmund-1998-evolutionary-games-population-dynamics]], [[maynard-smith-price-1973-logic-animal-conflict]], [[maynard-smith-1982-evolution-theory-games]]

## BibTeX
```bibtex
@article{taylor1978evolutionarily,
  author  = {Taylor, Peter D. and Jonker, Leo B.},
  title   = {Evolutionarily Stable Strategies and Game Dynamics},
  journal = {Mathematical Biosciences},
  volume  = {40},
  number  = {1--2},
  pages   = {145--156},
  year    = {1978},
  doi     = {10.1016/0025-5564(78)90077-9}
}
```
