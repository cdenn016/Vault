---
type: concept
title: "Transfer learning"
tags:
  - cluster/vfe
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Transfer learning

Transfer learning is the paradigm of pretraining a model on a large source task/corpus and then reusing the learned representations on a downstream target task, either by fine-tuning all parameters or by adapting a task head. It underlies the modern NLP recipe: self-supervised pretraining (masked or causal language modeling) yields general-purpose representations that transfer to many tasks with little labeled data. In the gauge-theoretic VFE program it is the practical training regime for the vfe3 transformer and frames how learned belief-geometry generalizes across tasks.

## Related
[[Predictive coding network]], [[VFE Transformer Program]]

## Sources
[[devlin-2018-bert]], [[raffel2020exploring]]
