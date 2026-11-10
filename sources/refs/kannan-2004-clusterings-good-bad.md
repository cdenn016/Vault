---
type: reference
title: "On clusterings: Good, bad and spectral"
aliases: ["kannan2004clusterings"]
authors: ["Ravi Kannan", "Santosh Vempala", "Adrian Vetta"]
year: 2004
venue: "Journal of the ACM"
doi: "10.1145/990308.990313"
url: "https://doi.org/10.1145/990308.990313"
tags: [cluster/multi-agent, project/multi-agent, field/cs-ml, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---

# On clusterings: Good, bad and spectral

> [!info] Citation
> Kannan, R., Vempala, S., Vetta, A. (2004). *On clusterings: Good, bad and spectral*. Journal of the ACM, 51(3), 497-515. [DOI](https://doi.org/10.1145/990308.990313)

No local copy: no open-access file passed validation on November 10, 2026. Reading basis: abstract and manuscript reading record.

## TL;DR

The paper develops a bicriteria measure of clustering quality and analyzes a popular spectral clustering algorithm, with worst-case guarantees for one variant.

## Problem & setting

Assessing the quality of a clustering with a measure that avoids drawbacks of existing ones.

## Key results

Per the abstract, a simple recursive heuristic has poly-logarithmic worst-case guarantees under the new measure. The main result is the analysis of a spectral algorithm: one variant has effective worst-case guarantees, and another finds a good clustering if one exists.

## Relevance to this research

The manuscript cites it for the bicriteria notion of a clustering, and describes its own contrast criterion for collectives as the spectral form, written for precision-weighted message passing, of that notion and of nearly decomposable systems. The manuscript's record says only the abstract was read. See [[Community detection and modularity]], [[Spectral graph theory]] and [[Markov Blanket]].

## Cross-links

[[Collective agents literature map]]; [[Community detection and modularity]]; [[Spectral graph theory]]; [[Markov Blanket]].

## BibTeX

```bibtex
@article{kannan2004clusterings,
  author  = {Kannan, Ravi and Vempala, Santosh and Vetta, Adrian},
  title   = {On clusterings: Good, bad and spectral},
  journal = {Journal of the ACM},
  volume  = {51},
  number  = {3},
  pages   = {497--515},
  year    = {2004},
  doi     = {10.1145/990308.990313}
}
```
