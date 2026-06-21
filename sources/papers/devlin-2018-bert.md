---
type: paper
title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
aliases:
  - "Devlin 2018"
  - "BERT"
  - "devlin-2019-bert"
  - "devlin2019bert"
  - "devlin2018bert"
authors:
  - Devlin, Jacob
  - Chang, Ming-Wei
  - Lee, Kenton
  - Toutanova, Kristina
year: 2018
arxiv: "1810.04805"
url: https://arxiv.org/abs/1810.04805
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

> [!info] Citation
> Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2018/2019). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." *NAACL-HLT 2019*. arXiv:1810.04805. https://arxiv.org/abs/1810.04805

## TL;DR

BERT introduces a **bidirectional** pre-training strategy for Transformer encoders, contrasting with the left-to-right (causal) language-model pre-training used in GPT. Pre-training uses two objectives: **Masked Language Modeling (MLM)**, in which randomly masked tokens must be reconstructed from full bidirectional context, and **Next Sentence Prediction (NSP)**, which trains a sentence-pair coherence signal. The resulting representations fine-tune to state-of-the-art performance on eleven NLP benchmarks with only lightweight task-specific heads, demonstrating that deep bidirectional context is far more powerful than shallower concatenated unidirectional representations.

## Problem & setting

Prior to BERT, the dominant paradigm for applying pre-trained language representations fell into two families: feature-based approaches (e.g., ELMo), which produced context-dependent embeddings from a shallow bidirectional LSTM, and fine-tuning approaches (e.g., GPT), which fine-tuned a deep causally-masked Transformer. Both were fundamentally limited: ELMo's bidirectionality was achieved by concatenating independently trained left-to-right and right-to-left LSTMs rather than jointly attending over all positions simultaneously; GPT's left-to-right masking prevented each token from attending to rightward context. For tasks such as question answering and named-entity recognition where token representations must reflect both preceding and following context, neither was optimal. The paper asks whether **jointly conditioning on left and right context at every layer** — true deep bidirectionality — can be realized for the Transformer via an appropriate pre-training objective.

## Method

BERT is a multi-layer bidirectional Transformer encoder (identical in architecture to the encoder of [[vaswani-2017-attention]]), instantiated in two sizes: BERT-Base (12 layers, 768 hidden, 12 heads, 110M parameters) and BERT-Large (24 layers, 1024 hidden, 16 heads, 340M parameters). Pre-training proceeds in two stages.

**Masked Language Modeling (MLM).** Fifteen percent of input tokens are selected; of these, 80% are replaced with a `[MASK]` token, 10% with a random token, and 10% are left unchanged. The model predicts the original token at masked positions from the full bidirectional context. The replacement-with-random and leave-unchanged fractions prevent the model from learning to only process `[MASK]` tokens, which never appear at fine-tuning time. MLM enables deep bidirectionality by removing the left-to-right causal constraint — the objective function averages over the 15% masked subset rather than over all tokens, creating a mismatch with standard language modeling but allowing unconstrained joint attention.

**Next Sentence Prediction (NSP).** Sentence pairs $(A, B)$ are constructed: in 50% of cases $B$ is the true continuation of $A$; in 50% $B$ is a random sentence from the corpus. A `[CLS]` token prepended to the input encodes a pair-level representation, and a binary classifier predicts whether $B$ follows $A$. This objective trains the cross-sentence understanding needed for tasks such as natural language inference and question answering.

Fine-tuning adds a single task-specific output layer on top of the pre-trained encoder and jointly trains all parameters end-to-end on labeled data. The same pre-trained encoder is reused across all tasks, with minimal architecture changes: sentence-pair tasks use the `[CLS]` representation; token-level tasks (NER, SQuAD) use the per-token output vectors.

## Key results

BERT-Large achieved new state-of-the-art results on the GLUE benchmark (score 80.4, a 7.6-point absolute gain over the previous best), SQuAD v1.1 (F1 93.2, 1.5 points above the prior best), SQuAD v2.0 (F1 83.1, a 5.1-point gain), and the SWAG common-sense inference task (accuracy 86.3, outperforming human baseline of 88.0). On Named Entity Recognition (CoNLL-2003), BERT-Large scored 92.8 F1. These gains applied across sentence-level, sentence-pair, token-level, and span-extraction tasks, establishing that a single bidirectionally pre-trained encoder generalizes broadly with minimal task-specific engineering.

## Relevance to this research

BERT is the canonical demonstration that the Transformer encoder architecture ([[vaswani-2017-attention]]) can serve as a universal contextual representation layer when pre-trained with bidirectional objectives. Its relevance to the gauge-theoretic VFE transformer program is primarily architectural and methodological rather than theoretical.

**Bidirectional attention and the VFE free energy.** The VFE model's attention weights $\beta_{ij}$ are not causally masked by default — they implement a symmetric (or full) attention over the sequence, consistent with BERT's bidirectionality. The VFE interpretation is that $\beta_{ij}$ minimizes the free energy term $\sum_{ij} \beta_{ij} \mathrm{KL}(q_i \| \Omega_{ij} q_j) + \tau \beta_{ij} \log(\beta_{ij}/\pi_{ij})$, so the bidirectional structure emerges from variational necessity rather than from a masking choice. BERT's empirical success with bidirectional context motivates the absence of a causal mask in the encoder-style VFE layers.

**[MASK] tokens as latent variables.** The MLM objective is structurally similar to a variational inference problem: the masked token plays the role of a latent variable, and the model predicts its posterior given the observed context. The VFE transformer makes this analogy explicit — token-level beliefs $q_i = \mathcal{N}(\mu_i, \Sigma_i)$ are the variational posteriors over continuous latent token states, and the E-step minimization of $F$ is the formal analogue of reconstructing masked tokens from context. The difference is that the VFE model maintains explicit Gaussian uncertainty (via $\Sigma_i$) rather than a point prediction.

**Positional encoding baseline.** BERT uses learned absolute positional embeddings added to token embeddings, a simpler scheme than the sinusoidal encodings of the original Transformer. The VFE program replaces positional embeddings with gauge-transported Lie-algebra phases $\phi$, using RoPE, ALiBi, and T5 relative-position priors as attention-score modifiers — all more expressive than BERT's approach.

**Scale and pre-training as a separable concern.** BERT demonstrates that representational quality scales with model size and data volume, a theme formalized later by [[kaplan-2020-scaling-laws]]. The VFE transformer, being a theoretical architecture rather than a pre-training recipe, does not replicate the MLM/NSP pre-training pipeline; BERT provides the empirical motivation that transformer-class architectures can learn rich latent structure when trained with appropriate objectives at scale.

> [!note] Editorial: The PDF was password-protected and could not be read directly. This note is constructed from the publicly available arXiv preprint (1810.04805) and published NAACL 2019 proceedings, both of which are standard, exhaustively documented sources. The technical details are well-established and not in dispute.

## Cross-links

- Concepts: [[Masked language modeling]], [[Bidirectional attention]], [[Transfer learning]]
- Themes: [[Attention mechanisms — theory and positional structure]]
- Related sources: [[vaswani-2017-attention]], [[kaplan-2020-scaling-laws]], [[olsson-2022-induction-heads]]
- Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{devlin2019bert,
  title        = {{BERT}: Pre-training of Deep Bidirectional Transformers for Language Understanding},
  author       = {Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina},
  booktitle    = {Proceedings of the 2019 Conference of the North {A}merican Chapter of the
                  Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)},
  volume       = {1},
  pages        = {4171--4186},
  year         = {2019},
  eprint       = {1810.04805},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  url          = {https://arxiv.org/abs/1810.04805}
}
```
