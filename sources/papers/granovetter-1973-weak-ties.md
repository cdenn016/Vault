---
type: paper
title: "The Strength of Weak Ties"
aliases: ["Granovetter 1973", "Strength of weak ties"]
authors: ["Granovetter M. S."]
year: 1973
url: https://doi.org/10.1086/225469
tags: [cluster/social-physics, project/social-physics, field/sociology, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# The Strength of Weak Ties

> [!info] Citation
> Granovetter, M. S. (1973). *The Strength of Weak Ties*. American Journal of Sociology, 78(6), 1360-1380. doi:10.1086/225469.

## TL;DR
Granovetter argues that the value of a social tie for information diffusion is inversely related to its strength. Strong ties (close friends, kin) tend to be embedded in dense, transitive, mutually overlapping cliques, so the information they carry is redundant; weak ties (acquaintances) more often *bridge* otherwise-disconnected social clusters and therefore transmit genuinely novel information across social distance. The paper links a micro property — the strength and embeddedness of individual dyads — to macro outcomes such as job-finding, the spread of ideas, and the cohesion of whole communities.

## What it establishes
The central structural claim is encoded in the "forbidden triad": if $A$ has strong ties to both $B$ and $C$, then a tie between $B$ and $C$ is highly likely (triadic closure), so a strong tie can almost never be a *local bridge*. Consequently the only edges that can serve as bridges between dense clusters are weak ties. Granovetter operationalizes tie strength as a combination of time spent, emotional intensity, intimacy, and reciprocal services, and shows that the removal of weak ties fragments the macro network far more severely than the removal of an equal number of strong ties — bridges, not hubs, hold the global graph together. This anticipates the small-world insight that a few long-range shortcuts dramatically shorten global path lengths.

## Relevance to this research
Tie strength maps onto the magnitude of the attention weights $\beta_{ij}$ that gate the gauge-transported divergence $\mathrm{KL}(q_i \,\|\, \Omega_{ij}[q_j])$ in the coupling term of the VFE functional. The weak-bridging-tie insight identifies which edges allow belief updates to cross between otherwise-isolated clusters, and thus governs whether the population reaches global consensus or fragments into echo chambers. This is a conceptual foundation for interpreting the model's edge weights rather than a piece of its dynamical machinery. See [[Network structure — small-world and scale-free]], [[Opinion dynamics]], and [[Echo chambers and polarization]].

## Cross-links
- Concept: [[Network structure — small-world and scale-free]]
- Related sources: [[watts-strogatz-1998-small-world]], [[centola-macy-2007-complex-contagion]], [[bond-2012-61-million-experiment]]

## BibTeX
```bibtex
@article{granovetter1973weakties,
  author  = {Granovetter, Mark S.},
  title   = {The Strength of Weak Ties},
  journal = {American Journal of Sociology},
  year    = {1973},
  volume  = {78},
  number  = {6},
  pages   = {1360--1380},
  doi     = {10.1086/225469}
}
```
