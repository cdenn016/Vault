---
type: concept
title: "Sequence-to-sequence learning"
aliases:
  - "Sequence-to-Sequence"
  - "seq2seq"
  - "Sequence-to-Sequence Models"
  - "Seq2seq"
  - "Sequence-to-sequence model"
  - "Encoder-decoder model"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Sequence-to-sequence learning

Sequence-to-sequence (seq2seq) learning is the encoder-decoder paradigm in which one variable-length sequence is mapped to another: an encoder compresses the input into a context representation and a decoder generates the output autoregressively. Introduced for machine translation with RNN/LSTM encoders and decoders, it was the architecture onto which soft attention (Bahdanau) and ultimately the Transformer were grafted, removing the fixed-length-bottleneck limitation. It is the immediate architectural ancestor of attention-based language models and the setting in which compositional generalization is typically tested.

## Related
[[Attention mechanisms — theory and positional structure]], [[Compositional generalization]]

## Sources
[[lake2018-generalization-scan]], [[bahdanau-2014-neural-machine-translation]]
