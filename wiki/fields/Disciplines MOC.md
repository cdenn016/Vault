---
type: moc
title: Disciplines MOC
aliases: [Disciplines, Fields MOC, field MOC hub, Discipline index]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Disciplines MOC

> The **discipline facet** of the wiki. Every `sources/` note carries one or more `field/<discipline>`
> tags recording its academic discipline(s) of origin (field-of-origin listed first). This is
> orthogonal to the topic axis (`cluster/*`) and the project axis (`project/*`) — see the
> [[CLAUDE|LLM-Wiki Schema]]. Discipline is a **multi-valued tag**, not a folder, because ≈65% of sources are
> cross-disciplinary. The per-field tables below are live **Bases** views.

## The ten fields

| Field | MOC | Sources (touches) | Where it lives in the program |
|-------|-----|------------------:|-------------------------------|
| Physics | [[Physics MOC]] | 149 | sociophysics · quantum foundations & gravity · gauge theory |
| Mathematics | [[Mathematics MOC]] | 96 | SPD/Riemannian & gauge geometry · info geometry · kinetic/mean-field opinion math |
| CS / ML | [[CS-ML MOC]] | 80 | transformers/attention · NN optimization · network science |
| Sociology | [[Sociology MOC]] | 66 | opinion dynamics · networks · polarization |
| Philosophy | [[Philosophy MOC]] | 62 | philosophy of mind & science · structural realism · it-from-bit |
| Statistics | [[Statistics MOC]] | 60 | Bayesian inference · divergences · model selection |
| Biology | [[Biology MOC]] | 41 | evolutionary dynamics · cultural evolution · flocking |
| Psychology | [[Psychology MOC]] | 39 | conformity · social influence · cognitive bias |
| Neuroscience | [[Neuroscience MOC]] | 38 | predictive coding / active inference · consciousness |
| Economics | [[Economics MOC]] | 22 | game theory · cascades/herding · mean-field games |

> [!note] Counts are "any-field touches" (a source is counted under every field it carries), so the
> column sums to more than the 361 source notes — by design, since discipline is multi-valued. Numbers
> are a snapshot; the Bases tables on each MOC are the live source of truth.

## Composing facets

The power of the faceted scheme is the intersection of axes via tag search:

- `tag:#field/physics tag:#cluster/gauge-theory` — gauge theory of physics origin
- `tag:#field/mathematics tag:#cluster/social-physics/opinion-dynamics` — the applied-math kinetic models
- `tag:#field/philosophy tag:#cluster/participatory/philosophy-of-mind` — the consciousness-philosophy wing
- `tag:#field/statistics tag:#cluster/info-geometry` — the statistical core of information geometry

## See also
- [[CLAUDE|LLM-Wiki Schema]] — the `field/*`, `cluster/*`, `project/*` tag taxonomy
- Topic themes: [[Information geometry and natural gradient]] · [[Statistical physics of social systems and collective behavior]] · [[Participatory realism and quantum foundations]]
