---
type: paper
title: "Deep Residual Learning for Image Recognition"
aliases:
  - "he2016resnet"
  - "Deep Residual Learning for Image Recognition"
  - "ResNet"
  - "He 2016"
  - "he-2016-resnet"
authors:
  - "He, Kaiming"
  - "Zhang, Xiangyu"
  - "Ren, Shaoqing"
  - "Sun, Jian"
year: 2016
url: https://arxiv.org/abs/1512.03385
venue: "CVPR"
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Deep Residual Learning for Image Recognition

> [!info] Citation
> He, Kaiming, Zhang, Xiangyu, Ren, Shaoqing, Sun, Jian (2016). "Deep Residual Learning for Image Recognition." CVPR. https://arxiv.org/abs/1512.03385

## TL;DR
Introduces residual networks (ResNets), in which each block learns a residual function F(x) added to its input x via an identity skip connection, enabling training of networks hundreds of layers deep. This solved the degradation problem and became foundational for deep architectures including Transformers.

## Relevance to this research
The canonical reference for residual connections, which the program's deep belief-refinement stacks rely on; provides the empirical and conceptual basis for treating depth as iterated identity-plus-correction updates.

## Cross-links
[[Residual Connections]], [[Deep Networks]]

## BibTeX
```bibtex
@inproceedings{he2016resnet,
  title={Deep Residual Learning for Image Recognition},
  author={He, Kaiming and Zhang, Xiangyu and Ren, Shaoqing and Sun, Jian},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages={770--778},
  year={2016},
  note={arXiv:1512.03385}
}
```
