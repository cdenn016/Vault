---
type: paper
title: "Evolutionary Dynamics on Graphs"
aliases: ["Lieberman, Hauert & Nowak 2005", "Moran process on graphs"]
authors: ["Lieberman E.", "Hauert C.", "Nowak M. A."]
year: 2005
url: https://doi.org/10.1038/nature03204
tags: [cluster/social-physics, project/social-physics, field/biology, field/mathematics, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# Evolutionary Dynamics on Graphs

> [!info] Citation
> Lieberman, E., Hauert, C., & Nowak, M. A. (2005). *Evolutionary Dynamics on Graphs*. Nature 433(7023):312–316. DOI: [10.1038/nature03204](https://doi.org/10.1038/nature03204).

## TL;DR
This paper generalizes the Moran process — the standard birth-death model of selection in a finite, well-mixed population — to populations structured as arbitrary weighted, directed graphs, where each vertex is an individual and edge weights set who can replace whom. The central question is how graph topology controls the fixation probability of an advantageous mutant. The authors show that a large class of graphs (the "isothermal" ones, satisfying a balance condition) reproduce the well-mixed fixation probability, while other structures act as amplifiers of selection (raising the chance a beneficial mutant fixes) or as suppressors (lowering it), with star and superstar graphs giving arbitrarily strong amplification.

## What it establishes
For a mutant of relative fitness $r$ in a well-mixed population of size $N$, the Moran fixation probability is
$$\rho = \frac{1 - 1/r}{1 - 1/r^N}.$$
The isothermal theorem states that a graph yields exactly this $\rho$ if and only if it is isothermal (the sum of incoming edge weights equals the sum of outgoing weights at every vertex), generalizing the well-mixed case. Departures from isothermality produce amplifiers and suppressors of selection; superstar structures can make any advantageous mutant fix with probability approaching one, while suppressors can drive fixation toward the neutral or even disadvantageous regime. Population structure is thus a tunable control on evolutionary outcomes.

## Relevance to this research
This establishes how the topology of the interaction graph controls whether a trait spreads through a population — structurally the same question the program asks about how beliefs propagate and fixate across the agent-coupling graph. It is a strong, directly relevant reference for graph-mediated collective dynamics and emergent consensus/fixation: the amplifier/suppressor dichotomy is exactly the kind of topology-to-outcome map the program seeks when it asks which coupling graphs drive agents toward shared belief versus persistent disagreement. The mechanics (stochastic Moran replacement) differ from VFE gradient flow, so the relationship is one of shared structural questions rather than a shared dynamical law. See [[Evolutionary game theory and cooperation]], [[Community detection and modularity]], and [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Evolutionary game theory and cooperation]]
- Related sources: [[ohtsuki-hauert-lieberman-nowak-2006-simple-rule-graphs]], [[nowak-may-1992-spatial-chaos]], [[santos-pacheco-2005-scale-free-cooperation]]

## BibTeX
```bibtex
@article{lieberman2005evolutionary,
  author  = {Lieberman, Erez and Hauert, Christoph and Nowak, Martin A.},
  title   = {Evolutionary Dynamics on Graphs},
  journal = {Nature},
  volume  = {433},
  number  = {7023},
  pages   = {312--316},
  year    = {2005},
  doi     = {10.1038/nature03204}
}
```
