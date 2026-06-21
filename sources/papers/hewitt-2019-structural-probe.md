---
type: paper
title: "A Structural Probe for Finding Syntax in Word Representations"
aliases:
  - Hewitt 2019
  - structural probe
  - hewitt-manning-2019-structural-probe
  - Hewitt & Manning 2019
authors:
  - Hewitt, John
  - Manning, Christopher D.
year: 2019
arxiv: null
url: https://aclanthology.org/N19-1419
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A Structural Probe for Finding Syntax in Word Representations

> [!info] Citation
> Hewitt, John and Manning, Christopher D. (2019). "A Structural Probe for Finding Syntax in Word Representations." Proceedings of NAACL-HLT 2019, pages 4129–4138. Minneapolis, Minnesota. https://aclanthology.org/N19-1419

## TL;DR
This paper introduces a structural probe — a learned low-rank linear transformation $B \in \mathbb{R}^{k \times m}$ — that tests whether entire parse trees are implicitly embedded in the word representation space of deep language models. The probe identifies a transformation under which squared L2 distance encodes tree distance between words, and squared L2 norm encodes depth in the parse tree. Applied to ELMo and BERT, the probe reveals that both models embed full dependency parse trees with high fidelity in a surprisingly low-dimensional (rank ~64–128) subspace, whereas uninformed baselines fail to encode this global syntactic structure.

## Problem & setting
Despite strong empirical performance, it remains unclear whether contextual word representations from deep models (ELMo, BERT) encode entire syntactic parse trees or only local dependency cues. Prior probing work tested specific syntactic phenomena but did not test whether global tree structure is preserved. This paper asks: does there exist an inner product on the representation space such that pairwise squared distances encode all tree distances simultaneously? The setting uses the Penn Treebank with Stanford Dependencies formalism.

## Method
The structural probe learns a matrix $B \in \mathbb{R}^{k \times m}$ (where $m$ is the representation dimension and $k \leq m$ is a rank hyperparameter) that minimizes the L1 loss between predicted and true tree distances over all word pairs in all sentences:

$$d_B(h_i^\ell, h_j^\ell)^2 = \left(B(h_i^\ell - h_j^\ell)\right)^T \left(B(h_i^\ell - h_j^\ell)\right)$$

$$\min_B \sum_\ell \frac{1}{|s^\ell|^2} \sum_{i,j} \left| d_{T^\ell}(w_i^\ell, w_j^\ell) - d_B(h_i^\ell, h_j^\ell)^2 \right|$$

This is equivalent to finding a positive semi-definite matrix $A = B^T B$ that defines an inner product on the original space. A companion depth probe trains $B$ to predict parse depth via squared norms $\|Bh_i\|^2$. The probe is trained with Adam (lr=0.001) and evaluated via UUAS (undirected unlabeled attachment score from minimum spanning trees on predicted distances) and Spearman correlations (DSpr., NSpr.).

## Key results
BERT-large achieves 82.5 UUAS and DSpr. 0.86 on the distance probe (Penn Treebank WSJ test set), and 89.4% root accuracy with NSpr. 0.88 on the depth probe. ELMo-layer-1 achieves 77.0 UUAS and DSpr. 0.83, versus the best baseline (PROJ0, randomly initialized BiLSTM) at 59.8 UUAS and DSpr. 0.73. Syntactic information peaks at middle layers for both models. The effective rank of the necessary transformation saturates around $k = 64$–$128$ across all three models (ELMo, BERT-base, BERT-large), suggesting syntax occupies a compact, low-dimensional subspace of the representation space.

## Relevance to this research
The structural probe's central insight — that geometric structure (distances and norms) in a transformed subspace encodes relational structure (parse trees) — is directly analogous to the VFE transformer's use of SPD belief geometry, where inner products on the GL(K)-transformed belief space encode information-geometric distances. The low-rank subspace finding parallels the use of rank-K gauge group representations: syntactic structure uses only a small part of the full ambient space, mirroring how the VFE model concentrates representational capacity in a K-dimensional latent geometry. The probe's formulation of a family of inner products $h^T A h$ parametrized by a PSD matrix $A = B^T B$ is exactly the Mahalanobis-type metric that appears in the GL(K) attention kernel. This paper provides empirical grounding for the idea that structured relational information is encoded in the geometry of representation spaces, supporting the geometric approach to attention taken in the VFE transformer. It is also the empirical foil for the PIFB **parse-completeness conjecture** (that the belief representation, under iterative free-energy minimization, comes to encode the full syntactic structure needed to predict the next token): because parse distance appears here as a *learned linear metric*, the project can ask whether parse-tree distance is recoverable from the *intrinsic* belief metric — the affine-invariant/Mahalanobis distance defined by the SPD covariance $\Sigma$ — rather than from a separately trained probe matrix.

## Cross-links
- Concepts: [[SPD-manifold geometry and Riemannian optimization|SPD Geometry]], [[GL(K) Gauge Group]], [[Information Geometry]], [[Attention Mechanism]], [[Mechanistic interpretability of attention]]
- Related sources: [[devlin-2018-bert|devlin-2019-bert]], [[peters-2018-elmo]], [[clark-2019-bert-attention]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) gauge-equivariant attention|GL(K) Attention]], [[participatory-it-from-bit]]

## BibTeX
```bibtex
@inproceedings{Hewitt2019,
  author    = {Hewitt, John and Manning, Christopher D.},
  title     = {A Structural Probe for Finding Syntax in Word Representations},
  booktitle = {Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)},
  pages     = {4129--4138},
  year      = {2019},
  address   = {Minneapolis, Minnesota},
  publisher = {Association for Computational Linguistics},
  url       = {https://aclanthology.org/N19-1419},
}
```
