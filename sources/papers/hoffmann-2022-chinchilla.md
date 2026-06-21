---
type: paper
title: "Training Compute-Optimal Large Language Models"
aliases:
  - "Hoffmann 2022"
  - "Chinchilla"
  - "Chinchilla scaling laws"
authors:
  - Hoffmann, Jordan
  - Borgeaud, Sebastian
  - Mensch, Arthur
  - Buchatskaya, Elena
  - Cai, Trevor
  - Rutherford, Eliza
  - de Las Casas, Diego
  - Hendricks, Lisa Anne
  - Welbl, Johannes
  - Clark, Aidan
  - Hennigan, Tom
  - Noland, Eric
  - Millican, Katie
  - van den Driessche, George
  - Damoc, Bogdan
  - Guy, Aurelia
  - Osindero, Simon
  - Simonyan, Karen
  - Elsen, Erich
  - Rae, Jack W.
  - Vinyals, Oriol
  - Sifre, Laurent
year: 2022
arxiv: "2203.15556"
url: https://arxiv.org/abs/2203.15556
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Training Compute-Optimal Large Language Models

> [!info] Citation
> Hoffmann, J., Borgeaud, S., Mensch, A., et al. (2022). "Training Compute-Optimal Large Language Models." arXiv:2203.15556 [cs.CL].

## TL;DR
This paper investigates the optimal trade-off between model size and number of training tokens under a fixed compute budget for autoregressive transformer language models. Training over 400 models ranging from 70M to 16B parameters, the authors show that for compute-optimal training, model size and training tokens should scale in equal proportions — not the model-size-dominant regime suggested by Kaplan et al. (2020). They validate this by training Chinchilla (70B parameters, 1.4T tokens), which uses the same compute as Gopher (280B) yet uniformly outperforms Gopher, GPT-3, Jurassic-1, and Megatron-Turing NLG on a wide range of downstream tasks.

## Problem & setting
Prior work (Kaplan et al., 2020) established power-law scaling between model parameters and loss, leading the field to prioritize growing model size while keeping training data roughly fixed at ~300B tokens. Kaplan et al. recommended scaling parameters ~5.5x for every 10x compute increase, with tokens scaling only 1.8x. This paper revisits the same question — how to allocate a fixed FLOPs budget between model size $N$ and training tokens $D$ — using more diverse training runs and a learning-rate schedule correctly matched to training horizon.

## Method
The problem is formalized as minimizing the pre-training loss $L(N, D)$ subject to the constraint $\text{FLOPs}(N, D) = C$:

$$N_\text{opt}(C),\, D_\text{opt}(C) = \arg\min_{N,D\;\text{s.t.}\;\text{FLOPs}(N,D)=C} L(N,D)$$

Three complementary approaches are used to estimate $N_\text{opt}$ and $D_\text{opt}$:

1. **Fix model sizes, vary training tokens.** For each of several model sizes (70M–10B), train at four different token budgets; extract the minimum loss per FLOP count; fit power laws $N_\text{opt} \propto C^a$, $D_\text{opt} \propto C^b$.

2. **IsoFLOP profiles.** Fix nine FLOP budgets (6e18 to 3e21) and sweep model size, reading off the minimum-loss model at each budget; fit power laws to the resulting optima.

3. **Parametric loss model.** Fit the functional form $\hat{L}(N,D) = E + A/N^\alpha + B/D^\beta$ to all experimental runs using Huber loss minimized with L-BFGS; derive the closed-form efficient frontier $N_\text{opt}(C) = G(C/6)^a$, $D_\text{opt}(C) = G^{-1}(C/6)^b$ where $a = \beta/(\alpha+\beta)$, $b = \alpha/(\alpha+\beta)$.

All three approaches consistently find exponents near $a \approx 0.5$, $b \approx 0.5$, in contrast to Kaplan et al.'s $a = 0.73$, $b = 0.27$. A key methodological correction is that the learning-rate cosine schedule length should match the number of training tokens; using a fixed schedule (as in Kaplan et al.) biases estimates toward over-parameterized models.

## Key results
All three approaches agree: optimal scaling requires increasing model parameters and training tokens in approximately equal proportions with compute. Specifically (Approach 1/2): $N_\text{opt} \propto C^{0.50}$, $D_\text{opt} \propto C^{0.50}$. For the Gopher compute budget (~5.76e23 FLOPs), the optimal model is ~4x smaller (67B vs 280B) and should be trained on ~4x more tokens (1.5T vs 300B).

Chinchilla (70B, 1.4T tokens) at the Gopher compute budget achieves:
- 67.5% average 5-shot accuracy on MMLU (vs. 60.0% for Gopher 280B, vs. expert forecast of 63.4% for June 2023)
- +7.6% average improvement over Gopher on MMLU (51/57 tasks individually better)
- +10.7% average improvement over Gopher on BIG-bench (58/62 tasks better)
- Improvements on LAMBADA, RACE-h, RACE-m, Natural Questions, TriviaQA, and all The Pile evaluation subsets
- Substantially reduced inference and fine-tuning cost due to 4x smaller model size

## Relevance to this research
This paper is not directly connected to the gauge-theoretic VFE transformer. It concerns empirical scaling laws for standard autoregressive transformers trained by gradient descent with backprop — a paradigm orthogonal to the VFE framework, which replaces learned weights with iterative variational free energy minimization over Gaussian belief tuples. The Chinchilla result (data quantity matters as much as model size) could inform decisions about training corpus size in any future empirical evaluation of VFE transformer scaling, but no specific architectural, theoretical, or mathematical connection to GL(K) gauge-equivariant attention, SPD belief geometry, variational free energy, or information geometry applies.

## Cross-links
- Concepts: [[Transformer Architecture]], [[Scaling Laws]]
- Related sources: [[kaplan-2020-scaling-laws]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{HoffmannChinchilla2022,
  author  = {Hoffmann, Jordan and Borgeaud, Sebastian and Mensch, Arthur and Buchatskaya, Elena and Cai, Trevor and Rutherford, Eliza and de Las Casas, Diego and Hendricks, Lisa Anne and Welbl, Johannes and Clark, Aidan and Hennigan, Tom and Noland, Eric and Millican, Katie and van den Driessche, George and Damoc, Bogdan and Guy, Aurelia and Osindero, Simon and Simonyan, Karen and Elsen, Erich and Rae, Jack W. and Vinyals, Oriol and Sifre, Laurent},
  title   = {Training Compute-Optimal Large Language Models},
  year    = {2022},
  journal = {arXiv preprint arXiv:2203.15556},
  url     = {https://arxiv.org/abs/2203.15556},
}
```
