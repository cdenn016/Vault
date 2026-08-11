---
type: paper
title: A Semi-Invertible Oseledets Theorem with Applications to Transfer Operator Cocycles
aliases:
  - Froyland Lloyd Quas semi-invertible Oseledets
authors:
  - Gary Froyland
  - Simon Lloyd
  - Anthony Quas
year: 2013
arxiv: "1001.5313"
url: https://doi.org/10.3934/dcds.2013.33.3835
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
status: stable
created: 2026-08-10
updated: 2026-08-10
---

# A Semi-Invertible Oseledets Theorem with Applications to Transfer Operator Cocycles

> [!info] Citation
> Gary Froyland, Simon Lloyd, and Anthony Quas. “A Semi-Invertible Oseledets Theorem with Applications to Transfer Operator Cocycles.” *Discrete and Continuous Dynamical Systems* 33(9):3835–3860, 2013. [doi:10.3934/dcds.2013.33.3835](https://doi.org/10.3934/dcds.2013.33.3835); [arXiv:1001.5313](https://arxiv.org/abs/1001.5313).

## TL;DR

The paper proves an Oseledets splitting for quasi-compact Banach-space cocycles whose base dynamics are invertible although the operator fibers need not be. Applications identify coherent structures and escape rates for random dynamical systems through transfer-operator cocycles.

## Problem & setting

Many transfer operators are noninvertible even when the environmental/base dynamics are invertible. Standard invertible-cocycle theorems are therefore too strong, while filtration-only results can be insufficient for tracking covariant subspaces.

## Method

The main semi-invertible theorem assumes an ergodic invertible base (presented as a homeomorphism on a Borel subset of a separable complete metric space), a $P$-continuous Banach-space generator, log-integrability, and quasi-compactness: the index-of-compactness exponent lies below the top Lyapunov exponent. It constructs equivariant exceptional Oseledets subspaces.

## Key results

- Under those hypotheses, a unique measurable/$P$-continuous Oseledets splitting exists for exceptional exponents.
- Fiber operators may be noninvertible even though the base is invertible.
- Transfer-operator applications relate exceptional directions to coherent structures and metastable behavior.

## Relevance to this research

If successive coarse-graining or learning Jacobians form a stationary quasi-compact cocycle, covariant subspaces could distinguish stable, unstable, and slowly mixing inference directions. The theorem also provides a checklist for a rigorous recovery/RG experiment rather than only an attractive vocabulary.

## Scope limits

Citation alone closes no Oseledets obligation. The project must identify an invertible ergodic base, a measurable/$P$-continuous operator generator on a specified Banach space, verify $\int\log^+\lVert L_\omega\rVert dP<\infty$, and establish quasi-compactness. Deterministic finite-depth Jacobian products or finite-time QR spectra do not prove the theorem applies.

## Cross-links

- [[Renormalization group flow]]
- [[Renormalization-group flow of beliefs]]
- [[blumenthal-2016-banach-multiplicative-ergodic]]

## BibTeX

```bibtex
@article{froyland2013semi,
  title   = {A Semi-Invertible Oseledets Theorem with Applications to Transfer Operator Cocycles},
  author  = {Froyland, Gary and Lloyd, Simon and Quas, Anthony},
  journal = {Discrete and Continuous Dynamical Systems},
  volume  = {33},
  number  = {9},
  pages   = {3835--3860},
  year    = {2013},
  doi     = {10.3934/dcds.2013.33.3835},
  eprint  = {1001.5313},
  archivePrefix = {arXiv}
}
```
