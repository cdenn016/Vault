---
type: paper
title: "Deep Contextualized Word Representations"
aliases:
  - "peters-2018-elmo"
  - "peters2018elmo"
  - "ELMo"
authors:
  - "Peters, Matthew E."
  - "Neumann, Mark"
  - "Iyyer, Mohit"
  - "Gardner, Matt"
  - "Clark, Christopher"
  - "Lee, Kenton"
  - "Zettlemoyer, Luke"
year: 2018
url: https://aclanthology.org/N18-1202
venue: "NAACL-HLT 2018"
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Deep Contextualized Word Representations

> [!info] Citation
> Peters, Matthew E., Neumann, Mark, Iyyer, Mohit, Gardner, Matt, Clark, Christopher, Lee, Kenton, Zettlemoyer, Luke (2018). "Deep Contextualized Word Representations." NAACL-HLT 2018. https://aclanthology.org/N18-1202

## TL;DR
Introduces ELMo, deep contextualized word representations derived from a bidirectional LSTM language model. Word vectors are functions of the entire input sentence, capturing both syntax and polysemy, and substantially improved downstream NLP tasks when added to existing models.

## Relevance to this research
A precursor to contextual transformer representations whose probed geometric structure (syntax encoded in representation distances) motivates the gauge-theoretic view of token feature frames in the GL(K)-attention program.

## Cross-links
[[hewitt-2019-structural-probe]]

## BibTeX
```bibtex
@inproceedings{peters2018elmo,
  title={Deep Contextualized Word Representations},
  author={Peters, Matthew E. and Neumann, Mark and Iyyer, Mohit and Gardner, Matt and Clark, Christopher and Lee, Kenton and Zettlemoyer, Luke},
  booktitle={Proceedings of NAACL-HLT},
  pages={2227--2237},
  year={2018}
}
```
