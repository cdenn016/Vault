---
type: paper
title: "A Formal Theory of Social Power"
aliases: ["French 1956", "French formal theory of social power"]
authors: ["French J. R. P."]
year: 1956
url: https://doi.org/10.1037/h0046123
tags: [cluster/social-physics, project/social-physics, field/psychology, field/sociology, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# A Formal Theory of Social Power

> [!info] Citation
> John R. P. French Jr. (1956). *A formal theory of social power*. Psychological Review, 63(3), 181–194. DOI: 10.1037/h0046123.

## TL;DR
French gives one of the first explicitly mathematical treatments of opinion change in a group, modeling the group as a directed graph of interpersonal influence relations and asking what happens to members' opinions under repeated rounds of influence. Each member's opinion is a point on a continuum, and on each step a member moves toward the opinions of those who exert influence on them. French proves that, under connectedness conditions on the influence network, this iterated averaging drives opinions to converge to a common value — a power-weighted average of the initial opinions — making him the formal antecedent of the DeGroot consensus rule.

## What it establishes
The model represents the influence structure as a matrix and updates the opinion vector by repeated multiplication, so that opinions at round $t$ are
$$\mathbf{x}^{(t+1)} = W\,\mathbf{x}^{(t)},$$
with $W$ a row-stochastic influence (power) matrix whose entry $w_{ij}$ measures how much member $j$ influences member $i$. French establishes that when the influence digraph is appropriately connected, $W^t$ converges and all opinions reach consensus; the limiting consensus value is the stationary-distribution-weighted average of the initial positions, with each member's contribution proportional to their network power. The framework links a structural property (who influences whom) to a dynamical outcome (whether and where the group converges).

## Relevance to this research
This is the direct precursor to DeGroot averaging and therefore to the overdamped, first-order limit the belief-inertia VFE functional claims to recover. French's power matrix $W$ is essentially the row-stochastic influence operator; in the VFE program the softmax attention weights $\beta_{ij}$ play the same role as French's per-edge influence weights, so the gradient-flow consensus dynamics reduce, in the appropriate linear-Gaussian limit, to iterated multiplication by a $\beta$-weighted stochastic operator. This makes French core lineage for claim (1): the recovery of classical consensus dynamics. The note of caution is that French's $W$ is fixed and exogenous, whereas VFE attention $\beta_{ij} = \mathrm{softmax}(-\mathrm{KL}/\tau)$ is belief-dependent and updates with the state, so the correspondence is exact only in the frozen-coupling limit. See [[Social influence and conformity]], [[Opinion dynamics]], and [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Social influence and conformity]]
- Related sources: [[french-raven-1959-bases-of-social-power]], [[festinger-1954-social-comparison-processes]], [[deutsch-gerard-1955-normative-informational-influence]]

## BibTeX
```bibtex
@article{french1956formal,
  author  = {French, John R. P.},
  title   = {A Formal Theory of Social Power},
  journal = {Psychological Review},
  year    = {1956},
  volume  = {63},
  number  = {3},
  pages   = {181--194},
  doi     = {10.1037/h0046123}
}
```
