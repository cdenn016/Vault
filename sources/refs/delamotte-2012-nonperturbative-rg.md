---
type: reference
title: "An Introduction to the Nonperturbative Renormalization Group"
aliases: ["Delamotte 2012", "An Introduction to the Nonperturbative Renormalization Group", "Delamotte FRG"]
authors: ["Bertrand Delamotte"]
year: 2012
arxiv: cond-mat/0702365
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/physics, field/mathematics]
created: 2026-06-20
updated: 2026-06-20
---

# An Introduction to the Nonperturbative Renormalization Group

> [!info] Citation
> Delamotte, B. (2012). *An Introduction to the Nonperturbative Renormalization Group*. In A. Schwenk & J. Polonyi (eds.), *Renormalization Group and Effective Field Theory Approaches to Many-Body Systems*, Lecture Notes in Physics, Vol. 852, pp. 49–132. Springer. arXiv:[cond-mat/0702365](https://arxiv.org/abs/cond-mat/0702365). DOI: 10.1007/978-3-642-27320-9_2.

## TL;DR

A widely used pedagogical introduction to the **nonperturbative (functional) renormalization group** built on the Wetterich equation for the scale-dependent effective average action $\Gamma_k$. Delamotte develops the exact RG flow equation $\partial_k \Gamma_k = \tfrac{1}{2}\,\mathrm{Tr}\big[(\Gamma_k^{(2)}+R_k)^{-1}\,\partial_k R_k\big]$ from scratch, explains the regulator $R_k$ that integrates fluctuations shell by shell, and works the derivative expansion and the local-potential approximation on concrete examples (Ising / $O(N)$ models).

## What it establishes

The exact functional RG flow interpolating between the bare action at the UV scale and the full effective action in the IR; the role of the infrared regulator; the derivative expansion as a controlled nonperturbative truncation; and the recovery of critical exponents and fixed-point structure without small-coupling expansions. It is a hands-on complement to the QFT-oriented review [[berges-tetradis-wetterich-2002-nonperturbative-rg]] already in the vault.

## Why the project cites it

The program reads coarse-graining over agents as a **renormalization-group flow of beliefs** ([[Renormalization-group flow of beliefs]], [[Renormalization group flow]]) feeding the [[Ouroboros multi-scale dynamics|Ouroboros tower]] and [[Meta-agents and hierarchical emergence|meta-agent]] formation. Delamotte is the accessible reference for the *functional* RG — flowing an entire effective action rather than a few couplings — which is the right formalism if belief coarse-graining is to be made exact rather than schematic. It pairs naturally with the information-geometric RG ([[beny-osborne-2015-info-geometric-rg]]) and the variational-RG/deep-learning correspondence ([[mehta-schwab-2014-variational-rg-deep-learning]]) the program already tracks, and with [[cardy-1996-scaling-renormalization|Cardy]] for the statistical-physics foundation.

> [!note] Editorial: Cited as a pedagogical functional-RG reference supporting the program's belief-coarse-graining / RG-flow reading; the program has not derived an explicit Wetterich equation for beliefs.

```bibtex
@incollection{delamotte2012introduction,
  author    = {Delamotte, Bertrand},
  title     = {An Introduction to the Nonperturbative Renormalization Group},
  booktitle = {Renormalization Group and Effective Field Theory Approaches to Many-Body Systems},
  editor    = {Schwenk, Achim and Polonyi, Janos},
  series    = {Lecture Notes in Physics},
  volume    = {852},
  pages     = {49--132},
  publisher = {Springer},
  year      = {2012},
  doi       = {10.1007/978-3-642-27320-9_2},
  note      = {arXiv:cond-mat/0702365}
}
```
