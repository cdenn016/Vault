---
type: paper
title: "Interpolated Estimation of Markov Source Parameters from Sparse Data"
aliases:
  - "jelinek1980interpolated"
  - "Jelinek & Mercer 1980"
  - "Interpolated estimation"
  - "Deleted interpolation"
authors:
  - "Jelinek, Frederick"
  - "Mercer, Robert L."
year: 1980
venue: "Workshop on Pattern Recognition in Practice"
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Interpolated Estimation of Markov Source Parameters from Sparse Data

> [!info] Citation
> Jelinek, Frederick, Mercer, Robert L. (1980). "Interpolated Estimation of Markov Source Parameters from Sparse Data." Workshop on Pattern Recognition in Practice.

## TL;DR
Introduces deleted-interpolation smoothing, which estimates n-gram language-model probabilities by linearly combining (interpolating) higher- and lower-order maximum-likelihood estimates, with interpolation weights fit via the EM algorithm on held-out data. A foundational smoothing technique for sparse Markov-source estimation.

## Relevance to this research
A foundational n-gram smoothing baseline cited alongside Kneser-Ney in the empirical-smoothing study (chen-1998), situating the VFE transformer's language modeling against classical interpolated estimation.

## Cross-links
[[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{jelinek1980interpolated,
  author    = {Jelinek, Frederick and Mercer, Robert L.},
  title     = {Interpolated Estimation of Markov Source Parameters from Sparse Data},
  booktitle = {Proceedings of the Workshop on Pattern Recognition in Practice},
  pages     = {381--397},
  year      = {1980},
  publisher = {North-Holland},
}
```
