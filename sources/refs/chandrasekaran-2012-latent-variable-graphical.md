---
type: reference
title: "Latent variable graphical model selection via convex optimization"
aliases: ["chandrasekaran2012latent"]
authors: ["Venkat Chandrasekaran", "Pablo A. Parrilo", "Alan S. Willsky"]
year: 2012
venue: "The Annals of Statistics"
doi: "10.1214/11-AOS949"
arxiv: "1008.1290"
url: "https://doi.org/10.1214/11-AOS949"
tags: [cluster/multi-agent, project/multi-agent, field/statistics, field/mathematics, field/cs-ml]
created: 2026-11-10
updated: 2026-11-10
---
# Latent variable graphical model selection via convex optimization

> [!info] Citation
> Chandrasekaran, V., Parrilo, P. A., Willsky, A. S. (2012). *Latent variable graphical model selection via convex optimization*. The Annals of Statistics, 40(4), 1935-1967. [DOI](https://doi.org/10.1214/11-AOS949), [arXiv](https://arxiv.org/abs/1008.1290)

[Local PDF](../pdfs/chandrasekaran-2012-latent-variable-graphical.pdf), 33 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper studies jointly Gaussian observed and latent variables when only the observed variables' statistics are available. It gives conditions for identifiability of a sparse-plus-low-rank decomposition and a convex program that estimates it.

## Problem & setting

Given samples of a subset of variables, with no information on the number of latent variables or how they relate to the observed ones, can one find the number of latent components and a model over all variables? The setting is Gaussian, with the observed variables' conditional statistics given the latent ones specified by a graphical model.

## Method

The authors first state conditions under which the model is identifiable from the marginal statistics of the observed variables: the conditional graphical model among the observed variables must be sparse, while the latent variables' effect must be spread over most observed variables. They then propose a regularized maximum-likelihood program whose regularizer combines the $\ell_1$ norm and the nuclear norm, and view it as joining dimensionality reduction with graphical modeling.

## Key results

The abstract states that the method consistently estimates both the number of latent components and the conditional graphical model structure, in a high-dimensional regime where the numbers of variables grow with the sample size. The geometry of the varieties of sparse and of low-rank matrices enters the analysis.

## Relevance to this research

The manuscript cites the paper for the local identifiability of the two parts of the observed precision matrix, a conditional precision given the latent coordinates minus a low-rank term from marginalizing them, from the observed covariance. It states the recovery by a convex program under a sparse conditional precision and a latent effect spread over most observed coordinates, and uses this for the identifiability of a world-conditional precision from members' statistics in static settings. The reading record says the paper was read in an earlier pass and not reopened for the move to this entry. See [[Gaussian Beliefs]], [[Dimensionality reduction]] and [[Active inference communication and collective boundaries]].

## Cross-links

[[Collective agents literature map]]; [[Gaussian Beliefs]]; [[Dimensionality reduction]]; [[Active inference communication and collective boundaries]].

## BibTeX

```bibtex
@article{chandrasekaran2012latent,
  author  = {Chandrasekaran, Venkat and Parrilo, Pablo A. and Willsky, Alan S.},
  title   = {Latent variable graphical model selection via convex optimization},
  journal = {The Annals of Statistics},
  volume  = {40},
  number  = {4},
  pages   = {1935--1967},
  year    = {2012},
  doi     = {10.1214/11-AOS949},
  eprint  = {1008.1290},
  archiveprefix = {arXiv}
}
```
