---
type: concept
title: "Probing classifiers"
tags:
  - cluster/attention
  - cluster/methodology
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Probing classifiers

Probing classifiers are an interpretability methodology in which a simple supervised classifier (a probe) is trained on the frozen internal representations of a neural network to test whether a target linguistic or structural property (e.g. part of speech, syntactic dependency, coreference) is linearly decodable from those activations. High probe accuracy is taken as evidence that the property is encoded in the representation. The method underlies studies of what attention heads and hidden states in transformers capture, motivating the program's interest in what structure emerges in learned belief representations.

## Related
[[Mechanistic interpretability of attention]], [[Attention mechanisms — theory and positional structure]]

## Sources
[[clark-2019-bert-attention|clark2019does-bert-look]]
