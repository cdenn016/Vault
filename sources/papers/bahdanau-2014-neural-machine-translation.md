---
type: paper
title: "Neural Machine Translation by Jointly Learning to Align and Translate"
aliases:
  - "Bahdanau et al. 2014"
  - "Bahdanau (2014) Soft Attention"
authors:
  - Dzmitry Bahdanau
  - Kyunghyun Cho
  - Yoshua Bengio
year: 2014
arxiv: "1409.0473"
url: https://arxiv.org/abs/1409.0473
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Neural Machine Translation by Jointly Learning to Align and Translate

> [!info] Citation
> Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio (2014). "Neural Machine Translation by Jointly Learning to Align and Translate." ICLR 2015. arXiv:1409.0473. <https://arxiv.org/abs/1409.0473>

## TL;DR

This paper introduces **soft attention**: rather than compressing a source sentence into a single fixed-length vector, the decoder, at each output step, computes a normalized distribution of weights over all source positions and reads out a weighted average of their encodings. The weights are an **alignment** — a soft, differentiable correspondence between target and source — learned jointly with translation. This is the origin of attention as a content-based, normalized mixture over a set of sources, the mechanism later generalized into self-attention by [[vaswani-2017-attention]].

## Problem & setting

Encoder-decoder neural machine translation bottlenecked the whole source through one vector, which hurt long sentences. The authors let the decoder consult the full source dynamically.

## Method

A bidirectional RNN encodes the source into per-position annotations; at each decoding step an alignment score between the decoder state and each annotation is normalized by softmax into attention weights, and the resulting context vector (a weighted sum of annotations) feeds the next output. The whole system is trained end to end, so alignments emerge without supervision.

## Key results

- Large translation-quality gains over the fixed-vector baseline, especially on long sentences.
- Learned attention weights recover linguistically sensible, sometimes non-monotonic, word alignments — interpretable as a soft alignment matrix.
- Established the now-universal template: normalized content-based weighting over a variable-length set of sources.

## Relevance to this research

This is the conceptual root of PIFB's ([[participatory-it-from-bit]]) reading of attention as a **mixture over sources**. PIFB interprets $\beta_{ij} = \mathrm{softmax}(-\mathrm{KL}(q_i\|\Omega_{ij}q_j)/\tau)$ as a normalized distribution describing how much agent $i$ draws its belief from each candidate source $j$ — structurally the same object as Bahdanau's alignment distribution, with a KL-divergence between transported Gaussian beliefs replacing the learned alignment score. Seeing the original soft attention stated as alignment-over-sources clarifies that PIFB is not redefining attention but giving its score function an information-geometric form (KL on the [[Statistical manifold]]) and its sum-over-sources a gauge-covariant transport $\Omega_{ij}$. The differentiable-alignment idea also underlies the source-attribution interpretability thread ([[Mechanistic interpretability of attention]], [[olsson-2022-induction-heads]]): whether $\beta_{ij}$ faithfully reports the source of information is a question first raised by treating attention as alignment.

## Cross-links

- Concepts: [[Attention mechanisms — theory and positional structure]], [[Mechanistic interpretability of attention]]
- Sources: [[vaswani-2017-attention]], [[olsson-2022-induction-heads]], [[tsai-2019-kernel-attention]]
- Project: [[participatory-it-from-bit]], [[Gauge-Theoretic Multi-Agent VFE Model]]

```bibtex
@inproceedings{bahdanau2015neural,
  title         = {Neural Machine Translation by Jointly Learning to Align and Translate},
  author        = {Bahdanau, Dzmitry and Cho, Kyunghyun and Bengio, Yoshua},
  booktitle     = {3rd International Conference on Learning Representations (ICLR)},
  year          = {2015},
  eprint        = {1409.0473},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/1409.0473}
}
```
