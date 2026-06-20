---
type: reference
title: "The Psychology of Social Norms"
aliases: ["Sherif 1936", "Autokinetic norm formation"]
authors: ["Sherif M."]
year: 1936
tags: [cluster/social-physics, project/social-physics, field/psychology, field/sociology, cluster/social-physics/social-influence]
created: 2026-06-19
updated: 2026-06-19
---

# The Psychology of Social Norms

> [!info] Citation
> Muzafer Sherif (1936). *The Psychology of Social Norms*. Harper & Brothers, New York.

## TL;DR
Sherif's monograph reports the autokinetic experiments, the earliest controlled demonstration of consensus emergence from interacting individual estimates. A stationary point of light in a dark room appears to drift (the autokinetic illusion); because there is no external frame of reference, an observer's perceived movement is genuinely ambiguous. Sherif shows that individuals tested alone develop idiosyncratic personal ranges of estimates, but when tested together their estimates converge over repeated trials onto a shared group norm — and this norm then persists, carrying over to later solitary sessions and even being transmitted to newcomers. The book argues that social norms are emergent frames of reference that arise spontaneously under ambiguity and become self-sustaining.

## What it establishes
The key result is bottom-up norm formation: initially heterogeneous estimates $\{x_i\}$ contract toward a common value once the individuals can observe one another, and the resulting consensus is internalized rather than merely a compliant public report (it survives removal of the group). The convergence is strongest precisely when the stimulus is most ambiguous, because there is no competing perceptual anchor; the social signal supplies the missing reference frame. This is the complement to Asch's later work: Sherif uses genuinely ambiguous stimuli (where convergence is informational and durable), whereas Asch uses unambiguous stimuli (where conformity is normative and largely public).

## Relevance to this research
This is the earliest experimental demonstration of spontaneous norm/consensus emergence from interacting estimates — exactly the convergence the overdamped VFE flow produces from initial belief heterogeneity. Sherif's ambiguous stimulus corresponds to high observation variance, i.e. a weak observation-likelihood term, the regime in which the social-coupling gradient $\beta_{ij}\,\mathrm{KL}(q_i \,\|\, \Omega_{ij} q_j)$ dominates and beliefs collapse to a common $\mu$. The durability of the internalized norm (it persists when the group is removed) is the empirical signature of consensus becoming a stable fixed point of the dynamics rather than a transient compromise, which the VFE flow predicts once coupling has driven beliefs into a shared basin. See [[Social influence and conformity]], [[Opinion dynamics]], and [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Social influence and conformity]]
- Related sources: [[asch-1955-opinions-and-social-pressure]], [[festinger-1954-social-comparison-processes]], [[deutsch-gerard-1955-normative-informational-influence]]

## BibTeX
```bibtex
@book{sherif1936psychology,
  author    = {Sherif, Muzafer},
  title     = {The Psychology of Social Norms},
  publisher = {Harper \& Brothers},
  address   = {New York},
  year      = {1936}
}
```
