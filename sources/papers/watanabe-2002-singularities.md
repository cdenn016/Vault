---
type: paper
title: "The Effect of Singularities in a Learning Machine when the True Parameters Do Not Lie on such Singularities"
aliases:
  - "Watanabe and Amari 2002 singularities"
authors:
  - Sumio Watanabe
  - Shun-ichi Amari
year: 2002
arxiv: null
url: https://proceedings.neurips.cc/paper/2002/hash/c2ba1bc54b239208cb37b901c0d3b363-Abstract.html
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/mathematics
  - field/cs-ml
created: 2026-08-10
---

# The Effect of Singularities in a Learning Machine when the True Parameters Do Not Lie on such Singularities

> [!info] Citation
> Watanabe, S., & Amari, S. (2002). The Effect of Singularities in a Learning Machine when the True Parameters Do Not Lie on such Singularities. In *Advances in Neural Information Processing Systems 15* (NIPS 2002). https://proceedings.neurips.cc/paper/2002/hash/c2ba1bc54b239208cb37b901c0d3b363-Abstract.html

## TL;DR

Watanabe and Amari study learning machines whose parameter-to-distribution map is nonidentifiable and whose Fisher information becomes degenerate at singularities. Even when the true parameter is near rather than on a singular set, regular-model relations between training and generalization error can fail.

## Problem & setting

Hidden-variable models such as neural networks and mixtures commonly have parameter symmetries and singular strata. Classical asymptotic learning theory assumes a locally identifiable, nonsingular Fisher metric. The paper analyzes a specified class of learning machines when the truth lies close to, but not exactly on, a singularity.

## Method

The authors use singular-learning asymptotics for a model whose hidden-unit parameter dimension controls behavior near the singular set. Their analysis tracks Bayes generalization and training errors rather than replacing the singular model with a regular quadratic approximation.

## Key results

For the analyzed setting, the paper finds dimension-dependent regions in which generalization error can be larger or smaller than the regular-model comparator and shows that the usual symmetry between generalization and training errors does not hold in general. These results do not establish every later theorem of singular learning theory, and they do not prove regularity properties of an unrelated geometric quotient.

## Relevance to this research

[[Singular statistical models]] provides the correct external category for latent-agent nonidentifiability, gauge orbits, stabilizers, and degenerate [[Fisher information metric|Fisher information]]. A Moore-Penrose inverse on an identifiable tangent subspace is a useful local finite diagnostic, but it does not prove that a global quotient is free, proper, Hausdorff, or smoothly stratified. This paper motivates preserving those obligations rather than applying regular natural-gradient asymptotics across singular strata.

## Cross-links

- Concepts: [[Singular statistical models]], [[Fisher information metric]], [[Statistical manifold]], [[Natural gradient]], [[Model Complexity]]
- Related sources: [[amari-2000-methods-information-geometry]]

## BibTeX

```bibtex
@inproceedings{watanabe2002singularities,
  author    = {Watanabe, Sumio and Amari, Shun-ichi},
  title     = {The Effect of Singularities in a Learning Machine when the True Parameters Do Not Lie on such Singularities},
  booktitle = {Advances in Neural Information Processing Systems 15},
  year      = {2002},
  url       = {https://proceedings.neurips.cc/paper/2002/hash/c2ba1bc54b239208cb37b901c0d3b363-Abstract.html}
}
```
