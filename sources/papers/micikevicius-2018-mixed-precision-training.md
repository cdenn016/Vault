---
type: paper
title: "Mixed Precision Training"
aliases: ["Micikevicius 2018", "Mixed Precision Training"]
authors: ["Paulius Micikevicius", "Sharan Narang", "Jonah Alben", "Gregory Diamos", "Erich Elsen", "David Garcia", "Boris Ginsburg", "Michael Houston", "Oleksii Kuchaiev", "Ganesh Venkatesh", "Hao Wu"]
year: 2018
arxiv: 1710.03740
url: https://arxiv.org/abs/1710.03740
tags: [cluster/attention, project/transformer, field/cs-ml]
created: 2026-06-20
updated: 2026-06-20
---

# Mixed Precision Training

> [!info] Citation
> Paulius Micikevicius, Sharan Narang, Jonah Alben, Gregory Diamos, Erich Elsen, David Garcia, Boris Ginsburg, Michael Houston, Oleksii Kuchaiev, Ganesh Venkatesh, Hao Wu (2018). *Mixed Precision Training*. ICLR 2018; arXiv:1710.03740. https://arxiv.org/abs/1710.03740

## TL;DR

Trains deep networks with FP16 weights/activations/gradients while keeping an FP32 master copy of weights and using loss scaling to preserve small-magnitude gradients, halving memory and accelerating training with no accuracy loss.

## Relevance to this research

FP16/FP32 mixed-precision training; numerical-precision context (the model is float32 throughout).

## Cross-links

- Theme: [[Transformer interpretability and scaling]]
- Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@inproceedings{micikevicius2018mixed,
  author={Micikevicius, Paulius and Narang, Sharan and Alben, Jonah and others},
  title={Mixed Precision Training},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2018}
}
```
