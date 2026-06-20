---
type: paper
title: "Majority Rule, Hierarchical Structures, and Democratic Totalitarianism: A Statistical Approach"
aliases: ["Galam 1986", "Galam hierarchical majority-rule model"]
authors: ["Galam S."]
year: 1986
url: https://doi.org/10.1016/0022-2496(86)90019-2
tags: [cluster/social-physics, project/social-physics, field/physics, field/sociology, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Majority Rule, Hierarchical Structures, and Democratic Totalitarianism: A Statistical Approach

> [!info] Citation
> Galam, S. (1986). *Majority Rule, Hierarchical Structures, and Democratic Totalitarianism: A Statistical Approach*. Journal of Mathematical Psychology 30(4), 426-434. DOI: [10.1016/0022-2496(86)90019-2](https://doi.org/10.1016/0022-2496(86)90019-2).

## TL;DR
Galam analyzes a hierarchical voting structure in which individuals at the bottom level are organized into small groups, each group elects a representative by local majority rule, those representatives form the next level's groups, and the process repeats up through several tiers. Treating the bottom-level support for a given position as a probability, he computes how that support transforms level by level and finds a stark amplification effect: a global majority slightly above one-half is driven toward total control of the top of the hierarchy, while a sizable minority can be entirely shut out. The disquieting conclusion is that nominally democratic, bottom-up majority aggregation can entrench a fixed group's dominance — a "democratic totalitarianism."

## What it establishes
Let $p$ be the probability that a randomly chosen individual supports position A, and let groups of size $r$ elect a representative by majority. The probability that the elected representative supports A is the majority-vote map
$$ p' = P_r(p) = \sum_{k > r/2} \binom{r}{k} p^k (1-p)^{r-k}, $$
which is then iterated across hierarchy levels. This map has unstable interior fixed points (a critical threshold $p_c$, e.g. $p_c \approx 0.77$ for groups of three with tie-breaking bias) and stable fixed points at $0$ and $1$. Iterating drives any starting majority above threshold to certain victory at the top and any below to extinction, with the threshold displaced from one-half whenever ties are resolved in favour of an incumbent group. The level-by-level iteration of $P_r$ is, structurally, a real-space renormalization transformation on the support probability.

## Relevance to this research
This is the original Galam hierarchical majority-rule model, and its repeated local-majority coarse-graining is a discrete precursor to the renormalization-group coarse-graining of beliefs and the meta-agent formation the program uses. Each tier plays the role of a scale in the ouroboros tower: a group of constituent agents is pooled into a single representative whose state feeds the next coarser scale, exactly the upward pass that builds meta-agents from clusters. Galam's majority map $P_r$ is the binary, hard-threshold caricature of the program's gauge-covariant coherence-weighted pooling, and the canonical agreement model the overdamped limit should recover. The RG reading of the level iteration directly motivates the renormalization-group-flow-of-beliefs strand. See [[Renormalization-group flow of beliefs]], [[Sociophysics]], [[Community detection and modularity]].

## Cross-links
- Concept: [[Discrete spin and majority-rule models of opinion]]
- Related sources: [[galam-2002-minority-opinion-spreading]], [[galam-gefen-shapir-1982-sociophysics-strike]]

## BibTeX
```bibtex
@article{galam1986majority,
  author  = {Galam, Serge},
  title   = {Majority Rule, Hierarchical Structures, and Democratic Totalitarianism: A Statistical Approach},
  journal = {Journal of Mathematical Psychology},
  year    = {1986},
  volume  = {30},
  number  = {4},
  pages   = {426--434},
  doi     = {10.1016/0022-2496(86)90019-2}
}
```
