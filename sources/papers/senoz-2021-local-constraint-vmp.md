---
type: paper
title: "Variational Message Passing and Local Constraint Manipulation in Factor Graphs"
aliases:
  - "Şenöz et al. 2021 constrained-Bethe VMP"
authors:
  - İsmail Şenöz
  - Thijs van de Laar
  - Dmitry Bagaev
  - Bert de Vries
year: 2021
arxiv: null
url: https://doi.org/10.3390/e23070807
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-08-10
---

# Variational Message Passing and Local Constraint Manipulation in Factor Graphs

> [!info] Citation
> Şenöz, İ., van de Laar, T., Bagaev, D., & de Vries, B. (2021). Variational Message Passing and Local Constraint Manipulation in Factor Graphs. *Entropy*, 23(7), Article 807. https://doi.org/10.3390/e23070807

## TL;DR

Şenöz and colleagues derive a family of message-passing updates by minimizing constrained Bethe free energy over local factor and variable beliefs. Changing local normalization, marginalization, factorization, moment-matching, Laplace, delta, or estimation constraints recovers sum-product, structured and mean-field VMP, Laplace propagation, EM, and EP within one framework.

## Problem & setting

Variational algorithms are often presented as unrelated update recipes. The paper asks how their approximation choices can be represented locally on a Forney-style factor graph and how those constraints determine both the objective and the resulting messages.

## Method

The starting point is Bethe free-energy minimization over beliefs in a local polytope. A Lagrangian enforces normalization and factor-variable marginalization constraints. Additional local form and factorization constraints alter the stationary equations, which can be read as message updates. The framework also provides local free-energy contributions for evaluating the constrained objective.

## Key results

The paper unifies familiar update rules and supplies first-principles derivations for their local stationary conditions. It does not imply that every constrained variant is exact or globally convergent. Ordinary sum-product belief propagation is exact on a tree under its standard assumptions; imposing mean-field, moment, Laplace, or other form constraints can leave an approximation even when the underlying factor graph is a tree. On loopy graphs, local consistency need not imply that the pseudomarginals arise from one exact global joint law.

## Relevance to this research

This is an algorithmic bridge from the exact finite [[Multi-agent variational free energy]] to typed approximation layers. A correct implementation should first use unconstrained sum-product on trees as the exact oracle, then measure approximation error separately for structured VMP, mean-field VMP, EP, or hybrid constraints. The repository's exact correlated $Q$ must not be identified with locally consistent Bethe beliefs without a realizability proof.

## Cross-links

- Concepts: [[Belief Propagation]], [[Mean-Field Approximation]], [[Variational free energy]], [[Multi-agent variational free energy]]
- Themes: [[Inference machinery — variational EM and filtering]]
- Related sources: [[winn-2005-variational-message-passing]], [[yedidia-freeman-weiss-2005-region-free-energy]]

## BibTeX

```bibtex
@article{senoz2021localconstraintvmp,
  author  = {Şenöz, İsmail and van de Laar, Thijs and Bagaev, Dmitry and de Vries, Bert},
  title   = {Variational Message Passing and Local Constraint Manipulation in Factor Graphs},
  journal = {Entropy},
  volume  = {23},
  number  = {7},
  pages   = {807},
  year    = {2021},
  doi     = {10.3390/e23070807}
}
```
