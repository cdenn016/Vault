---
type: paper
title: "Mistral 7B"
aliases:
  - "Jiang 2023"
  - "Mistral 7B"
authors:
  - Jiang, Albert Q.
  - Sablayrolles, Alexandre
  - Mensch, Arthur
  - Bamford, Chris
  - Chaplot, Devendra Singh
  - de las Casas, Diego
  - Bressand, Florian
  - Lengyel, Gianna
  - Lample, Guillaume
  - Saulnier, Lucile
  - Lavaud, Lélio Renard
  - Lachaux, Marie-Anne
  - Stock, Pierre
  - Le Scao, Teven
  - Lavril, Thibaut
  - Wang, Thomas
  - Lacroix, Timothée
  - El Sayed, William
year: 2023
arxiv: "2310.06825"
url: https://arxiv.org/abs/2310.06825
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Mistral 7B

> [!info] Citation
> Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D. S., de las Casas, D., Bressand, F., Lengyel, G., Lample, G., Saulnier, L., Lavaud, L. R., Lachaux, M.-A., Stock, P., Le Scao, T., Lavril, T., Wang, T., Lacroix, T., & El Sayed, W. (2023). "Mistral 7B." arXiv:2310.06825.

## TL;DR
Mistral 7B is a 7-billion-parameter open language model that outperforms Llama 2 13B across all evaluated benchmarks and Llama 1 34B on reasoning, mathematics, and code generation tasks. It achieves this through two key architectural innovations: grouped-query attention (GQA) for faster, memory-efficient inference, and sliding window attention (SWA) for handling arbitrarily long sequences at reduced computational cost. The model is released under the Apache 2.0 license and demonstrates that carefully designed smaller models can substantially outperform larger ones.

## Problem & setting
Scaling language models to higher performance typically requires increasing parameter counts, which raises inference latency and deployment costs. The challenge is to achieve strong performance across diverse NLP tasks while maintaining practical inference efficiency. Prior open models such as Llama 1 and Llama 2 had set the performance baseline at the 7B–34B scale; Mistral 7B aims to surpass them at 7B parameters by architectural choice rather than brute-force scaling.

## Method
Mistral 7B adopts a standard transformer backbone (32 layers, dim 4096, 32 attention heads) with two principal modifications. Sliding window attention (SWA) restricts each token to attend to at most $W = 4096$ tokens in the previous layer; through $k$ stacked layers this gives an effective receptive field of $k \times W$ tokens (approximately 131K at the final layer), avoiding the quadratic cost of full attention. A rolling buffer cache of fixed size $W$ replaces the growing KV cache: keys and values at position $i$ are stored at index $i \bmod W$, reducing cache memory by $8\times$ on 32K-token sequences without quality loss. Grouped-query attention (GQA) uses 8 KV heads shared across 32 query heads, substantially accelerating inference and reducing memory bandwidth. For instruction following, a fine-tuned variant (Mistral 7B – Instruct) is trained on publicly available instruction datasets without proprietary data.

## Key results
On the standard benchmark suite (MMLU, HellaSwag, Winogrande, PIQA, ARC, NaturalQuestions, TriviaQA, HumanEval, MBPP, MATH, GSM8K), Mistral 7B scores 60.1% on MMLU, 81.3% on HellaSwag, 30.5% on HumanEval, and 52.2% on GSM8K — exceeding Llama 2 13B on every metric. In reasoning and STEM tasks, Mistral 7B effectively matches what would be expected of a Llama 2 model more than 3× its size. The instruction-fine-tuned model achieves an MT-Bench score of 6.84, outperforming all 7B chat models and matching 13B-class chat models on human preference evaluations. The self-reflection content moderation prompt achieves 99.4% precision and 95.6% recall on an adversarial safety dataset.

## Relevance to this research
Mistral 7B is not directly related to the gauge-theoretic VFE transformer; it is a conventional neural language model using standard backpropagation and learned weight matrices throughout. However, two of its architectural ideas are of incidental technical interest. First, sliding window attention provides a local-neighborhood inductive bias on sequence structure, which connects loosely to the locality assumptions in belief-coupling terms $\beta_{ij}$ of the VFE free-energy functional. Second, grouped-query attention is a factorization of the key-value space that reduces redundancy across heads, a different approach to multi-head efficiency than the gauge-equivariant per-irrep structure used in GL(K) attention. The primary relevance is as a reference point for open-model scaling efficiency, not as a theoretical precursor.

## Cross-links
- Concepts: [[Attention Mechanism]]
- Related sources: [[vaswani2017-attention]], [[touvron2023-llama2]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{jiang2023mistral,
  author  = {Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and de las Casas, Diego and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and Lavaud, L{\'e}lio Renard and Lachaux, Marie-Anne and Stock, Pierre and Le Scao, Teven and Lavril, Thibaut and Wang, Thomas and Lacroix, Timoth{\'e}e and El Sayed, William},
  title   = {Mistral 7B},
  year    = {2023},
  journal = {arXiv preprint arXiv:2310.06825},
}
```
