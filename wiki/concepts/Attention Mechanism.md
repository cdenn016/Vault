---
type: concept
title: "Attention Mechanism"
aliases:
  - "Attention mechanism"
  - "Attention Mechanisms"
  - "Attention mechanisms"
tags:
  - cluster/attention
  - project/transformer
status: draft
created: 2026-06-21
updated: 2026-06-21
---

# Attention Mechanism

An **attention mechanism** is a content-based weighting rule that lets a model route information dynamically: instead of using a fixed wiring, each output position computes how much to draw from every input position by comparing them. It originated as the additive content-based alignment of [[bahdanau-2014-neural-machine-translation]] for neural machine translation, and was crystallized into its modern form — *scaled dot-product attention* — by the Transformer of [[vaswani-2017-attention]].

## Core formalism

Given queries $Q$, keys $K$, and values $V$ (linear projections of the inputs), scaled dot-product attention is

$$
\operatorname{Attention}(Q,K,V) = \operatorname{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V .
$$

Each query row scores every key by dot product, the scores are normalized into a probability distribution by the [[Softmax]] (the $\sqrt{d_k}$ scaling keeps logits in the soft regime), and the resulting weights take a convex combination of the values. The mechanism is permutation-equivariant on its own, so sequence order must be supplied separately by a positional encoding. In practice it is run as **[[Multi-head attention]]**: several independent $(Q,K,V)$ projections attend in parallel and their outputs are concatenated, letting different heads specialize in different relational patterns — empirically, identifiable syntactic and coreference structure, as catalogued by [[clark-2019-bert-attention]]. Standard attention is quadratic in sequence length; [[Linear attention]] and [[Sparse Attention]] trade exactness for cheaper scaling.

## The precision-weighting reading

This program reads attention through a Bayesian lens: the attention weights are not an arbitrary learned similarity but a **precision-weighted prediction-error gate**. In predictive coding and active inference, prediction errors are scaled by their *precision* (inverse variance) before propagation, so attention becomes a statement about *which sources to trust*, not merely which look similar. [[feldman-friston-2010-attention]] makes the identification explicit — attention *is* the optimization of expected precision in hierarchical free-energy minimization. See [[Precision weighting]] for the full correspondence between the attention matrix and the precision-weighted E-step.

## The gauge-theoretic reinterpretation

In the vfe3 / V3_Transformer each token is a Gaussian belief $(\mu,\Sigma)$ rather than a point vector, expressed in a per-token gauge frame. Attention then transports one token's belief into another's frame before comparing them, with the transport operator $\Omega_{ij}=\exp(\phi_i)\exp(-\phi_j)$ built from gauge Lie-algebra elements. The affinity becomes a precision-weighted Mahalanobis distance between transported means — the Gaussian KL $D_{\mathrm{KL}}[q_i\,\Vert\,\Omega_{ij}q_j]$ — recovering ordinary dot-product attention only in the flat, identity-metric limit. Each head acts as a block-diagonal $\mathrm{GL}(k_h)$ channel; the details, including the stationary-point derivation of the softmax weights, live in [[GL(K) gauge-equivariant attention]].

> [!note] Editorial: This page is the definitional hub. The full theory — attention as kernel smoothing, the positional-encoding family (RoPE/ALiBi/T5), SPD-Riemannian affinities, and the open questions — is synthesized in the theme page below; this page deliberately stays at the level of definition and orientation.

## See also

- [[Attention mechanisms — theory and positional structure]] — the synthesis theme (kernel view, positional structure, geometric affinities)
- [[GL(K) gauge-equivariant attention]] · [[Precision weighting]] · [[Multi-head attention]]
- [[Softmax]] · [[Linear attention]] · [[Sparse Attention]]
