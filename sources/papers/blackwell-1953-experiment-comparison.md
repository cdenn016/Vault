---
type: paper
title: Equivalent Comparisons of Experiments
aliases:
  - Blackwell 1953 experiment comparison
authors:
  - David Blackwell
year: 1953
arxiv: null
url: https://doi.org/10.1214/aoms/1177729032
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/mathematics
status: stable
created: 2026-08-10
updated: 2026-08-10
---

# Equivalent Comparisons of Experiments

> [!info] Citation
> David Blackwell. “Equivalent Comparisons of Experiments.” *The Annals of Mathematical Statistics* 24(2):265–272, 1953. [doi:10.1214/aoms/1177729032](https://doi.org/10.1214/aoms/1177729032).

## TL;DR

Blackwell comparison turns “one observation is at least as informative as another” into an operational statement: a single parameter-independent randomization maps the more informative experiment to the less informative one, equivalently the former is no worse across the relevant class of decision problems. The paper extends earlier finite-outcome equivalences and studies weaker finite-decision comparisons.

## Problem & setting

An experiment is a family of distributions indexed by an unknown parameter. Comparing experiments must therefore be uniform over the family, not fitted separately at a selected parameter or distribution. Blackwell asks when one experiment can replace another without increasing attainable decision risk.

## Method

The paper compares decision-theoretic and randomization criteria. In modern notation, experiment $E=\{P_\theta\}$ dominates $F=\{Q_\theta\}$ when one Markov kernel $K$, independent of $\theta$, satisfies $Q_\theta=P_\theta K$ for every $\theta$. The 1953 treatment removes the earlier finite-outcome restriction for equivalence comparisons and analyzes weaker $k$-decision comparisons, including a complete equivalence for dichotomies.

## Key results

- Randomization/garbling provides the operational simulation relation between experiments.
- Decision comparison must range over an appropriate class of losses and decision rules; improvement for one loss is not the Blackwell order.
- For dichotomies, the comparison methods studied in the paper coincide; for broader settings, the paper carefully separates weaker finite-decision criteria.

## Relevance to this research

This is the correct benchmark for claims that a coarse belief state or message “retains all usable information.” Exact recovery requires one common stochastic reconstruction channel over the entire statistical experiment. A decoder trained for one prior, one state, or one direction does not establish Blackwell sufficiency. Likewise, contraction of KL divergence or Fisher information is evidence of data processing, not proof of experiment equivalence.

## Scope limits

The frequently used quantitative deficiency
$\delta(E,F)=\inf_K\sup_\theta\lVert Q_\theta-P_\theta K\rVert_{\mathrm{TV}}$
is recorded here as a later Le Cam-style relaxation, not as a theorem established in this 1953 paper. This ingest verifies exact Blackwell comparison, not a complete deficiency theory.

## Cross-links

- [[Statistical experiment comparison and deficiency]]
- [[Sufficient statistics]]
- [[Coarse Graining]]
- [[williamson-2024-information-risk-bridge]]

## BibTeX

```bibtex
@article{blackwell1953equivalent,
  title   = {Equivalent Comparisons of Experiments},
  author  = {Blackwell, David},
  journal = {The Annals of Mathematical Statistics},
  volume  = {24},
  number  = {2},
  pages   = {265--272},
  year    = {1953},
  doi     = {10.1214/aoms/1177729032}
}
```
