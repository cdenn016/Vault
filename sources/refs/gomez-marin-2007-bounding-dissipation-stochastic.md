---
type: reference
title: "Bounding dissipation in stochastic models"
aliases: ["gomezmarin2007bounding"]
authors: ["Alex Gomez-Marin", "J. M. R. Parrondo", "C. Van den Broeck"]
year: 2007
arxiv: "0710.4290"
url: "https://arxiv.org/abs/0710.4290"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/physics]
created: 2026-11-10
updated: 2026-11-10
---
# Bounding dissipation in stochastic models

> [!info] Citation
> Gomez-Marin, A., Parrondo, J. M. R., Van den Broeck, C. (2007). *Bounding dissipation in stochastic models*. arXiv:0710.4290. [arXiv](https://arxiv.org/abs/0710.4290)

[Local PDF](../pdfs/gomez-marin-2007-bounding-dissipation-stochastic.pdf), 25 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and manuscript reading record.

## TL;DR

The paper extends an exact expression for the average dissipated work in driven systems from Hamiltonian dynamics to stochastic dynamics, writes it as a relative entropy between forward and backward path probabilities, and derives lower bounds on dissipation from coarse-grained, partial information.

## Problem & setting

The introduction recalls that for a system driven from equilibrium by a control parameter, the mean dissipated work equals the thermal energy scale times the relative entropy between the forward phase-space density and the time-reversed one, but that this needs full information on all microscopic degrees of freedom. The aim is to cover situations where only a limited number of degrees of freedom are relevant or available, as in master-equation and Langevin descriptions.

## Method

For stochastic dynamics the result is rewritten as an integral over paths, giving a relative entropy between the path probability and the time-reversed path probability. When only partial information about the path is used, the relative entropy decreases, so the equality becomes a lower bound. The bounds are illustrated on over- and underdamped Brownian particles.

## Key results

The paper states the exact path-space expression and a family of lower bounds from different coarse-graining procedures; the examples are analytically solvable models.

## Relevance to this research

The manuscript cites this paper, together with two others, for the relation between dissipation and a relative entropy of path laws, in its discussion of energetics under coarse-graining. The reading record notes that the setting is driven between equilibrium states, not stationary, and that a relative entropy computed from partial information is a lower bound. The journal reference was not verified, so the entry is an arXiv record. See [[Stochastic Thermodynamics]], [[Coarse Graining]] and [[Data processing inequality]].

## Cross-links

[[Collective agents literature map]]; [[Stochastic Thermodynamics]]; [[Coarse Graining]]; [[Data processing inequality]].

## BibTeX

```bibtex
@misc{gomezmarin2007bounding,
  author  = {Gomez-Marin, Alex and Parrondo, J. M. R. and Van den Broeck, C.},
  title   = {Bounding dissipation in stochastic models},
  year    = {2007},
  eprint  = {0710.4290},
  archiveprefix = {arXiv},
  primaryclass = {cond-mat.stat-mech},
  note    = {arXiv:0710.4290}
}
```
