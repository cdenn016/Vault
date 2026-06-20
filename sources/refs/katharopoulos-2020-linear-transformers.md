---
type: reference
title: "Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention"
aliases:
  - "Katharopoulos 2020"
  - "Linear Transformers"
authors:
  - Angelos Katharopoulos
  - Apoorv Vyas
  - Nikolaos Pappas
  - François Fleuret
year: 2020
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
created: 2026-06-18
updated: 2026-06-18
---

# Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention

> [!info] Citation
> Katharopoulos, A., Vyas, A., Pappas, N., & Fleuret, F. (2020). *Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention.* Proceedings of the 37th International Conference on Machine Learning (ICML), PMLR 119:5156–5165. arXiv:2006.16236.

## TL;DR

This paper rewrites self-attention as a linear dot product of kernel feature maps, $\text{sim}(q, k) = \phi(q)^\top \phi(k)$, and exploits the associativity of matrix products to reduce the per-token cost of attention from $O(N^2)$ to $O(N)$ in sequence length $N$. In the causal (autoregressive) regime this yields an exact recurrent formulation with a constant-size running state, exposing a formal equivalence between a class of transformers and recurrent neural networks and accelerating autoregressive inference by up to several thousand-fold.

## What it establishes

The central move is to replace the softmax kernel $\exp(q^\top k / \sqrt{d})$ with a generalized, factorizable similarity $\text{sim}(q, k) = \phi(q)^\top \phi(k)$ for a nonnegative feature map $\phi$. The standard attention output for query $i$,

$$
V'_i = \frac{\sum_j \text{sim}(Q_i, K_j)\, V_j}{\sum_j \text{sim}(Q_i, K_j)},
$$

then becomes

$$
V'_i = \frac{\phi(Q_i)^\top \sum_j \phi(K_j) V_j^\top}{\phi(Q_i)^\top \sum_j \phi(K_j)},
$$

so the aggregated quantities $\sum_j \phi(K_j) V_j^\top$ and $\sum_j \phi(K_j)$ are computed once and reused across all queries, giving linear time and memory. The authors adopt the elementwise feature map $\phi(x) = \mathrm{elu}(x) + 1$, which keeps the similarity positive without requiring an explicit high-dimensional random feature expansion.

In the causal case, the running sums become **states** $S_i = \sum_{j \le i} \phi(K_j) V_j^\top$ and $Z_i = \sum_{j \le i} \phi(K_j)$ that update additively as each token arrives, $S_i = S_{i-1} + \phi(K_i) V_i^\top$. This is precisely a recurrent neural network with a fixed-dimensional hidden state, evaluated in constant time and memory per step regardless of how many tokens precede it — the result that gives the paper its title and its large speedups on long autoregressive sequences.

## Why the project cites it

The project's [[VFE Transformer Program]] reads attention not as an opaque similarity table but as a mechanism for belief aggregation across tokens, and Katharopoulos 2020 supplies the structural template that makes such a reading tractable. By factorizing the similarity through a feature map, linear attention turns the all-pairs interaction into the maintenance of a **sufficient running state**, which aligns directly with the project's treatment of [[Belief inertia|belief inertia]] and the recurrent, state-carrying view of inference: each token updates an accumulated belief rather than recomputing global compatibility from scratch.

The exposed transformer–RNN equivalence is the relevant hook for the manuscripts' filtering perspective on [[Inference machinery — variational EM and filtering|sequential inference]]. Casting causal attention as a recurrence with additive state updates makes contact with [[Hamiltonian belief dynamics|belief dynamics]] over a sequence, and with the [[gl-k-attention]] line of work, where the kernel feature map $\phi$ is the natural place to inject geometric or [[Group equivariance|equivariant]] structure into the similarity. Because $\text{sim}(q,k) = \phi(q)^\top \phi(k)$ is an inner product in feature space, it is the obvious surface on which to impose the [[Fisher information metric|information-geometric]] and [[Gauge transformation|gauge-covariant]] inner products the project develops, rather than the unstructured softmax.

> [!note] Editorial: The connections to [[Variational free energy|VFE]], belief-state filtering, and gauge-structured similarity are positioning by this wiki for the project's program; the cited paper itself is a machine-learning efficiency and architecture result and makes no claims about active inference or information geometry.

## BibTeX

```bibtex
@inproceedings{katharopoulos2020transformers,
  title     = {Transformers are {RNNs}: Fast Autoregressive Transformers with Linear Attention},
  author    = {Katharopoulos, Angelos and Vyas, Apoorv and Pappas, Nikolaos and Fleuret, Fran{\c{c}}ois},
  booktitle = {Proceedings of the 37th International Conference on Machine Learning (ICML)},
  series    = {Proceedings of Machine Learning Research},
  volume    = {119},
  pages     = {5156--5165},
  year      = {2020},
  publisher = {PMLR},
  eprint    = {2006.16236},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG}
}
```
