---
type: reference
title: "Relevance in the Renormalization Group and in Information Theory"
aliases: ["gordon2021relevance"]
authors: ["Amit Gordon", "Aditya Banerjee", "Maciej Koch-Janusz", "Zohar Ringel"]
year: 2021
venue: "Physical Review Letters"
doi: "10.1103/PhysRevLett.126.240601"
url: "https://doi.org/10.1103/PhysRevLett.126.240601"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/physics, field/cs-ml]
created: 2026-11-10
updated: 2026-11-10
---
# Relevance in the Renormalization Group and in Information Theory

> [!info] Citation
> Gordon, A., Banerjee, A., Koch-Janusz, M., Ringel, Z. (2021). *Relevance in the Renormalization Group and in Information Theory*. Physical Review Letters, 126, 240601. [DOI](https://doi.org/10.1103/PhysRevLett.126.240601), [arXiv](https://arxiv.org/abs/2012.01447)

[Local PDF](../pdfs/gordon-2021-relevance-renormalization-group.pdf), 16 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and manuscript reading record.

## TL;DR

The paper establishes an equivalence between the field-theoretic notion of relevance in the renormalization group and an information-theoretic notion of relevance defined through the information bottleneck. For systems described by a field theory, the degrees of freedom kept by bottleneck compression correspond to operators of lowest scaling dimension.

## Problem & setting

The introduction poses the problem of extracting relevant degrees of freedom from complex systems and the interpretability gap between machine-learned features and the objects of physical theory. Information-theoretic relevance is defined by correlation with an auxiliary relevance variable, while renormalization-group relevance is defined by behavior of operators under scale transformations.

## Method

The authors derive the correspondence analytically for field theories, check the predictions numerically, and study how the bottleneck solutions depend on the symmetries of the data. They also relate a real-space mutual information method to a limit of the bottleneck problem.

## Key results

The claimed results are the analytic equivalence and its numerical confirmation, framed by the authors as a dictionary between two theoretical toolboxes.

## Relevance to this research

The manuscript cites the paper twice, as a scope statement for information-theoretic renormalization and as a result it knows from the abstract that would tie its conjecture on environments to the relevant variables of its renormalization section. It treats such results as conditional and not yet extended to controlled adaptive processes. The paper relates to [[Information bottleneck]], [[Renormalization group flow]] and [[Coarse Graining]].

## Cross-links

[[Collective agents literature map]]; [[Information bottleneck]]; [[Renormalization group flow]]; [[Coarse Graining]].

## BibTeX

```bibtex
@article{gordon2021relevance,
  author  = {Gordon, Amit and Banerjee, Aditya and Koch-Janusz, Maciej and Ringel, Zohar},
  title   = {Relevance in the Renormalization Group and in Information Theory},
  journal = {Physical Review Letters},
  volume  = {126},
  number  = {24},
  pages   = {240601},
  year    = {2021},
  doi     = {10.1103/PhysRevLett.126.240601}
}
```
