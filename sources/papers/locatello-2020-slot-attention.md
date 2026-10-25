---
type: paper
title: "Object-Centric Learning with Slot Attention"
aliases:
  - Locatello 2020
  - locatello2020object
  - Slot attention
authors:
  - Locatello, Francesco
  - Weissenborn, Dirk
  - Unterthiner, Thomas
  - Mahendran, Aravindh
  - Heigold, Georg
  - Uszkoreit, Jakob
  - Dosovitskiy, Alexey
  - Kipf, Thomas
year: 2020
arxiv: "2006.15055"
pdf: sources/pdfs/locatello-2020-slot-attention.pdf
tags:
  - cluster/attention
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
  - field/cs-ml
created: 2026-10-24
---

# Object-Centric Learning with Slot Attention

> [!info] Citation
> Locatello, F., Weissenborn, D., Unterthiner, T., Mahendran, A., Heigold, G., Uszkoreit, J., Dosovitskiy, A., & Kipf, T. (2020). *Object-centric learning with slot attention*. NeurIPS 2020. arXiv:2006.15055.

## TL;DR
A set of $K$ exchangeable slots is refined over a few iterations of dot-product attention to the input features. The attention coefficients are normalized over the slots rather than over the inputs, so slots compete to explain each input, and each slot is updated with a GRU from the weighted mean of the inputs it claims.

## Method
Slots are initialized randomly from a learned Gaussian and refined for $T$ iterations (Algorithm 1). Normalizing over slots, "introduces competition between the slots for explaining parts of the input" (Section 2.1). The paper relates the routing to soft k-means clustering and to mixtures of experts (Section 4). Trained without supervision it discovers objects, and it generalizes to unseen compositions and more objects.

## Relevance to this research
The normalization axis is the point of contact with the prototype layer of [[VFE Transformer Program|vfe3]]: there each token's weights are normalized over templates (a token chooses a template), while slot attention normalizes over slots for each input (inputs are partitioned among slots), the E-step of clustering inputs into slots. Slot attention is the in-context, iterated version of "parents fit to the current population", which the prototype bank lacks because it is learned only across the corpus. It supplies a learned, non-probabilistic precedent for an in-context meta-agent update ([[Meta-agents and hierarchical emergence]]).

## Cross-links
- Concepts: [[Meta-agents and hierarchical emergence]]
- Methods: [[Template routing]]
- Related sources: [[hinton-2018-matrix-capsules-em-routing]], [[sukhbaatar-2019-persistent-memory]]

## BibTeX
```bibtex
@inproceedings{locatello2020object,
  author    = {Locatello, Francesco and Weissenborn, Dirk and Unterthiner, Thomas and Mahendran, Aravindh and Heigold, Georg and Uszkoreit, Jakob and Dosovitskiy, Alexey and Kipf, Thomas},
  title     = {Object-Centric Learning with Slot Attention},
  booktitle = {Advances in Neural Information Processing Systems 33},
  year      = {2020},
  eprint    = {2006.15055},
  archivePrefix = {arXiv}
}
```
