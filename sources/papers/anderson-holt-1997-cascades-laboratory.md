---
type: paper
title: "Information Cascades in the Laboratory"
aliases: ["Anderson & Holt 1997", "Information cascades in the laboratory"]
authors: ["Anderson L. R.", "Holt C. A."]
year: 1997
tags: [cluster/social-physics, project/social-physics, field/economics, field/psychology, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Information Cascades in the Laboratory

> [!info] Citation
> Anderson, L. R., & Holt, C. A. (1997). *Information Cascades in the Laboratory*. American Economic Review, 87(5), 847-862.

## TL;DR
Anderson and Holt provide the first clean experimental test of informational-cascade theory and find that human subjects do, broadly, behave as the Bayesian model predicts. In their design, subjects draw private signals about an unknown state and decide in sequence, observing predecessors' announced decisions (but not their private draws), with monetary payoffs for correct guesses. They observe cascades forming exactly when the theory says they should: after a short run of agreeing decisions, later subjects rationally override their own private signal and follow the public history. The experiment captures both **correct cascades** (the herd lands on the right answer) and, instructively, **incorrect cascades** in which an early misleading run of signals locks the group onto the wrong state. Aggregate behavior matched the Bayesian prediction in 41 of 56 cases where the theory made a sharp prediction, establishing that rational herding is not just a theoretical artifact but a robust feature of real decision-making.

## What it establishes
The study operationalizes the Bayesian sequential-decision model in a controlled lab: with binary states and signals of known precision, theory predicts a cascade begins once the public count of one decision leads by enough that no single private signal can flip the posterior. Subjects largely follow this **Bayesian updating rule**, deferring to the public history when it is decisive and to their own signal otherwise; deviations occur but are the minority. The empirical demonstration of **incorrect cascades** is especially important — it confirms the theory's most distinctive and uncomfortable prediction, that rational imitation can systematically propagate error. The paper thereby supplies the behavioral validation that grounds the entire cascade literature, showing the mechanism is descriptively real and that its inefficiency is observable in human choice.

## Relevance to this research
This is the empirical anchor showing cascade theory is behaviorally real, and it is honestly *adjacent* to the program — valuable as a data target rather than as machinery the VFE functional uses. It provides the kind of human-behavioral benchmark a sociophysics model of belief coupling should ultimately aim to reproduce: if the program claims to recover herding as a limiting regime of softmax-weighted $\mathrm{KL}(q_i\|\Omega_{ij}[q_j])$ coupling, then the rates of correct versus incorrect cascades observed here (and their dependence on signal precision) are the empirical curves a calibrated belief-coupling model would be measured against. The relevance is grounding and validation, not mechanism: Anderson and Holt do not supply any equation the functional adopts; they supply the experimental phenomenon the functional should, in an appropriate regime, predict.

See [[Information cascades and herding]], [[Multi-agent variational free energy]], [[Opinion dynamics]], [[Sociophysics]].

## Cross-links
- Concept: [[Information cascades and herding]]
- Related sources: [[bikhchandani-hirshleifer-welch-1992-informational-cascades]], [[banerjee-1992-herd-behavior]], [[bikhchandani-hirshleifer-welch-1998-learning-from-others]]

## BibTeX
```bibtex
@article{anderson1997laboratory,
  author  = {Anderson, Lisa R. and Holt, Charles A.},
  title   = {Information Cascades in the Laboratory},
  journal = {American Economic Review},
  year    = {1997},
  volume  = {87},
  number  = {5},
  pages   = {847--862}
}
```
