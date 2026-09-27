---
type: paper
title: "Supervised Learning from Incomplete Data via an EM Approach"
aliases:
  - Ghahramani Jordan 1994
  - ghahramani1994
  - Gaussian mixture regression
authors:
  - Ghahramani, Zoubin
  - Jordan, Michael I.
year: 1994
url: https://proceedings.neurips.cc/paper/1993/hash/f2201f5191c4e92cc5af043eebfd0946-Abstract.html
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-09-27
---

# Supervised Learning from Incomplete Data via an EM Approach

> [!info] Citation
> Ghahramani, Z., & Jordan, M. I. (1994). *Supervised learning from incomplete data via an EM approach*. In Advances in Neural Information Processing Systems 6 (NIPS 1993), pp. 120–127.

## TL;DR
Supervised learning is recast as density estimation: fit a mixture model to the joint density of inputs and outputs by EM, then predict by conditioning on the input. Missing input components are handled inside the same EM framework, both for estimating the mixture and for prediction.

## Method
A Gaussian mixture over the joint vector $(x,y)$ is fit by EM. For a query $x$, the conditional mean is
$$\mathbb E[y\mid x]=\sum_a r_a(x)\bigl(m_a^{y}+\Sigma_a^{yx}(\Sigma_a^{xx})^{-1}(x-m_a^{x})\bigr),\qquad r_a(x)\propto\pi_a\mathcal N(x;m_a^x,\Sigma_a^{xx}),$$
a responsibility-weighted combination of local linear regressions.

## Key results
The approach handles arbitrary patterns of missing inputs within one likelihood framework and gives competitive regression and classification results in the paper's experiments.

## Relevance to this research
The conditional-mean formula above is the generative justification for untied values in [[Template routing]]: if each template is a joint Gaussian over a token's state and a residual increment, conditioning gives $\sum_a r_a(k)(w_a+B_a(k-\nu_a))$, and the implemented vfe3 block is the case $B_a=0$ with the point responsibilities replaced by variational KL responsibilities. See [[dennis-2026-template-routing]] for the scope of that replacement (exact only as the belief covariance vanishes).

## Cross-links
- Concepts: [[Variational EM]], [[Mean-Field Approximation]]
- Methods: [[Template routing]]
- Related sources: [[jacobs-1991-mixtures-of-local-experts]], [[dempster-1977-em-algorithm]], [[dennis-2026-template-routing]]

## BibTeX
```bibtex
@inproceedings{ghahramani1994supervised,
  author    = {Ghahramani, Zoubin and Jordan, Michael I.},
  title     = {Supervised learning from incomplete data via an {EM} approach},
  booktitle = {Advances in Neural Information Processing Systems 6},
  pages     = {120--127},
  year      = {1994}
}
```
