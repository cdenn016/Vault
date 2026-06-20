---
type: paper
title: "The Mathematical Structure of Integrated Information Theory"
aliases:
  - "Kleiner & Tull 2021"
  - "Kleiner-Tull (2021) Mathematical Structure of IIT"
authors:
  - Johannes Kleiner
  - Sean Tull
year: 2021
arxiv: "2002.07655"
url: https://arxiv.org/abs/2002.07655
tags:
  - cluster/participatory
  - project/multi-agent
  - field/neuroscience
  - field/mathematics
  - field/philosophy
  - cluster/participatory/consciousness
created: 2026-06-19
updated: 2026-06-19
---

# The Mathematical Structure of Integrated Information Theory

> [!info] Citation
> Kleiner, Johannes & Tull, Sean (2021). "The Mathematical Structure of Integrated Information Theory." *Frontiers in Applied Mathematics and Statistics*, 6, 602973. DOI: [10.3389/fams.2020.602973](https://doi.org/10.3389/fams.2020.602973). Preprint: [arXiv:2002.07655](https://arxiv.org/abs/2002.07655).

## TL;DR

Kleiner and Tull give the first fully explicit mathematical reconstruction of Integrated Information Theory (IIT 3.0), stripping the theory's intricate algorithm down to its essential mathematical objects and separating them from auxiliary computational choices. The payoff is a *generalized* IIT defined axiomatically, of which Tononi et al.'s IIT 3.0 and the quantum IIT of Zanardi, Tomka, and Venuti appear as special cases. The paper turns IIT from a procedurally specified algorithm into a structure amenable to theorem-proving and formal critique.

## Problem & setting

IIT aims to specify both the *quantity* and the *quality* of consciousness for a physical system in a state, via integrated information $\Phi$ and the associated cause–effect structure. But the canonical presentations interleave the core theoretical commitments with implementation detail — particular distance measures, partition schemes, and search procedures — making it hard to see which choices are load-bearing and which are conventional. Without a clean statement of the structure, it is difficult to prove general results, compare variants, or assess the theory's internal consistency.

## Method

The authors formalize the IIT pipeline as a sequence of well-defined mathematical maps: from a physical system and a state, to a repertoire of cause and effect probability distributions, to mechanism-level "concepts" (maximally irreducible cause–effect distinctions found by minimizing over partitions), to the system-level *cause–effect structure* (the conceptual structure or "Q-shape"), and finally to $\Phi^{\max}$ obtained by the exclusion postulate's maximization over candidate substrates and grains. Each step is given an abstract signature so that the distance measure, the space of mechanisms, and the partition lattice become parameters rather than fixed ingredients. This yields the generalized IIT and exposes exactly where the theory's irreducibility and exclusion operations live mathematically.

## Key results

The paper delivers an axiomatic, presentation-independent definition of IIT; demonstrates that classical IIT 3.0 and quantum IIT are instances of one generalized scheme; and isolates the formal core (cause–effect repertoires, integrated information as irreducibility under partition, exclusion as maximization) from incidental modeling choices. This provides the rigorous scaffolding needed for subsequent mathematical work on consciousness, including comparisons with other structural theories and analyses of whether the $\Phi$-structure is well-defined and unique.

## Relevance to this research

This is the formal counterpart of the manuscript [[participatory-it-from-bit]]'s contrast with IIT. Where PIFB engages IIT conceptually (via [[tononi-2016-iit]]) as the strongest existing program making information *intrinsic* to a substrate, Kleiner and Tull supply the precise mathematical object — the $\Phi$-structure as an irreducibility functional over a partition lattice — against which the project can state its differences exactly rather than informally. The relevance to PIFB's [[Mathematical consciousness science]] thread is direct: the manuscript's claim that conscious character is fixed by *relational/structural* content needs a rigorous notion of "structure," and IIT's conceptual structure is the canonical worked example of such a thing. The contrast is instructive for the gauge-theoretic [[Multi-agent variational free energy]] model: IIT's exclusion/integration maximization parallels the project's account of [[Meta-agents and hierarchical emergence]] and the [[Ouroboros multi-scale dynamics]], where a coarse-grained collective is a genuine higher-level unit only when irreducible to independent parts — but the project grounds emergence in [[Variational free energy]] and [[Fisher information metric]] geometry rather than in $\Phi$. Having the formalized IIT on hand lets the manuscript draw the line between an intrinsic-information identity theory and a participatory, frame-relative one (cf. [[tsuchiya-saigo-2016-category-theory-iit]] for the category-theoretic sibling).

## Cross-links

- Concepts: [[Mathematical consciousness science]], [[Participatory realism (it from bit)]], [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]], [[Fisher information metric]]
- Related sources: [[tononi-2016-iit]], [[tsuchiya-saigo-2016-category-theory-iit]], [[seth-2021-being-you]], [[wheeler-1990-it-from-bit]]
- Manuscript: [[participatory-it-from-bit]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

```bibtex
@article{kleiner2021mathematicalstructureiit,
  author  = {Kleiner, Johannes and Tull, Sean},
  title   = {The Mathematical Structure of Integrated Information Theory},
  journal = {Frontiers in Applied Mathematics and Statistics},
  year    = {2021},
  volume  = {6},
  pages   = {602973},
  doi     = {10.3389/fams.2020.602973},
  eprint  = {2002.07655},
  archivePrefix = {arXiv},
  primaryClass  = {q-bio.NC}
}
```
