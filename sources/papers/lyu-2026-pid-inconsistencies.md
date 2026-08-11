---
type: paper
title: "Multivariate Partial Information Decomposition: Constructions, Inconsistencies, and Alternative Measures"
aliases:
  - "Lyu Clark Raviv 2026 PID inconsistencies"
authors:
  - Lyu, Aobo
  - Clark, Andrew
  - Raviv, Netanel
year: 2026
arxiv: 2508.05530
url: https://doi.org/10.1103/8rzp-w5z1
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/statistics
  - field/mathematics
  - field/cs-ml
created: 2026-08-10
---

# Multivariate Partial Information Decomposition: Constructions, Inconsistencies, and Alternative Measures

> [!info] Citation
> Aobo Lyu, Andrew Clark, and Netanel Raviv (2026). "Multivariate Partial Information Decomposition: Constructions, Inconsistencies, and Alternative Measures." *Physical Review E* 113, 034102. DOI: [10.1103/8rzp-w5z1](https://doi.org/10.1103/8rzp-w5z1). arXiv: [2508.05530](https://arxiv.org/abs/2508.05530).

## TL;DR

The paper gives explicit formulas under its axiomatic treatment for the two-source case, then argues that lattice-based multivariate PID faces fundamental consistency obstructions with three or more sources. Its impossibility result is scoped to the analyzed lattice-based construction and consistency requirements; it does not prove that every possible measure of multivariate redundancy or synergy is impossible.

## Problem & setting

PID aims to decompose the information that multiple source variables provide about a target into redundant, unique, and synergistic atoms. Extending the redundancy lattice beyond two sources imposes overlapping marginal and subset constraints that may be mutually inconsistent.

## Method

The authors review PID axioms and desirable properties, derive closed-form two-source atoms satisfying the stated requirements, revisit a known three-source counterexample in which the proposed atoms overcount total information, and extend the obstruction to a theorem about consistency across subsets for lattice-based decompositions. They then construct alternative unique- and synergistic-information measures outside the PID lattice by introducing auxiliary variable systems that remove higher-order dependencies.

## Key results

The primary record reports three contributions: closed-form resolution of the two-source case under the paper's requirements; a three-source inconsistency and a broader impossibility result for lattice-based decompositions when the number of sources exceeds three; and alternative multivariate unique/synergistic measures with additivity and continuity properties plus Ising-model experiments. This is strong counterevidence to treating a high-order PID lattice as canonical, but not a blanket impossibility theorem for all operational or nonlattice information decompositions.

## Relevance to this research

This is a direct caution for [[Partial information decomposition]] as a MultiAgentELBO diagnostic. Two-source demonstrations do not justify a many-agent PID implementation by induction, and a multivariate estimator must declare its axioms and known failure modes. O-information remains usable as a different aggregate statistic, but it does not solve PID's atom-level identification problem.

## Cross-links

- Concepts: [[Partial information decomposition]], [[O-information]]
- Related sources: [[williams-beer-2010-pid]], [[rosas-2019-o-information]]

## BibTeX

```bibtex
@article{LyuClarkRaviv2026,
  author  = {Lyu, Aobo and Clark, Andrew and Raviv, Netanel},
  title   = {Multivariate Partial Information Decomposition: Constructions, Inconsistencies, and Alternative Measures},
  journal = {Physical Review E},
  volume  = {113},
  number  = {3},
  pages   = {034102},
  year    = {2026},
  doi     = {10.1103/8rzp-w5z1},
  eprint  = {2508.05530},
  archivePrefix = {arXiv},
  primaryClass  = {cs.IT}
}
```
