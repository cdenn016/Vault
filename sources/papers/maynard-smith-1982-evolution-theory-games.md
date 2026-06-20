---
type: reference
title: "Evolution and the Theory of Games"
aliases: ["Maynard Smith 1982", "Foundations of evolutionary game theory"]
authors: ["Maynard Smith J."]
year: 1982
tags: [cluster/social-physics, project/social-physics, field/biology, field/economics, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# Evolution and the Theory of Games

> [!info] Citation
> Maynard Smith, J. (1982). *Evolution and the Theory of Games*. Cambridge University Press. ISBN 978-0521288842.

## TL;DR
This monograph is the founding book-length treatment of evolutionary game theory (EGT). It systematizes the application of game-theoretic reasoning to evolving populations, replacing the rational optimizing agent of classical game theory with Darwinian selection acting on heritable strategies. The central organizing concept is the evolutionarily stable strategy (ESS): a strategy that, once common, cannot be invaded by any rare mutant. The book develops the hawk-dove game, asymmetric contests, the war of attrition, ESS in continuous strategy spaces, mixed strategies, and the relation between ESS and population-level game dynamics, establishing the vocabulary and methods the field has used ever since.

## What it establishes
A strategy $s^*$ is an ESS if for every alternative $s \neq s^*$ either $E(s^*, s^*) > E(s, s^*)$, or $E(s^*, s^*) = E(s, s^*)$ and $E(s^*, s) > E(s, s)$, where $E(a,b)$ is the expected payoff to an $a$-player against a $b$-player. The first condition is a Nash-equilibrium requirement; the second is the uninvadability refinement that makes ESS a stronger, dynamically meaningful equilibrium notion. The book connects this static stability criterion to the dynamics of population frequencies and frames a wide range of biological conflicts — territorial display, parental investment, sex ratios — as games with ESS solutions.

## Relevance to this research
As the authoritative book-length foundation of EGT, this is the canonical reference any complete treatment of the evolutionary-game neighborhood requires. It is adjacent to the belief-inertia VFE machinery rather than part of it — it predates and does not use information geometry, natural-gradient flow, or variational free energy — but it grounds the overdamped collective-dynamics analogy the program invokes, supplying the equilibrium concept (ESS) and the population-thinking that the program echoes when it studies stable consensus configurations of coupled belief-carrying agents. See [[Evolutionary game theory and cooperation]], [[Multi-agent variational free energy]], and [[Sociophysics]].

## Cross-links
- Concept: [[Evolutionary game theory and cooperation]]
- Related sources: [[maynard-smith-price-1973-logic-animal-conflict]], [[hofbauer-sigmund-1998-evolutionary-games-population-dynamics]], [[nowak-2006-evolutionary-dynamics-book]]

## BibTeX
```bibtex
@book{maynardsmith1982evolution,
  author    = {Maynard Smith, John},
  title     = {Evolution and the Theory of Games},
  publisher = {Cambridge University Press},
  year      = {1982},
  isbn      = {978-0521288842}
}
```
