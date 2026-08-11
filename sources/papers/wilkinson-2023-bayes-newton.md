---
type: paper
title: "Bayes–Newton Methods for Approximate Bayesian Inference with PSD Guarantees"
aliases:
  - "Wilkinson et al. 2023 Bayes-Newton"
authors:
  - William J. Wilkinson
  - Simo Särkkä
  - Arno Solin
year: 2023
arxiv: 2111.01721
url: https://jmlr.org/papers/v24/21-1298.html
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/cs-ml
created: 2026-08-10
---

# Bayes–Newton Methods for Approximate Bayesian Inference with PSD Guarantees

> [!info] Citation
> Wilkinson, W. J., Särkkä, S., & Solin, A. (2023). Bayes–Newton Methods for Approximate Bayesian Inference with PSD Guarantees. *Journal of Machine Learning Research*, 24(83), 1-50. https://jmlr.org/papers/v24/21-1298.html

## TL;DR

Wilkinson, Särkkä, and Solin cast natural-gradient variational inference, expectation propagation, and posterior linearization as Bayesian analogues of Newton's method. Gauss-Newton and quasi-Newton approximations then yield update families whose Gaussian covariance estimates remain positive semidefinite (PSD).

## Problem & setting

Second-order approximate-inference updates can produce indefinite curvature or invalid covariance matrices, particularly with nonconjugate likelihoods. The paper studies Gaussian posterior approximations for models with a Gaussian prior and a nonconjugate likelihood and asks how numerical-optimization safeguards can transfer across VI, EP, and posterior linearization.

## Method

The authors express the inference schemes as Newton-like updates of Gaussian posterior parameters and import Gauss-Newton and quasi-Newton curvature approximations. The resulting Bayes-Newton view separates the target update from a curvature approximation selected to maintain PSD structure.

## Key results

The paper derives a family of PSD-guaranteed covariance updates and demonstrates them on sparse Gaussian processes and state-space models. The guarantees concern the constructed covariance updates under the stated Gaussian-prior/nonconjugate-likelihood setting. They do not imply global objective convergence, exact posterior recovery, or PSD preservation for arbitrary manifold or gauge-frame parameterizations.

## Relevance to this research

The paper is a useful numerical baseline wherever approximate [[Recognition Density|recognition-law]] updates must preserve covariance validity. It supports explicit PSD gates and damping comparisons but does not identify the gauge-frame optimizer with a Fisher or Gauss-Newton block. The exact finite ELBO remains the correctness oracle; a Bayes-Newton layer would be a typed approximation with value, stationarity, and PSD diagnostics.

## Cross-links

- Concepts: [[Natural gradient]], [[Fisher information metric]], [[Recognition Density]], [[Variational free energy]]
- Related sources: [[senoz-2021-local-constraint-vmp]], [[hasenclever-2017-snep-posterior-server]]

## BibTeX

```bibtex
@article{wilkinson2023bayesnewton,
  author  = {Wilkinson, William J. and Särkkä, Simo and Solin, Arno},
  title   = {Bayes--Newton Methods for Approximate Bayesian Inference with PSD Guarantees},
  journal = {Journal of Machine Learning Research},
  volume  = {24},
  number  = {83},
  pages   = {1--50},
  year    = {2023},
  url     = {https://jmlr.org/papers/v24/21-1298.html}
}
```
