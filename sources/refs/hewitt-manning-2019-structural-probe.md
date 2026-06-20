---
type: reference
title: "A Structural Probe for Finding Syntax in Word Representations"
aliases:
  - "Hewitt & Manning 2019"
  - "Structural Probe"
authors:
  - John Hewitt
  - Christopher D. Manning
year: 2019
url: https://aclanthology.org/N19-1419/
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# A Structural Probe for Finding Syntax in Word Representations

> [!info] Citation
> John Hewitt and Christopher D. Manning (2019). "A Structural Probe for Finding Syntax in Word Representations." NAACL-HLT 2019, pp. 4129–4138. <https://aclanthology.org/N19-1419/>

## TL;DR

This paper asks whether the syntax tree of a sentence is encoded **geometrically** in a contextual word representation. The structural probe learns a single linear transformation of the representation space such that the squared Euclidean distance between two transformed word vectors approximates their **distance in the dependency parse tree**, and the squared norm approximates parse **depth**. Such a transformation is found for ELMo and BERT but not for baselines, evidence that deep contextual encoders embed parse structure as a low-rank metric on the representation space.

## What it establishes

- A probe recovering parse-tree distances and depths via a learned linear (low-rank) metric on representations.
- ELMo and BERT carry recoverable syntactic structure; non-contextual and random baselines do not.
- Syntax is present as approximate tree geometry, not as an explicit symbolic object.

## Why the project cites it

PIFB ([[participatory-it-from-bit]]) advances a **parse-completeness conjecture**: that the belief representation, under iterative free-energy minimization, comes to encode the full syntactic structure needed to predict the next token. Hewitt & Manning are the empirical foil for that claim — they establish both a positive (parse structure *is* recoverable as a metric on representations) and a methodological standard (a probe that reads structure out as geometry). The fact that parse distance appears as a *learned linear metric* is suggestive for PIFB, whose representations carry an explicit metric structure: the belief covariance $\Sigma$ on the SPD manifold and its affine-invariant / Mahalanobis form already define a distance, so the project can ask whether parse-tree distance is recoverable from the *intrinsic* belief metric rather than a separately learned probe matrix. This connects the parse-completeness thread to [[Mechanistic interpretability of attention]] and to the attention-tracks-dependency evidence of [[clark-2019-bert-attention]], against which the conjecture must be tested.

```bibtex
@inproceedings{hewitt2019structural,
  title     = {A Structural Probe for Finding Syntax in Word Representations},
  author    = {Hewitt, John and Manning, Christopher D.},
  booktitle = {Proceedings of the 2019 Conference of the North American Chapter of
               the Association for Computational Linguistics: Human Language
               Technologies (NAACL-HLT)},
  pages     = {4129--4138},
  year      = {2019},
  url       = {https://aclanthology.org/N19-1419/}
}
```
