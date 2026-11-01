---
type: "paper"
title: "How humans solve the frame problem"
aliases: ["How humans solve the frame problem (Fields 2013)"]
authors: ["Chris Fields"]
year: 2013
url: "https://chrisfieldsresearch.com/frame-how-pre.pdf"
tags: ["cluster/participatory", "cluster/participatory/philosophy-of-mind", "project/multi-agent", "field/cs-ml", "field/psychology", "field/neuroscience"]
created: "2026-11-01"
updated: "2026-11-01"
doi: "10.1080/0952813X.2012.741624"
---

# How humans solve the frame problem

> [!info] Citation
> Fields, C. (2013) How humans solve the frame problem. Journal of Experimental and Theoretical Artificial Intelligence 25: 441-456 (doi: 10.1080/0952813X.2012.741624).

Local PDF: [PDF](../pdfs/fields-2013-how-humans-solve-the-frame-problem.pdf)

## Summary

Fields challenges formulations of the frame problem that assume objects can be re-identified without computational work. Deciding which properties an action changes already requires deciding which current objects continue previously encountered individuals. The paper reviews visual categorization, episodic recall, and causal reasoning, then adopts the proposal that premotor systems construct fictive causal histories connecting remembered and current contexts.

Under that proposal, objects are handled as unfamiliar instances, familiar individuals whose relevant properties appear unchanged, or familiar individuals requiring a nontrivial history of change. Imagining an action's consequences uses the same constrained representations that support re-identification. Fields therefore argues that the frame problem and object re-identification are equivalent for the human architecture if the causal-history model is correct. The account is heuristic and resource-limited: attention, category knowledge, analogy, and memory biases restrict which possibilities can be considered. The paper reports no new experiment and does not give a general-purpose algorithm that solves unrestricted frame problems. Its equivalence claim is explicitly conditional in the conclusion.

## Relevance to this research

For [[Multi-agent variational free energy]], this highlights a modeling obligation when persistent agents, records, or objects are carried between updates: identity is part of the retained state and inference process. It motivates explicit continuity rules rather than assuming that a label supplies them. The proposed human mechanism is not a proof of variational stationarity or autonomous hierarchical formation.

## Reading and version

PDF pp. 1-3, 5-6, and 10-11: task definition, object-token and memory mechanisms, proposed solution, and conditional conclusion. Author manuscript marked in press, August 2012; journal publication is 2013, volume 25, 441-456.

## BibTeX

```bibtex
@article{fields-2013-how-humans-solve-the-frame-problem,
  author = {Fields, Chris},
  title = {How humans solve the frame problem},
  year = {2013},
  journal = {Journal of Experimental and Theoretical Artificial Intelligence},
  volume = {25},
  pages = {441--456},
  doi = {10.1080/0952813X.2012.741624},
  url = {https://chrisfieldsresearch.com/frame-how-pre.pdf}
}
```
