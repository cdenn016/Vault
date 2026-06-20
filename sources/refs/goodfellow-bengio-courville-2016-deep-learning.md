---
type: reference
title: "Deep Learning"
aliases:
  - "Goodfellow, Bengio & Courville 2016 — Deep Learning"
  - "The Deep Learning Book"
authors:
  - Ian Goodfellow
  - Yoshua Bengio
  - Aaron Courville
year: 2016
url: https://www.deeplearningbook.org/
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
created: 2026-06-20
updated: 2026-06-20
---

# Deep Learning

> [!info] Citation
> Ian Goodfellow, Yoshua Bengio, and Aaron Courville (2016). *Deep Learning*. MIT Press, Cambridge, MA. ISBN 978-0-262-03561-3. <https://www.deeplearningbook.org/>

## TL;DR

The standard graduate textbook of the modern deep-learning era, organized in three parts: applied mathematics and machine-learning background (linear algebra, probability, numerical computation, gradient-based optimization), deep networks proper (feedforward nets, regularization, optimization for training, convolutional and recurrent architectures), and a research survey (representation learning, structured probabilistic models, Monte Carlo methods, the partition function, approximate inference, and deep generative models). It is the reference the project reaches for when a piece of conventional deep-learning machinery — backpropagation, finite-difference gradient checking, numerical-stability practice, or a baseline optimizer — needs a canonical citation rather than a re-derivation.

## Relevance to this research

General deep-learning background, not VFE research theory: the gauge-theoretic VFE transformer is a no-neural-network construction (no `nn.Linear`, no MLP, no activations) whose capacity comes from iterative free-energy minimization, so it does not build on this book's network architectures. It is cited as background for the machinery the project *is* permitted to use — backpropagation and reverse-mode automatic differentiation for computing VFE gradients, and the finite-difference gradient-checking discipline that pins those gradients against an autograd-of-$F$ oracle in the test suite. The numerical-analyst audit lens and the ML-engineer debate lens cite it for exactly this conventional-DL grounding (gradient checking, numerical stability, baseline optimizers), against which the model's no-NN, Fisher-natural-gradient design is contrasted.

> [!note] Editorial: Cited as the standard deep-learning reference for conventional background (backprop, gradient checking, optimization), not for any architecture the VFE model adopts — the model is explicitly no-neural-network. The "finite-difference gradient checking" tie is to the project's golden/finite-difference gradient tests, a practice the book describes generically rather than a result it owns.

## Cross-links

- Theme: [[Transformer interpretability and scaling]]
- Project: [[VFE Transformer Program]]
- Related sources: [[vaswani-2017-attention]], [[von-oswald-2022-transformers-gradient-descent]], [[geshkovski-2023-mathematical-transformers]]

## BibTeX

```bibtex
@book{goodfellow2016deep,
  title     = {Deep Learning},
  author    = {Goodfellow, Ian and Bengio, Yoshua and Courville, Aaron},
  publisher = {MIT Press},
  address   = {Cambridge, MA},
  year      = {2016},
  isbn      = {978-0-262-03561-3},
  url       = {https://www.deeplearningbook.org/}
}
```
