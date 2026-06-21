---
type: concept
title: "Language Modeling"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Language Modeling

The task of estimating the probability distribution over sequences of tokens, typically by predicting the next token given prior context (autoregressive) or masked tokens (bidirectional). Language modeling is the training objective and evaluation setting for the program's VFE transformer (vfe3): perplexity / next-token cross-entropy on corpora such as WikiText-103. Long-context variants (Transformer-XL), adaptive softmax improvements, and large autoregressive models (GPT-2) are the standard baselines.

## Related
[[VFE Transformer Program]], [[Attention mechanisms — theory and positional structure]]

## Sources
[[dai2019transformerxl]], [[radford2019-gpt2]]
