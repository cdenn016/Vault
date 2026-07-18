---
type: reference
title: "Constructing Free-Energy Approximations and Generalized Belief Propagation Algorithms"
aliases:
  - "Yedidia, Freeman, and Weiss 2005"
  - "Region-graph free energy"
authors:
  - Jonathan S. Yedidia
  - William T. Freeman
  - Yair Weiss
year: 2005
url: https://doi.org/10.1109/TIT.2005.850085
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-07-17
updated: 2026-07-17
---

# Constructing Free-Energy Approximations and Generalized Belief Propagation Algorithms

> [!info] Citation
> Jonathan S. Yedidia, William T. Freeman, and Yair Weiss (2005). “Constructing Free-Energy Approximations and Generalized Belief Propagation Algorithms.” *IEEE Transactions on Information Theory* **51**(7), 2282–2312. DOI: [10.1109/TIT.2005.850085](https://doi.org/10.1109/TIT.2005.850085).

## TL;DR

The paper derives Bethe and region-graph free energies for factor graphs and shows that belief-propagation and generalized-belief-propagation fixed points are stationary points of the associated approximate free energies. Region beliefs and counting numbers restore selected correlations and entropy-overlap corrections that naive mean field discards. Exactness holds for the appropriate acyclic constructions; a generic loopy region approximation is not thereby an exact posterior or a guaranteed evidence lower bound.

## What it establishes

Yedidia, Freeman, and Weiss place belief propagation within a variational framework. The Bethe approximation retains node and factor beliefs subject to local consistency constraints, while generalized region graphs extend this construction to overlapping clusters with counting numbers chosen to correct repeated entropy and energy contributions. Their fixed-point result gives a principled route from a chosen region free energy to a message-passing algorithm. The paper also states the conditions needed for a valid region-graph construction and distinguishes exact acyclic cases from approximate loopy cases.

## Why the project cites it

The beyond-mean-field extension in [[participatory-it-from-bit]] uses region beliefs as one rung in a controlled hierarchy between a product posterior and a globally normalized correlated posterior. This source supports the region-graph and generalized-belief-propagation construction, but not an unconditional ELBO claim for arbitrary loopy pseudomarginals. It therefore sharpens [[Mean-Field Approximation]] and [[Belief Propagation]] while leaving sparse normalized block-Gaussian posteriors as the cleanest route when ordinary variational-gap semantics must be retained.

## Local full text

A legally reusable author-hosted MERL/MIT copy is cached locally at `sources/pdfs/Yedidia2005.pdf`. Source: [MIT/MERL author copy](https://people.csail.mit.edu/billf/publications/Constructing_Free_Energy.pdf). SHA-256: `0A9D26D7EBF9D282D8958A451CED38E2231BB0C1BF5AEEB593191CFE295C4629`.

## BibTeX

```bibtex
@article{Yedidia2005,
  author  = {Yedidia, Jonathan S. and Freeman, William T. and Weiss, Yair},
  title   = {Constructing Free-Energy Approximations and Generalized Belief Propagation Algorithms},
  journal = {IEEE Transactions on Information Theory},
  volume  = {51},
  number  = {7},
  pages   = {2282--2312},
  year    = {2005},
  doi     = {10.1109/TIT.2005.850085}
}
```
