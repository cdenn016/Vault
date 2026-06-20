---
type: reference
title: "Social Influence and Opinions"
aliases: ["Friedkin 1990", "Friedkin & Johnsen 1990"]
authors: ["Noah E. Friedkin", "Eugene C. Johnsen"]
year: 1990
tags: [cluster/social-physics, project/multi-agent, project/social-physics, field/sociology, field/mathematics, cluster/social-physics/opinion-dynamics]
created: 2026-06-18
updated: 2026-06-18
---

# Social Influence and Opinions

> [!info] Citation
> Friedkin, N. E., & Johnsen, E. C. (1990). "Social Influence and Opinions." *The Journal of Mathematical Sociology*, **15**(3-4), 193-205.

## TL;DR

Friedkin and Johnsen propose a dynamical model in which each agent updates its opinion as a weighted blend of (i) the influence of its network neighbours' current opinions and (ii) a fixed anchoring to its own initial opinion. By retaining a persistent attachment to the initial state, the model produces stable, generally non-consensual equilibria, distinguishing it from pure averaging dynamics. It has become a canonical formal account of how interpersonal influence structures shape the distribution of opinions.

## What it establishes

The Friedkin–Johnsen model specifies a *social process* rather than assuming a social equilibrium. Each agent $i$ holds a current opinion $y_i$ and a fixed initial opinion $y_i^{(0)}$, and updates according to

$$
y_i \leftarrow \lambda_i \sum_j W_{ij}\, y_j + (1-\lambda_i)\, y_i^{(0)},
$$

where $W$ is a row-stochastic matrix of interpersonal influence weights and $\lambda_i \in [0,1]$ is the agent's *susceptibility* to social influence. The term $(1-\lambda_i)\,y_i^{(0)}$ encodes a stubbornness or anchoring to the agent's own prejudice. The key consequences established in the paper are:

- Several earlier influence models — notably DeGroot-style consensus averaging — arise as special cases (e.g. when $\lambda_i = 1$ for all agents the dynamics reduce to repeated averaging and tend toward consensus).
- With $\lambda_i < 1$ the dynamics admit stable equilibria in which opinions remain heterogeneous, providing a formal mechanism for persistent disagreement, conflict, and partial conformity rather than forced consensus.
- The equilibrium opinion vector is a linear functional of the initial opinions mediated by the influence structure, making the steady state analytically tractable.

> [!note] Editorial: The exact parameterization (e.g. whether $\lambda$ is agent-specific or scalar, and the precise normalization of $W$) varies across presentations of the model; the formulation above follows the standard linear influence-process reading of the 1990 paper.

## Why the project cites it

This work is cited as a social-physics anchor for the project's treatment of coupled belief dynamics among many interacting agents. Its relevance to the gauge-theoretic, variational-free-energy program is concrete on several fronts:

- **Belief inertia.** The fixed anchoring term $(1-\lambda_i)\,y_i^{(0)}$ is a sociological precursor to the project's notion of [[Belief inertia]]: an agent's resistance to revising its state in the face of incoming influence. Where Friedkin–Johnsen impose a constant susceptibility, the project recasts such inertia geometrically (see [[Mass as Fisher information]]) so that resistance to belief change is set by the curvature of the agent's local statistical manifold via the [[Fisher information metric]].

- **Multi-agent coupling.** The influence matrix $W$ is a precursor to the relational coupling formalized in [[Multi-agent variational free energy]], where agents minimize a shared/aggregate free energy rather than linearly averaging scalar opinions. The Friedkin–Johnsen equilibrium being non-consensual aligns with the project's interest in stable heterogeneous belief configurations rather than collapse to a single fixed point.

- **From linear opinions to belief fields.** The project generalizes scalar opinions to full probabilistic beliefs carried by [[Agents as fibre-bundle sections]], with influence propagated by [[Parallel transport]] across a connection rather than by a flat stochastic mixing matrix. Friedkin–Johnsen thus serves as the flat, no-gauge-curvature limit against which the gauge-theoretic extension is positioned.

- **Social physics lineage.** Together with [[degroot-1974-consensus]] (the consensus-averaging limit recovered as a special case) and bounded-confidence variants such as [[deffuant-2000-bounded-confidence]] and [[hegselmann-krause-2002]], this paper situates the project within the [[Renormalization-group flow of beliefs]] and [[Meta-agents and hierarchical emergence]] picture of how micro-level interaction rules aggregate into macro-level opinion structure.

```bibtex
@article{friedkin1990social,
  author  = {Friedkin, Noah E. and Johnsen, Eugene C.},
  title   = {Social Influence and Opinions},
  journal = {The Journal of Mathematical Sociology},
  volume  = {15},
  number  = {3-4},
  pages   = {193--205},
  year    = {1990},
  doi     = {10.1080/0022250X.1990.9990069}
}
```
