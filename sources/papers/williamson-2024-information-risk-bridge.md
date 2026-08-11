---
type: paper
title: Information Processing Equalities and the Information–Risk Bridge
aliases:
  - Williamson Cranko 2024
authors:
  - Robert C. Williamson
  - Zac Cranko
year: 2024
arxiv: null
url: https://jmlr.org/papers/v25/22-0988.html
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
  - field/mathematics
status: stable
created: 2026-08-10
updated: 2026-08-10
---

# Information Processing Equalities and the Information–Risk Bridge

> [!info] Citation
> Robert C. Williamson and Zac Cranko. “Information Processing Equalities and the Information–Risk Bridge.” *Journal of Machine Learning Research* 25(103):1–53, 2024. [JMLR](https://jmlr.org/papers/v25/22-0988.html).

## TL;DR

The paper develops information measures for statistical experiments that connect Markov-operator processing, families of losses/hypotheses, Bayes risk, and familiar divergences. It clarifies why exact information preservation is a family-of-decisions statement rather than equality of one chosen divergence.

## Problem & setting

Data-processing inequalities say information cannot increase through a channel, but equality conditions and operational consequences depend on what information measure and decision class are used. The authors seek a common framework encompassing divergence- and risk-based comparisons.

## Method

Two information constructions are defined on statistical experiments using convex-analytic and risk representations. The framework subsumes $f$-divergences, integral probability metrics, maximum mean discrepancy/N-distances, and $(f,\Gamma)$ divergences, and studies closure under Markov operators.

## Key results

- The information–risk bridge relates information measures to achievable Bayes risks.
- Markov closure yields information-processing equalities under the paper’s conditions.
- Blackwell–Sherman–Stein comparison requires the full separating class—equivalently all relevant losses/convex information measures—not merely one KL equality.

## Relevance to this research

This paper supplies a hierarchy for recovery experiments. A claim can report preservation for a named hypothesis/loss class without inflating it to universal statistical equivalence. It motivates measuring downstream risks alongside KL/Fisher contraction and documenting which class is actually separated.

## Scope limits

An equality for one divergence, one task, or one hypothesis class does not prove the existence of a common Blackwell recovery kernel. Conversely, failure on an overly rich class need not refute task-specific sufficiency. The class and channel assumptions must be stated.

## Cross-links

- [[Statistical experiment comparison and deficiency]]
- [[blackwell-1953-experiment-comparison]]
- [[Sufficient statistics]]
- [[Coarse Graining]]

## BibTeX

```bibtex
@article{williamson2024information,
  title   = {Information Processing Equalities and the Information--Risk Bridge},
  author  = {Williamson, Robert C. and Cranko, Zac},
  journal = {Journal of Machine Learning Research},
  volume  = {25},
  number  = {103},
  pages   = {1--53},
  year    = {2024},
  url     = {https://jmlr.org/papers/v25/22-0988.html}
}
```
