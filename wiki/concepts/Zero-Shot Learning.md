---
type: concept
title: "Zero-Shot Learning"
tags:
  - cluster/attention
  - cluster/cs-ml
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Zero-Shot Learning

Zero-shot learning is the ability of a model to perform a task it was never explicitly trained on, by conditioning on a natural-language description or prompt at inference time. Radford et al.'s GPT-2 demonstrated that a sufficiently large language model trained only on next-token prediction over diverse text acquires emergent zero-shot capability across translation, summarization, and question answering — performing tasks specified purely in the prompt with no gradient updates. This generalization-by-prompting is a precursor to in-context learning and is central to understanding what large autoregressive transformers compute, motivating the program's interest in the inference dynamics inside attention.

## Related
`in-context learning`, [[Attention mechanisms — theory and positional structure]]

## Sources
[[radford-2019-gpt2]]
