---
type: paper
title: "Copula variational inference"
aliases:
  - "Tran Blei Airoldi 2015 copula VI"
authors:
  - Dustin Tran
  - David M. Blei
  - Edoardo M. Airoldi
year: 2015
arxiv: 1506.03159
url: https://proceedings.neurips.cc/paper/2015/hash/e4dd5528f7596dcdf871aa55cfccc53c-Abstract.html
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-08-10
---

# Copula variational inference

> [!info] Citation
> Tran, D., Blei, D. M., & Airoldi, E. M. (2015). Copula variational inference. In *Advances in Neural Information Processing Systems 28*, 3564-3572. https://proceedings.neurips.cc/paper/2015/hash/e4dd5528f7596dcdf871aa55cfccc53c-Abstract.html

## TL;DR

Copula variational inference augments an existing mean-field or structured variational family with a copula that models residual dependence among latent variables. Alternating optimization of the base variational parameters and copula parameters enlarges the representable family while retaining stochastic-optimization scalability in the paper's examples.

## Problem & setting

Mean-field inference is tractable but suppresses posterior dependence, while bespoke structured families are costly to derive. The paper seeks a reusable way to add dependence to an existing variational procedure without rewriting the entire model-specific inference algorithm.

## Method

Using a copula representation, the method separates marginal distributions from their dependence structure. Coordinate descent alternates between fitting the original variational parameters and fitting the copula. The original approximation is recovered as a restricted case, so the representational optimum of the augmented family cannot be worse when optimized exactly.

## Key results

Across the paper's continuous-latent examples, copula VI reduces mean-field bias, improves posterior-variance and dependency estimates, and scales through stochastic optimization. The family-containment argument concerns the variational optimum, not guaranteed attainment by a finite stochastic run. The presented construction is not an unrestricted discrete tabular $Q$, and it does not automatically respect gauge equivariance or mixed/discrete state constraints.

## Relevance to this research

Copula VI is a candidate intermediate recognition family for compatible continuous latent blocks, to be compared with product, structured Gaussian, and exact finite posterior baselines. It must not be described as a universal bridge from mean field to arbitrary correlated $Q$. Any application to discrete agent states or gauge-transformed variables needs a separately specified copula/relaxation and an equivariance proof.

## Cross-links

- Concepts: [[Mean-Field Approximation]], [[Recognition Density]], [[Multi-agent variational free energy]], [[Evidence lower bound (ELBO)]]
- Related sources: [[hoffman-2013-svi]]

## BibTeX

```bibtex
@inproceedings{tran2015copula,
  author    = {Tran, Dustin and Blei, David M. and Airoldi, Edoardo M.},
  title     = {Copula variational inference},
  booktitle = {Advances in Neural Information Processing Systems 28},
  pages     = {3564--3572},
  year      = {2015},
  url       = {https://proceedings.neurips.cc/paper/2015/hash/e4dd5528f7596dcdf871aa55cfccc53c-Abstract.html}
}
```
