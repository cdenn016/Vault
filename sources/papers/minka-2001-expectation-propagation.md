---
type: paper
title: "Expectation Propagation for Approximate Bayesian Inference"
aliases:
  - Minka 2001
  - minka2001expectation
  - Expectation propagation
authors:
  - Minka, Thomas P.
year: 2001
arxiv: "1301.2294"
pdf: sources/pdfs/minka-2001-expectation-propagation.pdf
tags:
  - cluster/vfe
  - project/transformer
  - field/statistics
  - field/cs-ml
created: 2026-10-24
---

# Expectation Propagation for Approximate Bayesian Inference

> [!info] Citation
> Minka, T. P. (2001). *Expectation propagation for approximate Bayesian inference*. Proceedings of the 17th Conference on Uncertainty in Artificial Intelligence (UAI 2001), pp. 362–369. arXiv:1301.2294.

## TL;DR
Assumed-density filtering (ADF) processes the factors of a posterior one at a time and, after each exact update, projects back onto a tractable family by matching moments. Expectation propagation (EP) revisits each factor's approximation so the retained expectations become mutually consistent, unifying ADF and loopy belief propagation.

## Method
Section 2 reviews ADF ("moment matching", "weak marginalization"): include one factor exactly, then replace the result by the member of the family with the same expected sufficient statistics, which minimizes $\mathrm{KL}(\hat p\Vert q)$ for the one-step posterior $\hat p$. EP stores each factor's contribution as a site approximation and iterates. The running example is a Gaussian observed in clutter, a two-component mixture likelihood, where EP is reported more accurate than Laplace's method, variational Bayes and Monte Carlo at similar cost; the method also trains Bayes point machines.

## Relevance to this research
The exact `prototype_agents` block of [[VFE Transformer Program|vfe3]] is one ADF step: it computes the exact Gaussian-mixture posterior over template label and content, then collapses it to one Gaussian by moment matching, discarding the label posterior. A depth stack of such blocks is sequential ADF without EP's revisiting step, and Minka's analysis of what ADF loses (information discarded early that matters later) applies to carrying or dropping the label belief across layers. The clutter problem is the same structure as one record and a mixture of sources ([[Template routing]]).

## Cross-links
- Themes: [[Inference machinery — variational EM and filtering]]
- Methods: [[Template routing]]
- Related sources: [[bovy-2011-extreme-deconvolution]], [[ghahramani-2000-switching-state-space]], [[winn-2005-variational-message-passing]]

## BibTeX
```bibtex
@inproceedings{minka2001expectation,
  author    = {Minka, Thomas P.},
  title     = {Expectation Propagation for Approximate {B}ayesian Inference},
  booktitle = {Proceedings of the Seventeenth Conference on Uncertainty in Artificial Intelligence},
  pages     = {362--369},
  year      = {2001},
  eprint    = {1301.2294},
  archivePrefix = {arXiv}
}
```
