---
type: paper
title: "Echo chambers online? Politically motivated selective exposure among Internet news users"
aliases: ["Garrett 2009", "Politically motivated selective exposure"]
authors: ["Garrett R. K."]
year: 2009
url: https://doi.org/10.1111/j.1083-6101.2009.01440.x
tags: [cluster/social-physics, project/social-physics, field/sociology, field/psychology, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Echo chambers online? Politically motivated selective exposure among Internet news users

> [!info] Citation
> Garrett, R. K. (2009). *Echo chambers online? Politically motivated selective exposure among Internet news users*. Journal of Computer-Mediated Communication 14(2):265-285. DOI: [10.1111/j.1083-6101.2009.01440.x](https://doi.org/10.1111/j.1083-6101.2009.01440.x).

## TL;DR
A behavior-tracking study of partisan online news readers that disentangles two halves of the selective-exposure hypothesis: the pull toward opinion-reinforcing information and the push away from opinion-challenging information. Garrett finds the two are asymmetric — readers are strongly drawn to reinforcing content (it markedly increases the likelihood and duration of viewing), but they only weakly avoid challenging content rather than actively shunning it. The result refines the echo-chamber account: chambers form mainly through approach to the agreeable, not avoidance of the disagreeable.

## What it establishes
Modeling exposure as a function of the match between content slant and reader opinion, the study estimates separate coefficients for reinforcement and challenge. Let $u_i(j)$ be reader $i$'s propensity to attend to item $j$ as a function of opinion congruence $c_{ij}$. The data show a steep positive response to congruent content, $\partial u/\partial c > 0$ and large, but only a shallow negative response to incongruent content — readers will still look at opposing views, sometimes to rebut them, so the avoidance term is small. Selective exposure is thus dominated by an approach bias toward the confirming rather than a strong avoidance of the disconfirming.

## Relevance to this research
This provides a microfoundation for the *shape* of the attention weights in the model. The program's softmax attention $\beta_{ij}$ encodes how strongly agent $i$ attends to neighbor $j$; Garrett's asymmetry argues that the confirmation-bias term should up-weight aligned signals far more than it down-weights dissonant ones, an asymmetric (not symmetric) modulation of the coupling. Honestly this is an adjacent-to-strong empirical mechanism rather than a result the functional already encodes: it constrains how a confirmation-bias variant of $\beta_{ij}$ ought to be parameterized if the model is to match observed selective-exposure behavior. It also distinguishes this entry from pure-avoidance accounts and from the affect-driven repulsion of backlash studies.

## Cross-links
- Concept: [[Belief perseverance and confirmation bias]]
- Related: [[Echo chambers and polarization]], [[Multi-agent variational free energy]], [[Opinion dynamics]]
- Related sources: [[del-vicario-2016-misinformation-online]], [[bakshy-2015-ideological-diversity-facebook]], [[bail-2018-exposure-opposing-views]]

## BibTeX
```bibtex
@article{garrett2009echo,
  author  = {Garrett, R. Kelly},
  title   = {Echo chambers online? Politically motivated selective exposure among Internet news users},
  journal = {Journal of Computer-Mediated Communication},
  volume  = {14},
  number  = {2},
  pages   = {265--285},
  year    = {2009},
  doi     = {10.1111/j.1083-6101.2009.01440.x}
}
```
