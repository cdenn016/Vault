---
type: paper
title: "Language Models are Unsupervised Multitask Learners"
aliases:
  - "Radford 2019"
  - "GPT-2"
  - "radford-2019-gpt2"
  - "Radford et al. 2019"
authors:
  - Radford, Alec
  - Wu, Jeffrey
  - Child, Rewon
  - Luan, David
  - Amodei, Dario
  - Sutskever, Ilya
year: 2019
arxiv: null
url: https://openai.com/research/better-language-models
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Language Models are Unsupervised Multitask Learners

> [!info] Citation
> Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). "Language Models are Unsupervised Multitask Learners." OpenAI technical report / OpenAI Blog. PDF: <https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf>

## TL;DR
GPT-2 demonstrates that a Transformer language model trained on a large, diverse web-scraped corpus (WebText, 40 GB) learns to perform a wide range of NLP tasks in a zero-shot setting, without any task-specific fine-tuning. The 1.5B parameter model achieves state-of-the-art results on 7 out of 8 language modeling benchmarks zero-shot. The key finding is that model capacity is essential to zero-shot task transfer, with performance improving log-linearly with scale across tasks.

## Problem & setting
Prior NLP systems were narrow experts trained on single-task, single-domain datasets with supervised labels. Multitask learning was nascent and required explicit (dataset, objective) pairs that were expensive to construct at scale. The paper asks whether a language model trained on sufficiently diverse text can learn to perform many tasks implicitly, without supervision, by modeling the conditional distribution p(output | input, task) through natural language prompting.

## Method
The approach is auto-regressive language modeling — estimating p(x) = prod_i p(s_i | s_1, ..., s_{i-1}) over sequences of tokens via a modified Transformer decoder architecture (GPT-style). Four model sizes are trained (117M to 1542M parameters), all following the GPT architecture (Radford et al., 2018) with modifications: layer normalization moved to sub-block inputs (pre-activation residual), an additional layer normalization after the final self-attention block, residual layer weights scaled by 1/sqrt(N) at initialization, vocabulary expanded to 50,257 tokens, context window increased to 1024 tokens. Training uses Byte Pair Encoding (BPE) applied at the byte level to handle arbitrary Unicode strings without lossy preprocessing. The WebText dataset consists of 45 million Reddit-linked web pages (filtered to karma >= 3) deduplicated to ~8 million documents and 40 GB. Zero-shot task evaluation is performed by conditioning the model on natural language context that specifies the task format (e.g., "TL;DR:" for summarization, question-answer pairs for translation/QA).

## Key results
GPT-2 (1.5B parameters) achieves state-of-the-art zero-shot perplexity on 7 of 8 tested language modeling benchmarks including WikiText-2 (18.34 PPL), Penn Treebank (35.76 PPL), LAMBADA (8.63 PPL; 63.24% accuracy), Children's Book Test (93.3% on common nouns, 89.1% on named entities), and Winograd Schema Challenge (70.70%, +7% over prior SOTA). On CoQA reading comprehension, GPT-2 reaches 55 F1 without any of the 127,000+ supervised training examples that baselines used. Summarization (CNN/DailyMail ROUGE) and translation (WMT-14, 5 BLEU En-Fr) remain weak, well below supervised methods. Performance improves log-linearly with model capacity across all tasks. Data overlap analysis via Bloom filters on 8-grams shows 1-6% WebText/test-set overlap, a small but consistent contribution to results. All models still underfit WebText, suggesting further gains with additional compute.

## Relevance to this research
GPT-2's Transformer architecture is the dominant baseline against which the VFE transformer's GL(K) gauge-equivariant attention mechanism is contrasted. Where GPT-2 learns task representations implicitly through maximum likelihood over token sequences, the VFE framework derives attention weights as the stationary point of a variational free energy functional with explicit belief geometry (Gaussian tuples (mu, Sigma, phi)) and gauge-equivariant transport. The log-linear scaling of zero-shot performance with capacity in GPT-2 is relevant context for understanding what the VFE transformer's inductive biases (gauge equivariance, SPD belief geometry) buy beyond raw parameter count. GPT-2's autoregressive factorization p(output | input, task) is a special case of the conditional modeling framework that the VFE approach generalizes via the observation likelihood term E_q[log p(o | x)] in the free energy. The BPE tokenization and pre-norm residual architecture details are standard engineering choices also inherited by VFE3's input encoding layer.

## Cross-links
- Concepts: [[Transformer Architecture]], [[Self-Attention]], [[Language Modeling]], [[Zero-Shot Learning]]
- Related sources: [[vaswani2017-attention]], [[radford2018-gpt1]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{radford2019language,
  author  = {Radford, Alec and Wu, Jeffrey and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya},
  title   = {Language Models are Unsupervised Multitask Learners},
  year    = {2019},
  url     = {https://openai.com/research/better-language-models},
}
```
