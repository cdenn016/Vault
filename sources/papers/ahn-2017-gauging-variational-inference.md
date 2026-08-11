---
type: paper
title: Gauging Variational Inference
aliases:
  - Ahn Chertkov Shin 2017
authors:
  - Sungsoo Ahn
  - Michael Chertkov
  - Jinwoo Shin
year: 2017
arxiv: "1703.01056"
url: https://proceedings.neurips.cc/paper/2017/hash/8d420fa35754d1f1c19969c88780314d-Abstract.html
tags:
  - cluster/vfe
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
  - field/physics
status: stable
created: 2026-08-10
updated: 2026-08-10
---

# Gauging Variational Inference

> [!info] Citation
> Sungsoo Ahn, Michael Chertkov, and Jinwoo Shin. “Gauging Variational Inference.” *Advances in Neural Information Processing Systems 30*, pp. 2881–2890, 2017. [Proceedings](https://proceedings.neurips.cc/paper/2017/hash/8d420fa35754d1f1c19969c88780314d-Abstract.html); [arXiv:1703.01056](https://arxiv.org/abs/1703.01056).

## TL;DR

The paper optimizes over invertible reparameterizations of graphical-model factors that preserve the partition function, yielding gauged mean-field and belief-propagation approximations. These gauges can tighten variational lower bounds and are exact for certain single-loop models.

## Problem & setting

Standard mean-field and belief propagation approximate a discrete graphical model in its supplied factorization even though many algebraically different factor tables encode the same partition function. The authors treat this representation freedom as an optimization variable.

## Method

Gauge transformations act locally on factor indices with inverse transformations on adjacent factors, leaving full contractions and hence the partition function invariant. The authors jointly optimize gauge parameters and variational approximations, deriving gauged mean-field (G-MF) and gauged belief propagation (G-BP) objectives and algorithms.

## Key results

- G-MF and G-BP provide lower bounds on the partition function and generalize their ungauged counterparts.
- For a special class of single-loop graphical models, the gauged formulation can recover the exact partition function.
- Experiments reported in the paper show improvements over ordinary MF/BP on the tested models.

## Relevance to this research

This is a direct precedent for treating representational redundancy as a variational degree of freedom. It suggests tests that verify invariance of a factor contraction while optimizing the factor gauge, and it offers a discrete graphical-model baseline against which any claimed benefit of learned gauge choice should be compared.

## Scope limits

> [!warning] Non-equivalence
> The paper’s “gauge” is an algebraic reparameterization of discrete factor tensors. It is **not automatically equivalent** to passive changes of local frame in a principal bundle with structure group $\mathrm{GL}(K)$, and its preserved partition function does not by itself establish connection, curvature, holonomy, or bundle-equivariance claims in this project. A correspondence would require an explicit map between objects, group actions, and invariants.

## Cross-links

- [[Belief Propagation]]
- [[Mean-Field Approximation]]
- [[Evidence lower bound (ELBO)]]
- [[Gauge transformation]]
- [[Quotient Bayesian learning]]

## BibTeX

```bibtex
@inproceedings{ahn2017gauging,
  title     = {Gauging Variational Inference},
  author    = {Ahn, Sungsoo and Chertkov, Michael and Shin, Jinwoo},
  booktitle = {Advances in Neural Information Processing Systems 30},
  pages     = {2881--2890},
  year      = {2017},
  url       = {https://proceedings.neurips.cc/paper/2017/hash/8d420fa35754d1f1c19969c88780314d-Abstract.html},
  eprint    = {1703.01056},
  archivePrefix = {arXiv}
}
```
