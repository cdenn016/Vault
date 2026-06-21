---
type: reference
title: "Sociophysics: A Review of Galam Models"
aliases:
  - "Galam 2008"
authors:
  - Serge Galam
year: 2008
tags:
  - cluster/social-physics
  - project/multi-agent
  - project/social-physics
  - field/physics
  - field/sociology
  - cluster/social-physics/opinion-dynamics
created: 2026-06-18
updated: 2026-06-18
---

# Sociophysics: A Review of Galam Models

> [!info] Citation
> Galam, S. (2008). "Sociophysics: A Review of Galam Models." *International Journal of Modern Physics C* **19**(3), 409–440. DOI: [10.1142/S0129183108012297](https://doi.org/10.1142/S0129183108012297). Preprint: [arXiv:0803.1800](https://arxiv.org/abs/0803.1800).

## TL;DR

A retrospective review by Serge Galam of roughly twenty-five years of his own sociophysics modeling, organizing the work into five classes: democratic voting in bottom-up hierarchical systems, decision making, fragmentation versus coalitions, terrorism, and opinion dynamics. The unifying method is to treat opinions and votes as discrete spin-like variables evolving under local majority rules and aggregation across hierarchical levels, with several models advanced as having anticipated real political outcomes.

## What it establishes

The paper consolidates Galam's program of applying statistical-physics machinery — Ising-type spin variables, local majority dynamics, and renormalization-style hierarchical aggregation — to collective social and political behavior. Its central recurring mechanism is the *bottom-up voting hierarchy*: agents at one level form local groups, each group resolves to a single opinion by a (possibly biased) majority rule, and the resolved opinions become the agents of the next level up. Iterating this rule drives the population toward fixed points, and the review emphasizes how a tie-breaking bias produces a *killing point* — a threshold below which a minority is progressively eliminated as one ascends the hierarchy, so that even a near-majority of dissenters can be filtered out by repeated local aggregation.

Beyond hierarchical voting, the review surveys models of opinion dynamics with contrarian and floater agents, coalition and fragmentation dynamics among interacting groups (modeled by analogy to bond and site interactions), and the spread of terrorism-supporting opinion through a passive network. The throughline is methodological rather than empirical: complex macro-level political phenomena are recovered from simple, local, repeated update rules on discrete-state agents, and Galam argues several of these models successfully anticipated outcomes such as the 2000 French presidential first round and the 2005 French referendum on the European constitution.

> [!note] Editorial: the "successful prediction" claims are the author's own framing within this review; the note records them as stated, not as independently verified.

## Why the project cites it

This work is the canonical entry point for the **social-physics** strand of the project — the modeling tradition that treats interacting opinion-holding agents as a physical many-body system. It sits alongside the other consensus-dynamics references the project draws on ([[degroot-1974-consensus]], [[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]], [[deffuant2000-bounded-confidence|deffuant-2000-bounded-confidence]], [[hegselmann-2002-opinion|hegselmann-krause-2002]]) and supplies the discrete-spin, majority-rule counterpart to their continuous-averaging accounts of belief updating.

For the [[Gauge-Theoretic Multi-Agent VFE Model]], Galam's program is a precursor and a contrast case. The project recasts populations of belief-carrying agents as [[Agents as fibre-bundle sections]] coupled through a gauge connection, with belief updates derived from [[Multi-agent variational free energy]] rather than imposed as ad hoc spin rules. Galam's majority dynamics can be read as a coarse, discrete shadow of this: where Galam fixes a local update rule by hand, the VFE formulation derives interaction from minimizing free energy, with [[Precision weighting]] modulating how strongly an agent conforms to its neighbors and [[Belief inertia]] resisting change. The project's information-geometric machinery — beliefs as points on a statistical manifold equipped with the [[Fisher information metric]] — generalizes Galam's binary opinion states to full probability distributions.

Galam's hierarchical bottom-up aggregation is also a concrete sociological instance of the project's [[Meta-agents and hierarchical emergence]] and [[Renormalization-group flow of beliefs]]: repeated local resolution producing higher-level collective opinions is structurally the social-science analogue of coarse-graining beliefs across scales, the same intuition the project formalizes in its [[Ouroboros multi-scale dynamics]]. Citing Galam (2008) thus anchors the project's claim that its gauge-theoretic, variational treatment of multi-agent belief is a principled successor to a well-established sociophysics literature, recovering majority-driven consensus and minority-elimination phenomena as limiting cases of a free-energy-minimizing dynamics.

```bibtex
@article{galam2008sociophysics,
  author  = {Galam, Serge},
  title   = {Sociophysics: A Review of {Galam} Models},
  journal = {International Journal of Modern Physics C},
  volume  = {19},
  number  = {3},
  pages   = {409--440},
  year    = {2008},
  doi     = {10.1142/S0129183108012297},
  eprint  = {0803.1800},
  archivePrefix = {arXiv},
  primaryClass  = {physics.soc-ph}
}
```
