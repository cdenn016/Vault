---
type: paper
title: "Matrix Capsules with EM Routing"
aliases:
  - Hinton 2018
  - hinton2018matrix
  - EM routing
authors:
  - Hinton, Geoffrey E.
  - Sabour, Sara
  - Frosst, Nicholas
year: 2018
url: https://openreview.net/forum?id=HJWLfGWRb
pdf: sources/pdfs/hinton-2018-matrix-capsules-em-routing.pdf
tags:
  - cluster/multi-agent
  - cluster/attention
  - project/multi-agent
  - project/transformer
  - field/cs-ml
created: 2026-10-24
---

# Matrix Capsules with EM Routing

> [!info] Citation
> Hinton, G. E., Sabour, S., & Frosst, N. (2018). *Matrix capsules with EM routing*. International Conference on Learning Representations (ICLR 2018). PDF from the author's Toronto page.

## TL;DR
Each capsule has a presence probability and a $4\times4$ pose matrix. A lower capsule votes for each higher capsule's pose through a learned transformation, and the assignment of lower capsules to higher ones is computed per image by a few iterations of EM for a Gaussian mixture: higher capsules are Gaussian clusters whose means, variances and activations are refit to the weighted votes.

## Method
Section 3 frames routing as fitting a mixture of Gaussians to votes $V_{ij}$. The M-step sets each parent's mean and variance to the assignment-weighted moments of its votes; the parent's activation is a logistic function, scaled by an inverse temperature $\lambda$ that increases with a fixed schedule, of the description-length saving between explaining the votes and paying a fixed cost (costs $\beta_u,\beta_a$). The E-step reassigns each child to the parents in proportion to activation times Gaussian density. The transformation matrices are trained by backpropagation through the unrolled EM iterations. The paper reports a 45% reduction in test errors on smallNORB relative to the previous state of the art and better resistance to white-box adversarial attacks than a CNN baseline.

## Relevance to this research
This is the closest published precedent for the meta-agent reading of a Gaussian template layer. Parents are Gaussians fit by an EM M-step to their children's weighted contributions (bottom-up), and children are assigned by Bayesian responsibility (top-down); both directions run inside the forward pass. In [[Meta-agents and hierarchical emergence]] the parent is the forward-KL barycenter of its constituents, and the EM M-step of a Gaussian component with retained dispersion is that barycenter. The capsule activation test is a description-length criterion, parallel to the meta-agent licensing criterion.

## Cross-links
- Concepts: [[Meta-agents and hierarchical emergence]]
- Methods: [[Template routing]]
- Related sources: [[locatello-2020-slot-attention]], [[bovy-2011-extreme-deconvolution]]

## BibTeX
```bibtex
@inproceedings{hinton2018matrix,
  author    = {Hinton, Geoffrey E. and Sabour, Sara and Frosst, Nicholas},
  title     = {Matrix Capsules with {EM} Routing},
  booktitle = {International Conference on Learning Representations},
  year      = {2018},
  url       = {https://openreview.net/forum?id=HJWLfGWRb}
}
```
