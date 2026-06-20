---
type: reference
title: "Perseverance of Social Theories"
aliases:
  - "Anderson Lepper Ross 1980"
  - "Anderson 1980"
  - "Perseverance of Social Theories"
authors:
  - Craig A. Anderson
  - Mark R. Lepper
  - Lee Ross
year: 1980
tags:
  - cluster/social-physics
  - project/social-physics
  - field/psychology
  - cluster/social-physics/social-influence
created: 2026-06-19
updated: 2026-06-19
---

# Perseverance of Social Theories

> [!info] Citation
> Anderson, C. A., Lepper, M. R., & Ross, L. (1980). "Perseverance of Social Theories: The Role of Explanation in the Persistence of Discredited Information." *Journal of Personality and Social Psychology* **39**(6), 1037–1049. DOI: [10.1037/h0077720](https://doi.org/10.1037/h0077720).

## TL;DR

A landmark experimental demonstration of **belief perseverance**: once people form a causal theory about a social relationship, that theory survives the complete discrediting of the very evidence that gave rise to it. Subjects shown (fabricated) case data linking, for example, risk-taking to firefighting success, and then asked to explain *why* such a relationship might hold, continued to endorse the theory at near-undiminished strength even after being told the original data were fictitious. The act of constructing an explanation, rather than the evidence itself, is what makes the belief stick.

## What it establishes

Working within the *debriefing paradigm*, Anderson, Lepper, and Ross presented subjects with concrete or abstract data suggesting a positive or negative correlation between two attributes, induced them to generate a causal explanation or narrative scenario for the observed relationship, and then administered a thorough *discrediting debriefing* revealing that the data were manufactured and uninformative. The central finding is that beliefs persevered: post-debriefing estimates of the underlying relationship remained substantially displaced toward the initially suggested direction, well away from the no-information baseline a normatively updating agent would return to once the evidence was withdrawn.

The mechanism the paper isolates is **explanation-based**. The cognitive work of constructing a causal account creates a self-supporting structure that outlives its evidential origin: the theory, once explained, recruits independent justification and is no longer tethered to the data that prompted it. Subjects who explained the relationship showed markedly stronger perseverance than those who did not, and the effect held for theories built on abstract statistical summaries as well as concrete cases. The result situates belief perseverance alongside the broader family of motivated and structural reasoning biases — biased assimilation, the primacy of first impressions, and the resistance of social judgments to disconfirmation — that together describe a belief system far stickier than any Bayesian-updating account would predict.

> [!note] Editorial: This note summarizes the explanation-based perseverance effect and the debriefing paradigm; the precise experimental conditions, effect sizes, and the abstract-versus-concrete data manipulation should be read in the original article.

## Why the project cites it

For the **SocialPhysics** program and its founding manuscript [[belief-inertia]], this paper supplies the empirical anchor for the claim that belief is *inertial* — that updating is not the frictionless, memoryless overwriting assumed by first-order opinion-dynamics models, but a process that resists displacement and retains momentum from its history. The manuscript reframes belief perseverance not as an isolated cognitive quirk but as a geometric consequence of [[Belief inertia]]: when the Fisher/precision tensor is read as an inertial [[Mass as Fisher information|mass]], a belief held with high precision (or one whose holder has invested in explaining it) has large effective mass and is correspondingly hard to move, so the trajectory back toward the no-information state is slow and incomplete. The Anderson–Lepper–Ross finding that *explanation* drives perseverance maps naturally onto this picture: constructing a causal account sharpens the precision of the belief, raising its mass, and thereby its resistance to subsequent evidence — even discrediting evidence.

This is the perseverance half of the manuscript's [[Belief perseverance and confirmation bias]] thread, the companion to the confirmation-bias literature ([[nickerson-1998-confirmation-bias]]). Where confirmation bias describes a *selective intake* of evidence, belief perseverance describes a *retention against withdrawn evidence*; together they characterize the asymmetry that [[Hamiltonian belief dynamics]] predicts when beliefs carry momentum rather than relaxing instantaneously. In the overdamped (gradient-flow) limit the system would return to baseline once evidence is removed, recovering the classical [[Opinion dynamics]] and [[Sociophysics]] models; it is precisely the underdamped, inertial regime — the manuscript's novel contribution — that produces overshoot, hysteresis, and the failure to relax that this experiment documents.

The paper therefore serves [[SocialPhysics]] as a falsifiable behavioral target: a real, replicated phenomenon that a memoryless averaging model (DeGroot, [[Bounded confidence]] Hegselmann–Krause / Deffuant) cannot reproduce, but that the inertial / Hamiltonian extension of [[Multi-agent variational free energy]] predicts as a structural consequence of treating the [[Fisher information metric]] as belief mass. It thus motivates moving beyond the overdamped limit shared with the [[Gauge-Theoretic Multi-Agent VFE Model]] toward the second-order dynamics the manuscript proposes.

## BibTeX

```bibtex
@article{anderson1980perseverance,
  author  = {Anderson, Craig A. and Lepper, Mark R. and Ross, Lee},
  title   = {Perseverance of Social Theories: The Role of Explanation in the Persistence of Discredited Information},
  journal = {Journal of Personality and Social Psychology},
  year    = {1980},
  volume  = {39},
  number  = {6},
  pages   = {1037--1049},
  doi     = {10.1037/h0077720}
}
```
