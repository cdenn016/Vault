---
type: paper
title: "Physics from Fisher Information: A Unification"
aliases:
  - "Frieden 1998"
  - "Frieden (1998) Physics from Fisher Information"
authors:
  - B. Roy Frieden
year: 1998
arxiv: null
url: https://doi.org/10.1017/CBO9780511622670
tags:
  - cluster/info-geometry
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/statistics
  - cluster/participatory/quantum-foundations
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Physics from Fisher Information: A Unification

> [!info] Citation
> B. Roy Frieden (1998). *Physics from Fisher Information: A Unification.* Cambridge University Press. ISBN: 9780521631679.

## TL;DR

Frieden's book advances the most ambitious version of the "physics from information" program: that the fundamental field equations of physics — the Schrödinger and Klein–Gordon equations, the Dirac equation, Maxwell's equations, the Einstein field equations, even thermodynamic and statistical laws — can be obtained as extremals of a Fisher-information functional. The unifying device is **Extreme Physical Information (EPI)**: a measurement is modeled as a transfer of [[Fisher information metric|Fisher information]] $I$ from a physical phenomenon to the observer, governed by a bound information $J$; physical law follows from extremizing $K = I - J$. The program makes the observer's act of measurement constitutive of the law that is found.

## Problem & setting

Conventional derivations posit Lagrangians and symmetries and read off equations of motion. Frieden inverts this: he asks whether a single information-theoretic variational principle, anchored in the Fisher information of the measured quantity, can *generate* the Lagrangians themselves. The setting is a measurement scenario — an observer estimating a parameter from data — so the resulting "physics" is inseparable from the epistemic situation of measuring.

## Method

EPI posits two informations: the Fisher information $I$ in the data and a "bound" information $J$ intrinsic to the phenomenon (fixed by an invariance principle appropriate to each domain). The physical law is the extremum of the *physical information* $K = I - J$, together with a zero condition $I - \kappa J = 0$. Choosing the invariance that fixes $J$ (Lorentz invariance, gauge invariance, unitarity, etc.) selects the domain, and the EPI extremization then yields the corresponding field equation. The Fisher term plays the role the quantum/Bohm potential plays in single-equation derivations such as [[reginatto-1998-fisher-quantum]], but EPI claims it as a universal organizing quantity rather than a special-case trick.

## Key results

1. A common Fisher-information variational template (EPI) reproduces a wide range of fundamental equations across quantum mechanics, electromagnetism, gravitation, and statistical physics.
2. Measurement is built into the foundations: the observer's information acquisition is the mechanism that fixes the law.
3. Fisher information, not entropy, is positioned as the master quantity of physical law — a metric-side (distinguishability) counterpart to entropy-side MaxEnt programs.

## Relevance to this research

Frieden is the maximal backdrop against which [[participatory-it-from-bit]]'s Level-3 claim must position itself. PIFB argues that an agent's physics emerges from the information geometry of its beliefs; Frieden argues that *all* of physics emerges from Fisher information transferred in measurement. The manuscript should adopt what is defensible (Fisher information as the metric that costs belief change — the [[Mass as Fisher information]] identification) while explicitly distancing itself from EPI's contested universality and the criticisms its derivations have drawn. Reading EPI as a strong, controversial precursor lets PIFB stake out a more modest and better-grounded position: not "all field equations come from Fisher information," but "belief dynamics inherit an inertial/metric structure from Fisher information," consistent with the narrower, rigorously demonstrated result of [[reginatto-1998-fisher-quantum]] and the entropic lineage of [[caticha-2019-entropic-dynamics]]. The participatory, measurement-centric framing of EPI also resonates with the [[Participatory realism (it from bit)]] thread and [[wheeler-1990-it-from-bit]], giving PIFB a clear ancestor for "observer-constitutive law."

## Cross-links

- Concept: [[Fisher information metric]], [[Mass as Fisher information]].
- Theme: [[Physics from Fisher information]], [[Participatory realism (it from bit)]].
- Sources: [[reginatto-1998-fisher-quantum]], [[caticha-2019-entropic-dynamics]], [[wheeler-1990-it-from-bit]].
- Manuscript: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@book{frieden1998physics,
  author    = {Frieden, B. Roy},
  title     = {Physics from Fisher Information: A Unification},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {1998},
  isbn      = {9780521631679},
  doi       = {10.1017/CBO9780511622670}
}
```
