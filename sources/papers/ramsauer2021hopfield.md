---
type: paper
title: "Hopfield Networks is All You Need"
aliases:
  - Ramsauer 2021
  - Hopfield Attention
  - Modern Hopfield Networks
  - ramsauer-2021-hopfield
  - Ramsauer et al 2021
authors:
  - Ramsauer, Hubert
  - Schäfl, Bernhard
  - Lehner, Johannes
  - Seidl, Philipp
  - Widrich, Michael
  - Adler, Thomas
  - Gruber, Lukas
  - Holzleitner, Markus
  - Pavlovic, Milena
  - Sandve, Geir Kjetil
  - Greiff, Victor
  - Kreil, David
  - Kopp, Michael
  - Klambauer, Günter
  - Brandstetter, Johannes
  - Hochreiter, Sepp
year: 2021
arxiv: "2008.02217"
url: https://arxiv.org/abs/2008.02217
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/physics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Hopfield Networks is All You Need

> [!info] Citation
> Ramsauer, H., Schäfl, B., Lehner, J., Seidl, P., Widrich, M., Adler, T., Gruber, L., Holzleitner, M., Pavlovic, M., Sandve, G. K., Greiff, V., Kreil, D., Kopp, M., Klambauer, G., Brandstetter, J., & Hochreiter, S. (2021). "Hopfield Networks is All You Need." ICLR 2021. arXiv:2008.02217.

## TL;DR

This paper introduces a modern Hopfield network with continuous states and a new update rule that can store exponentially many patterns, retrieves patterns with a single update step, and has exponentially small retrieval errors. The central result is that this new update rule is mathematically equivalent to the key-value attention mechanism used in transformer models, providing an associative memory interpretation of dot-product attention. Three specialized Hopfield layers (Hopfield, HopfieldPooling, HopfieldLayer) are proposed as drop-in building blocks for deep learning architectures beyond standard fully-connected, convolutional, or recurrent networks.

## Problem & setting

Classical Hopfield networks (Hopfield 1982) have storage capacity only $O(d / \log d)$ for $d$-dimensional patterns, making them impractical for deep learning use. Dense associative memory (DAM) models (Krotov & Hopfield 2016, 2018) increased capacity to $O(d^{n-1})$ with polynomial interaction functions $F(x) = x^n$, and Demircigil et al. (2017) reached exponential capacity $2^{d/2}$ using $F(x) = \exp(x)$, but only for binary patterns. The open problem was to generalize to continuous states and integrate differentiable Hopfield dynamics into deep learning as standard layers.

## Method

The authors propose a new energy function for continuous-state modern Hopfield networks:

$$E = -\mathrm{lse}(\beta, X^T \xi) + \tfrac{1}{2}\xi^T\xi + \beta^{-1}\log N + \tfrac{1}{2}M^2$$

where $\mathrm{lse}(\beta, x) = \beta^{-1} \log \sum_i \exp(\beta x_i)$ is the log-sum-exp, $X = (x_1,\ldots,x_N)$ are the stored key patterns, $\xi$ is the current state (query), and $M = \max_i \|x_i\|$. The update rule that minimizes $E$ via the Concave-Convex Procedure (CCCP) is:

$$\xi_{\mathrm{new}} = X \, \mathrm{softmax}(\beta X^T \xi)$$

This is proven to converge globally (Theorems 1 and 2). The critical observation is that under the substitution $X^T \to K = Y W_K$, $\xi \to Q = R W_Q$, and post-multiplication by $W_V$, this update rule becomes exactly transformer scaled dot-product attention:

$$Z = \mathrm{softmax}\!\left(\frac{1}{\sqrt{d_k}} Q K^T\right) V$$

with $\beta = 1/\sqrt{d_k}$. Three Hopfield layer types are introduced: (1) Hopfield for set-to-set association (equivalent to transformer self-attention), (2) HopfieldPooling for summarizing variable-size sets with learned static queries, and (3) HopfieldLayer for querying a fixed external memory (equivalent to cross-attention with a reference store).

