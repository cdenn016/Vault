---
type: paper
title: "Predictive Coding: a Theoretical and Experimental Review"
aliases:
  - "Millidge 2021"
  - "PC Review 2021"
authors:
  - Millidge, Beren
  - Seth, Anil
  - Buckley, Christopher L.
year: 2021
arxiv: "2107.12979"
url: https://arxiv.org/abs/2107.12979
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/neuroscience
  - field/cs-ml
  - field/psychology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Predictive Coding: a Theoretical and Experimental Review

> [!info] Citation
> Millidge, Beren, Anil Seth, and Christopher L. Buckley (2021). "Predictive Coding: a Theoretical and Experimental Review." arXiv:2107.12979. [arxiv.org/abs/2107.12979](https://arxiv.org/abs/2107.12979)

## TL;DR

This review provides a comprehensive treatment of predictive coding (PC) — the theory that the brain minimizes prediction errors with respect to an internal generative model of the world — covering its mathematical foundations, neurobiologically plausible microcircuit implementations, and its deep connections to backpropagation and modern machine learning. The authors unify existing results (Rao & Ballard 1999, Friston's FEP line, the PC-as-backprop result) into a single coherent framework and systematically survey experimental evidence alongside theoretical developments. It serves as the primary reference-level survey of the field as of 2021–2022.

## Problem & setting

Predictive coding has developed across at least three largely separate literatures: (1) computational neuroscience, where it models cortical message passing as hierarchical prediction-error suppression; (2) theoretical neuroscience / the free-energy principle, where it is the inference algorithm underlying active inference; and (3) machine learning, where recent work showed it approximates or recovers backpropagation gradients under local plasticity rules. Prior to this review no single treatment spanned all three perspectives with both mathematical rigor and experimental grounding. The paper addresses that gap, targeting readers who want a self-contained entry into PC or a synthesis of the now-dispersed literature.

## Method

The review develops predictive coding from first principles: it begins with the generative model assumption (a hierarchical Gaussian latent-variable model), derives the variational free energy objective and the prediction-error update equations (the E-step inner loop), and connects the fixed-point conditions to classical Kalman filtering. It then presents the neurobiologically plausible microcircuit implementation (superficial pyramidal cells carry prediction errors; deep pyramidal cells carry predictions), reviews the relationship between precision-weighted prediction errors and the gain modulation observed in attention, and covers the PC-as-backprop result: at inference convergence, local error signals equal backprop gradients on the same computation graph. The survey then reviews PC models for perception, motor control, attention, and learning, and surveys experimental tests of each.

Key equations follow the standard PC form. For a Gaussian generative model with layers $\ell$, the free energy decomposes as a sum of precision-weighted squared prediction errors:

$$F = \sum_\ell \frac{1}{2} \varepsilon_\ell^\top \Pi_\ell \varepsilon_\ell - \frac{1}{2}\ln|\Pi_\ell|$$

where $\varepsilon_\ell = \mu_\ell - g_\ell(\mu_{\ell+1})$ is the prediction error at layer $\ell$ and $\Pi_\ell$ is the precision (inverse covariance). Minimizing $F$ with respect to activities $\mu_\ell$ yields the prediction-error propagation equations; minimizing with respect to generative model parameters yields Hebbian-like weight updates.

## Key results

The review establishes the following contributions and syntheses. The mathematical framework is spelled out in full generality, clarifying when PC reduces to Kalman filtering (linear generative model, Gaussian noise) and what breaks under nonlinearity. The connection between PC and the free-energy principle is made precise: PC is the inference (E-step) half of variational EM under a hierarchical Gaussian generative model. The PC-as-backprop result (from Millidge et al. 2020 and related work) is presented as a theorem with explicit conditions. Precision weighting is shown to implement a form of learned attention in the cortical hierarchy, providing a mechanistic link between Bayesian inference and attentional gain control. The review surveys motor control under active inference (descending precision-weighted predictions driving proprioceptive prediction-error minimization) and discusses evidence for PC in V1 surround suppression, mismatch negativity, and attentional modulation of gain. On the ML side it covers PC networks as a biologically plausible alternative to backprop, including training convergence results and benchmarks.

## Relevance to this research

The VFE transformer is, at its mathematical core, a PC network operating on token sequences: each layer maintains Gaussian beliefs $(\mu, \Sigma)$ and iterates an E-step that minimizes the layer-local free energy $F$ (self-coupling $\alpha \cdot \mathrm{KL}(q_i \| p_i)$ plus belief-coupling terms). This review is the canonical reference for:

- The **E-step inference loop** as prediction-error minimization, supplying the neurobiological and theoretical motivation for the VFE-transformer's inner iteration and its convergence properties.
- **Precision weighting as attention**: the manuscript GL(K)_attention.tex derives gauge-equivariant attention weights $\beta_{ij}$ as precision-weighted prediction errors under the belief-coupling KL; this review is the theoretical provenance for that identification.
- **PC-as-backprop** (referencing Millidge et al. 2020 for details): confirms that the E-step/M-step training loop of the VFE transformer is gradient-consistent with end-to-end backprop, removing any doubt that local free-energy minimization sacrifices gradient fidelity.
- **Hierarchical generative models** (h → s → p → q hierarchy in the VFE manuscripts): the review's treatment of multi-level PC networks is the direct theoretical template for the hyper-prior and model-prior levels in the VFE free-energy functional.
- The multi-agent extension (MAgent_Model) interprets each agent as running an independent PC inference loop coupled through the belief-coupling KL and meta-entropy terms; this review's treatment of autonomous PC agents provides theoretical grounding.

## Cross-links

- Concepts: [[Variational free energy]], [[Prediction error]], [[Precision weighting]], [[Predictive processing and controlled hallucination]], [[Evidence lower bound (ELBO)]]
- Methods: [[Predictive coding network]], [[Free-energy principle active inference]], [[Variational EM]]
- Related sources: [[rao-1999-predictive-coding]], [[friston-2010-free-energy-principle]], [[millidge-2020-pc-approximates-backprop]], [[bogacz-2017-free-energy-tutorial]], [[friston-2017-active-inference-process-theory|friston-2017-active-inference-process]], [[buckley-2017-fep-mathematical-review]]
- Theme: [[Variational free energy and predictive coding]]
- Manuscript/Project: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model]], [[gl-k-attention|Attention as Gauge-Theoretic Variational Inference]]

## BibTeX

```bibtex
@article{millidge2021predictive,
  author        = {Millidge, Beren and Seth, Anil and Buckley, Christopher L.},
  title         = {Predictive Coding: a Theoretical and Experimental Review},
  journal       = {arXiv preprint arXiv:2107.12979},
  year          = {2021},
  eprint        = {2107.12979},
  archivePrefix = {arXiv},
  primaryClass  = {cs.NE},
  url           = {https://arxiv.org/abs/2107.12979}
}
```
