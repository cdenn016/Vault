---
type: reference
title: "Statistical Decision Rules and Optimal Inference (Cencov/Chentsov uniqueness theorem)"
aliases:
  - "Cencov (Chentsov) 1982"
  - "Chentsov 1982"
authors:
  - N. N. Cencov (Chentsov)
year: 1982
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/statistics
created: 2026-06-18
updated: 2026-06-18
---

# Statistical Decision Rules and Optimal Inference (Cencov/Chentsov uniqueness theorem)

> [!info] Citation
> N. N. Cencov (Chentsov), *Statistical Decision Rules and Optimal Inference*, Translations of Mathematical Monographs, vol. 53, American Mathematical Society, Providence, RI, 1982 (translated from the 1972 Russian original, Nauka, Moscow; translation edited by Lev J. Leifman). The monograph is the source of the **Cencov (Chentsov) uniqueness theorem** characterizing the [[Fisher information metric]] as the unique invariant metric on statistical manifolds.

## TL;DR

Cencov develops a category-theoretic, decision-theoretic foundation for mathematical statistics in which probability families are objects and Markov (stochastic) maps are the morphisms. Within this framework he proves that, up to scale, the [[Fisher information metric]] is the *only* Riemannian metric on the simplex of probability distributions that is invariant ("monotone") under sufficient statistics / Markov morphisms, and that the $\alpha$-connections are the corresponding invariant affine connections. This uniqueness result is the cornerstone justification for information geometry.

## What it establishes

- **Invariance / monotonicity principle.** Cencov treats statistical inference categorically: the natural transformations between probability families are Markov kernels (congruent embeddings by sufficient statistics). Any geometric structure that deserves to be "statistical" must be invariant under these morphisms, since sufficient statistics preserve all statistical information.
- **Uniqueness theorem.** On the interior of the finite probability simplex, the *unique* (up to a constant rescaling) Riemannian metric invariant under all Markov morphisms is the [[Fisher information metric]]. This singles out Fisher information as the canonical metric — not merely one convenient choice among many.
- **Invariant connections.** Beyond the metric, Cencov classifies the invariant affine connections, yielding the one-parameter family of $\alpha$-connections (dual to one another) that underlie the dually-flat structure later developed by Amari. This connects directly to [[Alpha-divergence]] and, via the duality, to [[Renyi divergence]].
- **Decision-theoretic grounding.** The geometry is derived from the structure of statistical decision problems rather than imposed, tying the metric to risk, estimation, and optimal inference.

> [!note] Editorial: This note summarizes the well-known content of the monograph from general knowledge of the work; it is not grounded in a local copy of the text. Page-level claims should be checked against the AMS edition before quotation.

## Why the project cites it

The project's information-geometric machinery rests on treating belief states as points on a statistical manifold and moving along that manifold by geometry-aware updates. Cencov's theorem is the formal license for that program:

- **Canonical metric for belief geometry.** The [[Mass as Fisher information]] identification and the [[Natural gradient]] used in [[Variational free energy]] minimization both presuppose that the Fisher metric is *the* right metric on belief space. Cencov supplies the uniqueness argument: invariance under sufficient statistics forces this choice, so the natural-gradient flow is canonical rather than ad hoc.
- **Foundations of information geometry.** The note sits in `cluster/info-geometry` alongside [[ay-2017-information-geometry|ay-2017-information-geometry]] and [[amari-2016-information-geometry-applications|amari-2016-information-geometry-applications]], which build the modern theory (dually-flat manifolds, $\alpha$-geometry) on top of Cencov's invariance result. The project's use of [[Alpha-divergence]] and [[Renyi divergence]] as belief-update objectives inherits its principled standing from the invariant $\alpha$-connections classified here.
- **Gauge-theoretic consistency.** In the [[Gauge-Theoretic Multi-Agent VFE Model]], agents are realized as [[Agents as fibre-bundle sections]] and beliefs are transported by a connection ([[Parallel transport]], [[Holonomy]], [[Gauge transformation]]). Cencov's monotonicity requirement — geometry invariant under statistical morphisms — is the statistical analogue of demanding gauge invariance: physically meaningful structure must not depend on the arbitrary chart/coordinatization of the data. The Fisher metric is the invariant object on which the connection acts.
- **Multi-agent and consensus dynamics.** Because the metric is invariant under coarse-graining by sufficient statistics, it behaves well under the aggregation operations central to [[Multi-agent variational free energy]] and [[Meta-agents and hierarchical emergence]] / [[Renormalization-group flow of beliefs]]: coarse-graining beliefs across scales preserves the canonical geometry, justifying scale-consistent natural-gradient updates.

```bibtex
@book{cencov1982statistical,
  author    = {Cencov, N. N.},
  title     = {Statistical Decision Rules and Optimal Inference},
  series    = {Translations of Mathematical Monographs},
  volume    = {53},
  publisher = {American Mathematical Society},
  address   = {Providence, RI},
  year      = {1982},
  note      = {Translated from the 1972 Russian original (Nauka, Moscow); translation edited by Lev J. Leifman},
  isbn      = {0-8218-4502-0}
}
```
