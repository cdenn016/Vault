---
type: paper
title: "Have Americans' Social Attitudes Become More Polarized?"
aliases: ["DiMaggio, Evans & Bryson 1996", "Have Americans' Attitudes Become More Polarized?"]
authors: ["DiMaggio P.", "Evans J.", "Bryson B."]
year: 1996
url: https://doi.org/10.1086/230995
tags: [cluster/social-physics, project/social-physics, field/sociology, field/statistics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Have Americans' Social Attitudes Become More Polarized?

> [!info] Citation
> DiMaggio, P., Evans, J., & Bryson, B. (1996). *Have Americans' Social Attitudes Become More Polarized?* American Journal of Sociology 102(3):690-755. DOI: [10.1086/230995](https://doi.org/10.1086/230995).

## TL;DR
A foundational measurement paper that disentangles what "polarization" means by decomposing it into four distinct, separately measurable statistical properties of an attitude distribution, then tests each against two decades of General Social Survey and National Election Studies data. The finding is largely deflationary: aggregate American social attitudes had not generally polarized over 1972-1994, with the notable exceptions of abortion and a growing divergence by party identification.

## What it establishes
Polarization is operationalized as four orthogonal moments of a population's opinion distribution: (i) **dispersion**, the variance $\operatorname{Var}(x)$ — how spread out opinions are; (ii) **bimodality**, captured by (negative) kurtosis — whether mass piles at the extremes leaving the middle empty; (iii) **constraint**, the cross-issue correlation — how tightly an individual's positions cohere into an ideology; and (iv) **between-group difference**, the gap in group means such as $|\bar{x}_{\text{Dem}}-\bar{x}_{\text{Rep}}|$. The paper insists these can move independently — a distribution can grow more bimodal without higher variance, or groups can separate without overall spread changing — so any claim of "rising polarization" must specify which moment.

## Relevance to this research
This supplies the rigorous statistical definitions a belief-distribution model must report, and they are precisely the moments of the population of Gaussian beliefs $q_i$ that the VFE flow evolves: dispersion is the variance of the means $\{\mu_i\}$, bimodality is their kurtosis, constraint is the off-diagonal structure of the joint belief covariance, and between-group difference is the separation of cluster centroids (the program's emergent meta-agent means). It is the methodological backbone for honestly measuring the program's polarization predictions and for avoiding the overclaiming this paper itself warns against — reporting which moment a simulation actually moves. Strong: it sets the measurement contract the model's outputs must meet.

## Cross-links
- Concept: [[Echo chambers and polarization]]
- Related: [[Opinion dynamics]], [[Multi-agent variational free energy]], [[Sociophysics]]
- Related sources: [[baldassarri-bearman-2007-political-polarization]], [[iyengar-2019-affective-polarization]], [[sunstein-2002-law-of-group-polarization]]

## BibTeX
```bibtex
@article{dimaggio1996polarized,
  author  = {DiMaggio, Paul and Evans, John and Bryson, Bethany},
  title   = {Have Americans' Social Attitudes Become More Polarized?},
  journal = {American Journal of Sociology},
  volume  = {102},
  number  = {3},
  pages   = {690--755},
  year    = {1996},
  doi     = {10.1086/230995}
}
```
