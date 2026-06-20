---
type: paper
title: A Mathematical Framework for Transformer Circuits
aliases:
  - "Elhage et al. 2021"
  - "A Mathematical Framework for Transformer Circuits"
authors:
  - Nelson Elhage
  - Neel Nanda
  - Catherine Olsson
  - Tom Henighan
  - Chris Olah
  - et al.
year: 2021
arxiv: null
url: https://transformer-circuits.pub/2021/framework/index.html
tags:
  - cluster/attention
  - cluster/methodology
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A Mathematical Framework for Transformer Circuits

> [!info] Citation
> Elhage, N., Nanda, N., Olsson, C., Henighan, T., Joseph, N., Mann, B., et al. (2021). A Mathematical Framework for Transformer Circuits. Transformer Circuits Thread (Anthropic). https://transformer-circuits.pub/2021/framework/index.html

## TL;DR

This paper recasts the decoder-only transformer as a system of additive, largely independent computations communicating through a single shared vector space — the **residual stream** — and shows that, once nonlinearities are set aside (attention-only models with frozen patterns), the entire network becomes a *linear* map that can be expanded into a sum of human-readable end-to-end paths from tokens to logits. Within this picture each attention head factors into two near-independent pieces: a **QK circuit** $W_Q^\top W_K$ that decides *where* a head attends, and an **OV circuit** $W_O W_V$ that decides *what* it writes if it attends. Reading these low-rank matrices directly off the weights, the authors fully account for one-layer models as ensembles of bigrams and "skip-trigrams," and then show that two-layer models acquire qualitatively new power through *composition* of heads across layers — culminating in the discovery of **induction heads**, the circuit responsible for a large fraction of in-context learning. It is the founding document of the mechanistic-interpretability program and the canonical reference for the residual-stream / QK-OV decomposition of attention.

## Problem & setting

The standard presentation of a transformer — embed, then alternate multi-head attention and MLP blocks with residual connections and layer norm, then unembed — is operationally complete but interpretively opaque: the concatenate-heads-and-project formulation tangles together computations that are in fact separable. The authors take the prior architecture of Vaswani et al. (2017) and the GPT-style decoder-only stack and ask what the weights *mean*. They restrict to **attention-only** transformers (no MLPs) of zero, one, and two layers so that, with attention patterns held fixed, every remaining operation is linear and the whole model is a product of matrices that can be multiplied out and inspected. The ambition is reverse-engineering: to read algorithms off trained weights rather than only observing input-output behavior, building on the circuits tradition from vision interpretability but adapting it to the sequence-mixing structure unique to attention.

## Method

The central reframing is the **residual stream** as a communication channel. Every component reads from the stream by a linear projection, performs its computation, and writes back by *adding* a linear projection — so heads and layers are not a pipeline but a set of independent writers contributing additively to one running sum $x$. Embeddings write the token identity in, the unembedding reads the final state out, and each attention head moves information between token positions.

A single head is written, using the tensor (Kronecker) product, as
$$ h(x) = \big(A \otimes W_O W_V\big)\cdot x, $$
where $A$ is the attention pattern — an $n_{\text{ctx}} \times n_{\text{ctx}}$ matrix mixing across token positions — and $W_O W_V$ acts within the per-token feature space. This factorization makes precise the claim that *where* a head attends and *what* it copies are separate computations. The attention pattern is the **QK circuit**
$$ A = \mathrm{softmax}\!\left(\frac{x^\top W_Q^\top W_K\, x}{\sqrt{d_k}}\right), $$
governed entirely by the bilinear form $W_Q^\top W_K$; the **OV circuit** $W_O W_V$ governs the value written. Because $W_Q^\top W_K$ and $W_O W_V$ each factor through the small head dimension $d_k$, both are low-rank, and the per-head split of the model dimension is what makes these factors interpretable objects rather than full-rank residual-space maps.

