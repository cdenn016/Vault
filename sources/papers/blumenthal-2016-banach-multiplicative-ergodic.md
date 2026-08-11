---
type: paper
title: A Volume-Based Approach to the Multiplicative Ergodic Theorem on Banach Spaces
aliases:
  - Blumenthal Banach-space MET
authors:
  - Alex Blumenthal
year: 2016
arxiv: "1502.06554"
url: https://doi.org/10.3934/dcds.2016.36.2377
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
status: stable
created: 2026-08-10
updated: 2026-08-10
---

# A Volume-Based Approach to the Multiplicative Ergodic Theorem on Banach Spaces

> [!info] Citation
> Alex Blumenthal. “A Volume-Based Approach to the Multiplicative Ergodic Theorem on Banach Spaces.” *Discrete and Continuous Dynamical Systems* 36(5):2377–2403, 2016. [doi:10.3934/dcds.2016.36.2377](https://doi.org/10.3934/dcds.2016.36.2377); [arXiv:1502.06554](https://arxiv.org/abs/1502.06554).

## TL;DR

The paper proves a multiplicative ergodic theorem for linear cocycles on Banach spaces using finite-dimensional volume growth, under measurability and log-integrability assumptions and without requiring injective cocycle operators.

## Problem & setting

Infinite-dimensional or noninvertible evolution does not fit the simplest finite-dimensional invertible Oseledets theorem. The paper seeks a direct geometric proof that identifies Lyapunov growth through volumes of finite-dimensional parallelepipeds in a Banach space.

## Method

Over an ergodic measure-preserving base transformation (not necessarily invertible), a uniformly measurable operator cocycle $T_x$ satisfying $\int\log^+\lVert T_x\rVert\,d\mu<\infty$ is analyzed via maximal $q$-dimensional volume growth. These quantities organize exceptional growth rates and invariant filtrations.

## Key results

- Banach-space Lyapunov exponents and one-sided invariant filtrations are obtained under the paper’s hypotheses.
- No injectivity assumption on individual cocycle operators is required.
- Sums of leading exponents are related to asymptotic finite-dimensional volume growth.

## Relevance to this research

This is a plausible theorem family for linearized multi-scale or learning dynamics when the state space becomes functional/infinite-dimensional. It indicates the exact evidence needed before calling measured finite-time singular-value slopes “Lyapunov exponents”: an identified cocycle, invariant ergodic base, measurability, and log-integrability.

## Scope limits

The citation does not manufacture a Banach state space, invariant measure, stationary base dynamics, or measurable derivative cocycle for the model. Its one-sided filtration should not be reported as an invertible Oseledets splitting. Finite numerical slopes are diagnostics, not verification of the theorem’s assumptions or asymptotic conclusion.

## Cross-links

- [[Renormalization group flow]]
- [[Renormalization-group flow of beliefs]]
- [[froyland-2013-semi-invertible-oseledets]]

## BibTeX

```bibtex
@article{blumenthal2016volume,
  title   = {A Volume-Based Approach to the Multiplicative Ergodic Theorem on Banach Spaces},
  author  = {Blumenthal, Alex},
  journal = {Discrete and Continuous Dynamical Systems},
  volume  = {36},
  number  = {5},
  pages   = {2377--2403},
  year    = {2016},
  doi     = {10.3934/dcds.2016.36.2377},
  eprint  = {1502.06554},
  archivePrefix = {arXiv}
}
```
