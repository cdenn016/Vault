---
type: concept
title: Statistical Experiment Comparison and Deficiency
aliases:
  - Blackwell comparison
  - Blackwell order
  - Statistical deficiency
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-08-10
updated: 2026-08-10
---

# Statistical Experiment Comparison and Deficiency

## Definition

A statistical experiment is a parameter-indexed family $E=\{P_\theta:\theta\in\Theta\}$. Experiment $E$ Blackwell-dominates $F=\{Q_\theta\}$ when there exists **one parameter-independent Markov kernel** $K$ such that

$$Q_\theta=P_\theta K\qquad\text{for every }\theta\in\Theta.$$

Operationally, $F$ is a garbling of $E$: any decision rule using $F$ can be simulated from $E$. Under the relevant regularity and decision-class assumptions, this coincides with $E$ having no larger optimal risk for every decision problem.

## Why it matters

This order distinguishes exact recovery from preservation of a selected statistic. A decoder that works only for one prior, one parameter value, or one distribution is not a Blackwell recovery channel. Equality of one divergence, one downstream accuracy, or one Fisher direction is likewise insufficient because universal experiment comparison quantifies over a separating class of decisions.

## Details

A standard quantitative relaxation is the one-sided deficiency

$$\delta(E,F)=\inf_K\sup_{\theta\in\Theta}
  \left\lVert Q_\theta-P_\theta K\right\rVert_{\mathrm{TV}},$$

with conventions varying by normalization and direction. This formula is recorded as a **Le Cam-style future-reading lead**: the present source set directly verifies Blackwell’s exact comparison and the modern information–risk bridge, not a complete theory of deficiency distance. Because the relation is directional, approximate simulation of $F$ from $E$ and approximate simulation of $E$ from $F$ are separate obligations.

Data processing supplies necessary monotonicity checks—divergences and decision information cannot improve after a channel—but a single equality rarely supplies the common reverse kernel needed for experiment equivalence. Entropy-rate preservation under a Markov aggregation is also a different statement: it concerns path coding, not every parameter-indexed decision problem.

## In this work

For multi-agent recovery or coarse-graining, specify the experiment: the parameter family, observation law, coarse channel, and allowed decoder. Then test a single held-out recovery kernel across the family and report the decision/loss class. KL or Fisher contraction should be described as a data-processing diagnostic unless a common reconstruction kernel and uniform error bound are established. Citation alone does not close the project’s recovery obligation.

## Sources

- [[blackwell-1953-experiment-comparison]]
- [[williamson-2024-information-risk-bridge]]
- [[geiger-2013-kl-aggregation]]
- [[geiger-temmel-2013-information-preserving-aggregation]]

## See also

- [[Sufficient statistics]]
- [[Coarse Graining]]
- [[Fisher information metric]]
- [[Renormalization-group flow of beliefs]]