## Key results

Theorem 3 (Storage Capacity): For random patterns on the sphere of radius $M = K\sqrt{d-1}$, the number of storable patterns is $N \geq \sqrt{p} \, c^{(d-1)/4}$ with failure probability $p$, yielding exponential capacity (e.g., $c \geq 3.15$ for $\beta=1$, $K=3$, $d=20$). Theorem 4 shows retrieval with one update step when patterns are well-separated: the distance to the fixed point is exponentially small in the separation $\Delta_i = x_i^T x_i - \max_{j \neq i} x_i^T x_j$. Theorem 5 provides an exponentially small retrieval error $\|f(\xi) - x_i\| \leq 2(N-1)\exp(-\beta \Delta_i)M$. Empirically, Hopfield layers set new state-of-the-art on immune repertoire classification (DeepRC, AUC 0.832), three of four MIL benchmark datasets, the UCI small classification benchmark (best average rank among all methods tested), and two of four drug design datasets.

## Relevance to this research

This paper is directly relevant to the VFE transformer program in two ways. First, the equivalence between the Hopfield update rule and softmax attention (Eq. 10 here vs the $\beta_{ij} = \mathrm{softmax}(\tau^{-1} \cdot \text{KL-costs})$ coupling weights in the GL(K) attention manuscript) establishes the associative memory interpretation of the VFE attention mechanism: the $\beta$-weighted retrieval from key patterns corresponds to the variational belief coupling term $\sum_{ij} \beta_{ij} \mathrm{KL}(q_i \| \Omega_{ij} q_j)$. Second, the energy function structure $E = -\mathrm{lse}(\beta, X^T\xi) + \frac{1}{2}\|\xi\|^2$ parallels the self-coupling term $\alpha \cdot \mathrm{KL}(q_i \| p_i)$ in the VFE free energy: both pin the state to a prior/reference via a regularizing quadratic term while allowing soft retrieval from stored patterns. The metastable-state characterization of BERT heads (global averaging in lower layers, sparse retrieval in higher layers) resonates with the multi-scale belief coupling structure across the VFE transformer's $h \to s \to p \to q$ hierarchy. The paper also provides a concrete prior art reference for the PriorBank decode: storing learned prototypes in HopfieldLayer memory is exactly the PriorBank $\{(\mu_k^p, \Sigma_k^p)\}$ used for KL-to-prior decoding in vfe3.

## Cross-links
- Concepts: [[Attention Mechanism]], [[Variational Free Energy]], [[Softmax]], [[Associative Memory]], [[Energy-Based Models]], [[Precision weighting]], [[Information geometry and natural gradient]]
- Themes: [[Meta-agents and hierarchical emergence]], [[Renormalization-group flow of beliefs]]
- Related sources: [[vaswani2017attention]], [[friston2022active]], [[krotov2016dense]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) Attention Manuscript]]

> [!note] Editorial: Depending on $\beta$ and the pattern geometry, fixed points fall into three regimes — single-pattern retrieval, **metastable states** that average over clusters of similar patterns, or a global fixed point averaging all patterns. The metastable regime gives attention an associative-memory mechanism for coarse-graining tokens into groups, resonating with the project's [[Meta-agents and hierarchical emergence]] and [[Renormalization-group flow of beliefs]] themes (structure at one scale condensing into effective units at the next).

## BibTeX
```bibtex
@inproceedings{ramsauer2021hopfield,
  author    = {Ramsauer, Hubert and Sch{\"a}fl, Bernhard and Lehner, Johannes and Seidl, Philipp
               and Widrich, Michael and Adler, Thomas and Gruber, Lukas and Holzleitner, Markus
               and Pavlovic, Milena and Sandve, Geir Kjetil and Greiff, Victor and Kreil, David
               and Kopp, Michael and Klambauer, G{\"u}nter and Brandstetter, Johannes
               and Hochreiter, Sepp},
  title     = {Hopfield Networks is All You Need},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2021},
  url       = {https://arxiv.org/abs/2008.02217},
}
```
