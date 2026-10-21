---
type: paper
title: "Initial conditions for models of dynamical systems"
aliases:
  - "Cox and Roberts 1995"
  - "isochron projection of initial conditions"
authors:
  - Cox S.M.
  - Roberts A.J.
year: 1995
arxiv: "chao-dyn/9411021"
doi: "10.1016/0167-2789(94)00201-Z"
url: "https://arxiv.org/abs/chao-dyn/9411021"
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
  - field/physics
created: 2026-09-28
updated: 2026-09-28
---

# Initial conditions for models of dynamical systems

> [!info] Citation
> Stephen M. Cox and A. J. Roberts (1995). "Initial conditions for models of dynamical systems."
> *Physica D* **85**(1–2), 126–141. DOI 10.1016/0167-2789(94)00201-Z. Preprint arXiv:chao-dyn/9411021.

## Verification record

Metadata verified on 2026-09-28 against the arXiv record chao-dyn/9411021 and the Crossref
record for the Physica D DOI (volume 85, issue 1–2, pages 126–141, 1995). Full text read from the
arXiv PDF. Gathered by Claude Opus 5.5, verified by Claude Fable 5.1.

## Verified content

Section 2 states property CM2 with Eq. (4): to each solution $P(t)$ of the full system there is a
solution $Q(t)$ on the centre manifold with $|P(t)-Q(t)|=O(e^{-\beta t})$ as $t\to\infty$. The
introduction says centre-manifold theory guarantees the existence of $Q(t)$ but gives no general
constructive means of determining $Q(0)$, and that van Kampen's perturbative method for $Q(0)$
requires solving a succession of ODE initial-value problems. The authors obtain $Q(0)$ from the
normal-form transformation: in normal-form coordinates the slow equation is independent of the
fast coordinate, so all initial conditions with the same slow normal-form coordinate share the
same long-term dynamics; the resulting projection is along the isochronic manifolds (a
generalisation of Winfree's isochrons), not the naive projection. Section 2 states that only with
a correct initial condition can long-term quantitative predictions be made by the low-dimensional
model. Section 3.1 (slow manifolds with fast oscillations) states that it is in general impossible
to project an initial condition so as to maintain the same essential dynamical behaviour for all
time, although matching is possible for a time of $o(|\eta|^{-2})$. Section 4.3 follows van
Kampen's perturbation-expansion approach, and Section 5.4 compares with the systematic adiabatic
elimination of Haake and Lewenstein.

## Cross-links

- Concepts: [[Meta-agents and hierarchical emergence]], [[Coarse Graining]]
- Themes: [[Meta-agents and hierarchical emergence]]
- Related sources: [[vankampen-1985-elimination-fast-variables]], [[haake-1983-adiabatic-drag-initial-slip]], [[geigenmuller-1983-elimination-fast-variables]], [[zwanzig-1961-memory-effects]]

## BibTeX

```bibtex
@article{cox1995initial,
  author  = {Cox, Stephen M. and Roberts, A. J.},
  title   = {Initial conditions for models of dynamical systems},
  journal = {Physica D},
  volume  = {85},
  number  = {1--2},
  pages   = {126--141},
  year    = {1995},
  doi     = {10.1016/0167-2789(94)00201-Z},
  eprint  = {chao-dyn/9411021},
  archivePrefix = {arXiv}
}
```