The analytic engine is **path expansion**. Multiplying out the matrix products (with attention frozen) yields the logits as a sum of terms, each a "path" through the network. For a one-layer model the expansion is the direct (embedding $\to$ unembedding) path plus, for each head, a term routing token content through that head's OV circuit under its QK-determined pattern. For two layers, paths that traverse two heads produce **virtual attention heads**, and the authors classify how an early head can feed a later one as **Q-composition**, **K-composition** (both altering *where* the later head looks, and so very different from value routing), or **V-composition** (altering *what* it moves). Induction heads are the canonical two-head circuit: a previous-token head composes with a later head so that the model attends to the token that followed the current token last time it appeared, implementing the rule "$[A][B]\dots[A]\to[B]$."

## Key results

The framework establishes, by direct weight inspection rather than only behavioral probing, a hierarchy of capability by depth. Zero-layer attention-only models can express only bigram statistics, readable straight from the embedding-unembedding product. One-layer models are characterized completely as ensembles of bigram and **skip-trigram** functions of the form "A … B C": the OV circuit's eigenvalue/copying structure determines which tokens get copied, and the QK circuit determines the skip-pattern, so the model's repertoire is enumerable from the weights. Two-layer models cross a qualitative threshold: composition of heads yields algorithms unavailable to any single layer, and the authors identify **induction heads** as the dominant such mechanism and connect them to in-context learning. The evidence is a mix of exact algebra (the path expansions and circuit factorizations are mathematical identities) and empirical case studies on small trained models (eigenvalue analyses of OV circuits, attention-pattern inspection, ablations); it is a conceptual-framework paper, so its strength is the decomposition's exactness and explanatory reach rather than large-scale benchmark numbers. The induction-head thread it opens is pursued quantitatively in the companion in-context-learning work.

## Relevance to this research

This is the canonical source for the residual-stream and QK/OV-circuit decomposition — the very architectural object the gauge-theoretic VFE transformer reinterprets. Where Elhage et al. write a head as $A \otimes W_O W_V$ with $A$ a softmax QK pattern and $W_O W_V$ a low-rank per-head map, the program replaces the value transport by a gauge factor $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ acting between token beliefs and treats heads as **block-diagonal $\mathrm{GL}(K_h)$ channels** writing additively into a shared belief stream — a structurally exact analogue of the additive residual stream, with the QK softmax pattern recovered by the attention weights $\beta_{ij}$ at the stationary point of the free energy. The OV/QK split therefore tells the program which of its objects plays the *where* role (the $\beta$/transport coupling) versus the *what* role (the gauge-transported value), and the residual-stream-as-additive-channel framing licenses reading each head as an independent writer into $(\mu,\Sigma,\phi)$. This paper is also the parent framework of the [[olsson-2022-induction-heads|induction-heads]] result already catalogued in the vault, and it grounds the program's interpretability claims against canonical mechanistic structure rather than bespoke notation. See [[Mechanistic interpretability of attention]], [[Attention mechanisms — theory and positional structure]], and [[Transformer interpretability and scaling]].

## Cross-links

- Concepts / Themes: [[Mechanistic interpretability of attention]], [[Attention mechanisms — theory and positional structure]], [[Transformer interpretability and scaling]]

## BibTeX

```bibtex
@article{elhage2021transfor,
  author  = {Elhage, Nelson and Nanda, Neel and Olsson, Catherine and Henighan, Tom and Joseph, Nicholas and Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and Conerly, Tom and DasSarma, Nova and Drain, Dawn and Ganguli, Deep and Hatfield-Dodds, Zac and Hernandez, Danny and Jones, Andy and Kernion, Jackson and Lovitt, Liane and Ndousse, Kamal and Amodei, Dario and Brown, Tom and Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},
  title   = {A Mathematical Framework for Transformer Circuits},
  journal = {Transformer Circuits Thread},
  year    = {2021},
  publisher = {Anthropic},
  url     = {https://transformer-circuits.pub/2021/framework/index.html}
}
```
