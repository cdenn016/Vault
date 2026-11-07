---
type: paper
title: "Learning Efficient Multi-agent Communication: An Information Bottleneck Approach"
aliases: ["IMAC", "Wang et al. 2020 information bottleneck communication"]
authors: ["Rundong Wang", "Xu He", "Runsheng Yu", "Wei Qiu", "Bo An", "Zinovi Rabinovich"]
year: 2020
venue: "ICML 2020; PMLR 119:9908–9918"
url: "https://proceedings.mlr.press/v119/wang20i.html"
version: "Published conference paper"
tags: [cluster/multi-agent, cluster/attention, cluster/info-geometry, project/multi-agent, project/transformer, field/cs-ml, field/statistics]
created: 2026-11-07
updated: 2026-11-07
---

# Learning Efficient Multi-agent Communication: An Information Bottleneck Approach

> [!info] Citation
> Wang, R., He, X., Yu, R., Qiu, W., An, B., and Rabinovich, Z. (2020). *Learning Efficient Multi-agent Communication: An Information Bottleneck Approach*. Proceedings of ICML, PMLR 119, 9908–9918. [Proceedings record](https://proceedings.mlr.press/v119/wang20i.html); [published PDF](https://proceedings.mlr.press/v119/wang20i/wang20i.pdf).

[Local proceedings PDF](../pdfs/wang-2020-information-bottleneck-communication.pdf), 11 pages; retrieved November 7, 2026.

## TL;DR

IMAC learns stochastic communication and recipient-specific scheduling with information-bottleneck penalties alongside task-return objectives.

## Problem & setting

Agents communicate through a scheduler. Section 4 relates message entropy to bandwidth under specified sampling, quantization, signaling, and noiseless-channel assumptions; entropy is not intrinsically a physical bit-rate budget.

## Method

Sections 5.1–5.2 penalize $I(H_i;M_i)$ for messages and $I(C_i;M_1,\ldots,M_n)$ for scheduled inputs. Variational KL bounds against reference distributions make these penalties trainable. Centralized critics support training, with gradients crossing recipient, scheduler, and sender modules. Section 5.3 simulates bandwidth constraints by reducing message variance during execution.

## Key results

The paper compares communication efficiency in particle-world navigation, predator–prey, and StarCraft II tasks. The measured gains are task- and bandwidth-setting dependent. Variance clipping is the implemented constraint proxy, not a demonstrated physical communication stack.

## Relevance to this research

The method separates compression and routing within [[Communication-constrained inference]]. Its return-minus-information objective should not be identified with [[Expected Free Energy]] without an additional derivation. Learned weighted aggregates also do not establish the covariance properties of [[GL(K) gauge-equivariant attention]] or identify a receiver's private generative model.

## Cross-links

[[Active inference communication and collective boundaries]]; [[kim-2019-schednet]]; [[lin-2021-autoencoder-communication]].

## BibTeX

```bibtex
@inproceedings{pmlr-v119-wang20i,
  author = {Wang, Rundong and He, Xu and Yu, Runsheng and Qiu, Wei and An, Bo and Rabinovich, Zinovi},
  title = {Learning Efficient Multi-agent Communication: An Information Bottleneck Approach},
  booktitle = {Proceedings of the 37th International Conference on Machine Learning},
  series = {Proceedings of Machine Learning Research},
  volume = {119},
  pages = {9908--9918},
  year = {2020},
  publisher = {PMLR},
  url = {https://proceedings.mlr.press/v119/wang20i.html}
}
```
