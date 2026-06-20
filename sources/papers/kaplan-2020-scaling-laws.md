---
type: paper
title: "Scaling Laws for Neural Language Models"
aliases:
  - "Kaplan et al. 2020"
  - "Kaplan (2020) Scaling Laws"
authors:
  - Jared Kaplan
  - Sam McCandlish
  - Tom Henighan
  - Tom B. Brown
  - Benjamin Chess
  - Rewon Child
  - Scott Gray
  - Alec Radford
  - Jeffrey Wu
  - Dario Amodei
year: 2020
arxiv: "2001.08361"
url: https://arxiv.org/abs/2001.08361
tags:
  - cluster/methodology
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/cs-ml
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Scaling Laws for Neural Language Models

> [!info] Citation
> Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei (2020). "Scaling Laws for Neural Language Models." arXiv:2001.08361. <https://arxiv.org/abs/2001.08361>

## TL;DR

This paper establishes that the cross-entropy loss of autoregressive transformer language models falls as a smooth **power law** in each of three resources — the number of non-embedding parameters $N$, the dataset size $D$, and the compute budget $C$ — across more than seven orders of magnitude. The exponents are small and stable, model shape (depth-versus-width, attention-head count) matters far less than total scale, and the curves are predictive enough to forecast the loss of a model before it is trained. This is the founding empirical document of the modern scaling-law genre that [[Neural scaling laws]] and the Chinchilla revision ([[hoffmann-2022-chinchilla]]) build on.

## Problem & setting

The motivating question is whether language-model performance is a chaotic function of architecture and hyperparameters or a lawful function of scale. The authors train decoder-only transformers on WebText2 over wide ranges of $N$, $D$, and $C$, holding the recipe otherwise fixed, and ask how test loss responds.

## Method

Systematic sweeps over model size, data, batch size, and training steps, with loss measured in nats per token. The empirical fits take the form $L(N) \approx (N_c/N)^{\alpha_N}$, $L(D) \approx (D_c/D)^{\alpha_D}$, and a combined $L(N, D)$ surface, with a separate critical-batch-size analysis relating data parallelism to serial steps.

## Key results

- Loss is a clean power law in $N$, $D$, and $C$ individually, with $\alpha_N \approx 0.076$ and $\alpha_D \approx 0.095$; the exponents are small, so each tenfold increase in scale buys a modest but reliable loss reduction.
- Architectural shape (aspect ratio, head count, feed-forward ratio) is largely irrelevant compared to total parameter count, an empirical universality.
- Large models are markedly more sample-efficient; under a fixed compute budget the loss-optimal strategy (per this paper) is to train very large models on relatively modest data and stop well short of convergence — a prescription later corrected by Chinchilla.
- Overfitting, learning-rate schedules, and transfer all scale predictably, making pre-training loss forecastable from small-scale runs.

## Relevance to this research

PIFB ([[participatory-it-from-bit]]) advances an **inverse-$K$ scaling** claim: because the model's representational capacity lives in the belief dimension $K$ of the Gaussian tuples $(\mu, \Sigma, \phi)$ rather than in learned weight matrices, the manuscript predicts how the achievable free-energy floor behaves as $K$ grows. PIFB anchors this against Chinchilla, but Kaplan et al. is the foundational document the entire genre rests on, and it is the right primary citation for the *form* of the law — a power law in a capacity variable with a small exponent — that PIFB is recapitulating in an unusual coordinate (capacity = belief dimension, not parameters). Their finding that loss is governed by total scale and is nearly indifferent to architectural shape is congenial to the PIFB thesis that the heavy lifting is done by iterative [[Variational free energy]] minimization, not by architectural machinery; the no-neural-network constraint of this project is, in this reading, a bet that the scaling exponent is a property of the inference problem rather than of the parameterization. The capacity-floor reading also touches the information-bottleneck framing ([[Information bottleneck]]): a power-law loss-versus-capacity curve is what one expects when accuracy is traded against a complexity budget.

## Cross-links

- Concepts: [[Neural scaling laws]], [[Information bottleneck]], [[Variational free energy]]
- Sources: [[hoffmann-2022-chinchilla]], [[vaswani-2017-attention]]
- Project: [[participatory-it-from-bit]], [[Gauge-Theoretic Multi-Agent VFE Model]]

```bibtex
@article{kaplan2020scaling,
  title         = {Scaling Laws for Neural Language Models},
  author        = {Kaplan, Jared and McCandlish, Sam and Henighan, Tom and
                   Brown, Tom B. and Chess, Benjamin and Child, Rewon and
                   Gray, Scott and Radford, Alec and Wu, Jeffrey and Amodei, Dario},
  journal       = {arXiv preprint arXiv:2001.08361},
  year          = {2020},
  eprint        = {2001.08361},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url           = {https://arxiv.org/abs/2001.08361}
}
```
