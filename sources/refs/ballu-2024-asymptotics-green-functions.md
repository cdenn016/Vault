---
type: reference
title: "Asymptotics of Green functions for Markov-additive processes: an approach via dyadic splitting of integrals"
aliases: ["ballu2024asymptotics"]
authors: ["Théo Ballu"]
year: 2024
arxiv: "2407.10685"
url: "https://arxiv.org/abs/2407.10685"
tags: [cluster/multi-agent, project/multi-agent, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---
# Asymptotics of Green functions for Markov-additive processes: an approach via dyadic splitting of integrals

> [!info] Citation
> Ballu, T. (2024). *Asymptotics of Green functions for Markov-additive processes: an approach via dyadic splitting of integrals*. arXiv preprint. [arXiv](https://arxiv.org/abs/2407.10685)

[Local PDF](../pdfs/ballu-2024-asymptotics-green-functions.pdf), 42 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

A preprint deriving an asymptotic equivalent of the Green function of a discrete Markov-additive process with a finite set $E$, which gives a new proof of a 2020 result of Dussaule and generalizes the Ney-Spitzer theorem to a spatially non-homogeneous case.

## Problem & setting

The process is a Markov chain on $\mathbb{Z}^d\times E$ whose jumps are invariant along the $\mathbb{Z}^d$ component. For sums of independent identically distributed variables, the corresponding asymptotics is the theorem of Ney and Spitzer (1966), which the paper's introduction presents as the starting point.

## Method

The proof follows the argument in Woess's book for the Ney-Spitzer theorem: an integral formula for the Green function, from which the asymptotic equivalent follows. Techniques of Babillot are used, in particular dyadic splitting of integrals, a Fourier-analytic tool for controlling the Fourier transform of a function with a singularity at the origin.

## Key results

The main result is the asymptotic equivalent of the Green function for finite $E$. The contents list a restriction of the integral around zero, identification of the leading term, and a complex-analysis step.

## Relevance to this research

The manuscript did not read the Ney-Spitzer theorem in its original paper. It read the restatement in Section 1.1 of this preprint, which gives the power and the rate but, per the manuscript, not the constant. The restatement supports the manuscript's claim about the exact pointwise decay of correlations with an Ornstein-Zernike prefactor, which the manuscript states only as a remark. This belongs to the scale and correlation-length analysis under [[Critical Phenomena]], [[Renormalization group flow]] and [[Graph Laplacian]].

## Cross-links

[[Collective agents literature map]]; [[Critical Phenomena]]; [[Renormalization group flow]]; [[Graph Laplacian]].

## BibTeX

```bibtex
@misc{ballu2024asymptotics,
  author        = {Ballu, Th{\'e}o},
  title         = {Asymptotics of Green functions for Markov-additive processes: an approach via dyadic splitting of integrals},
  year          = {2024},
  eprint        = {2407.10685},
  archivePrefix = {arXiv},
  note          = {Preprint}
}
```
