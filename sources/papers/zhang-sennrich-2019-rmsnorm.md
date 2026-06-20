---
type: paper
title: Root Mean Square Layer Normalization
aliases:
  - "Zhang, Sennrich 2019 — RMSNorm"
  - "Root Mean Square Layer Normalization"
authors:
  - Biao Zhang
  - Rico Sennrich
year: 2019
arxiv: 1910.07467
url: https://arxiv.org/abs/1910.07467
tags:
  - cluster/attention
  - cluster/methodology
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Root Mean Square Layer Normalization

> [!info] Citation
> Zhang, B., & Sennrich, R. (2019). Root Mean Square Layer Normalization. Advances in Neural Information Processing Systems 32 (NeurIPS 2019), 12360–12371. arXiv:1910.07467.

## TL;DR

Layer normalization stabilizes training by re-centering and re-scaling the summed inputs to each neuron, and both operations were long assumed to be essential. Zhang and Sennrich argue that the re-centering half of the recipe is dispensable: the property that does the work is re-scaling invariance, and one can obtain it by dividing each activation vector by its root mean square alone, without ever subtracting the mean. The resulting **RMSNorm** drops the mean-subtraction and the learned bias entirely, keeping only a per-dimension gain. It matches LayerNorm's accuracy across a range of tasks while cutting the per-layer normalization cost — they report wall-clock speedups of roughly 7% to 64% depending on architecture — because it computes one statistic (a sum of squares) instead of two (mean then variance). RMSNorm has since become the default normalizer in the modern decoder-only stack (it is the norm used throughout LLaMA and its descendants).

## Problem & setting

LayerNorm (Ba, Kiros, & Hinton, 2016) normalizes the vector of summed inputs $a \in \mathbb{R}^{d}$ feeding a layer by removing its empirical mean and dividing by its empirical standard deviation, then applying a learned elementwise gain $g$ and bias $b$. Its success is usually attributed to two invariances it confers on the layer's output: invariance to a shift of all inputs (re-centering) and invariance to a global rescaling of all inputs (re-scaling). LayerNorm is, however, a sequential two-pass statistic — the mean must be formed before the variance — and in throughput-bound training of large sequence models even this small overhead per layer accumulates. The authors set out to test which of the two invariances is actually responsible for LayerNorm's optimization benefit, hypothesizing that re-centering is incidental and that re-scaling invariance carries the load. The prior art they build on is LayerNorm itself, the broader normalization literature (batch normalization and weight normalization), and the analysis framing normalization in terms of invariance properties and implicit learning-rate adaptation.

## Method

LayerNorm computes, for the summed-input vector $a \in \mathbb{R}^{d}$,
$$ \mu = \frac{1}{d}\sum_{i=1}^{d} a_i, \qquad \sigma = \sqrt{\frac{1}{d}\sum_{i=1}^{d} (a_i - \mu)^2}, \qquad \bar{a}_i = \frac{a_i - \mu}{\sigma}\, g_i + b_i. $$
RMSNorm removes the mean entirely and rescales by the root mean square of the activations,
$$ \mathrm{RMS}(a) = \sqrt{\frac{1}{d}\sum_{i=1}^{d} a_i^{2}}, \qquad \bar{a}_i = \frac{a_i}{\mathrm{RMS}(a)}\, g_i, $$
where $g \in \mathbb{R}^{d}$ is a learned per-dimension gain and there is no bias term. When the mean of $a$ happens to be zero the two coincide, so RMSNorm can be read as LayerNorm with the re-centering step deleted. The construction makes the output invariant to any global rescaling $a \mapsto c\,a$ of the inputs (since $\mathrm{RMS}(c a) = |c|\,\mathrm{RMS}(a)$), but deliberately not invariant to a global shift $a \mapsto a + \beta\mathbf{1}$. The authors connect this surviving invariance to an implicit learning-rate adaptation effect: gradients to the weights producing $a$ are automatically scaled by $1/\mathrm{RMS}(a)$, damping updates when activations grow large. They also propose **pRMSNorm** (partial RMSNorm), which estimates $\mathrm{RMS}(a)$ from only the first $p\%$ of the dimensions on the assumption that the per-dimension statistics are roughly i.i.d., trading a small approximation for a further reduction in the summation cost.

## Method properties

The paper's analytical contribution is to separate the invariances LayerNorm provides and show that RMSNorm retains re-scaling invariance (both to weight-matrix rescaling and to input rescaling) while giving up re-centering invariance. Because RMSNorm forms a single second-moment statistic rather than a mean and then a variance, and because it carries no bias parameter, it is strictly cheaper than LayerNorm in both computation and parameter count.

## Key results

Across the tasks the authors evaluate — including machine translation and other sequence-modeling and recognition benchmarks — RMSNorm reaches accuracy comparable to LayerNorm while reducing normalization-layer running time. The headline efficiency figure is a reported reduction in running time of roughly **7% to 64%** across the different models tested, the spread reflecting how much of each architecture's cost the normalization layer occupies. The qualitative claim the evidence supports is the central hypothesis: discarding re-centering does not degrade learning, which is evidence that re-scaling invariance, not re-centering, is the property responsible for LayerNorm's stabilizing effect. The pRMSNorm variant is shown to remain competitive while estimating the norm from a fraction of the dimensions. The evidence is empirical and comparative rather than a formal optimization guarantee; the speedup range is architecture-dependent and should be read as such rather than as a single universal number.

## Relevance to this research

RMSNorm is the normalization layer of the modern decoder-only convention — the LLaMA-style stack — that the [[VFE Transformer Program]] uses as its architectural baseline, so any comparison of the program's no-neural-network residual pipeline against a contemporary transformer is implicitly a comparison against an RMSNorm-normalized one rather than the original post-LN LayerNorm transformer. More pointedly, the paper's central move — drop mean re-centering and the bias, keep only the RMS rescaling — maps directly onto the program's gauge-theoretic norm-cancellation story, in which the only physically meaningful operation on a belief or activation vector is a rescaling and additive offsets carry no gauge-invariant content; this rescaling-only, no-bias reading is already invoked in the GL(K) supplementary material. RMSNorm thus furnishes an external, empirically validated precedent for the design choice that the program reaches on geometric grounds: that re-centering is dispensable and that the load-bearing invariance is multiplicative. It also bears on how positional and scaling behavior is read in [[Attention mechanisms — theory and positional structure]] and [[Transformer interpretability and scaling]], since the choice of normalizer interacts with the residual-stream scale that downstream attention logits and softmax temperatures depend on.

## Cross-links

- Concepts / Themes: [[Attention mechanisms — theory and positional structure]], [[Transformer interpretability and scaling]]
- Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@inproceedings{zhangsennrich2019rmsnorm,
  author    = {Zhang, Biao and Sennrich, Rico},
  title     = {Root Mean Square Layer Normalization},
  booktitle = {Advances in Neural Information Processing Systems 32 (NeurIPS 2019)},
  pages     = {12360--12371},
  year      = {2019},
  eprint    = {1910.07467},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/1910.07467}
}
```
