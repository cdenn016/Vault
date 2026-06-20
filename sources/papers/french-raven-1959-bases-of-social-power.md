---
type: reference
title: "The Bases of Social Power"
aliases: ["French & Raven 1959", "Bases of social power"]
authors: ["French J. R. P.", "Raven B."]
year: 1959
tags: [cluster/social-physics, project/social-physics, field/psychology, field/sociology, cluster/social-physics/social-influence]
created: 2026-06-19
updated: 2026-06-19
---

# The Bases of Social Power

> [!info] Citation
> John R. P. French Jr. and Bertram Raven (1959). *The bases of social power*. In D. Cartwright (Ed.), *Studies in Social Power* (pp. 150–167). Institute for Social Research, University of Michigan, Ann Arbor.

## TL;DR
French and Raven propose that social power — one agent's capacity to influence another — is not a single quantity but comes in qualitatively distinct kinds depending on its source. They identify five bases: reward power (control over rewards), coercive power (control over punishments), legitimate power (a recognized right to prescribe behavior), referent power (influence rooted in identification with or attraction to the influencer), and expert power (influence rooted in attributed superior knowledge). The chapter argues that these bases differ in the kind of change they produce and in how dependent that change is on continued surveillance.

## What it establishes
The taxonomy ties the *amount* of influence to its *origin* and predicts different dynamics for each base. Reward and coercive power tend to produce surveillance-dependent compliance that decays when monitoring stops; legitimate, referent, and expert power tend to produce more internalized, durable change. Referent and expert power, in particular, are highlighted as sources of influence that operate without explicit incentives — identification and credibility make the target weight the influencer's position heavily on its own terms. The qualitative point is that influence weight is heterogeneous and asymmetric: who influences whom, and how durably, depends on the relational basis of the tie.

## Relevance to this research
This refines the influence-weight construct underlying $\beta_{ij}$: not all coupling is equal in origin, and the bare softmax-of-divergence attention treats all neighbours symmetrically up to belief distance. Expert and referent power suggest that the coupling weights should in general be heterogeneous and possibly asymmetric ($\beta_{ij} \neq \beta_{ji}$) — an expert agent exerts more pull than it receives — which is useful for interpreting what the attention weights are meant to represent and for motivating extensions where coupling carries source-dependent gain. It is adjacent-to-strong context: it informs the *interpretation* and possible generalization of the coupling weights rather than supplying machinery the current functional uses. See [[Social influence and conformity]], [[Opinion dynamics]], and [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Social influence and conformity]]
- Related sources: [[french-1956-formal-theory-social-power]], [[cialdini-2007-influence-psychology-persuasion]], [[deutsch-gerard-1955-normative-informational-influence]]

## BibTeX
```bibtex
@incollection{french1959bases,
  author    = {French, John R. P. and Raven, Bertram},
  title     = {The Bases of Social Power},
  booktitle = {Studies in Social Power},
  editor    = {Cartwright, Dorwin},
  publisher = {Institute for Social Research, University of Michigan},
  address   = {Ann Arbor, MI},
  year      = {1959},
  pages     = {150--167}
}
```
