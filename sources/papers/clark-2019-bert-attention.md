---
type: paper
title: "What Does BERT Look At? An Analysis of BERT's Attention"
aliases:
  - "Clark 2019"
  - "BERT attention analysis"
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
  - field/linguistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# What Does BERT Look At? An Analysis of BERT's Attention

> [!info] Citation
> Clark, K., Khandelwal, U., Levy, O., & Manning, C. D. (2019). "What Does BERT Look At? An Analysis of BERT's Attention." arXiv:1906.04341.

## TL;DR
This paper provides a systematic empirical analysis of the 144 attention heads in BERT-base, revealing that attention heads exhibit structured surface-level behaviors (attending to delimiter tokens, fixed positional offsets, or diffusely over the sentence) as well as linguistically meaningful specializations corresponding to syntactic dependency relations and coreference. An attention-based probing classifier combining BERT attention maps with GloVe embeddings achieves 77 UAS on dependency parsing, demonstrating that substantial syntactic knowledge is encoded in the attention mechanism itself — not merely in the hidden-state vectors.

## Problem & setting
Prior interpretability work on large pre-trained language models such as BERT focused either on model outputs (e.g., subject-verb agreement probes) or on internal vector representations via probing classifiers. Complementary to these, the authors ask what information is encoded in BERT's attention weights — a naturally interpretable quantity because each attention weight explicitly quantifies how much one token is weighted when computing the next representation for another. The analysis covers the 12-layer, 12-head (144 heads total) English BERT-base model.

## Method
The authors extract attention maps over 1000 Wikipedia segments and the Wall Street Journal Penn Treebank (annotated with Stanford Dependencies) and the CoNLL-2012 coreference dataset.

**Surface-level analysis.** For each head, they compute (a) how often it attends to the previous/next token, (b) how much total attention mass flows to special tokens ([CLS], [SEP], punctuation), and (c) the entropy of the attention distribution (low entropy = focused; high entropy = diffuse/bag-of-words). Gradient-based feature importance (magnitude of $|\partial L / \partial \alpha|$ for BERT's masked LM loss) is used to probe whether high attention to [SEP] is semantically meaningful or a no-op.

**Probing individual heads.** Each attention head is treated as a zero-parameter classifier: for a given word, it predicts the most-attended-to other word as the syntactic head (or antecedent). Accuracy is reported per dependency relation against Stanford Dependency gold labels. The softmax attention formula used is the standard:
$$\alpha_{ij} = \frac{\exp(q_i^\top k_j)}{\sum_l \exp(q_i^\top k_l)}, \quad o_i = \sum_j \alpha_{ij} v_j.$$

**Attention-based probing classifiers.** Two graph-based dependency probes are trained on top of frozen BERT attention maps. The attention-only probe learns a linear combination of head weights in both directions:
$$p(i \mid j) \propto \exp\!\Bigl(\sum_{k=1}^n w_k \alpha^k_{ij} + u_k \alpha^k_{ji}\Bigr).$$
The attention-and-words probe makes the linear coefficients word-sensitive by conditioning on GloVe embeddings $v$:
$$p(i \mid j) \propto \exp\!\Bigl(\sum_{k=1}^n W_{k,:}(v_i \oplus v_j)\,\alpha^k_{ij} + U_{k,:}(v_i \oplus v_j)\,\alpha^k_{ji}\Bigr).$$

**Head clustering.** Jensen-Shannon divergence between pairs of attention distributions is computed, and multidimensional scaling (Kruskal 1964) embeds all 144 heads in 2D for visualization.

## Key results
- A disproportionate share of BERT's attention (over 50% in layers 6-10) flows to [SEP]; gradient analysis shows this attention has near-zero influence on outputs, consistent with a no-op role.
- Four heads attend to the previous token with >50% average mass; five heads attend to the next token with >50% average mass — especially in early layers.
- Specific heads achieve striking per-relation accuracy with no training: det relation (head 8-11, 94.3%), dobj (head 8-10, 86.8%), auxpass (head 4-10, 82.5%), poss (head 7-6, 80.5%), pobj (head 9-6, 76.3%).
- One head (5-4) achieves 65% antecedent selection accuracy on CoNLL-2012 coreference, close to a rule-based sieve system (69%) and well above the nearest-mention baseline (27%).
- The attention + GloVe probing classifier reaches 77 UAS on Penn Treebank dependency parsing, comparable to the structural probe (80 UUAS, not directly comparable) operating on hidden states.
- Heads within the same layer tend to exhibit similar attention distributions, suggesting layer-level functional specialization.

## Relevance to this research
This paper is primarily empirical interpretability work on standard softmax attention (no gauge structure, no variational free energy), so it does not directly contribute mathematical content to the VFE/GL(K) program. Its relevance is as a reference point for what standard multi-head attention encodes and how it can be probed. Several connections are worth noting. First, the Jensen-Shannon divergence used to cluster heads is a natural information-geometric quantity closely related to the f-divergences (including KL) that appear throughout the VFE free-energy functional; the finding that within-layer heads cluster together resonates with the question of whether VFE attention heads also specialize by layer. Second, the "no-op" interpretation of high [SEP] attention — where a head routes attention to a dummy token when its specific function is not applicable — has a structural analogue in VFE attention: the beta_ij softmax weights are stationary points of F only when the attention-entropy term tau * beta_ij * log(beta_ij / pi_ij) is included, and degenerate attention (spiking to a single token) corresponds to a particular regime of that entropy balance. Third, the probing methodology (treating attention weights as zero-parameter classifiers of relational structure) is a useful empirical template for evaluating whether GL(K) gauge-equivariant heads specialize to structured relational patterns in the same way that BERT heads specialize to syntactic relations.

## Cross-links
- Concepts: [[Attention Mechanism]], [[Multi-Head Attention]], [[Transformer Architecture]]
- Related sources: [[vaswani-2017-attention]], [[devlin-2019-bert]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{Clark2019,
  author  = {Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D.},
  title   = {What Does {BERT} Look At? {A}n Analysis of {BERT}'s Attention},
  year    = {2019},
  journal = {arXiv preprint arXiv:1906.04341},
  url     = {https://arxiv.org/abs/1906.04341},
}
```
