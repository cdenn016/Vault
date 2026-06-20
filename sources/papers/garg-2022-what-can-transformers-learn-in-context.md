---
type: paper
title: "What Can Transformers Learn In-Context? A Case Study of Simple Function Classes"
aliases: ["Garg 2022", "What Can Transformers Learn In-Context? A Case Study of Simple Function Classes"]
authors: ["Shivam Garg", "Dimitris Tsipras", "Percy Liang", "Gregory Valiant"]
year: 2022
arxiv: 2208.01066
url: https://arxiv.org/abs/2208.01066
tags: [cluster/attention, project/transformer, field/cs-ml]
created: 2026-06-20
updated: 2026-06-20
---

# What Can Transformers Learn In-Context? A Case Study of Simple Function Classes

> [!info] Citation
> Shivam Garg, Dimitris Tsipras, Percy Liang, Gregory Valiant (2022). *What Can Transformers Learn In-Context? A Case Study of Simple Function Classes*. NeurIPS 2022; arXiv:2208.01066. https://arxiv.org/abs/2208.01066

## TL;DR

Shows empirically that transformers trained from scratch can in-context learn simple function classes (linear functions, sparse linear, two-layer ReLU nets, decision trees) at the level of the optimal estimator, treating in-context learning as a learned algorithm rather than memorization.

## Relevance to this research

Empirical in-context-learning study; complements the present von-Oswald gradient-descent-in-attention note on what attention computes.

## Cross-links

- Concepts: [[Mechanistic interpretability of attention]]
- Theme: [[Attention mechanisms — theory and positional structure]]
- Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@inproceedings{garg2022incontext,
  author={Garg, Shivam and Tsipras, Dimitris and Liang, Percy and Valiant, Gregory},
  title={What Can Transformers Learn In-Context? A Case Study of Simple Function Classes},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2022}
}
```
