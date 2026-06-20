---
type: paper
title: "The Evolution of Conformist Transmission and the Emergence of Between-Group Differences"
aliases: ["Henrich & Boyd 1998"]
authors: ["Henrich J.", "Boyd R."]
year: 1998
url: https://doi.org/10.1016/S1090-5138(98)00018-X
tags: [cluster/social-physics, project/social-physics, field/biology, field/psychology, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# The Evolution of Conformist Transmission and the Emergence of Between-Group Differences

> [!info] Citation
> Henrich, J., & Boyd, R. (1998). "The evolution of conformist transmission and the emergence of between-group differences." *Evolution and Human Behavior* **19**(4), 215–241. DOI: [10.1016/S1090-5138(98)00018-X](https://doi.org/10.1016/S1090-5138(98)00018-X).

## TL;DR
A formal model showing that natural selection on social-learning psychology favors a *conformist* bias — a disproportionate tendency to adopt whichever cultural variant is most common among the individuals one samples — across a wide range of conditions, particularly when the environment varies in space and individual (asocial) learning is costly or error-prone. Once established, conformist transmission acts as a homogenizing force within groups and, against migration, maintains stable cultural differences *between* groups, supplying the variance that group-level selection can act on.

## What it establishes
The paper places conformity on an adaptive footing and pins down its dynamical signature. Sampling $n$ models and adopting a variant with a frequency-weighted but *nonlinear* rule, the probability of adoption exceeds the variant's sample frequency when it is in the majority and falls below it when in the minority. For frequency $p$ the conformist adoption probability takes the cubic form
$$
p' = p + D\,p(1-p)(2p-1), \qquad D > 0,
$$
which has stable fixed points at $p=0$ and $p=1$ and an unstable interior equilibrium at $p=1/2$. This makes the within-group dynamics *bistable*: small majorities are amplified to fixation. Because conformity drives each group toward one or the other consensus, it counteracts the homogenizing effect of between-group migration and so preserves persistent inter-group variation, a precondition the authors emphasize for cultural group selection.

## Relevance to this research
Conformist transmission is the nonlinear, majority-amplifying force that produces multistability and persistent group polarization — exactly the behavior the SocialPhysics program studies under the heading of echo chambers and clustering. The cubic adoption rule is the frequency-dependent term that separates genuine social influence from linear consensus (DeGroot / Friedkin–Johnsen) dynamics, and its bistable structure is precisely what a VFE coupling must produce to generate metastable clusters rather than a single global consensus. In the gauge-theoretic functional this maps onto a regime where the attention kernel $\beta_{ij}$ over-weights agreement with the local majority, breaking the contractivity of pure averaging and yielding stable, separated belief basins. Strong, mechanism-level relevance to the polarization claim. See [[Echo chambers and polarization]].

Concept links: [[Echo chambers and polarization]], [[Cultural evolution and social learning]], [[Opinion dynamics]], [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Cultural evolution and social learning]]
- Related sources: [[boyd-richerson-1985-culture-evolutionary-process]], [[henrich-2016-secret-of-our-success]], [[henrich-boyd-2002-modeling-cognition-culture]]

## BibTeX
```bibtex
@article{henrich1998evolution,
  author  = {Henrich, Joseph and Boyd, Robert},
  title   = {The evolution of conformist transmission and the emergence of between-group differences},
  journal = {Evolution and Human Behavior},
  volume  = {19},
  number  = {4},
  pages   = {215--241},
  year    = {1998},
  doi     = {10.1016/S1090-5138(98)00018-X}
}
```
