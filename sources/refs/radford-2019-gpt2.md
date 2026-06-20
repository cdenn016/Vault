---
type: reference
title: "Language Models Are Unsupervised Multitask Learners (GPT-2)"
aliases:
  - "Radford et al. 2019"
  - "GPT-2"
authors:
  - Alec Radford
  - Jeffrey Wu
  - Rewon Child
  - David Luan
  - Dario Amodei
  - Ilya Sutskever
year: 2019
url: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# Language Models Are Unsupervised Multitask Learners (GPT-2)

> [!info] Citation
> Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever (2019). "Language Models Are Unsupervised Multitask Learners." OpenAI technical report.

## TL;DR

GPT-2 is a large decoder-only transformer trained autoregressively on the WebText corpus, showing that a single language model scaled up performs many downstream tasks zero-shot, without task-specific training. It is the standard architecture-and-recipe reference for modern autoregressive language modeling.

## Relevance to this research

Cited by PIFB ([[participatory-it-from-bit]]) as architecture furniture: the conventional decoder-only autoregressive transformer that the project's no-neural-network VFE construction is an alternative to. It fixes the baseline (scaled dot-product self-attention, [[vaswani-2017-attention]]; the scaling-law genre, [[kaplan-2020-scaling-laws]]) against which the project's belief-tuple architecture is positioned.

```bibtex
@techreport{radford2019language,
  title       = {Language Models Are Unsupervised Multitask Learners},
  author      = {Radford, Alec and Wu, Jeffrey and Child, Rewon and Luan, David and
                 Amodei, Dario and Sutskever, Ilya},
  institution = {OpenAI},
  year        = {2019},
  note        = {OpenAI technical report; GPT-2}
}
```
