---
type: reference
title: "Why Does Deep and Cheap Learning Work So Well?"
aliases: ["lin2017deep"]
authors: ["Henry W. Lin", "Max Tegmark", "David Rolnick"]
year: 2017
venue: "Journal of Statistical Physics"
doi: "10.1007/s10955-017-1836-5"
url: "https://doi.org/10.1007/s10955-017-1836-5"
tags: [cluster/multi-agent, project/multi-agent, field/physics, field/cs-ml]
created: 2026-11-10
updated: 2026-11-10
---
# Why Does Deep and Cheap Learning Work So Well?

> [!info] Citation
> Lin, H. W., Tegmark, M., Rolnick, D. (2017). *Why Does Deep and Cheap Learning Work So Well?*. Journal of Statistical Physics, 168(6), 1223-1247. [DOI](https://doi.org/10.1007/s10955-017-1836-5)

[Local PDF](../pdfs/lin-2017-why-does-deep.pdf), 16 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and manuscript reading record.

## TL;DR

The paper argues that the success of deep learning depends on physics as well as mathematics: functions of practical interest can often be approximated with exponentially fewer parameters than generic functions, because of properties such as symmetry, locality and compositionality.

## Problem & setting

Approximation theorems guarantee that neural networks can represent arbitrary functions, but the set of possible functions is far larger than the set of practically relevant ones. The authors adopt a physics perspective and focus on expressibility and efficiency, not on learnability.

## Method

They relate properties common in physics (symmetry, locality, compositionality, polynomial log-probability) to simple networks, argue that hierarchical data-generating processes favor deep over shallow networks, and formalize this with information theory and a discussion of the renormalization group.

## Key results

The paper proves "no-flattening theorems" showing when efficient linear deep networks cannot be approximated by shallow ones without loss of efficiency. One stated example is that multiplying $n$ variables requires at least $2n$ neurons in a single hidden layer.

## Relevance to this research

The manuscript cites this paper only as the source of the working definition of renormalization that a paper on free-energy renormalization adopts, and calls the composite a renormalization in that working sense. The reading record says it was known from its bibliographic record, and the first pages were read for this note; the working definition itself was not located there. It sits beside [[Renormalization group flow]] and [[Coarse Graining]] in the vault, and relates to [[Deep Networks]].

## Cross-links

[[Collective agents literature map]]; [[Renormalization group flow]]; [[Coarse Graining]]; [[Deep Networks]].

## BibTeX

```bibtex
@article{lin2017deep,
  author  = {Lin, Henry W. and Tegmark, Max and Rolnick, David},
  title   = {Why Does Deep and Cheap Learning Work So Well?},
  journal = {Journal of Statistical Physics},
  volume  = {168},
  number  = {6},
  pages   = {1223--1247},
  year    = {2017},
  doi     = {10.1007/s10955-017-1836-5}
}
```
