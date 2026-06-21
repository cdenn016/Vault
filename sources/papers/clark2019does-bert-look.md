---
type: paper
title: "What Does BERT Look At? An Analysis of BERT's Attention"
aliases:
  - "Clark 2019"
  - "BERT Attention Analysis"
authors:
  - Clark, Kevin
  - Khandelwal, Urvashi
  - Levy, Omer
  - Manning, Christopher D.
year: 2019
arxiv: "1906.04341"
url: https://arxiv.org/abs/1906.04341
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/neuroscience
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# What Does BERT Look At? An Analysis of BERT's Attention

> [!info] Citation
> Clark, K., Khandelwal, U., Levy, O., & Manning, C. D. (2019). "What Does BERT Look At? An Analysis of BERT's Attention." arXiv:1906.04341. Presented at BlackboxNLP / ACL 2019 workshop.

## TL;DR
This paper proposes methods for analyzing the attention mechanisms of BERT, a large pre-trained Transformer, and applies them to all 144 attention heads in BERT-base. The authors find that individual heads specialize to particular linguistic phenomena — including specific syntactic dependency relations (with some heads achieving >75% accuracy) and coreference — without any explicit supervision for these tasks. A linear combination of attention maps achieves 77 UAS on dependency parsing, demonstrating that BERT's attention encodes substantial syntactic structure as a byproduct of self-supervised pre-training.

## Problem & setting
Large pre-trained language models like BERT achieve state-of-the-art performance on many NLP tasks, but it is poorly understood what linguistic knowledge they acquire. Prior interpretability work focused on model outputs (language model surprisal, targeted evaluation) or internal vector representations (probing classifiers). This paper takes a complementary approach by directly analyzing the attention weight matrices, examining 144 heads across 12 layers of BERT-base over 1000 Wikipedia segments and labeled datasets (Penn Treebank, CoNLL-2012).

## Method
The authors extract attention maps from BERT-base and analyze them along three axes. First, they characterize surface-level patterns: relative positional attention (previous/next token), heavy attention to delimiter tokens ([SEP] acts as a "no-op" for heads whose function is not applicable, as confirmed by gradient-based importance scores showing near-zero gradients for [SEP] attention weight changes), and entropy of attention distributions (early layers have high-entropy, bag-of-vectors heads). Second, they probe individual attention heads against labeled dependency and coreference datasets: for each head and each word, the most-attended-to word is taken as the head's prediction, with no additional training. Third, they propose attention-based probing classifiers for dependency parsing — an attention-only probe learning a linear combination of attention weights across all heads, and an attention-and-words probe whose head weights are modulated by GloVe embeddings of the input words:

$$p(i \mid j) \propto \exp\!\Bigl(\sum_{k=1}^{n} W_{k,:}(v_i \oplus v_j)\,\alpha^k_{ij} + U_{k,:}(v_i \oplus v_j)\,\alpha^k_{ji}\Bigr)$$

Clustering of heads is performed using Jensen-Shannon divergence between attention distributions, visualized via multidimensional scaling.

## Key results
Certain individual heads achieve remarkably high accuracy on specific dependency relations without any training: head 8-11 achieves 94.3% on the determiner (det) relation, head 8-10 achieves 86.8% on direct objects (dobj), head 4-10 achieves 82.5% on passive auxiliaries (auxpass), and head 7-6 achieves 80.5% on possessives (poss). Head 5-4 achieves 65.1% accuracy on antecedent selection for coreference, close to a rule-based sieve system (69%) and far above the nearest-mention baseline (27%). No single head performs well overall (best is 34.5 UAS). The attention-and-GloVe probing classifier achieves 77 UAS, substantially above the distances-and-GloVe baseline (58 UAS) and comparable to a structural probe on BERT's vector representations (80 UUAS, undirected). Heads within the same layer tend to cluster together in behavior, suggesting layer-level coordination.

## Relevance to this research
This paper is directly relevant to the GL(K) gauge-equivariant attention framework in the VFE transformer. The finding that individual attention heads specialize to distinct linguistic functions parallels the theoretical motivation for multi-head attention in the VFE setting, where different heads can be understood as encoding different belief-coupling channels (the beta_{ij} terms in the free energy). The entropy analysis (Figure 4) — early layers with broad, high-entropy heads versus later layers with more focused heads — mirrors the layered VFE hierarchy (h → s → p → q) where early processing stages integrate over broad context and later stages sharpen to specific relations. The "no-op" interpretation of [SEP] attention (heads route attention to a null token when their specialized function is inapplicable) is conceptually related to the attention-entropy regularization term tau * beta_{ij} * log(beta_{ij}/pi_{ij}) in the VFE free energy: the softmax beta can concentrate on a null-information token as a minimum-cost strategy when the head's coupling function yields no signal. The JS-divergence-based head clustering foreshadows the need for diversity regularization among attention heads (cf. the model coupling gamma_{ij} terms), and the finding that same-layer heads behave similarly raises the question of whether gauge equivariance constraints naturally promote or suppress head diversity.

## Cross-links
- Concepts: [[Attention Mechanism]], [[Transformer Architecture]], [[Probing Classifiers]], [[Syntactic Structure in Neural Networks]]
- Related sources: [[vaswani2017attention]], [[devlin2019bert]]
- Manuscript/Project: [[GL(K) Attention Manuscript]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{clark2019does,
  author  = {Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D.},
  title   = {What Does {BERT} Look At? {An} Analysis of {BERT}'s Attention},
  year    = {2019},
  journal = {arXiv preprint arXiv:1906.04341},
}
```
