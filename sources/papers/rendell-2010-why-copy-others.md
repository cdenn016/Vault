---
type: paper
title: "Why Copy Others? Insights from the Social Learning Strategies Tournament"
aliases: ["Rendell et al. 2010", "Social Learning Strategies Tournament"]
authors: ["Rendell L.", "Boyd R.", "Cownden D.", "Enquist M.", "Eriksson K.", "Feldman M. W.", "Fogarty R.", "Ghirlanda S.", "Lillicrap T.", "Laland K. N."]
year: 2010
url: https://doi.org/10.1126/science.1184719
tags: [cluster/social-physics, project/social-physics, field/biology, field/psychology, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# Why Copy Others? Insights from the Social Learning Strategies Tournament

> [!info] Citation
> Rendell, L., Boyd, R., Cownden, D., Enquist, M., Eriksson, K., Feldman, M. W., Fogarty, R., Ghirlanda, S., Lillicrap, T., & Laland, K. N. (2010). "Why copy others? Insights from the social learning strategies tournament." *Science* **328**(5975), 208–213. DOI: [10.1126/science.1184719](https://doi.org/10.1126/science.1184719).

## TL;DR
An open computer tournament, modeled on Axelrod's prisoner's-dilemma contests, in which submitted strategies competed in a multi-armed-bandit-like environment to accumulate payoff while choosing each round among INNOVATE (asocial trial-and-error), OBSERVE (social learning by copying another agent's most recent action), and EXPLOIT (perform a known behavior). The striking and counterintuitive result was that the most successful strategies relied overwhelmingly on social learning, copying far more than they innovated, contradicting the prior theoretical expectation that heavy reliance on social information should be vulnerable to copying outdated or erroneous behavior.

## What it establishes
The winning entry, *discountmachine*, copied almost exclusively and innovated rarely, succeeding by weighting observed payoffs with a recency discount and acting on the best available social information. The authors' analysis explains why indiscriminate copying did not fail as theory predicted: because agents preferentially EXPLOIT their own highest-payoff behavior, what a copier observes is automatically filtered toward high-value actions — social learning inherits the adaptive filtering already performed by demonstrators, so copied information is, on average, better than random sampling would suggest. The tournament also showed that *how* one copies (integrating payoff estimates with appropriate temporal discounting to track a changing environment) matters more than *how much* one copies, and that copying remained advantageous even when social information was costly, error-prone, or stale.

## Relevance to this research
The tournament directly addresses when and from whom an agent should copy — i.e., how attention and coupling weights ought to be allocated in a population of belief-updaters. The "copy-the-best, discount-the-stale" winning policy is an empirical target for what the softmax attention $\beta_{ij}$ and precision-weighted coupling in the VFE model ought to recover: weight neighbors by the quality (payoff/precision) of their information and down-weight stale or low-value sources. The result that copying succeeds because demonstrators pre-filter toward high-payoff actions is the population-level reason a coupling term that pulls $q_i$ toward transported neighbor beliefs is adaptive rather than merely conformist. Strong, evidence-level relevance to the design of the coupling kernel, though the tournament is payoff-based and discrete whereas the VFE coupling is divergence-based over Gaussian beliefs. See [[Cultural evolution and social learning]].

Concept links: [[Cultural evolution and social learning]], [[Multi-agent variational free energy]], [[Social influence and conformity]], [[Collective active inference]].

## Cross-links
- Concept: [[Cultural evolution and social learning]]
- Related sources: [[laland-2004-social-learning-strategies]], [[rendell-2011-cognitive-culture]], [[henrich-gilwhite-2001-evolution-of-prestige]]

## BibTeX
```bibtex
@article{rendell2010why,
  author  = {Rendell, L. and Boyd, R. and Cownden, D. and Enquist, M. and Eriksson, K. and Feldman, M. W. and Fogarty, R. and Ghirlanda, S. and Lillicrap, T. and Laland, K. N.},
  title   = {Why copy others? Insights from the social learning strategies tournament},
  journal = {Science},
  volume  = {328},
  number  = {5975},
  pages   = {208--213},
  year    = {2010},
  doi     = {10.1126/science.1184719}
}
```
