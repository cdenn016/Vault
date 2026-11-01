---
type: "paper"
title: "Meta-learning goes hand-in-hand with metacognition"
aliases: ["Meta-learning goes hand-in-hand with metacognition (Fields source, 2024)"]
authors: ["Fields, C.", "Glazebrook, J. F."]
year: 2024
doi: "10.1017/S0140525X24000256"
url: "https://chrisfieldsresearch.com/Binz-commentary-Fields-Glazebrook.pdf"
tags: ["cluster/vfe", "cluster/multi-agent", "project/multi-agent", "project/transformer", "field/psychology", "field/cs-ml", "field/neuroscience"]
created: "2026-11-01"
updated: "2026-11-01"
---

# Meta-learning goes hand-in-hand with metacognition

> [!info] Citation
> Fields, C. and Glazebrook, J. F. (2024) Meta-learning goes hand-in-hand with metacognition. Behavioral and Brain Sciences 47: e151 (doi: 10.1017/S0140525X24000256).

[Local full text](../pdfs/fields-2024-meta-learning-goes-hand-in-hand-with-metacognition.pdf). [Primary source](https://chrisfieldsresearch.com/Binz-commentary-Fields-Glazebrook.pdf). [Publication record](https://doi.org/10.1017/S0140525X24000256).

## Reading basis

Author manuscript of the 2024 Behavioral and Brain Sciences commentary; the manuscript title writes Metalearning without a hyphen. Targeted reading of PDF pages 1, 2, covering the opening account and selected construction or discussion passages. Page numbers refer to the stored PDF. This ingestion is not a complete proof audit or an independent replication.

## Contribution and scope

Fields and Glazebrook examine the architectural assumptions behind meta-learned models of cognition. An inner process learns a task, while an outer process changes how the inner process learns. Treating this outer process as a component of a larger system raises a concrete question: what information constitutes its task environment, and how does object-level feedback train it? The authors point out that invoking another unrestricted meta-learning loop cannot by itself explain this feedback without an infinite regress. They connect differences between learning timescales with metacognition, memory, attention, and active inference. The commentary suggests biochemical and other experimentally accessible systems as settings in which these relations could be investigated. Its broad expectation that meta-learning is widespread in physical systems is a theoretical extension of the authors' framework, rather than a new comparative experiment or an algorithmic result established in the commentary.

## Relevance to this research

This sharpens the design question behind [[Meta-agents and hierarchical emergence]]: a higher-level agent needs identifiable inputs, retained state, and an update rule acting on lower-level processes. Labeling a variable a metaparameter does not explain how it is learned. For [[VFE Transformer Program]], the useful distinction is between adapting a prediction and adapting the rule that produces predictions, with each timescale and feedback source stated explicitly.

## BibTeX

```bibtex
@article{fields-2024-meta-learning-goes-hand-in-hand-with-metacognition,
  author = {Fields, C. and Glazebrook, J. F.},
  title = {Meta-learning goes hand-in-hand with metacognition},
  year = {2024},
  journal = {Behavioral and Brain Sciences},
  volume = {47},
  pages = {e151},
  doi = {10.1017/S0140525X24000256},
  url = {https://chrisfieldsresearch.com/Binz-commentary-Fields-Glazebrook.pdf}
}
```
