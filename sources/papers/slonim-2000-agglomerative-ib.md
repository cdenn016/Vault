---
type: paper
title: "Agglomerative Information Bottleneck"
aliases:
  - "Slonim Tishby 2000"
  - "AgglomerativeIB"
authors:
  - Slonim, Noam
  - Tishby, Naftali
year: 2000
arxiv: null
url: null
tags:
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/statistics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Agglomerative Information Bottleneck

> [!info] Citation
> Slonim, N. & Tishby, N. (2000). "Agglomerative Information Bottleneck." Advances in Neural Information Processing Systems (NIPS 2000), pp. 617–623.

## TL;DR
Slonim and Tishby introduce a bottom-up, greedy agglomerative clustering algorithm that maximizes mutual information between a compressed representation and a relevance variable, framed as a "hard" (zero-temperature) limit of the Information Bottleneck (IB) method. At each step the algorithm merges the pair of clusters whose join minimizes the loss in mutual information, with the merge cost equal to the Jensen-Shannon divergence between the cluster conditional distributions. On the 20 Newsgroups corpus the method achieves three-orders-of-magnitude compression while retaining 90% of the relevant mutual information.

## Problem & setting
The Information Bottleneck method (Tishby, Bialek & Pereira, 1998) seeks a compressed representation $\hat{X}$ of a variable $X$ that maximally preserves information about a relevance variable $Y$, by minimizing the Lagrangian $\mathcal{L}[p(\hat{x}|x)] = I(X;\hat{X}) - \beta I(\hat{X};Y)$. The original IB algorithm solved the resulting self-consistent equations via deterministic annealing (a top-down "soft," stochastic approach). The paper asks: is there a simpler, fully deterministic, bottom-up algorithm that works in the hard-clustering ($\beta \to \infty$) limit for any desired number of clusters?

## Method
Starting from the trivial $N$-partition (one cluster per data point), the algorithm greedily merges the pair $\{Z_i, Z_j\}$ that minimizes the mutual-information decrease

$$
\Delta I_Y(Z_i, Z_j) = \bigl(p(Z_i) + p(Z_j)\bigr) \cdot \mathrm{JS}_{\pi_2}\!\bigl[p(Y|Z_i),\, p(Y|Z_j)\bigr],
$$

where $\mathrm{JS}_{\pi_2}$ is the Jensen-Shannon divergence with prior $\pi_i = p(Z_i)/(p(Z_i)+p(Z_j))$. The key insight is Proposition 1: the mutual-information loss of merging a pair depends only on the two clusters' conditional distributions and priors, computable in $O(|Y|)$ per pair rather than $O(m \cdot |Y|)$, reducing total cost by a factor of $m$ per merge. After hard clusters are obtained, "reverse annealing" (decreasing $\beta$ in the original IB equations) softens them, recovering the full deterministic-annealing phase diagram without needing to locate cluster splits.

The update rules for the merged cluster $Z_k = Z_\alpha \cup Z_\beta$ are:
$$
p(Z_k) = p(Z_\alpha)+p(Z_\beta), \quad p(y|Z_k) = \frac{p(Z_\alpha,y)+p(Z_\beta,y)}{p(Z_k)}.
$$

## Key results
The agglomerative algorithm yields fully deterministic hard partitions for every cardinality from $N$ down to 1 in a single pass. On the 20 Newsgroups corpus: (1) the two-class subset (5 765 strings) is compressed to 50 clusters with only 0.1% mutual-information loss, and to 6 clusters retaining 90% of $I(X;Y)$; (2) the 20-class NG100 dataset (5 148 strings) compressed to 515 clusters retains 86% of mutual information, to 50 clusters retains ~70%. In the information plane (normalized $I(Z;Y)$ vs. $I(Z;X)$) the hard algorithm is suboptimal relative to the soft IB, but provides an excellent initialization for reverse annealing, which then recovers the globally optimal "rate-distortion" curve. The mutual-information decrease per merge, $\delta(m) = \frac{I(Z_m;Y) - I(Z_{m-1};Y)}{I(Z_m;Y)}$, is empirically found to be increasing as $m$ decreases, offering a natural stopping criterion for meaningful cluster number.

## Relevance to this research
The Information Bottleneck framework is a foundational precursor to the VFE / active-inference treatment of attention: both frame representation learning as a constrained mutual-information (or KL-divergence) optimization. The KL divergence $D_{\mathrm{KL}}[p(Y|x)\|p(Y|\hat{x})]$ that appears in the IB self-consistent equations is structurally identical to the belief-coupling KL terms in the VFE free-energy functional. The Lagrange multiplier $\beta$ (inverse temperature) maps directly to the inverse softmax temperature $\tau^{-1} = (\kappa\sqrt{d})^{-1}$ controlling the attention sharpness in GL(K) attention. The Jensen-Shannon divergence merge criterion provides an information-geometric view of cluster similarity that connects to the SPD/Riemannian geometry of Gaussian belief tuples $(\mu, \Sigma)$ used in VFE3. The "hard vs. soft clustering" duality (agglomerative IB vs. deterministic annealing) mirrors the distinction between hard (MAP) and soft (variational) inference modes available in the VFE transformer. The paper's "information plane" analysis — tracking $I(Z;Y)$ vs. $I(Z;X)$ as compression increases — is a precursor to information-geometric analyses of the attention mechanism's compression-fidelity trade-off central to the GL(K) manuscript.

## Cross-links
- Concepts: [[Information Bottleneck]] · [[Mutual Information]] · [[Jensen-Shannon Divergence]] · [[Distributional Clustering]] · [[Deterministic Annealing]]
- Related sources: [[tishby-2000-information-bottleneck]] · [[pereira-1993-distributional-clustering]]
- Manuscript/Project: [[VFE Transformer Program]] · [[GL(K) Attention]]

## BibTeX
```bibtex
@inproceedings{SlonimTishby2000,
  author    = {Slonim, Noam and Tishby, Naftali},
  title     = {Agglomerative Information Bottleneck},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {12},
  pages     = {617--623},
  year      = {2000},
}
```
