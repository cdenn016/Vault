---
type: paper
title: "Distributional Clustering of English Words"
aliases:
  - "pereira-1993-distributional-clustering"
  - "Distributional Clustering of English Words"
  - "Pereira Tishby Lee 1993"
  - "pereira1993distributionalclustering"
authors:
  - "Pereira, Fernando"
  - "Tishby, Naftali"
  - "Lee, Lillian"
year: 1993
url: https://aclanthology.org/P93-1024/
venue: "ACL (31st Annual Meeting of the Association for Computational Linguistics)"
tags:
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Distributional Clustering of English Words

> [!info] Citation
> Pereira, Fernando, Tishby, Naftali, Lee, Lillian (1993). "Distributional Clustering of English Words." ACL (31st Annual Meeting of the Association for Computational Linguistics). https://aclanthology.org/P93-1024/

## TL;DR
Clusters nouns by the distributions of verbs that take them as objects, using a deterministic-annealing / soft-clustering procedure that minimizes a relative-entropy distortion between a word's conditional distribution and its cluster centroid. It is the direct precursor of the Information Bottleneck method: the same KL-distortion soft-clustering machinery, applied to co-occurrence statistics, that IB later generalized.

## Relevance to this research
The historical and methodological ancestor of the Information Bottleneck used throughout the program's compression-based view of belief representation; cited by the agglomerative-IB source as the origin of distributional/soft KL clustering.

## Cross-links
[[Information bottleneck]], [[Agglomerative information bottleneck]]

## BibTeX
```bibtex
@inproceedings{pereira1993distributionalclustering,
  title={Distributional Clustering of English Words},
  author={Pereira, Fernando and Tishby, Naftali and Lee, Lillian},
  booktitle={Proceedings of the 31st Annual Meeting of the Association for Computational Linguistics (ACL)},
  pages={183--190},
  year={1993}
}
```
