---
type: paper
title: "Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned"
aliases:
  - Voita 2019
  - Voita attention heads
  - voita-2019-multihead
  - Voita et al. 2019
  - Voita (2019) Multi-Head Attention
authors:
  - Voita, Elena
  - Talbot, David
  - Moiseev, Fedor
  - Sennrich, Rico
  - Titov, Ivan
year: 2019
arxiv: "1905.09418"
url: https://arxiv.org/abs/1905.09418
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned

> [!info] Citation
> Voita, E., Talbot, D., Moiseev, F., Sennrich, R., & Titov, I. (2019). "Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned." ACL 2019. arXiv:1905.09418.

## TL;DR
The paper investigates the functional roles of individual attention heads in the Transformer encoder for neural machine translation. Using layer-wise relevance propagation (LRP) and a novel L0-based head-pruning method with Hard Concrete gates, the authors show that only a small subset of heads are important for translation quality, and these important heads play consistent, interpretable roles — attending to adjacent tokens (positional), tracking syntactic dependency relations (syntactic), or pointing to rare words. Pruning 38 of 48 encoder heads on English-Russian WMT results in a drop of only 0.15 BLEU.

## Problem & setting
Multi-head attention is central to the Transformer, but prior analyses averaged or took the maximum over all heads, obscuring the varying contributions of individual heads. The paper asks which encoder heads matter, what interpretable roles they play, and how redundant the remaining heads are. The setting is encoder-decoder neural machine translation on WMT English-Russian/German/French with 2.5m sentence pairs (Transformer-base, 6 layers, 8 heads each).

## Method
**Head importance via LRP.** Layer-wise relevance propagation (adapted from Ding et al., 2017) back-propagates the top-1 logit through the network to assign a relevance score to each head, measuring its contribution to the prediction. Head confidence is also measured as the average maximum attention weight.

**Head function characterization.** Three functional types are identified: (1) positional heads — at least 90% of the time maximum attention goes to a fixed relative position (±1); (2) syntactic heads — accuracy on a syntactic dependency relation (nsubj, dobj, amod, advmod) at least 10% above a positional baseline; (3) rare-words head — attends to the least frequent token in the sentence.

**L0-regularized pruning.** Each head output is multiplied by a scalar gate $g_i$. Because L0 regularization is non-differentiable, the gates are modeled as Hard Concrete random variables (Louizos et al., 2018) — the Concrete/Gumbel-softmax distribution stretched to $(-\epsilon, 1+\epsilon)$ and rectified to place mass at 0 and 1. The training objective is:
$$\mathcal{L}(\theta, \phi) = \mathcal{L}_\text{xent}(\theta, \phi) + \lambda \mathcal{L}_C(\phi), \quad \mathcal{L}_C(\phi) = \sum_{i=1}^h \bigl(1 - P(g_i = 0 \mid \phi_i)\bigr).$$
Fine-tuning starts from a converged full model with decoder parameters frozen; varying $\lambda$ yields models with different head counts.

## Key results
- LRP identifies a small number of per-layer heads as substantially more important than the rest; these highly-ranked heads are also the most confident (high average maximum attention weight).
- Important heads fall into three interpretable categories: positional, syntactic, and rare-words. The rare-words head in layer 1 is consistently the most important in that layer across all language pairs.
- Syntactic heads track nsubj, dobj, amod, and advmod with accuracies significantly above the positional baseline (e.g., dobj accuracy 73–84% vs. baseline ~41–46% for EN-RU).
- Pruning encoder heads: for WMT EN-RU, 10 heads out of 48 suffice to stay within 0.15 BLEU; for OpenSubtitles, 4 heads suffice with only 0.25 BLEU loss.
- When pruning all attention types, decoder-encoder attention heads are retained last (most important), encoder self-attention heads are pruned first; lower decoder layers retain self-attention heads (language modeling) while higher layers retain cross-attention heads (source conditioning).
- Sparse architectures learned through pruning outperform identically-sized models trained from scratch, consistent with the lottery-ticket/pruning literature.

## Relevance to this research
This paper is relevant to the GL(K) gauge-equivariant attention project in two complementary ways. First, the finding that most heads are redundant and that a small set of interpretable functional heads does the actual work resonates with the VFE perspective: the attention distribution $\beta_{ij}$ in the free-energy functional is a stationary-point softmax whose entropy is penalized, naturally concentrating weight on a few meaningful connections. The VFE framework gives a principled variational reason for why sparse, specialized attention patterns emerge rather than treating it as an empirical curiosity. Second, the syntactic dependency tracking by specific heads is structurally analogous to the gauge-transport interpretation of attention in GL(K): syntactic relations correspond to the parallel-transport paths $\Omega_{ij}$ that define which "coordinate frame" token $j$ should be aligned to before comparing to token $i$. The positional heads tracking $\pm 1$ neighbours are the simplest gauge connections. The LRP head-importance scores also suggest a practical diagnostic tool for auditing which heads in a VFE transformer are doing meaningful variational work versus which are near-zero gate. The pruning method itself (scalar gates with L0 relaxation) is a structural cousin to the $\beta_{ij}$ attention weights: both are learned sparse routing coefficients, though in the VFE framework sparsity emerges from variational optimality rather than an explicit penalty.

In the PIFB reading, the positional/syntactic head split maps onto the decomposition of the coupling: positional heads (fixed-offset attention) are the abelian gauge-frame / distance-prior part (the RoPE and ALiBi mechanisms of [[su-2021-roformer-rope]] and [[press-2021-alibi]]), while relation-specific syntactic heads are the content-driven KL coupling between beliefs. This grounds the head-role reading under [[Mechanistic interpretability of attention]].

## Cross-links
- Concepts: [[Multi-Head Attention]], [[Attention Mechanisms]], [[Transformer Architecture]], [[Gauge Transport]], [[Mechanistic interpretability of attention]]
- Related sources: [[vaswani-2017-attention]], [[louizos-2018-l0]], [[olsson-2022-induction-heads]], [[clark-2019-bert-attention]]
- Manuscript/Project: [[GL(K) Attention Manuscript]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{Voita2019,
  author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},
  title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},
  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  year      = {2019},
  pages     = {5797--5808},
  note      = {arXiv:1905.09418},
}
```
