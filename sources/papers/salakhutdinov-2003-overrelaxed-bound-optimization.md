---
type: paper
title: "Adaptive Overrelaxed Bound Optimization Methods"
aliases:
  - "Salakhutdinov 2003"
  - "Salakhutdinov and Roweis 2003"
  - "Overrelaxed EM"
  - "Adaptive overrelaxed EM"
authors:
  - "Salakhutdinov, Ruslan"
  - "Roweis, Sam"
year: 2003
url: https://mlanthology.org/icml/2003/salakhutdinov2003icml-adaptive
pdf: sources/pdfs/salakhutdinov-2003-overrelaxed-bound-optimization.pdf
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-10-25
---

# Adaptive Overrelaxed Bound Optimization Methods

> [!info] Citation
> Salakhutdinov, R., & Roweis, S. (2003). *Adaptive overrelaxed bound optimization methods*. Proceedings of the 20th International Conference on Machine Learning (ICML), 664–671. The local PDF is the copy on Sam Roweis's NYU memorial page.

## TL;DR
Bound optimizers (EM, iterative scaling, CCCP, NMF) can be overrelaxed, $\theta\leftarrow\theta+\eta(M(\theta)-\theta)$ with $\eta>1$. Near an optimum this contracts the error by the spectral radius of the overrelaxed rate matrix instead of EM's, an exponential gain when the fraction of missing information is high. An adaptive scheme grows $\eta$ multiplicatively while the objective improves and falls back to the plain step ($\eta=1$) when it does not, so the objective never decreases.

## Method
For EM the rate matrix is the ratio of missing to complete information near the optimum, and the paper reads a large optimal $\eta$ as a symptom of high missing information. Experiments use a growth factor of 1.1 and report speedups of several times on synthetic and real data.

## Relevance to this research
The overrelaxed arms `_or15` and `_or18` of [[vfe3-2026-10-25-local-learner-test]] use a fixed $\eta$ of 1.5 and 1.8 on the stepwise-EM statistics, without the adaptive safeguard, which the stochastic setting makes harder to apply. They gained 0.004 to 0.005 bits per byte after one pass, far below the paper's batch speedups.

## Cross-links
- Themes: [[Inference machinery — variational EM and filtering]]
- Methods: [[Variational EM]]
- Related sources: [[dempster-1977-em-algorithm]], [[liu-1998-px-em]], [[varadhan-2008-squarem]], [[vfe3-2026-10-25-local-learner-test]]

## BibTeX
```bibtex
@inproceedings{salakhutdinov2003adaptive,
  author    = {Salakhutdinov, Ruslan and Roweis, Sam},
  title     = {Adaptive Overrelaxed Bound Optimization Methods},
  booktitle = {Proceedings of the 20th International Conference on Machine Learning},
  pages     = {664--671},
  year      = {2003}
}
```
