---
type: reference
title: "Social Influence Network Theory"
aliases:
  - "Friedkin & Johnsen 2011"
  - "Social Influence Network Theory"
  - "Social Influence Networks"
authors:
  - Noah E. Friedkin
  - Eugene C. Johnsen
year: 2011
tags:
  - cluster/social-physics
  - project/social-physics
  - project/multi-agent
  - field/sociology
  - field/mathematics
  - cluster/social-physics/opinion-dynamics
created: 2026-06-19
updated: 2026-06-19
---

# Social Influence Network Theory

> [!info] Citation
> Friedkin, N. E., & Johnsen, E. C. (2011). *Social Influence Network Theory: A Sociological Examination of Small Group Dynamics*. Structural Analysis in the Social Sciences, No. 33. Cambridge: Cambridge University Press. DOI: [10.1017/CBO9780511976735](https://doi.org/10.1017/CBO9780511976735). ISBN 9781107002463 (hardback), 9781107617674 (paperback).

## TL;DR

This is the book-length consolidation of the Friedkin–Johnsen (FJ) model of opinion dynamics, twenty years after the founding paper. Friedkin and Johnsen develop a process theory of attitude formation and change in which each actor in a small group revises its opinion as a weighted blend of interpersonal influences mediated by the network and a persistent anchoring to its own initial position. The book situates this mechanism within social network theory, derives the equilibrium structure of opinions analytically, and confronts the model with experimental small-group data, treating consensus, persistent disagreement, polarization, and factional structure as outcomes of a single linear influence process rather than as separate phenomena.

## What it establishes

The FJ model posits that an actor's opinion at equilibrium reflects both who influences whom (the network) and how much each actor clings to its own prior view (susceptibility). For a group of $n$ actors with opinions $y \in \mathbb{R}^n$, the dynamics iterate

$$
y^{(t+1)} = \Lambda\, W\, y^{(t)} + (I - \Lambda)\, y^{(0)},
$$

where $W$ is a row-stochastic matrix of interpersonal influence weights, $\Lambda = \mathrm{diag}(\lambda_1, \dots, \lambda_n)$ collects each actor's *susceptibility* $\lambda_i \in [0,1]$ to social influence, and $y^{(0)}$ is the vector of fixed initial (anchoring) opinions. The complementary term $(I-\Lambda)\,y^{(0)}$ encodes each actor's stubbornness or attachment to its own prejudice. When the process converges it reaches the closed-form equilibrium

$$
y^{(\infty)} = (I - \Lambda W)^{-1} (I - \Lambda)\, y^{(0)},
$$

a linear functional of the initial opinions mediated by the influence structure.

The book's contributions extend well past the algebra of the founding paper. It embeds the model in social network theory, giving sociological interpretations of $W$ (via interpersonal influence and power) and of $\Lambda$ (via actors' openness to influence), and shows how the equilibrium operator $V = (I - \Lambda W)^{-1}(I-\Lambda)$ expresses total influence as a sum over direct and indirect (multi-step) influence paths through the network. Because susceptibilities below unity preserve attachment to initial positions, the model produces stable equilibria in which opinions remain heterogeneous — supplying a formal mechanism for persistent disagreement, partial conformity, factionalization, and polarization rather than forced consensus. The DeGroot consensus model is recovered as the special case $\Lambda = I$ (full susceptibility, pure repeated averaging). Throughout, the theory is tied to experimental small-group studies, positioning it as an empirically tested account of attitude change rather than a purely formal construction.

## Why the project cites it

[[belief-inertia]] cites this book as the canonical, book-length statement of the Friedkin–Johnsen opinion-dynamics model, which the manuscript recovers as a limiting case of multi-agent variational-free-energy minimization. The FJ update is among the classical sociophysics / [[Opinion dynamics]] models — alongside DeGroot social learning, bounded-confidence Hegselmann–Krause and Deffuant, echo-chamber formation, and Social Impact Theory — that [[belief-inertia]] shows arise from [[Multi-agent variational free energy]] on statistical manifolds with GL($K$) gauge-transported KL coupling $\mathrm{KL}(q_i \,\|\, \Omega_{ij} q_j)$.

The mapping is precise where it matters for the founding manuscript of [[SocialPhysics]]. The anchoring term $(I-\Lambda)\,y^{(0)}$ is the sociological precursor to the project's [[Belief inertia]]: an actor's persistent resistance to revising its state in the face of incoming influence. Where Friedkin and Johnsen impose susceptibility $\lambda_i$ as a constant parameter, [[belief-inertia]] recasts that resistance geometrically through [[Mass as Fisher information]], so the reluctance to move is set by the curvature of the actor's local statistical manifold via the [[Fisher information metric]] rather than fixed by hand. The influence matrix $W$ is the flat, scalar-opinion shadow of the project's relational coupling: in the gauge-theoretic generalization, scalar opinions become full probabilistic beliefs carried by [[Agents as fibre-bundle sections]], averaging becomes transport-and-combination governed by the [[Natural gradient]], and the static stochastic mixing is replaced by influence propagated along a connection via [[Gauge transformation]], with residual disagreement around belief-exchange loops registered as [[Holonomy]]. The FJ equilibrium — stable and generally non-consensual — is exactly the kind of heterogeneous fixed point the overdamped (gradient-flow) limit of the variational dynamics is meant to reproduce.

The deeper claim of [[belief-inertia]] is that reading the Fisher/precision tensor as an inertial mass (the Hamiltonian ansatz, [[Hamiltonian belief dynamics]]) gives beliefs *momentum*, predicting opinion oscillation, overshoot, resonance, and momentum transfer that first-order influence-process models like FJ cannot exhibit. Against that extension, Social Influence Network Theory furnishes the overdamped baseline: the well-tested, first-order linear-influence account that the novel underdamped regime is positioned to generalize. The model is implemented in the MAgent codebase (the Hamiltonian integrator), so the citation also ties [[SocialPhysics]] to the [[Gauge-Theoretic Multi-Agent VFE Model]]. The note sits in the same opinion-dynamics lineage as [[friedkin-johnsen-1990]] (the founding paper), [[degroot-1974-consensus]] (the recovered consensus limit), [[deffuant-2000-bounded-confidence]] and [[hegselmann-krause-2002]] (bounded-confidence variants), [[galam-2008-sociophysics]], and the broader [[Sociophysics]] survey [[castellano-fortunato-loreto-2009-social-dynamics]]; it also connects to the modern review of influence models [[flache-2017-social-influence-models]], and it sits within the [[Renormalization-group flow of beliefs]] and [[Meta-agents and hierarchical emergence]] picture of how micro-level interaction aggregates into macro-level opinion structure.

```bibtex
@book{friedkin2011social,
  author    = {Friedkin, Noah E. and Johnsen, Eugene C.},
  title     = {Social Influence Network Theory: A Sociological Examination of Small Group Dynamics},
  series    = {Structural Analysis in the Social Sciences},
  number    = {33},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {2011},
  doi       = {10.1017/CBO9780511976735},
  isbn      = {9781107002463}
}
```
