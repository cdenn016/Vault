---
type: paper
title: "Direct Feedback Alignment Scales to Modern Deep Learning Tasks and Architectures"
aliases: [DFA at scale, Launay 2020 DFA]
authors: [Launay J., Poli I., Boniface F., Krzakala F.]
year: 2020
arxiv: 2006.12878
url: https://arxiv.org/abs/2006.12878
tags: [cluster/vfe, cluster/attention, project/transformer, field/cs-ml]
created: 2026-07-11
---

# Direct Feedback Alignment Scales to Modern Deep Learning Tasks and Architectures

> [!info] Citation
> Launay, J., Poli, I., Boniface, F., & Krzakala, F. (2020). *Direct Feedback Alignment Scales to Modern Deep Learning Tasks and Architectures*. NeurIPS 33. arXiv:2006.12878.

## TL;DR
Direct Feedback Alignment (DFA) — projecting the global output error to every layer through fixed random feedback matrices instead of backpropagating through the transpose Jacobians — is tested at modern scale across recommendation, geometric learning, NLP, and vision. It trains transformer language models on WikiText-103, degraded but within striking distance of backprop, establishing the only published backprop-free transformer LM perplexities.

## Problem & setting
Biologically motivated alternatives to backprop (feedback alignment, DFA) had only been demonstrated on small vision tasks. The question: do they scale to architectures people actually use — transformers in particular?

## Method
DFA replaces the backward pass: layer $l$ receives $\delta_l = B_l e$ where $e$ is the output error and $B_l$ a fixed random matrix; weights update locally from $\delta_l$ and the layer's activations. No symmetric weight transport, no sequential backward sweep through the stack.

## Key results
On WikiText-103 with BPE-32k, a 6-layer transformer LM trained with DFA reaches test perplexity **93.3 (micro variant) / 52.0 (macro variant)** against **29.8** for the tuned backprop twin — roughly a 1.7-3x perplexity gap. Attention layers are the hardest component; the paper trains them with DFA applied around the attention block rather than through the softmax internals.

## Relevance to this research
This is the calibration anchor for the [[VFE Transformer Program]]'s backprop-free track ([[Nudged two-phase EM]]): the 52-93 PPL band is the only published backprop-free transformer LM result, so it defines the "beat the published field" milestone gate between the KenLM 5-gram class and backprop parity. It also calibrates expectations: the best published non-backprop transformer sits at 1.7-3x its backprop twin, so a 2x band against matched-K backprop vfe3 is an honest target, not a hedge. Distinct mechanism note: DFA still uses a global error broadcast through random projections, whereas the VFE program's prescription routes credit through inference (nudged equilibria), so the comparison is between credit-assignment families, not implementations.

## Cross-links
- Concepts: [[Vanishing gradient]]
- Methods: [[Nudged two-phase EM]] · [[Predictive coding network]]
- Related sources: [[hinton-2022-forward-forward]] · [[millidge-2020-pc-approximates-backprop]] · [[vaswani-2017-attention]]

## BibTeX
```bibtex
@inproceedings{launay2020direct,
  title     = {Direct Feedback Alignment Scales to Modern Deep Learning Tasks and Architectures},
  author    = {Launay, Julien and Poli, Iacopo and Boniface, Fran{\c{c}}ois and Krzakala, Florent},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {33},
  year      = {2020},
  eprint    = {2006.12878},
  archivePrefix = {arXiv}
}
```
