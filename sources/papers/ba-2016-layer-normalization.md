---
type: paper
title: "Layer Normalization"
aliases: ["Ba 2016", "Layer Normalization"]
authors: ["Jimmy Lei Ba", "Jamie Ryan Kiros", "Geoffrey E. Hinton"]
year: 2016
arxiv: 1607.06450
url: https://arxiv.org/abs/1607.06450
tags: [cluster/attention, project/transformer, field/cs-ml]
created: 2026-06-20
updated: 2026-06-20
---

# Layer Normalization

> [!info] Citation
> Jimmy Lei Ba, Jamie Ryan Kiros, Geoffrey E. Hinton (2016). *Layer Normalization*. arXiv:1607.06450. https://arxiv.org/abs/1607.06450

## TL;DR

Introduces layer normalization, which normalizes the summed inputs to each neuron across the feature dimension within a single example, removing the batch-size dependence of batch normalization and working unchanged at test time and for recurrent models.

## Relevance to this research

Introduces layer normalization; the normalization primitive whose VFE-native analogue the model's precision-weighting plays.

## Cross-links

- Concepts: [[Mechanistic interpretability of attention]]
- Theme: [[Attention mechanisms — theory and positional structure]]
- Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@article{ba2016layernorm,
  author={Ba, Jimmy Lei and Kiros, Jamie Ryan and Hinton, Geoffrey E.},
  title={Layer Normalization},
  journal={arXiv preprint arXiv:1607.06450},
  year={2016}
}
```
