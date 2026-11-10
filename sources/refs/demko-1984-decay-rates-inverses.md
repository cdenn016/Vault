---
type: reference
title: "Decay rates for inverses of band matrices"
aliases: ["demko1984decay"]
authors: ["Stephen Demko", "William F. Moss", "Philip W. Smith"]
year: 1984
venue: "Mathematics of Computation"
doi: "10.1090/S0025-5718-1984-0758197-9"
url: "https://doi.org/10.1090/S0025-5718-1984-0758197-9"
tags: [cluster/multi-agent, project/multi-agent, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---
# Decay rates for inverses of band matrices

> [!info] Citation
> Demko, S., Moss, W. F., Smith, P. W. (1984). *Decay rates for inverses of band matrices*. Mathematics of Computation, 43(168), 491-499. [DOI](https://doi.org/10.1090/S0025-5718-1984-0758197-9)

No local copy: no open-access file passed validation on November 10, 2026. Reading basis: abstract.

## TL;DR

A proof, via spectral theory and classical approximation theory, that entries of the inverse of a band matrix decay exponentially, with a rate given in terms of the spectrum.

## Problem & setting

The question is how fast the entries of $A^{-1}$ decay away from the diagonal when $A$ is banded.

## Method

Spectral theory and classical approximation theory give a new proof of exponential decay. The rate is bounded using the (essential) spectrum of $AA^{*}$ for general $A$ and of $A$ for positive definite $A$.

## Key results

The abstract states that the bound is attained in the positive definite case. The results are extended to a class of generalized eigenvalue problems, to certain sparse nonbanded matrices, and to decay rates for certain generalized inverses.

## Relevance to this research

The Collective Agents manuscript cites the paper for the statement that banded matrices have explicit decay rates for their inverses, in an argument that the precision (inverse covariance) of a collective decays with distance. This bears on locality of Gaussian beliefs and blanket structure. It connects to [[Gaussian Beliefs]] and [[Markov Blanket]].

## Cross-links

[[Collective agents literature map]]; [[Gaussian Beliefs]]; [[Markov Blanket]]; [[dahlhaus-2000-graphical-interaction-models]].

## BibTeX

```bibtex
@article{demko1984decay,
  author  = {Demko, Stephen and Moss, William F. and Smith, Philip W.},
  title   = {Decay rates for inverses of band matrices},
  journal = {Mathematics of Computation},
  volume  = {43},
  number  = {168},
  pages   = {491--499},
  year    = {1984},
  doi     = {10.1090/S0025-5718-1984-0758197-9}
}
```
