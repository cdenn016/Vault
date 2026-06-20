---
type: reference
title: "Asymptotic Approximations of Integrals"
aliases:
  - "Wong 2001"
  - "Wong (2001) Asymptotic Approximations of Integrals"
authors:
  - Roderick Wong
year: 2001
tags:
  - cluster/methodology
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
created: 2026-06-19
updated: 2026-06-19
---

# Asymptotic Approximations of Integrals

> [!info] Citation
> Roderick Wong (2001). *Asymptotic Approximations of Integrals.* Classics in Applied Mathematics 34. SIAM. ISBN: 9780898714975.

## TL;DR

The standard rigorous reference on asymptotic evaluation of integrals — Laplace's method, the saddle-point / steepest-descent method, Watson's lemma, and stationary phase — with full error control. It is the technical backstop for the Laplace / saddle-point closure the project uses to reduce the belief partition function to a tractable effective free energy.

## Why the project cites it

The project's RG-style closure expands the partition function over a population of beliefs about its dominant (saddle) configuration; doing this rigorously, with controlled errors, is exactly Laplace's method and steepest descent as treated here. Wong supplies the precise asymptotics behind the Gaussian-approximation step of [[Renormalization-group flow of beliefs]] and the BIC marginal-likelihood expansion ([[schwarz-1978-bic]]). Companion asymptotic-methods reference: [[bender-orszag-1999-asymptotic-methods]]; physics context: [[cardy-1996-scaling-renormalization]]. Manuscript thread: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@book{wong2001asymptotic,
  author    = {Wong, Roderick},
  title     = {Asymptotic Approximations of Integrals},
  series    = {Classics in Applied Mathematics},
  number    = {34},
  publisher = {SIAM},
  year      = {2001},
  isbn      = {9780898714975},
  doi       = {10.1137/1.9780898719260}
}
```
