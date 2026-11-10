---
type: reference
title: "Stein's method, logarithmic Sobolev and transport inequalities"
aliases: ["ledoux2015stein"]
authors: ["Michel Ledoux", "Ivan Nourdin", "Giovanni Peccati"]
year: 2015
venue: "Geometric and Functional Analysis"
doi: "10.1007/s00039-015-0312-0"
arxiv: "1403.5855"
url: "https://doi.org/10.1007/s00039-015-0312-0"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/mathematics, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# Stein's method, logarithmic Sobolev and transport inequalities

> [!info] Citation
> Ledoux, M., Nourdin, I., Peccati, G. (2015). *Stein's method, logarithmic Sobolev and transport inequalities*. Geometric and Functional Analysis, 25(1), 256-306. [DOI](https://doi.org/10.1007/s00039-015-0312-0), [arXiv](https://arxiv.org/abs/1403.5855)

[Local PDF](../pdfs/ledoux-2015-stein-method-logarithmic.pdf), 52 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and manuscript reading record.

## TL;DR

The paper introduces functional inequalities that link relative entropy, the Stein kernel, relative Fisher information and the Wasserstein distance with respect to a reference distribution on $\mathbb{R}^d$. For the Gaussian reference they improve the classical logarithmic Sobolev inequality and Talagrand's quadratic transportation cost inequality.

## Problem & setting

The classical Gaussian logarithmic Sobolev inequality bounds the relative entropy $H(\nu\,|\,\gamma)$ by half the relative Fisher information $I(\nu\,|\,\gamma)$. The authors extend this by bringing in the Stein kernel, which measures discrepancy from the reference measure. They treat further reference laws, including multidimensional gamma and beta distributions and families of log-concave densities.

## Method

The tools are semigroup interpolation and bounds based on iterated gradients of the Markov generator whose invariant measure is the reference law. A second part obtains entropic bounds for multidimensional functionals from data on the functional and its gradients, within the Markov Triple framework $(E,\mu,\Gamma)$ in which Malliavin-type arguments can be carried out.

## Key results

The new inequalities are stated to bear on convergence to equilibrium, concentration inequalities and entropic convergence expressed through the Stein kernel. The extract does not reach the detailed statements.

## Relevance to this research

The manuscript cites Section 2.3 of this paper as a restatement of the exponential decay of relative entropy along the Ornstein-Uhlenbeck semigroup, which it uses in an appendix on coherence and canonical correlations of a Gaussian pair; the original source of that form is a text by Bakry and others, and the reading record says only the arXiv rendering of this section was read. The decay equals the Gaussian logarithmic Sobolev inequality with constant one. It connects to [[Canonical Correlation Analysis]], [[Fisher information metric]] and [[Entropy]] in the vault's treatment of coherence in communicating agents.

## Cross-links

[[Collective agents literature map]]; [[Canonical Correlation Analysis]]; [[Fisher information metric]]; [[Entropy]].

## BibTeX

```bibtex
@article{ledoux2015stein,
  author        = {Ledoux, Michel and Nourdin, Ivan and Peccati, Giovanni},
  title         = {Stein's method, logarithmic {Sobolev} and transport inequalities},
  journal       = {Geometric and Functional Analysis},
  volume        = {25},
  number        = {1},
  pages         = {256--306},
  year          = {2015},
  doi           = {10.1007/s00039-015-0312-0},
  eprint        = {1403.5855},
  archivePrefix = {arXiv}
}
```
