---
type: reference
title: "What Does BERT Look At? An Analysis of BERT's Attention"
aliases:
  - "Clark et al. 2019"
  - "Clark (2019) BERT Attention"
authors:
  - Kevin Clark
  - Urvashi Khandelwal
  - Omer Levy
  - Christopher D. Manning
year: 2019
arxiv: "1906.04341"
url: https://arxiv.org/abs/1906.04341
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# What Does BERT Look At? An Analysis of BERT's Attention

> [!info] Citation
> Kevin Clark, Urvashi Khandelwal, Omer Levy, and Christopher D. Manning (2019). "What Does BERT Look At? An Analysis of BERT's Attention." BlackboxNLP @ ACL 2019. arXiv:1906.04341. <https://arxiv.org/abs/1906.04341>

## TL;DR

This paper analyzes the attention maps of a pre-trained BERT and finds that specific heads attend in linguistically meaningful ways: some track **syntactic dependencies** (e.g. a head reliably attends from objects to their verbs, or from determiners to their nouns), some track **coreference**, and many attend to delimiter tokens like `[SEP]` as a kind of no-op. Attention-based dependency-recovery accuracy for individual heads substantially exceeds chance, evidence that syntax is reflected in where attention points.

## What it establishes

- Individual heads specialize for particular dependency relations and for coreference, recoverable directly from attention weights.
- Heavy attention to `[SEP]`/delimiters functions as a default or null operation.
- Attention patterns carry real, if partial, syntactic information — a complementary readout to the geometric probe of [[hewitt-manning-2019-structural-probe]].

## Why the project cites it

Clark et al. is the **attention-tracks-dependency foil** for PIFB's ([[participatory-it-from-bit]]) parse-completeness conjecture. PIFB claims the belief representation comes to encode the syntactic structure needed for prediction; the strong form would have the coupling weights $\beta_{ij}$ themselves carry the parse. This paper is the evidence base for and against that strong form: it shows attention *does* reflect dependency relations head by head, supporting the idea that $\beta_{ij}$ has linguistic content consistent with PIFB's source-attribution reading, while also showing the signal is partial and head-specific (and confounded by delimiter attention), cautioning against reading a complete parse off the attention matrix. The result pairs with the geometric probe of [[hewitt-manning-2019-structural-probe]] (syntax in the representation metric) to bracket the conjecture from both the weight side and the representation side. Organized under [[Mechanistic interpretability of attention]]; see also head specialization ([[voita-2019-multihead]]).

```bibtex
@inproceedings{clark2019what,
  title         = {What Does BERT Look At? An Analysis of BERT's Attention},
  author        = {Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and
                   Manning, Christopher D.},
  booktitle     = {Proceedings of the 2019 ACL Workshop BlackboxNLP: Analyzing and
                   Interpreting Neural Networks for NLP},
  year          = {2019},
  eprint        = {1906.04341},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/1906.04341}
}
```
