---
type: paper
title: "Linear Transformers Are Secretly Fast Weight Programmers"
aliases:
  - Schlag 2021
  - schlag2021linear
  - Fast weight programmers
authors:
  - Schlag, Imanol
  - Irie, Kazuki
  - Schmidhuber, Jürgen
year: 2021
arxiv: "2102.11174"
pdf: sources/pdfs/schlag-2021-fast-weight-programmers.pdf
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
created: 2026-10-24
---

# Linear Transformers Are Secretly Fast Weight Programmers

> [!info] Citation
> Schlag, I., Irie, K., & Schmidhuber, J. (2021). *Linear transformers are secretly fast weight programmers*. Proceedings of the 38th International Conference on Machine Learning (ICML 2021), PMLR 139. arXiv:2102.11174.

## TL;DR
Linearized self-attention is formally a fast weight programmer: a slow network writes additive key–value outer products into a fast weight matrix that is then queried. This exposes a finite memory capacity, and the paper replaces the purely additive write by a delta-rule update with a learned, input-dependent learning rate, which corrects the stored key-to-value map.

## Method
The fast weight recursion is $W^{(i)}=\sigma(W^{(i-1)}+a^{(i)}\otimes b^{(i)})$ with output $y^{(i)}=W^{(i)}x^{(i)}$ (Eqs. 1–3). With a kernel feature map in place of softmax, causal linear attention accumulates $\sum_j v_j\phi(k_j)^\top$ in exactly this way. The delta-rule write subtracts the currently retrieved value before adding the new one (in the manner of Widrow and Hoff). Experiments cover synthetic retrieval, machine translation and language modeling, together with a new kernel feature map.

## Relevance to this research
An in-context meta-agent over a Gaussian template bank, restricted to the causal prefix, keeps additive per-template sufficient statistics such as $\sum_{i<t}w_{ia}$, $\sum_{i<t}w_{ia}m_{ia}$ and second moments. That state is a fast weight memory written by responsibilities. The capacity argument and the delta-rule correction are the matching cautions for such a memory, and conjugate Bayesian updating ([[broderick-2013-streaming-variational-bayes]]) is the probabilistic version of the write rule ([[Associative Memory]], [[Meta-agents and hierarchical emergence]]).

## Cross-links
- Concepts: [[Associative Memory]], [[Meta-agents and hierarchical emergence]]
- Related sources: [[broderick-2013-streaming-variational-bayes]], [[ramsauer2021hopfield]], [[sukhbaatar-2019-persistent-memory]]

## BibTeX
```bibtex
@inproceedings{schlag2021linear,
  author    = {Schlag, Imanol and Irie, Kazuki and Schmidhuber, J{\"u}rgen},
  title     = {Linear Transformers Are Secretly Fast Weight Programmers},
  booktitle = {Proceedings of the 38th International Conference on Machine Learning},
  series    = {Proceedings of Machine Learning Research},
  volume    = {139},
  year      = {2021},
  eprint    = {2102.11174},
  archivePrefix = {arXiv}
}
```
