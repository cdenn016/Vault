---
type: reference
title: "Effective Action for Composite Operators"
aliases:
  - "Cornwall, Jackiw, and Tomboulis 1974"
  - "CJT effective action"
  - "2PI effective action"
authors:
  - John M. Cornwall
  - Roman Jackiw
  - E. Tomboulis
year: 1974
url: https://doi.org/10.1103/PhysRevD.10.2428
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/methodology
  - project/multi-agent
  - field/physics
created: 2026-07-17
updated: 2026-07-17
---

# Effective Action for Composite Operators

> [!info] Citation
> John M. Cornwall, Roman Jackiw, and E. Tomboulis (1974). “Effective Action for Composite Operators.” *Physical Review D* **10**(8), 2428–2445. DOI: [10.1103/PhysRevD.10.2428](https://doi.org/10.1103/PhysRevD.10.2428).

## TL;DR

Cornwall, Jackiw, and Tomboulis construct an effective action whose independent variables include both a mean field and a two-point function. Stationarity produces coupled field and propagator equations, while truncating the two-particle-irreducible skeleton expansion yields systematic correlation corrections beyond a one-point or saddle description. The construction is a field-theoretic template for retaining connected fluctuations; it does not by itself turn an engineered belief-coupling energy into a state-level ELBO.

## What it establishes

The paper introduces sources coupled to elementary fields and bilocal composite operators, performs the corresponding Legendre transforms, and derives an effective action for the mean field and full propagator. The residual functional is organized by two-particle-irreducible vacuum graphs. This separates a saddle contribution, the fluctuation determinant, and higher connected corrections, giving a systematic approximation hierarchy when the underlying functional integral, measure, and expansion are well defined.

## Why the project cites it

The beyond-mean-field section of [[participatory-it-from-bit]] proposes a 2PI-style configuration theory for the structural gauge-VFE fields. The CJT construction supplies the standard prototype for promoting connected two-point structure to an independent variational object. In this program the analogy becomes a mathematical construction only after the configuration partition function exists, gauge redundancy is handled, and the chosen truncation has a declared operator basis and measurable residual. It connects [[Meta-entropy]] to the effective-action completion of the [[Renormalization-group flow of beliefs]].

## Full-text status

The [OSTI record](https://www.osti.gov/biblio/4236122), [INSPIRE record](https://inspirehep.net/literature/1295), and [CERN preprint record](https://cds.cern.ch/record/416634) were verified on 2026-07-17. OSTI and INSPIRE expose metadata but no downloadable document; CERN’s file service required an interactive proof-of-work challenge during acquisition. No unofficial mirror was used, so no local PDF was installed.

## BibTeX

```bibtex
@article{CornwallJackiwTomboulis1974,
  author  = {Cornwall, John M. and Jackiw, Roman and Tomboulis, E.},
  title   = {Effective Action for Composite Operators},
  journal = {Physical Review D},
  volume  = {10},
  number  = {8},
  pages   = {2428--2445},
  year    = {1974},
  doi     = {10.1103/PhysRevD.10.2428}
}
```
