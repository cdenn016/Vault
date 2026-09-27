---
type: reference
title: "Neural Mechanics: Symmetry and Broken Conservation Laws in Deep Learning Dynamics"
aliases:
  - "Kunin et al. 2021"
  - "Neural Mechanics: Symmetry and Broken Conservation Laws in Deep Learning Dynamics"
  - "Kunin2021NeuralMechanics"
authors:
  - Daniel Kunin
  - Javier Sagastuy-Brena
  - Surya Ganguli
  - Daniel L. K. Yamins
  - Hidenori Tanaka
year: 2021
arxiv: "2012.04728"
url: https://arxiv.org/abs/2012.04728
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/cs-ml
  - field/physics
created: 2026-09-23
updated: 2026-09-23
---

# Neural Mechanics: Symmetry and Broken Conservation Laws in Deep Learning Dynamics

> [!info] Citation
> Daniel Kunin, Javier Sagastuy-Brena, Surya Ganguli, Daniel L. K. Yamins, Hidenori Tanaka (2021). "Neural Mechanics: Symmetry and Broken Conservation Laws in Deep Learning Dynamics." *International Conference on Learning Representations* (ICLR 2021). Preprint: [arXiv:2012.04728](https://arxiv.org/abs/2012.04728) (v2 read).

## TL;DR

Continuous symmetries of a network's loss, which hold for any dataset, constrain its gradients and Hessians and imply Noether-like conservation laws under gradient flow. Weight decay, momentum, stochastic batches, and finite learning rates break these laws, and the resulting dynamics of the formerly conserved quantities can be solved exactly and match training of VGG-16 on Tiny ImageNet.

## What it establishes

Section 3 identifies three families of differentiable symmetries and the constraints they impose on gradients and Hessians. Translation symmetry arises, for example, from softmax logits, scale symmetry from normalization layers, and rescale symmetry from homogeneous activations. Section 4 (Theorem 1) proves that every differentiable symmetry of the loss satisfying the stated condition yields a conservation law of gradient flow. The conserved quantities are the parameter sum for translation symmetry, the squared norm for scale symmetry, and the difference of squared norms for rescale symmetry, the last recovering the layer balance of [[du-2018-balanced-layers]]. Section 5 builds a more realistic continuous model of stochastic gradient descent that includes weight decay, momentum, stochasticity, and discretization (modified gradient flow). Section 6 shows that these effects break the conservation laws, solves the resulting ODEs for the formerly conserved combinations, and validates the solutions on VGG-16 with and without batch normalization.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript cites this paper, with [[du-2018-balanced-layers]], for the optimizer behavior of its comparison maps. The Gaussian comparison is unchanged under the cogredient redundancy $(S_Q,S_K)\mapsto(AS_Q,AS_K)$ with $A\in\mathrm{GL}(r_h)$, so gradient flow conserves $S_QS_Q^\top+S_KS_K^\top$. AdamW without weight decay ([[loshchilov-hutter-2019-adamw]]) drifted along this orbit in the reported run, which is why raw conditioning diagnostics of $S_Q,S_K$ depend on the basis while the routing costs do not. See [[Natural gradient]] and [[GL(K) gauge-equivariant attention]].

> [!note] Editorial: The conservation law is Theorem 1 applied to this symmetry. Invariance of the loss under $S\mapsto e^{tX}S$ for every $X\in\mathfrak{gl}(r_h)$ gives $(\nabla_{S_Q}\mathcal L)S_Q^\top+(\nabla_{S_K}\mathcal L)S_K^\top=0$. Under $\dot S=-\nabla_S\mathcal L$ the time derivative of $S_QS_Q^\top+S_KS_K^\top$ is minus this matrix plus its transpose, which vanishes. An adaptive optimizer does not follow $-\nabla\mathcal L$, so the quantity is not conserved under AdamW.

## Local full text

The arXiv v2 PDF is stored at `sources/pdfs/Kunin2021NeuralMechanics.pdf` ([local PDF](../pdfs/Kunin2021NeuralMechanics.pdf)). Source: [arXiv:2012.04728](https://arxiv.org/pdf/2012.04728). SHA-256: `ec7836816b083323abbcfed53414547e1ccc8e9e0a56a942fbea831c0a0655bc`.

## BibTeX

```bibtex
@inproceedings{Kunin2021NeuralMechanics,
  author = {Kunin, Daniel and Sagastuy-Brena, Javier and Ganguli, Surya and Yamins, Daniel L. K. and Tanaka, Hidenori},
  title = {Neural Mechanics: Symmetry and Broken Conservation Laws in Deep Learning Dynamics},
  booktitle = {International Conference on Learning Representations},
  year = {2021},
  eprint = {2012.04728},
  archivePrefix = {arXiv}
}
```
