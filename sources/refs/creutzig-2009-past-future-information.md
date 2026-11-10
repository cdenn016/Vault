---
type: reference
title: "Past-future information bottleneck in dynamical systems"
aliases: ["creutzig2009past"]
authors: ["Felix Creutzig", "Amir Globerson", "Naftali Tishby"]
year: 2009
venue: "Physical Review E"
doi: "10.1103/PhysRevE.79.041925"
url: "https://doi.org/10.1103/PhysRevE.79.041925"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/physics, field/statistics, field/neuroscience]
created: 2026-11-10
updated: 2026-11-10
---
# Past-future information bottleneck in dynamical systems

> [!info] Citation
> Creutzig, F., Globerson, A., Tishby, N. (2009). *Past-future information bottleneck in dynamical systems*. Physical Review E, 79(4), 041925. [DOI](https://doi.org/10.1103/PhysRevE.79.041925)

No local copy: no open-access file passed validation on November 10, 2026. Reading basis: abstract and manuscript reading record.

## TL;DR

An information-theoretic framework that extracts the part of an input's past that is predictive of the output's future, which leads to a generalized eigenvalue problem.

## Problem & setting

The abstract frames the problem as a trade-off between accuracy of representation and coding cost for systems that process information in real time.

## Method

The trade-off is operationalized in an information-theoretic objective. The abstract reports a generalized eigenvalue problem as the outcome, a relation to canonical correlation analysis, and a numerical example.

## Key results

Per the abstract, the input history unfolds through structural phase transitions that correspond to additional dimensions of a state space, and the work relates information-theoretic optimization to joint system identification and model reduction.

## Relevance to this research

The Collective Agents manuscript cites the linear past-future bottleneck as a further precedent for its construction of environment-side sensing, in which a window of past observations is compressed to be predictive of an observation at a horizon, and it says it has not compared the two in detail. The manuscript's reading record states that the paper was known from its abstract page only. It connects to [[Information bottleneck]], [[Canonical Correlation Analysis]] and [[Coarse Graining]].

## Cross-links

[[Collective agents literature map]]; [[Information bottleneck]]; [[Canonical Correlation Analysis]]; [[Coarse Graining]]; [[creutzig-2008-predictive-coding-slowness]].

## BibTeX

```bibtex
@article{creutzig2009past,
  author  = {Creutzig, Felix and Globerson, Amir and Tishby, Naftali},
  title   = {Past-future information bottleneck in dynamical systems},
  journal = {Physical Review E},
  volume  = {79},
  number  = {4},
  pages   = {041925},
  year    = {2009},
  doi     = {10.1103/PhysRevE.79.041925}
}
```
