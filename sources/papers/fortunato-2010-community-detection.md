---
type: paper
title: "Community Detection in Graphs"
aliases:
  - "Fortunato 2010"
  - "Fortunato (2010) Community Detection review"
authors:
  - Santo Fortunato
year: 2010
arxiv: 0906.0612
tags:
  - cluster/social-physics
  - cluster/multi-agent
  - project/multi-agent
  - project/social-physics
  - field/cs-ml
  - field/physics
  - cluster/social-physics/networks-and-contagion
created: 2026-06-19
updated: 2026-06-19
---

# Community Detection in Graphs

> [!info] Citation
> Santo Fortunato (2010). "Community detection in graphs." *Physics Reports* **486**(3–5), 75–174. DOI: [10.1016/j.physrep.2009.11.002](https://doi.org/10.1016/j.physrep.2009.11.002). Preprint: [arXiv:0906.0612](https://arxiv.org/abs/0906.0612).

## TL;DR

The definitive review of community-detection methods — modularity maximization, spectral and hierarchical clustering, statistical-inference (stochastic block model) approaches, and dynamic/flow-based methods — with a careful treatment of their failure modes, above all the *resolution limit* of modularity (its blindness to communities below a size set by the total number of edges). It is the reference that catalogs the pitfalls the project must respect when its meta-agent clustering uses modularity-style criteria.

## Relevance to this research

The project's [[Meta-agents and hierarchical emergence|meta-agent formation]] detects coherent agent clusters to coarse-grain; whatever criterion it uses inherits the strengths and the documented hazards of community detection. Fortunato's review is the place to check those hazards — the modularity resolution limit means a global $Q$-maximization can merge small genuine clusters or miss them entirely, which directly bears on whether the project's culture-closure clustering produces the *right* coarse-graining blocks at each scale of [[Renormalization-group flow of beliefs]]. It backs the new [[Community detection and modularity]] page and extends [[newman-girvan-2004-community-structure]] with the caveats. Manuscript thread: [[participatory-it-from-bit]].

## Cross-links

- Concept: [[Community detection and modularity]], [[Meta-agents and hierarchical emergence]].
- Sources: [[newman-girvan-2004-community-structure]], [[fiedler-1973-algebraic-connectivity]].
- Manuscript: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@article{fortunato2010community,
  author  = {Fortunato, Santo},
  title   = {Community detection in graphs},
  journal = {Physics Reports},
  volume  = {486},
  number  = {3--5},
  pages   = {75--174},
  year    = {2010},
  doi     = {10.1016/j.physrep.2009.11.002},
  eprint  = {0906.0612},
  archivePrefix = {arXiv}
}
```
