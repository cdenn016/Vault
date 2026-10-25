---
type: paper
title: "On the Global and Componentwise Rates of Convergence of the EM Algorithm"
aliases:
  - "Meng and Rubin 1994"
  - "EM convergence rates"
authors:
  - "Meng, Xiao-Li"
  - "Rubin, Donald B."
year: 1994
url: https://doi.org/10.1016/0024-3795(94)90363-8
tags:
  - cluster/vfe
  - project/transformer
  - field/statistics
  - field/mathematics
created: 2026-10-25
---

# On the Global and Componentwise Rates of Convergence of the EM Algorithm

> [!info] Citation
> Meng, X.-L., & Rubin, D. B. (1994). *On the global and componentwise rates of convergence of the EM algorithm*. Linear Algebra and its Applications, 199, 413–425.

## TL;DR
Near a fixed point EM is a linear iteration whose rate matrix is the fraction of missing information, $DM=I_{\rm mis}I_{\rm com}^{-1}$. The paper relates the global rate (the largest eigenvalue of this matrix) to the componentwise rates of individual parameters.

## Method
The analysis is local: it describes the asymptotic linear convergence of EM near a solution and explains why EM is slow along directions the observed data inform poorly.

> [!note] Editorial: No local PDF; the publisher's open-archive copy could not be fetched non-interactively. The summary follows the title, the published record and secondary citations, and the DOI has not been checked against the publisher page.

## Relevance to this research
Cited in [[vfe3-2026-10-25-local-learner-test]] for the slow descent of the local arm: directions with a high fraction of missing information, here including the latent frame, which the observed bytes do not identify, converge slowly under EM.

## Cross-links
- Themes: [[Inference machinery — variational EM and filtering]]
- Methods: [[Variational EM]]
- Related sources: [[dempster-1977-em-algorithm]], [[liu-1998-px-em]], [[vfe3-2026-10-25-local-learner-test]]

## BibTeX
```bibtex
@article{meng1994global,
  author  = {Meng, Xiao-Li and Rubin, Donald B.},
  title   = {On the Global and Componentwise Rates of Convergence of the {EM} Algorithm},
  journal = {Linear Algebra and its Applications},
  volume  = {199},
  pages   = {413--425},
  year    = {1994},
  doi     = {10.1016/0024-3795(94)90363-8}
}
```
