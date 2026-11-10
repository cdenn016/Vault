---
type: reference
title: "Characterization, Stability and Convergence of Hierarchical Clustering Methods"
aliases: ["carlsson2010characterization"]
authors: ["Gunnar Carlsson", "Facundo Mémoli"]
year: 2010
venue: "Journal of Machine Learning Research"
tags: [cluster/multi-agent, project/multi-agent, field/mathematics, field/statistics, field/cs-ml]
created: 2026-11-10
updated: 2026-11-10
---
# Characterization, Stability and Convergence of Hierarchical Clustering Methods

> [!info] Citation
> Carlsson, G., Mémoli, F. (2010). *Characterization, Stability and Convergence of Hierarchical Clustering Methods*. Journal of Machine Learning Research, 11(47), 1425-1470.

No local copy: no open-access file passed validation on November 10, 2026. Reading basis: manuscript reading record.

## TL;DR

A paper on hierarchical clustering that treats dendrograms as ultrametrics and states an existence and uniqueness theorem, according to the abstract as read when the manuscript was written. The record does not name the method the theorem singles out.

## Relevance to this research

The collective-agents manuscript uses single-linkage clustering to form collectives and cites this paper for the fact that the dendrogram of single linkage is an ultrametric. That fact makes the nesting of collectives at successive thresholds automatic. The reference supports the coarse-graining step in which agents are grouped by a contrast threshold and the groups nest as the threshold rises, see [[Coarse Graining]] and [[Meta-agents and hierarchical emergence]]. The manuscript's reading record covers only the abstract, so no statement here goes beyond it. A related grouping notion is in [[Community detection and modularity]].

## Cross-links

[[Collective agents literature map]]; [[Coarse Graining]]; [[Meta-agents and hierarchical emergence]]; [[Community detection and modularity]].

## BibTeX

```bibtex
@article{carlsson2010characterization,
  author  = {Carlsson, Gunnar and M{\'e}moli, Facundo},
  title   = {Characterization, Stability and Convergence of Hierarchical Clustering Methods},
  journal = {Journal of Machine Learning Research},
  volume  = {11},
  number  = {47},
  pages   = {1425--1470},
  year    = {2010}
}
```
