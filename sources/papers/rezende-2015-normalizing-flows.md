---
type: paper
title: "Variational Inference with Normalizing Flows"
aliases:
  - "rezende-2015-normalizing-flows"
  - "Variational Inference with Normalizing Flows"
  - "Normalizing flows"
  - "Rezende Mohamed 2015"
  - "rezende2015normalizingflows"
authors:
  - "Rezende, Danilo Jimenez"
  - "Mohamed, Shakir"
year: 2015
url: https://arxiv.org/abs/1505.05770
venue: "ICML"
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Variational Inference with Normalizing Flows

> [!info] Citation
> Rezende, Danilo Jimenez, Mohamed, Shakir (2015). "Variational Inference with Normalizing Flows." ICML. https://arxiv.org/abs/1505.05770

## TL;DR
Builds flexible variational posteriors by transforming a simple base density through a sequence of invertible maps (normalizing flows), tracking the change of density via the Jacobian determinant. This escapes the mean-field/Gaussian limitation of standard variational inference while keeping a tractable ELBO.

## Relevance to this research
Defines how to enrich the approximate posterior in variational free-energy inference beyond the Gaussian beliefs the program uses by default; a reference point for trading off belief expressivity against tractability.

## Cross-links
[[Variational free energy]], [[Amortized inference]]

## BibTeX
```bibtex
@inproceedings{rezende2015normalizingflows,
  title={Variational Inference with Normalizing Flows},
  author={Rezende, Danilo Jimenez and Mohamed, Shakir},
  booktitle={International Conference on Machine Learning (ICML)},
  pages={1530--1538},
  year={2015},
  note={arXiv:1505.05770}
}
```
