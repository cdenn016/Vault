---
type: reference
title: "Reaching a Consensus"
aliases: ["DeGroot 1974"]
authors: ["Morris H. DeGroot"]
year: 1974
tags: [cluster/social-physics, project/multi-agent, project/social-physics, field/statistics, field/sociology, cluster/social-physics/opinion-dynamics]
created: 2026-06-18
updated: 2026-06-18
---

# Reaching a Consensus

> [!info] Citation
> Morris H. DeGroot (1974). "Reaching a Consensus." *Journal of the American Statistical Association*, **69**(345), 118–121. DOI: 10.1080/01621459.1974.10480137.

## TL;DR

DeGroot introduces a simple linear model in which a group of agents repeatedly revises its subjective opinions (probability distributions or point estimates) by taking weighted averages of one another's current opinions. He shows that, under mild conditions on the stochastic matrix of inter-agent trust weights, the iterated averaging converges to a common consensus opinion shared by the whole group.

## What it establishes

Each of $k$ agents holds an opinion $F_i$, and agent $i$ assigns a nonnegative weight $p_{ij}$ to agent $j$ with $\sum_j p_{ij} = 1$. Opinions are updated synchronously by

$$
F_i^{(t+1)} = \sum_{j=1}^{k} p_{ij}\, F_j^{(t)},
$$

so the opinion vector evolves under powers of the row-stochastic matrix $P$. DeGroot establishes that a consensus is reached — all $F_i^{(t)}$ converge to a single limiting opinion — precisely when $P^t$ converges to a matrix with identical rows, and he characterizes this in terms of the Markov chain associated with $P$ (essentially, the chain must be such that a stationary distribution is reached). The limiting consensus is a weighted average of the initial opinions, with weights given by the stationary distribution of $P$. The result holds whether opinions are full probability distributions or scalar parameter estimates, since the update is linear.

## Why the project cites it

DeGroot's averaging dynamics is the canonical starting point of opinion-dynamics and **social physics**: a tractable, fully linear model of how local trust-weighted interaction drives a population toward agreement. The project cites it as the classical baseline against which its own [[Multi-agent variational free energy]] formulation is contrasted.

Where DeGroot fixes opinions as objects pushed around by a static stochastic matrix, the project recasts inter-agent belief exchange as coupled minimization of [[Variational free energy]], so that consensus emerges from [[Prediction error]] reduction and [[Precision weighting]] rather than from prescribed averaging weights. The trust weights $p_{ij}$ acquire a geometric reading once beliefs live on a statistical manifold: averaging is replaced by transport and combination governed by the [[Fisher information metric]] and the [[Natural gradient]], and the gauge-theoretic picture treats each agent as a local frame via [[Agents as fibre-bundle sections]], with disagreement that fails to wash out registered as [[Holonomy]] around belief-exchange loops. DeGroot's stationary-distribution consensus is thus the flat, abelian limiting case of the richer, possibly non-trivial dynamics the project develops, and connects to its treatment of [[Belief inertia]] and [[Meta-agents and hierarchical emergence]].

The note sits in the same social-physics lineage the project draws on for opinion dynamics, alongside [[friedkin-johnsen-1990]], [[deffuant-2000-bounded-confidence]], [[hegselmann-krause-2002]], and [[galam-2008-sociophysics]].

```bibtex
@article{degroot1974consensus,
  author  = {DeGroot, Morris H.},
  title   = {Reaching a Consensus},
  journal = {Journal of the American Statistical Association},
  year    = {1974},
  volume  = {69},
  number  = {345},
  pages   = {118--121},
  doi     = {10.1080/01621459.1974.10480137}
}
```
