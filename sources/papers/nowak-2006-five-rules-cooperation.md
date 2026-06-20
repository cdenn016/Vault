---
type: paper
title: "Five Rules for the Evolution of Cooperation"
aliases: ["Nowak 2006 (Five Rules)", "Mechanisms for the evolution of cooperation"]
authors: ["Nowak M. A."]
year: 2006
url: https://doi.org/10.1126/science.1133755
tags: [cluster/social-physics, project/social-physics, field/biology, field/economics, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# Five Rules for the Evolution of Cooperation

> [!info] Citation
> Nowak, M. A. (2006). *Five Rules for the Evolution of Cooperation*. Science 314(5805):1560–1563. DOI: [10.1126/science.1133755](https://doi.org/10.1126/science.1133755).

## TL;DR
Nowak organizes the entire cooperation literature into five mechanisms by which natural selection can favor cooperators over defectors, each summarized by a simple cost-benefit threshold rule. The five are kin selection, direct reciprocity, indirect reciprocity, network (spatial) reciprocity, and group (multilevel) selection. The synthesizing claim is that, although cooperation is costly to the individual and so should be selected against in a well-mixed population, each mechanism introduces a form of assortment or correlated interaction that lets benefits flow preferentially to fellow cooperators, tipping selection toward cooperation when a single inequality is met.

## What it establishes
Each mechanism reduces to a threshold condition relating the cost $c$ of cooperating and the benefit $b$ it confers. Kin selection gives Hamilton's rule $r > c/b$ (relatedness exceeds cost/benefit). Direct reciprocity gives $w > c/b$ (probability of another round). Indirect reciprocity gives $q > c/b$ (probability of knowing reputation). Network reciprocity gives $b/c > k$ (benefit/cost exceeds average degree of the interaction graph). Group selection gives a condition involving group size $n$ and number of groups $m$, roughly $b/c > 1 + n/m$. The unifying message is that a single comparison of benefit to cost, scaled by the mechanism's structural parameter, decides whether cooperation is favored.

## Relevance to this research
This is the standard synthesizing review of the cooperation literature and the natural index entry for the program's evolutionary-cooperation subsection. It is adjacent to the VFE machinery itself, but core for mapping the conceptual landscape, and two of its mechanisms touch the program directly: network reciprocity ($b/c > k$) treats agents as nodes on a coupling graph, mirroring how the program couples belief-carrying agents by gauge-transported KL over a graph; and group selection prefigures the program's meta-agent / hierarchical coarse-graining picture in which clusters of agents become higher-scale agents. See [[Evolutionary game theory and cooperation]], [[Multi-agent variational free energy]], and [[Community detection and modularity]].

## Cross-links
- Concept: [[Evolutionary game theory and cooperation]]
- Related sources: [[axelrod-hamilton-1981-evolution-of-cooperation]], [[ohtsuki-hauert-lieberman-nowak-2006-simple-rule-graphs]], [[nowak-sigmund-2005-indirect-reciprocity]]

## BibTeX
```bibtex
@article{nowak2006five,
  author  = {Nowak, Martin A.},
  title   = {Five Rules for the Evolution of Cooperation},
  journal = {Science},
  volume  = {314},
  number  = {5805},
  pages   = {1560--1563},
  year    = {2006},
  doi     = {10.1126/science.1133755}
}
```
