---
type: paper
title: "Predicting pragmatic reasoning in language games"
aliases: ["Frank and Goodman 2012 language games"]
authors: ["Michael C. Frank", "Noah D. Goodman"]
year: 2012
venue: "Science 336(6084):998"
doi: "10.1126/science.1218633"
url: "https://doi.org/10.1126/science.1218633"
version: "Published article; author manuscript and supplement consulted"
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/psychology, field/cs-ml]
created: 2026-11-07
updated: 2026-11-07
---

# Predicting pragmatic reasoning in language games

> [!info] Citation
> Frank, M. C., and Goodman, N. D. (2012). *Predicting pragmatic reasoning in language games*. Science, 336(6084), 998. [Author manuscript and supplement](https://web.stanford.edu/~ngoodman/papers/FrankGoodman-Science2012.pdf); [author bibliography](https://langcog.stanford.edu/publications).

[Local author manuscript with supplement](../pdfs/frank-goodman-2012-pragmatic-reasoning.pdf), 10 pages; retrieved November 7, 2026. This is not the Science typeset layout.

## TL;DR

A listener infers a referent using a likelihood that represents an informative speaker's word choice, rather than literal compatibility alone.

## Problem & setting

Participants judge reference among three objects with shared color, shape, and texture features. Separate conditions measure speaker choices, referential salience, and listener judgments. Semantics and the available utterances are specified.

## Method

Equations (1)–(2) define

$$
P(r\mid w,C)\propto P(w\mid r,C)P(r),
P(w\mid r,C)=\frac{|w|^{-1}}{\sum_{w'\in W(r)}|w'|^{-1}},
$$

where $|w|$ counts compatible contextual objects and $W(r)$ contains truthful alternatives. Referential priors are measured empirically; the model does not infer them without data.

## Key results

Across the tested contexts, predicted and mean observed judgments correlate at $r=0.98$ for speakers and $r=0.99$ for listeners. The supplement reports 745 participants. These results concern a restricted reference game and aggregated judgments.

## Relevance to this research

This supplies a concrete precedent for strategic message likelihoods in [[Collective active inference]]. It does not derive an [[Expected Free Energy]] objective or explain emergence of shared semantics from arbitrary private models. [[gwon-2026-evidence-intervention]] explicitly extends this comparison to sequential partner modeling.

## Cross-links

[[Active inference communication and collective boundaries]]; [[Decentralized Bayesian inference]].

## BibTeX

```bibtex
@article{frank2012Predicting,
  author = {Frank, Michael C. and Goodman, Noah D.},
  title = {Predicting pragmatic reasoning in language games},
  journal = {Science},
  volume = {336},
  number = {6084},
  pages = {998},
  year = {2012},
  doi = {10.1126/science.1218633},
  url = {https://doi.org/10.1126/science.1218633}
}
```
