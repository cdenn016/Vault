---
type: paper
title: "Improved Backing-off for M-gram Language Modeling"
aliases:
  - "kneser1995improved"
  - "Kneser & Ney 1995"
  - "Kneser-Ney smoothing"
authors:
  - "Kneser, Reinhard"
  - "Ney, Hermann"
year: 1995
url: https://doi.org/10.1109/ICASSP.1995.479394
venue: "ICASSP"
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Improved Backing-off for M-gram Language Modeling

> [!info] Citation
> Kneser, Reinhard, Ney, Hermann (1995). "Improved Backing-off for M-gram Language Modeling." ICASSP. https://doi.org/10.1109/ICASSP.1995.479394

## TL;DR
Introduces Kneser-Ney smoothing for n-gram language models, which discounts higher-order counts and backs off to a lower-order distribution based on the number of distinct contexts a word completes rather than raw frequency. It became the strongest classical smoothing method for n-gram LMs.

## Relevance to this research
A classical language-modeling baseline cited in the empirical-smoothing comparison (chen-1998) that contextualizes the VFE transformer's generative language modeling against pre-neural n-gram methods.

## Cross-links
[[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{kneser1995improved,
  author    = {Kneser, Reinhard and Ney, Hermann},
  title     = {Improved Backing-off for M-gram Language Modeling},
  booktitle = {Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP)},
  volume    = {1},
  pages     = {181--184},
  year      = {1995},
  doi       = {10.1109/ICASSP.1995.479394},
}
```
