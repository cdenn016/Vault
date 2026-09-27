---
type: reference
title: "Probabilistic Transformers"
aliases:
  - "Movellan and Gabbur 2020"
  - "Probabilistic Transformers"
  - "Movellan2020ProbabilisticTransformers"
authors:
  - Javier R. Movellan
  - Prasad Gabbur
year: 2020
arxiv: "2010.15583"
url: https://arxiv.org/abs/2010.15583
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-09-23
updated: 2026-09-23
---

# Probabilistic Transformers

> [!info] Citation
> Javier R. Movellan and Prasad Gabbur (2020). "Probabilistic Transformers." arXiv preprint [arXiv:2010.15583](https://arxiv.org/abs/2010.15583) (v3 read).

## TL;DR

A six-page note showing that the transformer attention update is the maximum a posteriori (MAP) value estimate in a mixture-of-Gaussians model over memory units, computed by expectation maximization (EM). With equal precisions and a prior that is tied to the key and value norms, the norm terms cancel, and dot-product attention is recovered in one EM step.

## What it establishes

Each queried unit $i$ has a joint model of queries and values that is a mixture over units $j$ with mixing probabilities $\pi_{i,j}$ (Eq. 2). The EM responsibilities $w_{i,j}=p_i(u_j\mid q,v^t)$ (Eq. 5) play the role of the attention matrix. Queries and values are generated independently given the active unit (Eq. 7), each from an isotropic Gaussian centered on the unit's key $\xi_j$ or expected value $\mu_j$ with precisions $\alpha_i,\beta_i$ (Eqs. 8–9). The EM maximization step is then the responsibility-weighted mixture mean $v^{t+1}=\sum_jw^t_{i,j}\mu_j$ (Eq. 14). Section "Relation to Standard Transformers" equalizes the precisions across units and links the unit priors to the key and value lengths, $\pi_{i,j}\propto e^{\frac{\alpha}{2}\lVert\xi_j\rVert^2}e^{\frac{\beta}{2}\lVert\mu_j\rVert^2}$ (Eq. 16). This prior cancels the norm terms of the Gaussian likelihoods, and in the limit $\beta\to0$ the weights become $w_{i,j}\propto e^{\alpha\xi_j^\top q}$ with a single EM iteration (Eqs. 20–21), which is standard dot-product attention. The remaining sections use the same model for online unsupervised adaptation of keys under a Gaussian prior (Eqs. 22–29), adaptation of precisions under a Gamma prior (Eq. 30), and online propagation of values supplied at inference time (Eqs. 31 onward).

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript cites this note as the point-query precedent for its Section 4 shared-covariance reduction and compensating prior. The independent content law (Eq. 7), the mixture-mean readout (Eq. 14), the key-norm term, and the prior that cancels it (Eq. 16, with Eqs. 20–21) all appear here for point queries and keys. The manuscript's comparison scores Gaussian query and key states instead. Companion paper: [[gabbur-2021-probabilistic-attention]]. See [[GL(K) gauge-equivariant attention]] and [[Attention mechanisms — theory and positional structure]].

## Local full text

The arXiv v3 PDF is stored at `sources/pdfs/Movellan2020ProbabilisticTransformers.pdf` ([local PDF](../pdfs/Movellan2020ProbabilisticTransformers.pdf)). Source: [arXiv:2010.15583](https://arxiv.org/pdf/2010.15583). SHA-256: `89dce1a325888ca42205e656c2128f9f696a34c28bf4c54a33bf05e95a9f9b1c`.

## BibTeX

```bibtex
@misc{Movellan2020ProbabilisticTransformers,
  author = {Movellan, Javier R. and Gabbur, Prasad},
  title = {Probabilistic Transformers},
  year = {2020},
  howpublished = {arXiv preprint arXiv:2010.15583},
  eprint = {2010.15583},
  archivePrefix = {arXiv}
}
```
