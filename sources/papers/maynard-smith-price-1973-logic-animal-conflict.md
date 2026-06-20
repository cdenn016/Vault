---
type: paper
title: "The Logic of Animal Conflict"
aliases: ["Maynard Smith & Price 1973", "The hawk-dove game and ESS"]
authors: ["Maynard Smith J.", "Price G. R."]
year: 1973
url: https://doi.org/10.1038/246015a0
tags: [cluster/social-physics, project/social-physics, field/biology, field/economics, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# The Logic of Animal Conflict

> [!info] Citation
> Maynard Smith, J., & Price, G. R. (1973). *The Logic of Animal Conflict*. Nature 246(5427):15–18. DOI: [10.1038/246015a0](https://doi.org/10.1038/246015a0).

## TL;DR
This short Nature paper founds evolutionary game theory by asking why animal contests over resources are so often "limited" — ritualized display rather than escalation to injury — when an unrestrained fighter would seemingly win every encounter. Using computer simulations of strategies (Hawk, Dove, Retaliator, and others) competing for resources at the cost of injury, the authors show that pure aggression is not evolutionarily favored. They introduce the evolutionarily stable strategy (ESS): a strategy such that, if adopted by most of a population, no mutant strategy can invade. The hawk-dove game makes this concrete and explains the prevalence of restraint as an evolutionary equilibrium rather than group-level benevolence.

## What it establishes
In the hawk-dove game with resource value $V$ and injury cost $C$, when $C > V$ neither pure Hawk nor pure Dove is an ESS; the stable outcome is a mixed strategy (or polymorphic population) with Hawk frequency $p^* = V/C$. This was the first explicit formulation of the ESS, defined by the uninvadability condition that a resident strategy do at least as well against itself as any mutant does against it, with strict advantage breaking ties. The paper thereby supplies the population-level fixed-point notion that anchors all subsequent EGT.

## Relevance to this research
The ESS is the population-level equilibrium concept that evolutionary game theory contributes to the program's vocabulary of collective stable states. It is conceptual and adjacent context for the SocialPhysics program: the belief-inertia VFE machinery characterizes stability through gradient-flow rest points and Fisher-inertia (precision-as-mass) rather than through ESS uninvadability, so the correspondence is one of parallel intuition, not mathematical identity. Still, ESS is the canonical fixed-point notion any complete EGT shelf must hold, and it parallels the program's interest in stable consensus configurations of coupled agents. See [[Replicator dynamics]], [[Multi-agent variational free energy]], and [[Opinion dynamics]].

## Cross-links
- Concept: [[Replicator dynamics]]
- Related sources: [[maynard-smith-1982-evolution-theory-games]], [[taylor-jonker-1978-replicator-dynamics]], [[hofbauer-sigmund-1998-evolutionary-games-population-dynamics]]

## BibTeX
```bibtex
@article{maynardsmith1973logic,
  author  = {Maynard Smith, John and Price, George R.},
  title   = {The Logic of Animal Conflict},
  journal = {Nature},
  volume  = {246},
  number  = {5427},
  pages   = {15--18},
  year    = {1973},
  doi     = {10.1038/246015a0}
}
```
