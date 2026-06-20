---
type: paper
title: "Nonequilibrium Phase Transition in a Model for Social Influence"
aliases: ["Castellano, Marsili & Vespignani 2000", "Axelrod order-disorder transition"]
authors: ["Castellano C.", "Marsili M.", "Vespignani A."]
year: 2000
url: https://doi.org/10.1103/PhysRevLett.85.3536
tags: [cluster/social-physics, project/social-physics, field/physics, field/sociology, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# Nonequilibrium Phase Transition in a Model for Social Influence

> [!info] Citation
> Castellano, C., Marsili, M., & Vespignani, A. (2000). *Nonequilibrium Phase Transition in a Model for Social Influence*. Physical Review Letters 85(16), 3536-3539. DOI: [10.1103/PhysRevLett.85.3536](https://doi.org/10.1103/PhysRevLett.85.3536). arXiv:cond-mat/0003111.

## TL;DR
This paper subjects Axelrod's culture-dissemination model to a statistical-mechanics analysis and shows that the transition between a culturally ordered (monocultural) phase and a disordered (polarized, multicultural) phase is a genuine nonequilibrium phase transition controlled by the number of traits $q$. For fixed number of features $F$, increasing $q$ drives the system across a critical point $q_c$: below it the population converges to a single dominant culture, above it it freezes into many coexisting cultural domains. The nature of the transition depends on $F$ — continuous for $F = 2$ and discontinuous (first-order) for $F > 2$ — placing Axelrod's social model squarely within the language of critical phenomena.

## What it establishes
The order parameter is the relative size of the largest cultural domain, $\langle S_{\max}\rangle / L^2$ on an $L \times L$ lattice, which is of order one in the ordered phase and vanishes in the fragmented phase. As the trait count $q$ (equivalently the initial cultural variance) increases past $q_c$, the largest domain collapses. The authors establish that this order-disorder crossover is a true phase transition in the thermodynamic limit, with the transition being continuous in the two-feature case and switching to discontinuous for three or more features. The work thereby supplies the critical-phenomena vocabulary — order parameter, critical point, transition order — for what Axelrod had reported only as a phenomenological outcome of simulations.

## Relevance to this research
This paper brings the statistical-mechanics phase-transition lens to discrete opinion and culture dynamics, the same critical-phenomena framing the belief-inertia program adopts in treating consensus and polarization as collective phases of a free-energy-minimizing population. The polarized-versus-fragmented transition, with its order parameter and tunable transition order, is a concrete benchmark that any VFE functional claiming to subsume Axelrod-type dynamics should reproduce as it sweeps a control parameter (analogous to the attention temperature $\tau$ or confidence scale). It is an adjacent-to-core analysis of the Axelrod model: it does not supply machinery the functional uses, but it sets the quantitative bar for the program's emergent-transition claims. See [[Axelrod model of cultural dissemination]], [[Echo chambers and polarization]], [[Sociophysics]].

## Cross-links
- Concept: [[Axelrod model of cultural dissemination]]
- Related sources: [[axelrod-1997-dissemination-of-culture]], [[galam-gefen-shapir-1982-sociophysics-strike]]

## BibTeX
```bibtex
@article{castellano2000nonequilibrium,
  author  = {Castellano, Claudio and Marsili, Matteo and Vespignani, Alessandro},
  title   = {Nonequilibrium Phase Transition in a Model for Social Influence},
  journal = {Physical Review Letters},
  year    = {2000},
  volume  = {85},
  number  = {16},
  pages   = {3536--3539},
  doi     = {10.1103/PhysRevLett.85.3536}
}
```
