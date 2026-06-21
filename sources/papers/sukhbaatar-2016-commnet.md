---
type: paper
title: "Learning Multiagent Communication with Backpropagation"
aliases:
  - "sukhbaatar-2016-commnet"
  - "sukhbaatar2016learning"
  - "CommNet"
  - "Sukhbaatar 2016"
authors:
  - "Sukhbaatar, S."
  - "Szlam, A."
  - "Fergus, R."
year: 2016
url: https://arxiv.org/abs/1605.07736
venue: "NeurIPS 2016"
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/cs-ml
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Learning Multiagent Communication with Backpropagation

> [!info] Citation
> Sukhbaatar, S., Szlam, A., Fergus, R. (2016). "Learning Multiagent Communication with Backpropagation." NeurIPS 2016. https://arxiv.org/abs/1605.07736

## TL;DR
Introduces CommNet, a neural model in which multiple cooperating agents learn a continuous communication protocol end-to-end via backpropagation. At each step agents broadcast hidden-state messages that are averaged and fed back as input, letting a single differentiable controller coordinate a varying number of agents on cooperative tasks.

## Relevance to this research
An early differentiable multi-agent communication architecture relevant to the MAgent multi-agent VFE model: its mean-pooled message passing among agents prefigures the coupled belief-exchange dynamics that the gauge-theoretic multi-agent framework formalizes through shared latent state.

## Cross-links
[[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX
```bibtex
@inproceedings{sukhbaatar2016learning,
  title={Learning Multiagent Communication with Backpropagation},
  author={Sukhbaatar, Sainbayar and Szlam, Arthur and Fergus, Rob},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2016}
}
```
