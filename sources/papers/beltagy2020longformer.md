---
type: paper
title: "Longformer: The Long-Document Transformer"
aliases:
  - Beltagy 2020
  - Longformer
  - beltagy-2020-longformer
  - Beltagy et al. 2020
authors:
  - Beltagy, Iz
  - Peters, Matthew E.
  - Cohan, Arman
year: 2020
arxiv: "2004.05150"
url: https://arxiv.org/abs/2004.05150
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Longformer: The Long-Document Transformer

> [!info] Citation
> Beltagy, Iz, Matthew E. Peters, and Arman Cohan (2020). "Longformer: The Long-Document Transformer." arXiv:2004.05150. https://arxiv.org/abs/2004.05150

## TL;DR

Longformer proposes a drop-in replacement for standard $O(n^2)$ self-attention that scales linearly with sequence length by combining a sliding local window attention with task-driven global attention on select tokens. The architecture is pre-trained and fine-tuned on long-document NLP tasks (multi-hop QA, coreference resolution, classification) where prior Transformer models could not fit the input. It achieves state-of-the-art performance on several benchmarks while processing sequences of up to 4096 tokens efficiently.

## Problem & setting

Standard Transformer self-attention is quadratic in sequence length, making it infeasible for documents exceeding ~512 tokens. Prior work either truncated documents, used sliding-window chunking with limited cross-chunk interaction, or sparse attention approximations that were difficult to implement efficiently on hardware. Longformer addresses this scalability bottleneck while retaining the capacity to model long-range dependencies.

## Method

Longformer uses a **combination of two attention patterns**:

1. **Local windowed attention**: Each token attends to a symmetric window of $w$ neighboring tokens. With $L$ layers, the effective receptive field grows to $L \times w$ tokens. Window size is configurable per layer (smaller in lower layers, larger in upper layers).

2. **Global attention**: A small number of task-specific tokens (e.g., `[CLS]` for classification, question tokens for QA) attend to all positions and are attended to by all positions. This breaks the locality constraint where needed and injects task-specific supervision into the attention pattern.

The combined pattern gives $O(n)$ complexity. The implementation uses custom CUDA kernels (via TVM/diagonal band matrix ops) to realize the windowed attention without materializing the full $n \times n$ matrix. Pre-training follows RoBERTa's procedure, continued on long documents with the new attention pattern.

## Key results

- Longformer (large) achieves state-of-the-art on WikiHop (multi-hop QA), TriviaQA (reading comprehension), and HotpotQA, and matches or exceeds task-specific models on several long-document benchmarks.
- Linear scaling in memory and time is confirmed empirically up to sequences of 32k tokens.
- The global-attention mechanism is shown to be critical: removing it and relying purely on local windows degrades performance substantially on tasks requiring long-range reasoning.
- Longformer-Encoder-Decoder (LED) extends the architecture to generation tasks (summarization).

## Relevance to this research

Longformer is directly relevant to the VFE transformer program as a concrete, empirically validated instance of **sparse belief coupling**: the local window pattern is a hard-sparsified approximation of the distance-decaying coupling prior that the VFE framework derives softly through entropy regularization of the attention distribution. In the VFE manuscript framework (GL(K)\_attention.tex), the attention weights $\beta_{ij}$ emerge as the softmax stationary point of the free energy $F$, with the $\tau \beta_{ij} \log(\beta_{ij}/\pi_{ij})$ entropy term penalizing departure from a uniform or distance-decaying prior $\pi_{ij}$. Longformer's windowed pattern corresponds to a hard-threshold $\pi_{ij}$ — nonzero only within a local band — which is a limiting case of the VFE coupling prior rather than its general form.

The global-attention tokens are also structurally analogous to the hierarchical model layer ($s_i$) in the VFE belief hierarchy: tokens with global scope play the role of meta-agents that aggregate and broadcast across the population, mirroring the $\lambda_h \cdot \text{KL}(s_i \| h)$ hyper-prior coupling that grounds all local beliefs to a shared centroid. This parallel reinforces the theoretical motivation for the PIFB manuscript's use of Longformer as a long-context architectural reference.

## Cross-links

- Concepts: [[Attention mechanisms — theory and positional structure]], [[Sparse attention]]
- Related sources: [[press-2021-alibi]], [[participatory-it-from-bit]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) Attention Manuscript]], [[PIFB]]

> [!note] Editorial: PIFB ([[participatory-it-from-bit]]) cites Longformer as long-context "architecture furniture" — a representative efficient-attention scheme whose local-window-plus-global pattern is a hard, hand-designed special case of the distance-decaying coupling prior that PIFB derives softly (the entropy-regularized consensus prior behind ALiBi, [[press-2021-alibi]]).

## BibTeX

```bibtex
@article{beltagy2020longformer,
  title         = {Longformer: The Long-Document Transformer},
  author        = {Beltagy, Iz and Peters, Matthew E. and Cohan, Arman},
  journal       = {arXiv preprint arXiv:2004.05150},
  year          = {2020},
  eprint        = {2004.05150},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2004.05150}
}
```
