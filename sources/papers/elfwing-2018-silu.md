---
type: paper
title: "Sigmoid-Weighted Linear Units for Neural Network Function Approximation in Reinforcement Learning"
aliases:
  - Elfwing 2018
  - elfwing2018
  - SiLU
authors:
  - Elfwing, Stefan
  - Uchibe, Eiji
  - Doya, Kenji
year: 2018
arxiv: "1702.03118"
url: https://arxiv.org/abs/1702.03118
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
created: 2026-09-27
---

# Sigmoid-Weighted Linear Units for Neural Network Function Approximation in Reinforcement Learning

> [!info] Citation
> Elfwing, S., Uchibe, E., & Doya, K. (2018). *Sigmoid-weighted linear units for neural network function approximation in reinforcement learning*. Neural Networks, 107, 3–11. arXiv:1702.03118.

## TL;DR
The paper introduces the sigmoid-weighted linear unit, $\mathrm{SiLU}(x)=x\,\sigma(x)$ ("the sigmoid function multiplied by its input"), and its derivative dSiLU as activations, and shows that on-policy learning with eligibility traces using them can match or exceed DQN on Atari.

## Relevance to this research
The identity $x\,\sigma(x)=x\cdot e^{x}/(e^{x}+e^{0})$ shows that a SiLU unit is a softmax competition over two options with logits $(x,0)$ and values $(x,0)$; GELU is close to $x\,\sigma(1.702x)$ ([[hendrycks2016gaussian]]). This is the bridge in [[Template routing]] from pointwise activations to Gibbs routing: a GELU/SiLU MLP runs $M$ independent two-way competitions, while template routing runs one $M$-way competition among Gaussian templates. The same unit was later found by search as Swish ([[ramachandran2018searching]]).

## Cross-links
- Concepts: [[Activation Functions]], [[Gating Mechanisms]], [[Softmax]]
- Methods: [[Template routing]]
- Related sources: [[hendrycks2016gaussian]], [[ramachandran2018searching]], [[dennis-2026-template-routing]]

## BibTeX
```bibtex
@article{elfwing2018sigmoid,
  author  = {Elfwing, Stefan and Uchibe, Eiji and Doya, Kenji},
  title   = {Sigmoid-weighted linear units for neural network function approximation in reinforcement learning},
  journal = {Neural Networks},
  volume  = {107},
  pages   = {3--11},
  year    = {2018}
}
```
