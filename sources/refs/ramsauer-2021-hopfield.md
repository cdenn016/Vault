---
type: reference
title: "Hopfield Networks Is All You Need"
aliases:
  - "Ramsauer et al 2021"
  - "Modern Hopfield Networks"
authors:
  - Hubert Ramsauer
  - Bernhard Schäfl
  - Johannes Lehner
  - Philipp Seidl
  - Michael Widrich
  - Lukas Gruber
  - Markus Holzleitner
  - Thomas Adler
  - David Kreil
  - Michael K. Kopp
  - Günter Klambauer
  - Johannes Brandstetter
  - Sepp Hochreiter
year: 2021
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/physics
created: 2026-06-18
updated: 2026-06-18
---

# Hopfield Networks Is All You Need

> [!info] Citation
> Ramsauer, H., Schäfl, B., Lehner, J., Seidl, P., Widrich, M., Gruber, L., Holzleitner, M., Adler, T., Kreil, D., Kopp, M. K., Klambauer, G., Brandstetter, J., & Hochreiter, S. (2021). *Hopfield Networks Is All You Need*. 9th International Conference on Learning Representations (ICLR 2021). arXiv:2008.02217.

## TL;DR

This paper introduces a **modern Hopfield network** with continuous states and shows that its energy-minimizing update rule is mathematically equivalent to the attention mechanism of transformers. The continuous Hopfield network stores exponentially many patterns (in the dimension of the associative space), retrieves them in a single update step, and has exponentially small retrieval error, recasting transformer attention as one step of associative-memory retrieval.

## What it establishes

The authors define a new energy function for a Hopfield network whose states are continuous rather than binary. The associated update rule, derived via the concave–convex procedure, takes a query, computes a softmax over inner products with stored patterns, and returns a weighted combination of those patterns. This update is shown to coincide exactly with the scaled dot-product attention of [[parr-2022-active-inference|transformers]] — more precisely, the softmax attention of Vaswani et al. (2017) is recovered as a single step of the continuous modern Hopfield retrieval dynamics, with queries, keys, and values playing the role of the probe, the stored patterns, and their projections.

Key results grounded in the paper:

- **Exponential storage capacity.** The number of patterns that can be stored and retrieved grows exponentially with the dimension of the pattern space, far exceeding the linear capacity of the classical binary Hopfield network.
- **One-step retrieval.** Under separation conditions on the stored patterns, the update converges to a fixed point (a stored pattern or a metastable mixture) after a single application of the rule.
- **Exponentially small retrieval error**, controlled by the pattern separation and the inverse-temperature parameter $\beta$.
- **Retrieval regimes.** Depending on $\beta$ and the geometry of the stored patterns, fixed points correspond either to retrieval of a single pattern, to **metastable states** that average over groups of similar patterns, or to a global fixed point averaging all patterns — giving attention an interpretable associative-memory semantics.
- A drop-in `Hopfield` layer that generalizes attention, pooling, and associative-memory lookup as configurable special cases.

> [!note] Editorial: The continuous-state energy and the single-update equivalence to softmax attention are the load-bearing contributions for this project; capacity and error bounds are stated here at the level used by the manuscripts rather than reproduced in full.

## Why the project cites it

This project reads transformer attention through a variational and information-geometric lens, and Ramsauer et al. supply the energy-based bridge that makes that reading principled. Several connections are concrete:

- **Attention as energy descent / inference.** Casting attention as one step of energy minimization aligns it with the project's view of a forward pass as approximate inference. The Hopfield energy plays a role analogous to a [[Variational free energy]] functional whose minimization performs retrieval, supporting the program of [[gl-k-attention]] that treats attention layers as inference steps rather than opaque mixers.

- **Softmax weighting as precision-weighted evidence.** The $\beta$-scaled softmax over query–key inner products is the same form the project uses for [[Precision weighting]] of [[Prediction error]]: $\beta$ acts as an inverse-temperature / precision controlling how sharply a probe selects among stored patterns. This connects the retrieval dynamics to the active-inference reading in [[Free-energy principle active inference]].

- **Metastable states as emergent structure.** The metastable fixed points that average over clusters of similar patterns give an associative-memory mechanism for coarse-graining tokens into groups, resonating with the project's themes of [[Meta-agents and hierarchical emergence]] and [[Renormalization-group flow of beliefs]], where structure at one scale condenses into effective units at the next.

- **Geometry of the retrieval landscape.** Because retrieval is governed by an energy on a continuous state space, the curvature and separation of the pattern landscape become objects amenable to the project's [[Fisher information metric]] and [[Natural gradient]] machinery, linking attention to [[Information geometry and natural gradient]].

In short, the paper is cited as the formal warrant that the project's attention modules are associative-memory / energy-minimization operations, letting the [[VFE Transformer Program]] inherit a clean variational reading of softmax attention from an established result.

## BibTeX

```bibtex
@inproceedings{ramsauer2021hopfield,
  title     = {Hopfield Networks Is All You Need},
  author    = {Ramsauer, Hubert and Sch{\"a}fl, Bernhard and Lehner, Johannes and
               Seidl, Philipp and Widrich, Michael and Gruber, Lukas and
               Holzleitner, Markus and Adler, Thomas and Kreil, David and
               Kopp, Michael K. and Klambauer, G{\"u}nter and
               Brandstetter, Johannes and Hochreiter, Sepp},
  booktitle = {9th International Conference on Learning Representations (ICLR)},
  year      = {2021},
  eprint    = {2008.02217},
  archivePrefix = {arXiv},
  primaryClass  = {cs.NE},
  url       = {https://arxiv.org/abs/2008.02217}
}
```
