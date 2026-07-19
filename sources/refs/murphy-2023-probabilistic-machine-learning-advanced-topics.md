---
type: reference
title: "Probabilistic Machine Learning: Advanced Topics"
aliases:
  - "Murphy 2023"
  - "PML Advanced Topics"
  - "Probabilistic Machine Learning Volume II"
authors:
  - Kevin P. Murphy
year: 2023
url: https://probml.github.io/pml-book/book2.html
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-07-19
updated: 2026-07-19
---

# Probabilistic Machine Learning: Advanced Topics

> [!info] Citation
> Kevin P. Murphy (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press. ISBN 978-0-262-04843-9.

## TL;DR

The second Murphy volume develops the advanced inference and generative-model machinery needed to move beyond elementary mean-field treatments. It covers modern Bayesian computation, variational and Monte Carlo methods, deep generative models, structured latent-variable models, and sequential probabilistic modeling.

## What it establishes

The book presents approximate inference as a collection of explicitly stated approximations to a fixed probabilistic model. Its treatment connects optimization-based inference, stochastic estimators, sampling, amortization, and temporal latent-state models. That separation is useful for tracking whether an error comes from the model, the posterior family, the estimator, or the numerical optimizer.

## Relevance to this research

This volume is the broad computational companion to [[wainwright-2008-graphical-models-variational]]. It supports correlated and structured posterior families, stochastic VFE estimators, sequential gauge-causal models, and the distinction between exact identities and approximation-dependent objectives. It connects directly to [[Amortized inference]], [[Reparameterization trick]], [[Evidence lower bound (ELBO)]], and [[Inference machinery — variational EM and filtering]].

## Access

The [author's book page](https://probml.github.io/pml-book/book2.html) provides a complete author draft under CC BY-NC-ND. A private local copy is stored at `sources/pdfs/murphy-2023-pml-advanced-topics-author-draft.pdf`.

## Cross-links

- Concepts: [[Amortized inference]] · [[Reparameterization trick]] · [[Evidence lower bound (ELBO)]]
- Themes: [[Inference machinery — variational EM and filtering]] · [[Variational free energy and predictive coding]]
- Related sources: [[murphy-2022-probabilistic-machine-learning-introduction]] · [[sarkka-svensson-2023-bayesian-filtering-smoothing]]

## BibTeX

```bibtex
@book{Murphy2023PMLAdvanced,
  author    = {Kevin P. Murphy},
  title     = {Probabilistic Machine Learning: Advanced Topics},
  publisher = {MIT Press},
  year      = {2023},
  isbn      = {9780262048439},
  url       = {https://probml.github.io/pml-book/book2.html}
}
```
