---
type: paper
title: "Extreme Deconvolution: Inferring Complete Distribution Functions from Noisy, Heterogeneous and Incomplete Observations"
aliases:
  - Bovy 2011
  - bovy2011extreme
  - Extreme deconvolution
authors:
  - Bovy, Jo
  - Hogg, David W.
  - Roweis, Sam T.
year: 2011
arxiv: "0905.2979"
url: https://doi.org/10.1214/10-AOAS439
pdf: sources/pdfs/bovy-2011-extreme-deconvolution.pdf
tags:
  - cluster/vfe
  - project/transformer
  - field/statistics
  - field/physics
created: 2026-10-24
---

# Extreme Deconvolution

> [!info] Citation
> Bovy, J., Hogg, D. W., & Roweis, S. T. (2011). *Extreme deconvolution: Inferring complete distribution functions from noisy, heterogeneous and incomplete observations*. The Annals of Applied Statistics, 5(2B), 1657–1677. doi:10.1214/10-AOAS439. arXiv:0905.2979.

## TL;DR
A Gaussian mixture is fitted to data in which every point carries its own known Gaussian measurement covariance (and its own projection that removes missing directions). The model is the underlying mixture convolved with each point's noise, and an EM algorithm recovers the error-deconvolved density common to all samples.

## Method
Each observation is $w_i=R_iv_i+\text{noise}$ with noise covariance $S_i$ known per point, and the latent $v_i$ is drawn from $\sum_j\alpha_j\mathcal N(m_j,V_j)$. Section 2 writes the likelihood of the noisy mixture; Section 3 gives the EM algorithm, whose E-step needs the label posteriors $q_{ij}$ and the conditional moments of $v_i$ given $w_i$ and component $j$ (the Gaussian conditioning of the latent on its noisy record). Section 4 adds conjugate priors on all parameters and a split-and-merge procedure for local maxima. The application (Section 5) infers the three-dimensional velocity distribution of nearby stars from two-dimensional Hipparcos measurements.

## Relevance to this research
With $R_i=I$ this is exactly the record model behind the `prototype_agents` block MLP of [[VFE Transformer Program|vfe3]]: a template bank $\pi_a\mathcal N(\nu_a,\Lambda_a)$ observed through a token-specific Gaussian record with covariance $C_i$. The block's component posterior means equal this paper's E-step conditional means, and `block_mlp_em_weight` adds a gradient form of its M-step (VFE_3.0 `explainer_video/research/notes_2026-10-24/answers_verified.md`, Q51(3)). The correspondence is algebraic: an internal carrier covariance does not inherit the empirical meaning of a measured error. See [[Template routing]].

## Cross-links
- Methods: [[Template routing]], [[Variational EM]]
- Related sources: [[ghahramani-1994-incomplete-data-em]], [[efron-2011-tweedie-formula]], [[minka-2001-expectation-propagation]]

## BibTeX
```bibtex
@article{bovy2011extreme,
  author  = {Bovy, Jo and Hogg, David W. and Roweis, Sam T.},
  title   = {Extreme Deconvolution: Inferring Complete Distribution Functions from Noisy, Heterogeneous and Incomplete Observations},
  journal = {The Annals of Applied Statistics},
  volume  = {5},
  number  = {2B},
  pages   = {1657--1677},
  year    = {2011},
  doi     = {10.1214/10-AOAS439}
}
```
