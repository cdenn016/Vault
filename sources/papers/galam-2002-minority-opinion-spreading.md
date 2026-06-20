---
type: paper
title: "Minority Opinion Spreading in Random Geometry"
aliases: ["Galam 2002", "Minority opinion spreading"]
authors: ["Galam S."]
year: 2002
url: https://doi.org/10.1140/epjb/e20020045
tags: [cluster/social-physics, project/social-physics, field/physics, field/sociology, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Minority Opinion Spreading in Random Geometry

> [!info] Citation
> Galam, S. (2002). *Minority Opinion Spreading in Random Geometry*. European Physical Journal B 25(4), 403-406. DOI: [10.1140/epjb/e20020045](https://doi.org/10.1140/epjb/e20020045). arXiv:cond-mat/0203553.

## TL;DR
Galam shows that a local majority-rule dynamic with a small, fixed tie-breaking bias can let an initial minority opinion spread until it becomes the global majority. People gather in random small groups (of varying size), each group updates every member to its local majority, and ties are resolved in favour of one designated opinion (e.g. the conservative or status-quo view). Iterating these democratic group discussions repeatedly drives the population away from the true initial split and toward whichever side enjoys the tie-breaking advantage, so an opinion held by well below half the population can come to dominate. The result is a counterintuitive flagship of sociophysics: democratic deliberation can systematically betray the initial majority.

## What it establishes
With groups of size $r$ updating by majority and ties broken toward opinion A, the update map on the support fraction $p$ for A is
$$ p' = P_r(p) + (\text{tie-bias contribution at even } r), $$
whose interior unstable fixed point $p_c$ is pushed below one-half by the bias. Any initial support exceeding this lowered threshold flows under repeated grouping to total victory ($p \to 1$), even when that initial support is a minority of the whole population. Averaging over a distribution of group sizes (the "random geometry") preserves the effect. The mechanism is purely the asymmetry in resolving local ties, compounded by iteration — no persuasion strength, no external field, just biased majority aggregation applied again and again.

## Relevance to this research
This is a counterintuitive flagship Galam result: a discrete majority dynamic with a small structural asymmetry produces a qualitatively novel collective outcome (the minority wins), exactly the kind of emergent, non-obvious phenomenon the belief-inertia program must be able to capture rather than merely the trivial drift to the larger faction. It serves as a clean test case for the overdamped-limit recovery claim — a subsuming VFE functional with a slight prior asymmetry (an uneven $\pi_{ij}$ or a biased hyper-prior $h$) should likewise be able to flip the collective state against the numerical majority. The iterated group-update structure also echoes the program's repeated coarse-graining across scales. See [[Sociophysics]], [[Renormalization-group flow of beliefs]], [[Opinion dynamics]].

## Cross-links
- Concept: [[Discrete spin and majority-rule models of opinion]]
- Related sources: [[galam-1986-majority-rule-hierarchical]], [[galam-gefen-shapir-1982-sociophysics-strike]]

## BibTeX
```bibtex
@article{galam2002minority,
  author  = {Galam, Serge},
  title   = {Minority Opinion Spreading in Random Geometry},
  journal = {European Physical Journal B},
  year    = {2002},
  volume  = {25},
  number  = {4},
  pages   = {403--406},
  doi     = {10.1140/epjb/e20020045}
}
```
