---
type: paper
title: "Simple and Globally Convergent Methods for Accelerating the Convergence of Any EM Algorithm"
aliases:
  - "Varadhan and Roland 2008"
  - "SQUAREM"
  - "Squared extrapolation EM"
authors:
  - "Varadhan, Ravi"
  - "Roland, Christophe"
year: 2008
url: https://doi.org/10.1111/j.1467-9469.2007.00585.x
tags:
  - cluster/vfe
  - project/transformer
  - field/statistics
created: 2026-10-25
---

# Simple and Globally Convergent Methods for Accelerating the Convergence of Any EM Algorithm

> [!info] Citation
> Varadhan, R., & Roland, C. (2008). *Simple and globally convergent methods for accelerating the convergence of any EM algorithm*. Scandinavian Journal of Statistics, 35(2), 335–353. doi:10.1111/j.1467-9469.2007.00585.x.

## TL;DR
SQUAREM accelerates any EM map by squared extrapolation: two EM steps define a first and a second difference, and a steplength built from them extrapolates along the EM trajectory. Treating the scheme as a continuation of EM, with a fallback to the plain step, makes it globally convergent while needing only the EM map itself.

## Method
The method needs no derivatives or information matrices, only evaluations of the EM update, so it applies to learners that have an M-step but no gradient. It is implemented in the R package SQUAREM.

> [!note] Editorial: No legal free copy was found (publisher paywall); there is no local PDF, and this note summarizes the abstract and the published record. Equation-level claims should be checked against the article.

## Relevance to this research
Cited in [[vfe3-2026-10-25-local-learner-test]] as an untested extrapolation candidate for stepwise EM. Applying it in the stochastic stepwise setting needs care, since successive EM maps there use different minibatches.

## Cross-links
- Themes: [[Inference machinery — variational EM and filtering]]
- Methods: [[Variational EM]]
- Related sources: [[salakhutdinov-2003-overrelaxed-bound-optimization]], [[liu-1998-px-em]], [[dempster-1977-em-algorithm]], [[vfe3-2026-10-25-local-learner-test]]

## BibTeX
```bibtex
@article{varadhan2008simple,
  author  = {Varadhan, Ravi and Roland, Christophe},
  title   = {Simple and Globally Convergent Methods for Accelerating the Convergence of Any {EM} Algorithm},
  journal = {Scandinavian Journal of Statistics},
  volume  = {35},
  number  = {2},
  pages   = {335--353},
  year    = {2008},
  doi     = {10.1111/j.1467-9469.2007.00585.x}
}
```
