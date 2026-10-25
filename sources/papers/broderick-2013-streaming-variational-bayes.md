---
type: paper
title: "Streaming Variational Bayes"
aliases:
  - Broderick 2013
  - broderick2013streaming
  - SDA-Bayes
authors:
  - Broderick, Tamara
  - Boyd, Nicholas
  - Wibisono, Andre
  - Wilson, Ashia C.
  - Jordan, Michael I.
year: 2013
arxiv: "1307.6769"
pdf: sources/pdfs/broderick-2013-streaming-variational-bayes.pdf
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/cs-ml
created: 2026-10-24
---

# Streaming Variational Bayes

> [!info] Citation
> Broderick, T., Boyd, N., Wibisono, A., Wilson, A. C., & Jordan, M. I. (2013). *Streaming variational Bayes*. Advances in Neural Information Processing Systems 26. arXiv:1307.6769.

## TL;DR
Bayes' rule is applied sequentially, with the posterior after $b-1$ minibatches used as the prior for minibatch $b$, and any approximating batch primitive $\mathcal A$ (here variational Bayes) is applied at each step. In exponential families the updates become additive in natural parameters, which also permits distributed and asynchronous computation.

## Method
The recursion is $p(\Theta\mid C_1,\ldots,C_b)\propto p(C_b\mid\Theta)p(\Theta\mid C_1,\ldots,C_{b-1})$ (Eq. 1), approximated as $q_b=\mathcal A(C_b,q_{b-1})$ (Eq. 2). With an exponential-family prior and a primitive that returns the same family, each minibatch contributes an additive natural-parameter increment. The method is demonstrated by fitting latent Dirichlet allocation to large document collections and compared with stochastic variational inference.

## Relevance to this research
This is the recursion needed for an in-context, causal meta-agent over a template bank. In a language model a parent belief over the template parameters may aggregate only the prefix, so $q_t(\theta)=\mathcal A(x_t,q_{t-1}(\theta))$; with conjugate Gaussian updates the state is a set of additive sufficient statistics per template, a recurrent memory. The same recursion gives a precise reading of "the posterior of the previous layer is the prior of the next" for a persistent model belief ([[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]]).

## Cross-links
- Concepts: [[Meta-agents and hierarchical emergence]], [[Variational free energy]]
- Themes: [[Inference machinery — variational EM and filtering]]
- Related sources: [[schlag-2021-fast-weight-programmers]], [[minka-2001-expectation-propagation]]

## BibTeX
```bibtex
@inproceedings{broderick2013streaming,
  author    = {Broderick, Tamara and Boyd, Nicholas and Wibisono, Andre and Wilson, Ashia C. and Jordan, Michael I.},
  title     = {Streaming Variational {B}ayes},
  booktitle = {Advances in Neural Information Processing Systems 26},
  year      = {2013},
  eprint    = {1307.6769},
  archivePrefix = {arXiv}
}
```
