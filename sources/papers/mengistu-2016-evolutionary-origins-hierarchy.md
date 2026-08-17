---
type: paper
title: "The Evolutionary Origins of Hierarchy"
aliases:
  - "Mengistu et al. 2016"
  - "hierarchy from connection costs"
authors:
  - Mengistu H.
  - Huizinga J.
  - Mouret J.-B.
  - Clune J.
year: 2016
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/cs-ml
  - field/biology
created: 2026-08-17
updated: 2026-08-17
---

# The Evolutionary Origins of Hierarchy

> [!info] Citation
> H. Mengistu, J. Huizinga, J.-B. Mouret, J. Clune (2016). "The Evolutionary Origins of
> Hierarchy." *PLoS Computational Biology* **12**(6), e1004829.
> DOI: [10.1371/journal.pcbi.1004829](https://doi.org/10.1371/journal.pcbi.1004829).

## TL;DR

In evolved networks, hierarchy does not emerge merely because the task is hierarchical: without
a cost on connections, evolved networks stay non-hierarchical even on hierarchical tasks. Adding
a connection cost makes networks evolve to be both modular and hierarchical, with higher
performance and adaptability — the same pressure that produces modularity produces hierarchy.

## What it establishes

A causal simulation result: connection costs are the driver of hierarchical organization in
evolved networks; hierarchical task structure alone is insufficient.

## Relevance to this research

The gauge-VFE program's block formation is priced, not free — the retention charge, the Wilson
term, and the partition prior all charge for structure — and this paper is the external evidence
that pricing is exactly what makes hierarchy emerge rather than an obstacle to it. It also
suggests a lab-testable analog: vary the declared costs and measure whether the partition
posterior's preferred hierarchies sharpen or dissolve. See
[[Meta-agents and hierarchical emergence]] and
[[Staged hierarchy formation and RG composability]].

## BibTeX

```bibtex
@article{mengistu2016hierarchy,
  author  = {Mengistu, Henok and Huizinga, Joost and Mouret, Jean-Baptiste and Clune, Jeff},
  title   = {The Evolutionary Origins of Hierarchy},
  journal = {PLoS Computational Biology},
  volume  = {12},
  number  = {6},
  pages   = {e1004829},
  year    = {2016},
  doi     = {10.1371/journal.pcbi.1004829}
}
```
