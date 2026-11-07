---
type: paper
title: "Learning to Ground Multi-Agent Communication with Autoencoders"
aliases: ["Lin et al. 2021 autoencoder communication", "AE-Comm"]
authors: ["Toru Lin", "Jacob Huh", "Christopher Stauffer", "Ser Nam Lim", "Phillip Isola"]
year: 2021
venue: "Advances in Neural Information Processing Systems 34:15230–15242"
url: "https://proceedings.neurips.cc/paper/2021/hash/80fee67c8a4c4989bf8a580b4bbb0cd2-Abstract.html"
version: "Published conference paper; proceedings metadata and PDF byline differ"
tags: [cluster/multi-agent, cluster/attention, project/multi-agent, project/transformer, field/cs-ml]
created: 2026-11-07
updated: 2026-11-07
---

# Learning to Ground Multi-Agent Communication with Autoencoders

> [!info] Citation
> Lin, T., Huh, J., Stauffer, C., Lim, S. N., and Isola, P. (2021). *Learning to Ground Multi-Agent Communication with Autoencoders*. Advances in Neural Information Processing Systems, 34, 15230–15242. [Proceedings record](https://proceedings.neurips.cc/paper/2021/hash/80fee67c8a4c4989bf8a580b4bbb0cd2-Abstract.html); [published PDF](https://proceedings.neurips.cc/paper_files/paper/2021/file/80fee67c8a4c4989bf8a580b4bbb0cd2-Paper.pdf).

[Local proceedings PDF](../pdfs/lin-2021-autoencoder-communication.pdf), 13 pages; retrieved November 7, 2026.

The frontmatter and BibTeX follow the publisher's current metadata. The linked PDF byline instead gives Minyoung Huh, Chris Stauffer, and Ser-Nam Lim; this discrepancy is preserved rather than silently reconciled.

## TL;DR

Agents learn communication by reconstructing their own observation features, then learn how received messages support cooperative action.

## Problem & setting

Section 3 specifies independent policies, decentralized training, delayed broadcast messages, and cooperative task returns. Common architecture does not imply shared learned parameters.

## Method

An encoder produces quantized communication symbols. An auxiliary decoder reconstructs the sender's image features, minimizing squared reconstruction error with a straight-through estimator. A separate listener module combines received symbols with local features to select actions. Reconstruction and policy-gradient losses train each agent without gradients crossing between agents. See sections 4.1–4.2.

## Key results

Experiments use CIFAR Game, FindGoal, and RedBlueDoors, with ablations of grounding and communication. Reported improvements concern these cooperative environments; they do not prove arbitrary semantic alignment.

## Relevance to this research

This supplies a grounded-expression comparator for [[Communication-constrained inference]]. The sender's auxiliary reconstruction decoder is not the receiver's interpretation model. Learned response policies also do not by themselves define Bayesian posterior reconstruction or [[Expected Free Energy]] planning.

## Cross-links

[[Active inference communication and collective boundaries]]; [[Collective active inference]]; [[wang-2020-information-bottleneck-communication]].

## BibTeX

```bibtex
@inproceedings{NEURIPS2021_80fee67c,
  author = {Lin, Toru and Huh, Jacob and Stauffer, Christopher and Lim, Ser Nam and Isola, Phillip},
  title = {Learning to Ground Multi-Agent Communication with Autoencoders},
  booktitle = {Advances in Neural Information Processing Systems},
  volume = {34},
  pages = {15230--15242},
  year = {2021},
  publisher = {Curran Associates, Inc.},
  url = {https://proceedings.neurips.cc/paper_files/paper/2021/file/80fee67c8a4c4989bf8a580b4bbb0cd2-Paper.pdf}
}
```
