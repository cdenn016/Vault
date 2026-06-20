---
type: reference
title: "Towards a Geometry and Analysis for Bayesian Mechanics"
aliases:
  - "Sakthivadivel 2022"
  - "Sakthivadivel (2022) Geometry for Bayesian Mechanics"
authors:
  - Dalton A. R. Sakthivadivel
year: 2022
arxiv: "2204.11900"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/mathematics
  - field/statistics
  - cluster/participatory/consciousness
created: 2026-06-19
updated: 2026-06-19
---

# Towards a Geometry and Analysis for Bayesian Mechanics

> [!info] Citation
> Sakthivadivel, D. A. R. (2022). "Towards a Geometry and Analysis for Bayesian Mechanics." Preprint, [arXiv:2204.11900](https://arxiv.org/abs/2204.11900).

## TL;DR

An axiomatic, geometric formulation of **[[Bayesian mechanics]]**: it argues that any dynamical system with constraints on its dynamics necessarily *looks as though it performs inference against those constraints*, and that for a non-isolated system the constraints imply external (environmental) variables embedding it. Using classical dynamical-systems theory from statistical mechanics, the inference is shown to be equivalent to a gradient ascent on the Shannon entropy functional, recovering approximate Bayesian inference under a locally ergodic measure on state space. It supplies the geometric/analytic backbone the project cites for the Bayesian-mechanics machinery.

## What it establishes

- **Constraints induce apparent inference.** A constrained dynamical system behaves as if it is inferring against its constraints — a clean, assumption-light route to the "physics of beliefs" claim.
- **Entropy-gradient dynamics.** The inferential flow is gradient ascent on Shannon entropy under a local-ergodicity assumption, tying the dynamics to information-theoretic geometry and the [[Fisher information metric]].
- **Embedding from non-isolation.** A non-isolated constrained system implies external variables it is embedded in — the formal seed of the internal/external (Markov-blanket) partition.

## Why the project cites it

This is the **geometric Bayesian-mechanics reference** that [[participatory-it-from-bit]] cites for the analytic underpinnings of its inference-as-geometry stance. The entropy-gradient / [[Natural gradient]] flow on a statistical manifold is exactly the structure the project uses for belief updating, and the "constraints induce apparent inference" thesis is the minimal version of the participatory claim that what looks like physics is the geometry of an embedded observer's beliefs ([[Participatory realism (it from bit)]]). The embedding-from-non-isolation argument connects to the [[Markov blanket interpretation debate]] (what licenses the internal/external cut) and to the project's [[Multi-agent variational free energy]] (many mutually-embedding constrained sub-systems). Companion to the [[Bayesian mechanics]] hub and its lineage: [[friston-2019-particular-physics]], [[dacosta-2021-bayesian-mechanics]], [[ramstead-2023-bayesian-mechanics]], [[caticha-2019-entropic-dynamics]].

```bibtex
@article{sakthivadivel2022geometry,
  title   = {Towards a Geometry and Analysis for Bayesian Mechanics},
  author  = {Sakthivadivel, Dalton A. R.},
  journal = {arXiv preprint arXiv:2204.11900},
  year    = {2022},
  eprint  = {2204.11900},
  archivePrefix = {arXiv},
  primaryClass  = {math-ph}
}
```
