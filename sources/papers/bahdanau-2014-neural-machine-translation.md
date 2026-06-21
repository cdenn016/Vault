---
type: paper
title: "Neural Machine Translation by Jointly Learning to Align and Translate"
aliases:
  - "Bahdanau 2014"
  - "Bahdanau et al. 2014"
  - "Bahdanau (2014) Soft Attention"
authors:
  - Bahdanau, Dzmitry
  - Cho, Kyunghyun
  - Bengio, Yoshua
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
updated: 2026-06-20
---

# Neural Machine Translation by Jointly Learning to Align and Translate

> [!info] Citation
> Bahdanau, Dzmitry, Kyunghyun Cho, and Yoshua Bengio (2015). "Neural Machine Translation by Jointly Learning to Align and Translate." 3rd International Conference on Learning Representations (ICLR). arXiv:1409.0473. <https://arxiv.org/abs/1409.0473>

## TL;DR

This paper introduces soft attention: rather than compressing a source sentence into a single fixed-length vector, the decoder, at each output step, computes a normalized distribution of weights over all source positions and reads out a weighted average of their encodings. The weights are an alignment — a soft, differentiable correspondence between target and source — learned jointly with translation. This is the origin of attention as a content-based, normalized mixture over a set of sources, the mechanism later generalized into self-attention by [[vaswani-2017-attention]].

## Problem & setting

Encoder-decoder neural machine translation bottlenecked the whole source through one fixed-length vector, which hurt performance on long sentences. The authors let the decoder consult the full source sequence dynamically at each decoding step, removing the information-compression bottleneck.

## Method

A bidirectional RNN encodes the source into per-position annotation vectors $h_j$. At each decoding step $t$, an alignment score $e_{tj} = a(s_{t-1}, h_j)$ between the previous decoder state $s_{t-1}$ and each annotation is computed by a small feedforward network, then normalized by softmax into attention weights $\alpha_{tj} = \exp(e_{tj}) / \sum_k \exp(e_{tk})$. The context vector $c_t = \sum_j \alpha_{tj} h_j$ (a weighted sum of annotations) feeds the next decoder output. The whole system is trained end to end, so alignments emerge without explicit supervision.

## Key results

- Large translation-quality gains (measured in BLEU) over the fixed-vector baseline, especially on long sentences where the single-vector bottleneck is most acute.
- Learned attention weights recover linguistically sensible, sometimes non-monotonic, word alignments — interpretable as a soft alignment matrix between source and target positions.
- Established the now-universal template: normalized content-based weighting over a variable-length set of encoded sources.

## Relevance to this research

This paper is the conceptual root of the VFE program's reading of attention as a mixture over sources. The GL(K) attention manuscript interprets $\beta_{ij} = \mathrm{softmax}(-\mathrm{KL}(q_i\|\Omega_{ij}q_j)/\tau)$ as a normalized distribution describing how much agent $i$ draws its belief from each candidate source $j$ — structurally the same object as Bahdanau's alignment distribution, with a KL divergence between gauge-transported Gaussian beliefs replacing the learned alignment score. Seeing the original soft attention stated as alignment-over-sources clarifies that the VFE formulation is not redefining attention but giving its score function an information-geometric form (KL on the statistical manifold) and its sum-over-sources a gauge-covariant transport $\Omega_{ij}$. The differentiable-alignment idea also underlies the source-attribution interpretability thread: whether $\beta_{ij}$ faithfully reports the source of information is a question first raised by treating attention as alignment.

## Cross-links

- Concepts: [[Attention mechanisms — theory and positional structure]], [[Mechanistic interpretability of attention]]
- Related sources: [[vaswani-2017-attention]], [[olsson-2022-induction-heads]], [[tsai-2019-kernel-attention]]
- Manuscript/Project: [[GL(K) Attention Manuscript]], [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

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
