---
type: reference
title: "TarMAC: Targeted Multi-Agent Communication"
aliases:
  - "Das et al. 2019 TarMAC"
  - "TarMAC: Targeted Multi-Agent Communication"
  - "Das2019TarMAC"
authors:
  - Abhishek Das
  - Théophile Gervet
  - Joshua Romoff
  - Dhruv Batra
  - Devi Parikh
  - Michael Rabbat
  - Joelle Pineau
year: 2019
arxiv: "1810.11187"
url: https://arxiv.org/abs/1810.11187
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
created: 2026-09-23
updated: 2026-09-23
---

# TarMAC: Targeted Multi-Agent Communication

> [!info] Citation
> Abhishek Das, Théophile Gervet, Joshua Romoff, Dhruv Batra, Devi Parikh, Michael Rabbat, Joelle Pineau (2019). "TarMAC: Targeted Multi-Agent Communication." *Proceedings of the 36th International Conference on Machine Learning*, PMLR **97**. Preprint: [arXiv:1810.11187](https://arxiv.org/abs/1810.11187) (v2 read).

## TL;DR

Cooperating reinforcement-learning agents learn what to say and to whom by attention. Each message carries a signature (key) and a value, each receiver forms a query from its own hidden state, and scaled dot-product soft attention over incoming signatures decides how much of each message the receiver takes in. Targeting is learned from task reward alone, and several rounds of communication can precede each action.

## What it establishes

In Section 3 each agent's message consists of a signature $k_i\in\mathbb R^{d_k}$, encoding properties of the intended recipients, and a value $v_i\in\mathbb R^{d_v}$. A receiver $j$ predicts a query $q_j$ from its hidden state, and the attention weights are a softmax over incoming messages of $q_j^\top k_i/\sqrt{d_k}$, including the receiver's own message. The aggregated input is the attention-weighted sum of values. Multi-round communication feeds the aggregated message back into the hidden state before new signatures, queries, and values are predicted. The architecture is trained with centralized actor-critic learning and executed in a decentralized way, with policies sharing parameters across agents. Experiments on SHAPES navigation, traffic junctions, and House3D navigation show gains from both targeting and multiple rounds. In the traffic-junction task, adding rounds of communication helps more than enlarging messages. An extension that first gates whether to communicate (IC3Net) handles mixed and competitive settings.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript cites TarMAC as the precedent for reading attention between tokens as communication between agents: senders broadcast keyed messages and receivers route them by soft attention. The manuscript develops the same reading for Gaussian token states, with separate comparison maps for routing and content maps for the transmitted message. See [[GL(K) gauge-equivariant attention]] and [[Multi-agent variational free energy]].

## Local full text

The arXiv v2 PDF is stored at `sources/pdfs/Das2019TarMAC.pdf` ([local PDF](../pdfs/Das2019TarMAC.pdf)). Source: [arXiv:1810.11187](https://arxiv.org/pdf/1810.11187). SHA-256: `7818a0d02e517a0ba4a45e4aedfa8a6743ef0a41803cbcdada73284a0aee129e`.

## BibTeX

```bibtex
@inproceedings{Das2019TarMAC,
  author = {Das, Abhishek and Gervet, Th{\'e}ophile and Romoff, Joshua and Batra, Dhruv and Parikh, Devi and Rabbat, Michael and Pineau, Joelle},
  title = {{TarMAC}: Targeted Multi-Agent Communication},
  booktitle = {Proceedings of the 36th International Conference on Machine Learning},
  series = {Proceedings of Machine Learning Research},
  volume = {97},
  year = {2019},
  eprint = {1810.11187},
  archivePrefix = {arXiv}
}
```
