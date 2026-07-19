---
type: reference
title: "Probabilistic Machine Learning: An Introduction"
aliases:
  - "Murphy 2022"
  - "PML Introduction"
  - "Probabilistic Machine Learning Volume I"
authors:
  - Kevin P. Murphy
year: 2022
url: https://probml.github.io/pml-book/book1.html
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

# Probabilistic Machine Learning: An Introduction

> [!info] Citation
> Kevin P. Murphy (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press. ISBN 978-0-262-04682-4.

## TL;DR

Murphy supplies the broad probabilistic foundation required before specializing in variational free energy, information geometry, or gauge covariance. The book develops probability, Bayesian decision theory, generative and discriminative modeling, latent-variable models, graphical models, approximate inference, and modern machine-learning methods in a common notation.

## What it establishes

The book treats learning as inference in normalized probabilistic models. It develops likelihoods, priors, posteriors, predictive distributions, conditional independence, Gaussian models, mixtures, latent variables, and the relationship between probabilistic objectives and optimization. This makes it the principal general reference for separating a generative model from an inference family and for recognizing when a proposed objective is a genuine likelihood bound rather than a free-standing energy.

## Relevance to this research

The gauge-VFE program assumes the probability theory and modeling discipline developed here: a defined joint distribution, a posterior or restricted variational family, and a traceable relationship between KL divergence, evidence, and prediction. It should be read before [[wainwright-2008-graphical-models-variational]], [[amari-2016-information-geometry-applications]], and the geometric extensions. It supports [[Evidence lower bound (ELBO)]], [[Variational free energy]], [[Generative model]], and [[Inference machinery — variational EM and filtering]].

## Access

The [author's book page](https://probml.github.io/pml-book/book1.html) provides a complete author draft under CC BY-NC-ND. A private local copy is stored at `sources/pdfs/murphy-2022-pml-introduction-author-draft.pdf`.

## Cross-links

- Concepts: [[Evidence lower bound (ELBO)]] · [[Variational free energy]] · [[Generative model]]
- Themes: [[Inference machinery — variational EM and filtering]] · [[Information geometry and natural gradient]]
- Related sources: [[murphy-2023-probabilistic-machine-learning-advanced-topics]] · [[wainwright-2008-graphical-models-variational]]

## BibTeX

```bibtex
@book{Murphy2022PMLIntroduction,
  author    = {Kevin P. Murphy},
  title     = {Probabilistic Machine Learning: An Introduction},
  publisher = {MIT Press},
  year      = {2022},
  isbn      = {9780262046824},
  url       = {https://probml.github.io/pml-book/book1.html}
}
```
